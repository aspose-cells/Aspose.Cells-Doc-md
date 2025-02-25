---
title: Output Blank Page when there is Nothing to Print with Node.js via C++
linktitle: Output Blank Page when there is Nothing to Print
type: docs
weight: 90
url: /nodejs-cpp/output-blank-page-when-there-is-nothing-to-print/
---

## **Possible Usage Scenarios**

If the sheet is empty, then Aspose.Cells will not print anything when you export the worksheet to an image. You can change this behavior by using [**ImageOrPrintOptions.outputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#outputBlankPageWhenNothingToPrint-boolean-) property. When you set it **true**, it will print the blank page.

## **Output Blank Page when there is Nothing to Print**

The following sample code creates an empty workbook which has an empty worksheet and renders the empty worksheet to an image after setting the [**ImageOrPrintOptions.outputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#outputBlankPageWhenNothingToPrint-boolean-) property as **true**. Consequently, it generates the blank page as there is nothing to print which you can see in the image below.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Output directory
const outputDir = RunExamples.Get_OutputDirectory();

// Create workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet - it is empty sheet
const ws = wb.getWorksheets().get(0);

// Specify image or print options
// Since the sheet is blank, we will set OutputBlankPageWhenNothingToPrint to true
// So that empty page gets printed
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Png);
opts.setOutputBlankPageWhenNothingToPrint(true);

// Render empty sheet to png image
const sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, path.join(outputDir, "OutputBlankPageWhenNothingToPrint.png"));
```