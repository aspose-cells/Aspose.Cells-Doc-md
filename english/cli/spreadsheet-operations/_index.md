---
title: Excel Operations with Aspose CLI
linktitle: Excel Operations
type: docs
weight: 10
url: /cli/spreadsheet-operations/
description: "Build an Excel sales report with formulas, formatting, and a chart, then verify and export it with Aspose CLI."
keywords: "Aspose.Cells, Excel, spreadsheet automation, Excel Operations"
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Excel Operations with Aspose CLI

This example creates a workbook, applies a batch of changes, checks calculated totals, and exports a PDF. [Install Aspose CLI](/cells/cli/) first. Run the commands in a writable directory with unused output filenames.

## Create the workbook

```powershell
aspose-cli cells create report.xlsx --sheet-names Sales
```

## Add data, formulas, and a chart

Save the following JSON as `ops.json` in the same directory:

```json
{
  "ops": [
    {
      "op": "set_values",
      "sheet": "Sales",
      "range": "A1",
      "values": [
        [
          "Product",
          "Quantity",
          "Unit Price",
          "Total"
        ],
        [
          "Laptop",
          2,
          1200,
          null
        ],
        [
          "Mouse",
          5,
          25,
          null
        ]
      ]
    },
    {
      "op": "set_formula",
      "sheet": "Sales",
      "range": "D2:D3",
      "formula": "=B2*C2"
    },
    {
      "op": "format_range",
      "sheet": "Sales",
      "range": "A1:D1",
      "style": {
        "bold": true
      }
    },
    {
      "op": "format_range",
      "sheet": "Sales",
      "range": "C2:D3",
      "style": {
        "numberFormat": "#,##0.00"
      }
    },
    {
      "op": "insert_chart",
      "sheet": "Sales",
      "kind": "column",
      "dataRange": "A1:B3",
      "at": "F2:M16",
      "title": "Quantity by Product"
    },
    {
      "op": "resize_columns",
      "sheet": "Sales",
      "first": "A",
      "last": "D",
      "widthChars": 18
    },
    {
      "op": "freeze_panes",
      "sheet": "Sales",
      "cell": "A2"
    }
  ]
}
```

Apply it to a new output file:

```powershell
aspose-cli cells edit report.xlsx --ops ops.json --out report.ready.xlsx --verify --output-format json
```

`set_values` accepts a matrix starting at `A1`. JSON strings remain text; write numbers as numbers and formulas with `set_formula`. Here `set_formula` fills `D2:D3`, adjusting relative references in the second row, and the workbook recalculates after the batch. The chart plots product quantities.

Use a JSON file for multi-operation edits, especially in PowerShell. This is the CLI `ops` format; it is not the Node.js MCP `operations` format.

## Verify and export

```powershell
aspose-cli cells read report.ready.xlsx --sheet Sales --range D2:D3 --content formulas --output-format json
aspose-cli cells inspect report.ready.xlsx --detail errors --output-format json
aspose-cli cells render report.ready.xlsx --range Sales!A1:M16 --out report.png
aspose-cli cells convert report.ready.xlsx --to pdf --out report.pdf
```

The expected totals are **2,400** and **125**. Inspect `report.png` for clipped text, number formats, and the chart. Check PDF pagination separately; use `set_page_setup` and `set_print_area` if the report must fit a particular printed page. `aspose-cli schema v2/cells/ops --operation set_page_setup` describes its fields.

For a review directory covering visible sheets within the review limits, run:

```powershell
aspose-cli review report.ready.xlsx --out report.review --output-format json
```

Use a new review directory and inspect the generated images, findings, and coverage warnings. Hidden sheets are not reviewed. Large sheets or multiple print areas can be only partially rendered; follow the range-render commands in the warnings to inspect omitted areas. Evaluation outputs also include the engine's evaluation markings.

## Edit an existing workbook

Inspect and read the affected area before editing. For a single-cell update:

```powershell
aspose-cli cells edit report.ready.xlsx --set "Sales!B2=3" --out report.revised.xlsx --verify
aspose-cli cells read report.revised.xlsx --sheet Sales --range D2:D3 --output-format json
aspose-cli cells compare report.ready.xlsx report.revised.xlsx --output-format json
```

The first total should now be **3,600**. `compare` compares stored values and formula text; it does not certify unchanged formatting or chart appearance.

To replace an input deliberately, use `--in-place --backup`. Use `--if-match` with the inspected input's SHA-256 fingerprint to refuse a changed input. `--dry-run` applies a batch in memory without writing files; it does not guarantee a later save will succeed.

`--verify` reports semantic findings. If verification reports issues, the command can exit **8 with the output already written**, including an in-place replacement. Using `--out` as above keeps the source intact so you can review the result before delivery. Without `--best-effort`, a failed edit operation aborts the batch without writing its output.

## Other spreadsheet tasks

| Task | Operations or commands |
| --- | --- |
| Cells and ranges | `set_values`, `set_formula`, `clear_range`, `copy_range` |
| Formatting | `format_range`, `set_borders`, `resize_rows`, `resize_columns` |
| Sheets and workbook structure | `insert_sheet`, `rename_sheet`, `move_sheet`, `delete_sheet` |
| Charts and pivots | `insert_chart`, `set_chart`, `insert_pivot`, `refresh_pivot` |
| Tables and validation | `define_table`, `sort_range`, `set_validation`, `add_conditional_format` |
| Combine workbook content | `import_range`, `import_sheet` |
| Convert CSV to Excel | `aspose-cli cells convert data.csv --to xlsx` |
| Export a sheet to CSV | `aspose-cli cells convert book.xlsx --to csv --sheets 1 --bom` |

Discover the installed version's exact fields before constructing a batch:

```powershell
aspose-cli capabilities cells edit
aspose-cli schema v2/cells/ops --operation insert_chart
aspose-cli docs cells/editing
aspose-cli docs cells/verification
```

CSV exports contain a single sheet's data, without Excel's workbook structure, charts, or formulas. Review conversion warnings for omitted content. `--bom` helps Excel recognize non-English UTF-8 CSV text.

Next: [connect an AI agent and open a live preview](/cells/cli/ai-agents/).
