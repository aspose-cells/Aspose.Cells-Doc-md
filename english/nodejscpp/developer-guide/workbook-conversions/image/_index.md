---  
title: Image with Node.js via C++  
linktitle: Image  
type: docs  
weight: 300  
url: /nodejs-cpp/convert-excel-to-image/  
---  

{{% alert color="primary" %}}  
Aspose.Cells allows you to export a worksheet from the workbook and convert it into different formats. This article explains how to convert a worksheet to different formats.  
{{% /alert %}}  

## Converting Workbook to TIFF  

An Excel file can contain multiple sheets with multiple pages. [**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender) allows you to convert Excel to TIFF with multiple pages. Also, you can control multiple options for TIFF, like [Compression](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#tiffCompression), [Color depth](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#tiffColorDepth), Resolution([Horizontal resolution](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#horizontalResolution), [Vertical resolution](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#verticalResolution)).  

The following code snippet shows how to convert Excel to TIFF with multiple pages. The [source Excel file](workbook-to-tiff-with-mulitiple-pages.xlsx) and [generated TIFF image](workbook-to-tiff-with-mulitiple-pages.tiff) are attached for your reference.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "workbook-to-tiff-with-mulitiple-pages.xlsx");

// Load the workbook
const wb = new AsposeCells.Workbook(filePath);

const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setImageType(AsposeCells.ImageType.Tiff);

// Set resolution to 200
imgOptions.setHorizontalResolution(200);
imgOptions.setVerticalResolution(200);

// Set TIFF compression to LZW
imgOptions.setTiffCompression(AsposeCells.TiffCompression.CompressionLZW);

const workbookRender = new AsposeCells.WorkbookRender(wb, imgOptions);
workbookRender.toImage("workbook-to-tiff-with-mulitiple-pages.tiff");
```  

## **Converting Worksheet to Image**  

Worksheets contain data that you want to analyze. For example, a worksheet can contain parameters, totals, percentages, exceptions, and calculations.  

As a developer, you might need to present worksheets as images. For example, you might need to use an image of a worksheet in an application or web page. You might want to insert an image into a Microsoft Word document, a PDF file, a PowerPoint presentation or some other document type. Simply put, you want a worksheet rendered as an image so that you can use it somewhere else.  

Aspose.Cells supports converting Excel worksheets to images. To use this feature, you need to import the [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/nodejs-cpp/) module to your program or project. It has several valuable classes for rendering and printing, for example [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender), and others.  

The [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender) class represents a worksheet to render as images. It has an overloaded method, [**toImage**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage), that can convert a worksheet to image file(s) with different attributes or options. It returns a Buffer object and you can save an image file to disk or stream. Several image formats are supported, for example BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.  

The following code snippet shows how to convert a worksheet in an Excel file to an image file.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = RunExamples.Get_SourceDirectory();
// Output directory
const outputDir = RunExamples.Get_OutputDirectory();

const filePath = path.join(sourceDir, "sampleConvertWorksheetToImageByPage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

const options = new AsposeCells.ImageOrPrintOptions();
options.setHorizontalResolution(200);
options.setVerticalResolution(200);
options.setImageType(AsposeCells.ImageType.Tiff);

// Sheet2Image By Page conversion
const sr = new AsposeCells.SheetRender(sheet, options);
for (let j = 0; j < sr.getPageCount(); j++) {
    sr.toImage(j, path.join(outputDir, `outputConvertWorksheetToImageByPage_${j + 1}.tif`));
}
```  

{{% alert color="primary" %}}  
At present, the API for converting worksheets to images does not support 3D bubble charts.  
{{% /alert %}}  

## **Converting Worksheet to SVG**  

SVG stands for Scalable Vector Graphics. SVG is a specification based on XML standards for two-dimensional vector graphics. It is an open standard that has been under development by the World Wide Web Consortium (W3C) since 1999.  

Aspose.Cells for Node.js via C++ has been able to convert worksheets to SVG image since version 7.1.0. The following code snippet shows how to convert a worksheet in an Excel file to an SVG image file.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(dataDir, "output");

// Instantiate a workbook
const workbook = new AsposeCells.Workbook();

// Put sample text in the first cell of the first worksheet in the newly created workbook
workbook.getWorksheets().get(0).getCells().get("A1").putValue("DEMO TEXT ON SHEET1");

// Add second worksheet in the workbook
workbook.getWorksheets().add(AsposeCells.SheetType.Worksheet);

// Set text in the first cell of the second sheet
workbook.getWorksheets().get(1).getCells().get("A1").putValue("DEMO TEXT ON SHEET2");

// Set currently active sheet index to 1 i.e. Sheet2
workbook.getWorksheets().setActiveSheetIndex(1);

// Save workbook to SVG. It shall render the active sheet only to SVG
workbook.save(path.join(outputDir, "ConvertWorksheetToSVG_out.svg"));
```  

## **Advance topics**  
- [Convert an Excel Chart to Image](/cells/nodejs-cpp/convert-an-excel-chart-to-image/)  
- [Converting Chart to Image in SVG Format](/cells/nodejs-cpp/converting-chart-to-image-in-svg-format/)  
- [Export Chart to SVG with viewBox attribute](/cells/nodejs-cpp/export-chart-to-svg-with-viewbox-attribute/)  
- [Track Conversion Progress of Excel to TIFF](/cells/nodejs-cpp/track-conversion-progress-of-excel-to-tiff/)  
  