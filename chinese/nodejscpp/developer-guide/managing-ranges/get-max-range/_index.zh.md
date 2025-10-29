---  
title: 使用 C++ 在 Node.js 中获取工作表中的最大范围  
linktitle: 获取工作表中的最大范围  
type: docs  
weight: 360  
url: /zh/nodejs-cpp/get-max-range-in-a-worksheet/  
description: 本文描述了如何使用 Aspose.Cells for Node.js via C++ 获取 Excel 文件的最大范围、最大数据范围和最大显示范围。  
---  

{{% alert color="primary" %}}  

在从工作表读取数据时，我们需要知道最大的区域。  

在从工作表复制所有数据时，我们需要知道最大的区域。  

在导出指定区域为HTML和PDF时，我们需要知道最大区域。  

Aspose.Cells for Node.js via C++ 提供了多种方法来查找工作表中的最大范围。  

{{% /alert %}}  

## **获取最大范围**  
在Aspose.Cells中，如果初始化了[**row**](https://reference.aspose.com/cells/nodejs-cpp/row/)和[**column**](https://reference.aspose.com/cells/nodejs-cpp/column/)对象，这些行和列将被计入最大区域，即使空行或空列没有数据。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();
const sheet = worksheets.get(0);

// Gets the max data range.
let maxRow = sheet.getCells().getMaxRow();
let maxColumn = sheet.getCells().getMaxColumn();
// The range is A1:B3.
let range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);

sheet.getCells().get("A10").putValue(null);

maxRow = sheet.getCells().getMaxRow();
maxColumn = sheet.getCells().getMaxColumn();
// The range is updated to A1:B10.
range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);
```  

## **获取最大数据范围**  
在大多数情况下，我们只需要获取包含所有数据的所有范围，即使范围外的空单元格被格式化。  
以及有关形状、表格和数据透视表的设置将被忽略。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();
const sheet = worksheets.get(0);

// Gets the max data range.
let maxRow = sheet.getCells().getMaxDataRow();
let maxColumn = sheet.getCells().getMaxDataColumn();
// The range is A1:B3.
let range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);

sheet.getCells().get("A10").putValue(null);

maxRow = sheet.getCells().getMaxDataRow();
maxColumn = sheet.getCells().getMaxDataColumn();
// The range is still A1:B3.
range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);
```  

## **获取最大显示范围**  
当我们将工作表中的所有数据导出到 HTML、PDF 或图像时，需要获取一个包含所有可见对象的区域，包括数据、样式、图形、表格和数据透视表。  
以下代码演示如何将最大显示范围渲染为HTML：  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Gets the max display range.
const range = worksheets.get(0).getCells().getMaxDisplayRange();

// Save the range to html
const saveOptions = new AsposeCells.HtmlSaveOptions();
saveOptions.setExportActiveWorksheetOnly(true);
saveOptions.setExportArea(AsposeCells.CellArea.createCellArea(range.getFirstRow(), range.getFirstColumn(), range.getFirstRow() + range.getRowCount() - 1, range.getFirstColumn() + range.getColumnCount() - 1));

// Save the range.
workbook.save("html.html", saveOptions);
```  

这是 [源 Excel 文件](Book1.xlsx)。  

{{< app/cells/assistant language="nodejs-cpp" >}}
