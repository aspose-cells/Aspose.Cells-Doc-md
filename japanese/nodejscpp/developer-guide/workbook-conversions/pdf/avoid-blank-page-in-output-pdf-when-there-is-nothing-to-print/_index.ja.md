---
title: Node.jsをC++で使用して、何も印刷するものがない場合に出力PDFに空白ページが生成されるのを防ぐ
linktitle: 出力PDFの空白ページを回避する
type: docs
weight: 30
url: /ja/nodejs-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Aspose.Cells for Node.js via C++を使用して印刷する内容がなくても空白ページを避ける方法を学びます。
---

## **可能な使用シナリオ**

Excelファイルが空の場合、Aspose.Cells for Node.js via C++を使用してPDFに保存すると、出力PDFに空白ページがレンダリングされます。この既定の動作が望ましくない場合があります。Aspose.Cellsはこの問題を処理するために[**PdfSaveOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOutputBlankPageWhenNothingToPrint--)プロパティを提供します。これを**false**に設定すると、何も印刷するものがない場合には例外が発生します。

## **出力PDFの空白ページを回避する**

次のサンプルコードは空のワークブックを作成し、[**PdfSaveOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOutputBlankPageWhenNothingToPrint--)プロパティを**false**に設定した後、PDFとして保存します。何も出力したい内容がないため、例外が発生します。

## **サンプルコード**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Create Pdf save options.
const opts = new AsposeCells.PdfSaveOptions();

// Default value of OutputBlankPageWhenNothingToPrint is true.
// Setting false means - Do not output blank page when there is nothing to print.
opts.setOutputBlankPageWhenNothingToPrint(false);

// Save workbook to Pdf format, it will throw exception because workbook has nothing to print.
const ms = new Uint8Array();

try {
// Save to Pdf format. It will throw exception.
wb.save(ms, opts);
} catch (ex) {
console.error("Exception Message: " + ex.message + "\r\n");
}
```

## **例外**

{{< highlight javascript >}}

 exception was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
