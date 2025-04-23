---
title: Kopiera och flytta arbetsblad med Node.js via C++
linktitle: Kopiera och Flytta Kalkylblad
type: docs
weight: 10
url: /sv/nodejs-cpp/copying-and-moving-worksheets/
description: Denna artikel inkluderar exempel på kod och beskriver hur man kopierar och flyttar arbetsblad programmatiskt inom en Excel arbetsbok och mellan Excel arbetsböcker med Node.js API och C++.
keywords: kopiera kalkylblad Node.js, flytta kalkylblad Node.js
---

{{% alert color="primary" %}}

Ibland behöver du ett antal kalkylblad med gemensam formatering och data. Till exempel, om du arbetar med kvartalsvisa budgetar, kanske du vill skapa en arbetsbok med blad som innehåller samma kolumnrubriker, radrubriker och formler. Det finns ett sätt att göra detta: genom att skapa ett blad och sedan kopiera det.

Aspose.Cells for Node.js via C++ stödjer kopiering och flytt av kalkylblad inom eller mellan arbetsböcker. Kalkylblad, komplett med data, formatering, tabeller, matriser, diagram, bilder och andra objekt, kopieras med högsta precision.

{{% /alert %}}

## **Flytta eller Kopiera Blad med Microsoft Excel**

Följande steg är inblandade för att kopiera och flytta arksidor inom eller mellan arbetsböcker i Microsoft Excel.

1. För att flytta eller kopiera blad till en annan arbetsbok, öppna arbetsboken som kommer ta emot bladen.
1. Byt till arbetsboken som innehåller bladen du vill flytta eller kopiera, och välj sedan bladen.
1. På **Redigera**-menyn klickar du på **Flytta eller Kopiera Blad**.
1. I dialogrutan **Till bok** klicka på arbetsboken som ska ta emot sidorna.
1. För att flytta eller kopiera de valda sidorna till en ny arbetsbok, klicka på **Ny bok**.
1. I rutan **Innan blad** klickar du på det blad innan vilket du vill infoga de flyttade eller kopierade bladen.
1. För att kopiera bladen istället för att flytta dem, markera kryssrutan **Skapa en kopia**.

### **Kopiera kalkylblad inom en arbetsbok med Aspose.Cells for Node.js via C++**

Aspose.Cells tillhandahåller en överbelastad metod, [**Aspose.Cells.WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#addCopy-number-), som används för att lägga till ett kalkylblad i samlingen och kopiera data från ett befintligt kalkylblad. En version av metoden tar indexet för källkalkylbladet som parameter. Den andra versionen tar namnet på källkalkylbladet.

Det följande exemplet visar hur man kopierar ett befintligt kalkylblad inom en arbetsbok.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xls");

// Open an existing Excel file.
const wb = new AsposeCells.Workbook(inputPath);

// Create a Worksheets object with reference to
// the sheets of the Workbook.
const sheets = wb.getWorksheets();

// Copy data to a new sheet from an existing
// sheet within the Workbook.
sheets.addCopy("Sheet1");

// Save the Excel file.
wb.save(path.join(dataDir, "CopyWithinWorkbook_out.xls"));
```

### **Kopiera Kalkylblad mellan Arbetsböcker**

Aspose.Cells tillhandahåller en metod, [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#copy-worksheet-), som används för att kopiera data och formatering från ett käl kalkylblad till ett annat kalkylblad inom eller mellan arbetsböcker. Metoden tar objekten för käl kalkylbladet som parameter.

Det följande exemplet visar hur man kopierar ett kalkylblad från en arbetsbok till en annan arbetsbok.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xls");

// Create a Workbook.
// Open a file into the first book.
const excelWorkbook0 = new AsposeCells.Workbook(inputPath);

// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook();

// Copy the first sheet of the first book into second book.
excelWorkbook1.getWorksheets().get(0).copy(excelWorkbook0.getWorksheets().get(0));

// Save the file.
excelWorkbook1.save(path.join(dataDir, "CopyWorksheetsBetweenWorkbooks_out.xls"));
```

Det följande exemplet visar hur man kopierar ett kalkylblad från en arbetsbok till en annan.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook.
const excelWorkbook0 = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const ws0 = excelWorkbook0.getWorksheets().get(0);

// Put some data into header rows (A1:A4)
for (let i = 0; i < 5; i++) {
ws0.getCells().get(i, 0).putValue(`Header Row ${i}`);
}

// Put some detail data (A5:A999)
for (let i = 5; i < 1000; i++) {
ws0.getCells().get(i, 0).putValue(`Detail Row ${i}`);
}

// Define a pagesetup object based on the first worksheet.
const pagesetup = ws0.getPageSetup();

// The first five rows are repeated in each page...
// It can be seen in print preview.
pagesetup.setPrintTitleRows("$1:$5");

// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const ws1 = excelWorkbook1.getWorksheets().get(0);

// Name the worksheet.
ws1.setName("MySheet");

// Copy data from the first worksheet of the first workbook into the
// first worksheet of the second workbook.
ws1.copy(ws0);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "CopyWorksheetFromWorkbookToOther_out.xls"));
```

### **Flytta Kalkylblad inom en Arbetsbok**

Aspose.Cells tillhandahåller en metod [**Aspose.Cells.Worksheet.moveTo()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#moveto-number-) som används för att flytta ett kalkylblad till annan plats i samma kalkblad. Metoden tar målkalkylbladets index som parameter.

Det följande exemplet visar hur man flyttar ett kalkylblad till en annan plats inom arbetsboken.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "sample1.xlsx");

// Open an existing excel file.
const wb = new AsposeCells.Workbook(inputPath);

// Create a Worksheets object with reference to the sheets of the Workbook.
const sheets = wb.getWorksheets();

// Get the first worksheet.
const worksheet = sheets.get(0);

// Move the first sheet to the third position in the workbook.
worksheet.moveTo(2);

// Save the excel file.
wb.save(path.join(dataDir, "MoveWorksheet_out.xls"));
```
