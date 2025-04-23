--- 
title: 用C++创建高低收（HLC）股票图表 
linktitle: 创建高低收（HLC）股票图表 
description: 学习如何用Aspose.Cells for C++创建高低收股票图表。我们的逐步指南将演示如何绘制股票市场数据，包括最高价、最低价和收盘价，以便进行更好的分析与可视化。 
keywords: Aspose.Cells for C++，高低收股票图表，股票市场数据，分析，可视化。 
type: docs 
weight: 181 
url: /zh/cpp/create-high-low-close-stock-chart/ 
--- 

## **可能的使用场景** 
高低收（HLC）股票图表使用四列数据。第一列通常是类别，通常是日期，但也可以使用股票名称。接下来的三列分别表示最高、最低和收盘价格。每个类别价格范围通过垂直线来表示，收盘价格则使用延伸至该线右侧的刻度线显示。 

![todo:image_alt_text](sample.png) 
## **图表的可见性改进** 
有时，为了使图表看起来更直观，我们可以修改标记（收盘价）的外观，或者在辅助轴上显示它。 

![todo:image_alt_text](sample2.png) 
## **示例代码** 
以下示例代码加载[示例Excel文件](High-Low-Close.xlsx)并生成[输出Excel文件](out.xlsx)。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close-Stock Chart
    int pieIdx = worksheet.GetCharts().Add(ChartType::StockHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:D9", true);

    // Set category data 
    chart.GetNSeries().GetCategoryData() = u"A2:A9";

    // Set the marker with the built-in data 
    chart.GetNSeries().Get(2).GetMarker().SetMarkerStyle(ChartMarkerType::Dash);
    chart.GetNSeries().Get(2).GetMarker().SetMarkerSize(20);
    chart.GetNSeries().Get(2).GetMarker().GetArea().SetFormatting(FormattingType::Custom);
    chart.GetNSeries().Get(2).GetMarker().GetArea().SetForegroundColor(Color::Maroon());

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
``` 
