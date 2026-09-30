---
title: How to handle cell validation in semantic automation
description: Handle existing cell validation rules during semantic writes, including Stop failures and explicit continuation of Warning or Information alerts.
keywords: GridJs, Semantic Automation, JavaScript API, handle cell validation in semantic automation
type: docs
weight: 6
url: /java/aspose-cells-gridjs/user-guide/how-to-handle-cell-validation-in-semantic-automation/
---

## Introduction

Handle existing cell validation rules during semantic writes, including Stop failures and explicit continuation of Warning or Information alerts.

## How to use

1. Use a cell whose validation rule has already been configured. This API checks rules; it does not create them.
2. Submit a normal write with allowInvalid omitted or false.
3. Inspect the completed operation record. A failed operation can carry CELL_VALIDATION_CONFIRMATION_REQUIRED with alert details.
4. Ask the application user whether to continue a Warning or Information alert. Only after confirmation submit a new request with allowInvalid:true and a new invocation ID.
5. Never use allowInvalid to bypass a Stop alert or an unavailable evaluator.

## JavaScript API

The example assumes an existing GridJS instance named `orders-grid`, enabled as described in [How to enable semantic automation](/cells/java/aspose-cells-gridjs/user-guide/how-to-enable-semantic-automation/). Run it inside an async function or a module that supports top-level await. Use a disposable workbook for examples that change cells or selections.

```js
const semantic = window.GridJSSemanticAutomation.getInstance('orders-grid');
if (!semantic) throw new Error('orders-grid was not found');
await semantic.waitForRuntime({phase: 'ready', timeoutMs: 30000});
const sheetId = semantic.query({query: 'workbook.read', parameters: {}}).state.activeSheetId;
async function writeCandidate(allowInvalid = false) {
  const receipt = semantic.perform({
    action: 'cell.setValue', invocationId: `validation-${crypto.randomUUID()}`,
    parameters: {sheetId, address: 'D3', value: {kind: 'text', value: '12'}, allowInvalid},
  });
  return semantic.waitForOperation({operationId: receipt.operationId});
}
const operation = await writeCandidate();
if (operation.phase === 'completed') {
  console.log(operation.result.validation, operation.result.after);
} else if (operation.error?.code === 'CELL_VALIDATION_CONFIRMATION_REQUIRED') {
  console.log(operation.error.details);
  // In your user-confirmation handler, call writeCandidate(true), then check
  // that returned operation's phase and error as well. Do not auto-confirm.
} else {
  console.error(operation.error);
}
```

Stop rejects invalid input with `CELL_VALIDATION_FAILED`. Warning and Information can return `CELL_VALIDATION_CONFIRMATION_REQUIRED`, with details such as `canContinue`, `alertStyle`, `title`, and `message`. Continuing requires an explicit new invocation because allowInvalid changes the request. A failed operation is returned as a record; it is not automatically thrown by waitForOperation.

If a rule disables its error alert, invalid input can be permitted and reported with `result.validation.valid:false`. Same-value no-op writes do not revalidate unchanged data. Evaluation failures produce `CELL_VALIDATION_ERROR`; missing evaluators produce `CELL_VALIDATION_UNAVAILABLE`. Neither is permission to write unchecked.

Ordinary numeric, text-length, date/time, and literal-list rules can be checked locally. Formula-dependent rules and candidates require the compatible server evaluator; pure client mode cannot provide that evaluator. Frontend and backend must support the same validation flow.

Validation is a preflight check followed by a write, not an atomic transaction: referenced values or rules can change between those operations. Collaborative semantic writes remain unavailable.

## Common Questions

Q: Can allowInvalid override a Stop rule?
A: No. It only permits explicitly continued Warning or Information alerts.

Q: Should confirmation reuse the first invocation ID?
A: No. Changing allowInvalid changes the request fingerprint; use a new ID.

Q: Why does validation fail in a client-only workbook?
A: Formula-dependent validation needs a compatible server evaluator. The API reports evaluator errors rather than silently skipping the check.
