---  
title: ワークシートを画像に  Node.js経由のC++でレンダリングされた画像のピクセルフォーマットを設定する  
linktitle: 画像にレンダリング  レンダリングされた画像のピクセル形式を設定  
type: docs  
weight: 200  
url: /ja/nodejs-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/  
---  

{{% alert color="primary" %}}  
時々、ワークシートを画像形式にレンダリングする際にピクセル形式を指定したいことがあります。Aspose.Cells はデフォルトで32ビットピクセルを使用しますが、レンダリングされた画像のピクセル形式（ビットの深さ）をカスタマイズすることができます。  
{{% /alert %}}  

以下は、シートの画像をレンダリングする際に、望ましいピクセル形式を設定する方法を示すサンプルコードです。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Load an Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleSetPixelFormatRenderedImage.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the ImageOrPrintOptions with desired color depth (24 bits per pixel) and image format type
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setTiffColorDepth(AsposeCells.ColorDepth.Format24bpp);
opts.setImageType(AsposeCells.ImageType.Tiff);

// Instantiate SheetRender object based on the first worksheet
const sheetRender = new AsposeCells.SheetRender(worksheet, opts);

// Save the image (first page of the sheet) with the specified options
sheetRender.toImage(0, path.join(outputDir, "outputSetPixelFormatRenderedImage.tiff"));
```  

