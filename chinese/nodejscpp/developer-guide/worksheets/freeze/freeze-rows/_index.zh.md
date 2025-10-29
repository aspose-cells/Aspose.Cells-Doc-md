---
title: 通过C++用Node.js冻结Excel工作表的顶行
linktitle: 冻结行
type: docs
weight: 190
url: /zh/nodejs-cpp/how-to-freeze-rows-of-excel-worksheet
description: 在本文中，您将学习如何使用带有C++ API的Node.js库以编程方式冻结Excel工作表的顶部行。
keywords: 通过C++的Node.js冻结顶部行。
---

## **介绍**

在本文中，我们将学习如何冻结顶部行。当您有大量数据在共同标题下时，在向下滚动工作表时无法看到标题。您可以冻结顶部行，以便即使在滚动其他数据时也能看到冻结部分。您可以轻松识别顶部的标题行。

## **在Excel中冻结行**

**![在Excel中冻结顶部行](Freeze-Rows.png)**

1. 如果您想冻结顶部行，则首先选择需要冻结的行以下的行。
2. 单击“查看”>“冻结窗格”
3. 在下拉菜单中，单击“冻结顶部行”。
4. 滚动时，第一行始终显示在顶部视图中。

**![冻结行](Frozen-Row.png)**

如您所见，第一行已被冻结；当您向下滚动时，第一行始终保持在视图顶部。

冻结行让您在查看大量数据时无需关注行标签。

## **使用Aspose.Cells for Node.js via C++冻结行**
使用Aspose.Cells for Node.js via C++轻松冻结行。 
请使用[**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-)方法在所选行处冻结行。
1.构建工作簿以打开文件或创建一个空文件。
2. 使用Worksheet.freezePanes()方法冻结第一行。
3.保存文件。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Freeze.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Freezing panes at the cell B2
workbook.getWorksheets().get(0).freezePanes("A2", 1, 0);

// Saving the file
workbook.save("frozen.xlsx");
```

附有[示例源Excel文件](../Freeze.xlsx)。
{{< app/cells/assistant language="nodejs-cpp" >}}
