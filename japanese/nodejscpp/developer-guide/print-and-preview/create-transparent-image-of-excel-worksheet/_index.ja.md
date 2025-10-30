---  
title: Node.jsを経由したC++でExcelワークシートの透過画像を作成する  
linktitle: Create Transparent Image of Excel Worksheet  
type: docs  
weight: 170  
url: /ja/nodejs-cpp/create-transparent-image-of-excel-worksheet/  
description: Aspose.Cells for Node.js via C++を使用してExcelワークシートの透過画像を生成する方法を学びます。  
---  

{{% alert color="primary" %}}  

時々、ワークシートの画像を透明なイメージとして生成する必要があります。埋められていないセルに透明性を適用したい場合があります。Aspose.Cellsは透明性をワークシートイメージに適用するための[**ImageOrPrintOptions.getTransparent()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTransparent--)プロパティを提供しています。このプロパティが **false** の場合、埋められていないセルは白色で描画され、 **true** の場合、埋められていないセルは透明に描画されます。  

{{% /alert %}}  

以下のワークシートイメージでは、透明性が適用されていません。埋められていないセルは白色で描画されます。  

|**透明度なしの出力: セルの背景は白です**|  
| :- |  
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|  

以下のワークシート画像では、透明度が適用されました。塗りつぶしのないセルは透明です。  

|**透明度を有効にした出力**|  
| :- |  
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|  

次のサンプルコードは、Excelワークシートから透明な画像を生成します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook object from source file
const wb = new AsposeCells.Workbook(path.join(sourceDir, "sampleCreateTransparentImage.xlsx"));

// Apply different image or print options
const imgOption = new AsposeCells.ImageOrPrintOptions();
imgOption.setImageType(AsposeCells.ImageType.Png);
imgOption.setHorizontalResolution(200);
imgOption.setVerticalResolution(200);
imgOption.setOnePagePerSheet(true);

// Apply transparency to the output image
imgOption.setTransparent(true);

// Create image after applying image or print options
const sr = new AsposeCells.SheetRender(wb.getWorksheets().get(0), imgOption);
sr.toImage(0, path.join(outputDir, "outputCreateTransparentImage.png"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
