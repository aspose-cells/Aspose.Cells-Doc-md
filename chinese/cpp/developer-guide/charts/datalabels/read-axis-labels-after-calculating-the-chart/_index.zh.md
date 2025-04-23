---
title: 在 C++ 中计算完图表后读取坐标轴标签
linktitle: 在计算图表后读取轴标签
description: 了解如何在 Aspose.Cells for C++ 中在计算图表后读取坐标轴标签。我们的指南将向您展示如何访问和检索坐标轴标签，包括它们的格式和位置。
keywords: Aspose.Cells for C++，图表，坐标轴标签，计算，读取，访问，检索，格式，位置。
type: docs
weight: 90
url: /zh/cpp/read-axis-labels-after-calculating-the-chart/
---

## **可能的使用场景**

您可以使用[**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/)方法在计算图表的值后读取其轴标签。请使用[**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/getaxistexts/)方法，它将返回轴标签的列表。

## **计算图表后读取轴标签**

请参阅以下示例代码，加载[sample Excel file]（ReadAxisLabels.xlsx）并读取第一个工作表中图表的类别轴标签。然后在控制台上打印轴标签的值。请参阅下面的示例代码的控制台输出进行参考。

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook wb(srcDir + u"ReadAxisLabels.xlsx");

    Worksheet ws = wb.GetWorksheets().Get(0);

    Chart ch = ws.GetCharts().Get(0);

    ch.Calculate();

    Vector<U16String> lstLabels = ch.GetCategoryAxis().GetAxisTexts();

    std::wcout << L"Category Axis Labels: " << std::endl;
    std::wcout << L"---------------------" << std::endl;

    for (int32_t i = 0; i < lstLabels.GetLength(); ++i)
    {
        std::wcout << reinterpret_cast<const wchar_t*>(lstLabels[i].GetData()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **控制台输出**

{{< highlight cpp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
