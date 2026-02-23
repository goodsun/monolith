"""Monolith — Structural English Visualizer PoC"""
import os, json, re
from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

API_KEY_PATH = os.path.expanduser("~/.config/google/gemini_api_key")
with open(API_KEY_PATH) as f:
    API_KEY = f.read().strip()

client = genai.Client(api_key=API_KEY)

LEVEL_INSTRUCTIONS = {
    "beginner": """TRANSLATION LEVEL: Beginner
- Use simple, short sentences (SVO structure)
- Avoid relative clauses, subordinate clauses, and complex nesting
- Use common everyday vocabulary (CEFR A1-A2)
- Maximum 1 sentence, under 10 words
- Example: "I like cats." / "She goes to school."
""",
    "intermediate": """TRANSLATION LEVEL: Intermediate
- Use natural, common expressions and idioms
- Allow moderate complexity: one level of nesting (e.g., one relative clause or subordinate clause)
- Use common collocations and phrasal verbs (CEFR B1-B2)
- 1-2 sentences, 10-20 words each
- Example: "I think she knows the answer." / "The book that I read was interesting."
""",
    "advanced": """TRANSLATION LEVEL: Advanced
- Use complex, sophisticated sentence structures
- Include multiple levels of nesting: relative clauses, subordinate clauses, participial phrases
- Use academic/literary vocabulary and complex constructions (CEFR C1-C2)
- Allow long, multi-clause sentences
- Example: "The theory, which had been proposed by researchers who studied the phenomenon for decades, was finally validated."
""",
}

PARSE_PROMPT_BASE = """You are a structural English sentence parser with Japanese translation.

{translate_instruction}

{level_instruction}

Analyze the English sentence(s) and return JSON.

RULES:
1. Break into sentences. Each sentence gets: "text" (original English), "ja" (Japanese translation), "blocks" (structure array){source_field}
2. Each block has: "role", and either "text"+"ja"+"words" (leaf) or "children" (nested)
3. Roles: S (subject), V (verb), O (object), C (complement), M (modifier), CONJ (conjunction), REL (relative clause), SUB (subordinate clause)
4. "words" is an array of {{"en":"word","ja":"contextual translation"}} for each word in "text"
5. Nested blocks (with "children") also need "ja" (translation of the whole clause)
6. Keep original text exactly as-is
7. Return ONLY valid JSON, no markdown fences
8. IMPORTANT: Decompose as deeply as possible. NEVER leave long phrases as a single flat text block. Always split:
   - Relative clauses (who/which/that) → REL with children containing SVO
   - Subordinate clauses → SUB with children
   - Prepositional phrases (by/at/in/on/of/for/with/from/into/through...) → separate M blocks
   - Appositive phrases (", a mathematics don") → separate M block
   - Compound modifiers → separate blocks
   Each leaf block should be SHORT — ideally under 6 words. If longer, find a way to split further.

OUTPUT FORMAT:
{{"sentences":[{{"text":"...","ja":"...","blocks":[...]}}]}}

Parse this:
"""

def build_prompt(sentence, level="intermediate", translate=False):
    if translate:
        translate_instruction = (
            "The input is NOT in English. First translate it into natural English "
            f"at the specified level, then parse the English translation. "
            f"Include \"source\" field in each sentence with the original input text."
        )
        source_field = '\n   Also include "source" (the original non-English input) in each sentence object'
    else:
        translate_instruction = "The input is in English. Parse it directly."
        source_field = ""

    level_instruction = LEVEL_INSTRUCTIONS.get(level, LEVEL_INSTRUCTIONS["intermediate"])

    return PARSE_PROMPT_BASE.format(
        translate_instruction=translate_instruction,
        level_instruction=level_instruction,
        source_field=source_field,
    )

@app.route("/")
def landing():
    return render_template("lp.html")

@app.route("/app")
def index():
    return render_template("index.html")

@app.route("/api/parse", methods=["POST"])
def parse():
    data = request.json
    sentence = data.get("sentence", "").strip()
    if not sentence:
        return jsonify({"error": "No sentence provided"}), 400

    # Sanitize: keep only printable text
    sentence = re.sub(r'[^\x20-\x7E\u00A0-\uFFFF]', ' ', sentence).strip()
    if not sentence:
        return jsonify({"error": "No valid text after sanitization"}), 400

    level = data.get("level", "intermediate")
    if level not in LEVEL_INSTRUCTIONS:
        level = "intermediate"

    # Detect non-English input (contains CJK, Cyrillic, Arabic, etc.)
    import unicodedata
    non_latin_count = sum(1 for c in sentence if unicodedata.category(c).startswith('Lo'))
    translate = non_latin_count > len(sentence) * 0.1

    prompt = build_prompt(sentence, level=level, translate=translate)

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt + sentence,
        )
        raw = response.text.strip()
        # Strip markdown fences if present
        raw = re.sub(r'^```json\s*', '', raw)
        raw = re.sub(r'\s*```\s*$', '', raw)
        parsed = json.loads(raw)

        # Normalize response format
        if isinstance(parsed, dict) and "sentences" in parsed:
            return jsonify(parsed)
        elif isinstance(parsed, list):
            return jsonify({"sentences": [{"text": sentence, "blocks": parsed}]})
        else:
            return jsonify({"sentences": [{"text": sentence, "blocks": parsed}]})
    except json.JSONDecodeError:
        return jsonify({"error": "AI response was not valid JSON. Please try again."}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "").strip()
    context = data.get("context", "")  # JSON string of current parse result
    history = data.get("history", [])   # [{role, text}, ...]

    if not message:
        return jsonify({"error": "No message"}), 400

    system = """You are a friendly English tutor inside "Monolith", a structural English visualizer.
The user is looking at a color-coded structural breakdown of an English sentence.
Your job is to explain WHY the sentence has that structure, explain grammar concepts
in simple terms (avoid jargon — use colors and spatial metaphors when possible),
give usage examples, and answer any questions about the sentence.

Reply in Japanese (the user is a Japanese learner of English).
Keep answers concise but insightful — 2-4 short paragraphs max.
Use the parse context below to understand what the user is looking at.

CURRENT PARSE CONTEXT:
""" + (context or "(no parse yet)")

    contents = []
    for h in history[-10:]:  # keep last 10 turns
        role = "user" if h.get("role") == "user" else "model"
        contents.append({"role": role, "parts": [{"text": h["text"]}]})
    contents.append({"role": "user", "parts": [{"text": message}]})

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=contents,
            config={"system_instruction": system},
        )
        return jsonify({"reply": response.text.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8793, debug=False)
