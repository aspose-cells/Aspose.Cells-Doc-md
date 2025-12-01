---
title: Generate Thumbnail of the Worksheet with Node.js via C++
linktitle: Generate Thumbnail of the Worksheet
type: docs
weight: 110
url: /nodejs-cpp/generate-thumbnail-of-the-worksheet/
description: Learn how to generate a thumbnail image from a worksheet using Aspose.Cells for Node.js via C++. Create small images for previews in documents and presentations.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

It can be useful to generate thumbnails from worksheets. A thumbnail is a small image that can be pasted into a Word document or a PowerPoint presentation to give a preview of what's on the worksheet. It can be added to a webpage with a link to download the original document and has a host of other uses.

{{% /alert %}} 

Aspose.Cells for Node.js via C++ allows you to output worksheets to image files so making a thumbnail is easy. The sample code below shows you how to output worksheets to image files.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

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

// Set desired thumbnail dimensions
imgOptions.setDesiredSize(600, 600, true);

// Get the first worksheet
const sheet = book.getWorksheets().get(0);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Save the thumbnail directly
sr.toImage(0, path.join(outputDir, "outputGenerateThumbnailOfWorksheet.jpg"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
