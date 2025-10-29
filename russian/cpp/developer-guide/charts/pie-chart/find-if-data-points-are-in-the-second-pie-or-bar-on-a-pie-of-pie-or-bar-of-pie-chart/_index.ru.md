---
title: Узнайте, как определить, находятся ли точки данных во второй части пирога или в столбце на диаграмме Pie of Pie или Bar of Pie с помощью C++
linktitle: Определите, находятся ли данные во второй круговой или столбчатой диаграмме на круговой диаграмме с обрывным или столбчатой диаграмме
description: Узнайте, как использовать Aspose.Cells for C++, чтобы определить, находятся ли точки данных во второй части пирога или в столбце на диаграмме Pie of Pie или Bar of Pie. Наше руководство покажет, как идентифицировать и получить доступ к вторичной части пирога или столбца в составной диаграмме для эффективного анализа и манипуляций данными.
keywords: Aspose.Cells for C++, Диаграмма Pie of Pie, Диаграмма Bar of Pie, Второй пирог, Второй столбец, Анализ данных, Манипуляция данными.
type: docs
weight: 180
url: /ru/cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Возможные сценарии использования**
Вы можете определить, находятся ли точки данных серии во второй части пирога на диаграмме *Pie of Pie* или в столбце на диаграмме *Bar of Pie* с помощью Aspose.Cells. Используйте свойство [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/), чтобы определить это.

Пожалуйста, загрузите [образец excel-файла](5115193.xlsx), используемый в следующем образце кода, и проверьте его вывод в консоль. Если вы откроете [образец excel-файла](5115193.xlsx), вы увидите, что все точки данных, которые меньше 10, находятся внутри столба 'Столбец на круге', как показано в выводе консоли.

## **Определение того, находятся ли точки данных во втором сегменте или в столбце на круговой из кругов или столбчатой из кругов диаграмме**
В следующем образце кода показано, как определить, находятся ли точки данных во втором сегменте или в столбце на диаграмме *Круговой из кругов* или *Столбчатая из кругов*.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"PieBars.xlsx";
    Workbook workbook(inputFilePath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Chart chart = worksheet.GetCharts().Get(0);
    chart.Calculate();

    Series series = chart.GetNSeries().Get(0);

    int pointCount = series.GetPoints().GetCount();
    for (int i = 0; i < pointCount; ++i)
    {
        ChartPoint chartPoint = series.GetPoints().Get(i);

        if (chartPoint.Get_YValue().IsNull())
            continue;

        std::cout << "Value: " << chartPoint.Get_YValue().ToDouble() << std::endl;
        std::cout << "IsInSecondaryPlot: " << (chartPoint.IsInSecondaryPlot() ? "true" : "false") << std::endl;
        std::cout << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Вывод в консоль**
Пожалуйста, посмотрите следующий вывод консоли, созданный после выполнения приведенного выше примера кода с помощью [образца файла Excel](5115193.xlsx). Если [IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/) возвращает **false**, точка данных находится внутри Пирога, а если возвращает **true**, то внутри Столбца.

{{< highlight java >}}

 Value: 15

IsInSecondaryPlot: False

Value: 9

IsInSecondaryPlot: True

Value: 2

IsInSecondaryPlot: True

Value: 40

IsInSecondaryPlot: False

Value: 5

IsInSecondaryPlot: True

Value: 4

IsInSecondaryPlot: True

Value: 25

IsInSecondaryPlot: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
