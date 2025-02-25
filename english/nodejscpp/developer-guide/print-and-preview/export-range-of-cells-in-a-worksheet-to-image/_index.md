---  
title: Export Range of Cells in a Worksheet to Image with Node.js via C++  
linktitle: Export Range of Cells in a Worksheet to Image  
type: docs  
weight: 60  
url: /nodejs-cpp/export-range-of-cells-in-a-worksheet-to-image/  
---  

## **Possible Usage Scenarios**  

You can make an image of a worksheet using Aspose.Cells for Node.js via C++. However, sometimes you need to export only a range of cells in a worksheet to an image. This article explains how to achieve this.  

## **Export Range of Cells in a Worksheet to Image**  

To take an image of a range, set the print area to the desired range and then set all margins to 0. Also set [**ImageOrPrintOptions.onePagePerSheet**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#onePagePerSheet-boolean-) to **true**. The following code takes an image of the range D8:G16. Below is a screenshot of the [sample Excel file](47153160.xlsx) used in the code. You can try the code with any Excel file.  

## **Screenshot of Sample Excel File and its Exported Image**  

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**  

Executing the code creates an image of the range D8:G16 only.  

**![todo:image_alt_text](Output-Image.png)**  

## **Sample Code**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = RunExamples.Get_SourceDirectory();

// Output directory
const outputDir = RunExamples.Get_OutputDirectory();

// Create workbook from source file.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleExportRangeOfCellsInWorksheetToImage.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the print area with your desired range
worksheet.getPageSetup().setPrintArea("D8:G16");

// Set all margins as 0
worksheet.getPageSetup().setLeftMargin(0);
worksheet.getPageSetup().setRightMargin(0);
worksheet.getPageSetup().setTopMargin(0);
worksheet.getPageSetup().setBottomMargin(0);

// Set OnePagePerSheet option as true
const options = new AsposeCells.ImageOrPrintOptions();
options.setOnePagePerSheet(true);
options.setImageType(AsposeCells.ImageType.Jpeg);
options.setHorizontalResolution(200);
options.setVerticalResolution(200);

// Take the image of your worksheet
const sr = new AsposeCells.SheetRender(worksheet, options);
sr.toImage(0, path.join(outputDir, "outputExportRangeOfCellsInWorksheetToImage.jpg"));
```  
  