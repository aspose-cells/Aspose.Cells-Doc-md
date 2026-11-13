---
title: AI-powered Features
type: docs
weight: 200
url: /net/ai-powered-features/
keywords: AI,spreadsheet,AI features,AI power,Excel AI,OpenAI,Anthropic,Aspose.LLM,Cells AI,IChatClient.
description: This article is a step-by-step guide to using AI-powered features for processing spreadsheet files with Aspose.Cells.AI.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


# AI-powered Features

Aspose.Cells.AI brings large language models (LLMs) into spreadsheet workflows. You can summarize a
workbook, ask questions about its data, inspect it for problems, explain or generate formulas, edit
it, compare two versions, or route a natural-language request to the right operation automatically.

The library works with OpenAI, Anthropic, Aspose.LLM local models, and any provider that implements
`Microsoft.Extensions.AI.IChatClient`, including Azure OpenAI, Gemini, DeepSeek, Bedrock, and
self-hosted gateways.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Install the Package](#install-the-package)
3. [Configure a Model](#configure-a-model)
4. [Create a Cells AI Instance](#create-a-cells-ai-instance)
5. [Process Workbooks with AI](#process-workbooks-with-ai)
6. [Route a Natural-Language Request](#route-a-natural-language-request)
7. [Control What the Model Can See](#control-what-the-model-can-see)
8. [Results, Usage, and Warnings](#results-usage-and-warnings)
9. [Proxy Settings](#proxy-settings)
10. [Error Handling](#error-handling)
11. [Requirements](#requirements)

---

## Prerequisites

Before using Cells AI, ensure that you have:

- .NET 8.0 or later.
- An API key and model id for an LLM provider (OpenAI, Anthropic, or an OpenAI-compatible service),
  or an `IChatClient` implementation for another provider.
- A valid Aspose.Cells license for production use. Without one, the output carries the evaluation
  watermark.
- For Aspose.LLM local inference, a separate temporary or commercial Aspose.LLM license and the
  local model runtime. An Aspose.Cells license does not cover Aspose.LLM.

## Install the Package

Install `Aspose.Cells.AI` from NuGet:

```powershell
dotnet add package Aspose.Cells.AI
```

`Aspose.Cells.AI` targets .NET 8.0 and depends on `Aspose.Cells`. Aspose.LLM is intentionally not a
dependency: applications that do not need local inference do not ship its native runtime, model
files, or license.

## Configure a Model

### OpenAI

```csharp
using Aspose.Cells.AI;

using var ai = CellsAI.CreateOpenAI(
    modelId: "gpt-4o-mini",
    apiKey: Environment.GetEnvironmentVariable("OPENAI_API_KEY")!);
```

`endpoint` is optional and defaults to `https://api.openai.com/v1/`. It expects an absolute base URI:

```csharp
using var ai = CellsAI.CreateOpenAI(
    modelId: "gpt-4o-mini",
    apiKey: Environment.GetEnvironmentVariable("OPENAI_API_KEY")!,
    endpoint: new Uri("https://llm.example.com/v1"));
```

### Anthropic

```csharp
using var ai = CellsAI.CreateAnthropic(
    modelId: Environment.GetEnvironmentVariable("ANTHROPIC_MODEL")!,
    apiKey: Environment.GetEnvironmentVariable("ANTHROPIC_API_KEY")!);
```

### Any OpenAI-Compatible Endpoint

`CreateOpenAI` also works with providers that expose an OpenAI-compatible chat completions API. Pass
the base URI; `/chat/completions` is appended when needed, or pass the full chat completions URL.

```csharp
// DeepSeek
using var ai = CellsAI.CreateOpenAI(
    modelId: "deepseek-chat",
    apiKey: Environment.GetEnvironmentVariable("DEEPSEEK_API_KEY")!,
    endpoint: new Uri("https://api.deepseek.com/v1"));

// Gemini via its OpenAI-compatible endpoint
using var gemini = CellsAI.CreateOpenAI(
    modelId: "gemini-2.0-flash",
    apiKey: Environment.GetEnvironmentVariable("GEMINI_API_KEY")!,
    endpoint: new Uri(
        "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"));
```

### Any Other Provider via IChatClient

`CellsAI` only depends on the standard `Microsoft.Extensions.AI.IChatClient`. For providers not
covered by `CreateOpenAI` or `CreateAnthropic` (Azure OpenAI, Bedrock, a custom gateway, ...), use
that provider's `IChatClient` adapter, or write a small one, and pass it in:

```csharp
using Microsoft.Extensions.AI;

using IChatClient chatClient = CreateMyChatClient();
using var ai = new CellsAI(chatClient);
```

The constructor borrows the client, and the caller remains responsible for disposing it. Use
`CellsAI.CreateBuilder().UseOwnedChatClientFactory(...)` when `CellsAI` should own the client
instead.

### Aspose.LLM (Local Inference)

Aspose.LLM runs a model inside your process. It is intentionally not part of the
`Aspose.Cells.AI` package, so applications that do not need local inference do not ship its native
runtime, model files, or license.

Aspose.LLM does not run inference in evaluation mode. It requires its own temporary or commercial
Aspose.LLM license; an Aspose.Cells license does not cover it.

1. Install the package and set both licenses:

```powershell
dotnet add package Aspose.LLM
```

```csharp
using System;
using Aspose.Cells.AI;
using Aspose.LLM.Abstractions.Parameters.Presets;

new Aspose.Cells.License().SetLicense(
    Environment.GetEnvironmentVariable("ASPOSE_CELLS_LICENSE")!);

new Aspose.LLM.License().SetLicense(
    Environment.GetEnvironmentVariable("ASPOSE_LLM_LICENSE")!);
```

2. Add the adapter class below to your application. It is sample code, not part of the
   `Aspose.Cells.AI` package, and is the only place that references Aspose.LLM. Change
   `YourApplication.AI` to your project's namespace.

`AsposeLLMChatClient.cs`

```csharp
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using Aspose.LLM;
using Aspose.LLM.Abstractions.Parameters.Presets;
using Microsoft.Extensions.AI;
using CacheCleanupStrategy = Aspose.LLM.Abstractions.Models.CacheCleanupStrategy;

namespace YourApplication.AI;

internal sealed class AsposeLLMChatClient : IChatClient
{
    private readonly AsposeLLMApi _api;
    private readonly SemaphoreSlim _gate = new(1, 1);
    private string? _sessionId;

    public AsposeLLMChatClient(PresetCoreBase preset) =>
        _api = AsposeLLMApi.Create(preset);

    public async Task<ChatResponse> GetResponseAsync(
        IEnumerable<ChatMessage> messages,
        ChatOptions? options = null,
        CancellationToken cancellationToken = default)
    {
        ArgumentNullException.ThrowIfNull(messages);

        if (options is not null)
            throw new NotSupportedException(
                "This adapter does not support per-request ChatOptions.");

        var prompt = new StringBuilder();
        foreach (ChatMessage message in messages)
        {
            if (message.Role != ChatRole.System &&
                message.Role != ChatRole.User &&
                message.Role != ChatRole.Assistant)
            {
                throw new NotSupportedException(
                    $"Unsupported chat role: {message.Role}.");
            }

            foreach (AIContent content in message.Contents)
            {
                if (content is not TextContent)
                    throw new NotSupportedException("Text content only.");
            }

            prompt.Append('[').Append(message.Role.Value).AppendLine("]")
                .AppendLine(message.Text);
        }

        await _gate.WaitAsync(cancellationToken);
        try
        {
            _sessionId ??= await _api.StartNewChatAsync();
            string text = await _api.SendMessageToSessionAsync(
                _sessionId, prompt.ToString(), null, cancellationToken);
            return new ChatResponse(new ChatMessage(ChatRole.Assistant, text));
        }
        finally
        {
            if (_sessionId is not null)
                _api.ForceCacheCleanup(CacheCleanupStrategy.KeepSystemPromptOnly);
            _gate.Release();
        }
    }

    public IAsyncEnumerable<ChatResponseUpdate> GetStreamingResponseAsync(
        IEnumerable<ChatMessage> messages,
        ChatOptions? options = null,
        CancellationToken cancellationToken = default)
        => throw new NotSupportedException("Cells AI does not use streaming.");

    public object? GetService(Type serviceType, object? serviceKey = null)
        => serviceKey is null && serviceType.IsInstanceOfType(this) ? this : null;

    public void Dispose()
    {
        _api.Dispose();
        _gate.Dispose();
    }
}
```

This adapter implements what Cells AI calls (`GetResponseAsync` and `Dispose`) and fails fast on
unsupported roles, content, and `ChatOptions`. Cells AI does not require streaming, so
`GetStreamingResponseAsync` throws; implement it if you reuse the adapter elsewhere.

3. Build the client with a preset:

```csharp
using Aspose.Cells.AI;
using Aspose.LLM.Abstractions.Parameters.Presets;
using YourApplication.AI;

using var ai = CellsAI.CreateBuilder()
    .UseOwnedChatClientFactory(
        () => new AsposeLLMChatClient(new Qwen25Preset()))
    .Build();
```

Business calls are identical to cloud providers:

```csharp
WorkbookAnswerResult result = await ai.AskAsync(
    workbook,
    "What is the total revenue?");
```

Aspose.LLM allows one active engine per process. The sample adapter serializes inference and keeps
each Cells operation isolated. Switch local models by disposing the old `CellsAI` instance after
in-flight calls finish, then creating a new one.

## Create a Cells AI Instance

`CellsAI` is a long-lived, reusable object. Create one instance per provider, model, and credential
configuration at application startup, and pass it to your business methods. Do not create a new
instance for every workbook.

```csharp
using Aspose.Cells;
using Aspose.Cells.AI;

using var ai = CellsAI.CreateOpenAI(
    modelId: Environment.GetEnvironmentVariable("CELLSAI_OPENAI_MODEL")!,
    apiKey: Environment.GetEnvironmentVariable("CELLSAI_OPENAI_API_KEY")!,
    endpoint: new Uri(
        Environment.GetEnvironmentVariable("CELLSAI_OPENAI_ENDPOINT")!));

using var workbook = new Workbook("Sales.xlsx");

WorkbookSummaryResult summary = await ai.SummarizeAsync(workbook);
Console.WriteLine(summary.Summary);
```

The same `CellsAI` instance can be used concurrently for unrelated workbooks. A single `Workbook`
must not be used by two calls at the same time unless you synchronize access yourself.

## Process Workbooks with AI

Every `CellsAIResult` exposes `Warnings`, `Usage`, `Operation`, and `Text`.
`Text` is a human-readable answer you can display directly, and `Operation` identifies the
operation that produced it, so you rarely need to inspect the concrete result type. Collections are
never `null`; they are empty when there is nothing to report. `ToString()` returns the same text as
`Text`.

| Operation | Method | Result |
|---|---|---|
| Summarize | `SummarizeAsync` | `WorkbookSummaryResult` |
| Ask | `AskAsync` | `WorkbookAnswerResult` |
| Inspect | `InspectAsync` | `WorkbookInspectionResult` |
| Explain formula | `ExplainFormulaAsync` | `FormulaExplanationResult` |
| Generate formula | `GenerateFormulaAsync` | `FormulaGenerationResult` |
| Edit | `EditAsync` | `WorkbookEditResult` |
| Compare (summary) | `CompareAsync` | `WorkbookComparisonResult` |
| Compare (colored workbook) | `GenerateComparisonWorkbookAsync` | `Workbook` |
| Route a request | `ProcessAsync` | `CellsAIResult` (concrete subtype) |

### Summarize a Workbook

```csharp
WorkbookSummaryResult result = await ai.SummarizeAsync(workbook);

Console.WriteLine(result.Summary);

foreach (string point in result.KeyPoints)
{
    Console.WriteLine($"- {point}");
}

foreach (WorkbookCitation citation in result.Citations)
{
    Console.WriteLine(citation.Location.Reference);
}
```

Limit the readable scope to a table:

```csharp
var options = new WorkbookContentOptions(
    WorkbookLocation.FromTable("Sales", "Orders"));

WorkbookSummaryResult result = await ai.SummarizeAsync(workbook, options);
```

### Ask Questions About a Workbook

```csharp
WorkbookAnswerResult result = await ai.AskAsync(
    workbook,
    "Which region grew fastest last quarter?");

Console.WriteLine(result.Answer);
```

`AskAsync` answers against one workbook or an explicit range. It keeps no conversation history;
each call is independent. Requests and answers can be written in any language; no separate locale
option is needed.

### Inspect for Problems

Inspection is deterministic and runs locally against the workbook structure and formulas. It does
not call the model.

```csharp
WorkbookInspectionResult result = await ai.InspectAsync(workbook);

foreach (WorkbookFinding finding in result.Findings)
{
    string location = finding.Location?.Reference ?? "(workbook)";
    Console.WriteLine(
        $"{finding.Code} [{finding.Severity}] {location}: {finding.Message}");
}
```

Stable finding codes include `FORMULA_ERROR`, `INCONSISTENT_FORMULA`, `HARDCODED_VALUE`, `OUTLIER`,
`MISSING_VALUE`, `STRUCTURE_ISSUE`, `EXTERNAL_LINK`, and `RISKY_FORMULA`.

Limit the categories with `WorkbookInspectionOptions.Scope`:

```csharp
var options = new WorkbookInspectionOptions
{
    Scope = WorkbookInspectionScope.Formulas | WorkbookInspectionScope.Data
};

WorkbookInspectionResult result = await ai.InspectAsync(workbook, options);
```

### Explain a Formula

```csharp
Cell formulaCell = workbook.Worksheets["Forecast"].Cells["F12"];

FormulaExplanationResult result =
    await ai.ExplainFormulaAsync(formulaCell);

Console.WriteLine(result.Formula);
Console.WriteLine(result.Explanation);

foreach (WorkbookCitation dependency in result.Dependencies)
{
    Console.WriteLine(dependency.Location.Reference);
}
```

The target cell must contain a formula. Its cell is always included in the model context. Hidden
dependencies are only disclosed when `IncludeHiddenContent = true`.

### Generate a Formula

```csharp
Cell targetCell = workbook.Worksheets["Forecast"].Cells["F12"];

FormulaGenerationResult result = await ai.GenerateFormulaAsync(
    targetCell,
    "Calculate gross margin from Revenue and Cost.");

Console.WriteLine(result.Formula);
Console.WriteLine(result.Explanation);
```

Generation does not modify the workbook. Only formulas that pass the Aspose.Cells parser are
returned. The generated formula may reference visible cells in the target worksheet or explicitly
authorized locations; otherwise the operation fails with `ContentAccessDenied`.

### Edit a Workbook

`EditAsync` never modifies the input workbook. It edits a copy and returns it. Writable locations
are an explicit safety boundary chosen by your code, never by the model. Within those locations,
edits can set text, numeric, or Boolean cell values, write formulas, and apply formatting.

```csharp
var options = new WorkbookEditOptions(
    WorkbookLocation.FromTable("Sales", "Orders"));

options.ContextLocations.Add(
    WorkbookLocation.FromRange("Sales", "A1:H200"));

using WorkbookEditResult result = await ai.EditAsync(
    workbook,
    "Add a Total column using a validated formula.",
    options);

foreach (WorkbookChange change in result.Changes)
{
    Console.WriteLine(
        $"{change.Kind}: {change.Location.Reference} - {change.Description}");
}

result.UpdatedWorkbook.Save("Sales.updated.xlsx");
```

`WorkbookEditResult` owns `UpdatedWorkbook`; disposing the result also disposes the workbook. Save
the new workbook to accept the edit.

Highlighting is normal formatting, so it also uses `EditAsync`; there is no separate
`HighlightAsync`. When the rule should recalculate as data changes, ask for native conditional
formatting:

```csharp
var options = new WorkbookEditOptions(
    WorkbookLocation.FromTable("Sales", "Orders"));

using WorkbookEditResult result = await ai.EditAsync(
    workbook,
    "In the Orders table, add conditional formatting: when Actual is less than Target, "
        + "fill only the matching data rows (excluding the header and totals) with "
        + "light red #FCE8E6 and dark red text #B3261E. The highlight must update "
        + "automatically when data changes.",
    options);

result.UpdatedWorkbook.Save("Sales.highlighted.xlsx");
```

If you only want a one-time snapshot highlight, state that explicitly and do not request
conditional formatting.

Charts, pictures, shapes, and pivot tables are not sent to the model in v1. An edit request that
targets one of these objects fails with `CellsAIException(UnsupportedCapability)` before the model
is called; use the Aspose.Cells object model directly for those changes.

### Compare Two Workbooks

Summarize the differences:

```csharp
using var before = new Workbook("Sales-Previous.xlsx");
using var after = new Workbook("Sales-Current.xlsx");

WorkbookComparisonResult result =
    await ai.CompareAsync(before, after);

Console.WriteLine(result.Summary);

foreach (WorkbookDifference difference in result.Differences)
{
    WorkbookLocation? location =
        difference.AfterLocation ?? difference.BeforeLocation;

    Console.WriteLine(
        $"{difference.Kind}: {location?.Reference ?? "(workbook)"}");
}
```

Added content has a `null` `BeforeLocation`; removed content has a `null` `AfterLocation`. Values,
formulas, formatting, worksheets, tables, and defined names are compared. Restrict the comparison
with `WorkbookComparisonOptions.Locations`, `Dimensions`, and `IncludeHiddenContent`.

Generate a marked-up workbook the way document comparison tools do:

```csharp
using Workbook comparison =
    await ai.GenerateComparisonWorkbookAsync(before, after);

comparison.Save("Sales.comparison.xlsx");
```

The returned workbook is a copy of `after` with visual markup:

- **Inserted content** is shown in blue.
- **Deleted content** is shown in red at its original location.
- **Changed values** show the new value in blue followed by the old value in red in the same cell.
- **Formatting-only changes** leave the text unchanged but colored green.

## Route a Natural-Language Request

`ProcessAsync` classifies a request and dispatches it to one of the operations above. The caller
never chooses the operation, and does not need to switch on the result type to display the answer:

```csharp
CellsAIResult result = await ai.ProcessAsync(
    workbook,
    "Check this sheet for problems");

Console.WriteLine(result.Text);
Console.WriteLine(result.Operation); // Inspect
```

`Text` is for display. Structured data stays on the concrete result type, so cast only when you need
it:

```csharp
if (result is WorkbookInspectionResult inspection)
{
    foreach (WorkbookFinding finding in inspection.Findings)
    {
        Console.WriteLine($"{finding.Code} [{finding.Severity}]: {finding.Message}");
    }
}
```

`WorkbookEditResult.Text` summarizes the applied changes. The edited workbook is available through
`UpdatedWorkbook`, and the result still owns it:

```csharp
if (result is WorkbookEditResult edit)
{
    using (edit)
    {
        edit.UpdatedWorkbook.Save("Sales.updated.xlsx");
    }
}
```

Two workbooks enable comparison routing:

```csharp
CellsAIResult result = await ai.ProcessAsync(
    new[] { before, after },
    "Compare these two versions");
```

Routing does not relax safety boundaries. Edit requests still require writable locations, and the
classifier only sees worksheet names, table names, and the request text, never workbook content.

```csharp
var routerOptions = new WorkbookRouterOptions
{
    AllowedOperations = new[]
    {
        WorkbookOperationKind.Summarize,
        WorkbookOperationKind.Ask,
        WorkbookOperationKind.Inspect,
        WorkbookOperationKind.Edit
    },
    FailOnAmbiguous = true
};

routerOptions.WritableLocations.Add(
    WorkbookLocation.FromRange("Sales", "D2:D200"));

CellsAIResult result = await ai.ProcessAsync(
    workbook,
    "Add a ranking column",
    routerOptions);

Console.WriteLine(result.Text);
```

If an edit is routed but `WritableLocations` is empty, `ProcessAsync` throws `ArgumentException`.
Combined or chained requests are not supported in a single call: they fall back to an answer unless
`FailOnAmbiguous = true`, in which case they throw `CellsAIException` with `AmbiguousRequest`.

## Control What the Model Can See

`WorkbookLocation` is a structured value object for worksheets, cells, ranges, tables, and defined
names. Locations are validated before any content is sent to the model.

```csharp
WorkbookLocation sheet = WorkbookLocation.FromWorksheet("Sales");
WorkbookLocation cell = WorkbookLocation.FromCell("Sales", "C4");
WorkbookLocation range = WorkbookLocation.FromRange("Sales", "A1:H200");
WorkbookLocation table = WorkbookLocation.FromTable("Sales", "Orders");
WorkbookLocation name = WorkbookLocation.FromDefinedName("TaxRate");
WorkbookLocation localName = WorkbookLocation.FromDefinedName("Sales", "TaxRate");
```

Read operations accept locations through their options:

```csharp
var options = new WorkbookContentOptions(
    WorkbookLocation.FromRange("Sales", "A1:H200"),
    WorkbookLocation.FromTable("Sales", "Orders"));
```

Hidden worksheets, rows, and columns, and filtered rows are not disclosed by default. Set
`IncludeHiddenContent = true` only when the operation is allowed to read them:

```csharp
var options = new WorkbookContentOptions
{
    IncludeHiddenContent = true
};
```

For edits, `WritableLocations` is the write boundary and `ContextLocations` is read-only context.
Grant only what the request needs.

## Results, Usage, and Warnings

Every result exposes `Text` and `Operation`, so a caller can display a result without pattern
matching:

```csharp
Console.WriteLine(result.Text);
Console.WriteLine(result.Operation);
```

`Text` is never `null`. It is empty when the operation produced no displayable content, for example
when `InspectAsync` finds no problems or `CompareAsync` finds no differences.

Usage and warnings are available on every result:

```csharp
Console.WriteLine(result.Usage.ProviderName);
Console.WriteLine(result.Usage.ModelId);
Console.WriteLine(result.Usage.InputTokenCount);
Console.WriteLine(result.Usage.OutputTokenCount);
Console.WriteLine(result.Usage.Duration);

foreach (CellsAIWarning warning in result.Warnings)
{
    Console.WriteLine($"{warning.Code}: {warning.Message}");
}
```

Token counts and model ids are `null` when the provider does not report them; they are never
fabricated.

## Proxy Settings

If you are behind a proxy, the built-in clients use `HttpClient`'s default proxy, which honors
system proxy settings and the `HTTP_PROXY` / `HTTPS_PROXY` environment variables:

```powershell
$env:HTTP_PROXY  = "http://127.0.0.1:7890"   # replace with your proxy port
$env:HTTPS_PROXY = "http://127.0.0.1:7890"
```

You can also set the process-wide default proxy before creating the `CellsAI` instance:

```csharp
using System.Net;

HttpClient.DefaultProxy = new WebProxy("http://127.0.0.1:58591")
{
    BypassProxyOnLocal = false,
    UseDefaultCredentials = false
};
```

There is no `CellsAI.Proxy` property in vNext. For full control, create an `IChatClient` backed by
an `HttpClient` with your own proxy and pass it to `new CellsAI(chatClient)`.

## Error Handling

All operation failures use `CellsAIException` with a stable `CellsAIErrorCode`:

```csharp
try
{
    WorkbookSummaryResult result = await ai.SummarizeAsync(workbook);
}
catch (CellsAIException ex)
{
    Console.WriteLine(ex.ErrorCode);

    if (ex.ErrorCode == CellsAIErrorCode.ContentTooLarge)
    {
        Console.WriteLine(ex.ContentLimitKind);
        Console.WriteLine($"{ex.ObservedValue} / {ex.LimitValue}");
    }
}
```

| Error code | Meaning |
|---|---|
| `InvalidLocation` | The location does not exist, belongs to another workbook, or has the wrong type. |
| `ContentAccessDenied` | The operation needs hidden or unauthorized content. |
| `ContentTooLarge` | The content exceeds a field, serialized-size, cell-count, or token limit. |
| `InvalidModelOutput` | The model output violated the internal structured protocol or local validation. |
| `UnsupportedCapability` | The provider, model, or v1 scope cannot perform the operation. |
| `ProviderFailure` | Timeout, network, authentication, rate-limit, or other provider failure. |
| `AmbiguousRequest` | Routing could not select one operation and `FailOnAmbiguous` is enabled. |

Provider raw exceptions and credentials are never exposed through the exception.

## Requirements

- .NET 8.0 or later.
- A valid Aspose.Cells license for production use.
- An LLM endpoint: OpenAI, Anthropic, an OpenAI-compatible service, Aspose.LLM, or any
  `IChatClient` implementation.
- For Aspose.LLM, a separate temporary or commercial Aspose.LLM license (inference does not run
  in evaluation mode) and the local model runtime.

## See Also

- [Aspose.Cells.AI on NuGet](https://www.nuget.org/packages/Aspose.Cells.AI)
- [API reference](https://reference.aspose.com/cells/net/aspose.cells.ai/)
- [Aspose.Cells documentation](https://docs.aspose.com/cells/net/)
- [Support forum](https://forum.aspose.com/c/cells)
- [Temporary license](https://purchase.aspose.com/temporary-license/)
