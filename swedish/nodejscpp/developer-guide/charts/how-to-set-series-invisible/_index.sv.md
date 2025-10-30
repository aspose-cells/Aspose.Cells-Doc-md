---
title: Hur man ställer in serie som osynlig med Node.js via C++
linktitle: Hur man sätter serien osynlig
description: Lär dig hur man ställer in serie som osynlig i Excel diagram med Aspose.Cells for Node.js via C++. 
keywords: Excel diagram, Serie, Osynlig, IsFiltered Node.js via C++.
type: docs
weight: 74
url: /sv/nodejs-cpp/how-to-set-series-invisible/
---

## Hur man ställer in serie som osynlig i Excel-diagram

I Excel-diagram kan du högerklicka på ett diagram, klicka på "Välj data" och i pop-up-fönstret kan du ställa in om en serie är synlig genom att markera eller avmarkera den. Du kan ladda ner följande [exempelfil](SeriesFiltered.xlsx) och använda den i Excel enligt figuren för att uppnå denna funktion. Nästa steg är att visa dig hur du uppnår detta med Aspose.Cells-biblioteket.

![todo:image_alt_text](series-invisible.png)

## Hur man ställer in serie som osynlig med Aspose.Cells 

Vi använder följande kod för att göra serie osynlig med Aspose.Cells:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SeriesFiltered.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const charts = workbook.getWorksheets().get(0).getCharts();
const chart = charts.get("Chart 1");
const nSeriesFiltered = chart.getFilteredNSeries();
const nSeries = chart.getNSeries();
nSeries.get(1).setIsColorVaried(true);
nSeries.get(0).setIsColorVaried(true);
workbook.save(path.join(dataDir, "output.xlsx"));
```

Du kan hämta följande [Inmatningsfil](SeriesFiltered.xlsx) och [Utdatafil](output.xlsx).

Som visas i figuren nedan har de två första serierna, som ursprungligen var synliga, blivit osynliga i utdatafilen.
![todo:image_alt_text](output.png)
{{< app/cells/assistant language="nodejs-cpp" >}}
