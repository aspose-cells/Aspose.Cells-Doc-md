---
title: 用C++创建Sunburst图表的方法
description: 学习如何用Aspose.Cells for C++创建环状图，这是以圆圈形式呈现数据的图表。我们的指南将帮助您设置图表的各种属性和格式，包括数据标签、图例、颜色等。
keywords: Aspose.Cells for C++，环形图，创建，设置属性，数据标签，图例，格式，颜色，圆形，数据渲染。
type: docs
weight: 162
url: /zh/cpp/creating-sunburst-chart/
---

## **可能的使用场景**
树状图适合比较层级中的比例，但树状图在显示最大类别与每个数据点之间的层次级别方面并不理想。环形图是显示层级数据的更佳直观图表。环形图理想用于显示层级数据。每个层级由一个环或圆圈表示，最内圈代表层级的顶部。没有任何层级数据（仅一层类别）的环形图看起来类似于甜甜圈图。而具有多个层级的环形图则展示了外部环与内部环的关系。环形图在展示某一环被拆分成贡献部分方面最为有效，而另一类层级图形——树状图，更适合比较相对大小。

![todo:image_alt_text](sample.png)
## **旭日图表**
运行下面的代码后，您将会看到如下所示的旭日图表。

![todo:image_alt_text](result.png)
## **示例代码**
以下示例代码加载 [样本 Excel 文件](sunburst.xlsx) 并生成 [输出 Excel 文件](out.xlsx)。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"sunburst.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a Treemap chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::Sunburst, 5, 6, 25, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Sunburst Chart");

    // Add series data range
    chart.GetNSeries().Add(u"D2:D16", true);

    // Set category data (A2:A16 is incorrect, as hierarchical category)
    chart.GetNSeries().SetCategoryData(u"A2:C16");

    // Show the DataLabels with category names
    chart.GetNSeries().Get(0).GetDataLabels().SetShowCategoryName(true);

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
