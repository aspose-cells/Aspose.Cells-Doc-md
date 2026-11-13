---
title: Excel Font and Text Formatting with MCP
linktitle: Font and Text Formatting
type: docs
weight: 30
url: /nodejs-cpp/mcp/font-formatting
description: "Set Excel font names, sizes, colors, bold, italic, and underline with explicit MCP styles."
keywords: "Aspose.Cells, Excel, spreadsheet automation, Font and Text Formatting"
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Excel Font and Text Formatting

The JSON below is an `operations` array for `apply_workbook_plan`, not a list of independent tool calls. Use it with a revision-checked target from [File and Data Operations](/cells/nodejs-cpp/mcp/file-operations/). It assumes the `Sales` sheet from the [quick start](/cells/nodejs-cpp/mcp/) exists.

```json
[
  {
    "id": "header-font",
    "type": "style_range",
    "sheet_name": "Sales",
    "range": "A1:D1",
    "style": {
      "font": {
        "name": "Arial",
        "size": 12,
        "bold": true,
        "color": "#FFFFFF"
      }
    }
  },
  {
    "id": "product-font",
    "type": "style_range",
    "sheet_name": "Sales",
    "range": "A2:A3",
    "style": {
      "font": {
        "name": "Arial",
        "size": 11,
        "italic": true
      }
    }
  }
]
```

`style_range.style.font` accepts `name`, `size`, `bold`, `italic`, `underline`, and `color`. Colors use `#RRGGBB`, such as `#1F4E78`. Set a boolean to `false` to explicitly remove that font effect.

The default `mode: "preserve"` changes the requested properties while keeping other formatting. Use `mode: "replace"` only when you intend to reset the existing style before applying the new one.

Fonts used for rendering must be installed on the machine running the server. For multilingual workbooks, choose a font containing the required glyphs and inspect the PNG output. Changing a font does not automatically make every row or column fit; use [row and column sizing](/cells/nodejs-cpp/mcp/row-column-operations/).

See [cell formatting](/cells/nodejs-cpp/mcp/cell-formatting/) for fills, borders, alignment, and wrapping.
