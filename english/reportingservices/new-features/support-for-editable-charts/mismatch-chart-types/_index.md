---
title: Mismatch Chart Types
type: docs
weight: 40
url: /reportingservices/mismatch-chart-types/
ai_search_scope: cells_reportingservices
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
**Important:** The following SSRS 2008 chart types are **not** supported by Microsoft Excel. When a report containing any of these charts is exported to Excel, Aspose.Cells automatically converts the chart to a static image to preserve the visual layout.
{{% /alert %}}

## Overview

When exporting SSRS 2008 reports to Excel, chart types must have a matching Excel counterpart. If no equivalent exists, the chart cannot be recreated as an interactive Excel chart. Aspose.Cells therefore falls back to image rendering, ensuring the report looks identical to the original design.

### Why This Matters

* **Preserves visual fidelity** – The chart appearance remains unchanged.
* **Avoids broken or empty charts** – Users see a clear image instead of a missing element.
* **Impacts interactivity** – Images are static; users cannot edit data points directly in Excel.

## Chart Types Without Excel Equivalents

| SSRS Chart Type | Description (SSRS) | Excel Equivalent |
|-----------------|--------------------|------------------|
| **Line‑Stepped** | A line chart where each segment is drawn as a step rather than a straight slope. | – |
| **Range‑Plain** | Simple range chart showing a min‑max band without markers. | – |
| **Range‑Smooth** | Range chart with a smooth (curved) band. | – |
| **Range‑Column** | Column‑style range chart displaying vertical bands. | – |
| **Range‑Bar** | Horizontal bar range chart. | – |
| **Range‑ErrorBar** | Range chart with error bars for statistical variance. | – |
| **Range‑BoxPlot** | Box‑and‑whisker plot visualizing statistical distribution. | – |
| **Shape‑Funnel** | Funnel diagram often used in sales pipelines. | – |

> **Note:** The dash (–) in the *Excel Equivalent* column indicates that no native Excel chart type matches the SSRS chart.
