---
title: 如何使用C++设置系列不可见
linktitle: 如何设置系列不可见
description: 在Excel图表中，你可能需要将系列设置为不可见。本文介绍如何使用Aspose.Cells与C++实现。
keywords: Excel图表，系列，隐藏，已过滤。
type: docs
weight: 74
url: /zh/cpp/how-to-set-series-invisible/
---

## 如何在Excel图表中设置系列不可见

在Excel图表中，你可以右键点击图表，选择"选择数据"，在弹出窗口中，通过勾选或取消勾选系列来设置是否显示该系列。你可以下载下面的[示例文件](SeriesFiltered.xlsx)，在Excel中操作实现此功能。接下来，我们将告诉你如何使用Aspose.Cells库实现此功能。

![todo:image_alt_text](series-invisible.png)

## 如何使用Aspose.Cells设置系列不可见 

我们使用以下代码来将系列设置为不可见：

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // File path for the input and output Excel files
    U16String filePath(u"..\\Data\\01_SourceDirectory\\");

    // Open an existing Excel file
    Workbook workbook(filePath + u"SeriesFiltered.xlsx");

    // Access the charts collection of the first worksheet
    ChartCollection charts = workbook.GetWorksheets().Get(0).GetCharts();

    // Access a specific chart by name
    Chart chart = charts.Get(u"Chart 1");

    // Access filtered and non-filtered series collections
    SeriesCollection nSeriesFiltered = chart.GetFilteredNSeries();
    SeriesCollection nSeries = chart.GetNSeries();

    // Set the visibility of the first two series to be filtered
    nSeries.Get(1).SetIsFiltered(true);
    nSeries.Get(0).SetIsFiltered(true);

    // Save the modified Excel file
    workbook.Save(filePath + u"output.xlsx");

    std::cout << "Series filtered successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

你可以获取以下[输入文件](SeriesFiltered.xlsx)和[输出文件](output.xlsx)。

如下图所示，原本可见的前两个系列在输出文件中变成了隐藏。  
![todo:image_alt_text](output.png)
{{< app/cells/assistant language="cpp" >}}
