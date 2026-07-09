---
title: Aspose.Cells for C++ 中的迷你图
linktitle: Sparklines
description: Aspose.Cells 是一个用于处理电子表格文件的 C++ 库，支持创建迷你图——放置在工作表单元格内的小型图表。本文介绍如何使用 Aspose.Cells 库添加和自定义折线、柱形和盈亏迷你图。
keywords: Aspose.Cells, C++ library, spreadsheet, sparklines, line sparkline, column sparkline, win/loss sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /zh/cpp/creating-sparklines/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 支持在工作表单元格内创建迷你图。迷你图是适合放在单个单元格内的小型图表，可以快速直观地展示数据趋势。Aspose.Cells 支持折线、柱形和盈亏迷你图，每种类型都可以针对颜色、线宽、高/低点以及标记进行自定义。

{{% /alert %}}

## **简介**

迷你图是单元格内的小型图表，当您希望在数据行或列旁边显示快速趋势而又不占用完整图表的空间时，它们非常有用。Excel 支持三种迷你图类型：**折线**、**柱形**和**盈亏**。Aspose.Cells 通过 `Aspose.Cells.Charts` 命名空间中的 `SparklineGroup` 和 `SparklineGroupCollection` API 提供此功能。

在 Aspose.Cells 中，您添加的每个迷你图都是通过 `worksheet.SparklineGroups.Add(...)` 创建的，该方法返回一个 `SparklineGroup` 对象。然后，您可以使用该对象设置迷你图类型、数据区域、目标单元格以及视觉属性，例如线条颜色、线宽、标记和高/低点指示器。

{{% alert color="primary" %}}

单个 `SparklineGroup` 可以包含一个或多个共享相同样式的迷你图。当您调用 `Add` 并传入一行数据以及一个目标单元格时，您将在该单元格内得到一个迷你图。如果您的目标区域宽度超过一个单元格，则会在每个目标单元格中分别绘制一个迷你图，所有这些迷你图使用相同的样式和数据区域。

{{% /alert %}}

本文将逐一介绍 Aspose.Cells 支持的三种迷你图类型——**折线**、**柱形**和**盈亏**——并展示如何添加它们、自定义颜色以及保存生成的工作簿。

## **折线迷你图**

折线迷你图通过数据点绘制一条连续的线条，是显示随时间变化趋势的最自然选择。在 Aspose.Cells 中，通过将 `SparklineType.Line` 传递给 `SparklineGroups.Add` 方法来创建折线迷你图。

工作流程与其他迷你图类型相同：

1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 在一行源数据（例如第 1 行 A 列到 E 列）中填充您要可视化的值。
3. 构建一个 `CellArea`，描述将要绘制迷你图的目标单元格。
4. 调用 `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`。第三个参数 `false` 告诉 Aspose.Cells 数据区域是水平的（一行），而不是垂直的（一列）。
5. （可选）自定义返回的 `SparklineGroup`。对于折线迷你图，您可以使用 `group.Line.Color`（它接受来自 `Aspose.Cells.Drawing` 的 `CellsColor`）设置线条颜色，调整线宽，并切换高点/低点标记。
6. 保存工作簿。

下面的示例创建一个工作簿，将值 5、-3、8、-2、6 写入单元格 A1 到 E1，并在单元格 F1 中添加一个折线迷你图来描绘这些值。它还将线条颜色自定义为红色，并启用高点和低点的标记。

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // 步骤 1：创建 Workbook 并获取第一个工作表
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
    dest.StartColumn = 5;   // 列 F（从 0 开始索引）
    dest.EndColumn = 5;
    dest.StartRow = 0;      // 行 1（从 0 开始索引）
    dest.EndRow = 0;

    // 步骤 4：从 A1:E1 向 F1 添加折线迷你图
    int index = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(index);

    // 步骤 5：创建一个红色的 CellsColor 并将其分配给迷你图线条颜色
    CellsColor red = workbook.CreateCellsColor();
    red.SetColor(Color::Red());
    group.SetSeriesColor(red);

    // 步骤 6：启用高点标记和低点标记
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);

    // 步骤 7：保存工作簿
    workbook.Save(u"output_line.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **柱形迷你图**

柱形迷你图将每个数据点渲染为垂直条形。这使得它非常适合数据大小具有实际意义的情况——例如每月销售数字或计数。在 Aspose.Cells 中，通过将 `SparklineType.Column` 传递给 `SparklineGroups.Add` 方法来创建柱形迷你图。

操作流程与折线迷你图示例相同：

1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 在相同的源区域（A1:E1）中填充您要可视化的值。
3. 构建一个 `CellArea`，描述目标单元格。
4. 调用 `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`。
5. （可选）自定义生成的 `SparklineGroup`——例如，将 `group.Type` 设置为确认类型，或调整条形颜色。
6. 将工作簿保存到单独的输出文件，以免覆盖折线迷你图示例。

下面的示例将值 5、-3、8、-2、6 写入 A1:E1，并在 F1 中渲染一个柱形迷你图。负值绘制为向下的条形，正值绘制为向上的条形，这使得正负贡献一目了然。

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // 第 1 步：创建工作簿并获取第一个工作表
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // 第 2 步：将示例值写入 A1:E1
    int values[5] = { 5, -3, 8, -2, 6 };
    Cells cells = worksheet.GetCells();
    for (int i = 0; i < 5; i++) {
        cells.Get(0, i).PutValue(values[i]);
    }

    // 第 3 步：构建一个指向 F1 的 CellArea（列索引 5，行索引 0）
    CellArea dest;
    dest.StartColumn = 5;
    dest.EndColumn = 5;
    dest.StartRow = 0;
    dest.EndRow = 0;

    // 第 4 步：在目标单元格添加一个 Column 类型迷你图
    int idx = worksheet.GetSparklineGroups().Add(
        SparklineType::Column, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(idx);

    // 第 5 步：通过读取 group.Type 确认迷你图类型
    std::cout << "Sparkline Type added: " << static_cast<int>(group.GetType()) << std::endl;

    // 第 6 步：保存工作簿
    wb.Save(u"output_column.xlsx");

    std::cout << "Workbook saved as output_column.xlsx" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **盈亏迷你图**

盈亏迷你图是柱形迷你图的一种特殊变体，仅用于显示两种结果：正值绘制为"上"条形（胜），零或负值绘制为"下"条形（负）。盈亏迷你图通常用于可视化一系列胜负、通过/未通过结果或任何随时间变化的二元结果。

在 Aspose.Cells 中，通过将 `SparklineType.Stacked` 传递给 `SparklineGroups.Add` 方法来创建盈亏迷你图。（尽管名称如此，`SparklineType.Stacked` 是用于请求盈亏渲染的枚举值。）

操作流程与其他两种类型相同：

1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 填充源区域。由于盈亏迷你图将每个值视为胜或负，值的大小并不重要——只有其符号才重要。正值变为上条形，非正值变为下条形。
3. 构建一个 `CellArea`，描述目标单元格。
4. 调用 `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`。
5. （可选）自定义返回的 `SparklineGroup`，例如为胜负条形设置强调色。
6. 使用不同的文件名保存工作簿，以便所有三个示例可以共存于磁盘上。

下面的示例使用与前两节相同的输入数据。值 5、-3、8、-2、6 被解释为胜、负、胜、负、胜——在 F1 中绘制的迷你图准确地反映了这种模式。

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

    // 步骤 2：在第 1 行填充示例数据：A1=5, B1=-3, C1=8, D1=-2, E1=6
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

    // 步骤 4：添加 Win/Loss 迷你图（SparklineType.Stacked）
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

    // 将负值点颜色设置为橙色
    CellsColor negColor = workbook.CreateCellsColor();
    negColor.SetColor(Color::Orange());
    group.SetNegativePointsColor(negColor);

    // 设置默认系列颜色（用于正值条）
    CellsColor seriesColor = workbook.CreateCellsColor();
    seriesColor.SetColor(Color::SteelBlue());
    group.SetSeriesColor(seriesColor);

    // 步骤 6：保存工作簿
    workbook.Save(u"output_winloss.xlsx");

    std::cout << "工作簿已成功保存：output_winloss.xlsx" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **组合所有三种迷你图类型**

前面的三个示例各自生成一个工作簿，以便于单独检查输出文件。然而，在实际应用中，您通常会希望并排比较多个数据系列。实现此目的最简洁的方法是将多个迷你图组放入同一个工作表中，每组呈现不同的样式。

您可以将多个 `SparklineGroup` 对象添加到同一个 `SparklineGroupCollection` 中，每个组可以针对不同的目标单元格或不同的区域。例如，您可以在 F1 放置折线迷你图，在 F2 放置柱形迷你图，在 F3 放置盈亏迷你图——全部从第 1 行的相同源数据读取——以便读者可以看到相同数字的三种不同可视化呈现。

下面的组合示例创建一个工作簿，在第 1 行填充值 5、-3、8、-2、6，然后在单元格 F1、F2 和 F3 中添加三个迷你图组——每种类型各一个——生成的文件将一次性展示所有三种迷你图样式。

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // 步骤 1：创建一个 Workbook 并获取第一个工作表
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // 步骤 2：在第 1 行 (A1:E1) 填充示例数据
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    // 步骤 3：在 F1 添加一个折线迷你图组
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

    // 步骤 4：在 F2 添加一个柱形迷你图组
    CellArea columnArea;
    columnArea.StartColumn = 5;
    columnArea.EndColumn = 5;
    columnArea.StartRow = 1;
    columnArea.EndRow = 1;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, u"A1:E1", false, columnArea);
    SparklineGroup columnGroup = worksheet.GetSparklineGroups().Get(columnIdx);

    // 自定义柱形迷你图序列的颜色
    CellsColor columnColor = workbook.CreateCellsColor();
    columnColor.SetColor(Color::Green());
    columnGroup.SetSeriesColor(columnColor);

    // 步骤 5：在 F3 添加一个盈亏（堆叠）迷你图组
    CellArea stackedArea;
    stackedArea.StartColumn = 5;
    stackedArea.EndColumn = 5;
    stackedArea.StartRow = 2;
    stackedArea.EndRow = 2;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, u"A1:E1", false, stackedArea);
    SparklineGroup stackedGroup = worksheet.GetSparklineGroups().Get(stackedIdx);

    // 自定义盈亏迷你图序列的颜色
    CellsColor stackedColor = workbook.CreateCellsColor();
    stackedColor.SetColor(Color::FromArgb(0xFF8C00));
    stackedGroup.SetSeriesColor(stackedColor);

    // 步骤 6：保存工作簿
    workbook.Save(u"output_all.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

当您在一个工作表中组合多个迷你图组时，每个组都是独立的。它们可以共享相同的源区域或使用不同的源区域，并且可以独立设置样式。这使得直接在现有工作表中构建一个小型"仪表板"的单元格内可视化变得很容易。

{{% /alert %}}

## **自定义迷你图外观**

一旦 `SparklineGroup` 被创建并添加到 `worksheet.SparklineGroups` 中，您可以在保存工作簿之前读取或修改其多个视觉属性。最常自定义的属性包括：

- **`group.Type`** — `SparklineType`（Line、Column 或 Stacked）。它在添加组时设置，但您可以读回它以进行确认。
- **`group.Line.Color`** — 线条颜色，表示为通过 `workbook.CreateCellsColor()` 创建的 `CellsColor`。这是用于折线迷你图描边颜色的属性。
- **`group.Line.Weight`** — 以磅为单位的线宽。值越大，线条越粗。
- **高/低点标记** — 开启标志以在最高和最低数据点上显示小标记，用于强调极值。
- **首/末/负点标记** — 切换标志以在第一个、最后一个和负数据点上显示标记。

要更改颜色，请始终创建 `CellsColor` 实例并将其分配给相关属性。请勿将原始颜色值直接分配给迷你图颜色属性——它们期望使用 `Aspose.Cells.Drawing` 中的 `CellsColor` 类型。`SparklineGroups.Add` 方法本身返回一个完全类型化的 `SparklineGroup` 对象，因此您可以在返回值上链式分配属性，或将其存储在局部变量中，在保存之前进行自定义。



{{< app/cells/assistant language="cpp" >}}