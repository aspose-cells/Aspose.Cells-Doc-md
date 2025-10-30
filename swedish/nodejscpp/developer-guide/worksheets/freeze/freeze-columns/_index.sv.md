---  
title: Frys första kolumn(er) i Excel arbetsblad med Node.js via C++  
linktitle: Frys kolumner  
type: docs  
weight: 190  
url: /sv/nodejs-cpp/how-to-freeze-columns-of-excel-worksheet  
description: Lär dig hur du frys vänstra kolumner i Excel arbetsblad programmässigt med Aspose.Cells for Node.js via C++.  
keywords: Frys vänstra kolumner, Frys första kolumner, Lås kolumnen(n)  
---  

## **Introduktion**  

I denna artikel lär vi oss hur man fryser vänster kolumn(er). När du har en stor mängd data i en rad kan det vara svårt att se de vänstra kolumnerna när du skrollar horisontellt i arbetsbladet. Du kan frysa och låsa första kolumn(er) så att du kan se den frysta delen även när resten av datan skrollas. Det är enkelt att se rubriker i de vänstra kolumnerna.  

## **Frys kolumner i Excel**  

**![Frys vänster kolumn(er) i Excel](freeze-columns.png)**  

1. Om du vill frysa vänstra kolumn(er), välj först kolumnen under den kolumn som ska frysas.
2. Klicka på Visa > Frysa rader.
3. I rullgardinsmenyn, klicka på Frysa första kolumn.
4. Om du skrollar nedåt, är den första kolumnen alltid i vänster vy.

**![Frysen kolumn](frozen-columns.png)**  

Som du kan se är den första kolumnen fryst, och den första kolumnen är alltid låst högst upp när du skrollar horisontellt.

Frys kolumner låter dig visa din långa data utan besvär med att hålla koll på den första kolumnen.

## **Frys kolumner med Aspose.Cells for Node.js via C++**  
Det är enkelt att frysa första kolumn(en) med Aspose.Cells for Node.js via C++.  
Använd metod [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) för att frysa kolumn(er) vid den valda kolumnen.  
1. Konstruera Arbetsbok för att öppna filen eller skapa en tom fil.
2. Frys den första kolumnen med Worksheet.freezePanes() metod.
3. Spara filen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Freeze.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
// Freezing panes at the second column
workbook.getWorksheets().get(0).freezePanes("B1", 0, 1);
// Saving the file
workbook.save("frozen.xlsx");
```  

Bifogad [provkälla Excel-fil](Frys.xlsx).  

{{< app/cells/assistant language="nodejs-cpp" >}}
