---
title: 使用 Node.js 和 C++ 将指定工作表保存为 PDF
linktitle: 将指定的工作表保存为 PDF
type: docs
weight: 140
url: /zh/nodejs-cpp/save-specified-worksheets-to-pdf/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 将指定的工作表保存为 PDF。 
---


默认情况下，Aspose.Cells 将工作簿中的所有**可见**工作表保存为 PDF 文件。通过 [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--) 选项，可以将指定的工作表保存到 PDF 文件中。例如，可以将活动工作表保存为 PDF，保存所有（包括隐藏）工作表为 PDF，或保存自定义多工作表为 PDF。

## **将活动工作表保存为 PDF**

 如果只想导出活动工作表为 PDF，可以将 [**SheetSet.getActive()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getActive--) 传递给 [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--) 选项实现。

 源文件 [sheetset-example.xlsx](sheetset-example.xlsx) 的工作表 `Sheet2` 为活动工作表。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sheetset-example.xlsx");

// Open the template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Set active sheet to output
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setSheetSet(AsposeCells.SheetSet.getActive());

// Save the pdf file with PdfSaveOptions
workbook.save("output.pdf", pdfSaveOptions);
```

## ** 保存所有工作表为 PDF**

[**SheetSet.getVisible()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getVisible--) 表示工作簿中的可见工作表，而 [**SheetSet.getAll()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getAll--) 表示工作簿中的所有工作表，包括可见和隐藏/不可见的工作表。如果你想将所有工作表导出为 PDF，你可以只传递 [**SheetSet.getAll()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getAll--) 给 [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--) 选项。

源文件[sheetset-example.xlsx](sheetset-example.xlsx)包含所有四个工作表，其中隐藏了工作表`Sheet3`。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sheetset-example.xlsx");

// Open the template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Set all sheets to output
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setSheetSet(AsposeCells.SheetSet.getAll());

// Save the pdf file with PdfSaveOptions
workbook.save("output.pdf", pdfSaveOptions);
```

## **将指定的工作表保存为 PDF**

 如果想导出多个自定义工作表为 PDF，可以通过传递多个工作表索引到 [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--) 选项实现。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sheetset-example.xlsx");

// Open the template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Set custom multiple sheets(Sheet1, Sheet3) to output
const sheetSet = new AsposeCells.SheetSet([0, 2]);
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setSheetSet(sheetSet);

// Save the pdf file with PdfSaveOptions
workbook.save("output.pdf", pdfSaveOptions);
```

## ** 将工作表重新排序为 PDF**

如果你想在不修改源文件的情况下，将工作表（例如反向顺序）重新排序为 PDF，可以通过传递重新排序的工作表索引到 [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--) 选项来实现。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sheetset-example.xlsx");
// Open the template excel file
const wb = new AsposeCells.Workbook(filePath);

// Reorder sheets(Sheet1, Sheet2, Sheet3, Sheet4) to sheets(Sheet4, Sheet3, Sheet2, Sheet1)
const sheetSet = new AsposeCells.SheetSet([3, 2, 1, 0]);
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setSheetSet(sheetSet);

// Save the pdf file with PdfSaveOptions
wb.save("output.pdf", pdfSaveOptions);
```

{{% alert color="primary" %}} 

如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用 [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)。这样做将确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
