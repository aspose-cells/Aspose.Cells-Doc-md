---
title: 使用Node.js和C++拆分Excel工作表屏幕
linktitle: 分割屏幕
type: docs
weight: 190
url: /zh/nodejs-cpp/how-to-split-screen-of-excel-worksheet
description: 在本文中，您将学习如何通过编程方式使用Node.js C++插件将工作表分成两部分或四部分，以显示特定的行和/或列。
keywords: 冻结顶部行，冻结顶部行。
---

## **介绍**

在本文中，我们将学习如何通过分屏将工作表分成两部分或四部分，以显示特定的行和/或列。在处理大型数据集时，我们需要同时查看同一工作表中的几个区域以便比较不同的数据子集。分屏功能可以满足您的需求。

## **如何在Excel中分割屏幕**
要将工作表分割成两个或四个部分，请按照以下操作：

1. 选择要分割的行/列/单元格之前的位置。
2. 在“查看”选项卡上，在“窗口”组中，单击“拆分”按钮。

**![拆分屏幕](Split-Screen.png)**

## **在列上垂直拆分工作表**

要在电子表格的两个区域垂直分隔，选择要在其右侧出现分隔的列，并在Excel中单击“拆分”按钮。

使用Aspose.Cells for Node.js via C++，轻松地在列上垂直拆分工作表，只需选择顶行的一个单元格作为活动单元格，然后使用[**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--)方法进行拆分。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets C1 cell in the top row as the active cell.
sheet.setActiveCell("C1");

// Split worksheet vertically on columns
sheet.split();
```

## **在行上水平拆分工作表**
要在Excel中水平分隔您的Excel窗口，请选择要在其下方发生分隔的行。

使用Aspose.Cells for Node.js via C++，轻松地在行上水平拆分工作表，只需选择左列的一个单元格作为活动单元格，然后使用[**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--)方法进行拆分。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets A6 cell in the left column as the active cell.
sheet.setActiveCell("A6");

// Split worksheet horizontally on rows
sheet.split();

workbook.save("dest.xlsx");
```

## **将工作表分成四部分**
要同时查看同一工作表的四个不同部分，请在Excel中垂直和水平拆分屏幕。

利用Aspose.Cells for Node.js via C++，轻松在列上垂直拆分工作表，只需选择不在第一行和第一列的一个单元格作为活动单元格，然后使用[**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--)方法进行拆分。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets E6 cell as the active cell.
sheet.setActiveCell("E6");

// Split worksheet into four parts
sheet.split();
```

## **如何移除拆分**
要移除工作表的拆分，只需再次单击“拆分”按钮。

Aspose.Cells for Node.js via C++提供了一个[**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--)方法来取消拆分设置。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Remove split.
sheet.removeSplit();

// Split worksheet into four parts
sheet.split();
```

{{< app/cells/assistant language="nodejs-cpp" >}}
