---
title: Kopiera och flytta arbetsblad inom och mellan arbetsböcker med Node.js via C++
linktitle: Kopiera och flytta arbetsblad inom och mellan arbetsböcker
type: docs
weight: 80
url: /sv/nodejs-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Lär dig hur du kopierar och flyttar arbetsblad inom och mellan arbetsböcker med Aspose.Cells for Node.js via C++. Hantera effektivt strukturerna i dina arbetsböcker.
---

{{% alert color="primary" %}}

Ibland behöver du ett antal arbetsblad med gemensam formatering och datainmatning. Till exempel, om du arbetar med kvartalsvisa budgetar, kanske du vill skapa en arbetsbok med blad som innehåller samma kolumnrubriker, radrubriker och formler. Det finns ett sätt att göra detta: genom att skapa ett blad och sedan kopiera det tre gånger.

Aspose.Cells for Node.js via C++ stöder kopiering eller flytt av arbetsblad inom eller mellan arbetsböcker. Arbetsblad inklusive data, formatering, tabeller, matriser, diagram, bilder och andra objekt kopieras med högsta precision.

{{% /alert %}}

## **Kopiera och flytta arbetsblad**

### **Kopiera ett arbetsblad inom en arbetsbok**

De inledande stegen är desamma för alla exemplen.

1. Skapa två arbetsböcker med lite data i Microsoft Excel. För detta exempel skapade vi två nya arbetsböcker i Microsoft Excel och matade in data i kalkylbladen.

- FirstWorkbook.xlsx (3 kalkylblad).
- SecondWorkbook.xlsx (1 kalkylblad).

1. Ladda ner och installera Aspose.Cells:
   1. [Ladda ner Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).
   1. Installera det på din utvecklingsdator.
      Alla [Aspose](http://www.aspose.com/) -komponenter fungerar i utvärderingsläge när de är installerade. Utvärderingsläget har ingen tidsbegränsning och det lägger bara till vattenstämplar i producerade dokument.
1. Skapa ett projekt:
   1. Starta din utvecklingsmiljö.
   1. Skapa en ny konsolapplikation.
1. Lägg till referenser:
   1. Lägg till en referens till Aspose.Cells till projektet.
      Till exempel, lägg till en referens till ...\Program Files\Aspose\Aspose.Cells\Bin\NodeJs\Aspose.Cells.dll
1. Kopiera kalkylbladet inom en arbetsbok
   Det första exemplet kopierar det första kalkylbladet (Kopiera) inom FirstWorkbook.xlsx.

När koden körs kopieras kalkylbladet med namnet Kopiera inom FirstWorkbook.xlsx med namnet Sista blad.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open a file into the first book.
const excelWorkbook1 = new AsposeCells.Workbook(path.join(dataDir, "FirstWorkbook.xlsx"));

// Copy the first sheet of the first book within the workbook
excelWorkbook1.getWorksheets().get(2).copy(excelWorkbook1.getWorksheets().get("Copy"));

// Save the file.
excelWorkbook1.save(path.join(dataDir, "FirstWorkbookCopied_out.xlsx"));
```

### **Flytta ett blad inom en arbetsbok**

Koden nedan visar hur man flyttar ett blad från en position i en arbetsbok till en annan. Utförande av koden flyttar bladet som kallas Flytta från index 1 till index 2 i FirstWorkbook.xlsx.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "FirstWorkbook.xlsx");
// Open a file into the first book.
const excelWorkbook2 = new AsposeCells.Workbook(filePath);

// Move the sheet
const worksheets = excelWorkbook2.getWorksheets();
const worksheet = worksheets.get(0);
worksheet.moveTo(1);

// Save the file.
excelWorkbook2.save(path.join(dataDir, "FirstWorkbookMoved_out.xlsx"));
```

### **Kopiera ett kalkylblad mellan arbetsböcker**

När koden körs kopieras arbetsbladet som heter Copy till SecondWorkbook.xlsx med namnet Sheet2.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const excelWorkbook3 = new AsposeCells.Workbook();
const excelWorkbook4 = new AsposeCells.Workbook();

// Create source worksheet
excelWorkbook3.getWorksheets().add("Copy");

// Add new worksheet into second Workbook
excelWorkbook4.getWorksheets().add();

// Copy the first sheet of the first book into second book.
excelWorkbook4.getWorksheets().get(1).copy(excelWorkbook3.getWorksheets().get("Copy"));

// Save the file.
excelWorkbook4.save(path.join(dataDir, "CopyWorksheetsBetweenWorkbooks_out.xlsx"));
```

### **Flytta ett kalkylblad mellan arbetsböcker**

Genom att köra koden flyttas bladet med namnet Flytta från FirstWorkbook.xlsx till SecondWorkbook.xlsx med namnet Sheet3.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbooks instead of opening existing files
const excelWorkbook5 = new AsposeCells.Workbook();
const excelWorkbook6 = new AsposeCells.Workbook();

// Add New Worksheet
excelWorkbook6.getWorksheets().add();

// Copy the sheet from first book into second book.
excelWorkbook6.getWorksheets().get(0).copy(excelWorkbook5.getWorksheets().get(0));

// Remove the copied worksheet from first workbook
excelWorkbook5.getWorksheets().removeAt(0);

// Save the file.
excelWorkbook5.save(path.join(dataDir, "FirstWorkbookWithMove_out.xlsx"));

// Save the file.
excelWorkbook6.save(path.join(dataDir, "SecondWorkbookWithMove_out.xlsx"));
```
