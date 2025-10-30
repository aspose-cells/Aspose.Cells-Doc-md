---  
title: Skydda och avsäkra arbetsboksstrukturen med Node.js via C++  
linktitle: Skydda och avskydda arbetsbokens struktur  
type: docs  
weight: 40  
url: /sv/nodejs-cpp/protect-and-unprotect-workbook-structure/  
description: Skydda och avsäkra arbetsboksstrukturen för Excel filer med Node.js via C++  
---  


{{% alert color="primary" %}}  
För att förhindra att andra användare ser dolda kalkylblad, lägger till, flyttar, tar bort eller gömmer kalkylbladen, och döper om kalkylbladen, kan du skydda strukturen för din Excel-arbetsbok med ett lösenord.  
{{% /alert %}}  


## **Skydda och avskydda arbetsbokens struktur i MS Excel**  

**![skydda och avskydda arbetsbokens struktur](skydda-och-avskydda-arbetsbokens-struktur.png)**  

1. Klicka på **Granska > Skydda arbetsbok**.  
1. Ange ett lösenord i **Lösenordsrutan**.  
1. Välj **OK**, ange lösenordet igen för att bekräfta det, och välj sedan **OK** igen.  


## **Skydda arbetsboksstrukturen med Aspose.Cells for Node.js via C++**  
Bara behöver följande enkla koder för att implementera skydd av arbetsbokens struktur för Excel-filer.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Create a new file.
const workbook = new AsposeCells.Workbook();
// Protect workbook structure.
workbook.protect(AsposeCells.ProtectionType.Structure, "password");
// Save Excel file.
workbook.save(filePath);
```  

## **Avsäkra arbetsboksstrukturen med Aspose.Cells for Node.js via C++**  
Det är enkelt att avskydda arbetsbokens struktur med Aspose.Cells API.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open an Excel file which workbook structure is protected.
const workbook = new AsposeCells.Workbook(filePath);
// Unprotect workbook structure.
workbook.unprotect("password");
// Save Excel file.
workbook.save(filePath);
```  

{{% alert color="primary" %}}  
Observera: Ett korrekt lösenord krävs.  
{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
