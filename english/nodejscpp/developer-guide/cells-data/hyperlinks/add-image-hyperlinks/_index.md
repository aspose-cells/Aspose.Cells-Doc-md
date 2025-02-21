---
title: Add Image Hyperlinks with Node.js via C++
type: docs
weight: 140
url: /nodejs-cpp/add-image-hyperlinks/
description: Learn how to Add Image Hyperlinks through the Aspose.Cells for Node.js via C++ API.
keywords: Add Image Hyperlinks Node.js via C++, Insert Image Hyperlinks Node.js via C++
---

{{% alert color="primary" %}} 

Hyperlinks are useful for accessing information on other worksheets, or on websites. Microsoft Excel lets users add hyperlinks on text in cells, and on images. Image hyperlinks can make navigating a worksheet easier, for example, as next and previous buttons, or logos that link to particular sites. This document explains how to insert image hyperlinks in a worksheet using Aspose.Cells for Node.js via C++.

{{% /alert %}} 

Aspose.Cells for Node.js via C++ allows you to add hyperlinks to images in spreadsheets at runtime. It is possible to set and modify the link's screen tip and address. The following sample code illustrates how to add an image hyperlink into a worksheet.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
const fs = require("fs");
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir);
}

// Instantiate a new workbook
let workbook = new AsposeCells.Workbook();

// Get the first worksheet
let worksheet = workbook.getWorksheets().get(0);

// Insert a string value to a cell
worksheet.getCells().get("C2").putValue("Image Hyperlink");

// Set the 4th row height
worksheet.getCells().setRowHeight(3, 100);

// Set the C column width
worksheet.getCells().setColumnWidth(2, 21);

// Add a picture to the C4 cell
let index = worksheet.getPictures().add(3, 2, 4, 3, path.join(dataDir, "aspose-logo.jpg"));

// Get the picture object
let pic = worksheet.getPictures().get(index);

// Set the placement type
pic.setPlacement(AsposeCells.Drawing.PlacementType.FreeFloating);

// Add an image hyperlink
let hlink = pic.addHyperlink("http://www.aspose.com/");

// Specify the screen tip
hlink.setScreenTip("Click to go to Aspose site");
let outputFilePath = path.join(dataDir, "ImageHyperlink.out.xls");
// Save the Excel file
workbook.save(outputFilePath);
```
