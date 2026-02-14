---
title: How to batch insert Rows and Columns
description: Batch insert rows/columns from the context menu, and batch append rows from the Row Appender toolbar.
keywords: batch insert, insert rows above, insert rows below, insert columns left, insert columns right, row appender, insertRows, insertColumns
type: docs
weight: 1
url: /java/aspose-cells-gridjs/how-to-batch-insert-rows-columns
aliases:
- /java/aspose-cells-gridjs/how-to-batch-insert-rows
- /java/aspose-cells-gridjs/how-to-batch-insert-columns
- /java/aspose-cells-gridjs/how-to-insert-multiple-rows
- /java/aspose-cells-gridjs/how-to-insert-multiple-columns
- /java/aspose-cells-gridjs/how-to-insert-rows-and-columns-in-batch
- /java/aspose-cells-gridjs/how-to-use-row-appender
---

## Introduction

GridJs supports two batch insertion paths. The first path is context-menu batch input for rows/columns (**Insert rows above/below**, **Insert columns left/right**). The second path is the bottom **Row Appender** toolbar for batch appending rows. Both paths use the same row insertion pipeline (`sheet.insertRows(...)`) and update sheet layout/rendering.

## How to use

Method 1: Context menu batch insert (rows and columns).
1. Select a range, a row header, or a column header.
2. Right-click and open **Insert...** in the context menu.
3. Choose one action:
   - **Insert rows above**
   - **Insert rows below**
   - **Insert columns to left**
   - **Insert columns to right**
4. Enter the count in the number box and click **Insert**.
   - The input is configured with `min=1` and `max=300`.
   - The insert submenu pre-fills the number input with `10` when opened.
![](batch-insert-open-menu.png)

Method 2: Row Appender batch insert (rows only).
In edit mode, scroll near the bottom until the Row Appender appears, enter row count, then click **Add**.
![](row-appender-add.png)

## JavaScript API
```js
xs = x_spreadsheet('#gridjs-demo-uid', option);

// Insert 5 rows starting at row index 3.
xs.sheet.insertRows(3, 5);

// Insert 4 columns starting at column index 2.
xs.sheet.insertColumns(2, 4);

// Row Appender equivalent: append rows to the end.
const n = 20;
xs.sheet.insertRows(xs.sheet.data.rows.len, n);

// Optional: listen to insert events.
xs.on('rows-inserted', (start, count) => {
  console.log('rows inserted:', start, count);
});

xs.on('columns-inserted', (start, count) => {
  console.log('columns inserted:', start, count);
});

// Optional: enable/disable bottom Row Appender toolbar.
const xsWithAppender = x_spreadsheet('#gridjs-demo-uid-2', {
  showRowAppenderToolbar: true,
});
```

### Relevant functions

| Function | Description | Parameters | Returns |
|----------|-------------|------------|---------|
| `sheet.insertRows(start, n, raiseServerOpr = true)` | Batch inserts rows at the given start row index. | `start` (row index), `n` (count), `raiseServerOpr` (optional boolean) | `void` |
| `sheet.insertColumns(start, n, raiseServerOpr = true)` | Batch inserts columns at the given start column index. | `start` (column index), `n` (count), `raiseServerOpr` (optional boolean) | `void` |
| `data.insert('row' | 'column', n, raiseServerOpr)` | Internal insert operation used by sheet insert flow; updates data structures and triggers insert events. | `type`, `n`, `raiseServerOpr` | `void` |
| `showRowAppenderToolbar` (option) | Controls whether the bottom Row Appender toolbar is created (default enabled). | `true` / `false` | N/A |
| `xs.on(eventName, handler)` | Binds event handler; insert flow triggers `rows-inserted` and `columns-inserted`. | `eventName`, `handler` | `xs` |

Context menu mapping for batch insert:
- `insert-rows-above` -> `sheet.insertRows(sri, n)`
- `insert-rows-below` -> `sheet.insertRows(eri + 1, n)`
- `insert-columns-left` -> `sheet.insertColumns(sci, n)`
- `insert-columns-right` -> `sheet.insertColumns(eci + 1, n)`

## Common Questions

Q: Why do I only see row-related or column-related insert options in some cases?
A: Context menu mode switches by selection type. In row/column header mode, submenu items are filtered to matching row or column operations.

Q: Why does batch insert do nothing on a protected sheet?
A: Insert is blocked when the sheet is locked.

Q: Why is Row Appender not visible?
A: It is hidden in read mode, when `showRowAppenderToolbar` is `false`, or for chart-type sheets.

Q: Can I use batch insert in read mode?
A: No. In read mode, the context menu is reduced to copy-only behavior.

Q: Where is the insertion anchor for above/below/left/right?
A: It uses the current selected range: `sri`/`eri` for rows and `sci`/`eci` for columns, with below/right using `+1` as insertion start.
