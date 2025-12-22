---
title: Configuring Report Servers to store or cache the report server data
linktitle: Store report server data
type: docs
weight: 30
url: /reportingservices/configuring-report-servers-to-store-or-cache-the-report-server-data/
ai_search_scope: cells_reportingservices
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Aspose.Cells for Reporting Services Report Designer saves the URL of the last‑accessed report server. When you open **Report Server Manager** again, the dialog automatically loads that saved information, allowing you to reconnect quickly.  
This article explains how to **store** (persist) and **cache** (temporarily keep) report‑server data, why you might need each option, and how to configure them safely.

## When to Store vs. Cache Server Data

| Scenario | Store (Persist) | Cache (Temporary) |
|----------|-----------------|-------------------|
| **User convenience** – automatically repopulate the last used server on next launch | ✅ Recommended for desktop environments where the same user repeatedly works with a single server. |
| **Security‑sensitive environments** – avoid leaving credentials or URLs on disk | ❌ Not recommended; use cache only or rely on manual entry each session. |
| **High‑frequency switching** – users connect to many servers in a single session | ✅ Cache is faster; persisting each change may cause stale data. |
| **Performance‑critical reports** – minimize round‑trips to the server | ✅ Cache reduces network latency for repeated data retrievals. |
