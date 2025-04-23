---  
title: 使用Node.js导出工作表或图表为具有指定宽度和高度的图片  
linktitle: 导出工作表或图表为指定宽度和高度的图像  
type: docs  
weight: 290  
url: /zh/nodejs-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/  
description: 学习如何使用Aspose.Cells for Node.js via C++将工作表或图表导出为具有特定宽度和高度的图片。  
---  

{{% alert color="primary" %}}  
你可以使用Aspose.Cells for Node.js via C++将工作表或图表导出为具有所需宽度和高度的图片。它提供[**ImageOrPrintOptions.setDesiredSize(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#setDesiredSize-number-number-boolean-)方法来设置导出图片的宽度和高度，单位为像素。  
{{% /alert %}}  

以下代码将工作表导出为一个 400x400 大小的图像。  

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

