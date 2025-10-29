---
title: 用C++插入迷你图
linktitle: 迷你图
type: docs
weight: 160
url: /zh/cpp/creating-sparklines/
description: 使用Aspose.Cells结合C++为Excel创建迷你图。
---

## **插入火花线**
{{% alert color="primary" %}} 

迷你图是工作表单元格中的微型图表，提供数据的可视化表现。使用迷你图显示一系列值的趋势，例如季节性变化、经济周期，或突出最大最小值。在数据附近放置迷你图以达到最佳效果。迷你图有三种类型：线型、柱状和堆积型。

{{% /alert %}} 

使用以下示例代码，利用Aspose.Cells轻松创建一个火花线：

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

    // Create a new workbook
    Workbook book;
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Set values in cells
    sheet.GetCells().Get(u"A1").PutValue(5);
    sheet.GetCells().Get(u"B1").PutValue(2);
    sheet.GetCells().Get(u"C1").PutValue(1);
    sheet.GetCells().Get(u"D1").PutValue(3);

    // Define the CellArea
    CellArea ca;
    ca.StartColumn = 4;
    ca.EndColumn = 4;
    ca.StartRow = 0;
    ca.EndRow = 0;

    // Add a sparkline group
    int idx = sheet.GetSparklineGroups().Add(SparklineType::Line, sheet.GetName() + u"!A1:D1", false, ca);

    // Get the sparkline group
    SparklineGroup group = sheet.GetSparklineGroups().Get(idx);
    group.GetSparklines().Add(sheet.GetName() + u"!A1:D1", 0, 4);

    // Customize Sparklines
    // Create CellsColor
    CellsColor clr = book.CreateCellsColor();
    clr.SetColor(Color::Orange());
    group.SetSeriesColor(clr);

    // Set the high points to green and low points to red
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.GetHighPointColor().SetColor(Color::Green());
    group.GetLowPointColor().SetColor(Color::Red());

    // Set line weight
    group.SetLineWeight(1.0);

    // Optionally, apply a preset style
    // group.SetPresetStyle(SparklinePresetStyleType::Style10);

    // Save the workbook
    book.Save(outDir + u"output.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **高级主题**
- [使用迷你图和设置3D格式](/cells/zh/cpp/using-sparklines-and-settings-3d-format/)
{{< app/cells/assistant language="cpp" >}}
