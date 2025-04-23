---
title: 如何在没有Excel的情况下通过Node.js和C++检查冻结状态
linktitle: 冻结状态
type: docs
weight: 190
url: /zh/nodejs-cpp/how-to-check-frozen-state-of-excel-worksheet
description: 在本文中，您将学习如何使用带有C++库的Node.js以编程方式检查Excel工作表的冻结状态。

---

## **介绍**

在本文中，我们将学习如何以编程方式检查Excel工作表的冻结状态。我们可以轻松地在MS Excel中查找工作表是否被冻结或拆分。但是，有没有办法用Node.js查找它是否被冻结或拆分？我们可以用Aspose.Cells for Node.js via C++轻松实现。

## **窗格是否冻结**
利用Aspose.Cells for Node.js via C++，我们可以检查窗口是否被冻结以及多少行和列被锁定。

请使用[**Worksheet.getPaneState()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPaneState--)属性检查窗口面板的状态，并使用[**Worksheet.getFreezedPanes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFreezedPanes--)方法获取锁定的行和列。
1.构建工作簿以打开文件。
2.检查工作表是否被冻结。
3. 获取锁定的行和列。

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
