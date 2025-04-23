---  
title: Node.jsを使用してワークシートのセル範囲を画像にエクスポートする方法（C++経由）  
linktitle: ワークシート内のセルの範囲をイメージにエクスポート  
type: docs  
weight: 60  
url: /ja/nodejs-cpp/export-range-of-cells-in-a-worksheet-to-image/  
---  

## **可能な使用シナリオ**  

Aspose.Cells for Node.js via C++を使えばワークシートの画像を作成できます。ただし、時にはワークシートのセル範囲だけを画像にエクスポートする必要があります。この記事では、それを実現する方法を説明します。  

## **ワークシートのセルの範囲をイメージにエクスポート**  

範囲の画像を取得するには、印刷エリアを希望の範囲に設定し、余白をすべて0にします。また、[**ImageOrPrintOptions.getOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOnePagePerSheet--)を**true**に設定します。以下のコードはD8:G16の範囲の画像を取得します。以下はコードで使用されている[サンプルExcelファイル](47153160.xlsx)のスクリーンショットです。任意のExcelファイルで試すことができます。  

## **サンプルExcelファイルのスクリーンショットとそのエクスポートされたイメージ**  

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**  

コードを実行すると、範囲D8:G16のイメージが作成されます。  

**![todo:image_alt_text](Output-Image.png)**  

## **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook from source file.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleExportRangeOfCellsInWorksheetToImage.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the print area with your desired range
worksheet.getPageSetup().setPrintArea("D8:G16");

// Set all margins as 0
worksheet.getPageSetup().setLeftMargin(0);
worksheet.getPageSetup().setRightMargin(0);
worksheet.getPageSetup().setTopMargin(0);
worksheet.getPageSetup().setBottomMargin(0);

// Set OnePagePerSheet option as true
const options = new AsposeCells.ImageOrPrintOptions();
options.setOnePagePerSheet(true);
options.setImageType(AsposeCells.ImageType.Jpeg);
options.setHorizontalResolution(200);
options.setVerticalResolution(200);

// Take the image of your worksheet
const sr = new AsposeCells.SheetRender(worksheet, options);
sr.toImage(0, path.join(outputDir, "outputExportRangeOfCellsInWorksheetToImage.jpg"));
```  

