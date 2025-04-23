---
title: Hantera legend för Excel diagram med C++
linktitle: Teckenförklaring
description: Lär dig hur du använder Aspose.Cells for C++ för att effektivt använda och anpassa diagramlegender i Microsoft Excel. Vår omfattande guide förklarar legendens funktion, hur man får tillgång till och ändrar den, samt hur man förbättrar visualisering och dataförståelse med hjälp av legender.
keywords: Aspose.Cells for C++, Diagramlegender, Microsoft Excel, Visualisering, Dataförståelse.
type: docs
weight: 50
url: /sv/cpp/chart-legend/
---

## **Teckenförklaringsalternativ**
Aspose.Cells tillåter även att du hanterar ett diagramlegenden i realtid. Med [Legend](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legend/) objektet kan legenden flyttas, uppdateras och formateras.

|![todo:image_alt_text](chart_legend.png)|

## **Inställning av diagrammets teckenförklaring**
Det är enkelt att hantera legend för ett diagram med Aspose.Cells [Legend](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legend/).

Följande kodsnutt visar hur man hanterar legenden:

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(60);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Setting the title of a chart
    chart.GetTitle().SetText(u"Title");

    // Setting the font color of the chart title to blue
    chart.GetTitle().GetFont().SetColor(Color::Blue());

    // Move the legend to left
    chart.GetLegend().SetPosition(LegendPositionType::Left);

    // Set font color of the legend
    chart.GetLegend().GetFont().SetColor(Color::Blue());

    // Save the file
    workbook.Save(u"chart_legend.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Avancerade ämnen**
- [Ställ in texten för diagrammets teckenförklaringspostfyllning till ingen med hjälp av Aspose.Cells](/cells/sv/cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)
