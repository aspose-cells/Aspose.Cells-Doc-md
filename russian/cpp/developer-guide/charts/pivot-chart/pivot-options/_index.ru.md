---
title: Как управлять PivotChart с помощью PivotOptions в C++
linktitle: Опции сводной таблицы
type: docs
weight: 10
url: /ru/cpp/how-to-manage-pivotchart-with-pivotoptions/
description: Как управлять PivotChart с помощью PivotOptions, используя C++.
keywords: Сводная диаграмма
---

## Что такое сводная диаграмма

Сводная диаграмма в Excel - это графическое представление данных, созданное на основе сводной таблицы. Она позволяет пользователям визуализировать и анализировать данные динамически, суммируя и отображая информацию в виде диаграммы. Сводные диаграммы интерактивны и их легко изменять, чтобы показать различные перспективы данных, что делает их мощным инструментом для анализа и презентации данных в Excel.

## Как управлять сводной диаграммой с опциями сводной таблицы

Используя Aspose.Cells, вы можете использовать [**PivotOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/pivotoptions/) для управления сводной диаграммой.

Пример файла и кода:  
[Образец файла](Sample.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path for the sample Excel file
    U16String path = u"..\\Data\\01_SourceDirectory\\";

    // Create a Workbook object from the sample file
    Workbook book(path + u"Sample.xlsx");

    // Get the first chart from the first worksheet
    Chart chart = book.GetWorksheets().Get(0).GetCharts().Get(0);

    // Get the PivotOptions from the chart
    PivotOptions opt = chart.GetPivotOptions();

    // Hide ZoneFilter in PivotChart
    opt.SetDropZoneFilter(false); // HideZoneFilter

    // You can set more properties, try them!
    // opt.SetDropZoneCategories(false);  // HideZoneCategories
    // opt.SetDropZoneData(false);        // HideZoneData
    // opt.SetDropZoneSeries(false);      // HideZoneSeries
    // opt.SetDropZonesVisible(false);    // Hide All

    // Save the modified file to see the effect
    book.Save(path + u"HideZoneFilter.xlsx");

    std::cout << "Pivot chart updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

С помощью вышеуказанного примера кода вы можете проверить результатный файл с следующим эффектом, как показано на рисунке:

**![Вывод](Output.png)**
