---  
title: Node.jsとC++を使用したExcelをHTMLにツールチップ付きで変換  
linktitle: ツールチップ付きでExcelをHTMLに変換する  
type: docs  
weight: 200  
url: /ja/nodejs-cpp/convert-excel-to-html-with-tooltip/  
description: Aspose.Cells for Node.js via C++を使って、ツールチップ付きでExcelファイルをHTMLフォーマットに変換する方法を学びます。  
---  

## **ツールチップ付きでExcelをHTMLに変換する**

生成されたHTMLでテキストが切り取られている場合、そのホバー時に完全なテキストをツールチップとして表示したいことがあります。Aspose.Cells for Node.js via C++はこれを可能にする[**HtmlSaveOptions.getAddTooltipText()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getAddTooltipText--)プロパティを提供します。[**HtmlSaveOptions.getAddTooltipText()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getAddTooltipText--)プロパティを**true**に設定すると、完全なテキストがHTMLのツールチップとして追加されます。

次の画像は、生成されたHTMLファイル内のツールチップを示しています。

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

次のコードサンプルは、[源となるExcelファイル](98107416.xlsx)を読み込み、ツールチップ付きの[出力HTMLファイル](98107417.zip)を生成します。

サンプルコード

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "AddTooltipToHtmlSample.xlsx"));

const options = new AsposeCells.HtmlSaveOptions();
options.setAddTooltipText(true);

// Save as Markdown
workbook.save(path.join(outputDir, "AddTooltipToHtmlSample_out.html"), options);
```  

