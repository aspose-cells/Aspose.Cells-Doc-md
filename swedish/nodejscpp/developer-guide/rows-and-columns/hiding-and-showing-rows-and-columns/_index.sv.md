---
title: Dölj och visa rader och kolumner med Node.js via C++
linktitle: Dölja och visa rader och kolumner
type: docs
weight: 60
url: /sv/nodejs-cpp/hiding-and-showing-rows-and-columns/
description: Lär dig hur du döljer och visar rader och kolumner i ett kalkylblad med Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Ibland är det meningsfullt att dölja vissa rader eller kolumner i en arbetsbok och sedan visa dem senare. Microsoft Excel tillhandahåller den här funktionen och så gör även Aspose.Cells.

{{% /alert %}}

## **Kontrollera synligheten av rader och kolumner**

Aspose.Cells for Node.js via C++ tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen innehåller en [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) som tillåter utvecklare att komma åt varje kalkylblad i Excel-filen. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen tillhandahåller en [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samling som representerar alla celler i kalkylbladet. [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingen ger flera metoder för att hantera rader eller kolumner i ett kalkylblad. Några av dessa diskuteras nedan.

### **Dölja rader och kolumner**

Utvecklare kan dölja en rad eller kolumn genom att anropa metoderna [**hideRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRow-number-) och [**hideColumn(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumn-number-) av [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingen respektive. Båda metoder tar rad- och kolumnindex som parameter för att dölja den specifika raden eller kolumnen.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fileBuffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with Uint8Array
const workbook = new AsposeCells.Workbook(new Uint8Array(fileBuffer));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the 3rd row of the worksheet
worksheet.getCells().hideRow(2);

// Hiding the 2nd column of the worksheet
worksheet.getCells().hideColumn(1);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

{{% alert color="primary" %}}

Det är också möjligt att dölja en rad eller kolumn genom att ställa in radhöjden eller kolumnbredden till 0 respektive.

{{% /alert %}}

### **Visa rader och kolumner**

Utvecklare kan visa vilken dold rad eller kolumn som helst genom att anropa metoderna [**unhideRow(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRow-number-number-) och [**unhideColumn(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumn-number-number-) av [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingen respektive. Båda metoder tar två parametrar:

- **Rad- eller kolumnindex** - index för en rad eller kolumn som används för att visa den specifika raden eller kolumnen.
- **Radhöjd eller kolumnbredd** - radhöjden eller kolumnbredden tilldelad till raden eller kolumnen efter att ha visats.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Read the Excel file into a Buffer (Uint8Array)
const fileBuffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with file buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unhiding the 3rd row and setting its height to 13.5
worksheet.getCells().unhideRow(2, 13.5);

// Unhiding the 2nd column and setting its width to 8.5
worksheet.getCells().unhideColumn(1, 8.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

{{% alert color="primary" %}}

När du gör en dold kolumn synlig, om du behöver återställa den till den tidigare tilldelade bredden eller till dess ursprungliga bredd, avmarkera kolumnen med en negativ bredd. Till exempel: worksheet.cells.unhideColumn(5, -1)

{{% /alert %}}

### **Dölja flera rader och kolumner**

Utvecklare kan dölja flera rader eller kolumner samtidigt genom att anropa metoderna [**hideRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRows-number-number-) och [**hideColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumns-number-number-) av [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samlingen respektive. Båda metoder tar startrad- eller startkolumnindex och antalet rader eller kolumner som ska döljas som parametrar.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fileStream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fileStream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding 3, 4, and 5 rows in the worksheet
worksheet.getCells().hideRows(2, 3);

// Hiding 2 and 3 columns in the worksheet
worksheet.getCells().hideColumns(1, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "outputxls"));
```

{{% alert color="primary" %}}

Det är också möjligt att använda [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) klassens [**unhideRows(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRows-number-number-number-) och [**unhideColumns(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumns-number-number-number-) metoder för att göra flera rader och kolumner synliga.

{{% /alert %}}
