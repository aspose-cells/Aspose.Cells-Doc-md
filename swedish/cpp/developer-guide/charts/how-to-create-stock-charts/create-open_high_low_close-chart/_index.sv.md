---
title: Skapa öppna höga låga close(OHLC) aktiediagram med C++
description: Lär dig att skapa ett öppet höga låga close aktiediagram med Aspose.Cells for C++. Vår guide demonstrerar hur man plottar aktiemarknadsdata, inklusive öppnings , högsta , lägsta och stängningspriser, på ett diagram för bättre analys och visualisering.
keywords: Aspose.Cells for C++, Öppet Höga Låga Close aktiediagram, Aktiemarknadsdata, Analys, Visualisering.
type: docs
weight: 182
url: /sv/cpp/create-open-high-low-close-stock-chart/
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

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Open-High-Low-Close.xlsx");
    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Create High-Low-Close-Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockOpenHighLowClose, 5, 6, 20, 12);
    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);
    // Set the legend can be showed
    chart.SetShowLegend(true);
    // Set the chart title name
    chart.GetTitle().SetText(u"Open-High-Low-Close Stock");
    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);
    // Set data range
    chart.SetChartDataRange(u"A1:E9", true);
    // Set category data
    chart.GetNSeries().GetCategoryData() = u"A2:A9";
    // Set the DownBars and UpBars with different color
    chart.GetNSeries().Get(0).GetDownBars().GetArea().SetForegroundColor(Color::Green());
    chart.GetNSeries().Get(0).GetUpBars().GetArea().SetForegroundColor(Color::Red());
    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);
    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
