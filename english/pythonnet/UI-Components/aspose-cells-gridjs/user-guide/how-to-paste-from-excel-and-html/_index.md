---
title: How to paste from Excel and HTML
description: Paste tabular content from Excel or HTML into GridJs through the clipboard, including supported cell text and style properties parsed from HTML table content.
keywords: Paste, Excel, HTML, clipboard, text/html, pasteFromHTML, pasteFromText, getCellsFromHTML, pasteCellsWithStyle
type: docs
weight: 1
url: /python-net/aspose-cells-gridjs/user-guide/how-to-paste-from-excel-and-html/
aliases:
- /python-net/aspose-cells-gridjs/user-guide/how-to-paste-from-excel-and-html/
---

## Introduction

GridJs handles external paste through browser clipboard events. When the clipboard contains a single text item, GridJs routes the content to `pasteFromText`. When the clipboard contains multiple types and one of them is `text/html`, GridJs routes the HTML content to `pasteFromHTML`. The HTML path parses a table from the clipboard HTML, reads row and cell content, and applies supported style properties to the target GridJs cells.

## How to use

1. Copy a cell range from Excel or copy tabular HTML content from another source.

2. In GridJs, select the target cell or range where the pasted content should start.

3. Paste with the browser paste shortcut. The inspected code binds paste handling to the formula bar input and to the document paste event while GridJs is in edit mode and key events are enabled.

4. If the clipboard contains only one text type and the text is not an internal GridJs copy/cut marker, GridJs splits the text by `\r\n` for rows and by tab characters for columns, then writes the resulting cell text into the target range.

5. If the clipboard contains `text/html`, GridJs parses the HTML with `DOMParser`, finds the first `table`, reads its `tr` and `td` elements, and pastes the result into the target range.

6. For HTML paste, GridJs reads style rules from the clipboard HTML `style` element and matches them to each `td` class. The inspected code applies text, font color, background color, font size, font family, bold, italic, underline, horizontal alignment, vertical alignment, text wrapping, and number-format values supported by `setNumberFormat`.

7. If the target paste range reaches the current row or column limit, GridJs extends the row or column count by one extra row or column. If the target is a complete merged range, a single-source-cell paste writes to the top-left cell, while a multi-cell source can unmerge the target when the target size is an integer multiple of the source size.

## JavaScript API

The inspected code does not expose a public JavaScript method that directly accepts external Excel or HTML clipboard content. The feature is driven by browser paste events and internal data methods.

External text paste uses `pasteFromText(txt, error)`.

```js
// Internal GridJs data method used by the paste event path.
data.pasteFromText(textData, msg => xtoast('Tip', msg));
```

External HTML paste uses `pasteFromHTML(html, error)`.

```js
// Internal GridJs data method used when clipboard data includes text/html.
data.pasteFromHTML(htmlText, msg => xtoast('Tip', msg));
```

### Relevant functions
| Function / Location | Description | Parameters | Returns |
|----------|-------------|------------|---------|
| `act_w_paste_fromouter(e)` (`component/sheet.js`) | Handles the document paste event, checks edit/read and locked states, reads `clipboardData.types`, sends single text content to `pasteFromText`, and sends `text/html` content to `pasteFromHTML`. | `e`: paste event | `void` |
| `paste(what, evt)` (`component/sheet.js`) | Tries internal GridJs paste first. If no internal paste is available, it can read the browser clipboard and prefer `text/plain` before image data when more paste checking is needed. | `what`: `all`, `text`, or `format`; `evt`: optional paste event | `Promise<void>` |
| `pasteFromText(txt, error)` (`core/data_proxy.js`) | Splits text by `\r\n` and tab characters, checks the target range, writes cell text, and raises a batch cell update operation. | `txt`: clipboard text; `error`: callback | `void` |
| `pasteFromHTML(html, error)` (`core/data_proxy.js`) | Parses clipboard HTML into styled cell rows, checks the target range, calls `pasteFromHTMLAct`, and updates the selector range. | `html`: clipboard HTML; `error`: callback | `void` |
| `getCellsFromHTML(htmlText)` (`core/helper.js`) | Parses HTML with `DOMParser`, reads the first `table`, parses the `style` element, and returns a two-dimensional array of `{ txt, style }` cell objects from `tr` and `td` elements. | `htmlText`: clipboard HTML string | `Array<Array<{ txt, style }>>` |
| `cleanBrAndNewline(html)` (`core/helper.js`) | Removes extra newline characters from pasted Excel HTML cell content, keeping newlines that follow `<br>` by replacing the `<br>` with `\n`. | `html`: cell HTML string | `string` |
| `parseStyle(content)` (`core/helper.js`) | Parses CSS selector blocks from the clipboard `style` content and returns a selector-to-style map. | `content`: CSS text | `object` |
| `pasteFromHTMLAct(srcRange, rg, linescellwithstyle, raiseServerOpr = true)` (`core/data_proxy.js`) | Handles merged target behavior, extends rows or columns when needed, writes styled cells, and optionally raises the server operation. | `srcRange`, `rg`, `linescellwithstyle`, `raiseServerOpr` | `void` |
| `pasteCellsWithStyle(data, src, dstCellRange)` (`core/row.js`) | Writes parsed HTML cell text and applies supported style fields to each target cell. | `data`: DataProxy; `src`: parsed cell rows; `dstCellRange`: target range | `Array` |
| `setHtmlStyle(data, ri, ci, htmlStyle)` (`core/row.js`) | Converts supported HTML style properties into GridJs cell style fields and stores the style on the cell. | `data`, `ri`, `ci`, `htmlStyle` | `object` |
| `pasteHtmlCellsOpr(sheetName, cells, dstCellRange, linescellwithstyle)` (`core/data_proxy.js`) | Raises a `batchupdate` operation after HTML paste and includes `linescellwithstyle` when collaborative mode is enabled. | `sheetName`, `cells`, `dstCellRange`, `linescellwithstyle` | `void` |

## Common Questions

Q: Does GridJs paste from Excel through the HTML clipboard format?
A: Yes. The inspected paste handler looks for `text/html`, and the helper code parses an HTML `table`, `tr`, and `td` structure.

Q: What happens when the clipboard contains only plain text?
A: GridJs uses `pasteFromText`, splitting rows by `\r\n` and columns by tab characters.

Q: Which HTML style fields are applied to cells?
A: The inspected style conversion handles color, background, font size, font family, bold, italic, underline, horizontal alignment, vertical alignment, text wrapping, and `mso-number-format`.

Q: Does the inspected HTML paste code apply borders from Excel HTML?
A: No. Border examples appear in comments, but the inspected `setHtmlStyle` implementation does not assign border fields.

Q: Is there a public API for passing arbitrary HTML directly into GridJs?
A: Not in the inspected public declarations. The observed implementation uses browser paste events and internal data methods.
