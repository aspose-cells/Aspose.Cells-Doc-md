---
title: How to create Sunburst chart with C++
description: Learn how to create a sunburst chart in Aspose.Cells for C++, a chart that presents data in a circle. Our guide will help you set up various properties and formatting of your chart, including data labels, legends, colors, and more.
keywords: Aspose.Cells for C++, sunburst chart, create, set properties, data labels, legend, format, color, circle, data rendering.
type: docs
weight: 162
url: /cpp/creating-sunburst-chart/
---

## **Possible Usage Scenarios**
Treemap charts are good for comparing proportions within the hierarchy, however, treemap charts aren't great at showing hierarchical levels between the largest categories and each data point. A sunburst chart is a much better visual chart for showing that. The sunburst chart is ideal for displaying hierarchical data. Each level of the hierarchy is represented by one ring or circle with the innermost circle as the top of the hierarchy. A sunburst chart without any hierarchical data (one level of categories) looks similar to a doughnut chart. However, a sunburst chart with multiple levels of categories shows how the outer rings relate to the inner rings. The sunburst chart is most effective at showing how one ring is broken into its contributing pieces, while another type of hierarchical chart, the treemap chart, is ideal for comparing relative sizes.

![todo:image_alt_text](sample.png)
## **Sunburst chart**
After running the code below, you will see the Sunburst chart as shown below.

![todo:image_alt_text](result.png)
## **Sample Code**
The following sample code loads the [sample Excel file](sunburst.xlsx) and generates the [output Excel file](out.xlsx).

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