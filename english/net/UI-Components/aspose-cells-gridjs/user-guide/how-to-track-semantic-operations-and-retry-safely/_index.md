---
title: How to track semantic operations and retry safely
description: Track asynchronous semantic actions to a terminal result and handle timeouts and duplicate requests without blindly repeating mutations.
keywords: GridJs, Semantic Automation, JavaScript API, track semantic operations and retry safely
type: docs
weight: 7
url: /net/aspose-cells-gridjs/user-guide/how-to-track-semantic-operations-and-retry-safely/
---

## Introduction

Track asynchronous semantic actions to a terminal result and handle timeouts and duplicate requests without blindly repeating mutations.

## How to use

1. Catch synchronous perform errors separately from errors returned by a failed operation.
2. Save the operationId from the receipt before waiting.
3. After waitForOperation resolves, check phase; inspect result only for completed operations and error for failed ones.
4. On a waiting timeout, query the same operation ID and read the target back when needed. Do not assume the underlying mutation was cancelled.
5. For a duplicate cell.setValue request, reuse its original invocationId and identical parameters. Changed requests need new IDs.

## JavaScript API

The example assumes an existing GridJS instance named `orders-grid`, enabled as described in [How to enable semantic automation](/cells/net/aspose-cells-gridjs/user-guide/how-to-enable-semantic-automation/). Run it inside an async function or a module that supports top-level await. Use a disposable workbook for examples that change cells or selections.

```js
const semantic = window.GridJSSemanticAutomation.getInstance('orders-grid');
if (!semantic) throw new Error('orders-grid was not found');
await semantic.waitForRuntime({phase: 'ready', timeoutMs: 30000});
const sheetId = semantic.query({query: 'workbook.read', parameters: {}}).state.activeSheetId;
const request = {
  action: 'cell.setValue', invocationId: `edit-${crypto.randomUUID()}`,
  parameters: {sheetId, address: 'A1', value: {kind: 'text', value: 'Order ready'}},
};
const receipt = semantic.perform(request); // Can throw before an operation is created.
try {
  const operation = await semantic.waitForOperation({operationId: receipt.operationId, timeoutMs: 30000});
  if (operation.phase === 'completed') console.log(operation.result);
  else console.error(operation.error);
} catch (error) {
  if (error.code !== 'TIMEOUT') throw error;
  const current = semantic.getOperation(receipt.operationId);
  console.log(current.phase, current.result, current.error);
  // If still running, keep tracking this operation rather than submitting a new write.
}
// Example of an identical duplicate: the retained invocation returns its original receipt.
const duplicate = semantic.perform(request);
console.log(duplicate.operationId === receipt.operationId);
console.log(semantic.listOperations({offset: 0, limit: 100}));
```

perform returns a receipt with operationId, action, instanceGeneration, workbookSessionId, and a running phase. It is acceptance, not completion. Operation records contain phase, progress, result/error, timestamps, and revision. The current business actions publish cancellation:'none'. Passing an AbortSignal to waitForOperation cancels the wait only.

waitForOperation defaults to a 30-second timeout. A TIMEOUT includes details identifying the operation, an unknown outcome, and getOperation as the next action. If a result validation or serialization error occurs after execution, its details can instead request readBack; do not assume that an error guarantees no mutation occurred.

Only cell.setValue currently advertises invocation-ID support. An identical retained invocation returns the original receipt, including a previously failed operation; reusing an ID for different parameters produces INVOCATION_CONFLICT. IDs are at most 128 characters, start with a letter or digit, and otherwise allow letters, digits, underscore, dot, colon, and hyphen. Deduplication is session-local and bounded, not a permanent exactly-once ledger; completed entries can be evicted when the registry grows beyond 256 entries.

listOperations() returns an array; supplying paging options returns operations, total, and nextOffset. Page limits are 1–1000. Operation records and invocation history reset when a workbook session is replaced.

For cell writes, advertised server-mode guarantees include modelApplied and serverAcknowledged. Selection and sheet activation advertise modelApplied. Neither guarantee asserts durable Excel-file persistence or a real browser click.

## Common Questions

Q: Does a resolved wait promise prove success?
A: No. A failed operation also resolves to a terminal record; inspect phase and error.

Q: Does a timeout make it safe to retry with a new ID?
A: No. The original operation may still be running or may already have changed the cell. Inspect its state first.

Q: Is invocationId deduplication permanent?
A: No. It is bounded and scoped to the current workbook session.
