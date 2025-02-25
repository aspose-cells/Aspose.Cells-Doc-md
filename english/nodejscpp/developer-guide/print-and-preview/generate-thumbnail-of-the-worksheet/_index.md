---
title: Generate Thumbnail of the Worksheet with Node.js via C++
linktitle: Generate Thumbnail of the Worksheet
type: docs
weight: 110
url: /nodejs-cpp/generate-thumbnail-of-the-worksheet/
description: Learn how to generate a thumbnail image from a worksheet using Aspose.Cells for Node.js via C++. Create small images for previews in documents and presentations.
---

{{% alert color="primary" %}} 

It can be useful to generate thumbnails from worksheets. A thumbnail is a small image that can be pasted into a Word document or a PowerPoint presentation to give a preview of what's on the worksheet. It can be added to a webpage with a link to download the original document and has a host of other uses.

{{% /alert %}} 

Aspose.Cells for Node.js via C++ allows you to output worksheets to image files so making a thumbnail is easy. The sample code below shows you how to output worksheets to image files.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = RunExamples.Get_SourceDirectory();

// Output directory
const outputDir = RunExamples.Get_OutputDirectory();

// Instantiate and open an Excel file
const filePath = path.join(sourceDir, "sampleGenerateThumbnailOfWorksheet.xlsx");
const book = new AsposeCells.Workbook(filePath);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Set the vertical and horizontal resolution
imgOptions.setVerticalResolution(200);
imgOptions.setHorizontalResolution(200);

// One page per sheet is enabled
imgOptions.setOnePagePerSheet(true);

// Get the first worksheet
const sheet = book.getWorksheets().get(0);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Render the image for the sheet
const bmp = sr.toImage(0);

// Create a bitmap
const thumb = new Bitmap(600, 600);

// Get the graphics for the bitmap
const gr = System.Drawing.Graphics.FromImage(thumb);

if (bmp !== null) {
    // Draw the image
    gr.drawImage(bmp, 0, 0, 600, 600);
}

// Save the thumbnail
thumb.Save(path.join(outputDir, "outputGenerateThumbnailOfWorksheet.bmp"));
```
