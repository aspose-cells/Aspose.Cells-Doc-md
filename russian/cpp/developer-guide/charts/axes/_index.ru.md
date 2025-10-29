---
title: Управление осями графиков Excel с помощью C++
description: Узнайте, как настраивать оси графиков в Aspose.Cells for C++. Наше руководство покажет, как регулировать основные и вспомогательные оси, устанавливать их диапазоны и изменять свойства для улучшения ваших графиков.
keywords: Aspose.Cells for C++, оси графиков, настройка, основные оси, вспомогательные оси, диапазон, свойства.
linktitle: Оси
type: docs
weight: 50
url: /ru/cpp/chart-axes/
---

{{% alert color="primary" %}}

В диаграммах Excel существует 3 вида осей:
1. Горизонтальная (категориальная) ось : Ось X
1. Вертикальная (значения) ось : Ось Y
1. Ось глубины (серий) : Ось Z

{{% /alert %}}

## **Опции оси**
Aspose.Cells также позволяет управлять осями графиков во время выполнения. С помощью объекта [Axis](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/) вы можете изменять все параметры оси так же, как в Excel.

|![todo:image_alt_text](chart_axes.png)|

## **Управление осью X и Y**

В графиках Excel горизонтальные и вертикальные оси являются двумя наиболее популярными осями.

Следующий фрагмент кода демонстрирует, как установить параметры осей X и Y.

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

## **Дополнительные темы**
- [Изменение направления меток делений](/cells/ru/cpp/change-tick-label-direction/)
- [Определение существующих осей на графике](/cells/ru/cpp/determine-which-axis-exists-in-the-chart/)
- [Обработка автоматических единиц оси диаграммы, как в Microsoft Excel](/cells/ru/cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)
- [Чтение меток оси после вычисления диаграммы](/cells/ru/cpp/read-axis-labels-after-calculating-the-chart/)
- [Как установить ось категорий в графике Excel](/cells/ru/cpp/how-to-set-category-axis/)
{{< app/cells/assistant language="cpp" >}}
