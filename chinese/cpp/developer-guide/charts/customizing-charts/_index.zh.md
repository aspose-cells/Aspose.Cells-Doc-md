---
title: 使用 C++ 自定义图表
linktitle: 自定义图表
description: 了解如何在Aspose.Cells for C++中自定义图表。我们的指南将演示如何修改图表布局、添加和格式化数据系列、调整轴线，以及应用各种格式选项，提升图表的外观和可用性。
keywords: Aspose.Cells for C++，图表，自定义，布局，数据系列，轴线，格式，外观，可用性。
type: docs
weight: 40
url: /zh/cpp/customizing-charts/
---


## **创建自定义图表**

到目前为止，在我们讨论图表时，我们只查看了具有其标准格式设置的标准图表。我们只定义数据源，设置几个属性，然后使用默认格式设置创建图表。但Aspose.Cells API также支持创建自定义图表，允许开发人员自己设置格式。

开发人员可以使用Aspose.Cells在运行时创建自定义图表。

图表由数据系列组成。在Aspose.Cells中，每个数据系列由[**Series**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/)对象表示，而[**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)对象作为[**Series**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/)对象的集合。创建自定义图表时，开发人员可以自由选择不同类型的图表用于不同的数据系列（收集在[**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)对象中）。

下面的示例代码演示了如何创建自定义图表。在此示例中，我们将为第一个数据系列使用柱形图，为第二个系列使用折线图。结果是，我们在工作表中添加了一个柱形图，结合了一条折线图。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"A4").PutValue(110);
    worksheet.GetCells().Get(u"B1").PutValue(260);
    worksheet.GetCells().Get(u"B2").PutValue(12);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(100);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Set the chart type of 2nd NSeries to display as line chart
    chart.GetNSeries().Get(1).SetType(ChartType::Line);

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

目前，Aspose.Cells仅支持结合饼图、折线图、柱状图和堆积柱状图的自定义图表，但未来版本将支持更多图表类型。

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
