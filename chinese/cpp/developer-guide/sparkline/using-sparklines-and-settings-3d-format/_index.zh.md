---
title: 使用Sparkline和3D格式设置在C++中
linktitle: 使用Sparklines和设置3D格式
type: docs
weight: 40
url: /zh/cpp/using-sparklines-and-settings-3d-format/
description: 学习如何在Excel文件中使用Aspose.Cells和C++应用sparkline和3D格式。
---

## **使用迷你图**
Microsoft Excel 2010可以以前所未有的方式分析信息。它允许用户使用新的数据分析和可视化工具跟踪和突出重要的数据趋势。 Sparklines是迷你图，可以放置在单元格内，以便您可以在同一张表格中查看数据和图表。当Sparklines被正确使用时，数据分析更快捷、更简洁。它们还提供信息的简单视图，避免了拥挤的工作表和繁忙的图表。

Aspose.Cells提供了用于操作电子表格中迷你图的API。
### **Microsoft Excel 中的迷你图**
如何在 Microsoft Excel 2010 中插入迷你图：

1. 选择要显示迷你图的单元格。为了方便查看，选择数据旁边的单元格。
1. 在功能区上单击**插入**，然后在**迷你图**组中选择**柱**。
1. 选择或输入包含源数据的工作表中的单元格范围。图表将出现。

迷你图可帮助您查看趋势，例如垒球联赛的胜负记录。迷你图甚至可以总结联赛中每支队伍整个赛季的情况。
### **使用 Aspose.Cells 创建迷你图**
开发者可以用Aspose.Cells的API创建、删除或读取sparkline（在模板文件中）。管理sparkline的类位于[Aspose.Cells.Charts](https://reference.aspose.com/cells/cpp/aspose.cells.charts/)命名空间，因此在使用这些功能之前需要导入该命名空间。

通过为给定的数据范围添加自定义图形，开发人员可以自由地向选定的单元区域添加不同类型的迷你图。

下面的示例演示了迷你图功能。该示例显示了如何：

1. 打开一个简单的模板文件。
1. 读取工作表的迷你图信息。
1. 为给定的数据范围向单元区域添加新的迷你图。
1. 将 Excel 文件保存到磁盘。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    Workbook book(inputFilePath);
    Worksheet sheet = book.GetWorksheets().Get(0);

    SparklineGroupCollection sparklineGroups = sheet.GetSparklineGroups();
    for (int i = 0; i < sparklineGroups.GetCount(); ++i)
    {
        SparklineGroup g = sparklineGroups.Get(i);
        std::cout << "sparkline group: type:" << static_cast<int>(g.GetType()) << ", sparkline items count:" << g.GetSparklines().GetCount() << std::endl;
        for (int j = 0; j < g.GetSparklines().GetCount(); ++j)
        {
            Sparkline s = g.GetSparklines().Get(j);
            std::cout << "sparkline: row:" << s.GetRow() << ", col:" << s.GetColumn() << ", dataRange:" << s.GetDataRange().ToUtf8() << std::endl;
        }
    }

    CellArea ca;
    ca.StartColumn = 4;
    ca.EndColumn = 4;
    ca.StartRow = 1;
    ca.EndRow = 7;

    int idx = sheet.GetSparklineGroups().Add(SparklineType::Column, u"Sheet1!B2:D8", false, ca);
    SparklineGroup group = sheet.GetSparklineGroups().Get(idx);

    CellsColor clr = book.CreateCellsColor();
    clr.SetColor(Color::Orange());
    group.SetSeriesColor(clr);

    book.Save(outDir + u"Book1.out.xlsx");
    std::cout << "Sparklines added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **设置 3D 格式**
您可能需要 3D 图表样式，以便可以为您的特定情景获得恰当的结果。Aspose.Cells 提供了相关的 API 来应用 Microsoft Excel 2007 的 3D 格式。

下面给出了一个完整的示例，演示如何创建图表并应用 Microsoft Excel 2007 的 3D 格式。执行示例代码后，工作表中将添加一个带有 3D 效果的柱状图。

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

    // Instantiate a new Workbook
    Workbook book;

    // Add a Data Worksheet
    Worksheet dataSheet = book.GetWorksheets().Add(u"DataSheet");

    // Add Chart Worksheet
    Worksheet sheet = book.GetWorksheets().Add(u"MyChart");

    // Put some values into the cells in the data worksheet
    dataSheet.GetCells().Get(u"B1").PutValue(1);
    dataSheet.GetCells().Get(u"B2").PutValue(2);
    dataSheet.GetCells().Get(u"B3").PutValue(3);
    dataSheet.GetCells().Get(u"A1").PutValue(u"A");
    dataSheet.GetCells().Get(u"A2").PutValue(u"B");
    dataSheet.GetCells().Get(u"A3").PutValue(u"C");

    // Define the Chart Collection
    ChartCollection charts = sheet.GetCharts();

    // Add a Column chart to the Chart Worksheet
    int chartSheetIdx = charts.Add(ChartType::Column, 5, 0, 25, 15);

    // Get the newly added Chart
    Chart chart = book.GetWorksheets().Get(2).GetCharts().Get(0);

    // Set the background/foreground color for PlotArea/ChartArea
    chart.GetPlotArea().GetArea().SetBackgroundColor(Color::White());
    chart.GetChartArea().GetArea().SetBackgroundColor(Color::White());
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::White());
    chart.GetChartArea().GetArea().SetForegroundColor(Color::White());

    // Hide the Legend
    chart.SetShowLegend(false);

    // Add Data Series for the Chart
    chart.GetNSeries().Add(u"DataSheet!B1:B3", true);

    // Specify the Category Data
    chart.GetNSeries().SetCategoryData(u"DataSheet!A1:A3");

    // Get the Data Series
    Series ser = chart.GetNSeries().Get(0);

    // Apply the 3-D formatting
    ShapePropertyCollection spPr = ser.GetShapeProperties();
    Format3D fmt3d = spPr.GetFormat3D();

    // Specify Bevel with its height/width
    Bevel bevel = fmt3d.GetTopBevel();
    bevel.SetType(BevelPresetType::Circle);
    bevel.SetHeight(2);
    bevel.SetWidth(5);

    // Specify Surface material type
    fmt3d.SetSurfaceMaterialType(PresetMaterialType::WarmMatte);

    // Specify surface lighting type
    fmt3d.SetSurfaceLightingType(LightRigType::ThreePoint);

    // Specify lighting angle
    fmt3d.SetLightingAngle(20);

    // Specify Series background/foreground and line color
    ser.GetArea().SetBackgroundColor(Color::Maroon());
    ser.GetArea().SetForegroundColor(Color::Maroon());
    ser.GetBorder().SetColor(Color::Maroon());

    // Save the Excel file
    book.Save(outDir + u"3d_format.out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
