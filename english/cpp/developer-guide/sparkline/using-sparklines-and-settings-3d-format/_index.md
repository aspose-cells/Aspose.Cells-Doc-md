---
title: Using Sparklines and Settings 3D Format with C++
linktitle: Using Sparklines and Settings 3D Format
type: docs
weight: 40
url: /cpp/using-sparklines-and-settings-3d-format/
description: Learn how to use sparklines and apply 3D formatting in Excel files using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Using Sparklines**
Microsoft Excel 2010 can analyze information in more ways than ever before. It allows users to track and highlight important data trends with new data analysis and visualization tools. Sparklines are mini‑charts that you can place inside cells so that you can view data and a chart on the same table. When sparklines are used properly, data analysis is quicker and more to the point. They also provide a simple view of information, avoiding overcrowded worksheets with a lot of busy charts.

Aspose.Cells provides an API for manipulating sparklines in spreadsheets.
### **Sparklines in Microsoft Excel**
To insert sparklines in Microsoft Excel 2010:

1. Select the cells where you want the sparklines to appear. To make them easy to view, select cells at the side of the data.  
2. Click **Insert** on the ribbon and then choose **Column** in the **Sparklines** group.  
3. Select or enter the range of cells in the worksheet that contain the source data. The charts will appear.  

Sparklines help you to see trends, for example, the win or loss record for a softball league. Sparklines can even sum up the entire season of each team in the league.
### **Sparklines using Aspose.Cells**
Developers can create, delete, or read sparklines (in the template file) using the API provided by Aspose.Cells. The classes that manage sparklines are contained in the [Aspose.Cells.Charts](https://reference.aspose.com/cells/cpp/aspose.cells.charts/) namespace, so you need to import this namespace before using these features.

By adding custom graphics for a given data range, developers have the freedom to add different types of tiny charts to selected cell areas.

The example below demonstrates the Sparklines feature. The example shows how to:

1. Open a simple template file.  
2. Read sparklines information for a worksheet.  
3. Add new sparklines for a given data range to a cell area.  
4. Save the Excel file to disk.  

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

## **Setting 3D Format**
You might need 3D charting styles to obtain the results required for your scenario. Aspose.Cells provides the relevant API to apply Microsoft Excel 2007 3D formatting.

A complete example is given below to demonstrate how to create a chart and apply Microsoft Excel 2007 3D formatting. After executing the example code, a column chart (with 3D effects) will be added to the worksheet.

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

    // Apply the 3‑D formatting
    ShapePropertyCollection spPr = ser.GetShapeProperties();
    Format3D fmt3d = spPr.GetFormat3D();

    // Specify bevel with its height/width
    Bevel bevel = fmt3d.GetTopBevel();
    bevel.SetType(BevelPresetType::Circle);
    bevel.SetHeight(2);
    bevel.SetWidth(5);

    // Specify surface material type
    fmt3d.SetSurfaceMaterialType(PresetMaterialType::WarmMatte);

    // Specify surface lighting type
    fmt3d.SetSurfaceLightingType(LightRigType::ThreePoint);

    // Specify lighting angle
    fmt3d.SetLightingAngle(20);

    // Specify series background/foreground and line color
    ser.GetArea().SetBackgroundColor(Color::Maroon());
    ser.GetArea().SetForegroundColor(Color::Maroon());
    ser.GetBorder().SetColor(Color::Maroon());

    // Save the Excel file
    book.Save(outDir + u"3d_format.out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
