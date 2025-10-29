---  
title: 工作表到图片  设置渲染图片的像素格式，使用 Node.js 和 C++  
linktitle: 工作表转图像  为渲染的图像设置像素格式  
type: docs  
weight: 200  
url: /zh/nodejs-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/  
---  

{{% alert color="primary" %}}  
有时，当将工作表渲染为图像格式时，您可能需要指定像素格式。默认情况下，Aspose.Cells使用32位每像素。Aspose.Cells允许您使用渲染图像的选项自定义像素格式（位深度）。  
{{% /alert %}}  

请参阅下面的示例代码，演示了如何在渲染工作表的图像时设置所需的像素格式。  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
