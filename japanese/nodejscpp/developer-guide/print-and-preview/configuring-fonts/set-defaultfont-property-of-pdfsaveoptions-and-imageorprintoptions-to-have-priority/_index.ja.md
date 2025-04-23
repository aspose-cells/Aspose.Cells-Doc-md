---
title: PdfSaveOptions および ImageOrPrintOptions の DefaultFont プロパティを Node.js (C++ 経由) で優先順位を持たせて設定する
linktitle: PdfSaveOptionsおよびImageOrPrintOptionsのDefaultFontプロパティを設定し、優先度を持たせます。
type: docs
weight: 30
url: /ja/nodejs-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: Aspose.Cells for Node.js via C++ を使用して、PdfSaveOptions と ImageOrPrintOptions の DefaultFont プロパティを設定する方法を学びます。フォントが見つからない場合に適切なフォントレンダリングを確保します。
---

## **可能な使用シナリオ**

[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) および [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) の **DefaultFont** プロパティを設定する際には、フォントが見つからない（インストールされていない）場合に、ワークブック全体のテキストにそのDefaultFontを設定すると期待されるかもしれません。

一般的に、PDFまたは画像に保存する際、Aspose.Cells for Node.js via C++ は最初にワークブックのデフォルトフォント（すなわち `Workbook.DefaultStyle.Font`）を設定しようとします。もしもデフォルトフォントが正しくテキストを表示/レンダリングできない場合、Aspose.Cells は [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) の DefaultFont 属性に指定されたフォントでレンダリングしようとします。

この期待に対処するために、[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) には "**CheckWorkbookDefaultFont**" というブール型のプロパティがあります。このプロパティを **false** に設定すると、ワークブックのデフォルトのフォントを試行しないようになり、また [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) のDefaultFont設定が優先されます。

## **PdfSaveOptions/ImageOrPrintOptionsのDefaultFontプロパティを設定します**

次のサンプルコードはExcelファイルを開きます。最初のシートのセルA1には"Christmas Time Font text"というテキストが設定されており、フォント名は"Christmas Time Personal Use"ですが、これはインストールされていません。[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/)の**DefaultFont**属性を"Times New Roman"に設定し、**CheckWorkbookDefaultFont**ブール型プロパティを**"false"**に設定することで、A1セルのテキストを"Times New Roman"フォントでレンダリングし、Workbookのデフォルトフォント（"Calibri"）を使用しないようにします。このコードは最初のシートをPNGとTIFF画像フォーマットにレンダリングし、最後にPDFに出力します。

{{% alert color="primary" %}}

**CheckWorkbookDefaultFont**属性のデフォルト値は**true**です。

{{% /alert %}}

これは、例コードで使用されている [テンプレートファイル](49446913.xlsx)のスクリーンショットです。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

[**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--)プロパティを"Times New Roman"に設定した後の出力PNG画像例です。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

[**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--)プロパティを"Times New Roman"に設定した後の出力[TIF](48496672.tiff)画像を確認してください。

[**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--)プロパティを「Times New Roman」に設定した後の出力[PDF](48496673.pdf)ファイルを参照してください。

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Open an Excel file.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleSetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.xlsx"));

// Rendering to PNG file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
const imgOpt = new AsposeCells.ImageOrPrintOptions();
imgOpt.setImageType(AsposeCells.ImageType.Png);
imgOpt.setCheckWorkbookDefaultFont(false);
imgOpt.setDefaultFont("Times New Roman");
const sr = new AsposeCells.SheetRender(workbook.getWorksheets().get(0), imgOpt);
sr.toImage(0, path.join(outputDir, "out1_imagePNG.png"));

// Rendering to TIFF file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
imgOpt.setImageType(AsposeCells.ImageType.Tiff);
const wr = new AsposeCells.WorkbookRender(workbook, imgOpt);
wr.toImage(path.join(outputDir, "out1_imageTIFF.tiff"));

// Rendering to PDF file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
const saveOptions = new AsposeCells.PdfSaveOptions();
saveOptions.setDefaultFont("Times New Roman");
saveOptions.setCheckWorkbookDefaultFont(false);
workbook.save(path.join(outputDir, "out1_pdf.pdf"), saveOptions);
```
