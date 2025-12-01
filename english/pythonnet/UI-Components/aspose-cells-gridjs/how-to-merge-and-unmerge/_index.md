---
title: How to Merge and Unmerge
description: Learn how to merge and unmerge cells in Aspose.Cells.GridJs UI and JavaScript API. This guide covers UI actions, JavaScript calls
keywords: Aspose,Cells,GridJs, merge cells, unmerge cells, 
type: docs
weight: 190
url: /python-net/aspose-cells-gridjs/how-to-merge-and-unmerge/
aliases:
  - /python-net/aspose-cells-gridjs/merge-and-unmerge/
  - /python-net/aspose-cells-gridjs/how-to-merge-cells/
  - /python-net/aspose-cells-gridjs/how-to-unmerge-cells/
  - /python-net/aspose-cells-gridjs/cell-merge-and-unmerge/
  - /python-net/aspose-cells-gridjs/merge-unmerge-cells/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
**Cell Merge and Unmerge** lets you combine a rectangular range of cells into a single larger cell or split a previously merged cell back into its original grid. This is useful for titles, section headers, summary rows, or any layout where a value should span multiple columns or rows.
{{% /alert %}}

## 1. Feature Overview
Merging creates one visual cell that spans several columns and/or rows while preserving the value and style of the top‑left cell in the selected range. Un‑merging restores the original individual cells, keeping the data that was stored in the top‑left cell. 

### When to use
- Add a heading that stretches across the worksheet width.  
- Combine cells for a total row that should be visually distinct.  
- Split a merged area when the layout needs to change.

---

## 2. Client‑side Usage

### 2.1 UI Operations
Follow these steps directly in the GridJs spreadsheet UI.

1. **Select a rectangular range** – click the first cell, drag to the last cell. 
   ![selection of cell range to merge](select-range.gif)

2. **Click "Merge" icon in toolbar** – when icon is clicked, it toggles to "Un‑merge" if the selection is already merged.
   ![use merge icon to set merge](set-merge.gif)  

3. **Click "Merge" icon to un‑merge** – if the selected range is merged, clicking the icon again will restore the individual cells.  
   ![use merge icon to unmerge](set-unmerge.gif)  

The spreadsheet automatically redraws the affected area, showing a single merged cell or the restored individual cells.

---

### 2.2 JavaScript API 

Below is a complete GridJs initialization followed by the exact calls you need to merge or unmerge cells programmatically.

```javascript
// ------------------------------------------------------------
// 1️⃣ Initialize the x‑spreadsheet instance
// ------------------------------------------------------------
xs = x_spreadsheet('#gridjs-demo-uid', option);

function mergeRange(range) {
    // Apply the merge
    xs.sheet.data.setRangeAttr(range,'merge', true);
    // Refresh the grid to show changes
    xs.sheet.table.render();
}

function unmergeRange(range) {
    xs.sheet.data.setRangeAttr(range,'merge', false);
    xs.sheet.table.render();
}

// ------------------------------------------------------------
// 4️⃣ Example usage
// ------------------------------------------------------------
// Merge cells A1:B2
mergeRange({sri:0, sci:0, eri:1, eci:1});

// Later, un‑merge the same area
unmergeRange({sri:0, sci:0, eri:1, eci:1});
```

#### API Reference

| Function | Description | Parameters | Returns |
|----------|-------------|------------|---------|
| `xs.sheet.data.setRangeAttr(range, attr, value)` | Modifies an attribute of the currently selected range. For merging, set `attr` to `'merge'` and `value` to `true` (merge) or `false` (un‑merge). | `range` – **object** (contains `sri`, `sci`, `eri`, `eci` for start/end row/column).<br>`attr` – **string** (`'merge'` only).<br>`value` – **boolean** (`true` to merge, `false` to un‑merge). | `undefined` (grid refreshes automatically). |


> **Tip** – The merge icon is toggleable. If the selected range is already merged, clicking it will un‑merge the cells.
> **For live demos and more examples, visit:** <https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs>


