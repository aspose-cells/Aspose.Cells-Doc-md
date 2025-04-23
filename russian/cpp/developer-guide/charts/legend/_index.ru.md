---
title: Управление легендой диаграмм Excel с помощью C++
linktitle: Легенда
description: Узнайте, как эффективно использовать и настраивать легенды диаграмм в Microsoft Excel, используя Aspose.Cells for C++. Наш комплексный гид объясняет функцию легенды, как получить к ней доступ и изменять, а также как улучшить визуализацию и понимание данных с помощью легенд.
keywords: Aspose.Cells for C++, Легенды диаграмм, Microsoft Excel, Визуализация, Понимание данных.
type: docs
weight: 50
url: /ru/cpp/chart-legend/
---

## **Параметры легенды**
Aspose.Cells также позволяет управлять легендой диаграммы во время выполнения. С помощью объекта [Legend](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legend/), легенду можно перемещать, обновлять и форматировать.

|![todo:image_alt_text](chart_legend.png)|

## **Установка легенды диаграммы**
Просто управлять легендой диаграммы с помощью Aspose.Cells [Legend](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legend/) очень просто.

Следующий код демонстрирует, как управлять легендой:

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

## **Расширенные темы**
- [Установите текст заливки записи легенды диаграммы на отсутствие с использованием Aspose.Cells](/cells/ru/cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)
