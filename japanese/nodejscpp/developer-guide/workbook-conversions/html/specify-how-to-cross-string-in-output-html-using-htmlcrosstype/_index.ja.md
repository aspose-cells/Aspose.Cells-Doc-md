---
title: HtmlCrossTypeを使用して出力HTML内で文字列の交差方法を指定する
linktitle: 出力HTML内の文字列をHtmlCrossTypeを使用してクロスする方法を指定
type: docs
weight: 140
url: /ja/nodejs-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Aspose.Cells for Node.js via C++でHtmlCrossTypeを指定してHTML出力内の文字列のはみ出しを制御する方法を学びます。 
---

## **可能な使用シナリオ**

セルにテキストまたは文字列が含まれている場合でも、その幅を超えると次の列のセルがnullまたは空の場合に文字列がはみ出します。ExcelファイルをHTMLに保存するとき、[**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype)列挙型を使用してこのはみ出しを制御できます。主な値は以下の通りです：

- **HtmlCrossType.Default**: MS Excelのように表示; 次のセルに依存します。次のセルがnullの場合、文字列は跨るか切り捨てられます。

- **HtmlCrossType.MSExport**: 文字列はMS ExcelでHTMLをエクスポートしたように表示されます。

- **HtmlCrossType.Cross**: HTMLのクロス文字列を表示; 大きなHTMLファイルの作成パフォーマンスは、DefaultやFitToCell設定の十倍以上高速です。

- **HtmlCrossType.FitToCell**: 文字列をセル内の幅に合わせて表示します。

## **出力HTML内の文字列をHtmlCrossTypeを使用してクロスする方法を指定**

以下のサンプルコードは、[サンプルExcelファイル](51740732.xlsx)を読み込み、異なる [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) を指定してHTML形式に保存します。このコードで生成された[出力HTML](51740734.zip)をダウンロードしてください。サンプルExcelファイルには、赤色の枠線で囲まれた画像が含まれています。このスクリーンショットは、[**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) の値が出力HTMLに与える影響を示しています。

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHtmlCrossStringType.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Specify HTML Cross Type
const opts = new AsposeCells.HtmlSaveOptions();
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Default);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.MSExport);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Cross);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.FitToCell);

// Output Html
workbook.save("out" + opts.getHtmlCrossStringType() + ".htm", opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
