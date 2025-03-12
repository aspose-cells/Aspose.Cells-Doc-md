---
title: How to check Frozen State without Excel using Node.js via C++
linktitle: Frozen State
type: docs
weight: 190
url: /nodejs-cpp/how-to-check-frozen-state-of-excel-worksheet
description: In this article, you will learn how to check the frozen state of an Excel worksheet programmatically using Node.js with C++ library.

---

## **Introduction**

In this article, we will learn how to check the frozen state of an Excel worksheet programmatically. We can simply find whether the worksheet is frozen or split in MS Excel. But is there a way to find whether it is frozen or split with Node.js? We can simply do it with Aspose.Cells for Node.js via C++.

## **Are Window Panes Frozen**
With Aspose.Cells for Node.js via C++, we can check whether the window is frozen and how many rows and columns are locked.

Please use the [**Worksheet.getPaneState()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPaneState--) property to check the state of window panes and get locked rows and columns with the [**Worksheet.getFreezedPanes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFreezedPanes--) method.
1. Construct Workbook to open the file.
2. Check whether the worksheet is frozen.
3. Get the locked rows and columns.

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Frozen.xlsx");

// Loads the workbook which contains frozen panes
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Check whether worksheet is frozen.
if (sheet.getPaneState() === AsposeCells.PaneStateType.Frozen || sheet.getPaneState() === AsposeCells.PaneStateType.FrozenSplit) {
let row, column, rows, columns;
// Gets locked rows and columns.
sheet.getFreezedPanes().forEach((value) => {
row = value[0];
column = value[1];
rows = value[2];
columns = value[3];
```  
