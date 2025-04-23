---  
title: ExcelからPDFへ1ページずつレンダリング  Node.js経由のC++によるExcelのPDF変換  
linktitle: Excelワークシートごとに1つのPDFページをレンダリングする  ExcelからPDFへの変換  
type: docs  
weight: 100  
url: /ja/nodejs-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/  
---  

{{% alert color="primary" %}}  

多くのシートと50列以上、300行以上のデータを持つ大きなMicrosoft Excelファイル（例：ワークブック）を扱う場合、シートのサイズに関係なく、1ページずつ表示させたいことがあります。これは、各ページのサイズが大きく異なる可能性があるということです。これを実現するには、Aspose.Cells for Node.js via C++を使用します。  

{{% /alert %}}  

複数のワークシートを持つExcelファイルをPDFに変換するサンプルコードをご確認ください。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Initialize a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "input.xlsx"));

// Implement one page per worksheet option
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setOnePagePerSheet(true);

// Save the PDF file
workbook.save(path.join(dataDir, "OutputFile.out.pdf"), pdfSaveOptions);
```  

{{% alert color="primary" %}}  

[PdfSaveOptions.getOnePagePerSheet()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOnePagePerSheet--)オプションを**true**に設定すると、すべてのシート内容が1つのPDFページにレンダリングされます。  

{{% /alert %}} {{% alert color="primary" %}}  

スプレッドシートに数式が含まれている場合は、[Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)を呼び出すのが最良です。これにより、数式依存の値が再計算され、正しい値がPDFにレンダリングされます。  

{{% /alert %}}  

