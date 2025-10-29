---  
title: 使用 Node.js 通过 C++ 复制行和列  
linktitle: 复制行和列  
type: docs  
weight: 40  
url: /zh/nodejs-cpp/copying-rows-and-columns/  
description: 本文展示了如何通过 Aspose.Cells for Node.js via C++ API 复制行和列。  
keywords: 使用 C++ 在 Node.js 中复制行和列，复制行，复制列，使用 Aspose.Cells for Node.js via C++ 粘贴多行多列，粘贴单个行或列。  
---  

## **介绍**  

有时，您需要在不复制整个工作表的情况下复制工作表中的行和列。使用Aspose.Cells，可以在工作簿内部或工作簿之间复制行和列。  
复制行（或列）时，其中包含的数据，包括更新的引用的公式和值，注释，格式，隐藏单元格，图像以及其他绘图对象也会被复制。  

## **使用Microsoft Excel如何复制行和列**  

1. 选择要复制的行或列。  
1. 要复制行或列，请单击 **标准** 工具栏上的 **复制**，或按 **CTRL**+**C**。  
1. 选择要复制所选内容下方或右侧的行或列。  
1. 复制行或列时，单击 **已复制的单元格** 在 **插入** 菜单上。  

{{% alert color="primary" %}}  
如果您在**标准**工具栏上单击**粘贴**，或者按**Ctrl**+**V**键，而不是在**插入**菜单上单击命令，则目标单元格的任何内容都将被替换。  
{{% /alert %}}  

## **如何使用Microsoft Excel的粘贴选项粘贴行和列**  

1. 选择包含您要复制的数据或其他属性的单元格。  
1. 在主页选项卡上，单击**复制**。  
1. 单击要在其中**粘贴**所复制内容的区域中的第一个单元格。  
1. 在主页选项卡上，单击**粘贴**旁边的箭头，然后选择**粘贴**特殊。  
1. 选择您想要的**选项**。  

## **使用 Aspose.Cells for Node.js via C++ 复制行和列的方法**  

## **如何复制单行**  

Aspose.Cells 提供了 [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) 方法，来自 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 类。该方法复制源行的所有类型数据，包括公式、数值、评论、单元格格式、隐藏单元格、图像和其他绘图对象到目标行。  

[**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) 方法的参数如下：  

- 源 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 对象，  
- 源行索引, 和  
- 目标行索引.  

使用此方法在工作表内或到另一个工作表复制一行。[**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) 方法的功能与 Microsoft Excel 类似。例如，你无需显式设置目标行的高度，该值也会被复制。  

下面的示例演示如何在工作表中复制一行。它使用一个模板 Microsoft Excel 文件，将第二行（包含数据、格式、批注、图片等）复制并粘贴到同一工作表的第12行。  

你可以跳过获取源行高度的步骤（使用 [**Cells.getRowHeight(number, boolean, CellsUnitType)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRowHeight-number-boolean-cellsunittype-) 方法）以及设置目标行高度（使用 [**Cells.setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-) 方法），因为 [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) 方法会自动处理行高度。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing excel file.
const excelWorkbook1 = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Get the first worksheet in the workbook.
const wsTemplate = excelWorkbook1.getWorksheets().get(0);

// Copy the second row with data, formattings, images and drawing objects
// To the 16th row in the worksheet.
wsTemplate.getCells().copyRow(wsTemplate.getCells(), 1, 15);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  
在复制行时，重要的是注意相关的图像、图表或其他绘图对象，因为这与 Microsoft Excel 相同：  

1. 如果源行索引为5，则如果它包含在三行内（起始行索引为4，结束行索引为6），则图像、图表等会被复制。  
1. 目标行中现有的图像、图表等不会被移除。  
{{% /alert %}}  

## **如何复制多行**  

你也可以在使用 [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) 方法复制多行时，传入一个整数参数来指定要复制的源行数。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "aspose-sample.xlsx");

// Create an instance of Workbook class by loading the existing spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Get the cells collection of first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Copy the first 3 rows to 7th row
cells.copyRows(cells, 0, 6, 3);

// Save the result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

## **如何复制列**  

Aspose.Cells 提供 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 类中的 [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) 方法，该方法可以复制所有类型的数据，包括带有更新引用的公式、值、批注、单元格格式、隐藏的单元格、图片和其他绘图对象，从源列到目标列。  

[**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) 方法的参数如下：  

- 源 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 对象，  
- 源列索引, 和  
- 目标列索引.  

使用 [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) 方法在工作表内或到另一个工作表复制列。  

该示例将一个工作表中的列复制到另一个工作簿的工作表中。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook(filePath);

// Get the first worksheet in the book.
const ws1 = excelWorkbook1.getWorksheets().get(0);

// Copy the first column from the first worksheet of the first workbook into
// The first worksheet of the second workbook.
ws1.getCells().copyColumn(ws1.getCells(), ws1.getCells().getColumns().get(0).getIndex(), ws1.getCells().getColumns().get(2).getIndex());

// Autofit the column.
ws1.autoFitColumn(2);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "output.xls"));
```  

## **如何复制多列**  

类似于 [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) 方法，Aspose.Cells API 还提供 [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-) 方法，用于将多个源列复制到新位置。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an instance of Workbook class by loading the existing spreadsheet
const workbook = new AsposeCells.Workbook(path.join(dataDir, "aspose-sample.xlsx"));

// Get the first worksheet's cells collection
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

// Copy the first 3 columns to the 7th column
cells.copyColumns(cells, 0, 6, 3);

// Save the result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

## **如何粘贴行和列并设置粘贴选项**  

Aspose.Cells 现在提供 [**PasteOptions**](https://reference.aspose.com/cells/nodejs-cpp/pasteoptions/)，使用函数 [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) 和 [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-)。它允许设置类似于 Excel 的适当粘贴选项。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleChangeChartDataSource.xlsx"));

// Access the first sheet which contains chart
const source = workbook.getWorksheets().get(0);

// Add another sheet named DestSheet
const destination = workbook.getWorksheets().add("DestSheet");

// Set CopyOptions.ReferToDestinationSheet to true
const options = new AsposeCells.CopyOptions();
options.setReferToDestinationSheet(true);

// Set PasteOptions
const pasteOptions = new AsposeCells.PasteOptions();
pasteOptions.setPasteType(AsposeCells.PasteType.Values);
pasteOptions.setOnlyVisibleCells(true);

// Copy all the rows of source worksheet to destination worksheet which includes chart as well
// The chart data source will now refer to DestSheet
destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options, pasteOptions);

// Save workbook in xlsx format
workbook.save(path.join(outputDir, "outputChangeChartDataSource.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
