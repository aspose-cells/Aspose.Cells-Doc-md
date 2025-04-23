---
title: 如何使用C++创建龙卷风图
linktitle: 创建龙卷风图
type: docs
weight: 73
url: /zh/cpp/create-tornado-chart/
description: 了解如何使用API Aspose.Cells for C++创建龙卷风图。
keywords: 用C++创建龙卷风图，添加龙卷风图，插入龙卷风图。
---

## **介绍**
龙卷风图表，也称为龙卷风图或龙卷风图，是一种常用于Excel中的敏感性分析的数据可视化类型。它帮助您理解变量变化对特定结果或结果的影响。

## **如何在Excel中创建龙卷风图表**
您可以通过以下步骤在Excel中创建龙卷风图表：
1. 选择数据并转到插入 --> 图表 --> 插入柱状图或条形图 --> 堆积柱状图。点击。
<br>
<img src="1.png" width=70% />
2. 更改Y轴：右键单击Y轴。点击格式轴。在标签中，点击标签位置下拉菜单并选择低项。
<br>
<img src="2.png" width=70% />
3. 选择任何柱并进行格式设置。设置适当的间距宽度。
<br>
<img src="3.png" width=70% />
4. 让我们从龙卷风图表中删除减号（-）。选择X轴。转到格式设置。在轴选项中，点击数字。在类别中，选择自定义。在格式代码中写入###0,###0。点击添加。
<br>
<img src="4.png" width=70% />
5. 点击Y轴，进入轴设置。在轴设置中，选中逆序类别。
<br>
<img src="5.png" width=70% />

## **如何在Aspose.Cells中添加龙卷风图表**
请参阅以下示例代码。它加载包含一些示例数据的[示例Excel文件](sample.xlsx)。然后根据初始数据创建堆叠条形图表，并设置相关属性。最后，将工作簿保存到[输出XLSX格式](out.xlsx)。以下截图显示了Aspose.Cells在输出Excel文件中创建的龙卷风图表。
<br>
<img src="6.png" width=70% />

### **示例代码**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Get the chart collection from the worksheet
    ChartCollection charts = sheet.GetCharts();

    // Add a bar chart
    int index = charts.Add(ChartType::BarStacked, 8, 1, 24, 8);
    Chart chart = charts.Get(index);

    // Set data for the bar chart
    chart.SetChartDataRange(u"A1:C7", true);

    // Set properties for the bar chart
    chart.GetTitle().SetText(u"Tornado chart");
    chart.SetStyle(2);
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::White());
    chart.GetPlotArea().GetBorder().SetColor(Color::White());
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set properties for the category axis
    chart.GetCategoryAxis().SetTickLabelPosition(TickLabelPositionType::Low);
    chart.GetCategoryAxis().SetIsPlotOrderReversed(true);

    // Set gap width
    chart.SetGapWidth(10);

    // Set properties for the value axis
    Axis valueAxis = chart.GetValueAxis();
    valueAxis.GetTickLabels().SetNumberFormat(u"#,##0;#,##0");

    // Save the workbook
    wb.Save(outputFilePath);

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
