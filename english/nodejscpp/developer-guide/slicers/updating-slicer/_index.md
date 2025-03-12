---
title: Updating Slicer with Node.js via C++
linktitle: Updating Slicer
type: docs
weight: 50
url: /nodejs-cpp/updating-slicer/
description: This article shows how to update linked pivot tables by updating slicer using Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells Node.js via C++, Update slicer Node.js, how to change the slicer Node.js, how to adjust the slicer in Node.js, how to select or unselect the slicer items Node.js via C++.
---

## **Possible Usage Scenarios**

If you want to update a slicer in Microsoft Excel, select or unselect its items, and it will then update the slicer table or pivot table accordingly. Please use [**Slicer.getSlicerCacheItems()**](https://reference.aspose.com/cells/nodejs-cpp/slicercache/#getSlicerCacheItems--) to select or unselect slicer items with Aspose.Cells and then call [**Slicer.refresh()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#refresh--) method to update the slicer table or pivot table.

## **How to Update Slicer**

The following sample code loads the [sample Excel file](67338475.xlsx) that contains an existing slicer. It unselects the 2nd and 3rd items of the slicer and refreshes the slicer. It then saves the workbook as [output Excel file](67338476.xlsx). The following screenshot shows the effect of the sample code on the sample Excel file. As you can see in the screenshot, refreshing the slicer with selected items has also refreshed the pivot table accordingly.

![todo:image_alt_text](updating-slicer_1.png)

## **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleUpdatingSlicer.xlsx");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);

// Access the slicer items.
const scItems = slicer.getSlicerCache().getSlicerCacheItems();

const items = slicer.getSlicerCache().getSlicerCacheItems();

for (let i = 0; i < items.getCount(); i++) {
const item = items.get(i);
if (item.getValue() === "Pink" || item.getValue() === "Green") {
item.setSelected(false);
}
}
slicer.refresh();
wb.save("out.xlsx");
```
