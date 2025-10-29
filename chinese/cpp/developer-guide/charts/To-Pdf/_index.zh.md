---
title: 将图表导出为 PDF（C++版）
linktitle: 图表转换为PDF
description: 学习如何使用 Aspose.Cells for C++ 将图表转换为 PDF 文档。我们的指南将演示如何导出 Excel 图表并将其保存为 PDF，以便进一步分发和存档。
keywords: Aspose.Cells for C++，图表转 PDF，Microsoft Excel，PDF转换，导出，传播，存档。
type: docs
weight: 47
url: /zh/cpp/chart-to-pdf/
---

## **将图表渲染为PDF**

为了将图表渲染为 PDF 格式，Aspose.Cells API 已暴露 [**Chart::ToPdf**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/topdf/) 方法，支持将生成的 PDF 存储在磁盘路径或流中。

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

    // Obtain the reference of the newly added worksheet by passing its index to WorksheetCollection
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(4);
    worksheet.GetCells().Get(u"B2").PutValue(20);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Convert chart to PDF
    chart.ToPdf(outDir + u"chartPDF_out.pdf");

    std::cout << "Chart converted to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **使用所需的页面大小创建图表PDF**
您可以使用 Aspose.Cells 创建所需页面大小的图表 PDF，并指定图表在页面内的对齐方式，例如顶部、底部、居中、左侧、右侧等。此外，输出的图表可以在流或磁盘中生成。请查看以下示例代码，加载[示例Excel文件](64716906.xlsx)，访问工作表中的第一个图表，然后将其转换为[输出PDF](64716907.pdf)，并设置所需的页面大小。以下截图显示输出PDF中的页面大小为代码中指定的7x7，图表横竖两端对齐。

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)

## **示例代码**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load sample Excel file containing the chart
    Workbook wb(srcDir + u"sampleCreateChartPDFWithDesiredPageSize.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart ch = ws.GetCharts().Get(0);

    // Create chart pdf with desired page size
    ch.ToPdf(outDir + u"outputCreateChartPDFWithDesiredPageSize.pdf", 7, 7, PageLayoutAlignmentType::Center, PageLayoutAlignmentType::Center);

    std::cout << "Chart PDF created successfully with desired page size!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
