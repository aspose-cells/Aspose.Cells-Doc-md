---
title: How to enable semantic automation
description: Enable GridJS semantic automation, discover the intended grid instance, and wait for its workbook runtime before making business calls.
keywords: GridJs, Semantic Automation, JavaScript API, enable semantic automation
type: docs
weight: 1
url: /net/aspose-cells-gridjs/user-guide/how-to-enable-semantic-automation/
---

## Introduction

Enable GridJS semantic automation, discover the intended grid instance, and wait for its workbook runtime before making business calls.

## How to use

1. Enable semantic automation when creating the GridJS instance. It is disabled unless `enabled` is exactly `true`.
2. Assign a stable, unique `instanceId` when your automation must find a specific grid. IDs must start with a letter or digit, contain only letters, digits, underscores, or hyphens, and be at most 80 characters.
3. Load your workbook using your application's normal GridJS data-loading flow. Enabling automation does not load a workbook.
4. Get the instance facade and wait for the runtime to reach `ready` before reading or changing workbook data.
5. If workbook loading fails, handle the readiness error instead of issuing business calls against an unready runtime.

## JavaScript API

```js
// Browser build of GridJS; element is the host DOM element or selector.
// workbookData is a valid payload supplied by your existing workbook loader.
async function createAutomatedGrid(element, workbookData) {
  const grid = window.x_spreadsheet(element, {
    semanticAutomation: {enabled: true, instanceId: 'orders-grid'},
  });
  grid.loadData(workbookData);
  const semantic = grid.semantic;
  await semantic.waitForRuntime({phase: 'ready', timeoutMs: 30000});
  console.log(semantic.getRuntimeState());
  return grid;
}

// Discover a grid after your application has created it.
function findOrdersGrid() {
  const registry = window.GridJSSemanticAutomation;
  if (!registry) throw new Error('GridJS semantic registry is not installed');
  console.table(registry.listInstances());
  const semantic = registry.getInstance('orders-grid');
  if (!semantic) throw new Error('orders-grid was not found');
  return semantic;
}
```

`semanticAutomation` accepts `enabled` and `instanceId`; unknown option names are rejected. Omitting instanceId generates an ID, which you can discover with `listInstances()`. Duplicate IDs are rejected.

Instance descriptors include `instanceId`, `instanceGeneration`, `contractVersion`, `runtimePhase`, and `workbookSessionId`. Runtime state also includes `phase`, `revision`, `failure`, active operation IDs, and the active sheet ID. Readiness is tied to workbook loading and sheet rendering, not merely instance construction.

`waitForRuntime()` defaults to phase `ready` and a 30-second waiting timeout. Its optional `signal` cancels waiting. Runtime initialization, loading, rendering, updating, ready, failed, destroyed, and disabled states must not be treated as interchangeable.

## Common Questions

Q: Does enabling semantic automation make the worksheet editable?
A: No. Existing edit-mode, protection, and other business restrictions still apply.

Q: Does getInstance return an error for an unknown ID?
A: It returns null; check the result before calling facade methods.

Q: Can I keep the same facade after loading another workbook?
A: Reacquire the facade from the grid or registry after the new load starts. Old workbook-bound facades expire.
