---
title: Aspose.Cells for .NET 中的迷你图
linktitle: Aspose.Cells for .NET 中的迷你图
description: Aspose.Cells 是一个用于处理电子表格文件的 .NET 库，支持创建迷你图——即放置在工作表单元格内的微型图表。本文介绍如何使用 Aspose.Cells 库添加和自定义折线、柱形及盈亏迷你图。
keywords: Aspose.Cells, .NET 库, 电子表格, 迷你图, 折线迷你图, 柱形迷你图, 盈亏迷你图, SparklineGroup, SparklineType
type: docs
weight: 195
url: /zh/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持在工作表单元格内创建迷你图。迷你图是置于单个单元格内的小型图表，可快速、直观地呈现数据趋势。Aspose.Cells 支持折线、柱形和盈亏迷你图，每种迷你图均可自定义颜色、线宽、最高/最低点和标记。
{{% /alert %}}

## **简介**
迷你图是单元格内的小型图表，适合在一行或一列数据旁快速显示趋势，同时无需占用完整图表的空间。Excel 支持三种迷你图：**折线**、**柱形**和**盈亏**。Aspose.Cells 通过 `Aspose.Cells.Charts` 命名空间中的 `SparklineGroup` 和 `SparklineGroupCollection` API 提供相应功能。
在 Aspose.Cells 中，您添加的每个迷你图都通过 `worksheet.SparklineGroups.Add(...)` 创建，该方法返回一个 `SparklineGroup` 对象。然后，您可以使用该对象设置迷你图类型、数据区域、目标单元格以及可视化属性，例如线条颜色、线宽、标记和最高/最低点指示符。
本文将逐一介绍 Aspose.Cells 支持的三种迷你图类型——**折线**、**柱形**和**盈亏**——并演示如何添加这些迷你图、自定义其颜色以及保存生成的工作簿。

## **折线迷你图**
折线迷你图通过数据系列中的各个数据点绘制一条连续线条，是显示随时间变化趋势的最自然选择。在 Aspose.Cells 中，通过将 `SparklineType.Line` 传递给 `SparklineGroups.Add` 方法来创建折线迷你图。
1. 创建一个新的 `Workbook`，并访问第一个工作表。
2. 在一行源数据（例如第 1 行的 A 至 E 列）中填入要可视化的值。
3. 构建一个 `CellArea`，用于描述将要绘制迷你图的目标单元格。
4. 调用 `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`。第三个参数 `false` 表示数据区域为水平方向（一行），而非垂直方向（一列）。
5. 根据需要，自定义返回的 `SparklineGroup`。对于折线迷你图，您可以使用 `group.Line.Color`（该属性接受来自 `Aspose.Cells.Drawing` 的 `CellsColor`）设置线条颜色、调整线宽，并切换最高/最低点标记的显示状态。
6. 保存工作簿。
以下示例创建一个工作簿，将值 5、-3、8、-2、6 写入单元格 A1 至 E1，并在单元格 F1 中添加一个反映这些值的折线迷你图。该示例还将线条颜色设置为红色，并启用最高点和最低点标记。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
namespace SparklineDemo
{
    public class Program
    {
        public static void Main()
        {
            // 第 1 步：创建工作簿并获取第一个工作表
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            Cells cells = worksheet.Cells;
            // 第 2 步：将示例值 5、-3、8、-2、6 写入 A1:E1 单元格
            cells["A1"].PutValue(5);
            cells["B1"].PutValue(-3);
            cells["C1"].PutValue(8);
            cells["D1"].PutValue(-2);
            cells["E1"].PutValue(6);
            // 第 3 步：构建指向目标单元格 F1 的 CellArea
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // F 列（从 0 开始索引）
            dest.EndColumn = 5;
            dest.StartRow = 0;      // 第 1 行（从 0 开始索引）
            dest.EndRow = 0;
            // 第 4 步：添加从 A1:E1 到 F1 的 Line 迷你图
            // SparklineGroups.Add 返回新添加组的索引
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];
            // 第 5 步：创建红色 CellsColor 并将其赋给迷你图线条颜色
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;
            // 第 6 步：启用高点标记和低点标记
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            // 第 7 步：保存工作簿
            workbook.Save("output_line.xlsx");
        }
    }
}
```

## **柱形迷你图**
柱形迷你图将每个数据点呈现为垂直柱形，适用于数值大小具有实际意义的数据，例如月度销售额或计数值。在 Aspose.Cells 中，通过将 `SparklineType.Column` 传递给 `SparklineGroups.Add` 方法来创建柱形迷你图。
其步骤与折线迷你图示例类似：
1. 创建一个新的 `Workbook`，并访问第一个工作表。
3. 构建一个 `CellArea`，用于描述目标单元格。
4. 调用 `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`。
5. 根据需要，自定义生成的 `SparklineGroup`，例如通过 `group.Type` 确认类型，或调整柱形颜色。
6. 将工作簿保存到单独的输出文件，以避免覆盖折线迷你图示例。
以下示例将值 5、-3、8、-2、6 写入 A1:E1，并在 F1 中呈现柱形迷你图。负值绘制为向下的柱形，正值绘制向上的柱形，便于直观识别正值和负值。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
namespace SparklineDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // 步骤 1：创建 Workbook 并获取第一个工作表
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            // 步骤 2：将示例值写入 A1:E1
            int[] values = { 5, -3, 8, -2, 6 };
            for (int i = 0; i < values.Length; i++)
            {
                worksheet.Cells[0, i].PutValue(values[i]);
            }
            // 步骤 3：构建一个指向 F1（列索引 5，行索引 0）的 CellArea
            CellArea dest = new CellArea();
            dest.StartColumn = 5;
            dest.EndColumn = 5;
            dest.StartRow = 0;
            dest.EndRow = 0;
            // 步骤 4：在目标单元格添加柱形迷你图
            int idx = worksheet.SparklineGroups.Add(
                SparklineType.Column, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[idx];
            // 步骤 5：通过读取 group.Type 确认迷你图类型
            Console.WriteLine("Sparkline Type added: " + group.Type);
            // 步骤 6：保存工作簿
            workbook.Save("output_column.xlsx");
            Console.WriteLine("Workbook saved as output_column.xlsx");
        }
    }
}
```

## **盈亏迷你图**
盈亏迷你图是柱形迷你图的一种特殊变体，仅用于显示两种结果：正值绘制为“向上”柱形（赢），零或负值绘制为“向下”柱形（亏）。盈亏迷你图通常用于可视化一系列胜负结果、通过/失败结果，或随时间变化的任何二元结果。
在 Aspose.Cells 中，通过将 `SparklineType.Stacked` 传递给 `SparklineGroups.Add` 方法来创建盈亏迷你图。（尽管名称如此，盈亏呈现方式实际使用 `SparklineType.Stacked` 枚举值。）
1. 创建一个新的 `Workbook`，并访问第一个工作表。
2. 填充源区域。由于盈亏迷你图将每个值视为“赢”或“亏”，因此值的大小并不重要，只有符号才有意义。正值绘制为上升柱形，非正值绘制为下降柱形。
3. 构建一个 `CellArea`，用于描述目标单元格。
4. 调用 `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`。
5. 根据需要，自定义返回的 `SparklineGroup`，例如为表示赢和亏的柱形设置强调颜色。
6. 使用不同的文件名保存工作簿，使三个示例可以同时保存在磁盘中。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
namespace SparklineDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // 第 1 步：创建一个工作簿并获取第一个工作表
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            worksheet.Name = "WinLoss";
            // 第 2 步：在第 1 行填充示例数据：A1=5, B1=-3, C1=8, D1=-2, E1=6
            worksheet.Cells["A1"].PutValue(5);
            worksheet.Cells["B1"].PutValue(-3);
            worksheet.Cells["C1"].PutValue(8);
            worksheet.Cells["D1"].PutValue(-2);
            worksheet.Cells["E1"].PutValue(6);
            // 第 3 步：构建指向 F1 的 CellArea（第 5 列，第 0 行）
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // F
            dest.EndColumn = 5;
            dest.StartRow = 0;      // 第 1 行
            dest.EndRow = 0;
            // 第 4 步：添加 Win/Loss 迷你图（SparklineType.Stacked）
            int groupIndex = worksheet.SparklineGroups.Add(
                SparklineType.Stacked,
                "A1:E1",
                false,
                dest);
            SparklineGroup group = worksheet.SparklineGroups[groupIndex];
            // 第 5 步：自定义迷你图组
            // 启用高点标记和低点标记
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            group.ShowNegativePoints = true;
            // 将高点颜色设置为绿色
            CellsColor highColor = workbook.CreateCellsColor();
            highColor.Color = System.Drawing.Color.Green;
            group.HighPointColor = highColor;
            // 将低点颜色设置为红色
            CellsColor lowColor = workbook.CreateCellsColor();
            lowColor.Color = System.Drawing.Color.Red;
            group.LowPointColor = lowColor;
            // 将负值点颜色设置为橙色
            CellsColor negColor = workbook.CreateCellsColor();
            negColor.Color = System.Drawing.Color.Orange;
            group.NegativePointsColor = negColor;
            // 设置默认系列颜色（用于正值柱）
            CellsColor seriesColor = workbook.CreateCellsColor();
            seriesColor.Color = System.Drawing.Color.SteelBlue;
            group.SeriesColor = seriesColor;
            // 第 6 步：保存工作簿
            workbook.Save("output_winloss.xlsx");
            Console.WriteLine("Workbook saved successfully: output_winloss.xlsx");
        }
    }
}
```

## **组合三种迷你图类型**
以下综合示例创建一个工作簿，在第 1 行填入值 5、-3、8、-2、6，然后在单元格 F1、F2 和 F3 中分别添加三个迷你图组（每种类型一个），使生成的文件能够同时展示所有三种迷你图样式。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
// 步骤 1：创建一个 Workbook 并获取第一个工作表
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// 步骤 2：在第 1 行填充示例数据（A1:E1）
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);
// 步骤 3：在 F1 添加一个折线迷你图组
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.SparklineGroups[lineIdx];
// 通过 CellsColor 自定义折线迷你图的颜色
CellsColor lineColor = workbook.CreateCellsColor();
lineColor.Color = System.Drawing.Color.Blue;
lineGroup.SeriesColor = lineColor;
// 步骤 4：在 F2 添加一个柱形迷你图组
CellArea columnArea = new CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.SparklineGroups[columnIdx];
// 自定义柱形迷你图系列的颜色
CellsColor columnColor = workbook.CreateCellsColor();
columnColor.Color = System.Drawing.Color.Green;
columnGroup.SeriesColor = columnColor;
// 步骤 5：在 F3 添加一个盈亏（堆叠）迷你图组
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.SparklineGroups[stackedIdx];
// 自定义盈亏迷你图系列的颜色
CellsColor stackedColor = workbook.CreateCellsColor();
stackedColor.Color = System.Drawing.Color.DarkOrange;
stackedGroup.SeriesColor = stackedColor;
// 步骤 6：保存工作簿
workbook.Save("output_all.xlsx");
```

## **自定义迷你图外观**
创建 `SparklineGroup` 并将其添加到 `worksheet.SparklineGroups` 后，可以在保存工作簿之前读取或修改其多个可视化属性。最常自定义的属性包括：
- **`group.Type`** —— `SparklineType`（Line、Column 或 Stacked）。添加组时即会设置该属性，但您可以读取该值以确认类型。
- **`group.Line.Color`** —— 线条颜色，即通过 `workbook.CreateCellsColor()` 创建的 `CellsColor`。这是用于设置折线迷你图描边颜色的属性。
- **`group.Line.Weight`** —— 以磅为单位的线宽。值越大，线条越粗。
- **最高/最低点标记** —— 用于在最高和最低数据点上显示小型标记的标志，便于突出极值。
- **首点/末点/负值点标记** —— 用于切换第一个、最后一个和负值数据点上标记显示的标志。
若要更改颜色，请始终创建 `CellsColor` 实例并将其赋给相关属性。请勿将 `System.Drawing.Color` 直接赋给迷你图颜色属性；这些属性需要使用来自 `Aspose.Cells.Drawing` 的 `CellsColor` 类型。`SparklineGroups.Add` 方法本身返回类型明确的 `SparklineGroup` 对象，因此您可以在返回值上链式设置属性，也可以将其存储在局部变量中，并在保存之前进行自定义。

## 相关文章
- [在 Aspose.Cells for .NET 中将迷你图转换为图像和 HTML](/cells/zh/net/convert-sparkline-to-image-and-html/)
- [在 Aspose.Cells for .NET 中向数据透视表添加筛选字段](/cells/zh/net/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for .NET 中对数据透视表应用样式](/cells/zh/net/apply-style-to-pivot-table/)
- [修改数据透视表中的页面字段布局](/cells/zh/net/change-page-field-layout/)
- [将 Excel 转换为 OFD 格式](/cells/zh/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}