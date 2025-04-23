---
title: 通过Node.js与C++合并与拆分单元格
linktitle: 合并和分割单元格
description: Aspose.Cells是一个用于操作电子表格文件的Node.js库，支持合并和拆分单元格。本文章将介绍如何使用Aspose.Cells库合并和拆分单元格，并提供定制合并单元格样式的选项。
keywords: Aspose.Cells、Node.js库、电子表格、合并单元格、拆分单元格、样式设置、自定义样式
type: docs
weight: 190
url: /zh/nodejs-cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells支持此功能，还可以在工作表中合并单元格。您还可以取消合并或拆分合并的单元格。合并单元格的单元格引用是原始选择范围中左上角单元格的引用。

{{% /alert %}} 
## **介绍**
并非总是希望每行或每列中都有相同数量的单元格。例如，您可能希望在一个跨越多个列的单元格中放置标题。或者，如果创建发票，则可能希望总计列中的列数较少。将两个或多个单元格合并成一个单元格，以实现此目的。Microsoft Excel允许用户选择文件并将其合并以按照自己的方式构造电子表格。

{{% alert color="primary" %}} 

注意在合并单元格时，只会保留左上角单元格的数据。如果区域内的其他单元格中有数据，这些数据会被删除。同样，格式也基于参考单元格，因此在合并单元格时，应用于合并区域左上角单元格的格式设置将被应用于合并后的单元格。拆分时，新单元格保持其原有格式设置。

{{% /alert %}} 
## **在工作表中合并单元格**
### **在Microsoft Excel中合并单元格**
以下步骤描述如何在MS Excel中合并工作表中的单元格。

1. 将要复制的数据复制到范围内左上角的单元格中。
1. 选择要合并的单元格。
1. 要合并行或列中的单元格并将单元格内容居中，点击**合并和居中**图标上的**格式**工具栏。

### **使用Aspose.Cells合并单元格**
Aspose.Cells.Cells类具有一些实用的方法，例如`merge()`方法，可以将指定区域内的单元格合并为一个单元格。

以下示例显示了如何在工作表中合并单元格（C6:E7）。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a Workbook.
const wbk = new AsposeCells.Workbook();

// Create a Worksheet and get the first sheet.
const worksheet = wbk.getWorksheets().get(0);

// Create a Cells object to fetch all the cells.
const cells = worksheet.getCells();

// Merge some Cells (C6:E7) into a single C6 Cell.
cells.merge(5, 2, 2, 3);

// Input data into C6 Cell.
cells.get(5, 2).putValue("This is my value");

// Create a Style object to fetch the Style of C6 Cell.
const style = cells.get(5, 2).getStyle();

// Create a Font object
const font = style.getFont();

// Set the name.
font.setName("Times New Roman");

// Set the font size.
font.setSize(18);

// Set the font color
font.setColor(AsposeCells.Color.Blue);

// Bold the text
font.setIsBold(true);

// Make it italic
font.setIsItalic(true);

// Set the background color of C6 Cell to Red
style.setForegroundColor(AsposeCells.Color.Red);
style.setPattern(AsposeCells.BackgroundType.Solid);

// Apply the Style to C6 Cell.
cells.get(5, 2).setStyle(style);

// Save the Workbook.
wbk.save(path.join(dataDir, "mergingcells.out.xls"));
```

## **取消合并（拆分）合并的单元格**
### **使用Microsoft Excel**
以下是使用Microsoft Excel拆分合并单元格的步骤。

1. 选择已合并的单元格。
   当单元格已合并时，在**格式**工具栏上选择**合并和居中**。
1. 在**格式**工具栏上点击**合并和居中**。

### **使用Aspose.Cells**
Aspose.Cells.Cells类具有名为`unmerge()`的方法，可以将合并的单元格拆分回原始状态。该方法通过合并单元格范围的引用进行拆分。

以下示例显示了如何拆分合并的单元格（C6）。该示例使用上一个示例中创建的文件，并拆分了合并的单元格。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a Workbook.
// Open the excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "mergingcells.xls"));

// Create a Worksheet and get the first sheet.
const worksheet = workbook.getWorksheets().get(0);

// Create a Cells object to fetch all the cells.
const cells = worksheet.getCells();

// Unmerge the cells.
cells.unMerge(5, 2, 2, 3);

// Save the file.
workbook.save(path.join(dataDir, "unmergingcells.out.xls"));
```

## **高级主题**
- [在工作表中检测合并的单元格](/cells/zh/nodejs-cpp/detect-merged-cells-in-a-worksheet/)
