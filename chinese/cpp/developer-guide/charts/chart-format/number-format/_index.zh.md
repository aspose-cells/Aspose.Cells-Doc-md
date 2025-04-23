---
title: 用C++设置图表系列的值格式代码
linktitle: 数字格式
type: docs
weight: 100
url: /zh/cpp/set-the-values-format-code-of-chart-series/
description: 学习如何在Aspose.Cells for C++中设置图表系列的值格式代码。我们的指南将帮助您理解如何使用适当的格式代码格式化图表系列数据，以便准确专业地呈现您的数据。
keywords: Aspose.Cells for C++，图表系列，值格式代码，格式，数据展示，准确性，专业性。
---

## **可能的使用场景**
您可以使用[Series.GetValuesFormatCode()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getvaluesformatcode/)属性设置图表系列的值格式代码。此属性不仅适用于基于工作表范围的系列，还适用于用值数组创建的系列。

## **设置图表系列的值格式代码**
以下示例代码在之前没有系列的空图表中添加一个系列。它使用值数组添加系列，然后用代码`$#,##0`格式化，`10000`变成`$10,000`。截图显示了代码在[示例Excel文件](51740712.xlsx)和[输出Excel文件](51740713.xlsx)运行后的效果。

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **示例代码**
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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"51740712.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"51740713.xlsx";

    // Load the source Excel file
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Access first chart
    Chart ch = worksheet.GetCharts().Get(0);

    // Add series using an array of values
    ch.GetNSeries().Add(U16String(u"{10000, 20000, 30000, 40000}"), true);

    // Access the series and set its values format code
    Series srs = ch.GetNSeries().Get(0);
    srs.SetValuesFormatCode(U16String(u"$#,##0"));

    // Save the output Excel file
    wb.Save(outputFilePath);

    std::cout << "Chart series added and formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
