---  
title: Hur man ställer in punkt som total med Node.js via C++  
linktitle: Hur man ställer in punkt som total  
description: Lär dig att ställa in punkter som total i vattenfallsdiagram med Aspose.Cells for Node.js via C++.  
keywords: WaterFall diagram, Punkt, Ställ in som total, Node.js via C++  
type: docs  
weight: 72  
url: /sv/nodejs-cpp/how-to-set-point-as-total/  
---  

## Vad är "Ställ in punkt som total" i Excel-diagram

I vissa Excel-diagram, till exempel vattenfallsdiagram, är vissa datapunkter summan av de föregående punkterna, och du kan behöva "ställa in punkt som total". Vi visar exempel på kod och illustrationen nedan.

## Ett vattenfallsdiagram behöver "Ställa in punkt som total" 

![todo:image_alt_text](set-as-total1.png)

Denna bild visar ett vattenfallsdiagram i Excel. Vi kan se att det finns fyra datapunkter som börjar med "Total", och de används för att räkna alla föregående datapunkter. I denna bild är inställningarna inte helt rätt. När vi väljer en punkt "Total 2024", kan vi se att alternativet "Ställ som total" inte är ikryssat i Excel. Bifogat nedan är [provfilen](SampleSheet.xlsx) som behöver modifieras, och vi kommer att använda Aspose.Cells for Node.js via C++ för att ställa in det korrekt.

## Använd Aspose.Cells for Node.js via C++ för att "Ställa in punkt som total" 

Vi använder följande kod för att få filen att ställas in korrekt:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);
const chart = worksheet.getCharts().get("Graphiq5");

// set some points as total column 
// In this example, we set points 0, 4, 8, 12 as total
chart.getNSeries().get(0).getLayoutProperties().setSubtotals([0, 4, 8, 12]);
workbook.save(path.join(dataDir, "output.xlsx"));
```

Du kan få följande rätta [utdatafil](output.xlsx)

Som visas i figuren nedan är de fyra "Total"-datapunkterna korrekt inställda, och du kan se skillnaden från föregående diagram.

![todo:image_alt_text](set-as-total2.png)  
{{< app/cells/assistant language="nodejs-cpp" >}}
