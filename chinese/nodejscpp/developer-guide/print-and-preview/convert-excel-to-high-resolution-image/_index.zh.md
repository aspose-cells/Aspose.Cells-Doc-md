---  
title: 使用 Node.js 和 C++ 将Excel转换为高分辨率图像  
linktitle: 转换Excel到高分辨率图像  
type: docs  
weight: 100  
url: /zh/nodejs-cpp/convert-excel-to-high-resolution-image/  
description: 学习如何使用Aspose.Cells for Node.js via C++将Excel文件转换为高分辨率图片。  
---  

随着高分辨率屏幕的普及，默认96 DPI生成的图像通常显示模糊不清。为了确保在高分辨率屏幕上清晰，生成更高DPI的图像至关重要。Aspose.Cells for Node.js via C++提供设置[**ImageOrPrintOptions.getHorizontalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--)和[**ImageOrPrintOptions.getVerticalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--)的功能，使您能够从Excel文件创建高清晰度的图片，在高分辨率显示器上看起来更清晰。  

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

