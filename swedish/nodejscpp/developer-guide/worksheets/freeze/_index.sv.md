---  
title: Frys panorer i Excel kalkylblad med Node.js via C++  
linktitle: Frysa rader  
type: docs  
weight: 190  
url: /sv/nodejs-cpp/how-to-freeze-panes-of-excel-worksheet  
description: I den här artikeln lär du dig att frysa paneor i Excel kalkylblad programmässigt med Aspose.Cells for Node.js via C++.  
keywords: Frys paneor, Frys fönster.  
---  

## **Introduktion**  

I den här artikeln lär vi oss Hur man fryser paneor. När du har en stor mängd data under en gemensam rubrik kan du inte se rubriken när du scrollar ner i kalkylbladet. Och varje post innehåller mycket data. Du kan frysa paneor så att du kan se den frysta delen även när resten av datan scrollas. Du kan enkelt se rubriker i de översta raderna eller första kolumnerna. Att frysa och avfrysa paneor ändrar bara vy av datan utan att ändra själva datan.  

## **I Excel**  

**![Frys rader i Excel](Frys-panor.png)**  

1. Om du vill frysa paneor, frysa rader och kolumner, välj först en cell (som B2).  
2. Klicka på Visa > Frysa rader.  
3. I rullgardinsmenyn klickar du på Frysa rader.  
4. Om du scrollar ner eller till höger, är den första raden och kolumnen frysta.  

**![Frysade paneor](Frozen-Panes.png)**  

Som du kan se är den första raden och kolumn A frysta, den andra raden är 32 och den andra synliga kolumnen är D.  

Frys paneor låter dig visa din stora data utan att hålla koll på rad- eller kolumnetiketter.  

## **Frysfönster med Aspose.Cells for Node.js via C++**  
Det är enkelt att frysa fönster med Aspose.Cells for Node.js via C++. Använd [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-)-metoden för att frysa fönster vid den valda cellen.  
1. Konstruera Arbetsbok för att öppna filen eller skapa en tom fil.  
2. Frysa fönster med Worksheet.freezePanes()-metoden.  
3. Spara filen.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Freeze.xlsx")); 
// Freezing panes at the cell B2
workbook.getWorksheets().get(0).freezePanes("B2", 1, 1);
// Saving the file
workbook.save("frozen.xlsx");
```  

Bifogad [provkälla Excel-fil](Frys.xlsx).  

{{< app/cells/assistant language="nodejs-cpp" >}}
