---
title: Insert Background Image to Excel with Node.js via C++
linktitle: Insert Background Image to Excel
type: docs
weight: 90
url: /nodejs-cpp/insert-background-image-to-excel/
description: "How to insert a background image to Excel using Aspose.Cells for Node.js via C++."
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

You can make a worksheet more appealing by adding a picture as a worksheet background. This feature can be quite effective if you have a special corporate graphic that adds a hint of the background without obscuring the data on the sheet. You can set a background picture for a sheet using Aspose.Cells API.

{{% /alert %}} 

## **Setting Sheet Background in Microsoft Excel**

To set a sheet's background image in Microsoft Excel (for example, Microsoft Excel 2019):

1. From the **Page Layout** menu, find the **Page Setup** option, and then click the **Background** option.
2. Select a picture to set as the sheet's background.

   **Setting a sheet background**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **Setting Sheet Background with Aspose.Cells for Node.js via C++**

The code below sets a background image using an image from a stream.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const backgroundImagePath = path.join(dataDir, "background.jpg");

// Create a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Set the background image for the worksheet.
sheet.setBackgroundImage(fs.readFileSync(backgroundImagePath).buffer);

// Save the Excel file
workbook.save("outputBackImageSheet.xlsx");

// Save the HTML file
workbook.save("outputBackImageSheet.html", AsposeCells.SaveFormat.Html);
```

## Related Articles

- [Working with Background in ODS Files](/cells/nodejs-cpp/working-with-background-in-ods-files/)

{{< app/cells/assistant language="nodejs-cpp" >}}
