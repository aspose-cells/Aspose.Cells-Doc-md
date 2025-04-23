---
title: Dela skärm i Excel ark med Node.js via C++
linktitle: Dela skärm
type: docs
weight: 190
url: /sv/nodejs-cpp/how-to-split-screen-of-excel-worksheet
description: I denna artikel lär du dig hur man visar vissa rader och/eller kolumner i separata fönster genom att dela arbetsbladet i två eller fyra delar programatiskt med Node.js C++ tillägget.
keywords: Frysta översta rader, Frysta översta raden.
---

## **Introduktion**

I denna artikel kommer vi att lära oss hur man visar vissa rader och/eller kolumner i separata paneler genom att dela arket i två eller fyra delar. När man arbetar med stora datamängder behöver vi se några delar av samma ark samtidigt för att jämföra olika underuppsättningar av data. Funktionerna för att dela skärmen kan möta dina behov.

## **Hur man delar skärmen i Excel**
För att dela upp ett arbetsblad i två eller fyra delar, gör följande:

1. Välj rad/kolumn/cell innan vilken du vill placera uppdelningen.
2. På fliken Visa, i gruppen Fönster, klicka på knappen Dela.

**![Dela skärm](Split-Screen.png)**

## **Dela arbetsblad vertikalt på kolumner**

För att separera två områden av kalkylarket vertikalt, välj kolumnen till höger om den kolumn där du vill att uppdelningen ska visas och klicka på Split-knappen i Excel.

Det är enkelt att dela arbetsblad vertikalt på kolumner programmässigt med Aspose.Cells for Node.js via C++, vi behöver bara välja en cell i översta raden som aktiv cell, och sedan dela med [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--)-metoden.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets C1 cell in the top row as the active cell.
sheet.setActiveCell("C1");

// Split worksheet vertically on columns
sheet.split();
```

## **Dela arbetsblad horisontellt på rader**
För att separera ditt Excel-fönster horisontellt, välj raden under den rad där du vill att uppdelningen ska ske i Excel.

Det är enkelt att dela arbetsblad horisontellt på rader programmässigt med Aspose.Cells for Node.js via C++, vi behöver bara välja en cell i vänstra kolumnen som aktiv cell, och sedan dela med [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--)-metoden.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets A6 cell in the left column as the active cell.
sheet.setActiveCell("A6");

// Split worksheet horizontally on rows
sheet.split();

workbook.save("dest.xlsx");
```

## **Dela arbetsblad i fyra delar**
För att visa fyra olika sektioner av samma arbetsblad samtidigt, dela upp skärmen både vertikalt och horisontellt i Excel.

Det är enkelt att dela arbetsblad vertikalt på kolumner programmässigt med Aspose.Cells for Node.js via C++, vi behöver bara välja en cell som inte är i den första raden och kolumnen som aktiv cell, och sedan dela med [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--)-metoden.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets E6 cell as the active cell.
sheet.setActiveCell("E6");

// Split worksheet into four parts
sheet.split();
```

## **Hur man tar bort uppdelning**
För att ta bort arbetsbladets uppdelning, klicka bara på Split-knappen igen.

Aspose.Cells for Node.js via C++ erbjuder en [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--)-metod för att ta bort delningsinställningen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Remove split.
sheet.removeSplit();

// Split worksheet into four parts
sheet.split();
```

