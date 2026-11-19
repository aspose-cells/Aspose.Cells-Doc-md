---
title: Aspose.Cells for Node.js via Java 中的迷你图
linktitle: 迷你图
description: Aspose.Cells 是一个用于处理电子表格文件的 Node.js via Java 库，支持创建迷你图——放置在工作表单元格中的微型图表。本文介绍如何使用 Aspose.Cells 库添加和自定义折线、柱形和盈亏迷你图。
keywords: Aspose.Cells, Node.js via Java 库, 电子表格, 迷你图, 折线迷你图, 柱形迷你图, 盈亏迷你图, SparklineGroup, SparklineType
type: docs
weight: 195
url: /zh/nodejs-java/creating-sparklines/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持在工作表单元格中创建迷你图。迷你图是适合在单个单元格内显示的微型图表，可直观快速地展现数据趋势。Aspose.Cells 支持折线、柱形和盈亏迷你图，并且可以针对颜色、线条粗细、高低点以及标记等属性进行自定义。
{{% /alert %}}

## **简介**
迷你图是单元格内的小型图表，当您希望在一行或一列数据旁边快速显示趋势、又不希望占用完整图表的空间时，它们非常有用。Excel 支持三种迷你图：**折线**、**柱形** 和 **盈亏**。Aspose.Cells 通过 `com.aspose.cells.Charts` 命名空间中的 `SparklineGroup` 和 `SparklineGroupCollection` API 提供了相应的能力。
在 Aspose.Cells 中，您添加的每一个迷你图都是通过 `worksheet.SparklineGroups.add(...)` 创建的，该方法返回一个 `SparklineGroup` 对象。然后您可以使用该对象设置迷你图类型、数据区域、目标单元格，以及线条颜色、线条粗细、标记和最高/最低点指示等可视化属性。
本文将逐一介绍 Aspose.Cells 支持的三种迷你图类型——**折线**、**柱形** 和 **盈亏**——并演示如何添加它们、自定义颜色以及保存生成的工作簿。

## **折线迷你图**
折线迷你图通过一条连续的线条将数据系列中的各个数据点连接起来，是显示随时间变化趋势的最自然选择。在 Aspose.Cells 中，向 `SparklineGroups.add` 方法传入 `SparklineType.Line` 即可创建折线迷你图。
1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 在一行源数据中（例如第 1 行的 A 到 E 列）填充您希望可视化的值。
3. 构造一个 `CellArea`，描述将要绘制迷你图的目标单元格。
4. 调用 `worksheet.SparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`。第三个参数 `false` 告诉 Aspose.Cells 数据区域是水平的（行），而非垂直的（列）。
5. 可选地自定义返回的 `SparklineGroup`。对于折线迷你图，您可以使用 `group.Line.Color`（需要传入来自 `com.aspose.cells.Drawing` 的 `CellsColor`）设置线条颜色，调整线条粗细，以及开启最高/最低点标记。
6. 保存工作簿。
以下示例创建一个工作簿，将值 5、-3、8、-2、6 写入 A1 到 E1 单元格，并在 F1 单元格中添加一条折线迷你图来描绘这些值。该示例还将线条颜色自定义为红色，并为最高点和最低点启用标记。

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();
// Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// Step 3: Build a CellArea pointing to destination cell F1
let dest = new AsposeCells.CellArea();
dest.StartColumn = 5;   // column F (0-indexed)
dest.EndColumn = 5;
dest.StartRow = 0;      // row 1 (0-indexed)
dest.EndRow = 0;
// Step 4: Add a Line sparkline from A1:E1 into F1
// SparklineGroups.Add returns the index of the newly added group
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.LINE, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(index);
// Step 5: Create a red CellsColor and assign it to the sparkline line color
let red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);
// Step 6: Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// Step 7: Save the workbook
workbook.save("output_line.xlsx");
```

## **柱形迷你图**
柱形迷你图将每个数据点绘制为垂直柱形。这使得它非常适合表示数值大小具有意义的数据，例如月度销售额或计数。在 Aspose.Cells 中，向 `SparklineGroups.add` 方法传入 `SparklineType.Column` 即可创建柱形迷你图。
其步骤与折线迷你图示例类似：
1. 创建一个新的 `Workbook` 并访问第一个工作表。
3. 构造一个 `CellArea`，描述目标单元格。
4. 调用 `worksheet.SparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`。
5. 可选地自定义返回的 `SparklineGroup`，例如设置 `group.Type` 确认类型，或调整柱形颜色。
6. 将工作簿保存到另一个输出文件，以避免覆盖折线迷你图示例。
下面的示例将值 5、-3、8、-2、6 写入 A1:E1，并在 F1 中渲染一个柱形迷你图。负值绘制为向下的柱形，正值绘制为向上的柱形，这使得一眼就能区分正负贡献。

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Step 2: Write sample values into A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
let dest = new AsposeCells.CellArea();
dest.StartColumn = 5;
dest.EndColumn = 5;
dest.StartRow = 0;
dest.EndRow = 0;
// Step 4: Add a Column sparkline to the destination cell
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.COLUMN, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);
// Step 5: Confirm the sparkline type by reading group.Type
console.log("Sparkline Type added: " + group.getType());
// Step 6: Save the workbook
workbook.save("output_column.xlsx");
console.log("Workbook saved as output_column.xlsx");
```

## **盈亏迷你图**
盈亏迷你图是柱形迷你图的一种特殊变体，用于仅显示两种结果：正值绘制为向上的柱形（赢），零或负值绘制为向下的柱形（输）。盈亏迷你图通常用于可视化胜负序列、通过/未通过的结果，或任何随时间变化的二元结果。
在 Aspose.Cells 中，向 `SparklineGroups.add` 方法传入 `SparklineType.Stacked` 即可创建盈亏迷你图。（尽管名称如此，`SparklineType.Stacked` 是用于请求盈亏渲染的枚举值。）
1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 填充源区域。由于盈亏迷你图将每个值视为赢或输，因此值的大小并不重要——仅其符号重要。正值成为向上的柱形，非正值成为向下的柱形。
3. 构造一个 `CellArea`，描述目标单元格。
4. 调用 `worksheet.SparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`。
5. 可选地自定义返回的 `SparklineGroup`，例如为赢和输的柱形设置强调色。
6. 使用不同的文件名保存工作簿，以便三个示例可以共存于磁盘中。

```javascript
const AsposeCells = require("aspose.cells");
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
dest.StartColumn = 5;   // F
dest.EndColumn = 5;
dest.StartRow = 0;      // row 1
dest.EndRow = 0;
// Step 4: Add a Win/Loss sparkline (SparklineType.STACKED)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.STACKED,
    "A1:E1",
    false,
    dest
);
let group = worksheet.getSparklineGroups().get(groupIndex);
// Step 5: Customize the sparkline group
// Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Set the high-point color to green
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.getGreen());
group.setHighPointColor(highColor);
// Set the low-point color to red
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.getRed());
group.setLowPointColor(lowColor);
// Set the negative-point color to orange
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.getOrange());
group.setNegativePointsColor(negColor);
// Set the default series color (used for positive bars)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.getSteelBlue());
group.setSeriesColor(seriesColor);
// Step 6: Save the workbook
workbook.save("output_winloss.xlsx");
console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **组合三种迷你图类型**
下面的组合示例创建一个工作簿，在第 1 行填入值 5、-3、8、-2、6，然后在 F1、F2 和 F3 单元格中分别添加三种迷你图组——每种类型一个——从而生成的单个文件即可同时展示全部三种迷你图样式。

```javascript
const AsposeCells = require("aspose.cells");
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
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.LINE, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Customize the line sparkline color via CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// Step 4: Add a Column sparkline group at F2
let columnArea = new AsposeCells.CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.COLUMN, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Customize the column sparkline series color
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// Step 5: Add a Win/Loss (Stacked) sparkline group at F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.STACKED, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Customize the win/loss sparkline series color
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// Step 6: Save the workbook
workbook.save("output_all.xlsx");
```

## **自定义迷你图外观**
一旦 `SparklineGroup` 被创建并添加到 `worksheet.SparklineGroups` 中，您可以在保存工作簿之前读取或修改其若干可视化属性。最常用的可自定义属性包括：
- **`group.Type`** — `SparklineType`（Line、Column 或 Stacked）。该属性在添加组时设置，但您可以读回它以确认类型。
- **`group.Line.Color`** — 线条颜色，以通过 `workbook.createCellsColor()` 创建的 `CellsColor` 表示。这是用于设置折线迷你图描边颜色的属性。
- **`group.Line.Weight`** — 线条粗细，以磅为单位。值越大，线条越粗。
- **最高/最低点标记** — 用于在最高和最低数据点上显示小型标记的开关，适合突出极值。
- **首个/末个/负值点标记** — 用于在第一个、最后一个和负值数据点上切换标记显示的开关。
要更改颜色，务必创建一个 `CellsColor` 实例并将其赋值给相应属性。不要直接将 `java.awt.Color` 赋值给迷你图的颜色属性——这些属性要求使用来自 `com.aspose.cells.Drawing` 的 `CellsColor` 类型。`SparklineGroups.add` 方法本身会返回一个类型完整的 `SparklineGroup` 对象，因此您可以对该返回值链式设置属性，或将其存入局部变量后再进行自定义，然后保存。

{{< app/cells/assistant language="nodejs-java" >}}