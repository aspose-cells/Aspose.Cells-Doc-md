---
title: Node.jsを使ってC++経由でExcelファイル内のワークシートの既存プリンタ設定を削除する方法
linktitle: Excelファイルのワークシートの既存のPrinterSettingsを削除する方法
type: docs
weight: 60
url: /ja/nodejs-cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: この記事では、Aspose.Cells for Node.js via C++を使用してExcelファイル内のワークシートの既存のプリンタ設定をプログラム的に削除する方法を学びます。
keywords: ワークシートのプリンタ設定をC++経由のNode.jsで削除、Excelワークシートのプリンタ設定をC++経由のNode.jsで削除
---

## **可能な使用シナリオ**
開発者は、保存されたXLSXファイルにプリンター設定の*.bin*ファイルを含めないようにすることを望むことがあります。プリンター設定ファイルは*「[file "root"]\xl\printerSettings」*の下にあります。この文書では、Aspose.Cells APIを使用して既存のプリンター設定を削除する方法について説明しています。

## **Excelファイルのワークシートの既存のPrinterSettingsを削除する**
Aspose.Cellsを使用して、Excelファイルの異なるシートに指定された既存のプリンター設定を削除することができます。以下のサンプルコードは、ワークブック内のすべてのワークシートの既存のプリンター設定を削除する方法を示します。参考のために、[sample Excel file](45056020.xlsx)、[output Excel file](45056021.xlsx)、コンソール出力、およびスクリーンショットをご覧ください。

## **スクリーンショット**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **サンプルコード**
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

## **コンソール出力**
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
