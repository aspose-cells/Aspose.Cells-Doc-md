---  
title: Hantera kalkylblad i Microsoft Excel filer med Node.js via C++  
linktitle: Arbetsblad  
type: docs  
weight: 90  
url: /sv/nodejs-cpp/manage-worksheets/  
description: Lägg till, ta bort och aktivera kalkylblad med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Utvecklare kan enkelt skapa och hantera kalkylblad i Microsoft Excel-filer programmatiskt med hjälp av Aspose.Cells flexibla API. Denna ämne beskriver tillvägagångssätt för att lägga till och ta bort kalkylblad i Microsoft Excel-filer.  
{{% /alert %}}  

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) som representerar en Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) innehåller en [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-samling som möjliggör åtkomst till varje kalkylblad i Excel-filen.  

Ett kalkylblad uttrycks av klassen [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) erbjuder ett brett utbud av egenskaper och metoder för att hantera kalkylblad.  

## **Lägga till kalkylblad i en ny Excelfil**  

För att skapa en ny Excel-fil programmatiskt:  

1. Skapa ett objekt av klassen [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).  
1. Anropa metoden [**WorksheetCollection.add(SheetType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#add-sheettype-) för klassen [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection). Ett tomt kalkylblad läggs till i Excel-filen automatiskt. Det kan refereras genom att passera det nya kalkylbladets index till [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-samlingen.  
1. Få en referens till ett kalkylblad.  
1. Arbeta med kalkylbladen.  
1. Spara den nya Excel-filen med de nya kalkylbladen genom att anropa metoden [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) för klassen [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const i = workbook.getWorksheets().getCount();
workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Setting the name of the newly added worksheet
worksheet.setName("My Worksheet");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Lägga till kalkylblad i ett designerkalkylblad**  

Processen för att lägga till kalkylblad i ett designad kalkylark är densamma som att lägga till ett nytt kalkylblad, förutsatt att Excel-filen redan finns och ska öppnas innan kalkylblad läggs till. En designer-kalkylark kan öppnas med klassen [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(inputPath);

// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Adding a new worksheet to the Workbook object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Setting the name of the newly added worksheet
worksheet.setName("My Worksheet");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

## **Tillgång till kalkylblad med hjälp av kalkylbladsnamn**  

Få tillgång till vilket kalkylblad som helst genom att ange dess namn eller index.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(inputPath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing a worksheet using its sheet name
const worksheet = workbook.getWorksheets().get("Sheet1");
const cell = worksheet.getCells().get("A1");
console.log(cell.getValue());
```  

## **Ta bort kalkylblad med hjälp av kalkylbladsnamn**  

För att ta bort kalkylblad från en fil, anropa metoden [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) för klassen [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection). Passa kalkylbladets namn till metoden [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) för att ta bort ett specifikt kalkylblad.  

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

// Removing a worksheet using its sheet name
workbook.getWorksheets().removeAt("Sheet1");

// Save workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Ta bort kalkylblad med hjälp av kalkylbladsindex**  

Att ta bort kalkylblad efter namn fungerar bra när namnet på kalkylbladet är känt. Om du inte känner till kalkylbladets namn, använd en överbelastad version av metoden [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) som tar kalkylbladets index istället för dess namn.  

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

// Removing a worksheet using its sheet index
workbook.getWorksheets().removeAt(0);

// Save workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Aktivera kalkylblad och gör en aktiv cell i kalkylbladet**  

Ibland behöver du ett specifikt arbetsblad att vara aktivt och visas när en användare öppnar en Microsoft Excel-fil i Excel. På samma sätt kan du vilja aktivera en specifik cell och ställa in rullningslisterna för att visa den aktiva cellen. Aspose.Cells kan utföra alla dessa uppgifter.  

Ett **aktivt kalkylblad** är ett kalkylblad du arbetar med: det aktiva kalkylbladets namn på fliken är fetstil som standard.  

En **aktiv cell** är en markerad cell, den cell där data matas in när du börjar skriva. Endast en cell är aktiv åt gången. Den aktiva cellen är markerad med en tjock kantlinje.  

### **Aktivera blad och göra en cell aktiv**  

Aspose.Cells tillhandahåller specifika API-anrop för att aktivera ett blad och en cell. Till exempel är [**WorksheetCollection.getActiveSheetIndex()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getActiveSheetIndex--)-egenskapen användbar för att ställa in det aktiva bladet i en arbetsbok. På samma sätt används [**Worksheet.getActiveCell()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getActiveCell--)-egenskapen för att ställa in och hämta en aktiv cell i arbetsbladet.  

För att säkerställa att de horisontella eller vertikala rullningslisterna är vid den rad- och kolumnindexposition du vill visa specifika data, använd egendoms [**Worksheet.getFirstVisibleRow()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFirstVisibleRow--) och [**Worksheet.getFirstVisibleColumn()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFirstVisibleColumn--).  

Följande exempel visar hur du aktiverar ett kalkylblad och gör en cell aktiv i det. I den genererade utdatan kommer rullningsfälten att skrollas för att göra den 2: a raden och den 2: a kolumnen som deras första synliga rad och kolumn.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Add a worksheet if collection is empty
const worksheets = workbook.getWorksheets();
if (worksheets.getCount() === 0) {
worksheets.add();
}

// Get the first worksheet in the workbook.
const worksheet1 = worksheets.get(0);

// Get the cells in the worksheet.
const cells = worksheet1.getCells();

// Input data into B2 cell.
cells.get(1, 1).putValue("Hello World!");

// Set the first sheet as an active sheet.
workbook.getWorksheets().setActiveSheetIndex(0);

// Set B2 cell as an active cell in the worksheet.
worksheet1.setActiveCell("B2");

// Set the B column as the first visible column in the worksheet.
worksheet1.setFirstVisibleColumn(1);

// Set the 2nd row as the first visible row in the worksheet.
worksheet1.setFirstVisibleRow(1);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```  

## **Fortsatta ämnen**  
- [Kopiera och flytta arbetsblad](/cells/sv/nodejs-cpp/copying-and-moving-worksheets/)  
- [Räkna antalet celler i kalkylbladet](/cells/sv/nodejs-cpp/count-number-of-cells-in-the-worksheet/)  
- [Upptäcka tomma kalkylblad](/cells/sv/nodejs-cpp/detecting-empty-worksheets/)  
- [Ta reda på om kalkylbladet är Dialog sheet](/cells/sv/nodejs-cpp/find-if-the-worksheet-is-dialog-sheet/)  
- [Få arbetsbladets unika id](/cells/sv/nodejs-cpp/get-worksheet-unique-id/)  
- [Skapa, manipulera eller ta bort scenarier från kalkylblad](/cells/sv/nodejs-cpp/create-manipulate-or-remove-scenarios-from-worksheets/)  
- [Hantera sidbrytningar](/cells/sv/nodejs-cpp/managing-page-breaks/)  
- [Sidlayoutfunktioner](/cells/sv/nodejs-cpp/page-setup-features/)   
- [Använd Sheet.SheetId-egenskapen i OpenXml med hjälp av Aspose.Cells](/cells/sv/nodejs-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)  
- [Kalkylbladsvyer](/cells/sv/nodejs-cpp/worksheet-views/)  


