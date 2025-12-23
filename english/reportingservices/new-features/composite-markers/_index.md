---
title: Composite Markers
type: docs
weight: 10
url: /reportingservices/composite-markers/
ai_search_scope: cells_reportingservices
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Overview

We have introduced the **Composite Markers** feature.  
Now you can join markers together as a composite marker by using the concatenation character **&**.  
For example:

```vbnet
&= Parameters!ReportYear.Value & "-" & Parameters!ReportMonth.Value & " Sales Report"
```

The expression above creates a marker that consists of two **Parameter** markers and two **Static‑text** markers.  

Composite markers let you build a single, readable label from several individual markers.  
They are especially useful when a report title, axis label, or tooltip must contain dynamic data (parameters) combined with fixed text.

## Syntax

| Element | Description |
|---------|-------------|
| `&=`   | Starts a composite‑marker expression. |
| `&`    | Concatenates the next part of the expression. |
| `Parameters!Name.Value` | Inserts the value of a report parameter. |
| `"text"` | Adds static text. |
| `-` or any other character | Can be used as a literal separator inside the quotes. |

> **Note:** All parts must be separated by the **&** operator; spaces around the operator are optional but improve readability.

## Example in Context

```vbnet
&= Parameters!ReportYear.Value & "-" & Parameters!ReportMonth.Value & " Sales Report"
```

| Part                              | Result (assuming Year = 2025, Month = 03) |
|-----------------------------------|-------------------------------------------|
| `Parameters!ReportYear.Value`    | 2025                                      |
| `"-"`                             | -                                         |
| `Parameters!ReportMonth.Value`   | 03                                        |
| `" Sales Report"`                 |  Sales Report                             |
| **Composite marker output**       | **2025‑03 Sales Report**                  |

### Where to use it

- **Report titles** – Show the selected period directly in the title.
- **Axis labels** – Combine units with dynamic values (e.g., “Revenue (USD) – Q1”).
- **Tooltips** – Provide richer context without hard‑coding text.
