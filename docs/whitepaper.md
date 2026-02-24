# Monolith: Visual Structure Grounding for Grammar-Free Language Learning

**Perceptual Scaffolding Inspired by Symbol Emergence Systems**

---

**Authors:** Chikara Kawashima¹, Teddy (AI Assistant)¹  
**Affiliation:** ¹ bon-soleil  
**Date:** February 2026  
**Version:** 1.0  

---

## Abstract

We present Monolith, a web-based tool that visualizes English sentence structure using color-coded nested blocks without any grammar terminology. Traditional language education relies on metalinguistic labels (e.g., "subject," "relative pronoun") to explain structure—a multi-step indirect reference process that conflicts with the cognitive strengths of visual-spatial learners. Drawing on Symbol Emergence Systems theory (Taniguchi, 2016), Monolith replaces this label-mediated approach with direct visual grounding: syntactic roles are mapped to colors, and hierarchical clause nesting is rendered as block containment. AI (Gemini) handles parsing; the learner simply *experiences* the structure. We argue that this draws inspiration from Symbol Emergence Systems theory to create perceptual scaffolding, and that embracing the non-idempotent nature of natural language—rather than forcing a single "correct" parse—leads to more authentic language understanding.

**Keywords:** Symbol Emergence, Visual Structure Grounding, Grammar-Free Learning, Non-Idempotent Natural Language, Cognitive Adaptation, AGI-era Education

---

## 1. Introduction

### 1.1 The Structural Gap

When Japanese speakers learn English, the fundamental challenge is not vocabulary but *structural architecture*. Japanese employs SOV word order with postpositional particles, constructing meaning "from inside out." English uses SVO with positional grammar, expanding "from outside in":

```
Japanese: 「彼が言ったことを彼女が知っていると私は思う」
           ←←←←←←←←← inner to outer

English:  "I think that she knows what he said"
           →→→→→→→→→ outer to inner
```

Learning English is not substituting words—it is reconstructing the blueprint of thought itself.

### 1.2 The Grammar Terminology Trap

Conventional English education explains structure through grammar terminology: "subject," "relative pronoun," "participial construction." This approach demands *explaining symbols with other symbols*—a multi-step indirect reference chain:

1. Memorize grammar terms in Japanese
2. Map terms to English structural elements
3. When reading English, recall the relevant term
4. Apply the term's definition to understand structure

This process is cognitively expensive and particularly ill-suited for learners with strong visual-spatial processing ability, who would benefit more from direct perceptual pattern recognition.

### 1.3 Contribution

Monolith eliminates the grammar terminology layer entirely, replacing it with a visual encoding system based on color and spatial nesting. Our key contributions are:

1. **A grammar-free visualization system** mapping syntactic roles to colors and clause hierarchy to block nesting
2. **Educational framework inspired by symbol emergence theory** creating perceptual scaffolding for structural understanding
3. **Honest treatment of linguistic non-idempotency** as a pedagogical feature rather than a defect
4. **AI-powered parsing** that removes the prerequisite of grammar knowledge from structural understanding

### 1.4 Research Hypotheses

**H1 (Visual Grounding):** Color-coded structural visualization enables faster structural pattern recognition than grammar-terminology-based instruction for learners with strong visual-spatial cognitive preference.

**H2 (Non-Idempotency Awareness):** Exposing learners to multiple valid parses of the same sentence promotes deeper structural understanding compared to single-parse instruction.

**H3 (Grammar-Free Acquisition):** Learners can acquire functional structural intuition (measured by sentence construction accuracy) without explicit grammar terminology instruction, through sustained interaction with Monolith's visual representations.

---

## 2. Related Work

### 2.1 Traditional Grammar Instruction

Traditional methods (Grammar-Translation, Structural Approach) rely on explicit rule teaching and metalinguistic terminology. While effective for analytical learners, these methods create cognitive overhead for visual-spatial thinkers and often fail to produce intuitive structural understanding (Krashen, 1982).

### 2.2 Visual Approaches to Language

Sentence diagrams (Reed-Kellogg) and parse trees (Chomsky) provide visual representations but remain tightly coupled to grammar terminology. Learners must first understand the labeling system before benefiting from the visualization.

### 2.3 Symbol Emergence Systems

Taniguchi (2016) proposes that symbols (including language) emerge through bodily interaction with the environment rather than being assigned top-down. This framework connects to the broader tradition of Embodied Cognition (Varela et al., 1991), which argues that cognition is fundamentally grounded in bodily experience rather than abstract symbol manipulation. The Enactive Approach suggests that understanding emerges through direct interaction with the environment—a principle that bridges SES theory and educational design.

This theoretical lineage connects directly to Gibson's (1979) concept of **affordances**—the possibilities for action that objects or environments provide to an organism based on their physical properties and the organism's capabilities. In Monolith, the color-coded blocks function as structural affordances: they offer perceptual cues that *afford* specific patterns of understanding without requiring explicit grammatical explanation. Blue blocks afford "agent" recognition not through definitional teaching but through consistent perceptual association. This represents a shift from descriptive grammar (telling learners what structures "are") to affordance-based design (creating environments where understanding can emerge through direct perceptual engagement).

Monolith draws inspiration from this lineage: where SES demonstrates how symbols emerge from embodied interaction with the environment, and Embodied Cognition shows that knowledge is rooted in physical experience, Monolith translates these insights into language education by converting abstract linguistic structures into visual-spatial experiences—transforming grammar from symbol-to-symbol mapping into direct perceptual engagement.

### 2.4 Cognitive Profiles and Learning

Cognitive assessments reveal that individuals with strong visual-spatial processing abilities process information most efficiently through visual-spatial channels. Learners whose visual-spatial ability significantly exceeds their verbal reasoning would find color-pattern recognition far more natural than terminology memorization (Wechsler, 2008).

---

## 3. System Design

### 3.1 Color as Syntax

Monolith maps syntactic roles to colors:

| Color | Role | Description | Traditional Term |
|-------|------|-------------|-----------------|
| Blue 🔵 | S | Agent of action | Subject |
| Red 🔴 | V | The action itself | Verb |
| Yellow 🟡 | O | Target of action | Object |
| Green 🟢 | C | Equivalence (A = B) | Complement |
| Purple 🟣 | M | Additional info (when, where, how) | Modifier |
| Orange 🟠 | REL | Describes a noun from behind | Relative Clause |
| Teal 🩵 | SUB | A sentence within a sentence | Subordinate Clause |
| Gray ⚪ | CONJ | Connective glue | Conjunction |

Learners need not memorize any labels. Color patterns, observed repeatedly, form structural recognition naturally—analogous to how children acquire native language structure without studying grammar.

#### 3.1.1 The Three Primary Colors of Language

The three core roles—Subject (Blue), Verb (Red), Object (Yellow)—correspond to the subtractive primary colors universally known from childhood art education. This is not accidental.

When Red (Verb) functions as an action, Yellow (Object) receives the impact: *He kicked **the ball***. Blue and Yellow remain distinct—agent and target.

But when Red becomes "=" (the copula), something remarkable occurs. The element to the right of "=" refers to the same entity as the Subject. Blue (Subject) and Yellow (the position where Object would be) are no longer distinct—they point to the same thing. They harmonize. And in subtractive color mixing, **blue and yellow combine to produce green.**

This is why the Complement is green: it is not a primary color that exists independently, but an emergent color born from the harmony of Subject and Object through the mediating "=" of the Verb. The balance icon (⚖️) represents this equilibrium—the moment when left and right sides of the equation find balance and blend.

```
He kicked the ball.     → Blue  Red  Yellow  (action → target stays yellow)
The sky is blue.        → Blue  Red  Green   (= → harmony produces green)
```

Every learner who has mixed blue and yellow paint in elementary school art class carries this knowledge in their body. No explanation is needed. The color itself teaches.

This resonates with the Japanese philosophical principle *"wa wo motte tōtoshi to nasu"* (和をもって尊しとなす)—"harmony is to be valued above all." A language learning tool born in Japan explains the complement through harmony: the balancing of subject and predicate into a new, unified color.

#### 3.1.2 The Color Wheel as Syntactic Map

The eight colors of Monolith are not arbitrary assignments—they are systematically positioned on the color wheel, encoding syntactic relationships through chromatic relationships.

**Primary colors** form the sentence skeleton:

| Color | Role | Function |
|-------|------|----------|
| Blue 🔵 | S (Subject) | The agent—who acts |
| Red 🔴 | V (Verb) | The action—what happens |
| Yellow 🟡 | O (Object) | The target—what is acted upon |

**Secondary colors** are mixtures of primaries, and each mixture reflects a genuine syntactic relationship:

- **Green (C = Complement) = Blue + Yellow.** The complement refers to the same entity as the subject. Blue (subject) harmonizes with Yellow (object position) through the equalizing verb, producing Green. (§3.1.1)
- **Purple (M = Modifier) = Red + Blue.** Modifiers add information that touches both the verb (when/how the action happens) and the subject (what the agent is like). The color that mixes action and agency.
- **Orange (REL = Relative Clause) = Red + Yellow.** A relative clause contains a verb (Red) and references a noun (Yellow), but its subject is backgrounded—left behind in the main clause. "The book *that I bought*": what matters is the buying (Red) and the book (Yellow); the buyer (Blue) recedes. Orange is the color of **action and target with the agent left behind**.

**Tertiary color:**

- **Teal (SUB = Subordinate Clause) = Blue + Green.** A subordinate clause is a self-contained sentence: it has its own subject (Blue) and its internal structure has already achieved harmony (Green = SV completion). Independence (Blue) plus harmony (Green) yields Teal—a clause that is complete in itself yet subordinate to another.

**Achromatic:**

- **Gray (CONJ = Conjunction).** Conjunctions carry no meaning of their own. They merely connect. The absence of color *is* the meaning: a colorless link between colored elements.

This chromatic architecture means that the visual relationships between colors on screen mirror the structural relationships between syntactic roles. A learner need not be told that relative clauses contain verb-like elements—they can *see* that Orange sits between Red and Yellow on the color wheel.

### 3.2 Nesting as Hierarchy

English complexity largely stems from clause embedding. Monolith renders this as block containment:

```
┌─ Blue [I] ─┐ ┌─ Red [think] ─┐ ┌─────── Teal ──────────────────┐
│             │ │               │ │ Gray[that] Blue[she] Red[knows]│
│             │ │               │ │  ┌─── Teal ──────────┐        │
│             │ │               │ │  │ Gray[what] Blue[he]│        │
│             │ │               │ │  │ Red[said]          │        │
│             │ │               │ │  └────────────────────┘        │
└─────────────┘ └───────────────┘ └────────────────────────────────┘
```

For engineers, this is instantly recognizable: code indentation, DOM trees, directory structures. English sentence structure operates on the same principle.

### 3.3 Two-Mode Interface

Monolith provides two viewing modes, toggled by the Shift key:

- **Normal mode:** Colors only. No labels, no icons. Pure visual pattern. The monolith speaks without words.
- **Shift mode:** Role icons appear, word-level translations become accessible, legend switches to Japanese descriptions. A hint layer for deeper exploration.

This design follows the "subtraction" philosophy: start with minimal information, add detail only when actively sought.

### 3.4 Interaction Design

| Action | Normal Mode | Shift Mode |
|--------|-------------|------------|
| Hover | Block-level Japanese translation | Word-level contextual translation |
| Click | Speak the entire block (TTS) | Speak individual word (TTS) |

This dual-granularity interaction allows learners to move between holistic understanding (block-level) and detailed analysis (word-level) fluidly.

### 3.5 Multi-Language Input

Monolith accepts input in any language, not just English. When non-English text is detected (via Unicode character analysis), the AI first translates the input to English at the appropriate level, then parses the result. This enables:

- Japanese speakers to input thoughts in Japanese and see the English structural equivalent
- Cross-linguistic structural comparison (how a Japanese idea restructures in English)
- Zero-barrier entry for absolute beginners who cannot yet compose English sentences

### 3.6 Level Adaptation

Three difficulty levels adapt the output to the learner's proficiency:

| Level | CEFR | Characteristics |
|-------|------|----------------|
| Beginner | A1-A2 | Short SVO sentences, <10 words, basic vocabulary |
| Intermediate | B1-B2 | Natural idioms, compound sentences, everyday complexity |
| Advanced | C1-C2 | Nested clauses, academic vocabulary, complex subordination |

When combined with multi-language input, this creates a powerful workflow: a learner inputs a complex thought in Japanese, selects "Beginner," and sees a simple English structural pattern; switching to "Advanced" reveals how the same thought expands into nested complexity.

### 3.7 ◻ Tutor: AI Structural Guide

An integrated chat widget (the "◻ Tutor") provides contextual structural explanation in Japanese. After parsing a sentence, the learner can ask the Tutor questions about the resulting structure:

- "Why is this block purple?"
- "What does the nesting mean here?"
- "How would this sentence change if I moved this part?"

The Tutor has access to the current parse result and explains structure using Monolith's visual language (colors and blocks) rather than grammar terminology—maintaining the grammar-free philosophy even in natural language explanation.

### 3.8 Detailed Explanation Mode

An optional `explain` flag triggers per-sentence structural explanation directly in the parse response. When enabled, the AI appends a 2-3 sentence Japanese explanation to each parsed sentence covering:

- What sentence pattern/structure is used (e.g., SVO, passive, there-construction)
- Notable nesting or clause relationships
- Why this structure works and what nuance it conveys

Crucially, explanations use Monolith's own visual language rather than grammar terminology—e.g., *"赤ブロック(動詞)の後に緑の入れ子(従属節)が続く構造"* instead of *"主節の述語動詞に従属節が後続する"*. This keeps even the metalevel discourse within the grammar-free philosophy.

### 3.9 AI as Parser

The parsing engine uses Google Gemini 2.0 Flash via a single API call that simultaneously produces:
- Syntactic structure (roles + nesting)
- Block-level Japanese translation
- Word-level contextual translation

This design means **zero grammar knowledge is prerequisite**. The AI performs the expert analysis; the human experiences the result.

---

## 4. Theoretical Foundation

### 4.1 Symbol Grounding Through Vision

The Symbol Grounding Problem (Harnad, 1990) asks how symbols connect to real-world meaning. Traditional language education creates a *symbol-to-symbol mapping*: English symbols are explained via Japanese grammar symbols. True "grounding" rarely occurs.

Monolith introduces a new symbol system (colors + blocks + nesting) that leverages bodily experience (visual-spatial cognition) to ground English structural meaning directly:

```
Traditional:  English → Grammar Terms (Japanese) → Understanding
              [symbol]    [symbol]                  [meaning]

Monolith:     English → Color/Block Pattern → Understanding
              [symbol]    [embodied perception]    [meaning]
```

By bypassing the metalinguistic intermediate layer, Monolith enables what we term **Visual Structure Grounding**—direct perceptual access to syntactic meaning.

### 4.2 Symbol Emergence as Inspiration

Monolith does not implement symbol emergence itself but rather translates the core insight from SES theory—that direct perceptual experience enables understanding—into educational practice. Where SES demonstrates symbols emerging from embodied interaction, Monolith creates structured perceptual experiences that facilitate pattern recognition:

1. Providing repeated exposure to color patterns across diverse sentences
2. Allowing the structural "meaning" of each color to emerge naturally through experience
3. Never explicitly teaching what each color "means" in grammatical terms

The learner's understanding of "blue = the thing doing the action" emerges from seeing blue consistently associated with agents across hundreds of sentences—not from reading a definition. This represents an application of the SES-inspired principle that understanding develops through direct perceptual engagement rather than symbolic explanation.

### 4.3 Cognitive Adaptation

For learners with strong visual-spatial cognitive preference, Monolith aligns the learning channel with cognitive strengths:

- ❌ Grammar term memorization → linguistic processing (verbal reasoning dependent)
- ✓ Color-block pattern recognition → visual processing (visual-spatial ability leveraged)

This represents a form of Universal Design in language education: providing a visual-first channel that complements the traditional verbal-first approach.

---

## 5. Intrinsic Motivation and Personalized Learning

### 5.1 Desire-Driven Learning

Monolith accepts any English text as input. This design choice carries profound pedagogical implications beyond mere convenience.

When learners analyze sentences from their favorite novels, films, news articles, or academic papers, **intrinsic motivation** drives the learning process. The desire to understand beloved content creates a learning engine far more powerful and sustainable than extrinsic rewards (grades, test scores).

We align this with the concept of **Desire-Driven Development (BDD)**—originally coined for software development, but equally applicable to education: let the learner's authentic interests, curiosities, and obsessions fuel the learning process.

### 5.2 Deep Semantic Grounding

When learners bring their own texts, they bring background knowledge and emotional connection. The visual structure overlay doesn't exist in isolation—it maps onto meaning the learner already cares about. This strengthens the symbol grounding process: structural patterns are not abstract exercises but tools for accessing desired meaning.

### 5.3 Infinite Personalization

Every learner gets a different curriculum—their own. A programmer visualizes API documentation. A literature student visualizes Shakespeare. A researcher visualizes paper abstracts. The tool is constant; the content is infinitely variable.

This is the antithesis of mass-produced education: **AGI-era personalized learning at zero marginal cost**.

---

## 6. Non-Idempotent Natural Language

### 6.1 The Idempotency Assumption

Programming languages are idempotent: the same code always produces the same result. Traditional grammar education implicitly assumes natural language shares this property—that every sentence has one "correct" parse.

Formally, we can define this distinction:

```
Let f: S → T be a parsing function mapping sentence s ∈ S to parse tree t ∈ T.

In programming languages:    f(s) = f(s)    (idempotent — deterministic)
In natural language with AI: f(s) ≠ f(s)    (non-idempotent — stochastic)
```

Natural language is fundamentally non-idempotent:

```
"I saw the man with the telescope"
→ I used a telescope to see the man (with modifies saw)
→ I saw a man who had a telescope (with modifies man)
```

Both parses are grammatically valid. Context determines meaning—and sometimes context is insufficient.

This reveals a fundamental paradigm shift from **deterministic to probabilistic language education**. Traditional grammar instruction operates deterministically: each sentence has one "correct" analysis, students memorize rules, and deviation from the canonical parse is marked as error. Monolith embraces a probabilistic approach: multiple valid interpretations coexist, structural understanding develops through pattern recognition across variations, and ambiguity becomes a pedagogical resource rather than a problem to eliminate. This shift reflects the broader transition from rule-based to statistical approaches in AGI-era language processing.

This non-idempotency extends beyond structural ambiguity. While structural ambiguity represents static properties of language (a sentence having multiple valid interpretations), non-idempotency in AI-powered parsing introduces dynamic stochastic elements—the same input may yield different results due to the parser's temperature parameters and sampling processes. Monolith treats both dimensions honestly: the inherent ambiguity of natural language and the additional variance introduced by AI parsing.

### 6.2 Embracing Ambiguity

When the same sentence is input to Monolith multiple times, the AI may produce different structural analyses. This is not a bug—it is a feature that reveals a fundamental truth about language.

Traditional education would consider this a failure. Monolith treats it as a learning opportunity: the learner confronts the fact that **linguistic interpretation is not unique**, and learns to identify structural patterns within ambiguity rather than memorizing a single "correct" answer.

### 6.3 Honesty Toward Language

> *"Natural language has no idempotency. Until you stand at this point, you cannot face language with honesty."*

Monolith's design philosophy embraces this principle. It does not pretend to deliver the one true parse. It delivers *a* parse—one possible structural reading among potentially several. The learner develops structural intuition not by memorizing answers but by experiencing patterns across many interpretations.

This is the most honest stance toward natural language as a non-idempotent symbol system.

---

## 7. The Name: Monolith

The name references the monolith from Kubrick's *2001: A Space Odyssey*—a black slab that transforms those who encounter it without speaking a word.

Monolith (the tool) follows the same philosophy: **to convey without speaking**. No grammar terms. No explanations. Just colors and blocks that, through repeated encounter, transform the learner's structural perception.

Additionally, "monolith" literally means "single block"—precisely the atomic unit of the tool's visual language.

The dark theme is intentional: colored blocks floating on black, like the monolith's radiance against the void, or constellations against the night sky. Darkness heightens color perception and structural contrast.

---

## 8. Implementation

### 8.1 Architecture

- **Frontend:** Single-page HTML/CSS/JavaScript
- **Backend:** Flask (Python)
- **AI Engine:** Google Gemini 2.0 Flash (single API call)
- **TTS:** Web Speech API (client-side)
- **Hosting:** Apache reverse proxy → Flask on port 8793

### 8.2 API Design

A single endpoint `/api/parse` accepts English text and returns structured JSON:

```json
{
  "sentences": [{
    "text": "I think that she knows what he said.",
    "ja": "彼女は彼が言ったことを知っていると私は思う。",
    "blocks": [
      {"role": "S", "text": "I", "ja": "私は",
       "words": [{"en": "I", "ja": "私"}]},
      {"role": "V", "text": "think", "ja": "思う",
       "words": [{"en": "think", "ja": "思う"}]},
      {"role": "SUB", "ja": "〜ということ", "children": [
        {"role": "CONJ", "text": "that", ...},
        {"role": "S", "text": "she", ...},
        {"role": "V", "text": "knows", ...},
        {"role": "SUB", "ja": "彼が言ったこと", "children": [...]}
      ]}
    ]
  }]
}
```

The single-call design minimizes latency and ensures translation consistency between block-level and word-level Japanese.

### 8.3 Prompt Engineering

The parsing prompt enforces deep decomposition:
- Relative clauses → separate REL blocks with full SVO children
- Prepositional phrases → separate M blocks
- Appositives → separate M blocks
- Subordinate clauses → SUB blocks with recursive structure

This maximizes the visual information density and ensures complex sentences reveal their true nested structure.

---

## 9. Evaluation Design

### 9.1 Proposed Experiment

We propose a controlled study comparing three groups:

| Group | Method | Duration |
|-------|--------|----------|
| A (Control) | Traditional grammar instruction | 4 weeks |
| B (Monolith) | Color-block visualization only | 4 weeks |
| C (Hybrid) | Grammar instruction + Monolith | 4 weeks |

**Metrics:**
- Structural comprehension accuracy (sentence structure identification tasks)
- Processing speed (time to identify clause boundaries)
- Retention (1-month follow-up test)
- Subjective engagement (questionnaire)

### 9.2 Cognitive Profile Correlation

For each participant, cognitive assessments measuring visual-spatial processing and verbal reasoning abilities would be collected as optional supplementary measures (e.g., WAIS-IV subscores or approximated via shorter instruments) to analyze:

- Does strong visual-spatial cognitive preference predict greater benefit from Monolith?
- Does the gap between visual-spatial and verbal abilities predict preference for visual vs. verbal instruction?
- Is there a threshold visual-spatial ability above which Monolith becomes decisively more effective?

### 9.3 Non-Idempotency Study

A secondary study would present the same ambiguous sentences multiple times and analyze:

- Do learners notice parse variations?
- Does awareness of ambiguity improve after extended Monolith use?
- How does ambiguity awareness correlate with reading comprehension?

---

## 10. Discussion

### 10.1 Limitations

- **AI parsing reliability:** Gemini occasionally produces inconsistent or incorrect parses. For educational purposes, this is partially mitigated by the non-idempotency philosophy, but grossly wrong parses could mislead beginners.
- **Visual accessibility:** Color-dependent encoding excludes color-blind users. Future work should explore shape-based or texture-based alternatives.
- **Japanese-specific design:** Current translations and descriptions target Japanese speakers. Adaptation to other L1 backgrounds requires localization of the conceptual framing.
- **No empirical validation yet:** The theoretical framework is sound, but controlled experiments have not been conducted.

### 10.2 AGI-Era Implications

As AI language capabilities advance, the question "why learn English at all?" becomes increasingly valid. Our answer:

**Understanding language structure is acquiring a new cognitive frame.**

The ability to think in different structural paradigms—SOV vs. SVO, head-initial vs. head-final—provides perspectives that AI translation cannot replicate. This is not about replacing AI but about expanding human cognition alongside it.

Monolith embodies a division of labor: **AI analyzes, humans experience.** The expert knowledge (parsing) is delegated to AI; the human focuses on perception, pattern recognition, and meaning-making.

### 10.3 Beyond English

While designed for English learning by Japanese speakers, the color-block approach is language-agnostic in principle. Any language with identifiable syntactic roles can be visualized. Future work could explore:

- Japanese structure visualization for English speakers
- Mandarin structure visualization
- Cross-linguistic structural comparison (visualizing the same meaning in multiple languages side by side)

---

## 11. Conclusion

Monolith demonstrates that grammar terminology is not a prerequisite for structural understanding. By replacing metalinguistic labels with color and spatial nesting, the tool provides a **visual-first pathway** to English structure that:

1. Eliminates the multi-step indirect reference of traditional grammar instruction
2. Leverages visual-spatial cognition for more natural pattern acquisition
3. Applies symbol emergence theory to create direct structure-meaning grounding
4. Treats linguistic ambiguity honestly as a feature of natural language
5. Enables intrinsic-motivation-driven, infinitely personalized learning

The tool's philosophy—**to convey without speaking**—extends from its interface design to its pedagogical approach. Just as the monolith transforms without explaining, Monolith teaches without lecturing.

> *"Natural language has no idempotency. Until you stand at this point, you cannot face language with honesty."*

---

## References

1. Gibson, J. J. (1979). *The Ecological Approach to Visual Perception*. Houghton Mifflin.
2. Harnad, S. (1990). The Symbol Grounding Problem. *Physica D*, 42(1-3), 335-346.
3. Kawashima, C., & Teddy. (2026). Monolith — Structural English Visualizer. GitHub. https://github.com/goodsun/monolith
4. Krashen, S. (1982). *Principles and Practice in Second Language Acquisition*. Pergamon Press.
5. Kubrick, S. (Director). (1968). *2001: A Space Odyssey* [Film]. Metro-Goldwyn-Mayer.
6. Taniguchi, T. (2016). *Symbol Emergence in Robotics*. Springer.
7. Varela, F. J., Thompson, E., & Rosch, E. (1991). *The Embodied Mind: Cognitive Science and Human Experience*. MIT Press.
8. Wechsler, D. (2008). *Wechsler Adult Intelligence Scale—Fourth Edition (WAIS-IV)*. Pearson.

---

## Appendix A: Color Psychology

The color assignments are not arbitrary:

- **Blue (Subject):** Stability, presence—the foundation on which the sentence rests
- **Red (Verb):** Energy, action—the heartbeat of the sentence
- **Yellow (Object):** Illumination, clarity—the target made visible
- **Green (Complement):** Harmony—the emergent color when Blue (Subject) and Yellow (Object position) blend through the equalizing Red. Not a primary color, but born from balance (see §3.1.1)
- **Purple (Modifier):** Richness—additional layers of meaning
- **Orange (Relative):** Warmth, connection—linking back to enrich nouns
- **Teal (Subordinate):** Depth—a world within a world
- **Gray (Conjunction):** Neutrality—the invisible glue

These associations are intended to be subliminal rather than explicit, reinforcing structural intuition through chromatic affect.

## Appendix B: Live Demo

A live instance is available at: https://monolith.bon-soleil.com/

Source code: https://github.com/goodsun/monolith
