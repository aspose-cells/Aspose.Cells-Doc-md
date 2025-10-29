---
title: Определите, какая ось существует в диаграмме с помощью C++
description: Узнайте, как определить, какая ось существует в диаграмме, созданной с помощью Aspose.Cells for C++. Наше руководство поможет вам понять, как идентифицировать и получать доступ к различным осям в диаграмме, включая категориальные, значенческие и вторичные оси.
keywords: Aspose.Cells for C++, диаграмма, ось, наличие, категория, значение, вторичная.
type: docs
weight: 140
url: /ru/cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет метод {0} для определения, есть ли в диаграмме определенная ось или нет.

В следующем образце кода демонстрируется использование [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/hasaxis/) для определения, имеет ли образецная диаграмма основную и вторичную категориальные и числовые оси.

{{% /alert %}}

Следующий пример кода демонстрирует использование [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/hasaxis/) для определения наличия в образцовой диаграмме Первичной и Вторичной Категориальной и Значительной Оси.

## Код C++ для определения существования оси в диаграмме

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a workbook object
    Workbook workbook(srcDir + u"source.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the chart
    Chart chart = worksheet.GetCharts().Get(0);

    // Determine which axis exists in the chart
    bool ret = chart.HasAxis(AxisType::Category, true);
    std::wcout << u"Has Primary Category Axis: " << ret << std::endl;

    ret = chart.HasAxis(AxisType::Category, false);
    std::wcout << u"Has Secondary Category Axis: " << ret << std::endl;

    ret = chart.HasAxis(AxisType::Value, true);
    std::wcout << u"Has Primary Value Axis: " << ret << std::endl;

    ret = chart.HasAxis(AxisType::Value, false);
    std::wcout << u"Has Secondary Value Axis: " << ret << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Консольный вывод, сгенерированный образцовым кодом

Консольный вывод кода показан ниже, отображающий результат true для основной категории и оси значений и false для вторичной категории и оси значений.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
