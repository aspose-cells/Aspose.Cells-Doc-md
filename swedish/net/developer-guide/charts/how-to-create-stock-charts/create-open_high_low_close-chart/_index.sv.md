---
title: Skapa Open-High-Low-Close(OHLC) aktiediagram
description: Lär dig hur du skapar ett öppet-högt-låg-stängt aktiediagram med Aspose.Cells for .NET. Vår guide kommer att visa hur du plottar aktiemarknadsdata, inklusive öppna, höga, låga och stängda kurser, på ett diagram för bättre analys och visualisering.
keywords: Aspose.Cells for .NET, Open-High-Low-Close Stock Chart, Stock Market Data, Analysis, Visualization.
type: docs
weight: 182
url: /sv/net/create-open-high-low-close-stock-chart/
---
##  **Möjliga användningsscenarier**
Diagrammet Open-High-Low-Close (OHLC) använder fem kolumner med data, i ordning: kategori, öppen, hög, låg och stäng. Prisintervallet i varje kategori indikeras återigen med en vertikal linje, medan intervallet mellan öppet och stängt ges av en bredare flytande stapel; om priset ökar i kategorin (stängt är högre än öppet) fylls stapeln med en färg, medan om priset sjunker fylls stapeln med en annan. Denna typ av diagram kallas ofta ett ljusstakediagram.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
##  **Synlighetsförbättringar i diagrammet**
Vi använder ofta färger snarare än svartvitt för att indikera stigande och sjunkande priser. I den första uppsättningen av ljusstakar nedan visar rött ökande och grönt sjunkande priser.

![todo:image_alt_text](sample2.png)
##  **Exempelkod**
 Följande exempelkod laddar[exempel på Excel-fil](Open-High-Low-Close.xlsx) och genererar[utdata Excel-fil](out.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-open-high-low-close-stock-chart.cs" >}}
