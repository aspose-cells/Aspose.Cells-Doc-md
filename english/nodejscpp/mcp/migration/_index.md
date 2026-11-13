---
title: Upgrade Aspose.Cells MCP
linktitle: Upgrade from Older Versions
type: docs
weight: 90
url: /nodejs-cpp/mcp/migration/
description: "Migrate old Excel MCP tools to the seven-tool interface and revision-checked workbook plans introduced in 26.10."
keywords: "Aspose.Cells, Excel, spreadsheet automation, Upgrade from Older Versions"
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Upgrade Aspose.Cells MCP

The seven-tool interface introduced in 26.10 replaces the older 25.x tools. Updating the package alone is not sufficient for integrations that send tool calls directly: names, arguments, and editing behavior have changed.

Check the published version on [npm](https://www.npmjs.com/package/aspose.cells.mcp), update the version in your MCP client configuration, restart the server, and refresh the client's tool list. Follow the [current setup instructions](/cells/nodejs-cpp/mcp/).

## Old tools and their replacements

| Older interface | Current approach |
| --- | --- |
| `get_workbook_info`, `read_worksheet` | `inspect_workbook` and bounded `read_range` calls. |
| `read_data_from_excel` | `read_range` with `file_path`, `sheet_name`, and an A1 `range`. |
| `create_workbook` | `apply_workbook_plan` with `target.mode: "create"`. |
| `create_worksheet` | `add_sheet` inside the plan. |
| `write_data_to_excel` | `set_values` inside the plan. |
| `apply_formula`, `apply_formula_batch` | `set_formulas` with an explicit formula matrix. |
| Separate font tools or `cell_format` | `style_range` with an explicit `style.font` or other style properties. |
| Row and column tools | `edit_dimension` with an axis and action. |
| `merge_cells`, `copy_paste_cells`, `clear_cells` | `merge_range`, `copy_range`, and `clear_range` operations. |
| Chart tools | `create_chart`, `update_chart`, and `delete_chart` operations. |
| `pivot_table` | A `pivot` operation with a nested create, update, or delete definition. |
| `excel_converter`, `excel_to_pdf`, `excel_to_csv` | `convert_workbook`; the output extension selects the format. |
| `excel_to_image` | `render_workbook` returning an inline PNG. |

These are migration mappings, not compatibility aliases. Do not send the older tool names to the current server.

## Update editing code

1. Replace old `filepath` arguments with `file_path` or the appropriate target path.
2. Inspect existing inputs and retain their SHA-256 revisions.
3. Combine related writes into one `apply_workbook_plan`, with a unique `id` for each operation.
4. Create worksheets explicitly before using them. Supply rectangular value and formula matrices matching their ranges.
5. Use the current schemas advertised by `tools/list`; do not forward old parameters, style IDs, or presets.
6. Check tool errors and warnings, then verify data and rendered output before delivery.

The [file operations guide](/cells/nodejs-cpp/mcp/file-operations/) shows create, copy, and edit targets. The [audit guide](/cells/nodejs-cpp/mcp/audit-render-and-convert/) explains quality levels and conversion limits.

## MCP and CLI use different contracts

[Aspose CLI for Excel](/cells/cli/) also supports agent workflows, but its `--ops` format is different. For example, CLI uses `op: "set_formula"` and `sheet`, while this Node.js MCP uses `type: "set_formulas"` and `sheet_name` within a plan. Do not pass one product's operation document to the other.
