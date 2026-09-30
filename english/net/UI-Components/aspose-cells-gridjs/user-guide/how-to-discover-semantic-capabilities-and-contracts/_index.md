---
title: How to discover semantic capabilities and contracts
description: Inspect the live semantic contract before choosing a query or action, and distinguish published calls from calls currently available for a target.
keywords: GridJs, Semantic Automation, JavaScript API, discover semantic capabilities and contracts
type: docs
weight: 2
url: /net/aspose-cells-gridjs/user-guide/how-to-discover-semantic-capabilities-and-contracts/
---

## Introduction

Inspect the live semantic contract before choosing a query or action, and distinguish published calls from calls currently available for a target.

## How to use

1. Wait for the intended instance to become ready.
2. Read `getContract()` to inspect query and action names, parameter schemas, result schemas, and availability.
3. Inspect action execution and operation metadata before dispatching it.
4. Use `getAvailableActions()` for the intended target kind and sheet. Treat this list as discovery, not a guarantee that a specific cell can be edited.
5. Handle explicit call errors even after capability checks, because runtime state and target permissions can change.

## JavaScript API

The example assumes an existing GridJS instance named `orders-grid`, enabled as described in [How to enable semantic automation](/cells/net/aspose-cells-gridjs/user-guide/how-to-enable-semantic-automation/). Run it inside an async function or a module that supports top-level await. Use a disposable workbook for examples that change cells or selections.

```js
const semantic = window.GridJSSemanticAutomation.getInstance('orders-grid');
if (!semantic) throw new Error('orders-grid was not found');
await semantic.waitForRuntime({phase: 'ready', timeoutMs: 30000});
const sheetId = semantic.query({query: 'workbook.read', parameters: {}}).state.activeSheetId;
const contract = semantic.getContract();
console.log(contract.contractVersion, contract.schemaDialect, contract.limits);
console.log(Object.keys(contract.queries), Object.keys(contract.actions));
const edit = contract.actions['cell.setValue'];
console.log(edit.available, edit.unavailableReason, edit.parametersSchema,
  edit.resultSchema, edit.execution, edit.operation, edit.verification);
console.log(semantic.getCapabilities()['cell.edit.value']);
console.log(semantic.getAvailableActions({kind: 'cell', sheetId}));
```

The current call catalog publishes these queries: `workbook.read`, `workbook.sheets`, `sheet.read`, `selection.read`, and `cell.read`. It publishes these actions: `sheet.activate`, `cell.activate`, `range.select`, and `cell.setValue`. Use the live contract rather than assuming this list can never change.

`getContract()` combines contract information, instance/session identity, capabilities, limits, and the query/action catalogs. `describeContract()` provides the base contract description; `getCapabilities()` provides capability metadata. JSON schemas use the Draft 2020-12 dialect, with the `maxUtf8Bytes` annotation describing the text input byte limit.

Actions currently use business execution with `direct` delivery. Metadata includes completion through `waitForOperation`, cancellation support, invocation-ID support, completion guarantees, and a canonical-readback verification query. No `ui.controls.list`, `ui.controls.click`, or named `range.read` call is published by this catalog.

A capability can be available because some sheet supports it; the selected sheet or cell may still reject a call. In particular, collaborative sheets do not support semantic cell writes. Public snapshots have size/depth limits; exceeding them produces `VALUE_POLICY_DENIED`.

## Common Questions

Q: Can I call any name that resembles a JavaScript method?
A: No. Only published query/action names are dispatched; unsupported names are rejected.

Q: Does discovery bypass protection?
A: No. Target-specific validation still runs during execution.

Q: Can I request browser delivery for these actions?
A: No. The current actions support direct delivery; unsupported delivery produces SEMANTIC_DELIVERY_UNSUPPORTED.
