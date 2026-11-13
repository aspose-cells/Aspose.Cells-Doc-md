---
title: Use Aspose CLI with AI Agents
linktitle: AI Agents and Preview
type: docs
weight: 20
url: /cli/ai-agents/
description: "Connect AI agents through bundled Cells Skills or the Aspose CLI MCP server and preview Excel files locally."
keywords: "Aspose.Cells, Excel, spreadsheet automation, AI Agents and Preview"
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Use Aspose CLI with AI Agents

An agent that can run terminal commands can use `aspose-cli cells` directly. Bundled Skills teach it the editing, verification, and delivery workflow. The CLI also provides its own stdio MCP server for MCP clients.

[Install Aspose CLI](/cells/cli/) and check `aspose-cli doctor` before connecting an agent.

## Install the agent Skills

From the project directory, install the shared workflow and the Cells workflow:

```powershell
aspose-cli skill install aspose-cli-platform --host codex
aspose-cli skill install aspose-cli-cells --host codex
```

Use `--host claude-code` or `--host opencode` for those hosts. Add `--user` to install for your user account instead of the current project. The installer may already have installed Skills for detected hosts; `aspose-cli skill list` lists the bundled Skills available to install.

The shared Skill covers command discovery, local files, licensing, and verification. The Cells Skill covers workbook data, formulas, formatting, charts, and spreadsheet-specific checks.

Example request:

> Use Aspose CLI to turn sales.csv into an Excel sales report. Add formula totals, format the headers and amounts, add a product chart, and export a PDF. Check the totals and preview every sheet before delivering the files.

Agents can discover the installed contract without guessing parameters:

```powershell
aspose-cli capabilities cells
aspose-cli schema v2/cells/ops
aspose-cli docs cells/editing
```

## Connect the CLI through MCP

For a client using the `mcpServers` configuration format:

```json
{
  "mcpServers": {
    "aspose-cli": {
      "command": "aspose-cli",
      "args": ["mcp", "serve"]
    }
  }
}
```

The client must be able to find the executable. If its environment does not include the updated PATH, use the full path to `aspose-cli.exe`. Restart the client after changing its configuration. Other hosts may use a different configuration format, but the command remains `aspose-cli mcp serve`.

The CLI MCP server exposes **`capabilities`** and **`execute`**. Let the client discover their input schemas. These are different from the seven spreadsheet tools exposed by [Aspose.Cells MCP for Node.js](/cells/nodejs-cpp/mcp/).

| Integration | Use it when |
| --- | --- |
| CLI commands and Skills | The agent can run terminal commands and should follow the bundled spreadsheet workflow. |
| Aspose CLI MCP | The client uses MCP and should access the CLI's product commands. |
| Node.js Cells MCP | The client should use dedicated workbook tools such as `inspect_workbook` and `apply_workbook_plan`. |

An agent using CLI commands does not also need an MCP server for the same task.

## Preview a workbook locally

```powershell
aspose-cli preview open report.ready.xlsx
```

The command opens the default browser and returns a local browser URL. For automation, add `--no-open --output-format json` to obtain the URL without launching a browser. The service listens on `127.0.0.1`; open it on the machine running the CLI. The initial URL can be redeemed once within five minutes; use `aspose-cli preview status --output-format json` to obtain a fresh URL if needed.

The default workbook view shows a selectable grid and follows changes to the same file, including in-place edits. If rendering a new revision fails, it keeps the last successfully rendered revision visible; check preview errors before treating the view as current.

For a rendered-sheet view:

```powershell
aspose-cli preview open report.ready.xlsx --view sheets
```

To open the local workspace or close all preview sessions:

```powershell
aspose-cli app open --welcome
aspose-cli preview stop
```

Preview helps a person inspect the document; the agent should still read changed ranges, review rendered sheets, and check formula results. See the [complete report example](/cells/cli/spreadsheet-operations/).

## Related resources

- [Aspose CLI source and installation](https://github.com/aspose-cli/aspose-cli)
- [Aspose CLI releases](https://github.com/aspose-cli/aspose-cli/releases)
- [Node.js MCP setup and tools](/cells/nodejs-cpp/mcp/)
- [Excel operations with Aspose CLI](/cells/cli/spreadsheet-operations/)
