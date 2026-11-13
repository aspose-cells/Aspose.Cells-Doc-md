---
title: Excel File and Data Operations with MCP
linktitle: File and Data Operations
type: docs
weight: 10
url: /nodejs-cpp/mcp/file-operations
description: "Inspect Excel files, read ranges, search data, and create or edit workbooks with revision-aware MCP plans."
keywords: "Aspose.Cells, Excel, spreadsheet automation, File and Data Operations"
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Excel File and Data Operations

Use `inspect_workbook`, `read_range`, and `search_workbook` to discover data. Use `apply_workbook_plan` to create or edit a workbook. See [installation and the complete creation example](/cells/nodejs-cpp/mcp/).

## Inspect a workbook

```json
{
  "name": "inspect_workbook",
  "arguments": {
    "file_path": "sales.xlsx",
    "dimensions": [
      "summary",
      "structure"
    ]
  }
}
```

Successful results contain `ok`, `data`, and `warnings`. Keep `data.revision.sha256` for subsequent edits. Inspect structure before referring to sheets, charts, or pivot tables by name. Follow inspection pagination when the workbook has more sheets or objects than one response can include.

## Read and search

```json
{
  "name": "read_range",
  "arguments": {
    "file_path": "sales.xlsx",
    "sheet_name": "Sales",
    "range": "A1:D3",
    "include_formats": true
  }
}
```

If the result includes `next_range`, read that range next. Pass the previous response's `revision.sha256` as `expected_sha256` to detect a file change between pages.

```json
{
  "name": "search_workbook",
  "arguments": {
    "file_path": "sales.xlsx",
    "sheet_name": "Sales",
    "query": "Laptop",
    "target": "values"
  }
}
```

Use explicit ranges to narrow large searches. A response can be truncated; check the result metadata before drawing conclusions.

## Edit an existing workbook

Replace `REPLACE_WITH_REVISION_SHA256` below with the actual 64-character hash returned by inspection. This example updates a quantity and its dependent formula in the same transaction.

```json
{
  "name": "apply_workbook_plan",
  "arguments": {
    "target": {
      "mode": "edit",
      "file_path": "sales.xlsx",
      "expected_sha256": "REPLACE_WITH_REVISION_SHA256"
    },
    "operations": [
      {
        "id": "quantity",
        "type": "set_values",
        "sheet_name": "Sales",
        "range": "B2",
        "values": [
          [
            3
          ]
        ]
      },
      {
        "id": "total",
        "type": "set_formulas",
        "sheet_name": "Sales",
        "range": "D2",
        "formulas": [
          [
            "=B2*C2"
          ]
        ]
      }
    ]
  }
}
```

A changed input returns `CONFLICT`; inspect it again and reconsider the edit. Do not generate a hash or reuse one from a different file. After a successful plan, its `result_revision.sha256` identifies the new file revision.

## Choose a target

| `target.mode` | Required target fields | Result |
| --- | --- | --- |
| `create` | `output_path`, `first_sheet_name` | Create a new XLSX/XLSM workbook. |
| `copy` | `source_path`, `output_path`, `expected_source_sha256` | Edit a copy while keeping the source. |
| `edit` | `file_path`, `expected_sha256` | Replace the inspected workbook after verification. |

For `create` and `copy`, replacing an existing output requires both `overwrite: true` and `expected_output_sha256` for that output. Prefer a new filename for a first attempt. Other formats can be handled with [conversion](/cells/nodejs-cpp/mcp/audit-render-and-convert/).

## Add a worksheet and write values

The following is an `operations` array. Put it inside the `arguments` of an `apply_workbook_plan` call, alongside a target as above. The same convention applies to operation arrays in the other guides.

```json
[
  {
    "id": "add-summary",
    "type": "add_sheet",
    "name": "Summary"
  },
  {
    "id": "summary-values",
    "type": "set_values",
    "sheet_name": "Summary",
    "range": "A1:B2",
    "values": [
      [
        "Metric",
        "Amount"
      ],
      [
        "Sales Total",
        null
      ]
    ]
  },
  {
    "id": "summary-total",
    "type": "set_formulas",
    "sheet_name": "Summary",
    "range": "B2",
    "formulas": [["=SUM(Sales!D2:D3)"]]
  }
]
```

Worksheets are never created implicitly. Add a sheet before writing to it. `values` and `formulas` are rectangular matrices matching the specified range. JSON numbers and booleans retain their types; strings remain text. The summary formula keeps the total linked to the Sales sheet.

CSV/TSV input fields are read as text, preserving identifiers and leading zeros. Convert to XLSX, then write explicitly selected numeric fields as JSON numbers before calculations.

Next: [formulas](/cells/nodejs-cpp/mcp/apply-formula/) and [cell formatting](/cells/nodejs-cpp/mcp/cell-formatting/).
