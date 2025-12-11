---  
title: Converting Worksheet to Image using ImageOrPrint Options with Node.js via C++  
linktitle: Converting Worksheet to Image using ImageOrPrint Options  
type: docs  
weight: 90  
url: /nodejs-cpp/converting-worksheet-to-image-using-imageorprint-options/  
description: Learn how to convert a worksheet to an image file and apply various image and print options using Aspose.Cells for Node.js via C++.   
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  
This document is designed to provide a detailed understanding of how to convert a worksheet to an image file and apply different image and print options for the image, such as resolution, TIFF compression, image format, and page quality.  
{{% /alert %}}  

## **Saving Worksheets to Images - Different Approaches**  

Sometimes, you might require presenting your worksheets as a pictorial representation. You need to embed the worksheet images into your applications or web pages. You might need to insert the images into a Word document, a PDF file, a PowerPoint presentation, or use them in some other scenario. Simply, you want a worksheet rendered as an image so that you can use it elsewhere. Aspose.Cells supports converting worksheets in Excel files to images. Aspose.Cells also supports setting different options like image format, resolution (both vertical and horizontal), image quality, and other image and print options.  

You might try Office Automation, but Office automation has its own drawbacks. There are several reasons and issues involved: for example, security, stability, scalability and speed, price, and features. In short, there are many reasons, with the top one being that Microsoft itself strongly recommends against Office automation from software solutions.  

This article shows how to create a console application in Visual Studio .NET, perform the conversion of a worksheet to an image using different image and print options with a few simple lines of code using the Aspose.Cells API.  

The [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/) class provides functionality to render a worksheet as images. It has an overloaded [**toImage(number)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-) method that can directly convert a worksheet to image file(s) with your desired attributes or options. It returns an object that you can save as an image file to disk or a stream. Several image formats are supported, e.g., BMP, PNG, GIF, JPEG, TIFF, EMF, etc.  

## **Using Aspose.Cells to Convert Worksheet to Image using ImageOrPrint options**  

### **Creating a template workbook in Microsoft Excel**  

I created a new workbook in MS Excel and added some data in the first worksheet. Now, I will convert the template file’s worksheet “Sheet1” to an image file “SheetImage.tiff” and will apply different image options such as horizontal and vertical resolutions, TiffCompression, etc.  

### **Download and Install Aspose.Cells**  

First, you need to [download](https://downloads.aspose.com/cells/nodejs-cpp) Aspose.Cells for Node.js via C++. Install it on your development computer. All [Aspose](http://www.aspose.com/) components, when installed, work in evaluation mode. The evaluation mode has no time limit and it only injects watermarks into produced documents.  

### **Create a Project**  

Start your preferred development environment (e.g., Visual Studio). Create a new console application.  

### **Add References**  

This project will use Aspose.Cells. Therefore, you need to add a reference to the Aspose.Cells component in your project. For example, add a reference to `…\Program Files\Aspose\Aspose.Cells for Node.js via C++\Bin\Aspose.Cells.node`.  

### **Convert Worksheet to an Image file**  

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
const options = new AsposeCells.ImageOrPrintOptions();

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

## **Conversion Options**  

It is possible to save specific pages to images. The following code converts the first and second worksheets in a workbook to JPG images.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template Excel file
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

## **Image conversion using WorkbookRender**  

A TIFF image can contain more than one frame. You can save the whole workbook to a single TIFF image with multiple frames or pages:  

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
