---
title: Hur man skapar ett TreeMap diagram med C++
description: Lär dig hur man skapar ett Treemap diagram i Aspose.Cells for C++. Vår guide hjälper dig att förstå de olika egenskaper och formateringsalternativ som är tillgängliga för Treemap diagram, inklusive färger, etiketter och datarepresentation.
keywords: Aspose.Cells for C++, Treemap diagram, skapa, egenskaper, formatering, färger, etiketter, datarepresentation, cirkulärt diagram, hierarkiskt diagram.
type: docs
weight: 161
url: /sv/cpp/creating-treemap-chart/
---

## **Möjliga användningsscenario**
Ett träd-diagram ger en hierarkisk vy av dina data och gör det lätt att upptäcka mönster, till exempel vilka objekt som är bästsäljare i en butik. Trädstammarna representeras av rektanglar och varje underavdelning visas som en mindre rektangel. Träddiagrammet visar kategorier med färg och närhet och kan enkelt visa mycket data som skulle vara svårt med andra diagramtyper.

![todo:image_alt_text](sample.png)
## **Träddiagram**
Efter att ha kört koden nedan kommer du att se träddiagrammet som visas nedan.

![todo:image_alt_text](result.png)
## **Exempelkod**
Följande exempelkod laddar den [prov Excel-fil](treemap.xlsx) och genererar [utdata Excel-fil](ut.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"treemap.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a Treemap chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::Treemap, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"TreeMap Chart");

    // Add series data range (D2:F13, actually)
    chart.GetNSeries().Add(u"D2:F13", true);

    // Set category data (A2:C13 is incorrect)
    chart.GetNSeries().SetCategoryData(u"A2:C13");

    // Show the DataLabels with category names
    chart.GetNSeries().Get(0).GetDataLabels().SetShowCategoryName(true);

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
