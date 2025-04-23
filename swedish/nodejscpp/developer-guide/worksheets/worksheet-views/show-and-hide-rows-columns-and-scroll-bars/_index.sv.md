---  
title: Visa och Dölj Rader, Kolumner och Rullningsfält med Node.js via C++  
linktitle: Visa och Dölja rader, Kolumner och Rullningslistor  
type: docs  
weight: 20  
url: /sv/nodejs-cpp/show-and-hide-rows-columns-and-scroll-bars/  
description: Denna artikel visar hur man programmatiskt visar och döljer Excel arksbladets rader och kolumner med Node.js via C++. Kontrollera synligheten för rullningsfält och dölja flera rader och kolumner effektivt.  
---  

{{% alert color="primary" %}}  
Aspose.Cells tillhandahåller sätt att kontrollera synligheten av rader, kolumner och rullningslistor på ett kalkylblad.  
{{% /alert %}}  

## **Visa och göm rader och kolumner**  

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) klassen innehåller en [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) samling som tillåter utvecklare att komma åt varje arbetsblad i Excel-filen. Ett arbetsblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen tillhandahåller en [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) samling som representerar alla celler i arbetsbladet. [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samlingen innehåller flera metoder för att hantera rader eller kolumner i ett arbetsblad. Några av dessa diskuteras nedan.  

### **Visa Rader och Kolumner**  

Utvecklare kan visa vilken dold rad eller kolumn som helst genom att anropa metoderna [**unhideRow(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRow-number-number-) och [**unhideColumn(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumn-number-number-) av [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samlingen respektive. Båda metoder tar två parametrar:  

- **Rad- eller kolumnindex** - index för en rad eller kolumn som används för att visa den specifika raden eller kolumnen.  
- **Radhöjd eller kolumnbredd** - radhöjden eller kolumnbredden tilldelad till raden eller kolumnen efter att ha visats.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
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
När du gör en dold kolumn synlig, om du behöver återställa den till den tidigare tilldelade eller ursprungliga bredden, vänligen gör kolumnen ovisbar med negativ bredd. Till exempel: worksheet.Cells.unhideColumn(5, -1)  
{{% /alert %}}  

### **Dölj Rader och Kolumner**  

Utvecklare kan dölja en rad eller kolumn genom att anropa metoderna [**hideRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRow-number-) och [**hideColumn(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumn-number-) av [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samlingen respektive. Båda metoder tar rad- och kolumnindex som parameter för att dölja den specifika raden eller kolumnen.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

const fileBuffer = fs.readFileSync(filePath);

const workbook = new AsposeCells.Workbook(fileBuffer);

const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().hideRow(2);

worksheet.getCells().hideColumn(1);

workbook.save(path.join(dataDir, "output.out.xls"));
```  

{{% alert color="primary" %}}  
Det är också möjligt att dölja en rad eller kolumn genom att ställa in radhöjden eller kolumnbredden till 0 respektive.  
{{% /alert %}}  

### **Dölj Flera Rader och Kolumner**  

Utvecklare kan dölja flera rader eller kolumner samtidigt genom att anropa metoderna [**hideRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRows-number-number-) och [**hideColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumns-number-number-) av [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-samlingen respektive. Båda metoder tar startrad- eller startkolumnindex och antalet rader eller kolumner som ska döljas som parametrar.  

```javascript
const fs = require('fs');
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding 3, 4 and 5 rows in the worksheet
worksheet.getCells().hideRows(2, 3);

// Hiding 2 and 3 columns in the worksheet
worksheet.getCells().hideColumns(1, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "outputxls"));

// No explicit close needed for file stream as we're working with in-memory data
```  

## **Visa och dölj bildrullningsfält**  

Rullningslistor används för att navigera bland innehållet i en fil. Vanligtvis finns det två typer av rullningslistor:  

- Vertikala bildrullningsfält  
- Horisontella bildrullningsfält  

Microsoft Excel tillhandahåller också horisontella och vertikala bildrullningsfält så att användare kan bläddra genom arbetsbladets innehåll. Med Aspose.Cells kan utvecklare kontrollera synligheten av båda typer av bildrullningsfält i Excelfiler.  

### **Kontrollera Synligheten för Rullningslistor**  

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), som representerar en Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera en Excel-fil. För att kontrollera synligheten för rullningsfält, använd egenskaperna [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) och [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--). [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) och [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) är booleska egenskaper, vilket betyder att dessa egenskaper endast kan lagra **true** eller **false** värden.  

#### **Gör bildrullningsfält synliga**  

Gör rullningsfält synliga genom att ställa in [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) -klassens egenskaper [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) eller [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) till **true**.  

#### **Dölja bildrullningsfält**  

Dölj rullningsfält genom att ställa in egenskaperna [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) -klassens [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) eller [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) till **false**.  

**Exempelkod**  

Nedan finns en komplett kod som öppnar en Excel-fil, book1.xls, gömmer båda rullningsfälten och sparar sedan den modifierade filen som output.xls.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Hiding the vertical scroll bar of the Excel file
workbook.getSettings().setIsVScrollBarVisible(false);

// Hiding the horizontal scroll bar of the Excel file
workbook.getSettings().setIsHScrollBarVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

