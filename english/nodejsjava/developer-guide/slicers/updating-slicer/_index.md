---
title: Updating Slicer with Node.js via Java
linktitle: Updating Slicer
type: docs
weight: 50
url: /nodejs-java/updating-slicer/
description: This article shows how to update a slicer to filter the data of the linked pivot table or table using Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells Node.js via Java, Update slicer Node.js, how to change the slicer Node.js, how to filter a pivot table by slicer in Node.js, Slicer selectItems, Slicer clearFilter, Slicer unselectItems.
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Updating a slicer means filtering the data of the pivot table or table that the slicer is connected to. When you select or unselect slicer items in Microsoft Excel, the linked pivot table or table is recalculated accordingly. With Aspose.Cells for Node.js via Java, you do not need to iterate the slicer cache items and refresh the slicer manually — the [**Slicer.selectItems(labels, append)**](https://reference.aspose.com/cells/nodejs/slicer/) method updates the slicer and recalculates the linked pivot table or table directly from the filter items:
- `Slicer.selectItems(labels, append)` — selects the specified labels and recalculates the linked pivot table or table. When `append` is `true`, the originally selected labels are kept and the specified labels are added to the selection; when `append` is `false`, all original selections are cleared and only the specified labels stay selected.
- `Slicer.unselectItems(labels)` — unselects part of the currently selected items.
- `Slicer.clearFilter()` — removes the filter and selects all items.

{{% alert color="primary" %}}
Starting from Aspose.Cells for Node.js via Java 26.10, the `SlicerCacheItem.Selected` property becomes read-only and its setter is no longer supported. Use the `Slicer.selectItems`, `Slicer.unselectItems`, and `Slicer.clearFilter` methods instead of setting `SlicerCacheItem.Selected` item by item.
{{% /alert %}}

## **How to Update Slicer**
The following sample code loads the [sample Excel file](67338475.xlsx) that contains an existing slicer connected to a pivot table. It selects only the "Blue" and "Pink" items of the slicer with `Slicer.selectItems(labels, false)` — the pivot table is recalculated directly from the filter items, without a manual `Slicer.refresh()` call. It then saves the workbook as the [output Excel file](67338476.xlsx). The following screenshot shows the effect of the sample code on the sample Excel file. As you can see in the screenshot, the pivot table shows only the filtered items.
![todo:image_alt_text](updating-slicer_1.png)

## **Sample Code**
Replace the current selection (only the specified labels stay selected) and recalculate the linked pivot table or table:

```javascript
const AsposeCells = require("aspose.cells");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Select only "Blue" and "Pink"; the linked pivot table or table
// is recalculated directly from the filter items.
slicer.selectItems(["Blue", "Pink"], false);
// Save the modified workbook.
workbook.save("out.xlsx");
```

Keep the currently selected labels and additionally select more items:

```javascript
const AsposeCells = require("aspose.cells");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], true);
```

Unselect part of the selected items:

```javascript
const AsposeCells = require("aspose.cells");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"]);
```

Remove the filter (select all items):

```javascript
const AsposeCells = require("aspose.cells");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Clear the filter; all slicer items become selected again.
slicer.clearFilter();
```

{{< app/cells/assistant language="nodejs-java" >}}