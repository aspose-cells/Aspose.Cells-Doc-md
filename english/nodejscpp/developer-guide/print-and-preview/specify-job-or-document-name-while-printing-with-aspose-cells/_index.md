---  
title: Specify Job or Document Name while printing with Aspose.Cells for Node.js via C++  
linktitle: Specify Job or Document Name while printing with Aspose.Cells  
type: docs  
weight: 270  
url: /nodejs-cpp/specify-job-or-document-name-while-printing-with-aspose-cells/  
description: Learn how to specify job or document name while printing a workbook or worksheet using Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
You can specify Job or Document Name while printing your workbook or worksheet using the WorkbookRender or SheetRender objects. Aspose.Cells provides the WorkbookRender.toPrinter(printerName, jobName) and SheetRender.toPrinter(printerName, jobName) methods which you can use to specify Job Name while printing your workbook or worksheet.  
{{% /alert %}}  

## Specify Job or Document Name while printing with Aspose.Cells  

The sample code loads the source Excel file and then sends it to the printer by specifying the job or document name using the WorkbookRender.toPrinter(printerName, jobName) and SheetRender.toPrinter(printerName, jobName) methods.  

## Sample Code  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleBook.xlsx");
// Create workbook object from source Excel file
const workbook = new AsposeCells.Workbook(filePath);

let printerName = "";

while (!printerName || printerName.trim() === "") {
    console.log("Please Enter Your Printer Name:");
    printerName = require("readline-sync").question();
}

const jobName = "Job Name while Printing with Aspose.Cells";

// Print workbook using WorkbookRender
const wr = new AsposeCells.WorkbookRender(workbook, new AsposeCells.ImageOrPrintOptions());
try {
    wr.toPrinter(printerName, jobName);
} catch (ex) {
    console.log(ex.message);
}

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Print worksheet using SheetRender
const sr = new AsposeCells.SheetRender(worksheet, new AsposeCells.ImageOrPrintOptions());
try {
    sr.toPrinter(printerName, jobName);
} catch (ex) {
    console.log(ex.message);
}
```  
  