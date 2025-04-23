---
title: ワークブックにHTMLを読み込む際の列と行の自動調整（AutoFit Columns and Rows）についてNode.jsとC++を使用して
linktitle: ワークブックにHTMLをロードする際の列と行を自動調整する
type: docs
weight: 120
url: /ja/nodejs-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: Aspose.Cells for Node.js via C++を使用して、WorkbookにHTMLファイルを読み込む際の列と行の自動調整方法を学びます。
---

## **可能な使用シナリオ**

HTMLファイルをロードする際、Workbookオブジェクト内の列と行を自動調整できます。目的のために、[**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--)プロパティを**true**に設定してください。

## **ワークブックにHTMLをロードする際の列と行を自動調整する**

以下のサンプルコードは、最初にサンプルHTMLをLoadOptionsを使用せずにWorkbookに読み込み、XLSX形式で保存します。その後、再度サンプルHTMLをWorkbookに読み込み、今回は[**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--)プロパティを**true**に設定してXLSX形式で保存します。両方の出力Excelファイル（[AutoFitColsAndRowsなしの出力Excelファイル](outputWithout_AutoFitColsAndRows.xlsx)と[AutoFitColsAndRowsありの出力Excelファイル]](outputWith_AutoFitColsAndRows.xlsx)）をダウンロードしてください。以下のスクリーンショットは、両方の出力Excelファイルに対する[**HtmlLoadOptions.getAutoFitColsAndRows()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getAutoFitColsAndRows--)プロパティの効果を示しています。

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Sample HTML.
const sampleHtml = "<html><body><table><tr><td>This is sample text.</td><td>Some text.</td></tr><tr><td>This is another sample text.</td><td>Some text.</td></tr></table></body></html>";

// Load HTML string into memory stream.
const ms = Uint8Array.from(sampleHtml, c => c.charCodeAt(0));

// Load memory stream into workbook.
let wb = new AsposeCells.Workbook(ms);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputWithout_AutoFitColsAndRows.xlsx"));

// Specify the HTMLLoadOptions and set AutoFitColsAndRows = true.
const opts = new AsposeCells.HtmlLoadOptions();
opts.setAutoFitColsAndRows(true);

// Load memory stream into workbook with the above HTMLLoadOptions.
wb = new AsposeCells.Workbook(ms, opts);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "outputWith_AutoFitColsAndRows.xlsx"));
```

