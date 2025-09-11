---
title: Avoid Blank Page in Output PDF when there is Nothing to Print with Node.js via C++
linktitle: Avoid Blank Page in Output PDF when there is Nothing to Print
type: docs
weight: 30
url: /nodejs-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Learn how to avoid blank pages in output PDF when there is nothing to print using Aspose.Cells for Node.js via C++.
---

## **Possible Usage Scenarios**

When the Excel file is empty and the user saves it to PDF using Aspose.Cells for Node.js via C++, it renders a blank page in the output PDF. Sometimes, this default behavior is undesirable. Aspose.Cells provides the [**PdfSaveOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOutputBlankPageWhenNothingToPrint--) property to handle this issue. If you set it to **false**, then exception will occur whenever there is nothing to print in the output PDF.

## **Avoid Blank Page in Output PDF when there is Nothing to Print**

The following sample code creates an empty workbook and then saves it as PDF after setting the [**PdfSaveOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOutputBlankPageWhenNothingToPrint--) property to **false**. Since there is nothing to print in the output PDF, the exception occurs as shown below.

## **Sample Code**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Create Pdf save options.
const opts = new AsposeCells.PdfSaveOptions();

// Default value of OutputBlankPageWhenNothingToPrint is true.
// Setting false means - Do not output blank page when there is nothing to print.
opts.setOutputBlankPageWhenNothingToPrint(false);

// Save workbook to Pdf format, it will throw exception because workbook has nothing to print.
const ms = new Uint8Array();

try {
// Save to Pdf format. It will throw exception.
wb.save(ms, opts);
} catch (ex) {
console.error("Exception Message: " + ex.message + "\r\n");
}
```

## **Exception**

{{< highlight javascript >}}

 exception was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}