---  
title: 未使用スタイルを除外してExcelをHTMLに変換（Node.js経由でC++）  
linktitle: Excel を HTML に変換する際に未使用のスタイルを除外  
type: docs  
weight: 30  
url: /ja/nodejs-cpp/exclude-unused-styles-during-excel-to-html-conversion/  
description: ExcelをHTMLに変換する際に未使用のスタイルを除外する方法についてAspose.Cells for Node.js via C++を使用して学びましょう。  
---  

## **可能な使用シナリオ**  

Microsoft Excelファイルには、多くの未使用スタイルが含まれることがあります。これらをHTMLにエクスポートすると、ファイルサイズが増加します。ExcelからHTMLへの変換時に未使用のスタイルを除外するには、[**HtmlSaveOptions.getExcludeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExcludeUnusedStyles--)プロパティを使用します。**true**に設定すると、未使用のスタイルはすべて除外されます。以下のスクリーンショットは出力HTML内の未使用スタイルの例です。  

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)  

## **ExcelからHTMLへの変換時に未使用のスタイルを除外**  

以下のサンプルコードでは、ワークブックを作成し、未使用の名前付きスタイルも作成しています。[**HtmlSaveOptions.getExcludeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExcludeUnusedStyles--)が**true**に設定されているため、未使用の名前付きスタイルは[出力HTML](61767778.zip)にエクスポートされません。ただし、**false**に設定すると、未使用のスタイルがHTML内に保持され、上記スクリーンショットのようにHTMLマークアップ上で確認できます。  

## **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const wb = new AsposeCells.Workbook();

// Create an unused named style
wb.createStyle().setName("UnusedStyle_XXXXXXXXXXXXXX");

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Put some value in cell C7
ws.getCells().get("C7").putValue("This is sample text.");

// Specify html save options, we want to exclude unused styles
const opts = new AsposeCells.HtmlSaveOptions();

// Comment this line to include unused styles
opts.setExcludeUnusedStyles(true);

// Save the workbook in html format
wb.save("outputExcludeUnusedStylesInExcelToHTML.html", opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
