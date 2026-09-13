# AKS readiness vs liveness probe myth-bust

**Pillar:** 2 — Cloud-Native Architecture & DevOps
**Post Type:** Myth-Bust / Redirect-Blame
**Funnel:** Education (Middle funnel)
**Suggested publish date:** Thursday, September 17, 2026
**Suggested best time:** 10:00-11:30 AM IST
**Hashtags used:** #dotnet #azure #kubernetes #aks #devops #cloudnative
**Save potential:** Medium-high — probe misconfiguration is a common, checklist-worthy production gap
**Visual companion:** Simple diagram: "Liveness check (is it alive?) vs Readiness check (can it actually serve?)" as a two-column comparison graphic.
**Why this topic:** Chosen for Pillar 2 (cloud-native/DevOps) to balance the week's mix — rounds out Tue (Pillar 1) and Wed (Pillar 3) with a Kubernetes/AKS post, directly matching Kapil's real production experience (AKS, containerization, readiness/liveness probes are explicitly listed on his résumé).

---

Your AKS pods are healthy.

Your users are still timing out.

I've seen this exact gap more than once: Kubernetes says every pod is green, and production traffic is failing anyway.

Here's what's usually happening under the hood:

→ Liveness probe passing means the process hasn't crashed. That's it. It says nothing about whether the app can actually serve a request.

→ Readiness probe passing means the pod is added back to the service's load balancer rotation. If this check is too shallow (just "is the process up"), Kubernetes sends traffic to a pod that isn't actually ready.

→ A pod can be alive, ready, and still choking, if it's warming up a cache, opening database connections, or waiting on a downstream dependency that's slow.

The mistake I see most: teams point both probes at the same trivial endpoint ("return 200 OK") and call it done.

A readiness probe should check the things that actually matter: can it reach the database, is the connection pool initialized, is the cache warm enough to serve real requests.

A liveness probe should check almost nothing beyond "is the process responsive," because a liveness failure kills and restarts the pod. An overly strict liveness check turns a slow dependency into a restart loop.

None of this is free. Deeper health checks cost CPU and add latency to every probe interval. Get the interval and threshold wrong and you'll either restart healthy pods or keep serving from broken ones.

Do your readiness and liveness probes actually check different things, or are they hitting the same endpoint?

#dotnet #azure #kubernetes #aks #devops #cloudnative
