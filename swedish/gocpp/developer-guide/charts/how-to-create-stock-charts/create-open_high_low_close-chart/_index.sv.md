---
title: Skapa Open High Low Close (OHLC) aktiediagram med Golang via C++
description: Lär dig att skapa ett öppet höga låga close aktiediagram med Aspose.Cells for C++. Vår guide demonstrerar hur man plottar aktiemarknadsdata, inklusive öppnings , högsta , lägsta och stängningspriser, på ett diagram för bättre analys och visualisering.
keywords: Aspose.Cells for C++, Öppet Höga Låga Close aktiediagram, Aktiemarknadsdata, Analys, Visualisering.
type: docs
weight: 182
url: /sv/go-cpp/create-open-high-low-close-stock-chart/
---

## **Möjliga användningsscenario**
Det öppen-hög-låg-stänga (OHLC) diagrammet använder fem datakolumner, i ordning: kategori, öppen, hög, låg och stänga. Prisintervallet i varje kategori indikeras igen av en vertikal linje, medan intervallet mellan öppen och stänga ges av en bredare stångformad stapel; om priset ökar i kategorin (stänga är högre än öppen), fylls stapeln med en färg, medan om priset minskar, fylls stapeln med en annan färg. Den här typen av diagram kallas ofta ett ljusstakdiagram.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)

## **Synlighetsförbättringar i diagrammet**
Vi använder ofta färger snarare än svart och vitt för att indikera ökande och minskande priser. I den första uppsättningen av candlesticks nedan visar rött stigande priser och grönt fallande priser.

![todo:image_alt_text](sample2.png)

## **Exempelkod**
Följande exempelkod laddar den [exempelfil för Excel](Open-High-Low-Close.xlsx) och genererar den [utfärdade Excelfilen](out.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreateOpenHighLowCloseChart.go" >}}
