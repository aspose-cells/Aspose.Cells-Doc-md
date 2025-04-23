---
title: 生成されるページ数を制限する  ExcelからPDFへの変換 with Node.js via C++
linktitle: 生成されるページ数を制限  Excel を PDF に変換
type: docs
weight: 180
url: /ja/nodejs-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: ExcelスプレッドシートをPDFに変換する際に、生成されるページ数を制限する方法をAspose.Cells for Node.js via C++で学びましょう。 
---

{{% alert color="primary" %}}

場合によっては、ページ範囲を出力のPDFファイルに印刷したいことがあります。Aspose.Cells for Node.js via C++は、ExcelスプレッドシートをPDFファイル形式に変換する際に生成されるページ数の制限を設定する機能を持ちます。

{{% /alert %}}

## **生成されるページ数の制限**

次の例では、Microsoft Excelファイルのページ3と4をPDFにレンダリングする方法が示されています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "TestBook.xlsx"));
// Instantiate the PdfSaveOption
const options = new AsposeCells.PdfSaveOptions();

// Print only Page 3 and Page 4 in the output PDF
// Starting page index (0-based index)
options.setPageIndex(3);
// Number of pages to be printed
options.setPageCount(2);

// Save the PDF file
workbook.save(path.join(dataDir, "outPDF1.out.pdf"), options);
```

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、PDFにレンダリングする直前に[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)を呼び出すのが最良です。これにより、数式依存の値が再計算され、正しい値が出力ファイルにレンダリングされます。

{{% /alert %}}
