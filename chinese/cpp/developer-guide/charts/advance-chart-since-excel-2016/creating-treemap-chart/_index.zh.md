---
title: 用C++创建TreeMap图表的方法
description: 学习如何用Aspose.Cells for C++创建Treemap图表。我们的指南将帮助您了解有关Treemap图表的各种属性和格式选项，包括颜色、标签和数据表示。
keywords: Aspose.Cells for C++，Treemap图表，创建，属性，格式，颜色，标签，数据表示，环形图，层级图
type: docs
weight: 161
url: /zh/cpp/creating-treemap-chart/
---

## **可能的使用场景**
树状图表提供了数据的分级视图，可轻松找出模式，比如哪些项目是商店的畅销品。树的分支由矩形代表，每个子分支显示为较小的矩形。树状图表通过颜色和临近性显示类别，并且可以轻松显示大量数据，这在其他图表类型中可能会很困难。

![todo:image_alt_text](sample.png)
## **树状图表**
运行下面的代码后，您将会看到如下所示的树状图表。

![todo:image_alt_text](result.png)
## **示例代码**
以下示例代码加载 [样本 Excel 文件](treemap.xlsx) 并生成 [输出 Excel 文件](out.xlsx)。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"treemap.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a Treemap chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::Treemap, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"TreeMap Chart");

    // Add series data range (D2:F13, actually)
    chart.GetNSeries().Add(u"D2:F13", true);

    // Set category data (A2:C13 is incorrect)
    chart.GetNSeries().SetCategoryData(u"A2:C13");

    // Show the DataLabels with category names
    chart.GetNSeries().Get(0).GetDataLabels().SetShowCategoryName(true);

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
