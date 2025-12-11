---  
title: Print Comments while saving to PDF with Node.js via C++  
linktitle: Print Comments while saving to PDF  
type: docs  
weight: 10  
url: /nodejs-cpp/print-comments-while-saving-to-pdf/  
description: Learn how to print comments when saving Excel documents to PDF using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"  
---  

{{% alert color="primary" %}}  

Microsoft Excel allows you to print comments when printing or saving to PDF format, with the following options:  

- None  
- At the end of the sheet  
- As displayed on the sheet  

Aspose.Cells provides the [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) enum to support the same feature. The [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) enum has the following members:  

- PrintNoComments  
- PrintInPlace  
- PrintSheetEnd  

{{% /alert %}}  

## **Print Comments while saving to PDF**  

The following sample code illustrates how to use [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) to print comments while saving to PDF.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook from the source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleWorkbookWithComments.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

/*
* To print no comments, use "PrintCommentsType.PrintNoComments".
* To print the comments as displayed on the sheet, use "PrintCommentsType.PrintInPlace".
* To print the comments at the end of the sheet, use "PrintCommentsType.PrintSheetEnd".
*/
worksheet.getPageSetup().setPrintComments(AsposeCells.PrintCommentsType.PrintSheetEnd);

// Save the workbook in PDF format
workbook.save(path.join(dataDir, "PrintCommentWhileSavingToPdf_out.pdf"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
