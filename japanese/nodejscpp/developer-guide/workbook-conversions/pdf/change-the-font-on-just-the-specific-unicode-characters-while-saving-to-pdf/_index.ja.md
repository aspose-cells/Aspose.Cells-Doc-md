---
title: 特定のUnicode文字だけのフォントを変更し、PDFに保存する方法（Node.js via C++）
linktitle: 特定のUnicode文字のみのフォントを変更してPDFに保存する
type: docs
weight: 260
url: /ja/nodejs-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Aspose.Cells for Node.js via C++を使ってPDFに保存する際に特定のUnicode文字のフォントを変更する方法を学びます。 
---

{{% alert color="primary" %}} 

一部のUnicode文字は、ユーザー指定のフォントでは表示されません。そのようなUnicode文字の1つが **Non-breaking Hyphen** (U+2011) で、Unicode番号は8209です。この文字は **Times New Roman** では表示できませんが、**Arial Unicode MS** のような他のフォントでは表示できます。

Times New Romanのようなフォント内にある単語や文章の中でそのような文字が現れると、Aspose.Cellsはその文字を表示できるフォント（Arial Unicode MSなど）に変換します。一方、これは一部のユーザーには望ましくなく、その文字だけのフォントを変更したい場合があります。

この問題に対処するために、Aspose.Cellsは`PdfSaveOptions.isFontSubstitutionCharGranularity`プロパティを提供しています。これをtrueに設定すると、表示できない特定の文字だけのフォントが表示可能なフォントに変更され、残りの文章は元のフォントのままになります。

一つは`PdfSaveOptions.isFontSubstitutionCharGranularity`プロパティを設定せずに生成されたもので、もう一つはこのプロパティをtrueに設定して生成されたものです。

{{% /alert %}} 

## **例**
以下のスクリーンショットは、以下のサンプルコードによって生成された2つの出力 PDF を比較しています。

最初のPDFでは、完全な文章のフォントがタイムズ・ニュー・ローマンからArial Unicode MSに変わっていますが、これはノンブレイキングハイフンによるものです。2つ目のPDFでは、ノンブレイキングハイフンだけのフォントが変更されています。

ExcelファイルをPDF/A-1a互換のPDFフォーマットに変換する方法（Node.js via C++）

|**最初の PDF ファイル**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**2 番目の PDF ファイル**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **サンプルコード**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cells
const cell1 = worksheet.getCells().get("A1");
const cell2 = worksheet.getCells().get("B1");

// Set the styles of both cells to Times New Roman
let style = cell1.getStyle();
style.getFont().setName("Times New Roman");
cell1.setStyle(style);
cell2.setStyle(style);

// Put the values inside the cell
cell1.putValue("Hello without Non-Breaking Hyphen");
cell2.putValue("Hello" + String.fromCharCode(8209) + " with Non-Breaking Hyphen");

// Autofit the columns
worksheet.autoFitColumns();

// Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
workbook.save(path.join(dataDir, "SampleOutput_out.pdf"));

// Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true
const opts = new AsposeCells.PdfSaveOptions();
opts.setIsFontSubstitutionCharGranularity(true);
workbook.save(path.join(dataDir, "SampleOutput2_out.pdf"), opts);
```



