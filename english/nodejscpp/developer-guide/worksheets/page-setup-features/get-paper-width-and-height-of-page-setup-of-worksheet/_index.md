---
title: Get Paper Width and Height of Page Setup of Worksheet with Node.js via C++
linktitle: Get Paper Width and Height of Page Setup of Worksheet
type: docs
weight: 50
url: /nodejs-cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Discover how to get the Excel Worksheet Page Setup Paper Width and Height using Node.js via C++ programmatically.
keywords: excel page setup paper width Node.js via C++, excel page setup paper height Node.js via C++
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Sometimes, you need to know the width and height of paper size as it has been set in the page setup of the worksheet. Please use the [**PageSetup.getPaperWidth()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperWidth--) and [**PageSetup.getPaperHeight()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperHeight--) properties for this purpose.

## **Get Paper Width and Height of Page Setup of Worksheet**

The following sample code explains the usage of [**PageSetup.getPaperWidth()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperWidth--) and [**PageSetup.getPaperHeight()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperHeight--) properties. It first changes the paper size to *A2* and then finds the width and height of the paper, then it changes it to *A3*, *A4*, *Letter* and finds the width and height of the paper respectively.

### **Sample Code**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create an instance of Workbook class
const book = new AsposeCells.Workbook();

// Access first worksheet
const sheet = book.getWorksheets().get(0);

// Set paper size to A2 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA2);
console.log("PaperA2: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to A3 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3);
console.log("PaperA3: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to A4 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);
console.log("PaperA4: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to Letter and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperLetter);
console.log("PaperLetter: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());
```

### **Console Output**

Here is the console output of the above sample code.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
