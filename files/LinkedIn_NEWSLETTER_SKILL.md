---
name: linkedin-newsletter-writer
description: Write long-form LinkedIn Newsletter issues (LinkedIn "Pulse" articles) for Kapil's "The .NET Horizon" newsletter. Use this skill when the user asks to write a newsletter issue, a LinkedIn article, or a deep-dive/long-form piece on an AI/ML/GenAI or .NET architecture topic — as opposed to a short feed post (see LinkedIn_SKILL.md for that). Distinguish by request shape: "write a post about X" → short post. "Write the next newsletter issue about X" / "write an article about X" / "draft Issue #N" → this skill.
---

# The .NET Horizon — Newsletter Writer

"The .NET Horizon" is Kapil's LinkedIn Newsletter (857+ subscribers at last count). It publishes long-form, chaptered deep dives on AI/ML engineering topics, written for .NET/backend engineers who are shipping real AI features, not reading AI news. This is a distinct format from short feed posts: longer, more systematic, less personal-anecdote, more reference-grade.

Real published issues so far (most recent first):
1. **Context Engineering** (Aug 7, 2026) — "Your AI Is Only as Smart as the Context You Give It." 20 chapters, teases Issue #11 on Model Context Protocol.
2. **AI Reliability Engineering** (Jul 28, 2026) — "When the Model Says the Wrong Thing. Or Nothing At All."
3. **AI Cost Engineering — The Bill Arrives. Are You Ready?** (Jul 21, 2026)
4. **AI Guardrails: Building AI Systems You Can Actually Trust** (Jul 13, 2026) — opens referencing OWASP 2025 Prompt Injection (LLM01).
5. **You've Built AI Features. Now Build AI Systems That Think for Themselves.** (Jul 6, 2026) — agentic systems, references Microsoft Agent Framework reaching Release Candidate.

Cadence: roughly weekly. Each issue is a self-contained deep dive on one AI-systems-engineering discipline (context, cost, reliability, guardrails/security, agentic architecture), written with the same rigor .NET engineers already apply to latency, reliability, and security.

---

## Voice (Newsletter, Distinct From Short Posts)

This is NOT the same voice as short feed posts (see LinkedIn_SKILL.md). Differences:

- **Third-person-plural, systems-thinking voice**, not first-person war stories. "Teams that ship an LLM-backed feature eventually have the same meeting" — not "I shipped a feature and here's what I learned." Kapil writes as a domain authority documenting a discipline, not a narrator recounting his own incident.
- **No hashtags in the article body.** LinkedIn articles don't carry hashtags the way feed posts do.
- **No emoji**, except an occasional industry-update marker like "📢 INDUSTRY UPDATE" as a section label.
- **Longer, denser paragraphs are acceptable and expected.** This is not phone-scroll feed copy — readers who click into a newsletter are committing to a deep read. Paragraphs run 3-6 sentences.
- Still direct, still names tradeoffs honestly, still avoids AI-hype vocabulary (see banned lists in LinkedIn_SKILL.md — those apply here too).
- Still opens with a sharp, concrete scenario, not a throat-clearing intro — same instinct as the short-post hook rules, just executed as a paragraph instead of two lines.

---

## Structure

### Title + Hook Line
A punchy, often provocative title, immediately followed by a one-line hook that reframes the topic as a stake, not a definition:
- "Context Engineering" → "Your AI Is Only as Smart as the Context You Give It."
- "AI Reliability Engineering" → "When the Model Says the Wrong Thing. Or Nothing At All."
- "AI Cost Engineering" → "The Bill Arrives. Are You Ready?" (folded into the title itself)

### Opening (1-3 paragraphs)
Names a concrete, universally recognizable failure scenario ("someone from finance asks why last month's cloud bill jumped, and nobody in the room can say which feature... caused it"), then states the core thesis reframe in one crisp sentence: this is a design gap, not a tooling gap; the model is rarely the bottleneck, the pipeline is. This thesis sentence is the spine the whole issue argues from.

### Body: Two Valid Section Formats

**Format A — Chaptered (used for dense, multi-concept issues like Context Engineering):**

Each chapter follows this exact rotation:
```
CHAPTER N — TITLE IN CAPS

Production scenario: [a specific, concrete vignette — a team, a symptom, a number]

Engineering discussion: [the underlying mechanism or concept, explained plainly]

Tradeoffs: [the honest cost/benefit — nothing is free]

Common mistakes: [a specific, real antipattern teams fall into]

Best practices: [actionable guidance]

Enterprise recommendation: [a directive, often with a concrete .NET-specific angle]
```
Between chapters, a short 2-5 word diagram/image caption on its own line signals where a visual belongs (e.g. "Naive RAG vs Production RAG", "Semantic Search + Hybrid Retrieval", "Context Compression Pipeline"). Suggest these captions even when no image will actually be attached — they mark natural visual-companion points.

**Format B — Essay/Section (used for issues built around one sustained argument, like AI Cost Engineering):**

ALL-CAPS section headers (no chapter numbers), each followed by 2-5 flowing paragraphs that build one sub-argument to completion before moving to the next section. Still covers scenario → mechanism → tradeoff → mistake → practice, just woven into prose rather than labeled fields. Still gets an occasional diagram caption between sections (e.g. "Token Economics", "Multi-Model Routing", "Runtime Budget Enforcement").

Pick Format A when the topic naturally decomposes into 10+ discrete techniques/concepts (good for a reference-style issue). Pick Format B when the topic is one sustained argument with 6-10 major sections (good for a narrative/persuasive issue). Ask Kapil if unclear, or default to Format B for shorter requested issues and Format A for comprehensive/definitive ones.

### Closing: Checklist + Final Takeaways (always present, in both formats)

**[TOPIC] CHECKLIST** or **PRODUCTION CHECKLIST** — a bulleted list of verifiable, concrete yes/no questions or imperative items a team can literally check off before shipping. Examples of the real pattern:
- "Is retrieval hybrid (semantic + keyword), not vector-only?"
- "Is there a re-ranking step before final assembly?"
- "Cost instrumentation is emitted at call time, tagged with feature, owner, and model, not reconstructed later from provider invoices."

**FINAL TAKEAWAYS** — 2-4 paragraphs that restate the opening thesis in sharper, more quotable language, and close with a punchy final line with real rhythm. Real examples:
- "The model is rarely the bottleneck. The pipeline that decides what the model sees is."
- "The bill arrives either way. Whether it's a surprise is entirely up to how the system was built."

Optionally tease the next issue's topic in one sentence at the very end ("Next issue, we go deep on Model Context Protocol...").

---

## Writing Rules (Newsletter-Specific)

1. Open with a concrete, recognizable scenario — a meeting, a symptom, a specific number — never an abstract definition of the topic.
2. State the core thesis as one crisp, quotable sentence early. Everything after should argue for it.
3. Use "teams," "engineers," "a platform team," "a support assistant" as the actors — not "I." This is documentation of a discipline, not a personal story.
4. Every technique gets its tradeoff named explicitly. Never present a technique as a free win. This mirrors the short-post rule ("none of these options are free") but applied at essay length.
5. Every major section should be groundable in something concrete: a real number, a real architecture decision, a real failure mode. Avoid abstract AI-philosophy paragraphs with no engineering content.
6. No hashtags. No emoji except an occasional bracketed label like "📢 INDUSTRY UPDATE" if the issue opens with real news.
7. Close every issue with a checklist and a "Final Takeaways" section. Never skip these — they are the save-worthy, shareable payload of the issue.
8. Suggest diagram/visual captions between major sections, matching the style of real captions (2-5 words, naming a concept or comparison, not a full sentence).
9. If the issue is part of an ongoing numbered series (Kapil has referenced "Issue #11" internally), ask Kapil for the issue number, or leave a placeholder like "[Issue #N]" rather than guessing.
10. Avoid every word on the banned/AI-hype vocabulary lists in LinkedIn_SKILL.md — the newsletter is read by engineers evaluating whether to trust the source; hype language undercuts that immediately.
11. Length: real issues run long, easily 1,800-3,000+ words for a Format A chaptered issue, 1,200-2,000 for a Format B essay issue. Don't pad, but don't artificially shorten a topic that needs the space — this is the one format in Kapil's system where LinkedIn's short-attention-span post rules don't apply.

---

## Output Format

Return the full article text ready to paste into a LinkedIn Newsletter draft. Use the section headers as shown above (CHAPTER N — TITLE, or ALL-CAPS section headers). Include diagram-caption placeholder lines where a visual belongs. After the article, add a brief note:
- Word count
- Format used (A: Chaptered / B: Essay)
- Which of the 4 content pillars this supports (should almost always be Pillar 3: AI/ML Engineering & GenAI Systems, sometimes crossing into Pillar 1/2 for .NET-specific angles)
- Suggested next-issue teaser topic, if a natural one exists
- List of diagram/visual placeholders included, for Kapil to design separately

---

## Known Newsletter Facts (keep updated)

- Newsletter name: **The .NET Horizon**
- Subscriber count as of last check: 857
- Cadence: roughly weekly (issues observed on Jul 6, Jul 13, Jul 21, Jul 28, Aug 7, 2026)
- Internally numbered (references to "Issue #11" exist) — ask Kapil for the current issue number when drafting a new one, don't assume
- Topics covered so far: agentic systems/AI agent architecture, AI guardrails/prompt injection security, AI cost engineering, AI reliability engineering, context engineering (RAG, chunking, retrieval, caching, memory, multi-agent context, MCP preview)
- Natural next topics (from the Context Engineering teaser and general gaps): Model Context Protocol deep dive, evals/testing for LLM features, fine-tuning vs. RAG vs. prompting decision framework, observability for AI systems
