---
title: 用C++设置点为总数的方法。
linktitle: 设置点为总数的方法。
description: 在某些Excel图表中，例如瀑布图，可能需要将点设为总数。本文介绍如何用C++与Aspose.Cells实现此功能。
keywords: 水平瀑布图，点，设为总和。
type: docs
weight: 72
url: /zh/cpp/how-to-set-point-as-total/
---

## Excel图表中的"设为总和"是什么意思

在一些Excel图表中，例如瀑布图，某些点的数据是前面所有点的总和，你可能需要"设为总和"。我们会展示示例代码和说明。

## 瀑布图需要将点设为"总和" 

![todo:image_alt_text](set-as-total1.png)

此图显示了Excel中的瀑布图。我们可以看到有四个以"总和"开头的数据点，它们用于计算之前所有数据点的总和。
在此图中，设置并不完全正确，当我们选择"2024年总和"点时，可以看到Excel中"设为总和"选项没有被勾选。
下方附有需要修改的 [示例Excel文件](SampleSheet.xlsx)，我们将使用Aspose.Cells来正确设置它。

## 使用Aspose.Cells将点设为"总和" 

我们使用以下代码来正确设置文件：

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

你可以得到以下正确的[输出文件](output.xlsx)

如下图所示，四个"总和"数据点已正确设置，你可以看到与之前图表的区别。

![todo:image_alt_text](set-as-total2.png)
