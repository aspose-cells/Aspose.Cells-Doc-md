---
title: Read-only Mode and Edit Mode
description: Configure GridJs with read-only or edit mode, and understand exactly which interactions are disabled in read mode.
keywords: mode, read, edit, GridInput, formulaInput, bottombar, contextmenu, autofill
type: docs
weight: 1
url: /java/aspose-cells-gridjs/user-guide/read-only-mode-and-edit-mode/
aliases:
- /java/aspose-cells-gridjs/read-only-mode-and-edit-mode/
---

## Introduction

GridJs mode is configured by `options.mode`, with two values: `'edit'` and `'read'`. The default mode is `'edit'` in `defaultSettings`. In read mode, GridJs keeps navigation-related interactions, but blocks data-editing paths such as editor input, cell text write, and paste workflows.

## How to use

1. Initialize GridJs in edit mode when users need full editing features.

2. Initialize GridJs in read mode when users should browse data without changing cell content.

3. In read mode, these editing-related features are disabled by code:

   - Formula bar input and hidden key-input area are set to `disabled`.
   - Opening the in-cell editor is blocked.
   - Writing cell text is blocked.
   - Paste handlers return immediately in read mode (both regular paste and outer-document paste path).
   - Autofill by drag does not run .
   - GridInput keydown/composition/paste bindings are attached only when mode is not 'read'.

4. In read mode, sheet-tab management is reduced:

   - The bottom-bar add button is not rendered.
   - Sheet-tab context-menu and double-click rename handlers are not bound.
   - Tab click for sheet switching is still bound.

5. In read mode, the selector is created as readonly (`mode !== 'edit'`), so the selection corner UI is hidden.

## JavaScript API

```js
// Edit mode (default behavior)
const xsEdit = x_spreadsheet('#gridjs-edit', {
  mode: 'edit',
});

// Read-only mode
const xsRead = x_spreadsheet('#gridjs-read', {
  mode: 'read',
});
```

### Relevant functions
| Function / Location | Description | Parameters | Returns |
|----------|-------------|------------|---------|
| `Options.mode` (`index.d.ts`) | Declares supported mode values: `'edit' | 'read'`. | `mode`: `'edit'` or `'read'` | n/a |
| `defaultSettings.mode` (`core/data_proxy.js`) | Sets default mode to `'edit'`. | none | n/a |
| `editorSet(...)` (`component/sheet.js`) | Stops in-cell editing when `data.settings.mode === 'read'`. | `focus`: optional boolean | `void` |
| `dataSetCellText(...)` (`component/sheet.js`) | Stops cell text write in read mode. | `text`, `state` | `void` |
| `ContextMenu.setMode(...)` (`component/contextmenu.js`) | Shrinks menu items in read mode to a minimal copy-first set. | `mode`: row/column/range context | `void` |
| `Bottombar.setItemEvent(...)` (`component/bottombar.js`) | Binds rename/context-menu handlers only in edit mode. | `item`: tab element | `void` |

No public runtime API for switching mode after initialization was found in `index.d.ts` or the inspected `Spreadsheet` public methods in `index.js`.

## Common Questions

Q: What mode is used if I do not pass `options.mode`?
A: GridJs uses `mode: 'edit'` from `defaultSettings`.

Q: What is the simplest way to make GridJs read-only?
A: Initialize with `{ mode: 'read' }`.

Q: In read mode, can users still switch worksheets?
A: Yes. Sheet-tab click is still bound; only add/rename/context-menu management handlers are removed.

Q: In read mode, why can users not type or paste into cells?
A: Multiple edit paths explicitly return early when `data.settings.mode === 'read'`, including editor opening, text writing, and paste handlers.
