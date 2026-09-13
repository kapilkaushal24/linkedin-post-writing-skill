# Async/await myth-bust — does it create a thread?

**Pillar:** 1 — .NET / ASP.NET Core / EF Core Performance & Backend Engineering
**Post Type:** Myth-Bust / Redirect-Blame
**Funnel:** Education (Middle funnel)
**Suggested publish date:** Tuesday, September 15, 2026
**Suggested best time:** 10:00-11:30 AM IST (Tue/Wed/Thu 10 AM-12 PM local audience time is the strongest consistent LinkedIn window)
**Hashtags used:** #dotnet #csharp #aspnetcore #backenddevelopment #softwareengineering
**Save potential:** Medium-high — the async/await mental model correction is a common interview + production gap, worth bookmarking
**Visual companion:** None required. Optional: a simple before/after diagram of "thread blocked waiting" vs "thread released, continuation resumes" would work as a carousel companion.
**Why this topic:** Chosen for Pillar 1 (core .NET performance content) and because "does async create a thread" is a live, recurring point of confusion visible in Kapil's own audience (see the "Cuong Nguyen" comment thread under Kapil's interview-questions post, which covers the exact same misconception from a different angle) — a natural, credible follow-up topic, not a random pick.

---

Async/await does not create a new thread.

Most .NET developers say it does anyway, including some who've shipped async code for years.

Here's what's actually happening under the hood.

When you await a Task, the compiler generates a state machine. It doesn't spin up a thread and wait for the result.

public async Task<Customer> GetCustomerAsync(int id)
{
  var customer = await _db.Customers.FindAsync(id);
  return customer;
}

That await doesn't block a thread. It registers a continuation and gives the thread back to the pool.

→ If the operation is I/O-bound (database call, HTTP request, file read), no thread is doing anything while you wait. The OS handles the I/O, and a thread pool thread picks up the continuation when it's done.

→ If the operation is CPU-bound, wrapping it in Task.Run() does use a thread, because there's real work that has to happen somewhere.

This distinction is why "does async make my API faster" is the wrong question.

Async doesn't make one request faster. It lets your server handle more requests at the same time, because threads aren't sitting idle waiting on the database.

The tradeoff nobody mentions: the state machine has real overhead. For a genuinely CPU-bound, single-request workload, sync code can outperform async code doing the same work.

Async is a scalability tool, not a speed tool.

Do you know which of your "async" methods are actually I/O-bound versus just wrapping CPU work in Task.Run()?

#dotnet #csharp #aspnetcore #backenddevelopment #softwareengineering
