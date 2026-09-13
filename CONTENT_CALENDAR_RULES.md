# Content Calendar Folder Rules

How drafted posts and newsletter issues get saved to disk in this project. Read by Claude before saving any drafted content, and referenced from `LinkedIn PROJECT_INSTRUCTIONS to paste.md` and `files/linkedin-weekly-system.md`.

---

## Folder Structure

```
linkedin-post-writing-skill/
  posts/
    <MonthName>/
      <Day>/
        post.md
        thumbnail.png
  newsletters/
    <MonthName>/
      <Day>/
        newsletter.md
        thumbnail.png
  tools/
    make_thumbnail.py
    template_reference_example.png
    reference-thumbnails/       (Kapil's collected design references)
```

- `<MonthName>` — full month name, capitalized, no year (e.g. `September`). If content spans a year boundary and ambiguity matters, suffix with the year: `September-2026`.
- `<Day>` — the numeric day of month the post/issue is **intended to be published**, no leading zero (e.g. `15`, not `09`). Not the day it was drafted, if different.
- One post per day folder in the common case. If more than one post is drafted for the same day (rare — the weekly system targets one post per day), add a suffix: `post-2.md`, `post-3.md`.
- Newsletter issues follow the same month/day pattern under `newsletters/`, using the intended publish day.

## File Contents

Every `post.md` starts with a short metadata block, then a `---` separator, then the post text exactly as it should be copy-pasted to LinkedIn (no extra formatting around it):

```
# [Short internal title, not the post's hook]

**Pillar:** [1/2/3/4 — name]
**Post Type:** [from LinkedIn_SKILL.md Post Types]
**Funnel:** [Awareness/Education/Conversion]
**Suggested publish date:** [day, date]
**Suggested best time:** [time window + timezone]
**Hashtags used:** [list]
**Save potential:** [low/medium/high — why]
**Visual companion:** [none / carousel / infographic — what it would show]

---

[Post text, ready to copy-paste]
```

Every `newsletter.md` follows the same idea, using the metadata fields from `LinkedIn_NEWSLETTER_SKILL.md`'s Output Format section (word count, format A/B, pillar, next-issue teaser, diagram placeholders) instead of the post fields above.

## Thumbnails

Every post and newsletter issue gets a matching `thumbnail.png` in the same dated folder, generated with `tools/make_thumbnail.py` (Pillow-based, no external services or API keys, no internet dependency). This is **the one canonical template** — don't design a one-off thumbnail outside this system. `tools/reference-thumbnails/` holds real design references Kapil collected; `tools/legacy_v1_make_thumbnail.py` and `tools/legacy_v2_make_thumbnail.py` are superseded styles kept only for history and should not be used for new work.

**Design system (v3, adopted 2026-09-13 — "Light Glossy-Card SaaS"):** Kapil reviewed `tools/reference-thumbnails/` (a mix of dark-neon, light-glossy-card, and hand-drawn-cartoon styles he'd experimented with) and chose the **light glossy-card** direction, closest to the AutoMapper ("Hiding Complexity, Or Removing It?") and Cache Upgrade ("100→1") references in that folder. Every thumbnail is built from the same recipe:

1. **Canvas:** posts are 1080×1350 (4:5 portrait, best mobile feed real estate); newsletter covers are 1200×627 (1.91:1, standard article header ratio). PNG only. Never square or 16:9 for a post.
2. **Background:** light neutral gradient (`#F8F9FC` → `#EDEFF5`) with a very faint graph-paper grid — reads like a clean spec document, not a slide deck.
3. **Category label (top-left):** small bold accent-colored uppercase label (e.g. `.NET / PERFORMANCE`, `AI ENGINEERING`) with a short colored underline rule beneath it.
4. **Headline (top 20-35%):** short, punchy, sentence case (not all-caps) — matches the references' voice more than a terse all-caps hook. Rendered two-tone: the setup line in near-black (`#12141C`), the punchline/emphasis line in the pillar accent color, both in a faux-bold weight (Segoe UI Bold stamped twice for extra heft, simulating the "Black" weight the references use). A muted subtitle line with a small colored left-bar sits underneath.
5. **One content block (center):** exactly one of three reusable patterns in `CONTENT_BLOCKS` inside `tools/make_thumbnail.py` — pick whichever matches the post:
   - `flow_cards` — 3 white rounded cards with a simple line-icon + label, connected by black arrows (architecture / transformation chains, e.g. AutoMapper's Entity → AutoMapper → DTO)
   - `big_number` — a huge "before → after" number pair (e.g. `1 → 247`, `5 → 1`) with a small pill caption underneath, mirroring the Cache Upgrade "100→1" reference — best for dramatic stat/degradation/improvement posts
   - `comparison_cards` — 2-3 bordered white cards, each with a colored top bar and a ✓/✗ checklist (option comparisons, X vs Y posts, mirrors the IMemoryCache/IDistributedCache/HybridCache reference)
   
   Add new content-block functions as new post shapes come up, following the `(draw, img, box, accent, **kwargs)` signature already used by the three above.
6. **Negative space stays intentional** below the content block — don't force it to fill the whole canvas.
7. **Bottom branding (subtle, never dominant):** a small dark pill badge with a colored dot + short tagline (e.g. "AI ENGINEERING NOTES"), plus Kapil's circular photo (`Kapil-AI-1.jpg` from the project root, ~58px, accent-colored ring) with "Kapil Kaushal" + "@kapilkaushal24" beneath the pill.
8. **Color coding by pillar**, kept consistent across every thumbnail: **violet** for Pillar 1 (.NET/backend performance), **blue** for Pillar 2 (cloud-native/DevOps), **teal** for Pillar 3 (AI/ML/GenAI), **amber** as a distinct accent for Pillar 4 (career) or the newsletter. The newsletter masthead ("THE .NET HORIZON") always uses amber so it reads as a distinct publication from the four post pillars.
9. **Icons are simple line-drawn primitives** (`icon_glyph()` — db, code, brace, clock, bolt, loop, shield, check, etc.), never photographic or stock-icon assets. Add new glyphs to this function as needed, keeping the same minimal line-art weight.

**To generate a new week's thumbnails:** call `render_post()` (posts) or `render_newsletter()` (newsletter) in the `__main__` block of `tools/make_thumbnail.py` with that post's category, two-tone headline segments, subtitle, chosen content block + kwargs, and accent, then run `python tools/make_thumbnail.py`. A flagship reference example (`tools/template_reference_example.png`, the "1 → 247" N+1 example) shows the target quality bar — compare new thumbnails against it before considering them done.

## Workflow

1. When asked to plan or draft posts/issues, follow `files/linkedin-weekly-system.md` and the relevant skill file (`LinkedIn_SKILL.md` or `LinkedIn_NEWSLETTER_SKILL.md`) to produce the content.
2. Save the result to the correct dated folder under `posts/` or `newsletters/` using the structure above. Create the month/day folders if they don't exist.
3. Don't overwrite an existing dated post/issue without confirming — if a slot is already filled, ask whether to replace it, add a suffixed variant, or pick a different day.
4. Once Kapil confirms a post was actually published, it's fine to leave the file in place as an archive (it doubles as the historical record MEMORY_SEEDS.md summarizes from).
5. Old month/day folders are never deleted automatically — they're the archive of what was planned and published.

## Why dated folders instead of a flat list

This makes the publish calendar browsable directly in the filesystem (open `posts/September/` and see the whole month at a glance), keeps drafts for different days from colliding, and gives every post/issue a stable, referenceable path for MEMORY_SEEDS.md to point back to.
