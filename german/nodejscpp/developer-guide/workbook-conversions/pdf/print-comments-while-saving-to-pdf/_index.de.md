---  
title: Kommentare beim Speichern in PDF mit Node.js via C++ drucken  
linktitle: Kommentare beim Speichern in PDF drucken  
type: docs  
weight: 10  
url: /de/nodejs-cpp/print-comments-while-saving-to-pdf/  
description: Erfahren Sie, wie Sie Kommentare beim Speichern von Excel Dokumenten in PDF mit Aspose.Cells for Node.js via C++ drucken.  
---  

{{% alert color="primary" %}}  

Microsoft Excel ermöglicht es Ihnen, Kommentare beim Drucken oder Speichern im PDF-Format mit den folgenden Optionen zu drucken:  

- Keine  
- Am Ende des Blattes  
- Wie auf dem Blatt angezeigt  

Aspose.Cells bietet das [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) Enum zur Unterstützung derselben Funktion. Das [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) Enum hat die folgenden Mitglieder  

- PrintNoComments  
- PrintInPlace  
- PrintSheetEnd  

{{% /alert %}}  

## **Kommentare drucken beim Speichern als PDF**  

Das folgende Beispiel zeigt, wie [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) verwendet wird, um Kommentare beim Speichern in PDF zu drucken.  

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

