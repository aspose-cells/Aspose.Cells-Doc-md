---  
title: 通过 Node.js 使用 C++ 自动调整行和列的宽度  
linktitle: 自动调整行和列  
type: docs  
weight: 20  
url: /zh/nodejs-cpp/autofit-rows-and-columns/  
description: 本文展示了如何使用Aspose.Cells for Node.js via C++自动调整单元格范围内的行、列、合并单元格的行以及行的宽度。  
keywords: 使用 C++ 在 Node.js 中自动调整行宽，使用 C++ 在 Node.js 中自动调整列宽，使用 C++ 在 Node.js 中自动调整范围内的行，使用 C++ 在 Node.js 中自动调整合并单元格的行  
---  

{{% alert color="primary" %}}  
微软 Excel 允许根据内容自动调整单元格的宽度和高度。此功能也可以通过Aspose.Cells for Node.js via C++实现，开发者可以在运行时自动调整单元格的尺寸。  
{{% /alert %}}  

## **自动调整**  

Aspose.Cells 提供了 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类，表示一个 Microsoft Excel 文件。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类包含一个 [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) 集合，可以访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类提供了管理工作表的多种属性和方法。本文介绍了如何使用 [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类自动调整行或列宽。  

### **自动调整行 - 简单**  

最简单的自动调整行宽和列高的方法是调用[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类的[**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-)方法。[**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-)方法以行索引作为参数，调整特定行。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileBuffer = fs.readFileSync(inputPath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the 3rd row of the worksheet
worksheet.autoFitRow(1);

// Saving the modified Excel file
const outputPath = path.join(dataDir, "output.xlsx");
workbook.save(outputPath);
```  

### **如何在单元格范围内自动调整行**  

一行由多个列组成。Aspose.Cells允许开发者通过调用[**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-number-number-)方法的重载版本，根据该行中某个范围的单元格内容自动调整行高。参数如下：  

- **行索引**，即要自动调整的行的索引。  
- **第一个列索引**，即行的第一个列的索引。  
- **最后列索引**，指行的最后一列的索引。  

[**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-number-number-)方法会检查该行所有列的内容，然后自动调整行高。  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileData = fs.readFileSync(inputPath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileData);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the 3rd row of the worksheet
worksheet.autoFitRow(1, 0, 5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

### **如何在一系列单元格中自动调整列**  

一列由许多行组成。通过调用接受以下参数的 [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) 方法的重载版本，可以根据某个范围内的单元格内容自动调整列宽：  

- **列索引**，要自动调整的列的索引。  
- **第一行索引**，列的第一行的索引。  
- **最后行索引**，列的最后一行的索引。  

[**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-)方法会检查该列所有行的内容，然后自动调整列宽。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const workbook = new AsposeCells.Workbook(fs.readFileSync(inputPath));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the Column of the worksheet
worksheet.autoFitColumn(4);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

### **如何为合并单元格自动调整行高**  

使用 Aspose.Cells，即使单元格已合并，也可以自动调整行的宽度，使用 [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) API。[**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) 类提供 [**AutoFitterOptions.getAutoFitMergedCellsType()**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getAutoFitMergedCellsType--) 属性，可用于自动调整合并单元格的行宽。[**AutoFitterOptions.getAutoFitMergedCellsType()**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getAutoFitMergedCellsType--) 接受 [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/nodejs-cpp/autofitmergedcellstype) 枚举，其成员如下。  

- None：忽略合并的单元格。  
- FirstLine：只扩展第一行的高度。  
- 最后一行：只扩展最后一行的高度。  
- 每行：只扩展每一行的高度。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(dataDir, "output");

// Instantiate a new Workbook
const wb = new AsposeCells.Workbook();

// Get the first (default) worksheet
const worksheet = wb.getWorksheets().get(0);

// Create a range A1:B1
const range = worksheet.getCells().createRange(0, 0, 1, 2);

// Merge the cells
range.merge();

// Insert value to the merged cell A1
worksheet.getCells().get(0, 0).setValue("A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

// Create a style object
const style = worksheet.getCells().get(0, 0).getStyle();

// Set wrapping text on
style.setIsTextWrapped(true);

// Apply the style to the cell
worksheet.getCells().get(0, 0).setStyle(style);

// Create an object for AutoFitterOptions
const options = new AsposeCells.AutoFitterOptions();

// Set auto-fit for merged cells
options.setAutoFitMergedCellsType(AsposeCells.AutoFitMergedCellsType.EachLine);

// Autofit rows in the sheet (including the merged cells)
worksheet.autoFitRows(options);

// Save the Excel file
wb.save(path.join(outputDir, "AutofitRowsforMergedCells.xlsx"));
```  

{{% alert color="primary" %}}  
你还可以尝试使用接受行/列范围和 [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) 实例的 [**autoFitRows**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRows-number-number-AutoFitterOptions-) 和 [**autoFitColumns**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumns-number-number-AutoFitterOptions-) 方法的重载版本，以按您的需求自动调整选定的行/列。  

上述方法的签名如下：  

1. autoFitRows（int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) 选项)  
1. autoFitColumns（int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) 选项)  
{{% /alert %}}  

## **重要知识**  

{{% alert color="primary" %}}  
如果单元格被合并，那么自动调整方法将不会应用，这与 Microsoft Excel 中的行为相同。你可以通过使用自动筛选 API 来绕过这一点。此外，如果单元格中的文本换行，也不会应用 [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) 方法。还需要注意的是，*autoFit* 方法是耗时的。因此，应尽可能少调用这些方法，以确保你的应用效率。  
{{% /alert %}}  

## **高级主题**  
- [为合并单元格自动调整行高](/cells/zh/nodejs-cpp/autofit-rows-for-merged-cells/)  

