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

Microsoft Excel allows you to print comments while printing or saving to PDF format with the following options  

- None  
- At end of sheet  
- As displayed on sheet  

Aspose.Cells provide the [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) enum to support the same feature. The [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) enum has the following members  

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
* For print no comments use "PrintCommentsType.PrintNoComments"
* and for print the comments as displayed on sheet use "PrintCommentsType.PrintInPlace"
* For Print the comments at the end of sheet we use "PrintCommentsType.PrintSheetEnd"
*/
worksheet.getPageSetup().setPrintComments(AsposeCells.PrintCommentsType.PrintSheetEnd);

// Save workbook in pdf format
workbook.save(path.join(dataDir, "PrintCommentWhileSavingToPdf_out.pdf"));
```  
  
{{< app/cells/assistant language="nodejs-cpp" >}}
