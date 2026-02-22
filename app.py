"""Monolith — Structural English Visualizer PoC"""
import os, json, re
from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

API_KEY_PATH = os.path.expanduser("~/.config/google/gemini_api_key")
with open(API_KEY_PATH) as f:
    API_KEY = f.read().strip()

client = genai.Client(api_key=API_KEY)

PARSE_PROMPT = """You are a structural English sentence parser with Japanese translation. Analyze the given English sentence(s) and return JSON.

RULES:
1. Break into sentences. Each sentence gets: "text" (original), "ja" (Japanese translation), "blocks" (structure array)
2. Each block has: "role", and either "text"+"ja"+"words" (leaf) or "children" (nested)
3. Roles: S (subject), V (verb), O (object), C (complement), M (modifier), CONJ (conjunction), REL (relative clause), SUB (subordinate clause)
4. "words" is an array of {"en":"word","ja":"contextual translation"} for each word in "text"
5. Nested blocks (with "children") also need "ja" (translation of the whole clause)
6. Keep original text exactly as-is
7. Return ONLY valid JSON, no markdown fences
8. IMPORTANT: Decompose as deeply as possible. NEVER leave long phrases as a single flat text block. Always split:
   - Relative clauses (who/which/that) → REL with children containing SVO
   - Subordinate clauses → SUB with children
   - Prepositional phrases (by/at/in/on/of/for/with/from/into/through...) → separate M blocks
   - Appositive phrases (", a mathematics don") → separate M block
   - Compound modifiers → separate blocks
   Example: "an 1865 English children's novel by Lewis Carroll, a mathematics don at the University of Oxford" should become:
   O("an 1865 English children's novel"), M("by Lewis Carroll"), M(", a mathematics don at the University of Oxford")
   Each leaf block should be SHORT — ideally under 6 words. If longer, find a way to split further.

OUTPUT FORMAT:
{"sentences":[{"text":"...","ja":"...","blocks":[...]}]}

EXAMPLE:
Input: "The cat sat on the mat"
Output:
{"sentences":[{"text":"The cat sat on the mat","ja":"猫がマットの上に座った","blocks":[{"role":"S","text":"The cat","ja":"猫が","words":[{"en":"The","ja":"その"},{"en":"cat","ja":"猫"}]},{"role":"V","text":"sat","ja":"座った","words":[{"en":"sat","ja":"座った"}]},{"role":"M","text":"on the mat","ja":"マットの上に","words":[{"en":"on","ja":"〜の上に"},{"en":"the","ja":"その"},{"en":"mat","ja":"マット"}]}]}]}

EXAMPLE:
Input: "I think that she knows what he said"
Output:
{"sentences":[{"text":"I think that she knows what he said","ja":"彼女が彼の言ったことを知っていると私は思う","blocks":[{"role":"S","text":"I","ja":"私は","words":[{"en":"I","ja":"私は"}]},{"role":"V","text":"think","ja":"思う","words":[{"en":"think","ja":"思う"}]},{"role":"SUB","ja":"〜ということを","children":[{"role":"CONJ","text":"that","ja":"〜ということ","words":[{"en":"that","ja":"〜ということ"}]},{"role":"S","text":"she","ja":"彼女が","words":[{"en":"she","ja":"彼女が"}]},{"role":"V","text":"knows","ja":"知っている","words":[{"en":"knows","ja":"知っている"}]},{"role":"SUB","ja":"〜を","children":[{"role":"CONJ","text":"what","ja":"何を","words":[{"en":"what","ja":"何を"}]},{"role":"S","text":"he","ja":"彼が","words":[{"en":"he","ja":"彼が"}]},{"role":"V","text":"said","ja":"言った","words":[{"en":"said","ja":"言った"}]}]}]}]}]}

Parse this:
"""

@app.route("/")
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

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=PARSE_PROMPT + sentence,
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8793, debug=False)
