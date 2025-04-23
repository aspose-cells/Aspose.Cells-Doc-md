---
title: 用C++确定图表中存在的轴
description: 了解如何确定使用Aspose.Cells for C++创建的图表中存在的轴。我们的指南将帮助您理解如何识别和访问图表中的不同轴，包括类别轴、数值轴和次轴。
keywords: Aspose.Cells for C++，图表，轴，存在性，类别轴，数值轴，次轴。
type: docs
weight: 140
url: /zh/cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

有时，用户需要知道图表中是否存在特定的轴。例如，他想知道图表中是否存在次要值轴。有些图表，比如饼图，爆破饼图，饼-饼图，饼图-柱状图，3D饼图，3D爆破饼图，圆环图，爆破圆环图等，是没有轴的。

Aspose.Cells提供了[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/hasaxis/)方法来判断图表是否具有特定的轴。

{{% /alert %}}

以下示例代码演示了如何使用[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/hasaxis/)判断样本图表是否具有主类别和数值轴以及次类别和数值轴。

## 用C++判断图表中存在的轴的代码

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

## 示例代码生成的控制台输出

代码的控制台输出如下所示，显示主类别和值轴为true，次要类别和值轴为false。

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
