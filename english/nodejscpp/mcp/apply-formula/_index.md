---
title: Excel Formulas with MCP
linktitle: Formula Operations
type: docs
weight: 20
url: /nodejs-cpp/mcp/apply-formula
description: "Write and recalculate Excel formulas with set_formulas inside an Aspose.Cells MCP workbook plan."
keywords: "Aspose.Cells, Excel, spreadsheet automation, Formula Operations"
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Excel Formula Operations

The JSON below is an `operations` array for `apply_workbook_plan`, not a list of independent tool calls. Use it with a revision-checked target from [File and Data Operations](/cells/nodejs-cpp/mcp/file-operations/). It assumes the `Sales` sheet from the [quick start](/cells/nodejs-cpp/mcp/) exists.

```json
[
  {
    "id": "line-totals",
    "type": "set_formulas",
    "sheet_name": "Sales",
    "range": "D2:D3",
    "formulas": [
      [
        "=B2*C2"
      ],
      [
        "=B3*C3"
      ]
    ]
  },
  {
    "id": "grand-total",
    "type": "set_formulas",
    "sheet_name": "Sales",
    "range": "D4",
    "formulas": [
      [
        "=SUM(D2:D3)"
      ]
    ]
  }
]
```

Each formula starts with `=`. Supply one formula per cell: the matrix above has two rows for `D2:D3`. Unlike a fill-down command, it does not infer the second formula from the first. Use `$B$2` for an absolute reference and `'Sheet Name'!A1` for a sheet name containing spaces.

The plan recalculates after applying its operations. Put data writes before formulas that depend on them. `set_values` stores a string beginning with `=` as text; use `set_formulas` for calculations.

## Check results

```json
{
  "name": "read_range",
  "arguments": {
    "file_path": "sales.xlsx",
    "sheet_name": "Sales",
    "range": "D2:D4"
  }
}
```

For the original quick-start data, the results should be 2,400, 125, and 2,525. If you changed the quantities, verify the corresponding totals instead. Check formula text, calculated values, and any warnings.

Use `audit_workbook` to investigate calculation errors. Unresolved formulas and external dependencies need review; a successful read or conversion does not certify calculation correctness. See [audit and verification](/cells/nodejs-cpp/mcp/audit-render-and-convert/).
