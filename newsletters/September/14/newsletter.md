# The .NET Horizon — Model Context Protocol

**Format:** A (Chaptered)
**Pillar:** 3 — AI/ML Engineering & GenAI Systems (with a .NET-specific angle throughout)
**Suggested publish date:** Monday, September 14, 2026
**Word count:** ~1,850
**Why this topic now:** This is the explicit topic teased at the end of the "Context Engineering" issue ("Next issue, we go deep on Model Context Protocol"). It's also independently one of the most active current trends in AI engineering (agent infrastructure, orchestration, and cross-provider tool standardization), so it lands as both a promised follow-through and a timely topic.
**Diagram/visual placeholders included:** "Ad Hoc Tool Integration vs MCP", "MCP Architecture: Host, Client, Server", "Tools vs Resources vs Prompts", "MCP Request Lifecycle", "MCP Security Boundary"
**Suggested next-issue teaser:** Evals — how to actually measure whether an LLM feature works before your users find out it doesn't.

---

Model Context Protocol

Every Team Building Tool-Using Agents Invented the Same Integration Layer. Badly.

If you've shipped more than one AI feature that needed to call a tool, a database, or an external API, you've probably built the same thing twice: a bespoke adapter that takes the model's intent, maps it to a function call, executes it, and feeds the result back in the right shape. Do this for three features and you have three slightly different adapters, three different error-handling conventions, and no way to reuse a tool integration you already built for feature one when feature three needs it.

Model Context Protocol (MCP) exists because this problem was universal enough to standardize. It defines how an application exposes tools, data sources, and prompt templates to a model in a consistent, interoperable way, so a tool integration becomes a reusable component instead of a one-off wire-up. This issue covers what MCP actually standardizes, where it fits in the context engineering pipeline covered in the last issue, its security implications, and what adopting it looks like from a .NET team's perspective.

Ad Hoc Tool Integration vs MCP

CHAPTER 2 — WHY THIS NEEDED STANDARDIZING

Production scenario: A platform team has three AI features, each built by a different squad. All three need "look up a customer record." Each implemented its own version of that lookup as a tool, with different parameter names, different error formats, and no shared code.

Engineering discussion: Without a shared protocol, every tool integration is bespoke: how the model is told the tool exists, how parameters are validated, how results are returned, and how errors surface all get reinvented per feature, per team. This isn't a hypothetical inefficiency, it's the default outcome of multiple teams solving the same integration problem independently under deadline pressure.

Tradeoffs: Adopting a standard costs upfront effort: wrapping existing internal APIs as MCP servers instead of calling them directly. It pays off the moment you have more than one AI feature that needs the same underlying capability.

Common mistakes: Treating each new AI feature's tool needs as a brand-new integration problem instead of asking "do we already expose this as a reusable tool."

Best practices: Before writing a new tool integration, check whether an MCP server already exposes that capability, or whether it's worth building one that will.

Enterprise recommendation: If you're building more than one AI feature that needs external tools or data, standardize on MCP now rather than accumulating a second bespoke adapter.

CHAPTER 3 — WHAT MCP ACTUALLY STANDARDIZES

Production scenario: A new engineer joins a team already using MCP and asks, "so is this just a wrapper around REST APIs?"

Engineering discussion: MCP standardizes three kinds of context a server can expose to a model: tools (functions the model can invoke, with typed inputs and outputs), resources (data the model can read, like a file or a database record, without necessarily invoking an action), and prompts (reusable prompt templates the server can offer, so prompt engineering for a given tool lives next to the tool itself, not scattered across every client that calls it).

Tradeoffs: This three-way split adds a small amount of conceptual overhead compared to "everything is just a function call," but it maps cleanly onto how context engineering already separates instructions, data, and actions, which is exactly the distinction the Context Engineering issue argued matters.

Common mistakes: Modeling everything as a tool, including things that are really just data lookups, which unnecessarily implies the model is "doing" something rather than "reading" something.

Best practices: Use resources for read-only context the model needs to see, tools for anything with a side effect or that requires the model to decide when to invoke it, and prompts for reusable templates tied to a specific server's domain.

Enterprise recommendation: Audit existing "tools" in your current AI features. A meaningful fraction are probably resources in disguise, and reclassifying them simplifies both the model's decision-making and your own testing.

Tools vs Resources vs Prompts

CHAPTER 4 — HOSTS, CLIENTS, AND SERVERS

Production scenario: A team wants to let their internal support-ticket assistant use the same customer-data integration their sales assistant already built, without copy-pasting code between the two.

Engineering discussion: MCP defines three roles. A host is the application the user actually interacts with (the support assistant, the sales assistant). A client lives inside the host and manages the connection to one MCP server. A server exposes tools, resources, and prompts for a specific domain (customer data, an internal wiki, a ticketing system), independent of which host is calling it.

Tradeoffs: Separating server from host means the customer-data server can be written once and reused by both the support and sales assistants, but it also means the server has to be designed generically enough to serve callers it doesn't control, which requires more careful interface design than a tightly coupled internal function call.

Common mistakes: Building an MCP server that assumes too much about which host will call it, baking host-specific logic into a component that's supposed to be reusable.

Best practices: Design each server around a single domain of capability (customer data, ticketing, internal docs) and keep host-specific behavior (which tools to expose, in what order, with what framing) in the client/host layer, not the server.

Enterprise recommendation: Treat each MCP server the way you'd treat an internal microservice: one clear domain of responsibility, a stable contract, and no assumptions about its callers.

MCP Architecture: Host, Client, Server

CHAPTER 5 — WHERE MCP FITS IN THE CONTEXT ENGINEERING PIPELINE

Production scenario: A team that already built a context assembly pipeline (retrieve, filter, rank, compress, assemble, as covered in the Context Engineering issue) starts adopting MCP and isn't sure whether it replaces that pipeline or sits alongside it.

Engineering discussion: MCP doesn't replace the context assembly pipeline. It standardizes one of the pipeline's inputs: how retrieved data and available actions get exposed to the model in the first place. The filtering, ranking, and compression discipline from the previous issue still applies fully to whatever an MCP server returns.

Tradeoffs: Treating MCP servers as just another context source (subject to the same token budget as everything else) keeps the discipline consistent, but requires resisting the temptation to let an MCP server dump its full response into the prompt just because the protocol made it easy to fetch.

Common mistakes: Assuming that because MCP standardizes how you fetch context, you no longer need to curate what you fetch. The lost-in-the-middle effect doesn't care whether the extra tokens came from a hand-rolled retrieval call or a standardized MCP resource.

Best practices: Route MCP tool and resource results through the same filter-rank-compress stages as any other context source before they reach the final prompt.

Enterprise recommendation: MCP is a standardization layer for context sources, not a replacement for the context engineering discipline covering how much of that context actually earns a place in the prompt.

CHAPTER 6 — SECURITY: THE NEW ATTACK SURFACE

Production scenario: A team exposes an internal database as an MCP resource so their support assistant can look up order history. Three weeks later, a prompt injection in a customer's support message causes the model to request an unrelated customer's data through that same resource.

Engineering discussion: Every MCP server is a new trust boundary. The model decides when to call a tool or request a resource, which means anything that can influence the model's reasoning, including user input and retrieved documents, can potentially influence which tools get called and with what parameters.

Tradeoffs: Fine-grained permission checks on every tool call add latency and implementation complexity, but skipping them means the model's reasoning (which can be manipulated) is your only access control layer, which is not a security boundary at all.

Common mistakes: Granting an MCP server the same broad database access the backend service already has, on the assumption that the model will only ask for what it needs.

Best practices: Apply the principle of least privilege at the server level, not just the application level. An MCP server exposing customer lookups should only be able to reach the specific records the calling user is authorized to see, enforced server-side, not left to the model's judgment.

Enterprise recommendation: Treat every MCP tool call the way you'd treat an API call from an untrusted client: authenticate, authorize, and validate parameters server-side, regardless of what the model intended.

MCP Security Boundary

CHAPTER 7 — VERSIONING AND BREAKING CHANGES

Production scenario: A team updates their internal MCP server's "get order" tool to add a required parameter. Every AI feature that used the old version starts failing silently, because none of them pinned a protocol or schema version.

Engineering discussion: An MCP server's tool definitions are effectively an API contract with every host that calls it, and they need the same discipline: explicit versioning, deprecation windows, and backward compatibility guarantees, not silent changes.

Tradeoffs: Versioning tool schemas adds process overhead compared to just changing the function signature and redeploying, but the alternative is breaking every consumer of that server without warning.

Common mistakes: Treating an MCP server's internal implementation and its exposed tool contract as the same thing, so any refactor risks changing the contract by accident.

Best practices: Version tool schemas explicitly. Add new optional parameters freely; treat removing or changing the meaning of an existing parameter as a breaking change requiring a new version.

Enterprise recommendation: Apply the same API governance you already use for public or internal REST APIs to MCP server contracts. This is not a new problem, it's a familiar one wearing a new name.

CHAPTER 8 — MCP IN A .NET STACK

Production scenario: A .NET team wants to expose their existing internal APIs as MCP servers without rewriting the business logic those APIs already contain.

Engineering discussion: An MCP server is fundamentally a thin protocol adapter in front of existing capability. In a .NET stack, this maps naturally onto an existing service: the tool and resource definitions become a typed contract (similar in spirit to a gRPC or OpenAPI contract), and the underlying implementation calls the same repository and service layer the REST API already uses.

Tradeoffs: Building the MCP layer as a genuinely thin adapter (no business logic duplicated) keeps maintenance cost low, but requires resisting the temptation to add MCP-specific shortcuts that bypass the validation and authorization the existing API already enforces.

Common mistakes: Building a parallel, looser version of business logic specifically for the MCP server, because "the model doesn't need all those checks." It does. The model is an untrusted caller like any other.

Best practices: Route MCP tool implementations through the same service layer, validation, and authorization your existing controllers already use. The MCP server should be a new front door, not a new set of rules.

Enterprise recommendation: If you're building an MCP server in .NET, structure it as a thin translation layer over your existing service interfaces, the same way you'd structure a new API version, not as a standalone reimplementation.

CHAPTER 9 — WHEN NOT TO REACH FOR MCP

Production scenario: A team building a single, simple AI feature with one internal API call debates whether to build a full MCP server for it.

Engineering discussion: MCP earns its complexity when a capability needs to be reused across multiple AI features or exposed to external tools and clients you don't control. For a single feature with a single, stable integration that will never be reused, a direct function call is simpler and has less to maintain.

Tradeoffs: Building MCP infrastructure for a one-off integration adds protocol overhead (server setup, schema definitions, versioning discipline) with no reuse benefit to offset it.

Common mistakes: Adopting MCP everywhere because it's the current standard, rather than because a specific integration will actually be reused or exposed externally.

Best practices: Default to a direct function call for single-use, single-feature integrations. Reach for MCP when a second consumer of the same capability shows up, or when external interoperability is a real requirement, not a hypothetical one.

Enterprise recommendation: Let reuse, not trend-following, decide when an integration graduates from a direct call to a standardized MCP server.

CHAPTER 10 — MCP PRODUCTION CHECKLIST

Before exposing a capability through MCP, confirm:

- Is this capability actually going to be reused by more than one AI feature or host?
- Does the MCP server enforce authorization server-side, independent of what the model requests?
- Are tool, resource, and prompt definitions modeled as the right type, not everything forced into "tool"?
- Is the tool schema versioned, with breaking changes handled as a new version, not a silent change?
- Does context returned by the server still pass through the same filter-rank-compress discipline as any other context source?
- Is the server scoped to a single, clear domain of responsibility, without host-specific assumptions baked in?
- Is the MCP server treated as an untrusted-caller boundary, with the same validation as a public API?

CHAPTER 11 — FINAL TAKEAWAYS

MCP doesn't solve a new problem. It standardizes a problem every team building tool-using AI features was already solving, badly, in isolation, one bespoke adapter at a time.

The teams getting real value from it aren't the ones adopting it everywhere on principle. They're the ones who noticed a capability was about to be built twice, and built it once as a properly scoped, properly secured server instead.

Standardization only pays off when the discipline underneath it, authorization, versioning, and the same context curation covered in the last issue, is already in place. MCP makes reuse easier. It doesn't make sloppy context management or missing authorization checks go away.

Next issue, evals: how to actually measure whether an LLM feature works before your users find out it doesn't.

---

**Newsletter:** The .NET Horizon
