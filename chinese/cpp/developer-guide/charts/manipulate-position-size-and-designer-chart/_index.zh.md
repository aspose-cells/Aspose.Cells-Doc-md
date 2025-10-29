---
title: 操作位置、大小和设计图表的方法（C++）
linktitle: 操纵位置大小和设计图表
description: 学习如何使用Aspose.Cells for C++高效操作Microsoft Excel中的位置、大小和设计图表。我们的指南将演示如何调整这些属性以改善布局和可视化效果。
keywords: Aspose.Cells for C++，位置，大小，设计图表，Microsoft Excel，布局，可视化。
type: docs
weight: 45
url: /zh/cpp/manipulate-position-size-and-designer-chart/
---

## **图表位置和大小**
有时，你希望改变工作表内新建或已有图表的位置或大小。Aspose.Cells提供了[Chart.GetChartObject()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getchartobject/)属性实现此功能。你可以用其子属性调整图表的**高度**、**宽度**，或重新设置**X**、**Y**坐标。

### **控制图表的位置和大小**
要更改图表的位置（X、Y坐标）或大小（高度，宽度），请使用以下属性：

1. [Chart.GetX()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getx/)
1. [Chart.GetY()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gety/)
1. [Chart.GetHeight()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getheight/)
1. [Chart.GetWidth()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getwidth/)

以下示例解释了上述API的使用方法，它加载包含图表的现有工作簿的第一个工作表。然后使用Aspose.Cells重新调整和重新定位图表。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"chart.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"chart.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(1);

    // Load the chart from the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Resize the chart
    chart.GetChartObject().SetWidth(400);
    chart.GetChartObject().SetHeight(300);

    // Reposition the chart
    chart.GetChartObject().SetX(250);
    chart.GetChartObject().SetY(150);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Chart resized and repositioned successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **操作设计图表**
有时需要在设计模板文件中操纵或修改图表。Aspose.Cells完全支持操纵设计图表内容和元素。数据、图表内容、背景图像和格式可以准确保留。

### **在模板文件中操纵设计图表**
要在模板文件中操纵设计图表，请使用与图表相关的API。例如，您可以使用Worksheet.Charts属性获取模板文件中现有的图表集合。

#### **创建图表**
以下示例显示了如何创建金字塔图表。稍后我们将操纵此图表。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(4);
    worksheet.GetCells().Get(u"B2").PutValue(20);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    int chartIndex = worksheet.GetCharts().Add(ChartType::Pyramid, 5, 0, 15, 5);
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    chart.GetNSeries().Add(u"A1:B3", true);

    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **操作图表**
以下示例显示了如何操纵现有的图表。在此示例中，我们修改了上面创建的图表。请注意，在生成的输出中，一个数据点的日期标签已设置为“United Kingdom, 30K”。

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
    U16String inputFilePath = srcDir + u"piechart.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Open the existing file
    Workbook workbook(inputFilePath);

    // Get the designer chart in the second sheet
    Worksheet sheet = workbook.GetWorksheets().Get(1);
    Chart chart = sheet.GetCharts().Get(0);

    // Get the data labels in the data series of the third data point
    DataLabels datalabels = chart.GetNSeries().Get(0).GetPoints().Get(2).GetDataLabels();

    // Change the text of the label
    datalabels.SetText(u"Unided Kingdom, 400K ");

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Data label text updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **在设计师模板中操作折线图**
在这个例子中，我们将操作一个折线图。我们将向现有图表添加一些数据系列，并改变它们的线条颜色。

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the designer chart in the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Chart chart = worksheet.GetCharts().Get(0);

    // Add the third data series to it
    chart.GetNSeries().Add(U16String(u"{60, 80, 10}"), true);

    // Add another data series (fourth) to it
    chart.GetNSeries().Add(U16String(u"{0.3, 0.7, 1.2}"), true);

    // Plot the fourth data series on the second axis
    chart.GetNSeries().Get(3).SetPlotOnSecondAxis(true);

    // Change the Border color of the second data series
    chart.GetNSeries().Get(1).GetBorder().SetColor(Color::Green());

    // Change the Border color of the third data series
    chart.GetNSeries().Get(2).GetBorder().SetColor(Color::Red());

    // Make the second value axis visible
    chart.GetSecondValueAxis().SetIsVisible(true);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Chart modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
