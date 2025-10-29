---
title: Управление метками данных графика Excel с помощью C++
linktitle: Метки данных
type: docs
weight: 50
url: /ru/cpp/insert-datalabels-to-chart/
description: Узнайте, как эффективно управлять метками данных в графиках Excel с помощью Aspose.Cells for C++. Наш всесторонний гид охватывает различные задачи управления, включая добавление, удаление и изменение меток для повышения читаемости и удобства использования графика.
keywords: Aspose.Cells for C++, графики Excel, метки данных, управление, читаемость, удобство, добавление, удаление, изменение.
---

{{% alert color="primary" %}}

Метки данных — важная часть графика. Мы можем легко знать значение, процент и т. д. каждого ряда.

{{% /alert %}}

## **Опции меток данных**
Aspose.Cells также позволяет управлять метками данных графика во время выполнения с помощью объекта [DataLabels](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/). Просто перемещайте, обновляйте и форматируйте метки данных графика.

|![todo:image_alt_text](chart_datalabels.png)|

## **Управление метками данных диаграммы**
Легко управлять метками данных графика с помощью Aspose.Cells [DataLabels](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/).

Следующий фрагмент кода демонстрирует, как управлять DataLabels:

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

## **Дополнительные темы**
- [Добавление пользовательских меток к данным точек в серии диаграммы](/cells/ru/cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)
- [Отключение переноса текста для меток данных диаграммы](/cells/ru/cpp/disable-text-wrapping-for-data-labels-of-the-chart/)
- [Изменение формы метки данных диаграммы для подгонки текста](/cells/ru/cpp/resize-chart-s-data-label-shape-to-fit-text/)
- [Настройка метки данных диаграммы точки с использованием разностных стилей](/cells/ru/cpp/rich-text-custom-data-label-of-chart-point/)
- [Установка типа формы меток данных диаграммы](/cells/ru/cpp/set-the-shape-type-of-data-labels-of-chart/)
- [Показ диапазона ячеек в качестве меток данных](/cells/ru/cpp/showing-cell-range-as-the-data-labels/)
{{< app/cells/assistant language="cpp" >}}
