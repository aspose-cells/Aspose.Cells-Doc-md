---
title: ノード.js経由でC++を使用してすべてのワークシート列を単一のPDFページにフィットさせる
linktitle: ワークシートのすべての列を単一の PDF ページに収める
type: docs
weight: 160
url: /ja/nodejs-cpp/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

時々、ワークシートの全列を1ページに収めたPDFファイルを生成したいことがあります。[**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--)プロパティはその機能を非常に簡単に使用できます。ワークシートのデータに基づいて、出力PDFの高さや幅などの複雑な計算は内部で処理されます。

{{% /alert %}}

## **ワークシートの列を単一の PDF ページに収める**

[**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--)は、ワークシート内のすべての列を単一のPDFページにレンダリングし、行はワークシート内のデータに応じて複数ページに拡張されることを保証します。

以下のサンプルコードは、100列の大きなワークシートをレンダリングするために[**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--)プロパティを使用する方法を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create and initialize an instance of Workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "TestBook.xlsx"));
// Create and initialize an instance of PdfSaveOptions
const saveOptions = new AsposeCells.PdfSaveOptions();
// Set AllColumnsInOnePagePerSheet to true
saveOptions.setAllColumnsInOnePagePerSheet(true);
// Save Workbook to PDF format by passing the object of PdfSaveOptions
const outputFilePath = path.join(dataDir, "output.out.pdf");
workbook.save(outputFilePath, saveOptions);
```

{{% alert color="primary" %}}

あるワークシートに多くの列がある場合、レンダリングされたPDFファイルでは内容が非常に小さくなる場合があります。Acrobat Readerなどの閲覧アプリケーションで拡大するとまだ読める場合があります。

{{% /alert %}} {{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、PDF形式に変換する直前に [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。

{{% /alert %}}
