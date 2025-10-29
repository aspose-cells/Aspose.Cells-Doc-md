---
title: 禁用 C++ 中图表的数据标签换行
linktitle: 禁用数据标签换行
description: 学习如何在 Aspose.Cells for C++ 中禁用图表数据标签的换行。我们的指南将向您展示如何防止长标签重叠，并提供更清晰、更易读的图表显示。
keywords: Aspose.Cells for C++，图表，数据标签，换行，重叠，可读性，显示。
type: docs
weight: 70
url: /zh/cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013允许用户在图表的数据标签中换行或取消换行。默认情况下，图表的数据标签中的文字是处于换行状态。

Aspose.Cells提供了一个[**DataLabels.IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/istextwrapped/)属性，您可以设置为True或False以分别启用或禁用数据标签的文字换行。

{{% /alert %}}

下面的代码示例显示了如何禁用图表数据标签的文字换行。

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
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Output_out.xlsx";

    // Load the sample Excel file inside the workbook object
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Disable the Text Wrapping of Data Labels in all Series
    chart.GetNSeries().Get(0).GetDataLabels().SetIsTextWrapped(false);
    chart.GetNSeries().Get(1).GetDataLabels().SetIsTextWrapped(false);
    chart.GetNSeries().Get(2).GetDataLabels().SetIsTextWrapped(false);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Text wrapping disabled successfully in data labels!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
