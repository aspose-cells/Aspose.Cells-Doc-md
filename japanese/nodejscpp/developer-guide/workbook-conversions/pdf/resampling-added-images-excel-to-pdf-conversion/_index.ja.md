---
title: 画像のリサンプリング追加  ExcelからPDFへの変換（Node.js経由のC++）
linktitle: 画像のリサンプリング
type: docs
weight: 150
url: /ja/nodejs-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Aspose.Cells for Node.js via C++を使用して、追加された画像を圧縮し、PDFのサイズを縮小し、変換パフォーマンスを向上させる方法を学びましょう。
---

{{% alert color="primary" %}}

大量の画像を含む大きなMicrosoft Excelファイルを扱う場合、追加された画像を圧縮して出力PDFのファイルサイズを減らし、全体の変換性能を向上させる必要があるかもしれません。Aspose.Cells for Node.js via C++は、追加された画像をリサンプルして出力PDFのサイズを縮小し、パフォーマンスを若干改善します。

{{% /alert %}}

Aspose.Cells APIを使用してタスクを実行する方法を説明する以下のサンプルコードをご覧ください。この例では、Microsoft ExcelファイルをPDFファイルに変換しながら、ファイル内の画像を圧縮しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Initialize a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "input.xlsx"));

// Instantiate the PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
// Set Image Resample properties
pdfSaveOptions.setImageResample(300, 70);

// Save the PDF file
workbook.save(path.join(dataDir, "OutputFile_out_pdf"), pdfSaveOptions);
```

{{% alert color="primary" %}}

[**setImageResample(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#setImageResample-number-number-)オプションを使用すると、出力PDFのサイズを最小限に抑えることができますが、画像の品質には少し影響を与える可能性があります。

{{% /alert %}} {{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、PDF形式に変換する直前に [**workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
