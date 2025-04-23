---  
title: Imprimir comentarios al guardar en PDF con Node.js via C++  
linktitle: Imprimir comentarios al guardar en PDF  
type: docs  
weight: 10  
url: /es/nodejs-cpp/print-comments-while-saving-to-pdf/  
description: Aprenda cómo imprimir comentarios al guardar documentos de Excel en PDF usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Microsoft Excel te permite imprimir comentarios al imprimir o guardar en formato PDF con las siguientes opciones  

- Ninguno  
- Al final de la hoja  
- Según se muestra en la hoja  

Aspose.Cells proporciona la enumeración [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) para soportar la misma función. La enumeración [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) tiene los siguientes miembros  

- PrintNoComments  
- PrintInPlace  
- PrintSheetEnd  

{{% /alert %}}  

## **Imprimir comentarios al guardar en PDF**  

El siguiente código de ejemplo ilustra cómo usar [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) para imprimir comentarios al guardar en PDF.  

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

