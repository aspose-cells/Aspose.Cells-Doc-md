---
title: 使用C++将Excel图表转换为图像
linktitle: 将Excel图表转换成图像
type: docs
weight: 20
url: /zh/cpp/convert-an-excel-chart-to-image/
description: 学习如何使用Aspose.Cells结合C++将Excel图表转换为图像。
---

{{% alert color="primary" %}}

图表具有视觉吸引力，并且方便用户快速看到数据中的比较、模式和趋势。例如，不必分析工作表中的列数字，图表可以一目了然地显示销售是下降还是上升，或者实际销售与预测销售的比较。人们经常被要求以易于理解和维护的方式呈现统计和图形信息。图片可以帮助实现这一目标。

有时，应用程序或网页需要使用图表。或者可能需要在Word文档、PDF文件、PowerPoint演示文稿或其他应用程序中使用。在每种情况下，你都希望将图表呈现为图像，以便在其他地方使用。

{{% /alert %}}

## **将图表转换为图像**

在此示例中，饼图和柱状图被转换为图像。

### **将饼图转换为图像文件**

首先，在Microsoft Excel中创建一个饼图，然后使用Aspose.Cells将其转换为图像文件。该示例中的代码基于模板Microsoft Excel文件创建了一个EMF图像。

|**输出：饼图图像**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. 在Microsoft Excel中创建饼图：
   1. 在Microsoft Excel中打开一个新的工作簿。
   1. 在工作表输入一些数据。
   1. 根据数据创建饼图。
   1. 保存文件。

|**输入文件。**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

1. 下载并安装 Aspose.Cells：
   1. [下载Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp)。
   1. 在您的开发计算机上安装它。

在首次安装时，所有[Aspose](http://www.aspose.com/)组件均以评估模式运行。 评估模式没有时间限制，只会向输出文档中注入水印。

1. 创建一个项目：
   1. 启动你的C++开发环境（如Visual Studio）。
   1. 创建新的控制台应用程序。
   1. 添加对Aspose.Cells的引用。此项目使用Aspose.Cells，因此请添加对Aspose.Cells库的引用。
   1. 编写查找并转换图表的代码。 以下是组件用于完成任务的代码。 使用的代码行很少。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file which contains the pie chart.
    Workbook workbook(srcDir + u"PieChart.xlsx");

    // Get the designer chart (first chart) in the first worksheet of the workbook.
    Chart chart = workbook.GetWorksheets().Get(0).GetCharts().Get(0);

    // Convert the chart to an image file.
    chart.ToImage(srcDir + u"PieChart.out.emf", Aspose::Cells::Drawing::ImageType::Emf);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **将柱状图转换为图像文件**

首先，在Microsoft Excel中创建柱状图并转换为图像文件，如上所述。执行示例代码后，将根据模板Excel文件中的柱状图生成一个JPEG文件。

|**输出文件：柱状图图像。**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|

1. 在Microsoft Excel中创建柱状图：
   1. 在Microsoft Excel中打开一个新的工作簿。
   1. 在工作表输入一些数据。
   1. 根据数据创建柱状图。
   1. 保存文件。

|**输入文件。**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|

1. 配置项目及引用，如上所述。
1. 动态将图表转换为图像。 以下是组件用于完成任务的代码。 该代码与先前的代码类似。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file which contains the column chart.
    U16String inputFilePath = srcDir + u"ColumnChart.xlsx";
    Workbook workbook(inputFilePath);

    // Get the designer chart (first chart) in the first worksheet of the workbook.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Chart chart = worksheet.GetCharts().Get(0);

    // Convert the chart to an image file.
    U16String outputImagePath = srcDir + u"ColumnChart.out.jpeg";
    chart.ToImage(outputImagePath, ImageType::Jpeg);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
