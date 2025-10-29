---
title: 用C++设置图例项填充为无色
linktitle: 设置图例项填充为无色
description: 学习如何用Aspose.Cells for C++将图例项填充设置为无色。我们的指南将演示如何修改Microsoft Excel图表中图例项的填充色，以实现更好的可视化和自定义。
keywords: Aspose.Cells for C++，图例项填充，Microsoft Excel，可视化，定制。
type: docs
weight: 320
url: /zh/cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

如果您想设置图表图例条目填充的文本为无色，以便它不会显示在图例中，请将[**LegendEntry.IsTextNoFill**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legendentry/istextnofill/)设置为**true**。

{{% /alert %}}

以下示例代码将图表的第二个图例条目填充的文本设置为无色。请下载这段代码中使用的[sample excel file](5115219.xlsx)和由此生成的[output excel file](5115217.xlsx)进行参考。

以下屏幕截图突出显示了此代码对[sample excel file](5115219.xlsx)的影响。

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

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
    U16String inputFilePath = srcDir + u"Sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"ChartLegendEntry_out.xlsx";

    // Open the template file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the sheet
    Chart chart = sheet.GetCharts().Get(0);

    // Set text of second legend entry fill to none
    chart.GetLegend().GetLegendEntries().Get(1).SetIsTextNoFill(true);

    // Save the workbook in xlsx format
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Chart legend entry modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
