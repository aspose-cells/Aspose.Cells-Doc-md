---
title: Node.js経由のC++を使って指定されたワークシートをPDFに保存
linktitle: 指定されたワークシートをPDFに保存する
type: docs
weight: 140
url: /ja/nodejs-cpp/save-specified-worksheets-to-pdf/
description: Aspose.Cells for Node.js via C++を使用して、指定ワークシートをPDFに保存する方法を学びます。 
---


デフォルトでは、Aspose.Cellsはブック内のすべての**表示されている**ワークシートをPDFに保存します。[**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--) オプションを使用して、特定のワークシートだけをPDFに保存できます。例：アクティブなワークシートをPDFに保存、すべてのワークシート（表示および非表示）をPDFに保存、複数のカスタムワークシートをPDFに保存など。

## **アクティブワークシートをPDFに保存する**

アクティブシートのみをPDFにエクスポートしたい場合は、[**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--)に[**SheetSet.getActive()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getActive--)を渡すことで実現できます。

シート「Sheet2」は、ソースファイル[sheetset-example.xlsx](sheetset-example.xlsx)のアクティブシートです。

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

## **すべてのワークシートをPDFに保存**

[**SheetSet.getVisible()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getVisible--)はブック内の表示されているシートを示し、[**SheetSet.getAll()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getAll--)は表示・非表示に関わらずすべてのシートを含むものを示します。すべてのシートをPDFにエクスポートしたい場合は、[**SheetSet.getAll()**](https://reference.aspose.com/cells/nodejs-cpp/sheetset/#getAll--) を [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--) オプションに渡すだけです。

ソースファイル [sheetset-example.xlsx](sheetset-example.xlsx) には、非表示シート `Sheet3` を含むすべての4つのシートが含まれています。

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

## **指定されたワークシートをPDFに保存**

複数の目的のシートやカスタムシートをPDFにエクスポートしたい場合は、複数のシートインデックスを[**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--)に渡すことで実現できます。

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

## **ワークシートを並べ替えてPDFに変換**

ソースファイルを変更せずにシートの順序（例：逆順）を変更してPDFに出力したい場合は、並び替えたシートインデックスを [**PdfSaveOptions.getSheetSet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getSheetSet--) オプションに渡すことで実現できます。

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

スプレッドシートに数式が含まれている場合、PDF形式に変換する直前に [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
