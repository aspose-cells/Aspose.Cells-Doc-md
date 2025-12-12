---
title: Font Color Settings
description: Learn how to change font colors in Aspose.Cells GridJs using the toolbar, including preset swatches, custom colors, and UI behavior. This guide also covers the current JavaScript availability for programmatic color changes.
keywords: GridJs, Font Color, Text Color, Toolbar, Color Picker, UI, Front‑end
type: docs
weight: 210
url: /java/aspose-cells-gridjs/font-color-settings/
aliases:
  - /java/aspose-cells-gridjs/gridjs-font-color-configuration/
  - /java/aspose-cells-gridjs/font-color-configuration/
  - /java/aspose-cells-gridjs/text-color-settings/
  - /java/aspose-cells-gridjs/setting-font-color/
  - /java/aspose-cells-gridjs/changing-font-color/
---

{{% alert color="primary" %}}
The GridJs spreadsheet component provides a **Font Color** button on the toolbar that lets users apply preset or custom colours instantly to the selected cells. Changes are applied immediately without an extra “apply” step.
{{% /alert %}}

## Overview
Font colour determines the colour of the text displayed in a cell. GridJs implements this feature exclusively through a toolbar button with an attached colour‑picker dropdown. The button reflects the colour of the current selection, and the last used colour is remembered for quick re‑use.

## Accessing Font Color

1. **Locate the toolbar** at the top of the spreadsheet.
2. **Find the Font‑Color button** – an **A** character with a coloured bottom border indicating the active colour.  
   *Hover the mouse to see the tooltip “Font Color”.*

## UI Operations


**Apply the last used colour** 

1. Select one or more cells.
![](table_select_cells_with_content.png)
2. Click the coloured Font‑Color button.
![](font_color_toolbar_icon.png)
3. The stored colour is instantly written to the selected cell(s).
![](table_fontcolor_applied.png)

**Open the colour‑picker** 
1. Click the small ▼ arrow next to the Font‑Color button.
2. The colour‑palette dropdown appears below the button.
![](font_color_toolbar_dropdown.png)

**Choose a preset swatch** 
1. In the opened palette, click any colour swatch **or** the **Automatic** entry.
2. The button’s border updates to the chosen hue.
3. The colour is applied immediately to the current selection.
4. The palette closes automatically.



## Options & Behaviour

- **Automatic** – restores the default colour (usually black) defined by the spreadsheet theme.  
- **Preset swatches** – a set of frequently used colours displayed as square tiles.  
- **Last used colour** – remembered across toolbar re‑renders; clicking the main button re‑applies this colour without opening the palette.  
- **Immediate application** – no “OK” button is required; the colour is applied as soon as a swatch or custom colour is chosen.  

## JavaScript API
font colour changes can be achieved by setting the `color` attribute on a cell or range using the `setRangeAttr` method of the `data` object. After updating the attribute, call the `render` method to apply the changes visually.

```js
// Assume xs is your x_spreadsheet instance
xs = x_spreadsheet('#gridjs-demo-uid', option);
const range = {"sri":2,"sci":2,"eri":2,"eci":2}; // Define the cell range (row/col indices)
// Set the font color of a specific cell or range
xs.sheet.data.setRangeAttr(range, 'color', "red");
// Render the changes to update the UI
xs.sheet.table.render();
```



### Relevant functions (for reference only)

| Function | Description | Parameters | Returns |
|----------|-------------|------------|---------|
| `xs.sheet.data.setRangeAttr(range, attr, value)` | Modifies an attribute of the currently selected range. For font color, set `attr` to `'color'` and `value` to `red` (color name) or `#FF0000` (hex code). | `range` – **object** (contains `sri`, `sci`, `eri`, `eci` for start/end row/column).<br>`attr` – **string** (`'color'` only).<br>`value` – **string** (color name or hex code). | `undefined` (grid refreshes automatically). |
| `xs.sheet.table.render()` | Re-renders the table UI to reflect any data or style changes. | None. | `undefined`. |


## Tips & Best Practices

- **Quick reuse:** After selecting a custom colour, the button’s border updates, allowing you to re‑apply the same colour with a single click.
- **Consistent UI updates:** Switching cells automatically refreshes the toolbar state, ensuring you always see the correct current colour.
- **Protected ranges:** When the selection includes read‑only cells, the button is disabled – attempt to change colour only on writable cells.
- **Performance:** Colour changes are sent to the back‑end as part of a generic *style‑update* request, so they are lightweight and do not require a separate “apply” action.
- **Accessibility:** The tooltip “Font Color” remains visible even when the button is disabled, helping users understand the purpose of the control.

---