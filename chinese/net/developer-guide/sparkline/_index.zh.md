---
title: Aspose.Cells for .NET 中的迷你图
linktitle: 迷你图
description: Aspose.Cells 是一个用于处理电子表格文件的 .NET 库，支持创建迷你图——放置在工作表单元格内的微型图表。本篇文章说明如何使用 Aspose.Cells 库添加和自定义线形、柱形和盈亏迷你图。
keywords: Aspose.Cells, .NET 库, 电子表格, 迷你图, 线形迷你图, 柱形迷你图, 盈亏迷你图, SparklineGroup, SparklineType
type: docs
weight: 195
url: /zh/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持在工作表单元格内创建迷你图。迷你图是适合单个单元格的微型图表，可快速直观地展示数据趋势。Aspose.Cells 支持线形、柱形和盈亏迷你图，并且可以对其颜色、线宽、最高/最低点以及标记等进行自定义。
{{% /alert %}}

## **简介**
迷你图是放置在单元格内的微型图表，当您希望在数据行或列旁快速显示趋势而不占用完整图表空间时非常有用。Excel 支持三种类型的迷你图：线形、柱形和盈亏。Aspose.Cells 在 `Aspose.Cells.Charts` 命名空间下提供的 `SparklineGroup` 和 `SparklineGroupCollection` API 完全复刻了此功能。
在 Aspose.Cells 中，所有添加的迷你图均通过 `工作表.SparklineGroups.Add(...)` 创建，该方法返回一个 `SparklineGroup` 对象。随后可以使用该对象设置迷你图类型、数据区域、目标单元格以及线条颜色、线宽、标记和高/低点指示等视觉属性。
本文将逐一讲解 Aspose.Cells 支持的三种迷你图类型——线形、柱形和盈亏——并演示如何添加、定制颜色以及保存生成的工作簿。

## **线形迷你图**
线形迷你图在数据序列的各点之间绘制连续的线条，是显示时间趋势的最自然选择。在 Aspose.Cells 中，向 `SparklineGroups.Add` 方法传入 `SparklineType.Line` 即可创建线形迷你图。
1. 创建一个新的 `Workbook` 并获取第一个工作表。
2. 在源数据行中填充数据（例如第 1 行的 A 至 E 列），写入您希望可视化的数值。
3. 构建一个 `CellArea`，用于描述绘制迷你图的目标单元格。
4. 调用 `工作表.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`。第三个参数 `false` 表明数据区域是水平的（行），而非垂直的（列）。
5. 可选地对返回的 `SparklineGroup` 进行自定义。对于线形迷你图，可使用 `group.Line.Color`（需要 `Aspose.Cells.Drawing` 中的 `CellsColor`）设置线条颜色，调整线宽，并开启最高/最低点标记。
6. 保存工作簿。
下面的示例创建一个工作簿，将数值 5、-3、8、-2、6 写入 A1 到 E1 单元格，并在 F1 单元格中添加一条跟踪这些数值的线形迷你图。示例还将线条颜色自定义为红色，并启用最高点和最低点的标记。

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
            // Step 1: Create a Workbook and get the first worksheet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            Cells cells = worksheet.Cells;
            // Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
            cells["A1"].PutValue(5);
            cells["B1"].PutValue(-3);
            cells["C1"].PutValue(8);
            cells["D1"].PutValue(-2);
            cells["E1"].PutValue(6);
            // Step 3: Build a CellArea pointing to destination cell F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // column F (0-indexed)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // row 1 (0-indexed)
            dest.EndRow = 0;
            // Step 4: Add a Line sparkline from A1:E1 into F1
            // SparklineGroups.Add returns the index of the newly added group
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];
            // Step 5: Create a red CellsColor and assign it to the sparkline line color
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;
            // Step 6: Enable high-point and low-point markers
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            // Step 7: Save the workbook
            workbook.Save("output_line.xlsx");
        }
    }
}
```

## **柱形迷你图**
柱形迷你图将每个数据点渲染为纵向条形，适用于数值大小有意义的数据，例如月度销售额或计数。在 Aspose.Cells 中，向 `SparklineGroups.Add` 方法传入 `SparklineType.Column` 即可创建柱形迷你图。
其操作步骤与线形迷你图示例相同：
1. 创建一个新的 `Workbook` 并获取第一个工作表。
2. 在源数据行中填充数据（例如第 1 行的 A 至 E 列），写入您希望可视化的数值。
3. 构建一个 `CellArea`，用于描述绘制迷你图的目标单元格。
4. 调用 `工作表.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`。
5. 可选地对生成的 `SparklineGroup` 进行自定义，例如通过设置 `group.Type` 确认类型，或调整条形颜色。
6. 将工作簿保存为其他文件，以免覆盖线形迷你图示例。
下面的示例将数值 5、-3、8、-2、6 写入 A1:E1，并在 F1 单元格渲染柱形迷你图。负值显示为向下的条形，正值显示为向上的条形，能够一目了然地辨别正负贡献。

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
            // Step 1: Create a Workbook and get the first worksheet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            // Step 2: Write sample values into A1:E1
            int[] values = { 5, -3, 8, -2, 6 };
            for (int i = 0; i < values.Length; i++)
            {
                worksheet.Cells[0, i].PutValue(values[i]);
            }
            // Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;
            dest.EndColumn = 5;
            dest.StartRow = 0;
            dest.EndRow = 0;
            // Step 4: Add a Column sparkline to the destination cell
            int idx = worksheet.SparklineGroups.Add(
                SparklineType.Column, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[idx];
            // Step 5: Confirm the sparkline type by reading group.Type
            Console.WriteLine("Sparkline Type added: " + group.Type);
            // Step 6: Save the workbook
            workbook.Save("output_column.xlsx");
            Console.WriteLine("Workbook saved as output_column.xlsx");
        }
    }
}
```

## **盈亏迷你图**
盈亏迷你图是柱形迷你图的特殊变体，仅显示两种结果：正值绘制为向上的柱形（盈），零或负值绘制为向下的柱形（亏）。盈亏迷你图常用于可视化一系列的盈亏、通过/未通过结果或任何二元时间序列。
在 Aspose.Cells 中，向 `SparklineGroups.Add` 方法传入 `SparklineType.Stacked` 即可创建盈亏迷你图。（尽管名称为 Stacked，但该枚举值用于请求盈亏渲染。）
1. 创建一个新的 `Workbook` 并获取第一个工作表。
2. 填充源数据区域。盈亏迷你图将每个数值视为盈或亏，数值的大小无关紧要，只关注符号。正值显示为向上柱形，非正值显示为向下柱形。
3. 构建一个 `CellArea`，用于描述绘制迷你图的目标单元格。
4. 调用 `工作表.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`。
5. 可选地对返回的 `SparklineGroup` 进行自定义，例如为盈柱和亏柱设置强调颜色。
6. 使用不同的文件名保存工作簿，以便三个示例能够共存于磁盘。

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
            // Step 1: Create a Workbook and get the first worksheet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            worksheet.Name = "WinLoss";
            // Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
            worksheet.Cells["A1"].PutValue(5);
            worksheet.Cells["B1"].PutValue(-3);
            worksheet.Cells["C1"].PutValue(8);
            worksheet.Cells["D1"].PutValue(-2);
            worksheet.Cells["E1"].PutValue(6);
            // Step 3: Build a CellArea pointing to F1 (column 5, row 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // F
            dest.EndColumn = 5;
            dest.StartRow = 0;      // row 1
            dest.EndRow = 0;
            // Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
            int groupIndex = worksheet.SparklineGroups.Add(
                SparklineType.Stacked,
                "A1:E1",
                false,
                dest);
            SparklineGroup group = worksheet.SparklineGroups[groupIndex];
            // Step 5: Customize the sparkline group
            // Enable high-point and low-point markers
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            group.ShowNegativePoints = true;
            // Set the high-point color to green
            CellsColor highColor = workbook.CreateCellsColor();
            highColor.Color = System.Drawing.Color.Green;
            group.HighPointColor = highColor;
            // Set the low-point color to red
            CellsColor lowColor = workbook.CreateCellsColor();
            lowColor.Color = System.Drawing.Color.Red;
            group.LowPointColor = lowColor;
            // Set the negative-point color to orange
            CellsColor negColor = workbook.CreateCellsColor();
            negColor.Color = System.Drawing.Color.Orange;
            group.NegativePointsColor = negColor;
            // Set the default series color (used for positive bars)
            CellsColor seriesColor = workbook.CreateCellsColor();
            seriesColor.Color = System.Drawing.Color.SteelBlue;
            group.SeriesColor = seriesColor;
            // Step 6: Save the workbook
            workbook.Save("output_winloss.xlsx");
            Console.WriteLine("Workbook saved successfully: output_winloss.xlsx");
        }
    }
}
```

## **组合三种迷你图类型**
下面的综合示例创建一个工作簿，在第 1 行填入数值 5、-3、8、-2、6，然后在 F1、F2、F3 单元格分别添加三种类型的迷你图组（各一种），从而在同一文件中展示全部三种迷你图样式。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
// Step 1: Create a Workbook and get the first worksheet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Step 2: Populate sample data in row 1 (A1:E1)
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);
// Step 3: Add a Line sparkline group at F1
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.SparklineGroups[lineIdx];
// Customize the line sparkline color via CellsColor
CellsColor lineColor = workbook.CreateCellsColor();
lineColor.Color = System.Drawing.Color.Blue;
lineGroup.SeriesColor = lineColor;
// Step 4: Add a Column sparkline group at F2
CellArea columnArea = new CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.SparklineGroups[columnIdx];
// Customize the column sparkline series color
CellsColor columnColor = workbook.CreateCellsColor();
columnColor.Color = System.Drawing.Color.Green;
columnGroup.SeriesColor = columnColor;
// Step 5: Add a Win/Loss (Stacked) sparkline group at F3
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.SparklineGroups[stackedIdx];
// Customize the win/loss sparkline series color
CellsColor stackedColor = workbook.CreateCellsColor();
stackedColor.Color = System.Drawing.Color.DarkOrange;
stackedGroup.SeriesColor = stackedColor;
// Step 6: Save the workbook
workbook.Save("output_all.xlsx");
```

## **自定义迷你图外观**
在创建并将 `SparklineGroup` 添加到 `工作表.SparklineGroups` 后，您可以在保存工作簿之前读取或修改其多个视觉属性。最常自定义的属性包括：
- **`group.Type`** — `SparklineType`（Line、Column 或 Stacked）。该属性在添加分组时已设置，但您可以读取以确认。
- **`group.Line.Color`** — 线条颜色，以通过 `workbook.CreateCellsColor()` 创建的 `CellsColor` 表示。此属性用于设置线形迷你图的描边颜色。
- **`group.Line.Weight`** — 线宽（单位：磅），数值越大线条越粗。
- **High/Low point markers** — 用于在最高点和最低点显示小标记的标志，可用于突出极值。
- **First/Last/Negative point markers** — 用于在首点、尾点和负值点显示标记的标志。
要更改颜色，始终创建 `CellsColor` 实例并将其赋给相应属性。不要直接将 `System.Drawing.Color` 赋给迷你图颜色属性——它们期望的是来自 `Aspose.Cells.Drawing` 的 `CellsColor` 类型。`SparklineGroups.Add` 方法本身返回一个完整类型的 `SparklineGroup` 对象，您可以对返回值链式调用属性赋值，或将其存入局部变量后再进行自定义，最后保存。

## Related Articles
- [在 Aspose.Cells for .NET 中将迷你图转换为图像和 HTML](/cells/zh/net/convert-sparkline-to-image-and-html/)
- [在 Aspose.Cells for .NET 中向数据透视表添加筛选字段](/cells/zh/net/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for .NET 中为数据透视表应用样式](/cells/zh/net/apply-style-to-pivot-table/)
- [修改数据透视表的页面字段布局](/cells/zh/net/change-page-field-layout/)
- [将 Excel 转换为 OFD 格式](/cells/zh/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}