---
title: Hantera DataLabels för Excel diagram med C++
linktitle: Datamärken
type: docs
weight: 50
url: /sv/cpp/insert-datalabels-to-chart/
description: Lär dig hur du effektivt hanterar datamärken i Excel diagram med Aspose.Cells for C++. Vår omfattande guide täcker olika hanteringsuppgifter, inklusive att lägga till, ta bort och modifiera etiketter för att förbättra diagrammens läsbarhet och användbarhet.
keywords: Aspose.Cells for C++, Excel diagram, datamärken, hantering, läsbarhet, användbarhet, lägga till, ta bort, modifiera.
---

{{% alert color="primary" %}}

DataLabels är en viktig del av ett diagram. Vi kan enkelt känna till värdet, procenten, etc. för varje serie.

{{% /alert %}}

## **Datamärkenalternativ**
Aspose.Cells gör det också möjligt att hantera diagrammets datamärken i realtid med objektet [DataLabels](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/). Det är enkelt att flytta, uppdatera och formatera datamärken i diagrammet.

|![todo:image_alt_text](chart_datalabels.png)|

## **Hantera datamärken för diagram**
Det är enkelt att hantera datamärken i diagrammet med Aspose.Cells [DataLabels](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/).

Följande kodavsnitt visar hur man hanterar DataLabels:

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
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

    // Show value labels
    chart.GetNSeries().Get(0).GetDataLabels().SetShowValue(true);

    // Show series name labels
    chart.GetNSeries().Get(1).GetDataLabels().SetShowSeriesName(true);

    // Move labels to center
    chart.GetNSeries().Get(1).GetDataLabels().SetPosition(LabelPositionType::Center);

    // Save the file
    workbook.Save(u"chart_datalabels.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Avancerade ämnen**
- [Lägg till anpassade etiketter till datapunkter i diagramserien](/cells/sv/cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)
- [Inaktivera textbrytning för datamärken på diagrammet](/cells/sv/cpp/disable-text-wrapping-for-data-labels-of-the-chart/)
- [Ändra diagrammets datamärkesform för att passa texten](/cells/sv/cpp/resize-chart-s-data-label-shape-to-fit-text/)
- [Riktextanpassade datamärken för diagrammet](/cells/sv/cpp/rich-text-custom-data-label-of-chart-point/)
- [Ställ in datamärkenas formtyp i diagram](/cells/sv/cpp/set-the-shape-type-of-data-labels-of-chart/)
- [Visa cellområde som datamärken](/cells/sv/cpp/showing-cell-range-as-the-data-labels/)
