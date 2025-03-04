---
title: Extract Images from Worksheets using ImageOrPrintOptions with Node.js via C++
linktitle: Extract Images from Worksheets using ImageOrPrintOptions
type: docs
weight: 140
url: /nodejs-cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: Learn how to extract images from Excel worksheets and save them using Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}} 

Microsoft Excel users can add images to spreadsheets. With Aspose.Cells for Node.js via C++, it's possible to read images from Microsoft Excel files and save them to a local drive. This article shows how.

{{% /alert %}} 

The sample code below shows how to extract images from an Excel file and save them.



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleExtractImagesFromWorksheets.xlsx"));

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get the first Picture in the first worksheet
const pic = worksheet.getPictures().get(0);

// Set the output image file path
const picformat = pic.getImageType().toString();

// Note: you may evaluate the image format before specifying the image path
// Define ImageOrPrintOptions
const printoption = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
printoption.setImageType(AsposeCells.ImageType.Jpeg);

// Save the image
pic.toImage(path.join(outputDir, "outputExtractImagesFromWorksheets.jpg"), printoption);
```
