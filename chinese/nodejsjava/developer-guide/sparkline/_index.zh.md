---
title: Aspose.Cells for Node.js via Java 中的迷你图
linktitle: Sparklines
description: Aspose.Cells 是一个用于处理电子表格文件的 Node.js via Java 库，支持创建迷你图——放置在工作表单元格中的小型图表。本文介绍如何使用 Aspose.Cells 库添加和自定义折线、柱形和盈亏迷你图。
keywords: Aspose.Cells, Node.js via Java 库, 电子表格, 迷你图, 折线迷你图, 柱形迷你图, 盈亏迷你图, SparklineGroup, SparklineType
type: docs
weight: 195
url: /zh/nodejs-java/creating-sparklines/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 支持在工作表单元格内创建迷你图。迷你图是适合放置在单个单元格内的小型图表，能够快速直观地展示数据趋势。Aspose.Cells 支持折线、柱形和盈亏迷你图，并且可以针对颜色、线条粗细、高低点以及标记点等属性进行自定义。

{{% /alert %}}

## **简介**

迷你图是单元格内的小型图表，当您希望在数据行或列旁边快速显示趋势而又不占用完整图表的空间时，它们非常有用。Excel 支持三种迷你图：**折线**、**柱形**和**盈亏**。Aspose.Cells 通过 `com.aspose.cells.Charts` 命名空间中的 `SparklineGroup` 和 `SparklineGroupCollection` API 提供了相应的功能。

在 Aspose.Cells 中，您添加的每个迷你图都是通过 `worksheet.SparklineGroups.add(...)` 方法创建的，该方法返回一个 `SparklineGroup` 对象。然后，您可以使用该对象来设置迷你图类型、数据区域、目标单元格以及视觉属性，例如线条颜色、线条粗细、标记点和高低点指示器。

{{% alert color="primary" %}}

单个 `SparklineGroup` 可以包含一个或多个共享相同样式的迷你图。当您调用 `add` 并传入一行数据以及单个目标单元格时，该单元格内会生成一个迷你图。如果您的目标区域宽度超过一个单元格，则会在每个目标单元格中分别绘制一个迷你图，它们都使用相同的样式和数据区域。

{{% /alert %}}

本文将逐一介绍 Aspose.Cells 支持的三种迷你图类型——**折线**、**柱形**和**盈亏**——并展示如何添加它们、自定义它们的颜色以及保存生成的工作簿。

## **折线迷你图**

折线迷你图通过数据点绘制一条连续的线条，是显示随时间变化趋势的最自然的选择。在 Aspose.Cells 中，通过将 `SparklineType.Line` 传递给 `SparklineGroups.add` 方法来创建折线迷你图。

工作流程与其他迷你图类型相同：

1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 在源数据行（例如第 1 行，A 到 E 列）中填入您要可视化的值。
3. 构造一个 `CellArea`，描述将绘制迷你图的目标单元格。
4. 调用 `worksheet.SparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`。第三个参数 `false` 告诉 Aspose.Cells 数据区域是水平方向（一行），而不是垂直方向（一列）。
5. 可选地对返回的 `SparklineGroup` 进行自定义。对于折线迷你图，您可以使用 `group.Line.Color`（需要传入来自 `com.aspose.cells.Drawing` 的 `CellsColor`）来设置线条颜色，调整线条粗细，并切换高低点标记。
6. 保存工作簿。

以下示例创建一个工作簿，将值 5、-3、8、-2、6 写入单元格 A1 到 E1，并在单元格 F1 中添加一个跟踪这些值的折线迷你图。它还将线条颜色自定义为红色，并启用高点与低点的标记。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();

// 步骤 2：将示例值 5、-3、8、-2、6 写入单元格 A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);

// 步骤 3：构建一个指向目标单元格 F1 的 CellArea
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // 列 F（从 0 开始索引）
dest.setEndColumn(5);
dest.setStartRow(0);      // 第 1 行（从 0 开始索引）
dest.setEndRow(0);

// 步骤 4：从 A1:E1 添加一个折线迷你图到 F1
// SparklineGroups.Add 返回新添加组的索引
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(index);

// 步骤 5：创建一个红色 CellsColor 并将其分配给迷你图线条颜色
let red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);

// 步骤 6：启用高点标记和低点标记
group.setShowHighPoint(true);
group.setShowLowPoint(true);

// 步骤 7：保存工作簿
workbook.save("output_line.xlsx");
```

## **柱形迷你图**

柱形迷你图将每个数据点渲染为垂直条形。这使得它非常适合用于量级有意义的数据——例如，每月销售数据或计数。在 Aspose.Cells 中，通过将 `SparklineType.Column` 传递给 `SparklineGroups.add` 方法来创建柱形迷你图。

操作步骤与折线迷你图示例类似：

1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 在相同的源区域（A1:E1）中填入您要可视化的值。
3. 构造一个描述目标单元格的 `CellArea`。
4. 调用 `worksheet.SparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`。
5. 可选地对生成的 `SparklineGroup` 进行自定义——例如，通过将 `group.Type` 设置为指定类型来确认类型，或调整条形颜色。
6. 将工作簿保存到单独的输出文件，以免覆盖折线迷你图示例。

下面的示例将值 5、-3、8、-2、6 写入 A1:E1，并在 F1 中渲染一个柱形迷你图。负值绘制为向下的条形，正值绘制为向上的条形，这样正负贡献一目了然。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// 步骤 2：将样本值写入 A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// 步骤 3：构建一个指向 F1（列索引 5，行索引 0）的 CellArea
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// 步骤 4：将 Column 迷你图添加到目标单元格
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);

// 步骤 5：通过读取 group.Type 确认迷你图类型
console.log("Sparkline Type added: " + group.getType());

// 步骤 6：保存工作簿
workbook.save("output_column.xlsx");

console.log("Workbook saved as output_column.xlsx");
```

## **盈亏迷你图**

盈亏迷你图是柱形迷你图的一种特殊变体，用于仅显示两种结果：正值绘制为"上"条形（获胜），零或负值绘制为"下"条形（失败）。盈亏迷你图通常用于可视化胜负序列、通过/未通过结果或随时间变化的任何二元结果。

在 Aspose.Cells 中，通过将 `SparklineType.Stacked` 传递给 `SparklineGroups.add` 方法来创建盈亏迷你图。（尽管名称如此，`SparklineType.Stacked` 实际上是用于请求盈亏渲染的枚举值。）

操作步骤与其他两种类型相同：

1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 填充源区域。由于盈亏迷你图将每个值视为获胜或失败，因此值的大小并不重要——只有其符号才重要。正值变为向上条形，非正值变为向下条形。
3. 构造一个描述目标单元格的 `CellArea`。
4. 调用 `worksheet.SparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`。
5. 可选地对返回的 `SparklineGroup` 进行自定义，例如为获胜和失败条形设置强调色。
6. 使用不同的文件名保存工作簿，以便所有三个示例可以共存于磁盘上。

下面的示例使用与前两节相同的输入数据。值 5、-3、8、-2、6 被解释为胜、负、胜、负、胜——在 F1 中绘制的迷你图准确地反映了该模式。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");

// 第 2 步：在第 1 行填充示例数据：A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// 第 3 步：构建一个指向 F1（第 5 列，第 0 行）的 CellArea
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F
dest.setEndColumn(5);
dest.setStartRow(0);      // 第 1 行
dest.setEndRow(0);

// 第 4 步：添加 Win/Loss 迷你图（SparklineType.Stacked）
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest
);
let group = worksheet.getSparklineGroups().get(groupIndex);

// 第 5 步：自定义迷你图组
// 启用高点和低点标记
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// 将高点颜色设置为绿色
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.getGreen());
group.setHighPointColor(highColor);

// 将低点颜色设置为红色
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.getRed());
group.setLowPointColor(lowColor);

// 将负点颜色设置为橙色
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.getOrange());
group.setNegativePointsColor(negColor);

// 设置默认系列颜色（用于正值柱）
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.getSteelBlue());
group.setSeriesColor(seriesColor);

// 第 6 步：保存工作簿
workbook.save("output_winloss.xlsx");

console.log("工作簿已成功保存：output_winloss.xlsx");
```

## **组合所有三种迷你图类型**

前三个示例各自生成一个工作簿，以便可以单独查看输出文件。然而，在实际场景中，您通常希望并排比较多个数据系列。最简洁的方法是将多个迷你图组放入同一个工作表中，每组呈现不同的样式。

您可以将多个 `SparklineGroup` 对象添加到同一个 `SparklineGroupCollection` 中，每组可以针对不同的目标单元格或不同的区域。例如，您可以在 F1 放置一个折线迷你图，在 F2 放置一个柱形迷你图，在 F3 放置一个盈亏迷你图——它们都读取第 1 行中的相同源数据——这样读者即可看到同一组数字的三种不同可视化呈现。

下面的组合示例创建一个工作簿，在第 1 行中填入值 5、-3、8、-2、6，然后在 F1、F2 和 F3 单元格中添加三个迷你图组——每种类型一个——从而生成的文件可以一次演示所有三种迷你图样式。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// 步骤 2：在第 1 行 (A1:E1) 填充示例数据
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// 步骤 3：在 F1 添加一个折线迷你图组
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// 通过 CellsColor 自定义折线迷你图颜色
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);

// 步骤 4：在 F2 添加一个柱形迷你图组
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// 自定义柱形迷你图系列颜色
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);

// 步骤 5：在 F3 添加一个涨跌（堆叠）迷你图组
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// 自定义涨跌迷你图系列颜色
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);

// 步骤 6：保存工作簿
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

当您在单个工作表中组合多个迷你图组时，每组是独立的。它们可以共享相同的源区域或使用不同的源区域，并且可以独立设置样式。这使得在现有工作表内直接构建一个小型"仪表板"式的单元格内可视化变得很容易。

{{% /alert %}}

## **自定义迷你图外观**

一旦创建了 `SparklineGroup` 并将其添加到 `worksheet.SparklineGroups` 中，您可以在保存工作簿之前读取或修改其多个视觉属性。最常自定义的属性包括：

- **`group.Type`** —— `SparklineType`（Line、Column 或 Stacked）。它在组添加时设置，但您可以读回以进行确认。
- **`group.Line.Color`** —— 线条颜色，以通过 `workbook.createCellsColor()` 创建的 `CellsColor` 表示。这是用于设置折线迷你图描边颜色的属性。
- **`group.Line.Weight`** —— 以磅为单位的线条粗细。值越大，线条越粗。
- **高低点标记** —— 标志，用于在最高和最低数据点上开启小标记，便于强调极值。
- **首/末/负点标记** —— 标志，用于在第一个、最后一个和负数据点上切换标记。

要更改颜色，请始终创建 `CellsColor` 实例并将其分配给相关属性。不要将 `java.awt.Color` 直接分配给迷你图颜色属性——它们需要来自 `com.aspose.cells.Drawing` 的 `CellsColor` 类型。`SparklineGroups.add` 方法本身返回一个完全类型化的 `SparklineGroup` 对象，因此您可以在返回值上链式分配属性，或将其存储在局部变量中，在保存前进行自定义。

{{< app/cells/assistant language="javascript" >}}