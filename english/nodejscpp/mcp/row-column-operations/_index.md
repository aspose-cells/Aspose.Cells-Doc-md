---
title: Excel Row and Column Operations with MCP
linktitle: Row and Column Operations
type: docs
weight: 50
url: /nodejs-cpp/mcp/row-column-operations
description: "Insert, delete, resize, auto-fit, and hide Excel rows or columns with edit_dimension operations."
keywords: "Aspose.Cells, Excel, spreadsheet automation, Row and Column Operations"
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Excel Row and Column Operations

The JSON below is an `operations` array for `apply_workbook_plan`, not a list of independent tool calls. Use it with a revision-checked target from [File and Data Operations](/cells/nodejs-cpp/mcp/file-operations/). It assumes the `Sales` sheet from the [quick start](/cells/nodejs-cpp/mcp/) exists.

```json
[
  {
    "id": "column-width",
    "type": "edit_dimension",
    "sheet_name": "Sales",
    "axis": "columns",
    "action": "resize",
    "start": 1,
    "end": 4,
    "size": 18
  },
  {
    "id": "header-height",
    "type": "edit_dimension",
    "sheet_name": "Sales",
    "axis": "rows",
    "action": "resize",
    "start": 1,
    "size": 28
  },
  {
    "id": "fit-data-rows",
    "type": "edit_dimension",
    "sheet_name": "Sales",
    "axis": "rows",
    "action": "autofit",
    "start": 2,
    "end": 3
  }
]
```

Rows and columns use **1-based positions**: column A is 1, B is 2. `end` is inclusive. Column width is measured in characters; row height is measured in points.

| `action` | Fields after `sheet_name` and `axis` |
| --- | --- |
| `insert` | `start`, `count` |
| `delete` | `start`, `count` |
| `resize` | `start`, optional `end`, `size` |
| `autofit` | `start`, optional `end` |
| `set_visibility` | `start`, optional `end`, `hidden` |

Supply only fields relevant to the chosen action. To hide column C, use `axis: "columns"`, `action: "set_visibility"`, `start: 3`, and `hidden: true`. Set `hidden: false` to show it again.

Insertion and deletion change positions used by later operations. Order the batch accordingly, and use the plan's `dry_run: true` before a structural edit. A dry run does not replace the workbook. Read the affected ranges and inspect formulas after the actual edit.

Related: [cell operations](/cells/nodejs-cpp/mcp/cell-operations/) and [visual verification](/cells/nodejs-cpp/mcp/audit-render-and-convert/).
