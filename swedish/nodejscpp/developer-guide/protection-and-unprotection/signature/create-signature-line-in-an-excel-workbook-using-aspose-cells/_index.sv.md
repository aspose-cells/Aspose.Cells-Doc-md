---  
title: Skapa underskriftslinje i en Excel arbetsbok med Aspose.Cells for Node.js via C++  
linktitle: Skapa signaturlinje i en Excel arbetsbok med hjälp av Aspose.Cells  
type: docs  
weight: 150  
url: /sv/nodejs-cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/  
description: Denna artikel beskriver hur man skapar en underskriftslinje i en Excel arbetsbok med Node.js kod med Aspose.Cells for Node.js via C++.  
keywords: Skapa underskriftslinje i en Excel arbetsbok Node.js via C++, hur man skapar en underskriftslinje i en Excel arbetsbok, hur man lägger till underskriftslinje, hur man lägger till underskriftslinje till Excel fil.  
---  

## **Introduktion**  

Microsoft Excel tillhandahåller en funktion för att lägga till **Signature Line** i Excel-arbetsböcker. Du kan lägga till en signaturlinje genom att klicka på fliken **Infoga** och sedan välja **Signaturlinje** från gruppen **Text**.  

## **Hur man skapar en signeringsrad för Excel**  

Aspose.Cells for Node.js via C++ tillhandahåller även denna funktion och har exponerat [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--)-egenskapen för detta ändamål. Denna artikel förklarar hur man använder denna egenskap för att lägga till en underskriftslinje med Aspose.Cells.  

 Följande exempel kod lägger till en underskriftslinje med [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--)-egenskapen och sparar arbetsboken.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Create signature line object
const signatureLine = new AsposeCells.SignatureLine();
signatureLine.setSigner("John Doe");
signatureLine.setTitle("Development Lead");
signatureLine.setEmail("john.doe@aspose.com");

// Adds a Signature Line to the worksheet.
workbook.getWorksheets().get(0).getShapes().addSignatureLine(1, 1, signatureLine);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
