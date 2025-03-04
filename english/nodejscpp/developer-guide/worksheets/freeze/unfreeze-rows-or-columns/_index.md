---
title: Unfreeze Rows or Columns with Node.js via C++
linktitle: Unfreeze panes
type: docs
weight: 190
url: /nodejs-cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: In this article, you will learn how to unfreeze rows, columns, or panes of Excel Worksheets programmatically using Node.js API with C++.
keywords: Unfreeze panes, Unfreeze rows, Unfreeze columns, unFreeze window Node.js via C++.
---

## **Introduction**

In this article, we will learn how to unfreeze rows, columns, and panes. If worksheets in the Excel files are frozen, sometimes we want to unfreeze the worksheet or adjust frozen rows, columns, or panes.


## **In Excel**

1. Click View tab > Freeze Panes > Unfreeze Panes.

**![unfreeze panes in Excel](Unfreeze-Panes.png)**




## **Unfreeze Rows, Columns or Panes with Aspose.Cells for Node.js via C++**
It's simple to unfreeze panes with Aspose.Cells for Node.js via C++. Please use the [**Worksheet.unfreezePanes**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unfreezePanes) method to unfreeze panes.

1. Construct Workbook to open the frozen file.
2. Unfreeze panes with Worksheet.unfreezePanes() method.
3. Save the file.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const frozenFilePath = path.join(dataDir, "Frozen.xlsx");

const workbook = new AsposeCells.Workbook(frozenFilePath); 
workbook.getWorksheets().get(0).unFreezePanes();
workbook.save("Unfrozen.xlsx");
```

Attached [sample source Excel file](Frozen.xlsx).
