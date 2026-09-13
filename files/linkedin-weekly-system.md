# Kapil's Weekly LinkedIn Content System

## How It Works

One planning touchpoint, then write on demand. No external backlog tool required — this file and MEMORY_SEEDS.md track ideas and history directly.

This system covers two distinct deliverables:
- **Short feed posts** (LinkedIn_SKILL.md) — frequent, short, phone-readable.
- **The .NET Horizon newsletter issues** (LinkedIn_NEWSLETTER_SKILL.md) — roughly weekly, long-form AI systems engineering deep dives. Don't conflate the two: a newsletter issue is not just a longer post, it's a different voice and structure.

Drafted posts and issues get saved to disk as dated files under `posts/<Month>/<Day>/post.md` and `newsletters/<Month>/<Day>/newsletter.md`. See `CONTENT_CALENDAR_RULES.md` in the project root for the exact convention and file format. Always save after drafting, don't just leave it in the chat.

---

## PLANNING: Pick the Week's Topics (~10 min)

**You say:** "Plan my week" or "what should I post about"

**I will:**

1. Pull open ideas from the "Content Backlog" section of `LinkedIn MEMORY_SEEDS to paste.md`
2. Propose 1-3 posts, mixing pillars:

| Slot | Post Type | Funnel |
|---|---|---|
| **Primary** | Numbered checklist or production war story | Education (save-driven) |
| **Secondary** | Myth-bust / contrarian technical take | Awareness or Education |
| **Occasional** | Interview prep / career transparency | Education or Conversion |

3. For each proposed post, I'll show:
   - Topic
   - Content Pillar (1 .NET Performance / 2 Cloud-Native & DevOps / 3 AI/ML & GenAI / 4 Career & Interview Prep)
   - Post Type
   - Funnel position
   - Key angle / hook direction
   - Whether it needs input from you (a real bug, a real number, a code snippet)

4. You approve, swap, or adjust.

**Monthly balance check:** Roughly aim for:
- Most posts (60-70%) as education/checklist/war-story posts (Pillar 1, 2, or 3)
- A regular mix of .NET/cloud posts (Pillars 1-2) and AI/ML posts (Pillar 3), don't let one crowd out the other
- 1-2 career/interview posts per month (Pillar 4)
- No more than 1 pure job-search/conversion post per month

---

## WRITING: Draft a Post (~10 min)

**You say:** "Write a post about [X]" or just describe what happened

**I will:**

1. Pick the best post type for the input (see Post Types in LinkedIn_SKILL.md)
2. Draft the full post, ready to copy-paste
3. Run the AI Detection Layer before delivering (vocabulary scan → structure scan → tone scan → formatting scan → read-aloud test). See LinkedIn_SKILL.md and anti-ai-writing-guide.md for the full checklist.
4. Include metadata: char count, post type, pillar, funnel, save potential, visual suggestion
5. You review, tweak if needed, then post

**After publishing:** Tell me the engagement numbers if you want them logged. I'll add strong performers to `LinkedIn MEMORY_SEEDS to paste.md` under "Recent High Performers."

---

## Quality Gate: Anti-AI Check

Every post goes through this before delivery. No exceptions.

1. **Vocabulary:** No words from the banned list or the extended banned vocabulary in LinkedIn_SKILL.md. No AI transition words (Furthermore, Moreover, Additionally).
2. **Structure:** No generic intro. No summary closing. Start with the hook (redirect blame, scene, or confident claim), end with a specific question.
3. **Tone:** Post states the technical mechanism plainly. If it feels like it's hedging on every point, sharpen it.
4. **Formatting:** No dense paragraphs. → arrows or numbered lists, not markdown bullets. Code snippets where they help.
5. **Specificity:** Vague phrases replaced with real numbers, timeframes, technical detail.
6. **Read-aloud:** If a phrase sounds like a textbook, rewrite it.

Full framework with side-by-side examples: anti-ai-writing-guide.md

---

## Trigger Phrases

| You say | I do |
|---|---|
| "Plan my week" / "what should I post about" | Propose 1-3 topics from the backlog, mixed across pillars |
| "Write a post about [X]" | Immediate draft (skip planning) |
| "Turn this bug into a post" / paste a war story | Draft a production war story post |
| "Monthly review" | Look back at recent posts (from MEMORY_SEEDS) and check pillar/funnel balance |
| "Add [idea] to backlog" | Add an entry to the Content Backlog section of MEMORY_SEEDS.md |
| "Write the next newsletter issue about [X]" / "draft an article about [X]" | Draft a full The .NET Horizon issue using LinkedIn_NEWSLETTER_SKILL.md, not the short-post rules |

---

## Project Files Reference

| File | Purpose |
|---|---|
| **LinkedIn_SKILL.md** | Full writing guidelines for short posts: voice profile, banned words, post types, algorithm strategy, pre-publish checklist |
| **LinkedIn_NEWSLETTER_SKILL.md** | Writing guidelines for The .NET Horizon newsletter issues: distinct voice, chaptered/essay structure, checklist + takeaways format |
| **LinkedIn_POST_EXAMPLES.md** | Real post examples for voice calibration, voice patterns to notice |
| **LinkedIn_NEWSLETTER_EXAMPLES.md** | Real newsletter issue excerpts for voice calibration |
| **linkedin-weekly-system.md** | This file. Weekly workflow, triggers, content mix rules |
| **anti-ai-writing-guide.md** | Comprehensive guide for detecting and eliminating AI-sounding patterns. Covers vocabulary (40+ banned words with replacements), structure, tone, punctuation, openings/closings, content patterns, editing checklist. Applies to both formats. |

---

## Optional: Connecting a Real Backlog Tool

If you start tracking post ideas in Notion, a spreadsheet, or a task tool, update the "WRITING" and "PLANNING" sections above to pull from it instead of the MEMORY_SEEDS.md backlog, and tell Claude where it lives so it can be referenced going forward.
