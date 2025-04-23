---  
title: Tabeller och områden med Node.js via C++  
linktitle: Tabeller och Intervall  
type: docs  
weight: 50  
url: /sv/nodejs-cpp/tables-and-ranges/  
---  

## **Introduktion**  

Ibland skapar du en tabell i Microsoft Excel och vill inte fortsätta arbeta med tabellfunktionaliteten den kommer med. Istället vill du ha något som ser ut som en tabell. För att behålla data i en tabell utan att förlora formateringen, konvertera tabellen till en vanlig datamängd.  
Aspose.Cells stöder denna funktion i Microsoft Excel för tabeller och listobjekt.  

## **Använda Microsoft Excel**  

Använd **Konvertera till område**-funktionen för att snabbt konvertera en tabell till en mängd utan att förlora formateringen. I Microsoft Excel 2007/2010:  

1. Klicka var som helst i tabellen för att se till att den aktiva cellen är i en tabellkolumn.  
1. På fliken **Utformning**, i gruppen **Verktyg**, klicka på **Konvertera till område**.  

## **Använda Aspose.Cells**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "table_ranges.xlsx");

// Open an existing file that contains a table/list object in it
const wb = new AsposeCells.Workbook(filePath);

// Convert the first table/list object (from the first worksheet) to normal range
wb.getWorksheets().get(0).getListObjects().get(0).convertToRange();

// Save the file
wb.save(path.join(dataDir, "output.xlsx"));
```  

{{% alert color="primary" %}}  

Tabellfunktionerna är inte längre tillgängliga efter att tabellen har konverterats till en mängd. Till exempel inkluderar radrubrikerna inte längre sorterings- och filterpilar, och strukturerade referenser (referenser som använder tabellnamn) som användes i formler omvandlas till vanliga cellreferenser.  

{{% /alert %}}  

## **Konvertera tabell till område med alternativ.**  

Aspose.Cells tillhandahåller ytterligare alternativ när du konverterar tabell till intervall genom klassen [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/). Klassen [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/) tillhandahåller egenskapen [**getLastRow()**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/#getLastRow--) som gör att du kan ange den sista indexet för tabellraden. Tabellformateringen behålls upp till det angivna radindexet och resten av formateringen tas bort.  

Den angivna provkoden nedan visar användningen av klassen [**TableToRangeOptions**](https://reference.aspose.com/cells/nodejs-cpp/tabletorangeoptions/).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "table_ranges.xlsx");
// Open an existing file that contains a table/list object in it
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.TableToRangeOptions();
options.setLastRow(5);

// Convert the first table/list object (from the first worksheet) to normal range
workbook.getWorksheets().get(0).getListObjects().get(0).convertToRange(options);

// Save the file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

