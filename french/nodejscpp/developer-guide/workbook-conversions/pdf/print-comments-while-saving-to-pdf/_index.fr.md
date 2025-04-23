---  
title: Imprimer les commentaires lors de l enregistrement en PDF avec Node.js via C++  
linktitle: Imprimer les commentaires lors de l enregistrement au format PDF  
type: docs  
weight: 10  
url: /fr/nodejs-cpp/print-comments-while-saving-to-pdf/  
description: Apprenez comment imprimer les commentaires lors de la sauvegarde des documents Excel en PDF en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Microsoft Excel permet d'imprimer les commentaires lors de l'impression ou de l'enregistrement au format PDF avec les options suivantes  

- Aucun  
- À la fin de la feuille  
- Tel qu'affiché sur la feuille  

Aspose.Cells fournit l'énumération [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) pour supporter la même fonctionnalité. L'énumération [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) comporte les membres suivants  

- PrintNoComments  
- PrintInPlace  
- PrintSheetEnd  

{{% /alert %}}  

## **Imprimer les commentaires lors de l'enregistrement au format PDF**  

Le code d'exemple suivant illustre comment utiliser [**PrintCommentsType**](https://reference.aspose.com/cells/nodejs-cpp/printcommentstype) pour imprimer les commentaires lors de l'enregistrement en PDF.  

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

