---
title: Set Font Size
description: Guide to changing the font size of cells in the Aspose.Cells GridJs spreadsheet component using the toolbar and menubar controls.
keywords: GridJs, Font Size, Spreadsheet, Toolbar, Menubar, UI, Client-side
type: docs
weight: 200
url: /net/aspose-cells-gridjs/set-font-size/
aliases:
  - /net/aspose-cells-gridjs/font-size/
  - /net/aspose-cells-gridjs/adjust-font-size/
  - /net/aspose-cells-gridjs/text-font-size/
  - /net/aspose-cells-gridjs/format-font-size/
  - /net/aspose-cells-gridjs/font-size-control/
---

{{% alert color="primary" %}}

The **Set Font Size** feature lets end‑users change the text size of the selected cells directly in the browser. The component’s toolbar and menubar expose a ready‑made dropdown that lists common point sizes (e.g., 8 pt, 9 pt, 10 pt …). Selecting a size instantly updates the style of the active cell range.

{{% /alert %}}

## Overview
Changing font size is a core formatting operation. GridJs provides a **Font Size** dropdown in both the **Toolbar** (quick access) and the **Text** menu of the **Menubar** (menu‑driven access). The UI reflects the current cell’s font size, so the dropdown title always shows the active size.

## UI Operations
### Using the Toolbar
1. Locate the **Font Size** dropdown in the toolbar – it displays the current size (e.g., *11 pt*).  
2. Click the dropdown arrow to reveal the list of predefined sizes.  
3. Click the desired size (e.g., *14 pt*).  
4. The selected size is applied immediately to the currently selected cell or range, and the dropdown title updates to the new size.

![](toolbar-font-size.png)

### Using the Menubar
1. Open the **Text** menu on the menubar.  
2. Choose **Font Size** from the submenu – this opens the same size list as the toolbar dropdown.  
3. Pick the required size.  
4. The change is applied instantly, and the menubar entry shows the new size.
![](menubar-font-size.png)


### Synchronisation with Cell Selection
- When you move the selection to a different cell, the dropdown’s title automatically changes to reflect that cell’s font size.  
- If the selected range contains mixed sizes, the title shows a placeholder (e.g., *Multiple*), indicating that applying a new size will override the existing values.

## JavaScript API
text font changes can be achieved by setting the `font-size` attribute on a cell or range using the `setRangeAttr` method of the `data` object. After updating the attribute, call the `render` method to apply the changes visually.

```js
xs = x_spreadsheet('#gridjs-demo-uid', option);
const range = {"sri":2,"sci":2,"eri":2,"eci":2}; // Define the cell range (row/col indices)
// Set the text font size of a specific cell or range
xs.sheet.data.setRangeAttr(range, 'font-size', "14");
// Render the changes to update the UI
xs.sheet.table.render();
```



### Relevant functions 

| Function | Description | Parameters | Returns |
|----------|-------------|------------|---------|
| `xs.sheet.data.setRangeAttr(range, attr, value)` | Modifies an attribute of the currently selected range. For font size, set `attr` to `'font-size'` and `value` to the desired size in points (e.g., `"14"`). | `range` – **object** (contains `sri`, `sci`, `eri`, `eci` for start/end row/column).<br>`attr` – **string** (`'font-size'` only).<br>`value` – **string** (size in points). | `undefined` (grid refreshes automatically). |
| `xs.sheet.table.render()` | Re-renders the table UI to reflect any data or style changes. | None. | `undefined`. |

## Tips
- **Consistent Formatting** – Choose sizes from the dropdown to keep formatting uniform across the workbook.  
- **Batch Apply** – Select multiple cells before choosing a size to apply the same font size to the entire range in one step.  
- **Responsive Rendering** – The component automatically converts the selected point size to pixels, ensuring that the visual appearance matches the printed output.
