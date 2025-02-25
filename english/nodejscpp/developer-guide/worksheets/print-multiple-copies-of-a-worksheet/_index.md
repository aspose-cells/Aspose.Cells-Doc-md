---
title: Print multiple copies of a worksheet with Node.js via C++
linktitle: Print multiple copies of a worksheet
type: docs
weight: 170
url: /nodejs-cpp/print-multiple-copies-of-a-worksheet/
description: This article shows how to use the Node.js API with C++ addons to print multiple copies of an Excel worksheet programmatically.
keywords: print multiple excel copies Node.js via C++, print worksheets Node.js via C++
---

## **Print multiple copies of a worksheet**

Aspose.Cells provides the ability to print multiple copies of a worksheet by using the [**SheetRender.toPrinter(PrinterSettings)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toPrinter-PrinterSettings-) method. The following code snippet demonstrates the use of  [**SheetRender.toPrinter(PrinterSettings)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toPrinter-PrinterSettings-) method to print multiple copies of a worksheet. The following code snippet uses this [sample excel file](95584275.xlsx).

### Sample Code

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = RunExamples.Get_SourceDirectory();

// Load source Excel file
const filePath = path.join(sourceDir, "SheetRenderSample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const imgOpt = new AsposeCells.ImageOrPrintOptions();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(1);

const sheetRender = new AsposeCells.SheetRender(worksheet, imgOpt);

const printerSettings = new AsposeCells.PrinterSettings();
printerSettings.setPrinterName("<PRINTER NAME>");
printerSettings.setCopies(2);

sheetRender.toPrinter(printerSettings);
```
