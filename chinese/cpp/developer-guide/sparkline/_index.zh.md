---
title: Aspose.Cells for C++ 中的迷你图
description: Aspose.Cells 是一个用于处理电子表格文件的 C++ 库，支持创建迷你图（放置在工作表单元格内的小型图表）。本文介绍如何使用 Aspose.Cells 库添加和自定义折线、柱形和盈亏迷你图。
linktitle: 迷你图
keywords: Aspose.Cells, C++ 库, 电子表格, 迷你图, 折线迷你图, 柱形迷你图, 盈亏迷你图, SparklineGroup, SparklineType
type: docs
weight: 195
url: /zh/cpp/creating-sparklines/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持在工作表单元格内创建迷你图。迷你图是容纳在单个单元格内的小型图表，可以快速直观地呈现数据趋势。Aspose.Cells 支持折线、柱形和盈亏迷你图，并且每种迷你图都可以针对颜色、线宽、高/低点以及标记进行自定义。

## **简介**
迷你图是单元格内的小型图表，当您希望在数据行或列旁边快速显示趋势而又不占用完整图表的空间时，它们非常有用。Excel 支持三种迷你图：**折线**、**柱形**和**盈亏**。Aspose.Cells 通过位于 `Aspose.Cells.Charts` 命名空间中的 `SparklineGroup` 和 `SparklineGroupCollection` API 提供了相同的功能。
在 Aspose.Cells 中，您添加的每个迷你图都是通过 `worksheet.SparklineGroups.Add(...)` 创建的，该方法返回一个 `SparklineGroup` 对象。然后您可以使用该对象设置迷你图类型、数据区域、目标单元格以及线条颜色、线宽、标记和高/低点指示器等视觉属性。
本文将逐一介绍 Aspose.Cells 支持的三种迷你图类型——**折线**、**柱形**和**盈亏**——并演示如何添加它们、自定义颜色以及保存生成的工作簿。

## **折线迷你图**
折线迷你图在数据系列中绘制一条连续的连线，是显示随时间变化的趋势的最自然选择。在 Aspose.Cells 中，通过将 `SparklineType.Line` 传递给 `SparklineGroups.Add` 方法来创建折线迷你图。
1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 用您想要可视化的值填充一行源数据（例如第 1 行的 A 列到 E 列）。
3. 构建一个 `CellArea` 来描述将绘制迷你图的目标单元格。
4. 调用 `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`。第三个参数 `false` 告诉 Aspose.Cells 数据区域是水平方向（一行）而不是垂直方向（一列）。
5. 可选地对返回的 `SparklineGroup` 进行自定义。对于折线迷你图，您可以使用 `group.Line.Color`（该属性期望一个来自 `Aspose.Cells.Drawing` 的 `CellsColor`）设置线条颜色，调整线宽，并切换高/低点标记。
6. 保存工作簿。
以下示例创建一个工作簿，将值 5、-3、8、-2、6 写入单元格 A1 到 E1，并在单元格 F1 中添加一条追踪这些值的折线迷你图。它还将线条颜色自定义为红色，并为高/低点启用标记。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // 步骤 1：创建工作簿并获取第一个工作表
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // 步骤 2：将示例值 5、-3、8、-2、6 写入单元格 A1:E1
    cells.Get(u"A1").PutValue(5);
    cells.Get(u"B1").PutValue(-3);
    cells.Get(u"C1").PutValue(8);
    cells.Get(u"D1").PutValue(-2);
    cells.Get(u"E1").PutValue(6);
    // 步骤 3：构建一个指向目标单元格 F1 的 CellArea
    CellArea dest;
    dest.StartColumn = 5;   // F 列（从 0 开始索引）
    dest.EndColumn = 5;
    dest.StartRow = 0;      // 第 1 行（从 0 开始索引）
    dest.EndRow = 0;
    // 步骤 4：在 F1 中添加一条从 A1:E1 折线迷你图
    int index = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(index);
    // 步骤 5：创建红色 CellsColor 并将其分配给迷你图线条颜色
    CellsColor red = workbook.CreateCellsColor();
    red.SetColor(Color::Red());
    group.SetSeriesColor(red);
    // 步骤 6：启用高点和低点标记
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    // 步骤 7：保存工作簿
    workbook.Save(u"output_line.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **柱形迷你图**
柱形迷你图将每个数据点呈现为一个垂直条形。这使它非常适合数据大小具有实际意义的情况——例如每月销售额或计数。在 Aspose.Cells 中，通过将 `SparklineType.Column` 传递给 `SparklineGroups.Add` 方法来创建柱形迷你图。
其步骤与折线迷你图示例类似：
1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 构建一个 `CellArea` 来描述目标单元格。
3. 调用 `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`。
4. 可选地对生成的 `SparklineGroup` 进行自定义——例如，将 `group.Type` 设置为确认类型，或者调整条形颜色。
5. 将工作簿保存到单独的输出文件，以免覆盖折线迷你图示例。
以下示例将值 5、-3、8、-2、6 写入 A1:E1，并在 F1 中渲染柱形迷你图。负值绘制为向下的条形，正值绘制为向上的条形，这样可以一目了然地分辨出正值和负值的贡献。

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // 步骤 1：创建一个 Workbook 并获取第一个工作表
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    // 步骤 2：将示例值写入 A1:E1
    int values[5] = { 5, -3, 8, -2, 6 };
    Cells cells = worksheet.GetCells();
    for (int i = 0; i < 5; i++) {
        cells.Get(0, i).PutValue(values[i]);
    }
    // 步骤 3：构建一个指向 F1（列索引 5，行索引 0）的 CellArea
    CellArea dest;
    dest.StartColumn = 5;
    dest.EndColumn = 5;
    dest.StartRow = 0;
    dest.EndRow = 0;
    // 步骤 4：向目标单元格添加一个 Column 类型的迷你图
    int idx = worksheet.GetSparklineGroups().Add(
        SparklineType::Column, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(idx);
    // 步骤 5：通过读取 group.Type 确认迷你图的类型
    std::cout << "Sparkline Type added: " << static_cast<int>(group.GetType()) << std::endl;
    // 步骤 6：保存工作簿
    wb.Save(u"output_column.xlsx");
    std::cout << "Workbook saved as output_column.xlsx" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **盈亏迷你图**
盈亏迷你图是柱形迷你图的一种特殊变体，专为仅显示两种结果而设计：正值绘制为"向上"条形（赢），零值或负值绘制为"向下"条形（输）。盈亏迷你图通常用于可视化一系列胜负记录、通过/未通过的结果，或随时间变化的任何二元结果。
在 Aspose.Cells 中，通过将 `SparklineType.Stacked` 传递给 `SparklineGroups.Add` 方法来创建盈亏迷你图。（尽管名称如此，`SparklineType.Stacked` 是用于请求盈亏渲染的枚举值。）
1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 填充源区域。由于盈亏迷你图将每个值视为赢或输，因此值的大小并不重要——只有符号才重要。正值变为向上条形，非正值变为向下条形。
3. 构建一个 `CellArea` 来描述目标单元格。
4. 调用 `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`。
5. 可选地对返回的 `SparklineGroup` 进行自定义，例如为赢条形和输条形设置强调颜色。
6. 使用不同的文件名保存工作簿，以便所有三个示例可以共存于磁盘上。

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // 步骤 1：创建工作簿并获取第一个工作表
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"WinLoss");
    // 步骤 2：在第 1 行填充示例数据：A1=5，B1=-3，C1=8，D1=-2，E1=6
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);
    // 步骤 3：构建一个指向 F1（第 5 列，第 0 行）的 CellArea
    CellArea dest;
    dest.StartColumn = 5;   // F
    dest.EndColumn = 5;
    dest.StartRow = 0;      // 第 1 行
    dest.EndRow = 0;
    // 步骤 4：添加 Win/Loss 迷你图（SparklineType::Stacked）
    int groupIndex = worksheet.GetSparklineGroups().Add(
        SparklineType::Stacked,
        u"A1:E1",
        false,
        dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(groupIndex);
    // 步骤 5：自定义迷你图组
    // 启用高点标记和低点标记
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.SetShowNegativePoints(true);
    // 将高点颜色设置为绿色
    CellsColor highColor = workbook.CreateCellsColor();
    highColor.SetColor(Color::Green());
    group.SetHighPointColor(highColor);
    // 将低点颜色设置为红色
    CellsColor lowColor = workbook.CreateCellsColor();
    lowColor.SetColor(Color::Red());
    group.SetLowPointColor(lowColor);
    // 将负点颜色设置为橙色
    CellsColor negColor = workbook.CreateCellsColor();
    negColor.SetColor(Color::Orange());
    group.SetNegativePointsColor(negColor);
    // 设置默认系列颜色（用于正值条）
    CellsColor seriesColor = workbook.CreateCellsColor();
    seriesColor.SetColor(Color::SteelBlue());
    group.SetSeriesColor(seriesColor);
    // 步骤 6：保存工作簿
    workbook.Save(u"output_winloss.xlsx");
    std::cout << "Workbook saved successfully: output_winloss.xlsx" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **组合三种迷你图类型**
下面的组合示例创建一个工作簿，在第 1 行填充值 5、-3、8、-2、6，然后在单元格 F1、F2 和 F3 中添加三个迷你图组——每种类型一个——从而使生成的文件一次性展示所有三种迷你图样式。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // 步骤 1：创建 Workbook 并获取第一个工作表
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // 步骤 2：在第 1 行（A1:E1）填充示例数据
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);
    // 步骤 3：在 F1 处添加折线迷你图组
    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, lineArea);
    SparklineGroup lineGroup = worksheet.GetSparklineGroups().Get(lineIdx);
    // 通过 CellsColor 自定义折线迷你图的颜色
    CellsColor lineColor = workbook.CreateCellsColor();
    lineColor.SetColor(Color::Blue());
    lineGroup.SetSeriesColor(lineColor);
    // 步骤 4：在 F2 处添加柱形迷你图组
    CellArea columnArea;
    columnArea.StartColumn = 5;
    columnArea.EndColumn = 5;
    columnArea.StartRow = 1;
    columnArea.EndRow = 1;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, u"A1:E1", false, columnArea);
    SparklineGroup columnGroup = worksheet.GetSparklineGroups().Get(columnIdx);
    // 自定义柱形迷你图系列的颜色
    CellsColor columnColor = workbook.CreateCellsColor();
    columnColor.SetColor(Color::Green());
    columnGroup.SetSeriesColor(columnColor);
    // 步骤 5：在 F3 处添加胜负（堆积）迷你图组
    CellArea stackedArea;
    stackedArea.StartColumn = 5;
    stackedArea.EndColumn = 5;
    stackedArea.StartRow = 2;
    stackedArea.EndRow = 2;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, u"A1:E1", false, stackedArea);
    SparklineGroup stackedGroup = worksheet.GetSparklineGroups().Get(stackedIdx);
    // 自定义胜负迷你图系列的颜色
    CellsColor stackedColor = workbook.CreateCellsColor();
    stackedColor.SetColor(Color::FromArgb(0xFF8C00));
    stackedGroup.SetSeriesColor(stackedColor);
    // 步骤 6：保存 Workbook
    workbook.Save(u"output_all.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **自定义迷你图外观**
一旦 `SparklineGroup` 被创建并添加到 `worksheet.SparklineGroups` 中，您可以在保存工作簿之前读取或修改其多个视觉属性。最常用的自定义属性包括：
- **`group.Type`** —— `SparklineType`（Line、Column 或 Stacked）。它在添加组时设置，但您可以读回以进行确认。
- **`group.Line.Color`** —— 线条颜色，以通过 `workbook.CreateCellsColor()` 创建的 `CellsColor` 表示。这是用于折线迷你图描边颜色的属性。
- **`group.Line.Weight`** —— 以磅为单位的线宽。值越大，线条越粗。
- **高/低点标记** —— 用于在最高和最低数据点上打开小标记的标志，有助于突出极值。
- **首/尾/负值点标记** —— 用于切换第一个、最后一个和负值数据点上标记的标志。
要更改颜色，请始终创建 `CellsColor` 实例并将其分配给相关属性。不要将原始颜色值直接分配给迷你图的颜色属性——它们期望来自 `Aspose.Cells.Drawing` 的 `CellsColor` 类型。`SparklineGroups.Add` 方法本身返回一个完全类型化的 `SparklineGroup` 对象，因此您可以在返回值上链式分配属性，或者将其存储在本地变量中并在保存之前进行自定义。
{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}