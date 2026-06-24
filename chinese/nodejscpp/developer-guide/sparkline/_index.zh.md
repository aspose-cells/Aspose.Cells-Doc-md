---
title: Aspose.Cells for Node.js via C++ 中的迷你图
linktitle: Sparklines
description: Aspose.Cells 是一个用于处理电子表格文件的 Node.js 库,支持创建迷你图——放置在工作表单元格中的小型图表。本文介绍如何使用 Aspose.Cells 库添加和自定义线条、柱形和盈亏迷你图。
keywords: Aspose.Cells, Node.js 库, 电子表格, 迷你图, 线条迷你图, 柱形迷你图, 盈亏迷你图, SparklineGroup, SparklineType
type: docs
weight: 195
url: /zh/nodejs-cpp/creating-sparklines/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 支持在工作表单元格中创建迷你图。迷你图是适合单个单元格的微型图表,可以快速直观地展示数据趋势。Aspose.Cells 支持线条、柱形和盈亏迷你图,并且可以针对颜色、线条粗细、高/低点和标记进行自定义。

{{% /alert %}}

## **简介**

迷你图是单元格中的小型图表,当您想在数据行或列旁边显示快速趋势,而又不占用完整图表的空间时,它们非常有用。Excel 支持三种迷你图:**线条**、**柱形**和**盈亏**。Aspose.Cells 通过 `Aspose.Cells.Charts` 命名空间中的 `SparklineGroup` 和 `SparklineGroupCollection` API 提供了相应的功能。

在 Aspose.Cells 中,您添加的每个迷你图都是通过 `worksheet.sparklineGroups.add(...)` 创建的,该方法返回一个 `SparklineGroup` 对象。然后您可以使用该对象设置迷你图类型、数据区域、目标单元格,以及线条颜色、线条粗细、标记和高/低点指示器等可视属性。

{{% alert color="primary" %}}

单个 `SparklineGroup` 可以包含一个或多个共享相同样式的迷你图。当您调用 `add` 并传入一行数据以及单个目标单元格时,该单元格中将显示一个迷你图。如果您的目标区域宽度超过一个单元格,则会在每个目标单元格中分别绘制一个迷你图,所有这些迷你图使用相同的样式和数据区域。

{{% /alert %}}

本文将逐一介绍 Aspose.Cells 支持的三种迷你图类型——**线条**、**柱形**和**盈亏**——并展示如何添加它们、自定义其颜色以及保存生成的工作簿。

## **线条迷你图**

线条迷你图通过一系列数据点绘制一条连续的线条,使其成为展示随时间变化趋势的最自然选择。在 Aspose.Cells 中,通过将 `SparklineType.Line` 传递给 `sparklineGroups.add` 方法来创建线条迷你图。

工作流程与任何其他迷你图类型相同:

1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 在一行源数据中(例如第 1 行 A 到 E 列)填充您要可视化的值。
3. 构建一个 `CellArea` 来描述迷你图将要绘制的目标单元格。
4. 调用 `worksheet.sparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`。第三个参数 `false` 告诉 Aspose.Cells 数据区域是水平的(一行)而非垂直的(一列)。
5. 可选地自定义返回的 `SparklineGroup`。对于线条迷你图,您可以使用 `group.line.color` 设置线条颜色(需要来自 `Aspose.Cells.Drawing` 的 `CellsColor`),调整线条粗细,并切换高/低点标记。
6. 保存工作簿。

以下示例创建一个工作簿,将值 5、-3、8、-2、6 写入单元格 A1 到 E1,并在单元格 F1 中添加一个追踪这些值的线条迷你图。它还将线条颜色自定义为红色,并启用高点和低点的标记。

```javascript
const AsposeCells = require("aspose.cells");

// 步骤 1：创建工作簿并获取第一个工作表
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

// 步骤 2：将示例值 5、-3、8、-2、6 写入单元格 A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);

// 步骤 3：构建指向目标单元格 F1 的 CellArea
const dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // 列 F（从 0 开始索引）
dest.setEndColumn(5);
dest.setStartRow(0);      // 行 1（从 0 开始索引）
dest.setEndRow(0);

// 步骤 4：将 A1:E1 的折线迷你图添加到 F1
// SparklineGroups.Add 返回新添加组的索引
const index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
const group = worksheet.getSparklineGroups().get(index);

// 步骤 5：创建红色 CellsColor 并将其分配给迷你图线条颜色
const red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);

// 步骤 6：启用高点和低点标记
group.setShowHighPoint(true);
group.setShowLowPoint(true);

// 步骤 7：保存工作簿
workbook.save("output_line.xlsx");
```

## **柱形迷你图**

柱形迷你图将每个数据点渲染为一个垂直条形。这使其非常适合用于数值大小具有意义的场景——例如每月销售数据或计数。在 Aspose.Cells 中,通过将 `SparklineType.Column` 传递给 `sparklineGroups.add` 方法来创建柱形迷你图。

操作步骤与线条迷你图示例类似:

1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 在同一源区域(A1:E1)中填充您要可视化的值。
3. 构建一个 `CellArea` 来描述目标单元格。
4. 调用 `worksheet.sparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`。
5. 可选地自定义生成的 `SparklineGroup`——例如,通过设置 `group.type` 来确认类型,或者调整条形颜色。
6. 将工作簿保存到一个单独的输出文件,以避免覆盖线条迷你图示例。

下面的示例将值 5、-3、8、-2、6 写入 A1:E1,并在 F1 中渲染一个柱形迷你图。负值绘制为向下的条形,正值绘制为向上的条形,因此可以一目了然地区分正值和负值的贡献。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// 步骤 2: 将示例值写入 A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// 步骤 3: 构建一个指向 F1 的 CellArea（列索引 5，行索引 0）
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// 步骤 4: 向目标单元格添加柱形迷你图
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);

// 步骤 5: 通过读取 group.Type 确认迷你图类型
console.log("Sparkline Type added: " + group.getType());

// 步骤 6: 保存工作簿
workbook.save("output_column.xlsx");

console.log("Workbook saved as output_column.xlsx");
```

## **盈亏迷你图**

盈亏迷你图是柱形迷你图的一种特殊变体,用于仅显示两种结果:正值绘制为"向上"条形(赢),零或负值绘制为"向下"条形(亏)。盈亏迷你图通常用于可视化一系列的胜负、合格/不合格结果,或者随时间变化的任何二元结果。

在 Aspose.Cells 中,通过将 `SparklineType.Stacked` 传递给 `sparklineGroups.add` 方法来创建盈亏迷你图。(尽管名称如此,`SparklineType.Stacked` 是用于请求盈亏渲染的枚举值。)

操作步骤与其他两种类型相同:

1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 填充源区域。由于盈亏迷你图将每个值视为赢或亏,因此值的大小无关紧要——只有其正负号才重要。正值变为向上条形,非正值变为向下条形。
3. 构建一个 `CellArea` 来描述目标单元格。
4. 调用 `worksheet.sparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`。
5. 可选地自定义返回的 `SparklineGroup`,例如设置赢亏条形的强调颜色。
6. 使用不同的文件名保存工作簿,以便所有三个示例可以共存于磁盘上。

下面的示例使用与前两节相同的输入数据。值 5、-3、8、-2、6 被解释为赢、亏、赢、亏、赢——在 F1 中绘制的迷你图准确反映该模式。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");

// 步骤 2：在第 1 行填充示例数据：A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// 步骤 3：构建指向 F1 的 CellArea（第 5 列，第 0 行）
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F
dest.setEndColumn(5);
dest.setStartRow(0);      // 第 1 行
dest.setEndRow(0);

// 步骤 4：添加盈亏迷你图（SparklineType.Stacked）
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest);
let group = worksheet.getSparklineGroups().get(groupIndex);

// 步骤 5：自定义迷你图组
// 启用高点标记和低点标记
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// 将高点颜色设置为绿色
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.Green);
group.setHighPointColor(highColor);

// 将低点颜色设置为红色
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.Red);
group.setLowPointColor(lowColor);

// 将负点颜色设置为橙色
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.Orange);
group.setNegativePointsColor(negColor);

// 设置默认系列颜色（用于正值柱）
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.SteelBlue);
group.setSeriesColor(seriesColor);

// 步骤 6：保存工作簿
workbook.save("output_winloss.xlsx");

console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **组合使用所有三种迷你图类型**

前三个示例各自生成一个独立的工作簿,以便于单独查看输出文件。然而,在实际场景中,您通常希望并排比较多个数据序列。最简洁的方法是将多个迷你图组放入同一个工作表中,每组以不同的样式呈现。

您可以将多个 `SparklineGroup` 对象添加到同一个 `SparklineGroupCollection` 中,每个组可以针对不同的目标单元格或不同的区域。例如,您可以在 F1 放置线条迷你图,在 F2 放置柱形迷你图,在 F3 放置盈亏迷你图——它们都从第 1 行中的同一源数据读取——以便读者可以看到同一组数字的三种不同可视化呈现。

下面的组合示例创建一个工作簿,在第 1 行中填充值 5、-3、8、-2、6,然后在单元格 F1、F2 和 F3 中添加三个迷你图组——每种类型一个——使生成的文件同时展示所有三种迷你图样式。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// 步骤 2：在第 1 行 (A1:E1) 填充示例数据
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// 步骤 3：在 F1 添加折线迷你图组
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// 通过 CellsColor 自定义折线迷你图颜色
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.Blue);
lineGroup.setSeriesColor(lineColor);

// 步骤 4：在 F2 添加柱形迷你图组
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// 自定义柱形迷你图系列颜色
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.Green);
columnGroup.setSeriesColor(columnColor);

// 步骤 5：在 F3 添加胜负（堆叠）迷你图组
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// 自定义胜负迷你图系列颜色
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.DarkOrange);
stackedGroup.setSeriesColor(stackedColor);

// 步骤 6：保存工作簿
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

当您在单个工作表中组合多个迷你图组时,每个组都是独立的。它们可以共享相同的源区域或使用不同的源区域,并且可以独立设置样式。这使得直接在现有工作表中构建一个小型"仪表板"的单元格内可视化变得很容易。

{{% /alert %}}

## **自定义迷你图外观**

一旦 `SparklineGroup` 被创建并添加到 `worksheet.sparklineGroups` 中,您可以在保存工作簿之前读取或修改它的多个可视属性。最常自定义的属性包括:

- **`group.type`** — `SparklineType`(线条、柱形或堆叠)。它在组被添加时设置,但您可以读取它以确认类型。
- **`group.line.color`** — 线条颜色,以通过 `workbook.createCellsColor()` 创建的 `CellsColor` 表示。这是用于设置线条迷你图描边颜色的属性。
- **`group.line.weight`** — 线条粗细(以磅为单位)。值越大,线条越粗。
- **高/低点标记** — 标志,用于在最高和最低数据点上显示小标记,有助于突出极值。
- **首/末/负值点标记** — 标志,用于在第一个、最后一个和负值数据点上切换标记。

要更改颜色,请始终创建一个 `CellsColor` 实例并将其分配给相关属性。不要直接将 `System.Drawing.Color` 分配给迷你图颜色属性——它们期望来自 `Aspose.Cells.Drawing` 的 `CellsColor` 类型。`sparklineGroups.add` 方法本身返回完全类型化的 `SparklineGroup` 对象,因此您可以在返回值上链式分配属性,或者将其存储在局部变量中,在保存之前进行自定义。



{{< app/cells/assistant language="javascript" >}}