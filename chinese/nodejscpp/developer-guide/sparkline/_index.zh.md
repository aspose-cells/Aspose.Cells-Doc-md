---
title: Aspose.Cells for Node.js via C++ 中的迷你图
linktitle: Aspose.Cells for Node.js via C++ 中的迷你图
description: Aspose.Cells 是一个用于处理电子表格文件的 Node.js 库，支持在单元格内创建迷你图——一种放置在工作表单元格中的小型图表。本文介绍如何使用 Aspose.Cells 库添加和自定义折线、柱形和盈亏迷你图。
keywords: Aspose.Cells, Node.js 库, 电子表格, 迷你图, 折线迷你图, 柱形迷你图, 盈亏迷你图, SparklineGroup, SparklineType
type: docs
weight: 195
url: /zh/nodejs-cpp/creating-sparklines/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持在工作表单元格内创建迷你图。迷你图是放置在单个单元格内的小型图表，可快速直观地呈现数据趋势。Aspose.Cells 支持折线、柱形和盈亏三种迷你图，并且每种都可以从颜色、线宽、高/低点和标记等方面进行自定义。
{{% /alert %}}

## **简介**
迷你图是单元格内的小型图表，当您希望在数据行或数据列旁边快速显示趋势而不占用完整图表的空间时，它们非常有用。Excel 支持三种迷你图：**折线**、**柱形**和**盈亏**。Aspose.Cells 通过 `Aspose.Cells.Charts` 命名空间中的 `SparklineGroup` 和 `SparklineGroupCollection` API 提供了这一能力。
在 Aspose.Cells 中，您添加的每个迷你图都是通过 `worksheet.sparklineGroups.add(...)` 创建的，该方法返回一个 `SparklineGroup` 对象。然后您可以使用该对象设置迷你图类型、数据区域、目标单元格以及视觉属性，例如线条颜色、线宽、标记和高/低点指示器。
本文将逐一介绍 Aspose.Cells 支持的三种迷你图类型——**折线**、**柱形**和**盈亏**——并演示如何添加它们、自定义其颜色以及保存最终的工作簿。

## **折线迷你图**
折线迷你图通过一系列数据点绘制一条连续的线条，是显示随时间变化的趋势的最自然的选择。在 Aspose.Cells 中，通过将 `SparklineType.Line` 传递给 `sparklineGroups.add` 方法来创建折线迷你图。
1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 在一行源数据中（例如第 1 行，A 至 E 列）填入您要可视化的值。
3. 构造一个 `CellArea`，描述迷你图将绘制到的目标单元格。
4. 调用 `worksheet.sparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`。第三个参数 `false` 告诉 Aspose.Cells 数据区域是水平的（一行）而不是垂直的（一列）。
5. 可选地对返回的 `SparklineGroup` 进行自定义。对于折线迷你图，您可以使用 `group.line.color`（它需要一个来自 `Aspose.Cells.Drawing` 的 `CellsColor`）设置线条颜色，调整线宽，并切换高/低点的标记。
6. 保存工作簿。
以下示例创建一个工作簿，将值 5、-3、8、-2、6 写入单元格 A1 至 E1，并在单元格 F1 中添加一个折线迷你图来描绘这些值。它还将线条颜色自定义为红色，并启用高点和低点的标记。

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Step 2: Populate sample data in row 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Step 3: Add a Line sparkline group at F1
let lineArea = new AsposeCells.CellArea();
lineArea.startColumn = 5;
lineArea.endColumn = 5;
lineArea.startRow = 0;
lineArea.endRow = 0;
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Customize the line sparkline color via CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.Blue);
lineGroup.setSeriesColor(lineColor);
// Step 4: Add a Column sparkline group at F2
let columnArea = new AsposeCells.CellArea();
columnArea.startColumn = 5;
columnArea.endColumn = 5;
columnArea.startRow = 1;
columnArea.endRow = 1;
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Customize the column sparkline series color
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.Green);
columnGroup.setSeriesColor(columnColor);
// Step 5: Add a Win/Loss (Stacked) sparkline group at F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.startColumn = 5;
stackedArea.endColumn = 5;
stackedArea.startRow = 2;
stackedArea.endRow = 2;
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Customize the win/loss sparkline series color
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.DarkOrange);
stackedGroup.setSeriesColor(stackedColor);
// Step 6: Save the workbook
workbook.save("output_all.xlsx");
```

## **柱形迷你图**
柱形迷你图将每个数据点渲染为一个垂直柱形。这使其非常适合具有意义的数值大小的数据——例如每月销售额或计数。在 Aspose.Cells 中，通过将 `SparklineType.Column` 传递给 `sparklineGroups.add` 方法来创建柱形迷你图。
其步骤与折线迷你图示例相同：
1. 创建一个新的 `Workbook` 并访问第一个工作表。
3. 构造一个 `CellArea`，描述目标单元格。
4. 调用 `worksheet.sparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`。
5. 可选地对生成的 `SparklineGroup` 进行自定义——例如，通过设置 `group.type` 来确认类型，或调整柱形颜色。
6. 将工作簿保存到单独的输出文件，以免覆盖折线迷你图示例。
下面的示例将值 5、-3、8、-2、6 写入 A1:E1，并在 F1 中渲染一个柱形迷你图。负值绘制为向下的柱形，正值绘制为向上的柱形，这使得正向和负向贡献一眼即可分辨。

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Step 3: Build a CellArea pointing to F1 (column 5, row 0)
let dest = new AsposeCells.CellArea();
dest.startColumn = 5;   // F
dest.endColumn = 5;
dest.startRow = 0;      // row 1
dest.endRow = 0;
// Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest);
let group = worksheet.getSparklineGroups().get(groupIndex);
// Step 5: Customize the sparkline group
// Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Set the high-point color to green
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.Green);
group.setHighPointColor(highColor);
// Set the low-point color to red
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.Red);
group.setLowPointColor(lowColor);
// Set the negative-point color to orange
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.Orange);
group.setNegativePointsColor(negColor);
// Set the default series color (used for positive bars)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.SteelBlue);
group.setSeriesColor(seriesColor);
// Step 6: Save the workbook
workbook.save("output_winloss.xlsx");
console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **盈亏迷你图**
盈亏迷你图是柱形迷你图的一种特殊变体，旨在仅显示两种结果：正值绘制为"上升"柱形（胜利），零或负值绘制为"下降"柱形（失败）。盈亏迷你图通常用于可视化胜负序列、通过/未通过结果或随时间发生的任何二元结果。
在 Aspose.Cells 中，通过将 `SparklineType.Stacked` 传递给 `sparklineGroups.add` 方法来创建盈亏迷你图。（尽管名称如此，`SparklineType.Stacked` 是用于请求盈亏渲染的枚举值。）
1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 填充源区域。由于盈亏迷你图将每个值都视为胜利或失败，因此值的大小无关紧要——只有符号才有意义。正值变为上升柱形，非正值变为下降柱形。
3. 构造一个 `CellArea`，描述目标单元格。
4. 调用 `worksheet.sparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`。
5. 可选地对返回的 `SparklineGroup` 进行自定义，例如为胜利和失败柱形设置强调颜色。
6. 使用不同的文件名保存工作簿，以便所有三个示例可以同时存在于磁盘上。

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Step 2: Write sample values into A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
let dest = new AsposeCells.CellArea();
dest.startColumn = 5;
dest.endColumn = 5;
dest.startRow = 0;
dest.endRow = 0;
// Step 4: Add a Column sparkline to the destination cell
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);
// Step 5: Confirm the sparkline type by reading group.Type
console.log("Sparkline Type added: " + group.getType());
// Step 6: Save the workbook
workbook.save("output_column.xlsx");
console.log("Workbook saved as output_column.xlsx");
```

## **组合三种迷你图类型**
下面的组合示例创建一个工作簿，在第 1 行填入值 5、-3、8、-2、6，然后在 F1、F2 和 F3 单元格中添加三个迷你图组——每种类型各一个——使生成的文件同时展示所有三种迷你图样式。

```javascript
const AsposeCells = require("aspose.cells.node");
// Step 1: Create a Workbook and get the first worksheet
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// Step 3: Build a CellArea pointing to destination cell F1
const dest = new AsposeCells.CellArea();
dest.startColumn = 5;   // column F (0-indexed)
dest.endColumn = 5;
dest.startRow = 0;      // row 1 (0-indexed)
dest.endRow = 0;
// Step 4: Add a Line sparkline from A1:E1 into F1
// SparklineGroups.Add returns the index of the newly added group
const index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
const group = worksheet.getSparklineGroups().get(index);
// Step 5: Create a red CellsColor and assign it to the sparkline line color
const red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.Red);
group.setSeriesColor(red);
// Step 6: Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// Step 7: Save the workbook
workbook.save("output_line.xlsx");
```

## **自定义迷你图外观**
一旦 `SparklineGroup` 被创建并添加到 `worksheet.sparklineGroups`，您可以在保存工作簿之前读取或修改其多个视觉属性。最常自定义的属性包括：
- **`group.type`** —— `SparklineType`（Line、Column 或 Stacked）。该属性在添加组时设置，但您可以读回它进行确认。
- **`group.line.color`** —— 线条颜色，以通过 `workbook.createCellsColor()` 创建的 `CellsColor` 表示。这是用于折线迷你图描边颜色的属性。
- **`group.line.weight`** —— 以磅为单位的线宽。值越大，线条越粗。
- **高/低点标记** —— 用于在高数据点和低数据点上显示小标记的标志，有助于突出极值。
- **首/末/负点标记** —— 用于在第一个、最后一个和负数数据点上切换标记的标志。
要更改颜色，请始终创建一个 `CellsColor` 实例并将其分配给相关属性。不要直接将 `System.Drawing.Color` 分配给迷你图颜色属性——它们期望来自 `Aspose.Cells.Drawing` 的 `CellsColor` 类型。`sparklineGroups.add` 方法本身返回一个类型完整的 `SparklineGroup` 对象，因此您可以在返回值上链接属性赋值，或者将其存储在本地变量中并在保存之前进行自定义。

{{< app/cells/assistant language="nodejs-cpp" >}}