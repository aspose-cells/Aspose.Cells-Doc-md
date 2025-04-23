---  
title: Node.js経由でExcelを高解像度画像に変換  
linktitle: Excelを高解像度画像に変換する  
type: docs  
weight: 100  
url: /ja/nodejs-cpp/convert-excel-to-high-resolution-image/  
description: Aspose.Cells for Node.js via C++を使用してExcelファイルを高解像度画像に変換する方法を学びます。  
---  

高解像度スクリーンの普及に伴い、デフォルトの96 DPIで生成された画像はぼやけて見えることがあります。高精細な表示を確保するために、より高いDPIで画像を生成する必要があります。Aspose.Cells for Node.js via C++は、[**ImageOrPrintOptions.getHorizontalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--)と[**ImageOrPrintOptions.getVerticalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--)を設定し、高品質なExcel画像を作成して高解像度ディスプレイ上でシャープに見せる機能を提供します。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Load the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of ImageOrPrintOptions
const options = new AsposeCells.ImageOrPrintOptions();
options.setHorizontalResolution(300);
options.setVerticalResolution(300);
options.setImageType(AsposeCells.ImageType.Png);

// Get the worksheet
const sheet = workbook.getWorksheets().get(0);

// Create a SheetRender instance
const render = new AsposeCells.SheetRender(sheet, options);

// Generate and save the image
render.toImage(0, "output.png");
```  

