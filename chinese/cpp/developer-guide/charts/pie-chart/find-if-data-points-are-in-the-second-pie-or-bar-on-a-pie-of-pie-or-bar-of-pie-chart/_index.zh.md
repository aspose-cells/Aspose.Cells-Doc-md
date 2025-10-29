---
title: 用 C++ 判断数据点是否位于饼图中的第二个饼或条形图中的条上
linktitle: 查找数据点是否在饼图的第二个饼图或柱状图的柱状图上
description: 学习如何使用 Aspose.Cells for C++ 判断数据点是否位于饼图中的第二个饼或条形图中的条上。我们的指南将演示如何识别和访问复合图表中的次级饼或条，以便有效分析和操作数据。
keywords: Aspose.Cells for C++，饼中饼图，条形饼图，次级饼，次级条，数据分析，数据操作。
type: docs
weight: 180
url: /zh/cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **可能的使用场景**
你可以使用 Aspose.Cells 判断系列的数据点是否在 *Pie of Pie* 图表的第二个饼或 *Bar of Pie* 图表的条中。请使用 [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/) 属性判断。

请下载以下示例代码中使用的[样本excel文件](5115193.xlsx)，并查看其控制台输出。如果您打开[样本excel文件](5115193.xlsx)，您会发现所有小于10的数据点都在*饼图的柱状图*中，正如控制台输出所示。

## **查找数据点是否在饼图的第二个饼图或柱状图的柱状图上**
以下示例代码显示了如何查看数据点是否在*饼图*的第二个饼图上，或者在*柱状图*的柱状图上。

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

## **控制台输出**
请查看在执行上述示例代码后生成的控制台输出（包含[示例Excel文件](5115193.xlsx)）。如果 [IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/) 为 **false**，则数据点位于饼图内部；若为 **true**，则数据点位于条中。

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
