---
title: 如何用C++创建甘特图
linktitle: 如何创建甘特图
type: docs
weight: 72
url: /zh/cpp/how-to-create-gantt-chart/
description: 学习如何使用Aspose.Cells for C++ API创建甘特图。
keywords: 用C++创建甘特图、添加甘特图、插入甘特图
---

## **什么是甘特图**

甘特图是一种条形图，显示项目时间表。它显示项目各个元素的开始和结束日期。每个任务或活动由一条条形表示，其长度对应持续时间。甘特图还显示任务之间的依赖关系，使项目管理者可以直观地看到任务的执行顺序。它在项目管理中广泛用于规划、排程和跟踪项目。

## **如何在Excel中创建甘特图**

你可以按照以下步骤在Excel中创建甘特图：
1. 添加一些用于甘特图的数据。 
<br>
<img src="00.png" width=50% />
1. 选择数据，依次点击插入 --> 图表 --> 插入柱状图或条形图 --> 堆积条形图。在示例中，是B1:B7，然后插入**堆积条**图表。
<br>
<img src="1.png" width=50% />

1. 选择图表，**选择数据** -> **添加**，设置**系列名称**和**系列值**如下。
<br>
<img src="2.png" width=50% />

1. 选择图表，编辑**横（类别）轴标签**。
<br>
<img src="3.png" width=50% />

1. **格式轴**，选择**类别逆序**以格式化Y轴。
1. 选择**蓝色系列**，设置**填充->无填充**。
1. **格式轴**，设置X轴的**最小值和最大值**（2019年5月1日：43470，2019年1月30日：43494）。
<br>
<img src="4.png" width=50% />

1. **为图表添加数据标签**，现在你将获得一个甘特图。
<br>
<img src="0.png" width=50% />


## **在Aspose.Cells中添加甘特图的方法。**
请查看以下示例代码。它加载包含一些示例数据的[示例Excel文件](sample.xlsx)，然后基于初始数据创建堆积柱状图，并设置相关属性。最后将工作簿保存为[输出XLSX](result.xlsx)。下方截图显示了由Aspose.Cells在输出Excel文件中创建的甘特图。
<br>
<img src="5.png" width=60% />

### **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create BarStacked Chart
    int32_t chartIndex = worksheet.GetCharts().Add(ChartType::BarStacked, 5, 6, 20, 15);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Set the chart title name
    chart.GetTitle().SetText(u"Gantt Chart");

    // Set the chart title visibility
    chart.GetTitle().SetIsVisible(true);

    // Set data range
    chart.SetChartDataRange(u"B1:B6", true);

    // Add series data range
    chart.GetNSeries().Add(u"C2:C6", true);

    // No fill for one series
    chart.GetNSeries().Get(0).GetArea().GetFillFormat().SetFillType(FillType::None);

    // Set the Horizontal(Category) Axis
    chart.GetNSeries().SetCategoryData(u"A2:A6");

    // Reverse the Horizontal(Category) Axis
    chart.GetCategoryAxis().SetIsPlotOrderReversed(true);

    // Set the value axis's MinValue and MaxValue
    chart.GetValueAxis().SetMinValue(worksheet.GetCells().Get(u"B2").GetValue());
    chart.GetValueAxis().SetMaxValue(worksheet.GetCells().Get(u"D6").GetValue());

    // Set the PlotArea with no fill
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Show the DataLabels
    chart.GetNSeries().Get(1).GetDataLabels().SetShowValue(true);

    // Disable the Legend
    chart.SetShowLegend(false);

    // Save the result
    workbook.Save(u"result.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{< app/cells/assistant language="cpp" >}}
