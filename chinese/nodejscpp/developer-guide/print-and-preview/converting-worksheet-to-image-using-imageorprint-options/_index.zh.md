---  
title: 使用Node.js在C++中使用ImageOrPrint选项将工作表转换为图片  
linktitle: 使用ImageOrPrint Options将工作表转换为图像  
type: docs  
weight: 90  
url: /zh/nodejs-cpp/converting-worksheet-to-image-using-imageorprint-options/  
description: 学习如何使用Aspose.Cells for Node.js via C++将工作表转换为图片文件，并应用各种图像和打印选项。   
---  

{{% alert color="primary" %}}  
本文旨在详细介绍如何将工作表转换为图像文件，并应用不同的图像和打印选项，如分辨率、TIFF压缩、图像格式和页面质量。  
{{% /alert %}}  

## **将工作表保存为图像-不同方法**  

有时候，您可能需要将工作表呈现为图形表示。您可能需要将工作表图像嵌入到应用程序或网页中。您可能需要将图像插入到Word文档、PDF文件、PowerPoint演示文稿中，或者在某些其他情景中使用。简单来说，您希望将工作表呈现为图像，以便在别处使用。Aspose.Cells支持将Excel文件中的工作表转换为图像。此外，Aspose.Cells支持设置不同选项，如图像格式、分辨率（垂直和水平）、图像质量以及其他图像和打印选项。  

你可以尝试使用Office自动化，但Office自动化有其自身的缺点。存在若干原因和问题，比如安全、稳定性、可扩展性和速度、价格以及功能等。简而言之，原因很多，其中最主要的是微软自己强烈建议不要在软件方案中使用Office自动化。  

本文介绍了如何在Visual Studio .NET中创建控制台应用程序，使用Aspose.Cells API以及几行简单的代码执行工作表转换为图像的转换，并使用不同的图像和打印选项。  

[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/)类代表一张工作表，用于渲染工作表的图片，具有一个重载的[**toImage(number)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)方法，可以直接将工作表转换为指定属性或选项的图片文件。它可以返回一个对象，你可以将图片保存到磁盘/流中。支持多种图片格式，例如BMP、PNG、GIF、JPEG、TIFF、EMF等。  

## **使用Aspose.Cells将工作表转换为图像，使用图像或打印选项。**  

### **在Microsoft Excel中创建一个模板工作簿**  

我在MS Excel中创建了一个新的工作簿，并在第一个工作表中添加了一些数据。现在，我将把模板文件的工作表“Sheet1”转换为图像文件“SheetImage.tiff”，并将应用不同的图像选项，如水平和垂直分辨率、TiffCompression等。  

### **下载并安装Aspose.Cells**  

首先，你需要[下载](https://downloads.aspose.com/cells/nodejs-cpp)Aspose.Cells for Node.js via C++。将其安装到你的开发计算机上。所有[Aspose](http://www.aspose.com/)组件安装后，都在评估模式下运行。评估模式没有时间限制，只会在生成的文档中加入水印。  

### **创建一个项目**  

启动你的首选开发环境（例如，Visual Studio）。创建一个新的控制台应用程序。  

### **添加引用**  

这个项目将使用Aspose.Cells。因此，你需要在项目中添加对Aspose.Cells组件的引用，例如，添加对….\Program Files\Aspose\Aspose.Cells for Node.js via C++\Bin\Aspose.Cells.node的引用。  

### **将工作表转换为图像文件**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Open template
const filePath = path.join(sourceDir, "sampleWorksheetToAnImage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Apply different Image and Print options
const options = new AsposeCells.ImageOrPrintOptions(); // Corrected: Added the instantiation for ImageOrPrintOptions.

// Set Horizontal Resolution
options.setHorizontalResolution(300);

// Set Vertical Resolution
options.setVerticalResolution(300);

// Set TiffCompression
options.setTiffCompression(AsposeCells.TiffCompression.CompressionLZW);

// Set Image Format
options.setImageType(AsposeCells.ImageType.Tiff);

// Set printing page type
options.setPrintingPage(AsposeCells.PrintingPageType.Default);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, options);

// Render/save the image for the sheet
const pageIndex = 3;
sr.toImage(pageIndex, path.join(outputDir, `outputWorksheetToAnImage_${pageIndex + 1}.tiff`));
```  

## **转换选项**  

可以保存特定页面到图像。下面的代码将工作簿中的第一个和第二个工作表转换为JPG图像。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template excel file
const filePath = path.join(sourceDir, "sampleSpecificPagesToImages.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Specify page index to be rendered
const idxPage = 3;

// Render the third image for the sheet
const bitmap = sr.toImage(idxPage);

// Save the image file
const fs = require("fs");
fs.writeFileSync(path.join(outputDir, `outputSpecificPagesToImage_${idxPage + 1}.jpg`), bitmap);
```  

## **使用 WorkbookRender 进行图片转换**  

TIFF图像可以包含多个帧。你可以将整个工作簿保存为具有多个帧或页面的单一TIFF图像：  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleUseWorkbookRenderForImageConversion.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Tiff);

const workbookRender = new AsposeCells.WorkbookRender(workbook, opts);
workbookRender.toImage(path.join(outputDir, "outputUseWorkbookRenderForImageConversion.tiff"));
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
