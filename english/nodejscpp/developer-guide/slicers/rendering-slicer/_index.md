---  
title: Rendering Slicer with Node.js via C++  
linktitle: Rendering Slicer  
type: docs  
weight: 40  
url: /nodejs-cpp/rendering-slicer/  
---  

## **Possible Usage Scenarios**  
Aspose.Cells for Node.js via C++ supports the rendering of slicer shapes. If you convert your worksheet into an image or save your workbook to PDF or HTML formats, you will see that slicers are rendered properly.  

## **Rendering Slicer**  
The following sample code loads the [sample Excel file](67338479.xlsx) that contains an existing slicer. It converts the worksheet into an image by setting the print area that covers only the slicer. The resulting image is the [output image](67338480.png) that shows the rendered slicer. As you can see, the slicer has been rendered properly and looks the same as in the sample Excel file.  

![todo:image_alt_text](rendering-slicer_1)  
## **Sample Code**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRenderingSlicer.xlsx");

// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Set the print area because we want to render slicer only.
ws.getPageSetup().setPrintArea("B15:E25");

// Specify image or print options, set one page per sheet and only area to true.
const imgOpts = new AsposeCells.ImageOrPrintOptions();
imgOpts.setHorizontalResolution(200);
imgOpts.setVerticalResolution(200);
imgOpts.setImageType(AsposeCells.ImageType.Png);
imgOpts.setOnePagePerSheet(true);
imgOpts.setOnlyArea(true);

// Create sheet render object and render worksheet to image.
const sr = new AsposeCells.SheetRender(ws, imgOpts);
sr.toImage(0, "outputRenderingSlicer.png");
```  
  