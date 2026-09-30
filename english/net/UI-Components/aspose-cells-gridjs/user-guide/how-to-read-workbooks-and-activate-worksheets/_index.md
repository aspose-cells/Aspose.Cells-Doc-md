---
title: How to read workbooks and activate worksheets
description: Read workbook and sheet descriptors, enumerate sheets with pagination, and activate an explicitly identified worksheet.
keywords: GridJs, Semantic Automation, JavaScript API, read workbooks and activate worksheets
type: docs
weight: 3
url: /net/aspose-cells-gridjs/user-guide/how-to-read-workbooks-and-activate-worksheets/
---

## Introduction

Read workbook and sheet descriptors, enumerate sheets with pagination, and activate an explicitly identified worksheet.

## How to use

1. Read the workbook summary to obtain sheet count and active sheet ID.
2. Enumerate `workbook.sheets`; use pagination when you want smaller responses.
3. Read the intended sheet's descriptor using its returned `sheetId`.
4. Activate the sheet with `sheet.activate`, wait for completion, and read back the active sheet.
5. Rediscover sheet IDs after loading a different workbook; do not treat them as persistent worksheet names.

## JavaScript API

The example assumes an existing GridJS instance named `orders-grid`, enabled as described in [How to enable semantic automation](/cells/net/aspose-cells-gridjs/user-guide/how-to-enable-semantic-automation/). Run it inside an async function or a module that supports top-level await. Use a disposable workbook for examples that change cells or selections.

```js
const semantic = window.GridJSSemanticAutomation.getInstance('orders-grid');
if (!semantic) throw new Error('orders-grid was not found');
await semantic.waitForRuntime({phase: 'ready', timeoutMs: 30000});
const workbook = semantic.query({query: 'workbook.read', parameters: {}}).state;
const sheets = [];
let offset = 0;
do {
  const page = semantic.query({query: 'workbook.sheets', parameters: {offset, limit: 100}}).state;
  sheets.push(...page.sheets);
  offset = page.nextOffset;
} while (offset !== null);
console.table(sheets);
// Select an existing visible sheet; an application can choose by name instead.
const chosen = sheets.find(item => item.active && !item.hidden) || sheets.find(item => !item.hidden);
if (!chosen) throw new Error('No visible sheet is available');
const descriptor = semantic.query({query: 'sheet.read', parameters: {sheetId: chosen.sheetId}}).state;
console.log(workbook, descriptor);
async function complete(request) {
  const receipt = semantic.perform(request);
  const operation = await semantic.waitForOperation({operationId: receipt.operationId});
  if (operation.phase !== 'completed') {
    throw Object.assign(new Error(operation.error?.message || operation.phase), operation.error || {});
  }
  return operation.result;
}
const result = await complete({action: 'sheet.activate', parameters: {sheetId: chosen.sheetId}});
const after = semantic.query({query: 'workbook.read', parameters: {}}).state;
console.log(result.changed, after.activeSheetId);
```

Query responses wrap business data in `state`; the envelope also identifies the instance generation, workbook session, revision, and target. Workbook state contains `sheetCount` and `activeSheetId`.

Sheet descriptors contain `sheetId`, `name`, `index`, `active`, `hidden`, `protected`, and `loadState` (`unloaded` or `ready`). Enumerating a descriptor does not itself guarantee a lazily loaded sheet has finished loading.

With pagination requested, workbook.sheets returns `sheets`, `total`, and `nextOffset`; null nextOffset means the last page. Offset is nonnegative, and limit is 1–1000. Without pagination parameters, the state contains the sheets list without requiring pagination metadata.

Activation returns an operation receipt. A completed result includes `changed` and `sheetId`; waiting for completion must precede relying on the new active view.

## Common Questions

Q: Can I pass a sheet name as sheetId?
A: Use the sheetId returned by discovery, not the display name or numeric index.

Q: Why did an old sheetId stop working?
A: Sheet identifiers belong to the current workbook session. Discover them again after replacing the workbook.

Q: Does workbook.sheets modify the active sheet?
A: No. Use sheet.activate when you want to change it.
