---
title: Skapa arbetsbok och kalkylblad med namn intervall med Node.js via C++
linktitle: Namngivet intervall
type: docs
weight: 40
url: /sv/nodejs-cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Lär dig hur man skapar arbetsbok och kalkylblad med namngivna intervall med Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

Microsoft Excel tillåter användare att definiera namngivna områden med två olika omfång: arbetsbok (också känt som globalt omfång) och arbetsblad.

- Namngivna områden med ett arbetsboksomfång kan kommas åt från vilket arbetsblad som helst inom den arbetsboken genom att helt enkelt använda dess namn.
- Arbetsbladscoped namngivna områden kommas åt med referensen till det specifika arbetsbladet där det skapades.

Aspose.Cells for Node.js via C++ tillhandahåller samma funktionalitet som Microsoft Excel för att lägga till namngivna områden som är beroende av arbetsbok och arbetsblad. När du skapar ett namngivet område som är beroende av ett arbetsblad, bör arbetsbladets referens användas i det namngivna området för att specificera det som ett arbetsbladberoende namn.

{{% /alert %}} 
## **Lägga till ett namngivet intervall med arbetsboksuppsikt**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook object
const workbook = new AsposeCells.Workbook();

// Get first worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Get worksheet's cells collection
const cells = sheet.getCells();

// Create a range of Cells from Cell A1 to C10
const workbookScope = cells.createRange("A1", "C10");

// Assign the name to workbook scope named range
workbookScope.setName("workbookScope");

// Save the workbook
workbook.save(path.join(dataDir, "WorkbookScope.out.xlsx"));
```
## **Lägg till ett namngivet område med arbetsbladomfång**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook object
const workbook = new AsposeCells.Workbook();

// Get first worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Get worksheet's cells collection
const cells = sheet.getCells();
// Create a range of Cells
const localRange = cells.createRange("A1", "C10");

// Assign name to range with sheet reference
localRange.setName("Sheet1!local");

// Save the workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Fortsatta ämnen**
- [Skapa åtkomst och kopiera namngivna områden](/cells/sv/nodejs-cpp/create-access-and-copy-named-ranges/)
- [Formatera och modifiera namngivna områden](/cells/sv/nodejs-cpp/format-and-modify-named-ranges/)
- [Hämta intervall med externa länkar](/cells/sv/nodejs-cpp/get-range-with-external-links/)
- [Implementera icke-sekventiella områden](/cells/sv/nodejs-cpp/implementing-non-sequential-ranges/)


{{< app/cells/assistant language="nodejs-cpp" >}}
