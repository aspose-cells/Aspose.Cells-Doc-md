---
title: 用C++显示单元格范围作为数据标签
linktitle: 将单元格范围显示为数据标签
description: 学习如何在图表中使用Aspose.Cells for C++将一个单元格范围作为数据标签。我们的指南将演示如何将标签与数据源绑定并进行格式化，从而在图表中提供准确而有意义的信息。
keywords: Aspose.Cells for C++，制表，数据标签，单元格范围，数据源，格式化，准确性，有意义的信息。
type: docs
weight: 130
url: /zh/cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}

在Microsoft Excel 2013中，您可以显示用于数据标签的单元格范围。Aspose.Cells支持此功能。

{{% /alert %}}

## **复选框显示单元格范围作为数据标签**

在Microsoft Excel中显示单元格范围作为数据标签：

1. 选择系列数据标签，右键单击以打开上下文菜单。
1. 选择**格式数据标签**。标签选项会显示。
1. 选择或清除选项 **标签包含 - 来自单元格的值**。

下面的示例代码访问图表系列数据标签，并将 [**DataLabels.GetShowCellRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/getshowcellrange/) 属性设置为 **true** 以选择 **标签包含 - 来自单元格的值** 选项。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook from the source Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Check the "Label Contains - Value From Cells"
    DataLabels dataLabels = chart.GetNSeries().Get(0).GetDataLabels();
    dataLabels.SetShowCellRange(true);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
