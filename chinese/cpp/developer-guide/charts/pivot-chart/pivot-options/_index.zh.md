---
title: 在 C++ 中如何用 PivotOptions 管理数据透视图
linktitle: 数据透视表选项
type: docs
weight: 10
url: /zh/cpp/how-to-manage-pivotchart-with-pivotoptions/
description: 使用 C++ 管理带有 PivotOptions 的数据透视图的方法。
keywords: 数据透视图
---

## 什么是数据透视图

Excel中的数据透视图是从数据透视表中创建的数据的图形表示。它允许用户通过以图表形式汇总和显示信息来动态可视化和分析数据。数据透视图是交互式的，可以轻松修改以显示数据的不同视角，因此是Excel中数据分析和演示的强大工具。

## 如何使用数据透视表选项管理数据透视图

通过使用Aspose.Cells，您可以使用[**PivotOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/pivotoptions/)来管理数据透视图。

样本文件和代码：  
[样本文件](Sample.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path for the sample Excel file
    U16String path = u"..\\Data\\01_SourceDirectory\\";

    // Create a Workbook object from the sample file
    Workbook book(path + u"Sample.xlsx");

    // Get the first chart from the first worksheet
    Chart chart = book.GetWorksheets().Get(0).GetCharts().Get(0);

    // Get the PivotOptions from the chart
    PivotOptions opt = chart.GetPivotOptions();

    // Hide ZoneFilter in PivotChart
    opt.SetDropZoneFilter(false); // HideZoneFilter

    // You can set more properties, try them!
    // opt.SetDropZoneCategories(false);  // HideZoneCategories
    // opt.SetDropZoneData(false);        // HideZoneData
    // opt.SetDropZoneSeries(false);      // HideZoneSeries
    // opt.SetDropZonesVisible(false);    // Hide All

    // Save the modified file to see the effect
    book.Save(path + u"HideZoneFilter.xlsx");

    std::cout << "Pivot chart updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

通过上面的示例代码，您可以查看以下效果的结果文件，如下图所示：

**![输出](Output.png)**
