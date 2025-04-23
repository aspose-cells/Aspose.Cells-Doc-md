---
title: 像Microsoft Excel一样处理图表轴的自动单位（使用C++）
linktitle: 处理图表轴的自动单位
description: 了解如何在Aspose.Cells for C++中处理图表轴上的自动单位，类似于Microsoft Excel。我们的指南将展示如何配置和自定义图表轴的自动单位，包括科学计数法的显示和比例调整。
keywords: Aspose.Cells for C++，图表轴，自动单位，Microsoft Excel，配置，自定义，科学计数法，比例。
type: docs
weight: 120
url: /zh/cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/
---

## **可能的使用场景**
早期版本的Aspose.Cells无法在将图表渲染为图像或PDF时正确处理图表轴的自动单位。现在，Aspose.Cells支持处理图表轴的自动单位。无需更改代码。只需将图表转换为图像或PDF，它将渲染图表轴，就像Microsoft Excel渲染它一样。

## **处理Microsoft Excel的图表轴的自动单位**
以下示例代码加载了[示例Excel文件](61767755.xlsx)并生成了[输出PDF图表](61767752.pdf)。屏幕截图显示了图表轴上的自动单位，在红色矩形中，还比较了示例Excel文件中的图表与输出PDF图表，两者完全相似。

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)

## **示例代码**
```c++
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

    // Load the sample Excel file
    U16String inputFilePath = srcDir + u"sampleHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet ws = worksheets.Get(0);

    // Access first chart
    ChartCollection charts = ws.GetCharts();
    Chart ch = charts.Get(0);

    // Render chart to PDF
    U16String outputFilePath = outDir + u"outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf";
    ch.ToPdf(outputFilePath);

    std::cout << "Chart rendered to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
