---
title: 使用 Chart.SetChartDataRange 方法与 C++ 轻松设置图表的方法
linktitle: 使用Chart.SetChartDataRange方法轻松设置图表。
description: 学习如何在 Aspose.Cells for C++ 中轻松使用 Chart.SetChartDataRange 方法设置图表。我们的指南将向您展示如何指定图表的数据范围，让您能以最少的努力创建专业且准确的图表。
keywords: Aspose.Cells for C++，图表，SetChartDataRange 方法，数据范围，专业，准确，图表。
type: docs
weight: 190
url: /zh/cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/
---

{{% alert color="primary" %}}

Aspose.Cells现在提供[**Chart.SetChartDataRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/setchartdatarange/)方法来轻松设置图表。使用此方法，您不需要分别添加系列和分类轴数据。

{{% /alert %}}

以下示例代码说明了如何使用 [**Chart.SetChartDataRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/setchartdatarange/) 方法轻松设置图表。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create new workbook
    Workbook workbook(FileFormatType::Xlsx);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add data for chart

    // Category Axis Values
    worksheet.GetCells().Get(u"A2").PutValue(u"C1");
    worksheet.GetCells().Get(u"A3").PutValue(u"C2");
    worksheet.GetCells().Get(u"A4").PutValue(u"C3");

    // First vertical series
    worksheet.GetCells().Get(u"B1").PutValue(u"T1");
    worksheet.GetCells().Get(u"B2").PutValue(6);
    worksheet.GetCells().Get(u"B3").PutValue(3);
    worksheet.GetCells().Get(u"B4").PutValue(2);

    // Second vertical series
    worksheet.GetCells().Get(u"C1").PutValue(u"T2");
    worksheet.GetCells().Get(u"C2").PutValue(7);
    worksheet.GetCells().Get(u"C3").PutValue(2);
    worksheet.GetCells().Get(u"C4").PutValue(5);

    // Third vertical series
    worksheet.GetCells().Get(u"D1").PutValue(u"T3");
    worksheet.GetCells().Get(u"D2").PutValue(8);
    worksheet.GetCells().Get(u"D3").PutValue(4);
    worksheet.GetCells().Get(u"D4").PutValue(2);

    // Create Column chart with easy way
    int32_t idx = worksheet.GetCharts().Add(ChartType::Column, 6, 5, 20, 13);
    Chart ch = worksheet.GetCharts().Get(idx);
    ch.SetChartDataRange(u"A1:D4", true);

    // Save the workbook
    U16String outputPath = u"..\\Data\\02_OutputDirectory\\output_out.xlsx";
    workbook.Save(outputPath, SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
