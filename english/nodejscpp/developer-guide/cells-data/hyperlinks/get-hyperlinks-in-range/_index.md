---
title: Get Hyperlinks in Range with Node.js via C++
type: docs
weight: 100
url: /nodejs-cpp/get-hyperlinks-in-range/
description: Learn how to get hyperlinks in range through the Aspose.Cells for Node.js via C++ API.
keywords: Get Hyperlinks in Range Node.js via C++, Get all the hyperlinks in the selected range Node.js via C++, Delete hyperlink in Range Node.js via C++, Delete the hyperlinks in the selected range Node.js via C++
---

## **Get Hyperlinks in Range**

The [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) class provides a [**hyperlinks**](https://reference.aspose.com/cells/nodejs-cpp/range/properties/hyperlinks) property which returns all the hyperlinks in the selected range. You may also delete the hyperlink by calling the [**Hyperlink.delete**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink/methods/delete) method.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(`${sourceDir}/HyperlinksSample.xlsx`);

// Get the first (default) worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a range A2:B3
const range = worksheet.getCells().createRange("A2", "B3");

// Get Hyperlinks in range
const hyperlinks = range.getHyperlinks();

hyperlinks.forEach(link => {
    console.log(`${link.getArea()} : ${link.getAddress()}`);
    
    // To delete the link, use the Hyperlink.Delete() method.
    link.delete();
});

workbook.save(`${outputDir}/HyperlinksSample_out.xlsx`);
```
