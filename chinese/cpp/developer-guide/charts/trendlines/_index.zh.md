---
title: 获取图表趋势线的方程文本（C++版）
linktitle: 趋势线
description: 学习如何使用 Aspose.Cells for C++ 获取 Microsoft Excel 中创建的图表趋势线的方程文本。我们的指南将演示如何访问和提取趋势线的方程以进行后续分析或显示。
keywords: Aspose.Cells for C++，图表趋势线，方程文本，Microsoft Excel，数据分析，显示。
type: docs
weight: 110
url: /zh/cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

您可以使用Aspose.Cells检索图表趋势线的方程文本。Aspose.Cells提供了[**Trendline.GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/gettext/)属性，该属性返回图表趋势线的方程文本。要使用此属性，您首先必须调用[**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/)方法。

{{% /alert %}}

以下截图显示带有趋势线的图表及其方程文本（红色显示）。我们将在下面的示例代码中使用 [**Trendline.GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/gettext/) 属性检索这段文本。

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## 获取图表趋势线方程文本的 C++ 代码

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

## 示例代码生成的输出

这是上述示例代码的控制台输出。

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
