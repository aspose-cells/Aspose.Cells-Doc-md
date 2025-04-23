---
title: 使用C++设置图表数据源
linktitle: 数据源
type: docs
weight: 10
url: /zh/cpp/data-formatting-in-charts/
description: 了解Aspose.Cells for C++支持的各种数据源。我们的指南将引导您了解不同类型的数据源，以及如何连接和从中检索数据以填充工作表。
keywords: Aspose.Cells for C++、图表、数据格式、标签、颜色、字体、外观、易用性。
---

在之前的主题中，我们已经提供了许多示例，演示如何为您的图表设置数据源。在本主题中，我们将提供有关可为图表设置的数据类型的更多详细信息。

## **设置图表数据**

使用Aspose.Cells处理图表时，有以下两种数据类型需要处理：

 - 图表数据。
 - 类别数据。

### **图表数据**

图表数据是我们用作图表数据源的数据。我们可以通过调用 [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) 对象的 [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/add/) 方法来添加包含图表数据的单元格范围。

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Excel object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(170);
    worksheet.GetCells().Get(u"A4").PutValue(300);
    worksheet.GetCells().Get(u"B1").PutValue(160);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(40);

    // Adding sample values to cells as category data
    worksheet.GetCells().Get(u"C1").PutValue(u"Q1");
    worksheet.GetCells().Get(u"C2").PutValue(u"Q2");
    worksheet.GetCells().Get(u"C3").PutValue(u"Y1");
    worksheet.GetCells().Get(u"C4").PutValue(u"Y2");

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Saving the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **分类数据**

类别数据用于标记图表数据，并且可以通过其 [**GetCategoryData()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/getcategorydata/) 属性添加到 [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) 中。下面提供了一个完整的示例，演示了如何使用图表和分类数据。执行以上示例代码后，工作表将添加一个柱状图，如下所示。

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

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(10);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(170);
    worksheet.GetCells().Get(u"A4").PutValue(200);
    worksheet.GetCells().Get(u"B1").PutValue(120);
    worksheet.GetCells().Get(u"B2").PutValue(320);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(40);

    // Add sample values to cells as category data
    worksheet.GetCells().Get(u"C1").PutValue(u"Q1");
    worksheet.GetCells().Get(u"C2").PutValue(u"Q2");
    worksheet.GetCells().Get(u"C3").PutValue(u"Y1");
    worksheet.GetCells().Get(u"C4").PutValue(u"Y2");

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Set the data source for the category data of SeriesCollection
    chart.GetNSeries().SetCategoryData(u"C1:C4");

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高级主题**
- [复制行或区域时更改图表的数据源到目标工作表](/cells/zh/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [创建动态图表](/cells/zh/cpp/create-dynamic-charts/)
- [使用 Chart.SetChartDataRange 方法设置图表的简单方法](/cells/zh/cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [查找图表系列中点的X和Y值类型](/cells/zh/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)
