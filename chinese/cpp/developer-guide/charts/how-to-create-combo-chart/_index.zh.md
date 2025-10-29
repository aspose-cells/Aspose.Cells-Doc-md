---  
title: 如何用C++创建组合图表  
linktitle: 如何创建组合图表  
description: 了解如何使用Aspose.Cells for C++创建组合图表。我们的全面指南将演示如何将不同类型的图表组合成一个组合图表，以实现更有效的数据展示。  
keywords: Aspose.Cells for C++、组合图表、图表类型结合、数据展示、有效可视化。  
type: docs  
weight: 73  
url: /zh/cpp/create-combo-chart/  
---  

## **可能的使用场景**  
Excel中的组合图表让您能够利用此选项，因为您可以轻松地组合两种或更多种图表类型，以使您的数据易于理解。当您的数据包含多种值（包括价格和交易量）时，组合图表是有用的。此外，当您的数据数字在系列之间有明显变化时，组合图表是可行的。  


![todo:image_alt_text](sample.png)  
## **组合图表**  
运行以下代码后，您将看到下面展示的组合图表。  

![todo:image_alt_text](result.png)  
## **示例代码**  
以下示例代码加载了[示例Excel文件](combo.xlsx)并生成了[输出Excel文件](out.xlsx)。  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create the workbook
    Workbook workbook(u"combo.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a stock volume (VHLC) chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockVolumeHighLowClose, 15, 0, 34, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend to be shown
    chart.SetShowLegend(true);

    // Set the chart title
    chart.GetTitle().SetText(u"Combo Chart");

    // Set the Legend position to bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:E12", true);

    // Set category data
    chart.GetNSeries().GetCategoryData() = u"A2:A12";

    // Set the Series[1], Series[2], and Series[3] to different Marker Styles
    for (int32_t j = 0; j < chart.GetNSeries().GetCount(); j++)
    {
        switch (j)
        {
            case 1:
                chart.GetNSeries().Get(j).GetMarker().SetMarkerStyle(ChartMarkerType::Circle);
                chart.GetNSeries().Get(j).GetMarker().SetMarkerSize(15);
                chart.GetNSeries().Get(j).GetMarker().GetArea().SetFormatting(FormattingType::Custom);
                chart.GetNSeries().Get(j).GetMarker().GetArea().SetForegroundColor(Color::Pink());
                chart.GetNSeries().Get(j).GetBorder().SetIsVisible(false);
                break;
            case 2:
                chart.GetNSeries().Get(j).GetMarker().SetMarkerStyle(ChartMarkerType::Dash);
                chart.GetNSeries().Get(j).GetMarker().SetMarkerSize(15);
                chart.GetNSeries().Get(j).GetMarker().GetArea().SetFormatting(FormattingType::Custom);
                chart.GetNSeries().Get(j).GetMarker().GetArea().SetForegroundColor(Color::Orange());
                chart.GetNSeries().Get(j).GetBorder().SetIsVisible(false);
                break;
            case 3:
                chart.GetNSeries().Get(j).GetMarker().SetMarkerStyle(ChartMarkerType::Square);
                chart.GetNSeries().Get(j).GetMarker().SetMarkerSize(15);
                chart.GetNSeries().Get(j).GetMarker().GetArea().SetFormatting(FormattingType::Custom);
                chart.GetNSeries().Get(j).GetMarker().GetArea().SetForegroundColor(Color::LightBlue());
                chart.GetNSeries().Get(j).GetBorder().SetIsVisible(false);
                break;
        }
    }

    // Set the chart type for Series[0]
    chart.GetNSeries().Get(0).SetType(ChartType::Line);

    // Set style for the border of the first series
    chart.GetNSeries().Get(0).GetBorder().SetStyle(LineType::Solid);

    // Set color for the first series
    chart.GetNSeries().Get(0).GetBorder().SetColor(Color::DarkBlue());

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().SetFormatting(FormattingType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```  
{{< app/cells/assistant language="cpp" >}}
