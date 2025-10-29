---
title: 用C++改变刻度标签方向
linktitle: 更改刻度标签方向
description: 了解如何在Aspose.Cells for C++中更改刻度标签的方向。我们的指南将帮助您理解如何调整轴上的刻度标签的方向，包括水平、垂直和倾斜方向。
keywords: Aspose.Cells for C++，刻度标签，方向，方向性，轴，水平，垂直，倾斜。
type: docs
weight: 170
url: /zh/cpp/change-tick-label-direction/
---

## **更改刻度标签方向**

Aspose.Cells 通过使用 [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/ticklabels/getdirectiontype/) 属性提供更改图表刻度标签方向的能力。 [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/ticklabels/getdirectiontype/) 属性接受 [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype) 枚举值。 [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype) 枚举包含以下成员：

- 水平
- 垂直
- 旋转90度
- 旋转270度
- 堆叠

以下图片对比了源文件和输出文件：

### **源文件图像**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **输出文件图像**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

以下代码片段将刻度标签方向从Rotate90更改为水平方向

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Directory source and output paths
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook and load the sample Excel file
    Workbook workbook(sourceDir + u"SampleChangeTickLabelDirection.xlsx");

    // Obtain the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Load the chart from the source worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Set the category axis tick labels direction to Horizontal
    chart.GetCategoryAxis().GetTickLabels().SetDirectionType(ChartTextDirectionType::Horizontal);

    // Output the modified workbook to a new file
    workbook.Save(outDir + u"outputChangeChartDataLableDirection.xlsx");

    std::cout << "Chart tick label direction changed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

可以从以下链接下载源文件和输出文件。

[源文件](105480221.xlsx)

[输出文件](105480223.xlsx)
{{< app/cells/assistant language="cpp" >}}
