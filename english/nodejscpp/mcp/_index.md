---
title: Aspose.Cells MCP for Node.js
linktitle: MCP
type: docs
weight: 30
url: /nodejs-cpp/mcp/
description: "Connect an AI assistant to Excel with Aspose.Cells MCP. Inspect, edit, audit, convert, and render local workbooks."
keywords: "Aspose.Cells, Excel, spreadsheet automation, MCP"
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Aspose.Cells MCP for Node.js

Aspose.Cells MCP lets an MCP-compatible AI assistant inspect, create, edit, check, convert, and render local Excel files. It uses Aspose.Cells for Node.js via C++ and does not require Microsoft Excel.

Use it for sales reports, budgets, dashboards, and changes to existing workbooks. The assistant interprets your request; the server performs the spreadsheet operations. For terminal commands, scripts, and CLI-based agents, see [Aspose CLI for Excel](/cells/cli/).

## Install and connect

Install Node.js 20 or newer and create a directory for your workbooks. The native dependency provides packages for Windows x64, Linux x64/ARM64, and macOS x64/ARM64; Node.js must match a supported architecture. Configure an MCP client that uses the `mcpServers` JSON format with a stdio server:

```json
{
  "mcpServers": {
    "aspose-cells": {
      "command": "npx",
      "args": ["--yes", "aspose.cells.mcp@26.10.0"],
      "env": {
        "WORK_DIR": "C:/ExcelWork",
        "LICENSE_PATH": "C:/Licenses/Aspose.Cells.lic"
      }
    }
  }
}
```

Replace the paths with existing directories and your license file. Omit `LICENSE_PATH` to use evaluation mode. The client must be able to find Node.js and `npx`; restart it after changing the configuration.

On Windows, clients that cannot launch `npx` directly can use `"command": "cmd"` and `"args": ["/c", "npx", "--yes", "aspose.cells.mcp@26.10.0"]`, keeping the same `env`. Other clients may use a different configuration format; use their stdio-server settings for the same command and environment.

These examples target the seven-tool 26.10 interface and pin `26.10.0`. Check the published versions and tags before upgrading:

```shell
npm view aspose.cells.mcp dist-tags --json
npm view aspose.cells.mcp@26.10.0 version
```

Do not assume that `latest` and `next` identify the same release. An older 25.x server cannot run these examples. After connecting, confirm that the client lists the seven tools below; use its `tools/list` schemas as the reference for the installed server.

`WORK_DIR` defaults to the server's current directory. All workbook paths must stay within it. Output directories must already exist; parent traversal and symbolic links are rejected.

## Available tools

| Tool | Purpose |
| --- | --- |
| `inspect_workbook` | Discover sheets, structure, presentation, objects, and the file revision. |
| `read_range` | Read a bounded range of values, formulas, display text, and optional formats. |
| `search_workbook` | Find values, formulas, formula errors, comments, hyperlinks, or placeholders. |
| `apply_workbook_plan` | Create, copy, or edit an XLSX/XLSM workbook with one ordered batch of operations. |
| `audit_workbook` | Check workbook integrity, calculations, data validation, and presentation. |
| `convert_workbook` | Save a separate output in the format selected by its extension. |
| `render_workbook` | Return a PNG of a range, printed sheet page, or chart. |

`apply_workbook_plan` is the editing tool. Names such as `set_values`, `set_formulas`, and `style_range` are operations inside its `operations` array, not separate MCP tools. Conversion uses `convert_workbook` and writes a separate file.

Plans support worksheet and range edits, formulas, formatting and borders, tables and appended rows, sorting and filters, charts and sparklines, pivot tables, validation, conditional formatting, defined names, comments, hyperlinks, images, and print setup. The package also bundles workflow Skills for general workbooks, executive dashboards, budgets/forecasts, and operations tracking. Loading Skills depends on the agent host; an MCP connection alone does not install them.

### Formats and imported data

Plan outputs are limited to **XLSX and XLSM**. Use XLSM when editing a workbook with VBA. Conversion supports XLSX, XLSM, XLSB, XLS, ODS, CSV, TSV, PDF, and HTML; the [export guide](/cells/nodejs-cpp/mcp/audit-render-and-convert/) explains sheet selection and overwrite checks.

CSV/TSV input imports every nonempty field as text, preserving leading zeros and long identifiers; empty fields become blank cells. Before calculations, write selected numeric fields as JSON numbers with `set_values`. UTF-8 is supported with or without a BOM, and UTF-16LE/BE requires a BOM. Invalid encoding or malformed quoting is rejected. Existing typed Excel workbooks keep their stored types.

## Create your first report

Ask your assistant:

> Create sales.xlsx with a Sales sheet. Add two laptops at 1,200 each and five mice at 25 each. Calculate totals with formulas, format the header and amounts, and check the results.

For developers, the corresponding MCP `tools/call` parameters are shown below. Each JSON example with `name` and `arguments` uses this convention; it is not a shell command.

```json
{
  "name": "apply_workbook_plan",
  "arguments": {
    "target": {
      "mode": "create",
      "output_path": "sales.xlsx",
      "first_sheet_name": "Sales"
    },
    "operations": [
      {
        "id": "data",
        "type": "set_values",
        "sheet_name": "Sales",
        "range": "A1:C3",
        "values": [
          [
            "Product",
            "Quantity",
            "Unit Price"
          ],
          [
            "Laptop",
            2,
            1200
          ],
          [
            "Mouse",
            5,
            25
          ]
        ]
      },
      {
        "id": "total-header",
        "type": "set_values",
        "sheet_name": "Sales",
        "range": "D1",
        "values": [
          [
            "Total"
          ]
        ]
      },
      {
        "id": "totals",
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
        "id": "header",
        "type": "style_range",
        "sheet_name": "Sales",
        "range": "A1:D1",
        "style": {
          "font": {
            "bold": true,
            "color": "#FFFFFF"
          },
          "fill_color": "#1F4E78"
        }
      },
      {
        "id": "currency",
        "type": "style_range",
        "sheet_name": "Sales",
        "range": "C2:D3",
        "style": {
          "number_format": "#,##0.00"
        }
      },
      {
        "id": "widths",
        "type": "edit_dimension",
        "sheet_name": "Sales",
        "axis": "columns",
        "action": "resize",
        "start": 1,
        "end": 4,
        "size": 18
      }
    ]
  }
}
```

Use a new output name if `sales.xlsx` already exists. Read `Sales!D2:D3` with `read_range`: the expected totals are **2,400** and **125**. Continue with [charts and pivot tables](/cells/nodejs-cpp/mcp/charts-and-pivot-tables/), then [audit, preview, and export the report](/cells/nodejs-cpp/mcp/audit-render-and-convert/).

## Editing workflow

1. Inspect the existing file and retain `revision.sha256` from the result's `data` object.
2. Put dependent changes in one `apply_workbook_plan`. Every operation needs a unique `id`.
3. For an in-place edit, use `target.mode: "edit"` and `expected_sha256`. For a new copy, use `target.mode: "copy"` and `expected_source_sha256`.
4. Use `dry_run: true` to exercise the plan without replacing the target. It still saves and reopens a temporary file for verification, so the output directory must be writable. A normal plan publishes the verified file only if its checks pass.
5. Read changed cells, audit the workbook, and inspect rendered images before delivery. Technical checks do not establish that business totals or assumptions are correct.

The default `quality_level` is `integrity`: it blocks integrity and calculation errors, but reports data-validation violations without blocking solely on those violations. Use `standard` to enforce data-validation errors and include presentation checks, or `strict` to also block findings marked as delivery-blocking. See [quality levels and verification](/cells/nodejs-cpp/mcp/audit-render-and-convert/).

Check calculation warnings even when a call succeeds. Successful reads and exports can contain unresolved or cached formula results. Follow `read_range.next_range` using the previous response's `revision.sha256` as `expected_sha256`; the same revision check is available for search and rendering. It identifies source file bytes, not a shared calculation snapshot for volatile formulas.

`render_workbook` returns one inline PNG per call. Both a range and a printed sheet can span pages: follow `next_page` and inspect `rendered_range` where present instead of assuming that the first image covers the whole request.

## Guides

- [File and data operations](/cells/nodejs-cpp/mcp/file-operations/)
- [Formulas](/cells/nodejs-cpp/mcp/apply-formula/)
- [Font and text formatting](/cells/nodejs-cpp/mcp/font-formatting/)
- [Cell formatting](/cells/nodejs-cpp/mcp/cell-formatting/)
- [Rows and columns](/cells/nodejs-cpp/mcp/row-column-operations/)
- [Merge, copy, and clear cells](/cells/nodejs-cpp/mcp/cell-operations/)
- [Charts and pivot tables](/cells/nodejs-cpp/mcp/charts-and-pivot-tables/)
- [Audit, render, and convert](/cells/nodejs-cpp/mcp/audit-render-and-convert/)
- [Upgrade from older MCP versions](/cells/nodejs-cpp/mcp/migration/)

## Licensing and limits

The MCP server code is MIT-licensed; the Aspose.Cells engine has its own commercial license. Without a license, each save adds an evaluation warning worksheet and rendered output may contain a watermark. Evaluation mode allows at most 100 workbook loads per server process; a tool call can load more than one workbook. After the limit is reached, restart the server or configure a valid license and restart it. Check startup diagnostics and result warnings if `LICENSE_PATH` cannot be loaded.

Plans accept at most 100 operations and must fit the 250,000-instantiated-cell workbook budget, object budgets, and required audit coverage. This counts the resulting workbook, not just changed cells. Split large workloads into separate workbooks or reduce their size. Larger files can still be inspected, read, searched, rendered, or converted within those tools' individual limits; check partial-coverage and calculation warnings. Reads return at most 2,000 cells per response and may be shortened further by the response-size budget.

Rendering depends on fonts installed on the server machine. Missing glyphs or a successful save do not prove a visually correct result.

## Related resources

- [Aspose.Cells MCP on npm](https://www.npmjs.com/package/aspose.cells.mcp)
- [Aspose.Cells for Node.js via C++ documentation](/cells/nodejs-cpp/)
- [Aspose CLI for Excel](/cells/cli/)
- [Temporary license](https://purchase.aspose.com/temporary-license/)
- [Aspose.Cells support forum](https://forum.aspose.com/c/cells/9)

{{< app/cells/assistant language="nodejs-cpp" >}}
