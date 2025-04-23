---  
title: Node.js経由のC++を用いたスライサーレンダリング  
linktitle: スライサーのレンダリング  
type: docs  
weight: 40  
url: /ja/nodejs-cpp/rendering-slicer/  
---  

## **可能な使用シナリオ**  
Aspose.Cells for Node.js via C++はスライサー図形のレンダリングをサポートしています。ワークシートを画像に変換したり、ワークブックをPDFやHTML形式で保存したりすると、スライサーが適切にレンダリングされているのがわかります。  

## **スライサーをレンダリングする**  
以下のサンプルコードは、既存のスライサーを含む[サンプルExcelファイル](67338479.xlsx)を読み込み、印刷範囲をスライサーだけに設定してワークシートを画像に変換します。その結果得られる画像は[出力画像](67338480.png)で、レンダリングされたスライサーが表示されています。ご覧のとおり、スライサーは正しくレンダリングされており、サンプルExcelファイルと同じ外観です。  

![todo:image_alt_text](rendering-slicer_1)  
## **サンプルコード**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRenderingSlicer.xlsx");

// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Set the print area because we want to render slicer only.
ws.getPageSetup().setPrintArea("B15:E25");

// Specify image or print options, set one page per sheet and only area to true.
const imgOpts = new AsposeCells.ImageOrPrintOptions();
imgOpts.setHorizontalResolution(200);
imgOpts.setVerticalResolution(200);
imgOpts.setImageType(AsposeCells.ImageType.Png);
imgOpts.setOnePagePerSheet(true);
imgOpts.setOnlyArea(true);

// Create sheet render object and render worksheet to image.
const sr = new AsposeCells.SheetRender(ws, imgOpts);
sr.toImage(0, "outputRenderingSlicer.png");
```  

