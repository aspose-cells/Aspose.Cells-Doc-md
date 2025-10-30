---  
title: Stampa Commenti durante il salvataggio in PDF con Node.js tramite C++  
linktitle: Stampa commenti durante il salvataggio in PDF  
type: docs  
weight: 10  
url: /it/nodejs-cpp/print-comments-while-saving-to-pdf/  
description: Impara come stampare commenti quando salvi documenti Excel in PDF usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Microsoft Excel consente di stampare i commenti durante la stampa o il salvataggio nel formato PDF con le seguenti opzioni  

- Nessuna  
- Alla fine del foglio  
- Come visualizzato nel foglio  

Aspose.Cells fornisce l'enum [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) per supportare la stessa funzione. L'enum [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) ha i seguenti membri.  

- PrintNoComments  
- PrintInPlace  
- PrintSheetEnd  

{{% /alert %}}  

## **Stampa commenti durante il salvataggio in PDF**  

Il seguente esempio di codice illustra come usare [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) per stampare commenti durante il salvataggio in PDF.  

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
