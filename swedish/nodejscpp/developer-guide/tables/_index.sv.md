---
title: Skapa och hantera tabeller i Microsoft Excel filer med Node.js via C++
linktitle: Tabeller
type: docs
weight: 150
url: /sv/nodejs-cpp/create-and-format-table/
description: Infoga, ändra storlek, redigera, ta bort och formatera tabeller i Excel filer med Aspose.Cells for Node.js via C++.
---

## **Skapa tabell**

En av fördelarna med kalkylblad är att de tillåter dig att skapa olika typer av listor, till exempel telefonlistor, uppgiftslistor, listor över transaktioner, tillgångar eller skulder. Flera användare kan samarbeta för att använda, skapa och underhålla olika listor.

Aspose.Cells stödjer skapande och hantering av listor.

### **Fördelar med en List-objekt**

Det finns ganska många fördelar när du konverterar en lista med data till ett faktiskt List-objekt

- Nya rader och kolumner inkluderas automatiskt.
- En totalrad längst ner i din lista kan enkelt läggas till för att visa SUMMA, MEDELVÄRDE, ANTAL, osv.
- Kolumner som läggs till till höger inkorporeras automatiskt i listobjektet.
- Diagram baserade på rader och kolumner kommer att utökas automatiskt.
- Namngivna intervall tilldelade rader och kolumner kommer att utökas automatiskt.
- Listan är skyddad från oavsiktlig rad- och kolumnradering.

### **Skapa ett List-objekt med hjälp av Microsoft Excel**

- Välj dataintervall för att skapa ett List-objekt
- Detta visar skapa List-dialogrutan.
- Implementera List-objektet för data och ange totalsraden (Välj **Data**, sedan **Lista**, och därefter **Totalrad**).

### **Använda Aspose.Cells API**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) innehåller en [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) -samling som möjliggör åtkomst till varje arbetsblad i en Excel-fil.

Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen erbjuder ett brett utbud av egenskaper och metoder för att hantera ett kalkylblad. För att skapa ett [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) i ett kalkylblad, använd [**getListObjects()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getListObjects--)-samlingsegenskapen av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. Varje [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) är i själva verket ett objekt av [**ListObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/)-klassen, som vidare tillhandahåller [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/#add-number-number-number-number-boolean-)-metoden för att lägga till ett List-objekt och ange ett cellområde för listan.

Enligt det angivna cellområdet skapas List-objektet av Aspose.Cells. Använd attribut (till exempel [**getShowTotals()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getShowTotals--), [**getListColumns()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getListColumns--) osv.) för [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/)-klassen för att styra listan.

I exemplet nedan har vi skapat samma [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) med Aspose.Cells API som vi skapade med Microsoft Excel i föregående avsnitt.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Create a Workbook object.
// Open a template excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the List objects collection in the first worksheet.
const listObjects = workbook.getWorksheets().get(0).getListObjects();

// Add a List based on the data source range with headers on.
listObjects.add(1, 1, 7, 5, true);

// Show the total row for the List.
listObjects.get(0).setShowTotals(true);

// Calculate the total of the last (5th) list column.
listObjects.get(0).getListColumns().get(4).setTotalsCalculation(AsposeCells.TotalsCalculation.Sum);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

## **Formatera en tabell**

För att hantera och analysera en grupp relaterade data är det möjligt att göra om ett cellområde till ett listobjekt (även känt som en Exceltabell). En tabell är en serie rader och kolumner som innehåller relaterade data som hanteras oberoende från data i andra rader och kolumner. Som standard har varje kolumn i tabellen filtrering aktiverat i rubrikraden så att du snabbt kan filtrera eller sortera dina listobjektdata. Du kan lägga till en totalrad (en specialrad i en lista som ger ett urval av aggregeringsfunktioner som är användbara för att arbeta med numeriska data) till listobjektet som ger en rullista med aggregeringsfunktioner för varje cell i totalraden. Aspose.Cells tillhandahåller alternativ för att skapa och hantera listor (eller tabeller).

### **Formatera ett Listobjekt**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) innehåller en [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) -samling som möjliggör åtkomst till varje arbetsblad i en Excel-fil.

Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen erbjuder ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att skapa ett [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) i ett kalkylblad, använd [**getListObjects()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getListObjects--)-samlingsegenskapen av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. Varje [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) är i själva verket ett objekt av [**ListObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/)-klassen, som vidare tillhandahåller [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/#add-number-number-number-number-boolean-)-metoden för att lägga till ett List-objekt och specificera det cellområde det ska omfatta. Enligt det angivna cellområdet skapas ett [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) i kalkylbladet av Aspose.Cells. Använd attribut (till exempel [**TableStyleType**](https://reference.aspose.com/cells/nodejs-cpp/tablestyletype/)) för [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/)-klassen för att formatera tabellen efter dina behov.

Nedan följer ett exempel som lägger till exempeldata i ett kalkylblad, lägger till ett [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) och tillämpar standardstilar. [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) stilar stöds av Microsoft Excel 2007/2010.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook.
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the default(first) worksheet
const sheet = workbook.getWorksheets().get(0);

// Obtaining Worksheet's cells collection
const cells = sheet.getCells();

// Setting the value to the cells
cells.get(1, 1).putValue("Employee");
cells.get(1, 2).putValue("Quarter");
cells.get(1, 3).putValue("Product");
cells.get(1, 4).putValue("Continent");
cells.get(1, 5).putValue("Country");
cells.get(1, 6).putValue("Sale");

cells.get(2, 1).putValue("David");
cells.get(3, 1).putValue("David");
cells.get(4, 1).putValue("David");
cells.get(5, 1).putValue("David");
cells.get(6, 1).putValue("James");
cells.get(7, 1).putValue("James");
cells.get(8, 1).putValue("James");
cells.get(9, 1).putValue("James");
cells.get(10, 1).putValue("James");
cells.get(11, 1).putValue("Miya");
cells.get(12, 1).putValue("Miya");
cells.get(13, 1).putValue("Miya");
cells.get(14, 1).putValue("Miya");
cells.get(15, 1).putValue("Miya");
cells.get(2, 2).putValue(1);
cells.get(3, 2).putValue(2);
cells.get(4, 2).putValue(3);
cells.get(5, 2).putValue(4);
cells.get(6, 2).putValue(1);
cells.get(7, 2).putValue(2);
cells.get(8, 2).putValue(3);
cells.get(9, 2).putValue(4);
cells.get(10, 2).putValue(4);
cells.get(11, 2).putValue(1);
cells.get(12, 2).putValue(1);
cells.get(13, 2).putValue(2);
cells.get(14, 2).putValue(2);
cells.get(15, 2).putValue(2);

cells.get(2, 3).putValue("Maxilaku");
cells.get(3, 3).putValue("Maxilaku");
cells.get(4, 3).putValue("Chai");
cells.get(5, 3).putValue("Maxilaku");
cells.get(6, 3).putValue("Chang");
cells.get(7, 3).putValue("Chang");
cells.get(8, 3).putValue("Chang");
cells.get(9, 3).putValue("Chang");
cells.get(10, 3).putValue("Chang");
cells.get(11, 3).putValue("Geitost");
cells.get(12, 3).putValue("Chai");
cells.get(13, 3).putValue("Geitost");
cells.get(14, 3).putValue("Geitost");
cells.get(15, 3).putValue("Geitost");

cells.get(2, 4).putValue("Asia");
cells.get(3, 4).putValue("Asia");
cells.get(4, 4).putValue("Asia");
cells.get(5, 4).putValue("Asia");
cells.get(6, 4).putValue("Europe");
cells.get(7, 4).putValue("Europe");
cells.get(8, 4).putValue("Europe");
cells.get(9, 4).putValue("Europe");
cells.get(10, 4).putValue("Europe");
cells.get(11, 4).putValue("America");
cells.get(12, 4).putValue("America");
cells.get(13, 4).putValue("America");
cells.get(14, 4).putValue("America");
cells.get(15, 4).putValue("America");

cells.get(2, 5).putValue("China");
cells.get(3, 5).putValue("India");
cells.get(4, 5).putValue("Korea");
cells.get(5, 5).putValue("India");
cells.get(6, 5).putValue("France");
cells.get(7, 5).putValue("France");
cells.get(8, 5).putValue("Germany");
cells.get(9, 5).putValue("Italy");
cells.get(10, 5).putValue("France");
cells.get(11, 5).putValue("U.S.");
cells.get(12, 5).putValue("U.S.");
cells.get(13, 5).putValue("Brazil");
cells.get(14, 5).putValue("U.S.");
cells.get(15, 5).putValue("U.S.");

cells.get(2, 6).putValue(2000);
cells.get(3, 6).putValue(500);
cells.get(4, 6).putValue(1200);
cells.get(5, 6).putValue(1500);
cells.get(6, 6).putValue(500);
cells.get(7, 6).putValue(1500);
cells.get(8, 6).putValue(800);
cells.get(9, 6).putValue(900);
cells.get(10, 6).putValue(500);
cells.get(11, 6).putValue(1600);
cells.get(12, 6).putValue(600);
cells.get(13, 6).putValue(2000);
cells.get(14, 6).putValue(500);
cells.get(15, 6).putValue(900);

// Adding a new List Object to the worksheet
const index = sheet.getListObjects().add("A1", "F15", true);

const listObject = sheet.getListObjects().get(index);

// Adding Default Style to the table
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium10);

// Show Total
listObject.setShowTotals(true);

// Set the Quarter field's calculation type
listObject.getListColumns().get(1).setTotalsCalculation(AsposeCells.TotalsCalculation.Count);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```

## **Fortsatta ämnen**
- [Konvertera tabell till ODS](/cells/sv/nodejs-cpp/convert-table-to-ods/)
- [Hitta frågetabeller och lista objekt relaterade till externa dataanslutningar](/cells/sv/nodejs-cpp/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Läs och skriv tabell med datakälla för frågetabell](/cells/sv/nodejs-cpp/read-and-write-table-with-query-table-data-source/)
- [Ange kommentaren för tabell eller listobjekt inne i kalkylbladet](/cells/sv/nodejs-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tabeller och områden](/cells/sv/nodejs-cpp/tables-and-ranges/)

