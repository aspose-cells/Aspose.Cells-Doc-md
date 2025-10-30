---  
title: Kopiera rader och kolumner med Node.js via C++  
linktitle: Kopiera rader och kolumner  
type: docs  
weight: 40  
url: /sv/nodejs-cpp/copying-rows-and-columns/  
description: Den här artikeln visar hur man kopierar rader och kolumner via Aspose.Cells for Node.js via C++ API et.  
keywords: Node.js via C++, Hur man kopierar rader och kolumner, Kopiera rader i Node.js, Kopiera kolumner med Node.js, Hur man klistrar in rader och kolumner med Aspose.Cells for Node.js via C++, Klistra in flera rader och kolumner, Hur man kopierar och klistrar in en enskild rad eller kolumn.  
---  

## **Introduktion**  

Ibland behöver du kopiera rader och kolumner i en arbetsbok utan att kopiera hela arbetsboken. Med Aspose.Cells är det möjligt att kopiera rader och kolumner inom eller mellan arbetsböcker.  
När en rad (eller kolumn) kopieras, kopieras också den data som finns i den, inklusive formler - med uppdaterade referenser - och värden, kommentarer, formatering, dolda celler, bilder och andra ritobjekt.  

## **Hur man kopierar rader och kolumner med Microsoft Excel**  

1. Markera raden eller kolumnen som du vill kopiera.  
1. För att kopiera rader eller kolumner, klicka på **Kopiera** på **Standard** verktygsfältet, eller tryck på **CTRL**+**C**.  
1. Välj en rad eller en kolumn nedanför eller till höger om där du vill kopiera ditt val.  
1. När du kopierar rader eller kolumner, klicka på **Kopierade celler** på menyn **Infoga**.  

{{% alert color="primary" %}}  
Om du klickar på **Klistra in** på **Standard** verktygsfältet eller trycker på **CTRL**+**V** istället för att klicka på en kommando i **Infoga** menyn, ersätts eventuella innehåll i destinationens celler.  
{{% /alert %}}  

## **Hur man klistrar in rader och kolumner med hjälp av klistra in-alternativ med Microsoft Excel**  

1. Välj cellerna som innehåller data eller andra attribut som du vill kopiera.  
1. På fliken Hem, klicka på **Kopiera**.  
1. Klicka på den första cellen i det område där du vill **klistra in** det du kopierade.  
1. På fliken Hem, klicka på pilen bredvid **Klistra in**, och välj sedan **Klistra in** Special.  
1. Välj de **alternativ** du vill.  

## **Hur man kopierar rader och kolumner med Aspose.Cells for Node.js via C++**  

## **Hur man kopierar enskilda rader**  

Aspose.Cells tillhandahåller metoden [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) av [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-klassen. Den här metoden kopierar all typ av data, inklusive formler, värden, kommentarer, cellformat, dolda celler, bilder och andra ritobjekt från källraden till destinationsraden.  

[**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-)-metoden tar följande parametrar:  

- källekon,  
- källradens index, och  
- destinationsradens index.  

Använd denna metod för att kopiera en rad inom ett blad, eller till ett annat blad. [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-)-metoden fungerar på ett liknande sätt som Microsoft Excel. Så, till exempel, behöver du inte ange höjden på destinationsraden explicit, det värdet kopieras också.  

Nedan visas ett exempel på hur man kopierar en rad i ett kalkylblad. Det använder en mall Microsoft Excel-fil och kopierar den andra raden (med data, formatering, kommentarer, bilder och så vidare) och klistrar in den på den 12:e raden i samma kalkylblad.  

Du kan hoppa över steget som hämtar kälrradens höjd med [**Cells.getRowHeight(number, boolean, CellsUnitType)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRowHeight-number-boolean-cellsunittype-)-metoden och sedan sätter höjden på destinationsraden med [**Cells.setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-)-metoden eftersom [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-)-metoden automatiskt tar hand om radens höjd.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing excel file.
const excelWorkbook1 = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Get the first worksheet in the workbook.
const wsTemplate = excelWorkbook1.getWorksheets().get(0);

// Copy the second row with data, formattings, images and drawing objects
// To the 16th row in the worksheet.
wsTemplate.getCells().copyRow(wsTemplate.getCells(), 1, 15);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  
Vid kopiering av rader är det viktigt att notera relaterade bilder, diagram eller andra ritobjekt eftersom detta är detsamma med Microsoft Excel:  

1. Om källradens index är 5, kopieras bilden, diagrammet osv. om den finns i de tre raderna (startindexet är 4 och slutindexet är 6).  
1. De befintliga bilderna, diagrammen osv. i destinationsraden kommer inte att tas bort.  
{{% /alert %}}  

## **Hur man kopierar flera rader**  

Du kan också kopiera flera rader till ett nytt destination medan du använder [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-)-metoden som tar ett ytterligare parameter av typen heltal för att ange antalet kälrrader som ska kopieras.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "aspose-sample.xlsx");

// Create an instance of Workbook class by loading the existing spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Get the cells collection of first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Copy the first 3 rows to 7th row
cells.copyRows(cells, 0, 6, 3);

// Save the result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

## **Hur man kopierar kolumner**  

Aspose.Cells tillhandahåller [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-)-metoden i [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-klassen, denna metod kopierar alla typer av data, inklusive formler - med uppdaterade referenser - samt värden, kommentarer, cellformat, dolda celler, bilder och andra ritobjekt från källekän i kolumnen till destinationskolumnen.  

[**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-)-metoden tar följande parametrar:  

- källekon,  
- källkolumnens index och  
- destinationskolumnens index.  

Använd [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-)-metoden för att kopiera en kolumn inom ett blad eller till ett annat blad.  

Detta exempel kopierar en kolumn från ett blad och klistrar in den i ett blad i en annan arbetsbok.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook(filePath);

// Get the first worksheet in the book.
const ws1 = excelWorkbook1.getWorksheets().get(0);

// Copy the first column from the first worksheet of the first workbook into
// The first worksheet of the second workbook.
ws1.getCells().copyColumn(ws1.getCells(), ws1.getCells().getColumns().get(0).getIndex(), ws1.getCells().getColumns().get(2).getIndex());

// Autofit the column.
ws1.autoFitColumn(2);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "output.xls"));
```  

## **Hur man kopierar flera kolumner**  

Liknande [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-)-metoden, ger API:erna Aspose.Cells också [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-)-metoden för att kopiera flera källekolumner till en ny plats.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an instance of Workbook class by loading the existing spreadsheet
const workbook = new AsposeCells.Workbook(path.join(dataDir, "aspose-sample.xlsx"));

// Get the first worksheet's cells collection
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

// Copy the first 3 columns to the 7th column
cells.copyColumns(cells, 0, 6, 3);

// Save the result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

## **Hur man klistrar in rader och kolumner med klistringsalternativ**  

Aspose.Cells tillhandahåller nu [**PasteOptions**](https://reference.aspose.com/cells/nodejs-cpp/pasteoptions/) medan man använder funktionerna [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) och [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-). Det gör det möjligt att ställa in lämpligt klistringsalternativ liknande Excel.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleChangeChartDataSource.xlsx"));

// Access the first sheet which contains chart
const source = workbook.getWorksheets().get(0);

// Add another sheet named DestSheet
const destination = workbook.getWorksheets().add("DestSheet");

// Set CopyOptions.ReferToDestinationSheet to true
const options = new AsposeCells.CopyOptions();
options.setReferToDestinationSheet(true);

// Set PasteOptions
const pasteOptions = new AsposeCells.PasteOptions();
pasteOptions.setPasteType(AsposeCells.PasteType.Values);
pasteOptions.setOnlyVisibleCells(true);

// Copy all the rows of source worksheet to destination worksheet which includes chart as well
// The chart data source will now refer to DestSheet
destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options, pasteOptions);

// Save workbook in xlsx format
workbook.save(path.join(outputDir, "outputChangeChartDataSource.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
