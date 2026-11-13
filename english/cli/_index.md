---
title: Aspose CLI for Excel
linktitle: Aspose CLI for Excel
type: docs
weight: 65
url: /cli/
is_root: true
description: "Process Excel files locally with Aspose CLI. Install on Windows, create and edit spreadsheets, convert to PDF, and connect AI agents."
keywords: "Aspose.Cells, Excel, spreadsheet automation, Aspose CLI for Excel"
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Aspose CLI for Excel

Use `aspose-cli cells` to create, read, edit, calculate, convert, and render spreadsheets from a terminal or an AI agent. Files are processed locally with Aspose.Cells, without Microsoft Excel.

Aspose CLI also supports other document products; this section focuses on Excel and the **Cells** commands. The supported distribution is **Windows x64**. For the separate Node.js MCP server, see [Aspose.Cells MCP](/cells/nodejs-cpp/mcp/).

## Install

Run the official installer in PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://github.com/aspose-cli/aspose-cli/releases/latest/download/install.ps1 | iex"
```

The installer downloads and verifies the release, installs it for the current user, and adds it to the user PATH. Reopen your terminal, then check the installation:

```powershell
aspose-cli --version
aspose-cli doctor
aspose-cli capabilities cells
```

These examples use the 1.0 command interface. Check the installed version's `--help`, `capabilities`, and `schema` output for its exact options and limits.

Alternatively, download and extract a package from [GitHub Releases](https://github.com/aspose-cli/aspose-cli/releases) and run its `install.ps1`. The installer can install bundled Skills for detected agent hosts; MCP registration is optional. See [AI agents and preview](/cells/cli/ai-agents/).

## Create and export a workbook

Run these commands in a writable working directory. The output filenames must not already exist.

```powershell
aspose-cli cells create sales.xlsx --sheet-names Sales
aspose-cli cells edit sales.xlsx --set "Sales!A1=Product" --set "Sales!B1=Amount" --set "Sales!A2=Laptop" --set "Sales!B2=2400" --out sales.updated.xlsx --verify
aspose-cli cells read sales.updated.xlsx --sheet Sales --range A1:B2
aspose-cli cells convert sales.updated.xlsx --to pdf --out sales.pdf
```

The result is an Excel workbook containing one sale and a PDF export. The original `sales.xlsx` remains available. For formulas, formatting, and a chart, continue with the [complete sales report example](/cells/cli/spreadsheet-operations/).

## Common tasks

| Task | Command |
| --- | --- |
| Discover sheets and workbook structure | `aspose-cli cells inspect book.xlsx` |
| Read a bounded range | `aspose-cli cells read book.xlsx --sheet Sales --range A1:D20` |
| Search workbook text | `aspose-cli cells search book.xlsx --pattern TODO` |
| Apply formulas, styles, charts, or other operations | `aspose-cli cells edit book.xlsx --ops ops.json --out book.updated.xlsx --verify` |
| Compare cell values and formulas | `aspose-cli cells compare book.xlsx book.updated.xlsx` |
| Export PDF | `aspose-cli cells convert book.xlsx --to pdf` |
| Export one sheet to CSV for Excel | `aspose-cli cells convert book.xlsx --to csv --sheets 1 --bom` |
| Render visible worksheets | `aspose-cli cells render book.xlsx --sheets all --out book.png` |
| Generate visual review evidence | `aspose-cli review book.xlsx --out book.review --output-format json` |
| Open a local browser preview | `aspose-cli preview open book.xlsx` |

Use `--output-format json` for scripts and agents. `--sheet` selects a name for reading and searching; `--sheets` selects 1-based sheet positions for conversion and rendering. Inspect the workbook first instead of assuming a position.

Rendering several sheets produces separate files such as `book.Sales.png`, not one combined image. Rendering is limited to 20 sheets per call; use explicit selections for larger workbooks. Check warnings and continuation information for omitted or partially rendered content. PDF pagination follows the workbook's print settings and should be checked separately.

### Editing and verification

Edits recalculate the workbook after the operation batch by default. `--no-recalc` skips that final calculation and cannot be combined with `--verify`; some operations still calculate earlier changes when they need current results. A failed operation aborts the batch without publishing an output unless `--best-effort` is requested. Use `--out` to keep the source, or `--in-place --backup` to replace it with a backup. `--if-match` checks the input fingerprint; `--dry-run` applies the edit in memory without saving and does not guarantee that a later save will succeed.

`--verify` reads the staged output back and reports supported value, formula, and sheet changes. It does not render the workbook or certify formatting, chart appearance, or business totals. Verification findings can produce **exit code 8 with the edited output already written**; check `verification.ok`, findings, warnings, and unchecked operations before delivery. Use `review` and range rendering for visual checks. A review covers visible sheets within its item and rendering limits; it is not a guarantee that every cell was inspected.

Discover operation fields and verification details with:

```powershell
aspose-cli schema v2/cells/ops
aspose-cli docs cells/editing
aspose-cli docs cells/verification
```

### CSV input and fonts

CSV/TSV import preserves ambiguous identifiers and values as text. Use `--encoding` for a non-UTF-8 source and `--culture` when its number or date conventions require it; inspect imported types and warnings before calculations. For example, `aspose-cli cells convert --help` explains the import rules. These rules differ from the Node.js MCP server's text-only CSV/TSV import.

PDF and image output depend on available fonts. Add local fonts with `--font-dir` when needed, and inspect the rendered output for missing glyphs or clipped text.

## License and evaluation

```powershell
aspose-cli license install C:/Licenses/Aspose.Cells.lic
aspose-cli license status --output-format json
```

With no configured license, the commercial Aspose.Cells engine runs in evaluation mode. Outputs may contain evaluation warning sheets, watermarks, or other evaluation changes; the CLI reports these as warnings. An invalid configured license is an error rather than a silent fallback to evaluation. An MIT license for the CLI source does not license the Aspose engines.

For license discovery and supported environment variables, run `aspose-cli docs licensing`. Use `aspose-cli update check` to check for a newer release and `aspose-cli update install` to update it.

## Learn more

- [Excel operations and a complete report](/cells/cli/spreadsheet-operations/)
- [AI agents, MCP, and browser preview](/cells/cli/ai-agents/)
- [Aspose CLI source](https://github.com/aspose-cli/aspose-cli)
- [Downloads and release notes](https://github.com/aspose-cli/aspose-cli/releases)
- [Aspose.Cells MCP for Node.js](/cells/nodejs-cpp/mcp/)
- [Aspose.Cells for .NET](/cells/net/)
- [Aspose.Cells support forum](https://forum.aspose.com/c/cells/9)
