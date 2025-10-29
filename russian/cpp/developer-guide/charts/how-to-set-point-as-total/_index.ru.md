---
title: Как установить точку как сумму с помощью C++
linktitle: Как установить точку как сумму
description: В некоторых диаграммах Excel, например, гистограмме WaterFall, возможно потребуется установить точку как сумму. В этой статье описывается, как использовать Aspose.Cells с C++ для этого.
keywords: Диаграмма WaterFall, Точка, Установить как сумму.
type: docs
weight: 72
url: /ru/cpp/how-to-set-point-as-total/
---

## Что означает "Установить точку как сумму" в диаграмме Excel

В некоторых диаграммах Excel, например, WaterFall, некоторые данные точки являются суммой предыдущих точек, и вам может понадобиться "установить точку как сумму". Мы покажем пример кода и иллюстрацию ниже.

## Диаграмма WaterFall требует "Установить точку как сумму" 

![todo:image_alt_text](set-as-total1.png)

На изображении показана диаграмма WaterFall в Excel. Видно, что есть четыре точки, начинающиеся с "Total", и они используются для подсчета всех предыдущих данных.
На этом изображении настройки не совсем правильные, когда мы выбираем точку "Итого 2024", и видно, что опция "Установить как итого" в Excel не активирована.
Ниже прикреплен [пример файла Excel](SampleSheet.xlsx), который нужно изменить, и мы будем использовать Aspose.Cells для правильной настройки.

## Использование Aspose.Cells для "Настройка точки как итого" 

Мы используем следующий код для правильной настройки файла:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Initialize file path
    U16String filePath(u"");

    // Load the workbook
    Workbook wb(filePath + u"SampleSheet.xlsx");

    // Get the first worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Get the chart by name
    Chart chart = worksheet.GetCharts().Get(u"Graphiq5");

    // Set some points as total column
    // In this example, we set points 0, 4, 8, 12 as total
    Vector<int32_t> subtotals = {0, 4, 8, 12};
    chart.GetNSeries().Get(0).GetLayoutProperties().SetSubtotals(subtotals);

    // Save the workbook
    wb.Save(filePath + u"output.xlsx");

    std::cout << "Chart subtotals set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Вы можете получить следующий исправленный [выходной файл](output.xlsx)

Как видно на рисунке ниже, четыре точки "Total" настроены правильно, и вы можете заметить различия с предыдущей диаграммой.

![todo:image_alt_text](set-as-total2.png)
{{< app/cells/assistant language="cpp" >}}
