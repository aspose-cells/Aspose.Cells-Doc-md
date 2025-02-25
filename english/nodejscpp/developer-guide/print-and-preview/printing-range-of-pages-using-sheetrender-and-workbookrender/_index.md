---  
title: Printing Range of Pages using SheetRender and WorkbookRender with Node.js via C++  
linktitle: Printing Range of Pages using SheetRender and WorkbookRender  
type: docs  
weight: 250  
url: /nodejs-cpp/printing-range-of-pages-using-sheetrender-and-workbookrender/  
description: Learn how to print a range of pages using SheetRender and WorkbookRender in Node.js via C++.  
---  

{{% alert color="primary" %}}  

Microsoft Excel allows you to print a range of pages of a workbook or worksheet. The following screenshot shows the Microsoft Excel interface to specify the range of pages.

Aspose.Cells provides the `WorkbookRender.toPrinter(printerName: string, printPageIndex: number, printPageCount: number)` and `SheetRender.toPrinter(printerName: string, printPageIndex: number, printPageCount: number)` methods for this purpose.

{{% /alert %}}  
## **Microsoft Excel Interface to specify the Range of Pages to Print**  
The following sample code illustrates the use of `WorkbookRender.toPrinter(printerName: string, printPageIndex: number, printPageCount: number)` and `SheetRender.toPrinter(printerName: string, printPageIndex: number, printPageCount: number)` methods. It prints the pages 2-5 of the workbook and worksheet.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleBook.xlsx");
// Create workbook from source Excel file
const workbook = new AsposeCells.Workbook(filePath);

let printerName = "";

while (!printerName || printerName.trim().length === 0) {
    console.log("Please Enter Your Printer Name:");
    const stdin = require("readline").createInterface({
        input: process.stdin,
        output: process.stdout
    });
    printerName = await new Promise(resolve => {
        stdin.question("", input => {
            stdin.close();
            resolve(input);
        });
    });
}

const bookRenderOptions = new AsposeCells.ImageOrPrintOptions();
bookRenderOptions.setPageIndex(1);
bookRenderOptions.setPageCount(2);
// Print the workbook specifying the range of pages. Here we are printing pages 2-3
const wr = new AsposeCells.WorkbookRender(workbook, bookRenderOptions);
try {
    wr.toPrinter(printerName);
} catch (ex) {
    console.log(ex.message);
}

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

const sheetRenderOptions = new AsposeCells.ImageOrPrintOptions();
sheetRenderOptions.setPageIndex(1);
sheetRenderOptions.setPageCount(2);
// Print the worksheet specifying the range of pages. Here we are printing pages 2-3
const sr = new AsposeCells.SheetRender(worksheet, sheetRenderOptions);
try {
    sr.toPrinter(printerName);
} catch (ex) {
    console.log(ex.message);
}
```  
  