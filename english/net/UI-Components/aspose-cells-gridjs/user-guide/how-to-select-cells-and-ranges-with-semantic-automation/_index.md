---
title: How to select cells and ranges with semantic automation
description: Activate a cell or select a range by A1 address, then verify the active cell and selected range through semantic readback.
keywords: GridJs, Semantic Automation, JavaScript API, select cells and ranges with semantic automation
type: docs
weight: 4
url: /net/aspose-cells-gridjs/user-guide/how-to-select-cells-and-ranges-with-semantic-automation/
---

## Introduction

Activate a cell or select a range by A1 address, then verify the active cell and selected range through semantic readback.

## How to use

1. Obtain the target sheet ID from workbook discovery.
2. Use `cell.activate` for one cell or `range.select` for a rectangular range.
3. Wait for the operation and check that it completed.
4. Read `selection.read` to inspect the actual active cell and selected range, including merged-cell expansion.

## JavaScript API

The example assumes an existing GridJS instance named `orders-grid`, enabled as described in [How to enable semantic automation](/cells/net/aspose-cells-gridjs/user-guide/how-to-enable-semantic-automation/). Run it inside an async function or a module that supports top-level await. Use a disposable workbook for examples that change cells or selections.

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
await complete({action: 'cell.activate', parameters: {sheetId, address: 'C2'}});
console.log(semantic.query({query: 'selection.read', parameters: {sheetId}}).state);
await complete({action: 'range.select', parameters: {sheetId, range: 'E4:B2'}});
const selection = semantic.query({query: 'selection.read', parameters: {sheetId}}).state;
console.log(selection.activeCell, selection.range);
```

Cell inputs use A1 strings such as `C2`; surrounding whitespace and lowercase letters are accepted and normalized. Range input accepts one cell or two endpoints, including reversed endpoints. On an ordinary unmerged area, `E4:B2` normalizes to `B2:E4`. Results use uppercase A1 coordinates, and a one-cell selection is represented as a range such as `C2:C2`.

Selection actions activate the target sheet if needed. Merged cells can expand the actual selected range. Always read back the selection instead of assuming its string equals the submitted range. `activeCell` is the active cell coordinate; `range` describes the selection extent.

Use `parameters.range` for range.select and `parameters.address` for cell.activate. The removed top-level `target` request form and range.select.address alias are not accepted. Unsupported addresses or invalid ranges produce explicit errors; inability to reach the requested selection produces `SELECTION_POSTCONDITION_FAILED`.

## Common Questions

Q: Is selection required before reading or writing a cell?
A: No. Cell read/write calls identify the sheet and cell explicitly.

Q: Why is the selected range larger than requested?
A: Merged-cell boundaries can expand the selection. Use selection.read to inspect the actual result.

Q: Does a selection action change cell contents?
A: No. Use cell.setValue for value changes.
