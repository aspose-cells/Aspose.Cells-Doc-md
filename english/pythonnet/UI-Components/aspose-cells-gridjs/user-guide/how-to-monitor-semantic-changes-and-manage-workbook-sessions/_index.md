---
title: How to monitor semantic changes and manage workbook sessions
description: Subscribe to semantic events, resume from retained revisions, and replace stale facade bindings when the workbook or grid instance changes.
keywords: GridJs, Semantic Automation, JavaScript API, monitor semantic changes and manage workbook sessions
type: docs
weight: 8
url: /python-net/aspose-cells-gridjs/user-guide/how-to-monitor-semantic-changes-and-manage-workbook-sessions/
---

## Introduction

Subscribe to semantic events, resume from retained revisions, and replace stale facade bindings when the workbook or grid instance changes.

## How to use

1. Acquire the current facade and wait for readiness.
2. Subscribe to a named event or to all events with event:'*'. Retain the returned subscription for cleanup.
3. Record revisions within the current workbook session. Use fromRevision only while the relevant history remains available.
4. Before replacing a workbook, stop using its old facade and clean up your subscriptions. After loading begins, reacquire the current facade and wait for readiness again.
5. Rediscover sheet IDs and register new subscriptions for the new session.

## JavaScript API

The example assumes an existing GridJS instance named `orders-grid`, enabled as described in [How to enable semantic automation](/cells/python-net/aspose-cells-gridjs/user-guide/how-to-enable-semantic-automation/). Run it inside an async function or a module that supports top-level await. Use a disposable workbook for examples that change cells or selections.

```js
const semantic = window.GridJSSemanticAutomation.getInstance('orders-grid');
if (!semantic) throw new Error('orders-grid was not found');
await semantic.waitForRuntime({phase: 'ready', timeoutMs: 30000});
let lastRevision = semantic.getRuntimeState().revision;
const subscription = semantic.subscribe({
  event: '*', fromRevision: lastRevision,
  onEvent(event) {
    lastRevision = event.revision;
    console.log(event.event, event.workbookSessionId, event.revision, event.reason);
  },
});
// Call subscription.unsubscribe() when this listener is no longer needed.

// Call this after your application's loader has started loading a replacement workbook.
async function attachToCurrentWorkbook() {
  subscription.unsubscribe();
  const current = window.GridJSSemanticAutomation.getInstance('orders-grid');
  if (!current) throw new Error('The grid instance no longer exists');
  await current.waitForRuntime({phase: 'ready', timeoutMs: 30000});
  const snapshot = current.query({query: 'workbook.sheets', parameters: {}});
  console.log(snapshot.workbookSessionId, snapshot.state.sheets);
  const nextSubscription = current.subscribe({
    event: 'cellchange', onEvent: event => console.log(event.state),
  });
  return {semantic: current, subscription: nextSubscription};
}
```

Available controller events include runtimechange, operationchange, sheetchange, selectionchange, and cellchange. Events carry an event name, revision, workbookSessionId, and event-specific payload such as state, operation, or reason. These are semantic state notifications, not a promise to capture every possible UI interaction.

fromRevision replays retained events with a greater revision and then subscribes to new ones. History is finite; an older unavailable revision produces REVISION_TOO_OLD. Recover by taking a fresh state snapshot and resubscribing from the current revision. This is not a durable audit log.

A new workbook load creates a new workbookSessionId and resets operations, invocation history, event history, revisions, and sheet identifiers. Existing listeners are cleared when replacing an established session. Old workbook-bound facades reject access with WORKBOOK_SESSION_EXPIRED; reacquire through the registry or grid.semantic instead of repeatedly retrying the old object.

instanceGeneration identifies the grid instance lifetime. Destroying an instance unregisters it; stale access can produce INSTANCE_GENERATION_EXPIRED. A new instance with the same human-chosen instanceId must still be treated as a new generation. Cancellation signals stop waits, not workbook loading or mutations.

## Common Questions

Q: Can I resume a revision from the previous workbook?
A: No. Revision history belongs to a workbook session and resets on replacement.

Q: Will old subscriptions automatically follow a replacement workbook?
A: No. Reacquire the facade and subscribe again for the new session.

Q: Can I use these events as a permanent audit trail?
A: No. Retention is bounded and reset with the session. Persist any audit information your application requires separately.
