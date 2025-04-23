---
title: Hantera intervall med Node.js via C++
linktitle: Områden
type: docs
weight: 105
url: /sv/nodejs-cpp/managing-ranges/
description: Lär dig att hantera intervall i Excel med Aspose.Cells for Node.js via C++. Skapa intervall, ställ in värden, stilar och utför olika operationer.
---

## **Introduktion**

I Excel kan du välja flera celler med hjälp av ett musklick; det valda området kallas "Range".

Till exempel kan du klicka i cell "A1" i Excel och dra till cell "C4". Det rektangulära området du valt kan också enkelt skapas som ett objekt med hjälp av Aspose.Cells for Node.js via C++.

Så här skapar du ett område, sätter ett värde, tilldelar en stil och utför fler operationer på "Range"-objektet.

## **Hantera intervall med Aspose.Cells for Node.js via C++**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) som representerar en Microsoft Excel-fil. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-klassen innehåller en [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-samling som möjliggör åtkomst till varje kalkylblad i en Excel-fil. Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassen tillhandahåller en [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)-samling.

### **Skapa område**

När du vill skapa ett rektangulärt område som sträcker sig över A1:C4 kan du använda följande kod:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const range = cells.createRange("A1:C4");
```

### **Sätt värde i cellerna i området**

Säg att du har ett område med celler som sträcker sig över A1:C4. Matrisen gör 4 * 3 = 12 celler. De individuella områdscellerna är arrangerade sekventiellt: Område[0,0], Område[0,1], Område[0,2], Område[1,0], Område[1,1], Område[1,2], Område[2,0], Område[2,1], Område[2,2], Område[3,0], Område[3,1], Område[3,2].

Följande exempel visar hur man anger värden i cellerna i området.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "RangeValueTest.xlsx");

// Create a Workbook
const workbook = new AsposeCells.Workbook();
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const range = cells.createRange("A1:C4");
// Put value
range.get(0, 0).setValue("A1");
range.get(0, 1).setValue("B1");
range.get(0, 2).setValue("C1");
range.get(3, 0).setValue("A4");
range.get(3, 1).setValue("B4");
range.get(3, 2).setValue("C4");
// Save the Workbook
workbook.save(filePath);
```

### **Ställ in stil på cellerna i området**

Följande exempel visar hur man sätter stil på cellerna i intervallet.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Creates a Workbook
const workbook = new AsposeCells.Workbook();
// Gets Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Creates Range
const range = cells.createRange("A1:C4");
// Puts value
range.get(0, 0).setValue("A1");
range.get(3, 2).setValue("C4");
// Sets Style
let style00 = workbook.createStyle();
style00.setPattern(AsposeCells.BackgroundType.Solid);
style00.setForegroundColor(new AsposeCells.Color(255, 0, 0)); // Red
range.get(0, 0).setStyle(style00);
let style32 = workbook.createStyle();
style32.setPattern(AsposeCells.BackgroundType.HorizontalStripe);
style32.setForegroundColor(new AsposeCells.Color(0, 255, 0)); // Green
range.get(3, 2).setStyle(style32);
// Saves the Workbook
workbook.save("RangeStyleTest.xlsx");
```

### **Hämta aktuellt område av området**

CurrentRegion är en egenskap som returnerar ett områdesobjekt som representerar det aktuella området. 

Det aktuella området är ett område som begränsas av en kombination av tomma rader och tomma kolumner. Endast läsbar.

I Excel kan du få området CurrentRegion genom:
1. Välj ett område (range1) med musen.
2. Klicka på "Hem - Redigering - Sök & välj - Gå till special - Nuvarande område", eller använd "Ctrl+Shift+*", du kommer att se att Excel automatiskt hjälper dig att välja ett område (range2). Nu har du gjort det, range2 är Nuvarande område av range1.

Var god ladda ner följande testfil, öppna den i Excel, använd musen för att markera ett område "A1:D7", klicka sedan på "Ctrl+Shift+*", du kommer att se området "A1:C3" markerat.

[current_region.xlsx](current_region.xlsx)

Nu, vänligen kör följande exempel för att se hur det fungerar i Aspose.Cells:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "current_region.xlsx");
// Create a Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const src = cells.createRange("A1:D7");
// Get CurrentRegion
const A1C3 = src.getCurrentRegion();
```


## **Fortsatta ämnen**
- [Autofyllt område i Excel-fil](/cells/sv/nodejs-cpp/autofill-ranges/)
- [Kopiera områden i Excel](/cells/sv/nodejs-cpp/copy-ranges-of-Excel/)
- [Kopiera områdesdata endast](/cells/sv/nodejs-cpp/copy-range-data-only/)
- [Kopiera områdesdata med stil](/cells/sv/nodejs-cpp/copy-range-data-with-style/)
- [Kopiera områdesstil endast](/cells/sv/nodejs-cpp/copy-range-style-only/)
- [Skapa unionsspann](/cells/sv/nodejs-cpp/create-union-range/)
- [Klipp och klistra område](/cells/sv/nodejs-cpp/cut-and-paste-cells/)
- [Radera områden](/cells/sv/nodejs-cpp/delete-ranges-from-Excel/)
- [Få adresscellsantal offset hela kolumnen och hela raden för området](/cells/sv/nodejs-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Infoga områden](/cells/sv/nodejs-cpp/insert-ranges-to-Excel/)
- [Sammanfoga eller dela upp cellområde](/cells/sv/nodejs-cpp/merge-or-unmerge-range-of-cells/)
- [Flytta cellområde i ett kalkylblad](/cells/sv/nodejs-cpp/move-range-of-cells-in-a-worksheet/)
- [Skapa arbetsbok och arbetsbladsspecifika namngivna områden](/cells/sv/nodejs-cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [Sök och ersätt data i ett område](/cells/sv/nodejs-cpp/search-and-replace-data-in-a-range/)
