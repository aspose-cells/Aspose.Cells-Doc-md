---
title: 用C++筛选图表数据的三种方法。
linktitle: 过滤图表数据的三种方法
description: 了解如何使用Aspose.Cells for C++在Excel中筛选图表。我们全面的指南将演示如何应用筛选、定制图表元素，以及使用数据分析工具获取更好的洞察和做出明智的决策。
keywords: Aspose.Cells for C++，Excel中过滤图表，数据分析，决策制定，视觉化。
type: docs
weight: 2210
url: /zh/cpp/filtering-charts-in-excel/
---

{{% alert color="primary" %}}

## **1. 过滤以渲染图表的系列**

### **在Excel中，我们可以过滤掉图表中的特定系列，导致这些被过滤的系列不会显示在图表中。 原始图表显示在**图1**中。然而，当我们过滤掉**Testseries2**和**Testseries4**时，图表将会如**图2**所示。**
在Excel中，我们可以筛选出特定系列，从而在图表中隐藏那些筛选的系列。原始图表如**图1**所示。当我们筛选掉**Testseries2**和**Testseries4**后，图表将如**图2**所示。

在Aspose.Cells中，我们可以执行类似操作。对于[示例](seriesFiltered.xlsx)文件，如果要筛选掉**Testseries2**和**Testseries4**，可以执行以下代码。此外，我们会维护两个列表：一个（[GetNSeries()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getnseries/)）存储所有被选中的系列，另一个（[GetFilteredNSeries](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getfilterednseries/)）存储筛选后的系列。

请**注意**，在代码中，当我们设置**chart->GetNSeries()->Get(0)->SetIsFiltered(true);**时，第一条系列将被移除并放入[GetFilteredNSeries](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getfilterednseries/)中。接着，之前的**NSeries[1]**将变为新列表的第一项，之后的系列向后移动一位。这意味着如果随后运行**chart->GetNSeries()->Get(1)->SetIsFiltered(true);**，实际上是移除了原第三个系列。这有时会引起混淆，建议按代码操作，从后向前删除系列。

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **示例代码**
以下示例代码加载了[示例Excel文件](seriesFiltered.xlsx)。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of existing Workbook
    Workbook workbook(u"seriesFiltered.xlsx");

    // Get filtered series list
    SeriesCollection nSeriesFiltered = workbook.GetWorksheets().Get(0).GetCharts().Get(u"Chart 1").GetFilteredNSeries();

    // Get selected series list
    SeriesCollection nSeries = workbook.GetWorksheets().Get(0).GetCharts().Get(u"Chart 1").GetNSeries();

    // Should be 0
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 6
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    // Process from the end to the beginning
    nSeries.Get(1).SetIsFiltered(true);
    nSeries.Get(0).SetIsFiltered(true);

    // Should be 2
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 4
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    // Save the workbook
    workbook.Save(u"seriesFiltered-out.xlsx");

    // Reload the workbook
    workbook = Workbook(u"seriesFiltered-out.xlsx");

    // Should be 2
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 4
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **2. 过滤数据并使图表发生变化**

筛选数据是处理大量图表数据的好方法。当你筛选数据时，图表也会相应变化。需要注意的是，要确保图表始终显示在屏幕上，筛选可能会隐藏行，而图表可能位于这些隐藏行中。

![todo:image_alt_text](Figure3.png)

### **使用数据筛选器更改Excel中图表的步骤**

1. 点击数据范围内部。
2. 单击**数据**选项卡，通过单击筛选器进行筛选。 您的标题行将有下拉箭头。
3. 通过转到**插入**选项卡并选择列图表来创建图表。
4. 现在使用数据中的下拉箭头筛选您的数据。 不要使用图表筛选器。

### **示例代码**
以下示例代码展示了使用Aspose.Cells实现相同功能。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Get the First sheet.
    Worksheet sheet = workbook.GetWorksheets().Get(u"Sheet1");

    // Add data into details cells.
    sheet.GetCells().Get(0, 0).PutValue(u"Fruits Name");
    sheet.GetCells().Get(0, 1).PutValue(u"Fruits Price");
    sheet.GetCells().Get(1, 0).PutValue(u"Apples");
    sheet.GetCells().Get(2, 0).PutValue(u"Bananas");
    sheet.GetCells().Get(3, 0).PutValue(u"Grapes");
    sheet.GetCells().Get(4, 0).PutValue(u"Oranges");
    sheet.GetCells().Get(1, 1).PutValue(5);
    sheet.GetCells().Get(2, 1).PutValue(2);
    sheet.GetCells().Get(3, 1).PutValue(1);
    sheet.GetCells().Get(4, 1).PutValue(4);

    // Add a chart to the worksheet
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 7, 7, 15, 15);

    // Access the instance of the newly added chart
    Chart chart = sheet.GetCharts().Get(chartIndex);

    // Set data range
    chart.SetChartDataRange(u"A1:B5", true);

    // Set AutoFilter range
    sheet.GetAutoFilter().SetRange(u"A1:B5");

    // Add filters for a filter column.
    sheet.GetAutoFilter().AddFilter(0, u"Bananas");
    sheet.GetAutoFilter().AddFilter(0, u"Oranges");

    // Apply the filters
    sheet.GetAutoFilter().Refresh();

    // Save the chart as an image
    chart.ToImage(u"Autofilter.png");

    // Save the workbook
    workbook.Save(u"Autofilter.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **3. 使用表格过滤数据并使图表发生变化**

使用表格类似于方法2，使用范围，但表格比范围有优势。当您将范围更改为表格并添加数据时，图表会自动更新。使用范围时，您将不得不更改数据源。

### **在Excel中格式化为表格**

单击数据内部并使用**CTRL + T**或使用主页选项卡，**格式为表格**

![todo:image_alt_text](Figure4.png)

### **示例代码**
以下示例代码加载了[示例Excel文件](TableFilters.xlsx)，展示了使用Aspose.Cells实现相同功能。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Tables;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook
    Workbook workbook(u"TableFilters.xlsx");

    // Access first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the instance of the newly added chart
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 7, 7, 15, 15);
    Chart chart = sheet.GetCharts().Get(chartIndex);

    // Set data range
    chart.SetChartDataRange(u"A1:B7", true);

    // Convert the chart to image
    chart.ToImage(u"TableFilters.before.png");

    // Add a new List Object to the worksheet
    ListObject listObject = sheet.GetListObjects().Get(sheet.GetListObjects().Add(u"A1", u"B7", true));

    // Add default style to the table
    listObject.SetTableStyleType(TableStyleType::TableStyleMedium10);

    // Show Total
    listObject.SetShowTotals(false);

    // Add filters for a filter column
    listObject.GetAutoFilter().AddFilter(0, u"James");

    // Apply the filters
    listObject.GetAutoFilter().Refresh();

    // After adding new value the chart will change
    listObject.PutCellValue(7, 0, Object(u"Me"));
    listObject.PutCellValue(7, 1, Object(1000));

    // Check the changed images
    chart.ToImage(u"TableFilters.after.png");

    // Saving the Excel file
    workbook.Save(u"TableFilter.out.xlsx");

    Aspose::Cells::Cleanup();
}
```
