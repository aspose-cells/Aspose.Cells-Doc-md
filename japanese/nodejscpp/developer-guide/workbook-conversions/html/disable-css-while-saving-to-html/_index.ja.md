---
title: Node.jsとC++を使ったCSSの無効化（HTMLに保存時）
linktitle: HTMLに保存する際にCSSを無効にする
type: docs
weight: 320
url: /ja/nodejs-cpp/disable-css-while-saving-to-html/
description: Aspose.Cells for Node.js via C++を使ってExcelファイルのHTML保存時にCSSを無効にする方法を学びます。 
---

## **可能な使用シナリオ**

ExcelファイルをシングルページHTMLに保存するとき、通常CSS要素はHTMLファイル内に埋め込まれやすく、HEADセクションに位置します。このファイルをコンテンツ/本文としてメールに添付すると、多くのメールクライアントによってCSS要素が除去され、不適切な表示となる場合があります。Aspose.Cellsのバージョン24.12では、CSSをオプションで無効にできる機能が導入されており、スタイルをHTML要素内に直接適用できるようになっています。メールの本文としてHTMLを設定したい場合は、[**HtmlSaveOptions.getDisableCss()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableCss--)プロパティを使用し、**true**に設定してください。

## **HTML保存時にCSSを無効にする**

次のサンプルコードは、[**HtmlSaveOptions.getDisableCss()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableCss--) プロパティの使用例を示しています。 

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleDisableCss.xlsx"));

// Disable CSS
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDisableCss(true);

// Save the workbook in HTML
workbook.save(path.join(outputDir, "outputDisable.html"), opts);
```
