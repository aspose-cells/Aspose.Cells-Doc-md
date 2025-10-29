---
title: Определение типа X и Y значений точек в серии диаграммы с помощью C++
linktitle: Найдите тип значений X и Y точек в серии графика
description: Узнайте, как определить тип X и Y значений в точках серии диаграммы с помощью Aspose.Cells for C++. Наш гид объяснит различные типы данных и покажет, как получать и работать с ними в ваших диаграммах.
keywords: Aspose.Cells for C++, построение диаграмм, X значения, Y значения, типы данных, доступ, работа, серия диаграммы.
type: docs
weight: 150
url: /ru/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Возможные сценарии использования**
Иногда нужно определить тип X и Y значений точек диаграммы в серии. Aspose.Cells предоставляет методы `ChartPoint::get_XValueType` и `ChartPoint::get_YValueType`, которые можно использовать для этой цели. Обратите внимание, что перед использованием этих свойств необходимо вызвать метод `Chart::Calculate()`.

## **Найдите тип значений X и Y точек в серии графика**
Следующий пример кода загружает [пример файла Excel](64716905.xlsx) и обращается к первому графику внутри первого листа. Затем вызывает метод `Chart::Calculate()` и определяет тип X и Y значений первой точки графика, выводя их в консоль. Пожалуйста, смотрите вывод консоли ниже для参考.

## **Образец кода**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load sample Excel file containing chart
    Workbook wb(srcDir + u"sampleFindTypeOfXandYValuesOfPointsInChartSeries.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first chart
    Chart ch = ws.GetCharts().Get(0);

    // Calculate chart data
    ch.Calculate();

    // Access first chart point in the first series
    ChartPoint pnt = ch.GetNSeries().Get(0).GetPoints().Get(0);

    // Print the types of X and Y values of chart point
    std::cout << "X Value Type: " << static_cast<int>(pnt.GetXValueType()) << std::endl;
    std::cout << "Y Value Type: " << static_cast<int>(pnt.GetYValueType()) << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Вывод в консоль**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
