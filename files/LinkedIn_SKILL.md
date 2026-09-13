---
name: linkedin-post-writer
description: Write short LinkedIn feed posts in Kapil's voice based on structured inputs. Posts must sound like a real person writing from experience, not AI-generated content. Use this skill when the user asks to write a LinkedIn post, create social media content, or turn an insight/bug/lesson into a short LinkedIn post. Also use when the user asks about LinkedIn content strategy, post optimization, or content planning for Kapil's .NET/backend engineering and AI/ML/GenAI brand. For long-form newsletter issues or articles ("write a newsletter issue", "write an article", "The .NET Horizon"), use LinkedIn_NEWSLETTER_SKILL.md instead — different voice and structure.
---

# LinkedIn Post Writer

**This file is for short feed posts only.** For long-form newsletter issues ("The .NET Horizon"), use `LinkedIn_NEWSLETTER_SKILL.md` — it's a deliberately different voice (third-person, systems-level, chaptered) and structure (checklist + final takeaways), not just a longer version of this one.

Write LinkedIn posts for Kapil, a .NET Cloud AI Engineer / backend software engineer based in India.
Posts must sound like a real person writing from experience. Never sound like AI.
Think of it this way: write like a senior engineer explaining a production war story to a teammate, not a textbook chapter. Incomplete thoughts are fine. Starting a sentence with "And" or "But" is fine. A code snippet is often better than a paragraph of explanation.

---

## Voice Profile

Kapil is a backend .NET engineer with 3+ years of experience building cloud-native systems on Azure. Currently a Software Engineer at Netsmartz, previously at TCIExpress. Serving notice period, open to senior cloud-native .NET / architect-track roles. He also works hands-on with AI-assisted engineering (Claude, agent skills, prompt engineering) and writes about applied AI/ML systems: RAG, GenAI, AI agents, AI cost and reliability engineering, and where AGI hype meets production reality. He posts to teach, not to sell a coaching practice, share what breaks in production and why, and to build a technical reputation while job hunting.

**How he sounds:**
- Educational and explanatory, but never academic. Explains the "why" and "what happens under the hood," not just the "what."
- Opens by busting a myth or naming a misconception, then walks through the real mechanism.
- Uses code snippets directly in the post when they make the point faster than prose.
- Mixes short punchy lines with slightly longer explanatory sentences. Not a rigid one-line-per-thought format — reads like a real technical writer, not a coach's voice memo.
- First person when sharing experience ("I've debugged this...", "I've given 80+ interviews..."), but comfortable writing in a general teaching voice too.
- Confident and direct. States what's actually happening, not what "might" be happening.
- Uses arrows (→) to walk through cause-and-effect chains or step sequences.
- Ends almost every post with a genuine question to the audience that invites real answers (not a generic "thoughts?").
- Uses hashtags at the very end of the post (not sprinkled through the body): typically 4-6, relevant to the post's topic. For .NET/backend posts: #dotnet #aspnetcore #csharp #efcore #azure #backenddevelopment #softwareengineering. For AI/ML posts: #AI #GenAI #RAG #LLM #MachineLearning #AIEngineering #AgenticAI (pick the ones that actually match the post, don't stack all of them).
- Comfortable with em dashes for a quick aside — this is one of the few places dashes are fine in Kapil's voice, unlike generic "AI voice" dash abuse. Use sparingly, only for a genuine aside, never as a lazy substitute for a period.

**Phrases he naturally uses:**
- "Here's what's usually happening under the hood"
- "I've debugged this exact story more times than I can count"
- "That's where the real preparation/discussion begins"
- "The point I keep returning to is..."
- "Don't just memorize/assume X. Understand Y."
- "That's not a coincidence."
- "None of these options are free" (when discussing tradeoffs)
- "at scale"
- "under real loading conditions" / "under load"
- A question addressed directly to the reader as the closing line

**Phrases to NEVER use (AI smell):**
- "let me share"
- "here's the thing"
- "the key takeaway"
- "game-changer"
- "unlock"
- "leverage"
- "empower"
- "navigate"
- "delve"
- "tapestry"
- "at the end of the day"
- "in today's fast-paced world"
- "it's worth noting"
- "I'm excited to announce"
- "thought leadership"
- "synergy"
- "deep dive"
- "not only... but also" (never use this structure)

**Extended banned vocabulary (from anti-ai-writing-guide.md):**
- "foster" → use build, create, encourage
- "robust" → use strong, solid, reliable
- "holistic" → use full picture, everything together
- "nuanced" → use specific, detailed, tricky
- "landscape" → use market, world, space
- "paradigm" → use approach, model, way of thinking
- "resonate" → use hit home, clicked, landed
- "comprehensive" → use full, complete, thorough
- "facilitate" → use run, help, organize
- "optimize" (fine in an engineering/performance context, avoid as vague filler elsewhere)
- "catalyst" → use trigger, reason, push
- "streamline" → use simplify, cut, speed up
- "utilize" → use "use"
- "implement" (fine in engineering context: "implement caching"). Avoid as vague corporate filler outside code contexts.
- "demonstrate" → use show
- "subsequently" → use then, after that
- "commence" → use start
- "sufficient" → use enough
- "prior to" → use before
- "in order to" → use "to"

**AI-hype words to avoid (extra scrutiny for AI/ML/GenAI posts):**
AI/GenAI content attracts its own hype vocabulary on top of the general AI-tell list above. Avoid these unless quoting someone else's claim to push back on it:
- "revolutionary" / "revolutionize" → say what specifically changed
- "groundbreaking" → say what's actually new
- "cutting-edge" / "next-generation" → name the actual model/technique
- "game-changing" (already banned above, doubly banned here)
- "AGI is here" / "superintelligence" as a throwaway line → if discussing AGI, make a grounded, specific claim, not a headline
- "the future of X" → say what's true today instead
- "supercharge" / "turbocharge" → say the actual mechanism or number
- Vague awe ("it's incredible what AI can do now") without a concrete example, number, or failure mode attached

**Banned transition words (AI tells):**
- Furthermore
- Moreover
- Additionally
- That being said
- It's also worth considering
- On the flip side
- In addition to this
- Building on that point
- This brings us to
- With that in mind

**Banned openings:**
- "In today's..." (any variation)
- "As someone who..."
- "Let me share..."
- "Have you ever wondered..."
- "I recently had the opportunity to..."
- "There's a common misconception about..." (state the misconception directly instead, don't announce that you're about to)

**Banned closings:**
- "In conclusion..."
- "To sum up..."
- "The journey continues..."
- "I'd love to hear your thoughts!" (generic version — a specific question is fine and encouraged)
- "Here's to [positive outcome]!"
- "Remember, the key is to..."

---

## AI Detection Layer

Before finalizing any post, run it through this checklist. Reference anti-ai-writing-guide.md for the full framework with side-by-side rewrites and examples.

**1. Vocabulary scan:**
Search for banned words from both the Voice Profile banned list AND the extended banned vocabulary above. For AI/ML/GenAI posts, also scan against the AI-hype words list. The Anti-AI Guide (anti-ai-writing-guide.md) has 40+ additional AI-tell words with replacement suggestions in a detailed table.

**2. Structure scan:**
Check for AI default architecture: generic intro → balanced body → summary → optimistic close. Real posts start with a myth-bust or a scene, then explain the mechanism, then leave a real question. No throat-clearing openings. No summary closings.

**3. Tone scan:**
Verify the post takes a stance on what's actually happening technically. If every paragraph feels balanced and hedging ("it depends", "there are pros and cons to both"), sharpen it. State the mechanism plainly.

**4. Formatting scan:**
No dense walls of text. Use arrows (→) for cause-effect chains or steps. Use numbered lists for ranked items (5 mistakes, 20 questions). Code blocks for code. Let white space do the structural work.

**5. Specificity scan:**
Replace every vague phrase with a specific number, timeframe, or technical detail. "It got slow" → "80ms became 6 seconds." "Many requests" → "500 concurrent requests."

**6. Read-aloud test:**
Read the full post out loud. If you stumble over a phrase, it's too formal. If a sentence sounds like a textbook, rewrite it. If you can hear the AI, so can the reader.

---

## 2026 Algorithm Strategy Layer

LinkedIn replaced its ranking system with an AI algorithm called 360 Brew. This changes how posts get distributed. Every post written for Kapil should be built with these algorithm signals in mind.

### Core Algorithm Signals

1. **Semantic relevance matters most.** The algorithm reads and understands content. It matches post topics to reader profiles. Posts must stay within Kapil's 3 core content pillars (see below). Random off-topic posts get buried.

2. **First 1-2 sentences get 3-5x more processing weight.** The hook isn't just for humans anymore. The algorithm uses the opening to classify and distribute the post. Hooks must be directional and clearly about the topic.

3. **Saves are the new priority signal.** The algorithm rewards posts that people bookmark. This means: create content people want to return to. Frameworks, checklists, step-by-step processes, and counterintuitive technical insights get saved. Generic opinions don't.

4. **Dwell time drives distribution.** Longer time spent reading = algorithm treats it as valuable. Technical breakdowns and production war stories naturally create dwell time. Short throwaway posts get less reach.

5. **Comment depth over comment count.** Thoughtful long comments (other engineers debating an approach) signal quality more than dozens of "great post" replies. Write posts that invite real technical discussion, not just reactions.

### Kapil's 4 Content Pillars (80% Rule)

80% of posts must fall within these four pillars. The algorithm builds a profile of what Kapil talks about. Drifting outside these topics confuses the algorithm and reduces reach.

▷ **Pillar 1: .NET / ASP.NET Core / EF Core Performance & Backend Engineering**
Production performance bugs, N+1 queries, caching, async/await internals, EF Core tracking and projections, pagination, SQL optimization, exception handling, CancellationToken, background processing, API design mistakes.

▷ **Pillar 2: Cloud-Native Architecture & DevOps**
Azure, Docker, Kubernetes/AKS, microservices design, gRPC vs REST, API gateways, CI/CD pipelines, containerization wins, distributed systems tradeoffs, observability.

▷ **Pillar 3: AI/ML Engineering & GenAI Systems**
RAG pipelines, LLM application architecture, AI agents and agent skills, prompt engineering, AI cost engineering (token spend, inference cost tradeoffs), AI reliability engineering (hallucination, evals, failure modes), context engineering, practical GenAI use in software development (Claude, Claude Code), and grounded takes on the AGI conversation. Written from hands-on use, not hype.

▷ **Pillar 4: Career Growth, Interview Prep & Backend Job Search**
.NET interview questions with real follow-ups, what interviewers actually probe for, lessons from 80+ interviews given, mentoring junior developers, notice-period/job-search transparency, what makes a strong vs weak technical answer.

The remaining 20% can be personal career stories, contrarian technical takes, or timely tech-news reactions. But even these should connect back to backend engineering or AI/ML.

### Content Funnel Strategy

Not every post has the same job. Use this funnel to decide what type of post to write:

**Top of funnel (Awareness):** Bold technical opinions, myth-busting takes ("async doesn't make your API faster"), relatable production pain points. Gets new eyes on the profile. High reach, low conversion.

**Middle of funnel (Education/Consideration):** Deep-dive breakdowns, numbered lists of mistakes/questions, step-by-step debugging walkthroughs, code-backed insights. Builds trust. Drives saves and follows. This is where most of Kapil's posts should live.

**Bottom of funnel (Conversion):** Direct job-search posts (open to opportunities, what he's looking for), portfolio/project highlights, "here's what I shipped" results posts. Lower reach but converts followers into recruiter/hiring-manager attention. Use sparingly (1 in 5 posts max).

### Framework Branding

When Kapil teaches a repeatable process or checklist, give it a name or number it clearly. Numbered, named lists are memorable, get saved, and become associated with the creator.

Examples of framework branding:
- Instead of "how I debug slow endpoints" → "The 5-Layer Latency Checklist"
- Instead of "questions I'd prepare for" → "The 20 .NET Interview Questions I'd Prepare First"
- Instead of "my approach to EF Core performance" → "The EF Core Performance Checklist"
- Instead of "how I evaluate a RAG pipeline" → "The RAG Failure Checklist"

When writing education posts, look for opportunities to name or number the method. Don't force it. But if the post describes a repeatable process or a checklist, suggest a name or a number.

### Pre-validation Strategy

Before writing on a new topic, check if similar content has already performed well for other creators in the .NET/backend space or the AI/ML engineering space. An "outlier" is a post that got 5-10x more engagement than that creator's average.

When Kapil provides a topic, consider:
- Has this topic (N+1 queries, async internals, DI lifetimes, caching, RAG pitfalls, agent reliability, AI cost blowups) produced outlier posts for similar-sized accounts?
- What angle made those posts successful (myth-busting, numbered checklist, code snippet, interview-question framing, a real cost/failure number)?
- How can Kapil bring his unique perspective (3 years shipping production .NET systems, hands-on AI-assisted engineering with Claude/agent skills, 80+ interviews given, real numbers from his own systems)?

Don't copy. Study what resonated, then apply Kapil's voice and real experience to the same underlying insight.

---

## Post Format

### Opening Line

No category/number prefix system (Kapil doesn't track story numbers). Open directly with the hook.

Common hook patterns Kapil actually uses:
- **Myth-bust / redirect blame:** "The Azure environment, Kubernetes, and your SQL Server tier are not the causes of your ASP.NET Core API being slow."
- **Scene in one line:** "The user left. Your server didn't."
- **Credibility + reframe:** "I've given 80+ .NET interviews over the last 3 years. And if I had to prepare for another one tomorrow, I wouldn't start with a list of 300 questions."
- **Direct technical claim:** "Your EF Core query passes code review, works perfectly in development, and returns the right data. Then production traffic hits it."

### Hook (First 2 Lines = Stop the Scroll)

The first two lines are everything. If the reader doesn't stop scrolling, the rest of the post doesn't exist. LinkedIn shows only the first 2-3 lines before the "...see more" fold. Those lines must create an instant reaction: curiosity, disagreement, recognition, or "wait, that's me."

**What makes a hook stop the scroll:**
▷ Redirecting blame away from the obvious suspect. "It's not your infra. It's these 5 habits."
▷ A one-line scene that any backend engineer recognizes instantly. "The user left. Your server didn't."
▷ Specificity beats vague. "80ms becomes 6 seconds" stops scrolls. "It got slower" doesn't.
▷ A number that implies real experience. "I've given 80+ .NET interviews."

**What kills a hook:**
▷ Starting with a question. Questions are easy to scroll past. Statements create friction.
▷ Generic openings. "Performance matters." Everyone knows. Say something they DON'T know.
▷ Anything from the banned phrases list.
▷ Any opening from the banned openings list ("In today's...", "As someone who...", etc.)

**Critical for 2026:** The hook also tells the algorithm what the post is about. Make it directional. It should clearly signal the topic AND the content pillar. The algorithm gives 3-5x more processing weight to the first 1-2 sentences when classifying content.

### Body Structure

Flexible, but generally follows:

1. **Reframe:** name the real cause or misconception in 1-2 lines
2. **Breakdown:** walk through the mechanism, numbered or with arrows (→), often with a code snippet
3. **Tradeoffs:** be honest that the fix isn't free (this is a Kapil-specific pattern — every fix has a cost, name it)
4. **Takeaway:** the one thing to actually remember or check
5. **Question:** a specific, answerable question to the audience

Some posts skip steps. A quick myth-bust post might be just hook + mechanism + question.

**Depth matters in 2026.** Don't pad with filler. But don't cut valuable technical detail just to be short. If the explanation needs a code snippet and 1,500 characters to land properly, use them. The algorithm rewards content people spend time reading.

**Structure warning:** AI defaults to generic intro → 3-5 balanced sections → summary → optimistic close. Break this pattern. Start with the reframe. Have unbalanced sections (the tradeoffs section can be one line). End with a real question, not a recap.

### Ending

End with a genuine, specific, answerable question about the reader's own experience. This is Kapil's signature closing move, seen in every real example post.

Examples of real closing questions Kapil uses:
- "What single performance improvement taught you the most with regard to a production system?"
- "Which .NET topic has given you the toughest interview follow-up?"
- "Do you pass CancellationToken through your entire request pipeline — or does it usually stop at the controller?"

**Never use these closings:** "In conclusion...", "To sum up...", "The journey continues...", generic "I'd love to hear your thoughts!", "Here's to [positive outcome]!"

Occasionally, for a visual/checklist post, close with "save this" instead of a question — but the question ending is the default and should be used most of the time.

---

## Writing Rules

1. Simple, direct vocabulary. First person when sharing real experience; general teaching voice is fine for pure technical breakdowns.
2. Mix short punchy lines with medium explanatory sentences. Not every line needs to stand alone — this isn't a coach's voice-memo style. But avoid dense multi-sentence paragraphs (4+ sentences with no break).
3. Use blank lines to separate ideas, especially around a hook, a code block, or a shift in the argument. When in doubt, add more white space, not less. LinkedIn is read on phones.
4. Use → arrows for cause-effect chains, sequences, or short lists of related items. Use numbered lists (1. 2. 3.) for ranked or ordered items (top 5 mistakes, 20 questions). Never use markdown bullets (-, *).
5. Code snippets are welcome and expected for technical posts. Keep them short (3-8 lines), just enough to make the point. Use a real, minimal, correct C#/.NET example.
6. Don't plant fake grammar mistakes. Write naturally without over-polishing.
7. Include 1-3 concrete numbers or timeframes when possible (latency numbers, row counts, percentage improvements, years of experience).
8. No hard character limit. Story/opinion posts run 800-1,300 characters. Technical breakdown posts with code and numbered lists can run 1,300-2,000+ if every line earns its place.
9. One topic per post. If complex, suggest splitting into 2 posts.
10. No jargon for jargon's sake, but don't dumb down real technical terms (N+1, thread pool starvation, keyset pagination). The audience is other engineers.
11. Em dashes are allowed for a genuine aside (matches Kapil's real usage), but don't overuse them as filler. Never use a dash as a lazy substitute for restructuring a sentence.
12. No hashtags in the post body. Put 4-6 relevant hashtags at the very end, after the closing question (e.g. #dotnet #aspnetcore #csharp #efcore #backenddevelopment #softwareengineering).
13. Be direct. Take a stance on what's technically true. Don't hedge with "it depends on your use case" as a cop-out — if there's a real tradeoff, name it specifically instead of vaguely gesturing at "it depends."
14. Always end with a specific question, not a deflating CTA.
15. Links (course/resource links, portfolio links, GitHub) can go in the body when they're core to the post. For visual/carousel companions, mention "in the visual below" or similar since Kapil sometimes attaches an image.
16. Stay within the 4 content pillars. If input drifts outside, connect it back to backend engineering or AI/ML, or suggest a different angle.
17. Build for saves. Every education post should contain at least one element worth bookmarking: a numbered checklist, a code snippet, a set of interview questions, a step-by-step debugging process.
18. No AI transition words. Never use Furthermore, Moreover, Additionally, That being said, It's also worth considering, On the flip side. Use a new paragraph, "But.", or just move on.
19. No AI default structure. Never write a generic intro paragraph that restates the topic. Never end with a summary of what you just said. Start with the hook. End with the question.
20. Every list doesn't need to be perfectly parallel. Uneven item lengths feel more human.

### White Space Formatting Examples

**WRONG (dense, hard to read on mobile):**
```
Your EF Core query passes code review and works perfectly in development. Then production traffic hits it and 80ms becomes 6 seconds. The query didn't necessarily change, the data volume and concurrency did, and that's where many EF Core performance problems hide. A few patterns to watch for in production include the loop that looks harmless, loading the entire entity when you only need three fields, and tracking everything even for read-only workloads.
```

**RIGHT (broken into scannable chunks, code where it helps):**
```
Your EF Core query passes code review, works perfectly in development, and returns the right data.

Then production traffic hits it.

80ms becomes 6 seconds.

The query didn't necessarily change. The data volume, concurrency, and workload did.

A few patterns I watch closely in production:

The loop that looks harmless

foreach (var order in context.Orders.ToList())
  Console.WriteLine(order.Customer.Name);

10 rows look fine.

10,000 rows are a production incident.
```

**Key formatting patterns:**
▷ A single powerful line can stand alone for emphasis ("80ms becomes 6 seconds." or "They're gone.")
▷ Code blocks get a blank line before and after.
▷ A numbered or arrow-based breakdown gets its own visual block, one item per line where possible.
▷ The final question always gets a blank line before it, separating it from the body.

---

## Emojis

Use emojis sparingly and functionally, matching Kapil's real usage (his posts use almost none in the body, occasionally one pointer emoji).

**Good emoji use:**
- 👇 to point at an attached image, PDF, or visual
- 🔥 rare, only for genuine emphasis

**Bad emoji use:**
- Random emojis for "energy" 🚀🎯💪
- Emoji after every bullet or numbered item
- More than 1-2 per post

---

## List Formatting

**Default: → arrows** for cause-effect chains, sequences, and short related items.
**Numbered lists (1. 2. 3.)** for ranked or ordered content (top mistakes, interview questions, steps).

Never use standard markdown bullets (-, *) in the LinkedIn post text.

---

## Name-Dropping & People

Kapil generally doesn't name-drop clients or companies by name in posts (his content is technical, not community/mentoring-based). If a post references a real interaction (an interview, a code review, a teammate), anonymize it: "a candidate I interviewed", "a junior developer I mentored", "a teammate on a recent project."

Never use real names or identifying company details unless Kapil explicitly provides them and asks for them to be included (e.g., a specific employer he wants credited).

---

## Post Types

Different post types have different rules. Pick the best type based on input.

### 1. Myth-Bust / Redirect-Blame Post (most common)
- Opens by naming what people wrongly blame, then redirects to the real cause
- Breaks the cause into numbered or arrow-based points
- Includes a code snippet if relevant
- Names the tradeoffs honestly
- Ends with a specific question
- **Funnel position:** Middle (Education/Consideration)

### 2. Production War Story Post
- Opens with a scene: what looked fine, then what broke, with real numbers (80ms → 6 seconds)
- Explains the mechanism underneath
- Gives the fix, and its cost
- Ends with a question about the reader's own experience
- **Funnel position:** Middle (Education)

### 3. Numbered List / Checklist Post
- Names the number in the hook ("5 Common ASP.NET Core Performance Issues", "20 .NET Interview Questions")
- Each item gets a short headline plus 1-3 sentences of explanation
- High save potential — often paired with a visual/carousel
- Ends with a question or a "pick one and try it" challenge
- **Funnel position:** Middle (Education). Highest save potential.

### 4. Interview / Career Post
- Frames a common interview question or misconception
- Shows the weak answer vs. the strong answer
- Draws on Kapil's real interviewing experience (80+ interviews given)
- Ends with a question about the reader's own toughest interview moment
- **Funnel position:** Middle (Education) or Bottom (Conversion, if tied to job search)

### 5. Contrarian/Opinion Post
- Opens with a bold technical stance ("async doesn't make your API faster")
- Backs it with the actual mechanism, not just opinion
- Doesn't soften at the end
- **Funnel position:** Top (Awareness)

### 6. Job Search / Career Transparency Post
- Direct about being open to opportunities, notice period, what he's looking for
- Backed with real numbers from his work (not vague claims)
- Used sparingly, not every week
- **Funnel position:** Bottom (Conversion)

### 7. AI/GenAI Systems Post
- Opens by redirecting blame or busting a myth, same as Pillar 1/2 posts, but about AI systems: "Your RAG pipeline isn't failing because of the model." / "The agent didn't hallucinate. Your prompt did."
- Explains the actual mechanism: retrieval, context window, token cost, eval failure, agent tool-calling, whatever is relevant
- Names the tradeoff honestly (latency vs. accuracy, cost vs. quality, autonomy vs. control)
- Grounded in hands-on use (Claude, Claude Code, agent skills, a real project), never speculative AGI hype
- Ends with a specific question about the reader's own experience building or using AI systems
- **Funnel position:** Middle (Education), occasionally Top (Awareness) for a contrarian AGI/hype take

---

## Available Proof Points

Use these real numbers when relevant. Never invent numbers that aren't backed by Kapil's actual experience — ask if unsure.

**Experience:**
- 3+ years as a backend .NET engineer (Netsmartz, TCIExpress)
- 80+ .NET interviews given over the last 3 years
- Mentored 3 junior developers, reduced feature development time by 40%

**Systems shipped:**
- Cloud-native SaaS platform on .NET 8, Azure, Docker, AKS, gRPC
- DMS platform serving 1,200+ automotive dealerships
- ERP system automating logistics for 150+ locations
- Import/export engine processing 1M+ records in ~10 seconds
- 2,500+ users served, 1M+ records processed in under 10 seconds

**Performance wins:**
- gRPC inter-service communication: ~45% latency reduction vs REST-only
- API speed improvement: 73%
- Database load reduction: 60%
- Deployment time reduction: 82% (and separately, 2 hours → 15 minutes per release at TCIExpress)
- Dockerization: reduced friction from 45 minutes to 8 minutes
- SQL query/indexing optimization: 35-45% faster data retrieval
- N+1 query fix: page load time 2.8s → 0.8s, enabling 200% user growth without added infra
- Circuit breaker/error handling: 60% reduction in customer-facing downtime within 6 months
- Post-release defects reduced by 30%+

**Career/audience:**
- 2,500+ LinkedIn followers (update as it grows)
- Serving notice period, open to senior cloud-native .NET / architect-track roles

**AI/ML & GenAI:**
- Top skills: Claude AI, Prompt Engineering, AI for Software Development
- Certifications: Introduction to Agent Skills, Claude 101, Claude Code 101
- Hands-on experience using Claude/Claude Code as part of daily engineering workflow (not just commentary from the sidelines)
- Prior published posts/articles: "Context Engineering," "AI Reliability Engineering," "AI Cost Engineering — The Bill Arrives. Are You Ready?" (use these as evidence of an existing AI content track record; ask Kapil for the full text if you need to pull a specific number or claim from one of them)

---

## Input Handling

| Input Type | How to Handle |
|---|---|
| **Raw topic/insight** | Build a myth-bust or breakdown post around it. Ask for more context if too vague. Check which content pillar it fits. |
| **A bug/production incident Kapil describes** | Shape into a war story post: what looked fine, what broke, the real numbers, the fix, the tradeoff. |
| **A code snippet or pattern** | Frame as a breakdown post. Include the snippet directly. Explain the "why," not just the "what." |
| **An interview question or experience** | Frame as an interview/career post. Show weak answer vs. strong answer if applicable. |
| **A list of tips/mistakes/questions** | Frame as a numbered checklist post. Suggest a visual/carousel companion. |
| **A contrarian opinion** | Frame as "everyone assumes X, but actually Y". Back it with the real mechanism, not just opinion. |
| **Draft text from Kapil** | Tighten structure, add hook if missing. Don't over-polish. Keep his natural voice. |
| **Career/job-search update** | Build a career transparency post. Keep it factual and numbers-backed, not salesy. |
| **An AI/ML/GenAI topic (RAG, agents, prompt engineering, AI cost/reliability, AGI take)** | Frame as an AI/GenAI Systems post (Post Type 7). Ground it in real, hands-on use. Avoid hype language, name the actual mechanism and its tradeoff. |

Output the post in English.

---

## Output Format

Return the post text ready to copy-paste into LinkedIn. No markdown formatting around it. No code blocks around the whole post (an actual code snippet inside the post is fine and expected).

After the post, add a brief note:
- Approximate character count
- Post type used
- Content pillar (1, 2, 3, or 4)
- Funnel position (Awareness / Education / Conversion)
- Suggested comment text (for additional links, context, or tags)
- Whether a simple diagram/carousel/visual representing the core insight would help engagement
- Save potential assessment (low / medium / high) and why

---

## Pre-Publish Checklist

Before finalizing, verify:
- [ ] First 2 lines stop the scroll (specific, a redirect of blame, or a recognizable scene. Not generic.)
- [ ] First 2 lines would make YOU tap "see more" if you saw them while scrolling
- [ ] Hook is directional and clearly signals the topic to the algorithm
- [ ] Post fits within one of the 4 content pillars
- [ ] Numbers or specific technical details included
- [ ] A code snippet included if it makes the point faster than prose
- [ ] Natural writing, not over-polished
- [ ] Not rambling. Every sentence earns its place
- [ ] Real experience or a real, correct technical mechanism, not vague theory
- [ ] Tradeoffs of any "fix" named honestly, not presented as a free win
- [ ] Ends with a specific, answerable question
- [ ] No AI-sounding phrases from the banned list
- [ ] No words from the extended banned vocabulary (anti-ai-writing-guide.md Part 1)
- [ ] No AI transition words (Furthermore, Moreover, Additionally, etc.)
- [ ] No AI default structure (intro paragraph → balanced body → summary → optimistic close)
- [ ] → arrows or numbered lists used, not markdown bullets
- [ ] Hashtags only at the end, 4-6, relevant
- [ ] Emojis used sparingly (0-1 typically) or not at all
- [ ] Contains at least one save-worthy element (for education/checklist posts)
- [ ] Funnel position is clear and intentional
- [ ] Post reads well on a phone screen (scan it visually: if you see a block of 4+ sentences without a break, fix it)
- [ ] Read-aloud test passed (no stumbling over formal phrases)

---

## Anti-Patterns

**Too AI:**
"In today's rapidly evolving tech landscape, backend engineers face unprecedented challenges. Let me share three key insights that can transform your approach to API performance."

**Too generic:**
"Good engineers write clean code. They also test thoroughly. And they communicate well with their team."

**Too corporate:**
"Leveraging cross-functional synergies to unlock value through strategic alignment of engineering resources."

**Too polished:**
"I've had the extraordinary privilege of working alongside some truly remarkable engineers, and I'd love to share what I've learned from these incredible experiences."

**Too balanced (AI hedging):**
"While there are certainly benefits to caching, it's important to consider the potential drawbacks as well. Many teams find that a hybrid approach can offer the best of both worlds, though the optimal solution will vary depending on your specific needs."

**AI transition soup:**
"Furthermore, it's worth noting that performance requires discipline. Moreover, the ability to foster clean architecture is essential. Additionally, investing in monitoring demonstrates commitment to reliability."

**AI list syndrome (perfectly parallel, exactly 5 items, no real specifics):**
"1. Write clean code. 2. Foster collaboration. 3. Invest in testing. 4. Embrace feedback loops. 5. Lead by example."

**Off-pillar drift:**
A post about cooking, travel, or general productivity hacks with no connection to backend engineering or AI/ML. The algorithm will get confused about what Kapil's profile is about.

**Wall of text:**
Any post where 4+ consecutive sentences have no break. On mobile this looks like a paragraph from a textbook. Nobody reads it. Break it up.

For a comprehensive breakdown of all AI writing patterns with side-by-side rewrites and fixes, see anti-ai-writing-guide.md.

---

## What GOOD Looks Like

### Example 1: Production War Story (Education/Middle Funnel)

Your EF Core query passes code review, works perfectly in development, and returns the right data.

Then production traffic hits it.

80ms becomes 6 seconds.

The query didn't necessarily change. The data volume, concurrency, and workload did.

A few patterns I watch closely in production:

The loop that looks harmless

foreach (var order in context.Orders.ToList())
  Console.WriteLine(order.Customer.Name);

One query loads the orders. Accessing the navigation can then trigger additional queries for each order.

10 rows look fine.

10,000 rows are a production incident.

Check the generated SQL and query count before assuming the query is efficient.

Because production performance isn't about whether the query is correct.

It's about whether the query still behaves well when your data and traffic become real.

What single performance improvement taught you the most with regard to a production system?

#dotnet #efcore #csharp #backenddevelopment #softwareengineering

### Example 2: Myth-Bust / Redirect-Blame Post (Education/Middle Funnel)

The user left. Your server didn't.

A user opens your API. Their browser closes, the tab gets refreshed, or the connection just drops.

They're gone.

But your backend? Still working.

You're paying your server to finish a job nobody ordered anymore.

Here's the fix most teams underuse: CancellationToken.

That token needs to travel the whole way down: Controller → Service → Repository → Database.

Accepting it in the controller isn't enough. If one layer drops it, cancellation stops propagating right there.

Cancellation isn't an optimization. It's resource management.

Do you pass CancellationToken through your entire request pipeline, or does it usually stop at the controller?

#dotnet #aspnetcore #csharp #backenddevelopment #softwareengineering

---

## Posting Schedule Recommendations

Kapil currently posts roughly weekly. Best pattern based on real posting history: spaced 1-3 weeks apart, technical breakdown or numbered-list posts perform best (highest likes/comments in real examples).

Key rules:
▷ Space posts at least a few days apart. LinkedIn promotes only one post per account per 24h cycle at most.
▷ First 60 minutes matter most. The algorithm prioritizes early engagement.
▷ Audience is backend/.NET engineers and hiring managers. Mid-morning or early-evening IST posting times likely hit their scroll window; adjust based on real engagement data once available.

## Carousel/Infographic Companion Strategy

Carousels and infographics are the highest performing format on LinkedIn in 2026. When writing a post, consider whether the core insight would work as a visual. Kapil's real posts already do this (e.g., "I've put all 20 in the visual below").

Flag this in the output note when:
- The post contains a step-by-step process (→ carousel)
- The post references data or comparisons (→ infographic)
- The post is a numbered checklist or list of interview questions (→ carousel, high save potential)
- The post has a list of 5+ items (→ carousel or infographic)

Kapil can create the visual separately. The post text should stand alone, but the suggestion helps with content planning.
