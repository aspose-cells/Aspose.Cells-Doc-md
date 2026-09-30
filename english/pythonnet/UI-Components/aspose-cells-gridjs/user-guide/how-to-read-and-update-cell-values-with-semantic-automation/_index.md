---
title: How to read and update cell values with semantic automation
description: Read canonical cell state, enter text or formula input, clear a cell, and verify the actual result after a completed semantic write.
keywords: GridJs, Semantic Automation, JavaScript API, read and update cell values with semantic automation
type: docs
weight: 5
url: /python-net/aspose-cells-gridjs/user-guide/how-to-read-and-update-cell-values-with-semantic-automation/
---

## Introduction

Read canonical cell state, enter text or formula input, clear a cell, and verify the actual result after a completed semantic write.

## How to use

1. Choose an editable, non-collaborative worksheet and obtain its sheet ID.
2. Read the intended cell before changing it. Note its value, formula, protection state, and any merged range.
3. Submit text with `{kind: 'text', value: '...'}` or clear it with `{kind: 'blank'}`.
4. Wait for completion and inspect both the operation result and a fresh cell.read snapshot.
5. Use disposable cells for the example below: it replaces A1 and clears B1.

## JavaScript API

The example assumes an existing GridJS instance named `orders-grid`, enabled as described in [How to enable semantic automation](/cells/python-net/aspose-cells-gridjs/user-guide/how-to-enable-semantic-automation/). Run it inside an async function or a module that supports top-level await. Use a disposable workbook for examples that change cells or selections.

```js
const semantic = window.GridJSSemanticAutomation.getInstance('orders-grid');
if (!semantic) throw new Error('orders-grid was not found');
await semantic.waitForRuntime({phase: 'ready', timeoutMs: 30000});
const sheetId = semantic.query({query: 'workbook.read', parameters: {}}).state.activeSheetId;
async function complete(request) {
  const receipt = semantic.perform(request);
  const operation = await semantic.waitForOperation({operationId: receipt.operationId});
  if (operation.phase !== 'completed') {
    throw Object.assign(new Error(operation.error?.message || operation.phase), operation.error || {});
  }
  return operation.result;
}
const before = semantic.query({query: 'cell.read', parameters: {sheetId, address: 'A1'}}).state;
const result = await complete({
  action: 'cell.setValue', invocationId: `write-${crypto.randomUUID()}`,
  parameters: {sheetId, address: 'A1', value: {kind: 'text', value: '=1+2'}},
});
const after = semantic.query({query: 'cell.read', parameters: {sheetId, address: 'A1'}}).state;
console.log(before, result.changed, result.before, result.after,
  after.value, after.formula, after.displayValue, after.valueKind);
await complete({
  action: 'cell.setValue', invocationId: `clear-${crypto.randomUUID()}`,
  parameters: {sheetId, address: 'B1', value: {kind: 'blank'}},
});
```

The write API accepts only Text and Blank, even though readback can represent number and boolean values. Text follows normal GridJS input semantics: numeric-looking strings and formula strings may become numeric or formula cells. A Text request is not a promise that readback will remain a text value. Inspect the canonical result rather than comparing it blindly with the input object.

Text must be nonempty and at most 1024 UTF-8 bytes. Empty text is rejected; use Blank to clear a cell. Rich-text markup is not supported. Cell readback includes `value`, `displayValue`, `formula`, `valueKind`, `readonly`, `rowHidden`, `columnHidden`, and merged-range information when present.

A completed write result contains `changed`, `target`, `before`, `after`, `formula`, and `displayValue`, with transaction/invocation and validation information when returned. No-op writes may report changed:false. Writes to read-only or locked cells, outside sheet bounds, or into a non-anchor merged cell are rejected. Collaborative semantic writes are unavailable.

The explicit sheetId/address determines the write target, not the visible selection. Completion confirms the advertised model/server guarantees, not that an Excel file has been durably saved. See [operation tracking](/cells/python-net/aspose-cells-gridjs/user-guide/how-to-track-semantic-operations-and-retry-safely/) before adding retries.

## Common Questions

Q: Can I send kind:number or kind:boolean to setValue?
A: No. These are canonical readback kinds, not currently supported write kinds.

Q: Does kind:text prevent formula interpretation?
A: No. Text is entered through normal GridJS cell input semantics, including formula handling.

Q: Can I clear a cell with an empty string?
A: Use {kind:'blank'}; empty Text is rejected.
