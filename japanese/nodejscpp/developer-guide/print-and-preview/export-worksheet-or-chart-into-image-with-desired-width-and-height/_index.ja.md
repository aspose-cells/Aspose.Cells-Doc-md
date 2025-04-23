---  
title: Node.jsを通じてワークシートまたはチャートを希望の幅と高さで画像にエクスポートする  
linktitle: 所定の幅と高さでワークシートまたはグラフをイメージにエクスポート  
type: docs  
weight: 290  
url: /ja/nodejs-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/  
description: Aspose.Cells for Node.js via C++を使用して、ワークシートやチャートを指定した幅と高さの画像にエクスポートする方法を学びます。  
---  

{{% alert color="primary" %}}  
Aspose.Cells for Node.js via C++を使えば、希望の幅と高さでワークシートやチャートを画像にエクスポートできます。[**ImageOrPrintOptions.setDesiredSize(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#setDesiredSize-number-number-boolean-)メソッドを提供し、エクスポートされた画像の希望の幅と高さを設定します。幅と高さはピクセル単位で指定します。  
{{% /alert %}}  

次のコードは、400x400のサイズでワークシートをイメージにエクスポートします。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook object from source file
const filePath = path.join(sourceDir, "sampleWorksheetToImageDesiredSize.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set image or print options we want one page per sheet. The image format is in png and desired dimensions are 400x400
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setOnePagePerSheet(true);
opts.setImageType(AsposeCells.ImageType.Png);
opts.setDesiredSize(400, 400, false);

// Render sheet into image
const sr = new AsposeCells.SheetRender(worksheet, opts);
sr.toImage(0, path.join(outputDir, "outputWorksheetToImageDesiredSize.png"));
```  

