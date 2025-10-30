---
title: Skapa Volume Open Hög Låg Close(VOHLC) aktiediagram med C++
description: Lär dig att skapa ett volume open high low close aktiediagram med Aspose.Cells for C++. Vår guide visar hur man plottrar aktiemarknadsdata, inklusive volym, öppnings , högsta , lägsta och stängningspriser, på ett diagram för bättre analys och visualisering.
keywords: Aspose.Cells for C++, Volume Open High Low Close aktiediagram, Aktiemarknadsdata, Analys, Visualisering.
type: docs
weight: 184
url: /sv/cpp/create-volume-open-high-low-close-stock-chart/
---

## **Möjliga användningsscenario**
Det fjärde aktiediagrammet vi tittar på är Volume Open High Low Close-diagrammet. Återigen är det viktigt att påpeka att du måste ha data i rätt ordning. Om du behöver omarrangera din datatabell bör du göra det innan du skapar diagrammet. Detta diagram inkluderar en kolumn för volym precis efter den första (kategori-) kolumnen, och diagrammen inkluderar ett kolumndiagram på primäraxeln som visar denna volym, medan priserna flyttas till sekundäraxeln.

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
    Workbook workbook(u"Volume-Open-High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close-Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockVolumeOpenHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend to be shown
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Volume-Open-High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:F9", true);

    // Set category data 
    chart.GetNSeries().GetCategoryData() = u"A2:A9";

    // Set Color for the first series (Volume) data 
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color{0xff, 79, 129, 189});

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
