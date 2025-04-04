---  
title: Converting Worksheet to Image and Worksheet to Image by Page with Node.js via C++  
linktitle: Converting Worksheet to Image and Worksheet to Image by Page  
type: docs  
weight: 80  
url: /nodejs-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/  
---  

{{% alert color="primary" %}}  
This document is designed to provide developers with a detailed understanding of how to convert a worksheet to an image file & worksheet with multiple pages to an image file per page.  

Sometimes, you might need to present worksheets as images, for example, to use them in applications or web pages. You might need to insert the images into a Word document, a PDF file, a PowerPoint presentation, or use them in some other scenario. Simply, you want to render the worksheet as an image. Aspose.Cells supports converting worksheets in Microsoft Excel files to images. Also, Aspose.Cells supports converting a workbook to multiple image files, one per page.  

You might use Office Automation to achieve this, but Office automation has its own drawbacks. There are several reasons and issues involved: for example security, stability, scalability/Speed, price, and features. In short, there are many reasons, but the main one is that Microsoft themselves strongly recommends against Office automation.  
{{% /alert %}}  

## **Using Aspose.Cells for Node.js via C++ to Convert Worksheet to Image File**  

This article shows how to create a console application, convert a worksheet to an image, and convert a worksheet into one image for each worksheet with a few and simplest lines of code using the Aspose.Cells API.  

You need to import several valuable classes related to rendering functionalities into your program or project, such as [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender/), and so on. The [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/) class represents a worksheet to render images for the worksheet and has an overloaded [**toImage(number)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-) method that can convert a worksheet to image files directly with any attributes or options set. It can return an image object and you can save an image file to the disk/stream. Several image formats are supported, for example, BMP, PNG, GIF, JPG, JPEG, TIFF, EMF, and others.  

This article explains how to:  

- Convert a worksheet to an image  
- Convert every page in a worksheet to an image  

This task shows how to use Aspose.Cells to convert a worksheet from a template workbook to an image file.  

### **Setup Project**  

1. First, [download Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).  
1. Install it on your development computer. All [Aspose](http://www.aspose.com/) components, when installed, work in evaluation mode. The evaluation mode has no time limit and it only injects watermarks into produced documents. Now start your development environment and create a new console application. This example uses a Node.js console application, but you can use any setup that integrates with Node.js. Add reference to Aspose.Cells into created project.  

### **Convert Worksheet to Image File**  

I created a new workbook in Microsoft Excel and added some data in the first worksheet: **Testbook.xlsx** (1 worksheet). Next, convert the template file’s worksheet Sheet1 to an image file called SheetImage.jpg.  

Following is the code used by the component to accomplish the task. It converts Sheet1 in **Testbook.xlsx** to an image file to explain how easy this conversion is.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template excel file
const filePath = path.join(sourceDir, "sampleConvertWorksheettoImageFile.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setOnePagePerSheet(true);

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Save the image file
const outputFilePath = outputDir + "outputConvertWorksheettoImageFile.jpg";

sr.toImage(0, outputFilePath);
```  

## **Using Aspose.Cells for Node.js via C++ to Convert Worksheet to Image File by Page**  

This example shows how to use Aspose.Cells to convert a worksheet from a template workbook that has several pages to one image file per page.  

### **Convert Worksheet to Image by Page**  

I created a new workbook in Microsoft Excel and added some data in the first worksheet: **Testbook2.xlsx** (1 worksheet).  

Now, convert the template file's worksheet Sheet1 to image files (one file per page). As I already created the console application to perform the copy task, I will skip those console application creation steps and directly move to the worksheet conversion steps.  

Following is the code used by the component to accomplish the task. It converts Sheet1 in Testbook2.xlsx to image files by page.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleConvertWorksheetToImageByPage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

const options = new AsposeCells.ImageOrPrintOptions();
options.setHorizontalResolution(200);
options.setVerticalResolution(200);
options.setImageType(AsposeCells.ImageType.Tiff);

// Sheet2Image By Page conversion
const sr = new AsposeCells.SheetRender(sheet, options);
for (let j = 0; j < sr.getPageCount(); j++) 
{
sr.toImage(j, outputDir + "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif");
}
```  

  