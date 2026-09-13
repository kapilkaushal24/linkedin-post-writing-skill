# Suggested Memory Seeds for LinkedIn Content

## Recent High Performers
- "20 Essential .NET Interview Questions" post: 335 likes, 21 comments. Best performer so far. Numbered checklist + carousel visual. Lean into this format.
- "5 Common ASP.NET Core Performance Issues" post: 23 likes, 10 comments, sparked an EF Core vs Dapper debate in comments. Myth-bust + numbered list format works.
- "CancellationToken" post: 52 likes, 12 comments, sparked real technical pushback/debate. Confident single-concept myth-busts perform well.

## The .NET Horizon Newsletter (Pillar 3)
Kapil publishes a weekly LinkedIn Newsletter called **The .NET Horizon** (857 subscribers as of last check). Long-form AI systems engineering deep dives, distinct voice/structure from short posts — see LinkedIn_NEWSLETTER_SKILL.md and LinkedIn_NEWSLETTER_EXAMPLES.md.

Published issues so far (most recent first):
- **Context Engineering** (Aug 7, 2026) — 14 likes, 2 comments. Full text captured in LinkedIn_NEWSLETTER_EXAMPLES.md. Teases Issue #11 on Model Context Protocol.
- **AI Reliability Engineering** (Jul 28, 2026) — 10 likes, 3 comments. "When the Model Says the Wrong Thing. Or Nothing At All." Full text not yet captured — paste in when available.
- **AI Cost Engineering — The Bill Arrives. Are You Ready?** (Jul 21, 2026) — 10 likes. Full text captured in LinkedIn_NEWSLETTER_EXAMPLES.md.
- **AI Guardrails: Building AI Systems You Can Actually Trust** (Jul 13, 2026) — 6 likes. Opens on OWASP 2025 Prompt Injection (LLM01). Full text not yet captured.
- **You've Built AI Features. Now Build AI Systems That Think for Themselves.** (Jul 6, 2026) — 7 likes, 1 comment. References Microsoft Agent Framework (MAF) reaching Release Candidate. Full text not yet captured.

Next natural topic: Model Context Protocol (explicitly teased at the end of the Context Engineering issue).

## Voice Corrections
[Add corrections as you use the project. Examples:]
- "Don't use the word 'journey'. I never say that."
- "I prefer statement/scene hooks over question hooks."
- "Keep the code snippet short, don't pad it with comments."

## Week of September 13, 2026 — Planned Content
Drafted and saved to disk (see CONTENT_CALENDAR_RULES.md for the folder convention):
- `posts/September/13/post.md` — bonus Sunday post, "agentic AI vs backend fundamentals" (contrarian, Pillar 1+3 crossover)
- `posts/September/15/post.md` — Tuesday, "does async/await create a thread" myth-bust (Pillar 1)
- `posts/September/16/post.md` — Wednesday, "AI agent memory" myth-bust (Pillar 3)
- `posts/September/17/post.md` — Thursday, "AKS readiness vs liveness probes" myth-bust (Pillar 2)
- `newsletters/September/14/newsletter.md` — Monday, The .NET Horizon issue on Model Context Protocol (fulfills the teaser from the "Context Engineering" issue)

Update this section after each week's planning session so it reflects only the current/upcoming week; move anything published to "Recent High Performers" once engagement numbers are known.

## Content Backlog
[No external backlog tool connected yet. Track post ideas directly in this file, or set one up in Notion/a spreadsheet if you want the weekly planning workflow in linkedin-weekly-system.md.]

Ideas to consider (.NET / Cloud):
- Async/await internals (state machine, thread pool, common misconceptions)
- DI lifetimes: Singleton vs Scoped vs Transient, with a production gotcha
- gRPC vs REST: when the 45% latency win actually matters
- Dockerizing a .NET service: the 45-min-to-8-min story
- What "serving notice period" job searching in .NET actually looks like in 2026

Ideas to consider (AI/ML/GenAI):
- Why a RAG pipeline returns confident wrong answers (retrieval vs. generation failure)
- What actually breaks when you put an AI agent in a production workflow
- Prompt engineering vs. context engineering: where the real leverage is
- The real cost curve of an LLM feature at scale (token cost, retries, context bloat)
- What "AI reliability" means when the model is non-deterministic
- Using Claude Code day-to-day as a .NET engineer: what it actually replaces vs. what it doesn't
- A grounded take on an AGI headline: what changes for a working backend engineer, what doesn't
