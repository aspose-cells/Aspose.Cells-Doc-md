---
title: Skapa Open High Low Close (OHLC) Stock Chart
description: Lär dig hur man skapar ett öppet högt lågt stängt aktiekartogram med Aspose.Cells för Python via .NET. Vår guide visar hur man plottar aktiemarknadsdata, inklusive öppet, högt, lågt och stängningspriser, på ett diagram för bättre analys och visualisering.
keywords: Aspose.Cells för Python via .NET, Öppet Högt Lågt Stängt Aktie Diagram, Aktiemarknadsdata, Analys, Visualisering.
type: docs
weight: 182
url: /sv/python-net/create-open-high-low-close-stock-chart/
---

## **Möjliga användningsscenario**
Det öppen-hög-låg-stänga (OHLC) diagrammet använder fem datakolumner, i ordning: kategori, öppen, hög, låg och stänga. Prisintervallet i varje kategori indikeras igen av en vertikal linje, medan intervallet mellan öppen och stänga ges av en bredare stångformad stapel; om priset ökar i kategorin (stänga är högre än öppen), fylls stapeln med en färg, medan om priset minskar, fylls stapeln med en annan färg. Den här typen av diagram kallas ofta ett ljusstakdiagram.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)

## **Synlighetsförbättringar i diagrammet**
Vi använder ofta färger istället för svartvitt för att indikera ökande och minskande priser. I det första setet med ljusstakar nedan visar rött ökande och grönt minskande priser.

![todo:image_alt_text](sample2.png)

## **Exempelkod**
Följande exempelkod laddar den [exempelfil för Excel](Open-High-Low-Close.xlsx) och genererar den [utfärdade Excelfilen](out.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-create-open-high-low-close-stock-chart.py" >}}
{{< app/cells/assistant language="python-net" >}}
