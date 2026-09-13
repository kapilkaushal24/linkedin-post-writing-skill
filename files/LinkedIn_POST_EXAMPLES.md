# Real LinkedIn Post Examples

These are actual posts Kapil published. Use them to calibrate voice, structure, and tone.

**Note:** All 4 examples below are .NET/backend posts (Pillars 1-2). Kapil has also published AI/ML posts (Pillar 3) — "Context Engineering," "AI Reliability Engineering," and "AI Cost Engineering — The Bill Arrives. Are You Ready?" — but only the titles are known so far. When writing AI/ML posts, apply the same voice patterns documented below (myth-bust hooks, honest tradeoffs, code/specifics over hype, a closing question) until real AI post text is pasted in here for tighter calibration.

---

## Example 1: Production War Story (EF Core Performance)

Your EF Core query passes code review, works perfectly in development, and returns the right data.

Then production traffic hits it.

80ms becomes 6 seconds.

The query didn't necessarily change. The data volume, concurrency, and workload did.

That's where many EF Core performance problems hide.

A few patterns I watch closely in production:

The loop that looks harmless

foreach (var order in context.Orders.ToList())
  Console.WriteLine(order.Customer.Name);

One query loads the orders. Accessing the navigation can then trigger additional queries for each order.

10 rows look fine.

10,000 rows are a production incident.

Check the generated SQL and query count before assuming the query is efficient.

Loading the entire entity

You need Id, Total, and Status. But the query materializes the entire entity and potentially its relationships.

Projection keeps the database result focused:

.Select(x => new { x.Id, x.Total, x.Status })

Less data transferred. Less materialization. Less memory.

Tracking everything

EF Core tracks entities by default so it can detect changes. That's useful when you're going to update them.

For read-only workloads returning thousands of entities, that tracking adds overhead.

AsNoTracking() can help, but don't add it everywhere blindly. Understand the workload first.

Multiple collection Includes

10 orders × 5 items × 3 payments = 150 result rows. Sometimes split queries are the better trade-off.

Filtering after ToList()

Now the database already returned every row. Push filtering, projection, and aggregation to SQL whenever possible.

Pagination that ignores scale

Deep offsets can become increasingly expensive as the dataset grows. For large ordered datasets, keyset pagination can be a better approach.

Don't optimize the C# first.

Understand the database work your C# is creating.

Because production performance isn't about whether the query is correct.

It's about whether the query still behaves well when your data and traffic become real.

#dotnet #efcore #csharp #backenddevelopment #softwareengineering

**Type:** Production War Story | **Pillar:** 1 (.NET/EF Core Performance) | **Funnel:** Education | **~1,750 chars** | **9 likes**

---

## Example 2: Numbered List / Myth-Bust Post (ASP.NET Core Performance)

The Azure environment, Kubernetes, and your SQL Server tier are not the causes of your ASP.NET Core API being slow.

The slow-down is due to five habits which gradually accumulate until they become apparent when production traffic is involved.

I've debugged this exact story more times than I can count: a simple endpoint takes 200 milliseconds locally, then slows to 3-4 seconds in production. The infrastructure hasn't changed. The code was simply never designed for handling large volumes.

Here's what's usually happening under the hood:

1. No caching on data that barely changes
Hitting the database every request for config values or lookup tables that update once a day. Fixable in an afternoon with IMemoryCache or Redis.

2. Sync calls hidden inside "async" methods
Call .Result or .Wait() three layers down and you block a thread pool thread. Under load, you're not scaling, you're queuing.

3. EF Core queries built for correctness, not speed
Tracked queries and full entities loaded when three columns would do.

4. Returning everything instead of paging
GetAllOrders() returning 40,000 rows because pagination "can wait." It can't.

5. N+1 queries hidden inside a foreach loop
One query for orders, then one more per order for line items. 50 orders becomes 51 round trips.

If there's just one issue to fix, it's the N+1 problem. It's the easiest to miss in a code review and usually the biggest latency spike.

None of these fixes are free. Caching risks stale data. Pagination changes your API contract. Query tuning can cost readability. Every fix is a trade-off, not a magic bullet.

A fast API isn't the result of one big optimization. It's the absence of a dozen small mistakes nobody caught in review.

What single performance improvement taught you the most with regard to a production system?

#dotnet #aspnetcore #efcore #backenddevelopment #softwareengineering

**Type:** Numbered List / Myth-Bust | **Pillar:** 1 (.NET Performance) | **Funnel:** Education | **~1,650 chars** | **23 likes, 10 comments** (real engagement: sparked a debate in comments about EF vs Dapper)

---

## Example 3: Numbered Checklist Post (Interview Prep)

I've given 80+ .NET interviews over the last 3 years.

And if I had to prepare for another one tomorrow, I wouldn't start with a list of 300 questions.

I'd start with 20.

Because after enough interviews, you start noticing a pattern.

Interviewers aren't just checking whether you remember a definition. They keep digging into:

→ Why does it work this way?
→ What happens under the hood?
→ What are the trade-offs?
→ What breaks in production?
→ Have you actually used it?

You answer "It's just async/await." Then comes "What happens when you await?" "Thread or Task?" "I/O-bound vs CPU-bound?" "What about cancellation?"

One concept suddenly becomes 5-10 questions.

Don't memorize 300 answers. Build depth around the concepts that keep coming back.

So I put together the 20 .NET interview questions I'd prepare first, covering C#, ASP.NET Core, SQL & EF Core, Architecture, Distributed Systems, and Production & Problem Solving.

👇 I've put all 20 in the visual below.

Pick one question. Try answering it without Google. Then ask yourself: "What follow-up questions could the interviewer ask me?"

That's where the real preparation starts.

Which .NET topic has given you the toughest interview follow-up?

#dotnet #csharp #aspnetcore #softwareengineering #interviewprep

**Type:** Numbered Checklist (with carousel companion) | **Pillar:** 4 (Career/Interview Prep) | **Funnel:** Education | **~1,150 chars** | **335 likes, 21 comments** — Kapil's best-performing post. Multiple commenters asked for the PDF. Highest save/share potential of all examples.

---

## Example 4: Myth-Bust Post (CancellationToken)

The user left. Your server didn't.

A user opens your API. Their browser closes, the tab gets refreshed, or the connection just drops.

They're gone.

But your backend? Still working:
→ Querying the database
→ Calling an external API
→ Processing data
→ Building a response

For someone who isn't there anymore.

This isn't just wasted CPU cycles. At scale, abandoned requests quietly eat into database connections, thread-pool capacity, memory, and external API rate limits.

You're paying your server to finish a job nobody ordered anymore.

Here's the fix most teams underuse: CancellationToken. It's a simple signal that says: "This work isn't needed anymore. Stop if you can."

public async Task<IActionResult> GetCustomer(
  CancellationToken cancellationToken)
{
  var customer =
    await service.GetCustomerAsync(cancellationToken);

  return Ok(customer);
}

That token needs to travel the whole way down: Controller → Service → Repository → Database / HTTP call.

Accepting it in the controller isn't enough. If one layer drops it, cancellation stops propagating right there, and everything downstream keeps running like nothing happened.

Cancellation isn't an optimization. It's resource management.

Do you pass CancellationToken through your entire request pipeline, or does it usually stop at the controller?

#dotnet #aspnetcore #csharp #backenddevelopment #softwareengineering

**Type:** Myth-Bust / Redirect-Blame | **Pillar:** 1 (.NET Performance) | **Funnel:** Education | **~1,150 chars** | **52 likes, 12 comments** — sparked a real technical debate in comments (one commenter pushed back with "why is a cancellation token needed?", others jumped in to answer).

---

## Voice Patterns to Notice

1. **Hooks redirect blame or set a scene, never ask a question.** "The Azure environment... are not the causes" not "Is your API slow?" "The user left. Your server didn't." not "Do you know what happens when a user disconnects?"

2. **Numbers everywhere, always real.** 80ms → 6 seconds. 80+ interviews. 50 orders, 51 round trips. Never vague ("significantly slower").

3. **→ arrows for chains and short lists. Numbered lists (1. 2. 3.) for ranked items.** Never dashes or asterisks as bullets.

4. **Code snippets appear directly in the post** when they explain faster than prose. Short, real, minimal.

5. **Every "fix" gets its trade-off named honestly.** "None of these fixes are free." This is a signature move, not hedging, it's confidence: naming the cost without being asked.

6. **Endings are always a specific question about the reader's own experience.** Never a generic CTA, never "thoughts?"

7. **Hashtags only at the very end, 4-6 of them, always relevant** (#dotnet, #aspnetcore, #efcore, #csharp, #backenddevelopment, #softwareengineering, #interviewprep).

8. **Minimal emoji use.** One pointer emoji (👇) at most, only when referencing an attached visual.

9. **Comfortable with an em dash for a genuine aside**, unlike a "no dashes ever" rule, this is one place Kapil's real voice differs from generic anti-AI advice. Used sparingly.

10. **No throat-clearing.** Posts start mid-scenario or with a direct, confident claim. Never "In today's..." or "As someone who...".

11. **Confident teaching voice, not confrontational.** He states the mechanism plainly and lets the technical clarity do the work, rather than being combative or coach-like.

For the full framework on eliminating AI patterns from writing, see anti-ai-writing-guide.md.

---

## ADD YOUR OWN EXAMPLES BELOW

Paste new best-performing posts here as they get published, with engagement numbers if available. The more examples, the sharper the voice calibration. Paste the full text of "Context Engineering," "AI Reliability Engineering," and "AI Cost Engineering" here when available — they'll sharpen the Pillar 3 (AI/ML) voice calibration significantly.

### Example 5: [Paste an AI/ML post here, e.g. "Context Engineering"]

### Example 6: [Paste here]
