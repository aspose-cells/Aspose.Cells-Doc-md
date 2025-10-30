---  
title: ImageOrPrintOptionsのPageIndexとPageCountプロパティを使用してページシーケンスをレンダリング（Node.jsとC++経由）  
linktitle: ImageOrPrintOptionsのPageIndexおよびPageCountプロパティを使用してページのシーケンスをレンダリングする  
type: docs  
weight: 110  
url: /ja/nodejs-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/  
description: Aspose.Cells for Node.js via C++を使用してExcelファイルの特定のページを画像にレンダリングする方法を学びます。  
---  

## **可能な使用シナリオ**  

Aspose.Cellsと[**ImageOrPrintOptions.getPageIndex()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageIndex--)および[**ImageOrPrintOptions.getPageCount()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageCount--)のプロパティを使用して、Excelファイルのページシーケンスを画像にレンダリングできます。これらのプロパティは、数千ページもあるワークシートの一部だけをレンダリングしたい場合に便利です。これにより処理時間だけでなく、レンダリングプロセスのメモリ消費も削減されます。  

## **ImageOrPrintOptionsのPageIndexおよびPageCountプロパティを使用したページのシーケンスをレンダリングする**  

[サンプルExcelファイル](55541781.xlsx)を読み込み、[**ImageOrPrintOptions.getPageIndex()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageIndex--)と[**ImageOrPrintOptions.getPageCount()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getPageCount--)のプロパティを使用してページ4、5、6、7のみをレンダリングし、生成されたページを示すサンプルコードです。  

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2)|  
| :- | :- |  
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4)|  

## **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");
// Load the sample Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleImageOrPrintOptions_PageIndexPageCount.xlsx"));
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Specify image or print options
// We want to print pages 4, 5, 6, 7
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setPageIndex(3);
opts.setPageCount(4);
opts.setImageType(AsposeCells.ImageType.Png);
// Create sheet render object
const sheetRender = new AsposeCells.SheetRender(worksheet, opts);
// Print all the pages as images
for (let i = opts.getPageIndex(); i < sheetRender.getPageCount(); i++) {
sheetRender.toImage(i, path.join(outputDir, `outputImage-${i + 1}.png`));
}
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
