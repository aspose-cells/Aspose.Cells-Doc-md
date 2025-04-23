---
title: Frys översta raden(rad) i Excel arbetsblad med Node.js via C++
linktitle: Frys rader
type: docs
weight: 190
url: /sv/nodejs-cpp/how-to-freeze-rows-of-excel-worksheet
description: I denna artikel lär du dig hur du fryser översta raderna i Excel arbetsblad programmatiskt med Node.js bibliotek med C++ API.
keywords: Frys översta rader, Frys översta raden i Node.js via C++.
---

## **Introduktion**

I denna artikel lär vi oss hur man fryser översta rad(rader). När du har mycket data under en gemensam rubrik kan det vara svårt att se rubriken när du skrollar ner i arbetsbladet. Du kan frysa översta rad(rader) så att du kan se den frysta delen även när resten av datan skrollas. Det är enkelt att se rubriker i de översta raderna.

## **Frysa rader i Excel**

**![Frysa översta rad(er) i Excel](Freeze-Rows.png)**

1. Om du vill frysa översta rad(er), välj först raden under den rad som ska frysas.
2. Klicka på Visa > Frysa rader.
3. I rullgardinsmenyn, klicka på Frysa översta rad.
4. Om du skrollar nedåt, är den första raden alltid i översta vyn.

**![Frysen rad](Frozen-Row.png)**

Som du kan se är den första raden fryst; den första raden behålls alltid högst upp när du skrollar ner.

Frys rader låter dig visa din stora data utan att hålla koll på radetiketten.

## **Frys rader med Aspose.Cells for Node.js via C++**
Det är enkelt att frysa rad(er) med Aspose.Cells for Node.js via C++. 
Använd [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-)-metoden för att frysa rad(er) vid vald rad.
1. Konstruera Arbetsbok för att öppna filen eller skapa en tom fil.
2. Frysa den första raden med Worksheet.freezePanes()-metoden.
3. Spara filen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Freeze.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Freezing panes at the cell B2
workbook.getWorksheets().get(0).freezePanes("A2", 1, 0);

// Saving the file
workbook.save("frozen.xlsx");
```

Bifogad [provkäll-Excel-fil](../Freeze.xlsx).
