---
title: Excel Charts and Pivot Tables with MCP
linktitle: Charts and Pivot Tables
type: docs
weight: 70
url: /nodejs-cpp/mcp/charts-and-pivot-tables/
description: "Create native Excel charts and pivot tables in an ordered Aspose.Cells MCP workbook plan."
keywords: "Aspose.Cells, Excel, spreadsheet automation, Charts and Pivot Tables"
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Excel Charts and Pivot Tables

The JSON below is an `operations` array for `apply_workbook_plan`, not a list of independent tool calls. Use it with a revision-checked target from [File and Data Operations](/cells/nodejs-cpp/mcp/file-operations/). It assumes the `Sales` sheet from the [quick start](/cells/nodejs-cpp/mcp/) exists.


## Add a sales chart

```json
[
  {
    "id": "sales-chart",
    "type": "create_chart",
    "sheet_name": "Sales",
    "name": "SalesTotals",
    "chart_type": "column",
    "series": [
      {
        "name": "Total",
        "values": "Sales!D2:D3",
        "categories": "Sales!A2:A3"
      }
    ],
    "position": {
      "top_row": 6,
      "left_column": 1,
      "bottom_row": 20,
      "right_column": 8
    },
    "title": "Sales by Product",
    "show_legend": false
  }
]
```

The chart reads the formulas and values created in the quick start. Choose either explicit `series` or `source_range`, not both. Chart positions use 1-based row and column numbers. Use `update_chart` and `delete_chart` for existing charts, after inspecting their names.

## Add a pivot table

```json
[
  {
    "id": "summary-sheet",
    "type": "add_sheet",
    "name": "PivotSummary"
  },
  {
    "id": "product-pivot",
    "type": "pivot",
    "sheet_name": "PivotSummary",
    "operation": {
      "type": "create",
      "name": "SalesByProduct",
      "source": {
        "sheet_name": "Sales",
        "range": "A1:D3"
      },
      "destination": "A1",
      "rows": [
        "Product"
      ],
      "values": [
        {
          "field": "Total",
          "aggregation": "sum"
        }
      ]
    },
    "layout": "tabular",
    "number_format": "#,##0.00"
  }
]
```

Pivot fields use source header names, not numeric column indexes. Write source values and formulas before creating the pivot. The destination sheet must exist, and the output needs empty space.

The nested `operation.type` selects `create`, `update`, or `delete`. Updates supply the full pivot definition; a delete identifies the pivot by name. Do not edit pivot results with `set_values`: change the source and update the pivot instead.

## Inspect the result

Use `inspect_workbook` with `dimensions: ["structure"]` to find the chart and pivot objects. Read the summary cells to verify totals. Render the chart using `render_workbook` with `mode: "chart"`, `sheet_name: "Sales"`, and `chart_name: "SalesTotals"`.

Continue with [audit, rendering, and PDF export](/cells/nodejs-cpp/mcp/audit-render-and-convert/).
