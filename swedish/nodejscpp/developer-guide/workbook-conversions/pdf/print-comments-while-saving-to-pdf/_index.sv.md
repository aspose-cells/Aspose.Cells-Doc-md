---  
title: Skriv ut kommentarer när du sparar till PDF med Node.js via C++  
linktitle: Skriv ut kommentarer vid sparning till PDF  
type: docs  
weight: 10  
url: /sv/nodejs-cpp/print-comments-while-saving-to-pdf/  
description: Lär dig hur du skriver ut kommentarer när du sparar Excel dokument till PDF med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Microsoft Excel låter dig skriva ut kommentarer när du skriver ut eller sparar till PDF-format med följande alternativ  

- Ingen  
- I slutet av bladet  
- Enligt visad på kalkylbladet  

Aspose.Cells tillhandahåller enum [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) för att stödja samma funktionalitet. Enum [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) har följande medlemmar  

- PrintNoComments  
- PrintInPlace  
- PrintSheetEnd  

{{% /alert %}}  

## **Skriv ut kommentarer vid sparande till PDF**  

Följande exempel kod visar hur man använder [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) för att skriva ut kommentarer när man sparar till PDF.  

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
