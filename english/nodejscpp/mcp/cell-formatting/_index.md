---
title: Excel Cell Formatting with MCP
linktitle: Cell Formatting
type: docs
weight: 40
url: /nodejs-cpp/mcp/cell-formatting
description: "Apply explicit Excel fills, borders, alignment, wrapping, and number formats with Aspose.Cells MCP."
keywords: "Aspose.Cells, Excel, spreadsheet automation, Cell Formatting"
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Excel Cell Formatting

The JSON below is an `operations` array for `apply_workbook_plan`, not a list of independent tool calls. Use it with a revision-checked target from [File and Data Operations](/cells/nodejs-cpp/mcp/file-operations/). It assumes the `Sales` sheet from the [quick start](/cells/nodejs-cpp/mcp/) exists.

```json
[
  {
    "id": "header-style",
    "type": "style_range",
    "sheet_name": "Sales",
    "range": "A1:D1",
    "style": {
      "fill_color": "#1F4E78",
      "font": {
        "bold": true,
        "color": "#FFFFFF"
      },
      "horizontal_alignment": "center",
      "vertical_alignment": "center",
      "wrap_text": true,
      "borders": [
        {
          "style": "thin",
          "color": "#D9E2F3",
          "sides": [
            "bottom"
          ]
        }
      ]
    }
  },
  {
    "id": "amount-style",
    "type": "style_range",
    "sheet_name": "Sales",
    "range": "C2:D3",
    "style": {
      "number_format": "#,##0.00",
      "horizontal_alignment": "right"
    }
  }
]
```

| Property | Example |
| --- | --- |
| `fill_color` | `"#1F4E78"` |
| `number_format` | `"#,##0.00"`, `"0.0%"`, or `"yyyy-mm-dd"` |
| `horizontal_alignment` | `"left"`, `"center"`, or `"right"` |
| `vertical_alignment` | `"top"`, `"center"`, or `"bottom"` |
| `wrap_text` | `true` |
| `borders` | An array of border styles, colors, and sides. |

Number formats change display, not the stored type. A numeric-looking string is still text; write a number before applying a numeric format. Dates need an Excel date value or a date-producing formula as well as a date format.

Styles are explicit: there is no `preset` parameter. The default `mode: "preserve"` keeps unrelated formatting; `mode: "replace"` resets it before applying the supplied style.

For readable output, also set column widths and row heights, then [render the result](/cells/nodejs-cpp/mcp/audit-render-and-convert/).
