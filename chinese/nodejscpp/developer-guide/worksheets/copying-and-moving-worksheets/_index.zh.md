---
title: 使用C++在Node.js中复制和移动工作表
linktitle: 复制和移动工作表
type: docs
weight: 10
url: /zh/nodejs-cpp/copying-and-moving-worksheets/
description: 本文包含示例代码，描述如何使用C++的Node.js API在Excel工作簿内以及跨工作簿编程复制和移动工作表。
keywords: 复制工作表Node.js，移动工作表Node.js
---

{{% alert color="primary" %}}

有时，您确实需要一些具有共同格式和数据的工作表。例如，如果您在季度预算上工作，您可能希望创建一个包含具有相同列标题、行标题和公式的工作表的工作簿。有一种方法可以做到这一点：先创建一个工作表，然后进行复制。

Aspose.Cells for Node.js via C++支持在工作簿内或之间复制和移动工作表。包含数据、格式、表格、矩阵、图表、图像及其他对象的工作表，复制时精度最高。

{{% /alert %}}

## **使用Microsoft Excel移动或复制工作表**

以下是在Microsoft Excel中在工作簿内部或不同工作簿之间复制和移动工作表所涉及的步骤。

1. 要将工作表移动或复制到另一个工作簿中，请打开将要接收工作表的工作簿。
1. 切换到包含您想要移动或复制的工作表的工作簿，然后选择这些工作表。
1. 在“编辑”菜单上，单击“移动或复制工作表”
1. 在“选择工作簿”对话框中，单击要接收工作表的工作簿。
1. 要将所选工作表移动或复制到新工作簿中，请单击“新建工作簿”
1. 在“工作表之前”框中，单击要在其之前插入移动或复制的工作表。
1. 要复制工作表而不是移动它们，请选择“创建副本”复选框。

### **使用Aspose.Cells for Node.js via C++在工作簿内复制工作表**

Aspose.Cells提供了一个重载方法，[**Aspose.Cells.WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#addCopy-number-)，用于将工作表添加到集合并从现有工作表复制数据。该方法的一个版本将源工作表的索引作为参数。另一个版本将源工作表的名称作为参数。

以下示例显示了如何在工作簿内复制现有工作表。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xls");

// Open an existing Excel file.
const wb = new AsposeCells.Workbook(inputPath);

// Create a Worksheets object with reference to
// the sheets of the Workbook.
const sheets = wb.getWorksheets();

// Copy data to a new sheet from an existing
// sheet within the Workbook.
sheets.addCopy("Sheet1");

// Save the Excel file.
wb.save(path.join(dataDir, "CopyWithinWorkbook_out.xls"));
```

### **在工作簿之间复制工作表**

Aspose.Cells提供一种方法[**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#copy-worksheet-)，用于复制数据和格式，从源工作表到另一个工作表，支持在或跨工作簿中操作。该方法需要源工作表对象作为参数。

以下示例显示了如何将一个工作表从一个工作簿复制到另一个工作簿。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xls");

// Create a Workbook.
// Open a file into the first book.
const excelWorkbook0 = new AsposeCells.Workbook(inputPath);

// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook();

// Copy the first sheet of the first book into second book.
excelWorkbook1.getWorksheets().get(0).copy(excelWorkbook0.getWorksheets().get(0));

// Save the file.
excelWorkbook1.save(path.join(dataDir, "CopyWorksheetsBetweenWorkbooks_out.xls"));
```

以下示例显示了如何将一个工作表从一个工作簿复制到另一个。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook.
const excelWorkbook0 = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const ws0 = excelWorkbook0.getWorksheets().get(0);

// Put some data into header rows (A1:A4)
for (let i = 0; i < 5; i++) {
ws0.getCells().get(i, 0).putValue(`Header Row ${i}`);
}

// Put some detail data (A5:A999)
for (let i = 5; i < 1000; i++) {
ws0.getCells().get(i, 0).putValue(`Detail Row ${i}`);
}

// Define a pagesetup object based on the first worksheet.
const pagesetup = ws0.getPageSetup();

// The first five rows are repeated in each page...
// It can be seen in print preview.
pagesetup.setPrintTitleRows("$1:$5");

// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const ws1 = excelWorkbook1.getWorksheets().get(0);

// Name the worksheet.
ws1.setName("MySheet");

// Copy data from the first worksheet of the first workbook into the
// first worksheet of the second workbook.
ws1.copy(ws0);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "CopyWorksheetFromWorkbookToOther_out.xls"));
```

### **在工作簿内部移动工作表**

Aspose.Cells提供一种方法[**Aspose.Cells.Worksheet.moveTo()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#moveto-number-)，用于将工作表移动到同一工作簿的另一个位置。该方法接受目标工作表索引作为参数。

以下示例显示了如何将工作表移动到工作簿内的另一个位置。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "sample1.xlsx");

// Open an existing excel file.
const wb = new AsposeCells.Workbook(inputPath);

// Create a Worksheets object with reference to the sheets of the Workbook.
const sheets = wb.getWorksheets();

// Get the first worksheet.
const worksheet = sheets.get(0);

// Move the first sheet to the third position in the workbook.
worksheet.moveTo(2);

// Save the excel file.
wb.save(path.join(dataDir, "MoveWorksheet_out.xls"));
```
