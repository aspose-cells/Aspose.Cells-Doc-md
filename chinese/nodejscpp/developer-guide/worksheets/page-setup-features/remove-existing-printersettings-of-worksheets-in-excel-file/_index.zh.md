---
title: 用 Node.js 和 C++ 移除 Excel 文件中工作表的现有 PrinterSettings
linktitle: 删除Excel文件中工作表的现有打印设置
type: docs
weight: 60
url: /zh/nodejs-cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: 本文将讲解如何通过 Aspose.Cells for Node.js via C++ 编程移除 Excel 文件中工作表的现有 PrinterSettings。
keywords: 用 Node.js 和 C++ 移除工作表的打印机设置
---

## **可能的使用场景**
有时开发人员希望阻止Excel在保存的XLSX文件中包含打印机设置的*.bin*文件。打印机设置文件位于*“[file "root"]\xl\printerSettings”*。本文介绍了如何使用Aspose.Cells API移除现有的打印机设置。

## **删除Excel文件中工作表的现有打印设置**
Aspose.Cells允许您移除Excel文件中不同工作表的现有打印机设置。以下示例代码说明了如何移除工作簿中所有工作表的现有打印机设置。请参阅其示例Excel文件，输出Excel文件，控制台输出以及屏幕截图以供参考。

## **屏幕截图**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **示例代码**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Load source Excel file
const filePath = path.join(sourceDir, "sampleRemoveExistingPrinterSettingsOfWorksheets.xlsx");
const wb = new AsposeCells.Workbook(filePath);

// Get the sheet counts of the workbook
const sheetCount = wb.getWorksheets().getCount();

// Iterate all sheets
for (let i = 0; i < sheetCount; i++) {
// Access the i-th worksheet
const ws = wb.getWorksheets().get(i);

// Access worksheet page setup
const ps = ws.getPageSetup();

// Check if printer settings for this worksheet exist
if (ps.getPrinterSettings() != null) {
// Print the following message
console.log("PrinterSettings of this worksheet exist.");

// Print sheet name and its paper size
console.log("Sheet Name: " + ws.getName());
console.log("Paper Size: " + ps.getPaperSize());

// Remove the printer settings by setting them null
ps.setPrinterSettings(null);
console.log("Printer settings of this worksheet are now removed by setting it null.");
console.log("");
} // if
} // for

// Save the workbook
wb.save(path.join(outputDir, "outputRemoveExistingPrinterSettingsOfWorksheets.xlsx"));
```

## **控制台输出**
{{< highlight javascript >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
