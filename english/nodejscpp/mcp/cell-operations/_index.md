---
title: Merge, Copy, and Clear Excel Cells with MCP
linktitle: Cell Operations
type: docs
weight: 60
url: /nodejs-cpp/mcp/cell-operations
description: "Merge and unmerge ranges, copy cells between sheets, and clear Excel values or formatting with MCP plans."
keywords: "Aspose.Cells, Excel, spreadsheet automation, Cell Operations"
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Excel Cell Operations

The JSON below is an `operations` array for `apply_workbook_plan`, not a list of independent tool calls. Use it with a revision-checked target from [File and Data Operations](/cells/nodejs-cpp/mcp/file-operations/). It assumes the `Sales` sheet from the [quick start](/cells/nodejs-cpp/mcp/) exists.

```json
[
  {
    "id": "copy-data",
    "type": "copy_range",
    "source_sheet_name": "Sales",
    "source_range": "A1:D3",
    "destination_sheet_name": "Sales",
    "destination_start": "F1",
    "mode": "contents_and_formats"
  },
  {
    "id": "clear-copy",
    "type": "clear_range",
    "sheet_name": "Sales",
    "range": "F2:I3",
    "what": "contents"
  },
  {
    "id": "merge-title",
    "type": "merge_range",
    "sheet_name": "Sales",
    "range": "A6:D6"
  },
  {
    "id": "title",
    "type": "set_values",
    "sheet_name": "Sales",
    "range": "A6",
    "values": [
      [
        "Sales Report"
      ]
    ]
  }
]
```

`copy_range` copies within the workbook, including between existing worksheets. `destination_start` is the top-left destination cell. Choose `contents`, `formats`, or `contents_and_formats`.

`clear_range.what` accepts `contents`, `formats`, or `all`. Clearing contents retains formatting; clearing formats retains cell contents.

Merge an empty range or first decide how its existing values should be preserved. Write a merged cell through its top-left cell. Use `unmerge_range` with the same `sheet_name` and `range` to separate it again. Do not merge cells inside an Excel table or write over pivot-table output.

Read copied formulas to confirm their references and render merged titles to check clipping. See [audit, render, and convert](/cells/nodejs-cpp/mcp/audit-render-and-convert/).
