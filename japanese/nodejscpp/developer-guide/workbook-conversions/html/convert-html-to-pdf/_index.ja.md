---
title: Node.jsとC++を使ったHTMLをPDFに変換する方法
linktitle: HTMLをPDFに変換する方法
type: docs
weight: 80
url: /ja/nodejs-cpp/convert-html-to-pdf/
description: このトピックでは、Aspose.Cells for Node.js via C++を使ってHTMLとMHTMLをPDFに変換する方法を説明します。
keywords: Node.jsを使ったHTMLからPDFやMHTMLからPDFへの変換（C++経由）。 
---

## **概要**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>HTMLをPDFに変換する</b>. It covers the following topics.

<ul>
<li><a href="#js-convert-html-to-pdf">JavaScriptを使ったHTMLからPDFへの変換</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScriptを使ったHTMLをPDFに変換</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScriptでHTMLをPDFに変換する方法</a></li>
</ul>

## **Node.jsでのHTMLからPDFへの変換**
HTMLをPDFに変換するには？[Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/)ライブラリを使えば、数行のコードですぐにHTMLをPDFにプログラム的に変換できます。Aspose.Cells for Node.js via C++は、Excelファイルの生成、修正、変換、レンダリング、印刷が可能なクロスプラットフォームアプリケーションの構築に対応しています。

## **JavaScriptを使ったHTMLをPDFに変換**
次のJavaScriptコードサンプルは、[Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/)を使ってHTMLドキュメントをPDFに変換する方法を示しています。

1. [HtmlLoadOptions](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/)クラスのインスタンスを作成します。
1. [Workbook](https://reference.aspose.com/cells/nodejs-cpp/workbook/)オブジェクトを初期化します。
1. Workbook.save() メソッドを呼び出して、出力 PDF ドキュメントを保存します。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.html");

// Loads the workbook which contains hidden external links
const options = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);
const book = new AsposeCells.Workbook(filePath, options);
book.save("out.pdf");
```

## **オンラインでHTMLをPDFに変換してみてください**

[Aspose.Cells for Node.js via C++](https://releases.aspose.com/cells/nodejs-cpp/) presents you online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">「HTMLをPDFに」</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
