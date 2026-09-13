# LinkedIn Post Writing Skill for Claude AI

A complete system for writing LinkedIn posts that sound like a real person, not AI. Adapted from an open-source template, customized for my own voice.

## What This Is

6 files that turn Claude (or any LLM) into a LinkedIn ghostwriter that actually sounds like me, across two formats: short feed posts and long-form newsletter issues. The system includes voice calibration, anti-AI detection, content strategy, algorithm optimization, and a weekly publishing workflow.

I use this system to write LinkedIn posts and newsletter issues about .NET, ASP.NET Core, Azure/cloud-native backend engineering, and AI/ML/GenAI (RAG, agents, AI cost and reliability engineering). I also publish "The .NET Horizon," a weekly LinkedIn Newsletter with long-form deep dives on AI systems engineering. Every post and issue goes through an AI detection checklist before publishing.

## The Files

### Skill Files (upload these to your AI project)

| File | What It Does |
|---|---|
| `files/LinkedIn_SKILL.md` | Core writing guidelines for short feed **posts**. Voice profile, banned words (40+), post types, 2026 algorithm strategy, pre-publish checklist. |
| `files/LinkedIn_NEWSLETTER_SKILL.md` | Writing guidelines for long-form **newsletter issues** ("The .NET Horizon" on LinkedIn). Different voice, chaptered/essay structure, checklist + takeaways format. Use for "write a newsletter issue" / "write an article", not for short posts. |
| `files/anti-ai-writing-guide.md` | How to NOT sound like AI. 8-part guide covering vocabulary, structure, tone, formatting, openings/closings, and content patterns. Includes side-by-side rewrites. Applies to both posts and newsletter issues. |
| `files/LinkedIn_POST_EXAMPLES.md` | Real short-post examples for voice calibration. Annotated with what makes each one work. |
| `files/LinkedIn_NEWSLETTER_EXAMPLES.md` | Real newsletter issue excerpts for voice calibration (distinct, more formal voice than short posts). |
| `files/linkedin-weekly-system.md` | Weekly content workflow. Planning and writing sessions, content backlog, content mix rules. |

### Setup Files (for configuring Claude Projects)

| File | What It Does |
|---|---|
| `SETUP_GUIDE.md` | Step-by-step guide to build your own LinkedIn writing skill from scratch. Written for beginners. |
| `LinkedIn PROJECT_INSTRUCTIONS to paste.md` | Project instructions to paste into your Claude Project's system prompt. Defines triggers, formatting rules, and behavior. |
| `LinkedIn MEMORY_SEEDS to paste.md` | Suggested memory entries for tracking story numbers, high-performing formats, and voice corrections. |

## How to Use It

### With Claude Projects
1. Create a new Claude Project
2. Upload the files from `files/` to the project's knowledge base (both the post skill and newsletter skill files)
3. Copy the contents of `LinkedIn PROJECT_INSTRUCTIONS to paste.md` into the project's custom instructions
4. Optionally seed your memory with entries from `LinkedIn MEMORY_SEEDS to paste.md`
5. Start writing posts

### With Claude Code (this folder)
Just ask Claude to write a post about a topic. It reads the skill files directly from this folder, no project setup needed.

### With Other LLMs
The files are plain markdown. You can paste them into any LLM's system prompt or context window. Start with `LinkedIn_SKILL.md` and `anti-ai-writing-guide.md` as the minimum setup.

## What Makes This Different

Most AI writing prompts focus on what to write. This system focuses on what NOT to write.

The anti-AI detection layer catches 40+ vocabulary tells, 10+ structural patterns, and 6 tone problems that make AI-generated content obvious to readers. Every post runs through a 6-step quality gate before delivery.

The system also includes 2026 LinkedIn algorithm signals (360 Brew), content funnel strategy, and framework branding guidelines.

## The Anti-AI Philosophy

Your readers have developed an internal AI detector. They can't always name what feels off, but they feel it. The text is too smooth. Too balanced. Too careful.

This system eliminates that "AI smell" by:
- Banning 40+ words that AI overuses (leverage, navigate, unlock, empower, delve...)
- Breaking AI's default structure (intro → balanced body → summary → optimistic close)
- Forcing specific details over vague generalizations
- Requiring a clear stance instead of "on the other hand" hedging
- Checking every post against a read-aloud test

Full breakdown in `anti-ai-writing-guide.md`.

## About

I'm [Kapil Kaushal](https://www.linkedin.com/in/kapilkaushal24/), a .NET Cloud AI Engineer based in Sahibzada Ajit Singh Nagar, Punjab, India. I build backend systems on Azure using ASP.NET Core, focused on microservices, containerization (Docker/AKS), and API/database performance. I also work with AI-assisted engineering (Claude, agent skills, prompt engineering) and write about applied AI/ML: RAG, GenAI systems, AI agents, and the AGI conversation. I post about .NET, ASP.NET Core, Azure/cloud-native backend engineering, and AI/ML/GenAI.

These files are the actual system I use to write my LinkedIn content.

## License

MIT. Use it, adapt it, share it.

## Connect

- LinkedIn: [kapilkaushal24](https://www.linkedin.com/in/kapilkaushal24/)
- Personal site: [kapilkaushal.netlify.app](https://kapilkaushal.netlify.app/)
