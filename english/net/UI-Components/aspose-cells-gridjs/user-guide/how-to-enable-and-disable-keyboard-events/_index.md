---
title: How to enable and disable keyboard events
description: Enable or disable GridJs sheet keyboard event handling through the public enableKeyEvent method and understand the shortcut operations handled by the inspected code.
keywords: enableKeyEvent, keyboard events, keydown, shortcut, copy, paste, undo, redo, selectorMove
type: docs
weight: 1
url: /net/aspose-cells-gridjs/user-guide/how-to-enable-and-disable-keyboard-events/
aliases:
- /net/aspose-cells-gridjs/user-guide/how-to-enable-and-disable-keyboard-events/
---

## Introduction

GridJs stores keyboard-event status on the sheet as `enableKeyEvent`. The inspected sheet constructor sets this value to `true` when the sheet mode is not `read`, and to `false` when the sheet mode is `read`. The public spreadsheet method `enableKeyEvent(b)` updates the same sheet flag.

When sheet keyboard events are enabled in edit mode, the global `keydown` handler can process selection movement, clipboard shortcuts, formatting shortcuts, search and replace shortcuts, fill shortcuts, date and time input, deletion, direct cell input, and F2 editing. When this flag is disabled after an edit-mode sheet is created, the inspected global sheet `keydown` path returns before those sheet shortcut actions run.

## How to use

1. Create or obtain the GridJs spreadsheet instance.

```js
const xs = x_spreadsheet('#gridjs-demo-uid', {
  mode: 'edit',
});
```

2. Disable sheet keyboard shortcut handling by passing `false`.

```js
xs.enableKeyEvent(false);
```

3. Enable sheet keyboard shortcut handling by passing `true`.

```js
xs.enableKeyEvent(true);
```

4. In edit mode, use the following shortcut operations when sheet keyboard events are enabled.

| Shortcut | Operation found in code |
|----------|-------------------------|
| `Ctrl`/`Cmd` + `C` | Copies the selected cells and calls the canvas copy operation. |
| `Ctrl`/`Cmd` + `Left` | Moves the selector to the first column of the current row; with `Shift`, extends the selection. |
| `Ctrl`/`Cmd` + `Up` | Moves the selector to the first row of the current column; with `Shift`, extends the selection. |
| `Ctrl`/`Cmd` + `Right` | Moves the selector to the last column of the current row; with `Shift`, extends the selection. |
| `Ctrl`/`Cmd` + `Down` | Moves the selector to the last row of the current column; with `Shift`, extends the selection. |
| `Ctrl`/`Cmd` + `Space` | Selects the current column. |
| `Shift` + `Space` | Selects the current row. |
| `Esc` | Hides the context menu and comment tip, then clears the clipboard state. |
| `Left` | Moves the selector left; with `Shift`, extends the selection. |
| `Up` | Moves the selector up; with `Shift`, extends the selection. |
| `Right` | Moves the selector right; with `Shift`, extends the selection. |
| `Down` | Moves the selector down; with `Shift`, extends the selection. |
| `Tab` | Clears the editor and moves the selector right. |
| `Shift` + `Tab` | Clears the editor and moves the selector left. |
| `Enter` | Clears the editor and moves the selector down. |
| `Shift` + `Enter` | Clears the editor and moves the selector up. |
| `Ctrl`/`Cmd` + `Z` | Runs undo. |
| `Ctrl`/`Cmd` + `Y` | Runs redo. |
| `Ctrl`/`Cmd` + `1` | Opens the more number formats modal for the selected cell. |
| `Ctrl`/`Cmd` + `X` | Cuts the selected cells. |
| `Ctrl`/`Cmd` + `U` | Toggles underline through the toolbar. |
| `Ctrl`/`Cmd` + `V` | Runs the canvas paste operation when an internal canvas clipboard exists; otherwise the inspected code leaves browser paste handling available. |
| `Ctrl`/`Cmd` + `F` | Opens the search modal. |
| `Ctrl`/`Cmd` + `H` | Opens the replace view of the search modal when the sheet mode is not `read`. |
| `Ctrl`/`Cmd` + `B` | Toggles bold through the toolbar. |
| `Ctrl`/`Cmd` + `I` | Toggles italic through the toolbar. |
| `Ctrl`/`Cmd` + `R` | Fills right across a multiple selection and copies the source cell style to the filled cells. |
| `Ctrl`/`Cmd` + `D` | Fills down across a multiple selection and copies the source cell style to the filled cells. |
| `Ctrl`/`Cmd` + `;` | Inserts the current date into the selected cell and opens the editor. |
| `Ctrl`/`Cmd` + `Shift` + `;` | Inserts the current time into the selected cell and opens the editor. |
| `Backspace` | Deletes the selected cell text. |
| `Delete` | Deletes the selected cell text and calls the canvas delete operation. |
| `A`-`Z`, `0`-`9`, numpad `0`-`9`, or `=` | Starts direct cell input with the pressed key, updates the formula bar, and opens the editor. |
| `F2` | Opens the editor for the selected cell. |

5. In read mode, the inspected constructor binds the read-mode keyboard handler. That path runs the common selection and clipboard shortcuts, but does not run the edit-only shortcut group.

6. Other keyboard handlers were also found in the inspected code, but they are local input or modal handlers rather than the public `enableKeyEvent(b)` sheet toggle.

| Area | Key operation found in code |
|------|-----------------------------|
| Cell editor | `Alt` + `Enter` inserts a line break in the editor. |
| Cell editor | `Ctrl` + `;` inserts the current date into the editor text. |
| Cell editor | `Ctrl` + `Shift` + `;` inserts the current time into the editor text. |
| Cell editor | `Left`, `Right`, `Up`, or `Down` moves the selector when the original editor text is empty. |
| Cell editor | `Up` moves the cursor to the start when the original editor text is not empty. |
| Cell editor | `Down` moves the cursor to the end when the original editor text is not empty. |
| Formula bar | `Enter` blurs the formula input unless `Alt` is pressed, then calls the formula-bar enter callback. |
| Formula bar | `Tab` blurs the formula input and calls the formula-bar tab callback. |
| Suggest list | `Up` moves to the previous suggestion. |
| Suggest list | `Down` moves to the next suggestion. |
| Suggest list | `Enter` accepts the current suggestion. |
| Suggest list | `Tab` accepts the current suggestion. |
| Modal | `Esc` closes the modal created by `component/modal.js`. |
| File name bar | `Enter` blurs the editable file-name element. |

## JavaScript API

Use `enableKeyEvent(b)` on the spreadsheet instance. The implementation assigns the value directly to `this.sheet.enableKeyEvent`.

```js
xs.enableKeyEvent(false);
xs.enableKeyEvent(true);
```

### Relevant functions
| Function / Location | Description | Parameters | Returns |
|----------|-------------|------------|---------|
| `Sheet(targetEl, data, xs)` (`component/sheet.js`) | Initializes `this.enableKeyEvent` to `mode !== 'read'`, then registers window and input event handlers. | `targetEl`, `data`, `xs` | `Sheet` instance |
| `addWindowEvent()` (`component/sheet.js`) | Binds sheet-level resize, paste, formula-bar input, document paste, and window keydown handlers. The binding path depends on the current `enableKeyEvent` value at setup time. | None | `void` |
| `act_w_keydown_action(evt, readOnly)` (`component/sheet.js`) | Handles the sheet keyboard shortcut logic. In edit mode, it returns before processing when `it.enableKeyEvent` is false. | `evt`: keyboard event; `readOnly`: boolean | `void` |
| `act_w_paste(evt)` (`component/sheet.js`) | Handles paste from the formula-bar input and returns when `it.enableKeyEvent` is false. | `evt`: paste event | `Promise<void>` |
| `enableKeyEvent(b)` (`index.js`) | Sets `this.sheet.enableKeyEvent = b`. | `b`: boolean-like value | `void` |
| `keydownEventHandler(evt)` (`component/editor.js`) | Handles local editor keyboard behavior such as `Alt` + `Enter`, date/time insertion, and arrow-key behavior inside the editor. | `evt`: keyboard event | `void` |
| `FormulaBar` keydown handler (`component/formula-bar.js`) | Handles `Enter` and `Tab` inside the formula input. | `evt`: keyboard event | `void` |
| `inputKeydownHandler(evt, sheet)` (`component/suggest.js`) | Handles keyboard navigation and acceptance inside a suggestion list. | `evt`, `sheet` | `void` |

The inspected `index.d.ts` file does not declare `enableKeyEvent(b)` on the `Spreadsheet` class, but the `index.js` implementation exposes the method directly.

The inspected setter does not call `addWindowEvent()` again and does not unbind handlers that were already registered. It changes the flag that the sheet-level keydown and paste paths check.

## Common Questions

Q: How are keyboard events enabled by default?
A: The inspected sheet constructor sets `enableKeyEvent` to `true` when `mode !== 'read'`.

Q: How are keyboard events disabled by default?
A: The inspected sheet constructor sets `enableKeyEvent` to `false` when `mode === 'read'`.

Q: Which public method changes the keyboard-event flag?
A: The inspected public method is `enableKeyEvent(b)`, and it assigns `b` to `this.sheet.enableKeyEvent`.

Q: Does disabling keyboard events remove all event listeners?
A: No. The inspected setter only changes the flag. It does not rebind or unbind event listeners.

Q: Are modal and editor keyboard handlers controlled by the same public toggle?
A: Not in the inspected code. Modal, editor, formula-bar, suggestion-list, and file-name handlers are registered separately.
