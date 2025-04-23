---
title: ノード.js経由でC++を使用してPDFに変換時にドキュメント構造をエクスポート
linktitle: PDF への変換時にドキュメント構造をエクスポート
type: docs
weight: 360
url: /ja/nodejs-cpp/export-document-structure-while-converting-to-pdf/
description: Aspose.Cells for Node.js via C++を使用してExcelファイルをタグ付きPDFに変換する際に、ドキュメント構造をエクスポートする方法を学びます。 
---

PDFの論理構造機能は、ドキュメント内容の構造に関する情報をPDFファイルに組み込むための仕組みを提供します。Aspose.Cells for Node.js via C++は、セル、行、テーブル、ワークシート、画像、シェイプ、ヘッダー/フッターなど、Microsoft Excelドキュメントの構造情報を保持します。

[PdfSaveOptions.getExportDocumentStructure()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getExportDocumentStructure--) オプションを利用し、ドキュメント構造をエクスポートしたタグ付きPDFとして保存できます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "document-structure-example.xlsx");
// Open the excel file with image, shape, chart, etc.
const wb = new AsposeCells.Workbook(filePath);

// Set to export document structure.
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setExportDocumentStructure(true);

// Save the pdf file with PdfSaveOptions
wb.save("output.pdf", pdfSaveOptions);
```

