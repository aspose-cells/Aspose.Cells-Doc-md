---
title: ExcelからHTMLへ  より良いレイアウトのためのPresentationPreferenceオプションの使用（Node.js経由でC++）
linktitle: ExcelをHTMLに変換する際、PresentationPreferenceオプションを使用してレイアウトを向上させる
type: docs
weight: 220
url: /ja/nodejs-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/
---

{{% alert color="primary" %}} 

Aspose.Cellsは、Microsoft ExcelファイルをHTMLまたはMHT形式に保存するときに見た目を改善するためのHtmlSaveOptions.presentationPreferenceプロパティを提供しています。デフォルトはfalseです。より魅力的なプレゼンテーションを得るために、このプロパティをtrueに設定することを推奨します。

{{% /alert %}} 

プレゼンテーションプリファレンスオンでExcelレポートからHTMLファイルをレンダリングする方法のサンプルコードを以下に示します。



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate the Workbook
// Load an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Create HtmlSaveOptions object
const options = new AsposeCells.HtmlSaveOptions();
// Set the Presentation preference option
options.setPresentationPreference(true);

// Save the Excel file to HTML with specified option
workbook.save(path.join(dataDir, "outPresentationlayout1.out.html"), options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
