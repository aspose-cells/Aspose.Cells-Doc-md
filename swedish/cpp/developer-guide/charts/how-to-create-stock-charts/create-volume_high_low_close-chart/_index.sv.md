---
title: Skapa Volym Hög Låg Close(VHLC) aktiediagram med C++
linktitle: Skapa Volym Öppen Hög Låg Stäng (VOHLC) Aktiediagram
description: Lär dig att skapa ett volym hög låg close aktiediagram med Aspose.Cells for C++. Vår guide visar hur man plottar aktiemarknadsdata, inklusive volym, högsta, lägsta och stängningspriser, på ett diagram för bättre analys och visualisering.
keywords: Aspose.Cells for C++, Volume Hög Låg Close aktiediagram, Aktiemarknadsdata, Analys, Visualisering.
type: docs
weight: 183
url: /sv/cpp/create-volume-high-low-close-stock-chart/
---

## **Möjliga användningsscenario**
Det tredje aktiediagrammet vi tittar på är Volume High Low Close-diagrammet. Det är viktigt att påpeka att du måste ha data i rätt ordning. Om du behöver omarrangera din datatabell bör du göra det innan du skapar diagrammet. Detta diagram inkluderar en kolumn för volym direkt efter den första (kategori-) kolumnen, och diagrammen innehåller ett kolumndiagram på primäraxeln som visar denna volym, medan priserna flyttas till sekundäraxeln.

![todo:image_alt_text](data.png)
## **Volym-Öppen-Hög-Låg-Stäng (VOHLC) aktiediagram**

![todo:image_alt_text](sample.png)
## **Exempelkod**
Följande exempelkod laddar den [exempelfil för Excel](Volume-Open-High-Low-Close.xlsx) och genererar den [utfärdade Excelfilen](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Volume-High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockVolumeHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Volume-High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:E9", true);

    // Set category data 
    chart.GetNSeries().SetCategoryData(u"A2:A9");

    // Set Color for the first series (Volume) data 
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color{ 79, 129, 189 });

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

