---
title: 使用C++为图表点添加富文本自定义数据标签
description: 了解如何在Aspose.Cells for C++中为图表点添加富文本自定义数据标签。我们的指南将展示如何使用不同的字体、颜色和对齐选项来格式化标签，提升图表的外观和易读性。
keywords: Aspose.Cells for C++，制表，富文本，自定义数据标签，字体，颜色，对齐，外观，易读性。
type: docs
weight: 10
url: /zh/cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

你可以使用Aspose.Cells创建图表点的富文本自定义数据标签。Aspose.Cells提供[DataLabels.Characters()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/characters/)方法返回[FontSetting](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/)对象，可以用于设置文本的字体属性，比如颜色、粗细等。

{{% /alert %}}

## 数据点的图表富文本自定义数据标签

以下代码访问第一个系列的第一个图表点，设置其文本，然后设置前十个字符的字体，将其颜色设为红色，粗体设为**true**。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a workbook from source Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the sheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Access the data label of first series first point
    DataLabels dlbls = chart.GetNSeries().Get(0).GetPoints().Get(0).GetDataLabels();

    // Set data label text
    dlbls.SetText(u"Rich Text Label");

    // Set the font setting of the first 10 characters
    FontSetting fntSetting = dlbls.Characters(0, 10);
    fntSetting.GetFont().SetColor(Color::Red());
    fntSetting.GetFont().SetIsBold(true);

    // Save the workbook
    workbook.Save(srcDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
