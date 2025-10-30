--- 
title: Skapa High Low Close(HLC) aktiediagram med C++ 
linktitle: Skapa High Low Close (HLC) Stock Chart 
description: Lär dig att skapa ett high low close aktiediagram med Aspose.Cells for C++. Vår steg för steg guide visar hur du plottar aktiemarknadsdata, inklusive high, low och closing priser, på ett diagram för bättre analys och visualisering. 
keywords: Aspose.Cells for C++, High Low Close aktiediagram, Aktiemarknadsdata, Analys, Visualization. 
type: docs 
weight: 181 
url: /sv/cpp/create-high-low-close-stock-chart/ 
--- 

## **Möjliga användningsscenario** 
HLC-aktiediagrammet använder fyra datakolumner. Den första kolumnen är en kategori, vanligtvis en datum men aktienamn kan också användas. De nästkommande tre kolumnerna i ordning är för höga, låga och stängningspriser. Prisintervallet för varje kategori indikeras av en vertikal linje från låg till hög, och stängningspriset visas med hjälp av ett markering som sträcker sig till höger om denna linje. 

![todo:image_alt_text](sample.png) 
## **Synlighetsförbättringar i diagrammet** 
Ibland, för att göra diagrammet mer intuitivt, kan vi ändra utseendet på markören (stäng) eller få den att visas på den sekundära axeln. 

![todo:image_alt_text](sample2.png) 
## **Exempelkod** 
Följande exempelkod laddar [exempel Excel-filen](High-Low-Close.xlsx) och genererar [utdatamappar Excel-filen](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close-Stock Chart
    int pieIdx = worksheet.GetCharts().Add(ChartType::StockHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:D9", true);

    // Set category data 
    chart.GetNSeries().GetCategoryData() = u"A2:A9";

    // Set the marker with the built-in data 
    chart.GetNSeries().Get(2).GetMarker().SetMarkerStyle(ChartMarkerType::Dash);
    chart.GetNSeries().Get(2).GetMarker().SetMarkerSize(20);
    chart.GetNSeries().Get(2).GetMarker().GetArea().SetFormatting(FormattingType::Custom);
    chart.GetNSeries().Get(2).GetMarker().GetArea().SetForegroundColor(Color::Maroon());

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
``` 
{{< app/cells/assistant language="cpp" >}}
