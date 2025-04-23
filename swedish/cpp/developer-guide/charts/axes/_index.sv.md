---
title: Hantera Excel diagramaxlar med C++
description: Lär dig konfigurera diagramaxlar i Aspose.Cells for C++. Vår guide visar hur du justerar primära och sekundära axlar, ställer in deras intervall och ändrar deras egenskaper för att förbättra diagrammen.
keywords: Aspose.Cells for C++, diagramaxlar, konfiguration, primära axlar, sekundära axlar, intervall, egenskaper.
linktitle: Axlar
type: docs
weight: 50
url: /sv/cpp/chart-axes/
---

{{% alert color="primary" %}}

I Excel-diagram finns det 3 typer av axlar:
1. Horisontell (Kategori) Axel : X-axel
1. Vertikal (Värde) Axeln : Y-axel
1. Djup (Serier) Axel : Z-axel

{{% /alert %}}

## **Axelealternativ**
Aspose.Cells tillåter också att du hanterar diagramaxlar vid körning. Med [Axis](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/)-objektet kan du ändra alla alternativ för axeln, precis som i Excel.

|![todo:image_alt_text](chart_axes.png)|

## **Hantera X- och Y-axlar**

I Excel-diagram är horisontella och vertikala axlar de två mest populära axlarna att använda.

Följande kodsnutt visar hur man ställer in alternativen för X- och Y-axlar.

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
    worksheet.GetCells().Get(u"A1").PutValue(u"Series1");
    worksheet.GetCells().Get(u"A2").PutValue(50);
    worksheet.GetCells().Get(u"A3").PutValue(100);
    worksheet.GetCells().Get(u"A4").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(u"Series2");
    worksheet.GetCells().Get(u"B2").PutValue(60);
    worksheet.GetCells().Get(u"B3").PutValue(32);
    worksheet.GetCells().Get(u"B4").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.SetChartDataRange(u"A1:B4", true);

    // Hiding X axis
    chart.GetCategoryAxis().SetIsVisible(false);

    // Setting max value of Y axis
    chart.GetValueAxis().SetMaxValue(200);

    // Setting major unit
    chart.GetValueAxis().SetMajorUnit(50);

    // Save the file
    workbook.Save(u"chart_axes.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Avancerade ämnen**
- [Ändra riktning för ticketiketter](/cells/sv/cpp/change-tick-label-direction/)
- [Bestäm vilken axel som finns i diagrammet](/cells/sv/cpp/determine-which-axis-exists-in-the-chart/)
- [Hantera automatiska enheter för diagramaxeln som Microsoft Excel](/cells/sv/cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)
- [Läs av axeletiketter efter att ha beräknat diagrammet](/cells/sv/cpp/read-axis-labels-after-calculating-the-chart/)
- [Hur man ställer in kategoriaxel i Excel-diagram](/cells/sv/cpp/how-to-set-category-axis/)
