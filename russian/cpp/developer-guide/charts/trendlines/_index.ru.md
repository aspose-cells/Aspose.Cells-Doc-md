---
title: Получить текст уравнения трендовой линии диаграммы с помощью C++
linktitle: Трендовые линии
description: Узнайте, как использовать Aspose.Cells for C++ для получения текста уравнения трендовой линии в диаграмме, созданной в Microsoft Excel. Наше руководство покажет, как получить и извлечь уравнение трендовой линии для дальнейшего анализа или отображения.
keywords: Aspose.Cells for C++, Трендовая линия диаграммы, Текст уравнения, Microsoft Excel, Анализ данных, Отображение.
type: docs
weight: 110
url: /ru/cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Вы можете получить текст уравнения трендовой линии диаграммы с помощью Aspose.Cells. Aspose.Cells предоставляет свойство [**Trendline.GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/gettext/), которое возвращает текст уравнения трендовой линии диаграммы. Для использования этого свойства сначала нужно вызвать метод [**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/).

{{% /alert %}}

Следующий скриншот показывает диаграмму с трендлайном и его текст уравнения, выделенный красным цветом. Мы получим этот текст, используя свойство [**Trendline.GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/gettext/) в следующем примере.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## C++ код для получения текста уравнения трендовой линии диаграммы

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

    // Create workbook object from source Excel file
    Workbook workbook(srcDir + u"source.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Calculate the Chart first to get the Equation Text of Trendline
    chart.Calculate();

    // Access the Trendline
    Trendline trendLine = chart.GetNSeries().Get(0).GetTrendLines().Get(0);

    // Read the Equation Text of Trendline
    std::cout << "Equation Text: " << trendLine.GetDataLabels().GetText().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Вывод, созданный образцовым кодом

Это вывод консоли вышеуказанного образца кода.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
