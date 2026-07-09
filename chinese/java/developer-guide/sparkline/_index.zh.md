---
title: 在 Aspose.Cells for Java 中创建迷你图
linktitle: Sparklines
description: Aspose.Cells 是一个用于处理电子表格文件的 Java 库，支持创建迷你图——放置在工作表单元格中的小型图表。本文介绍如何使用 Aspose.Cells 库添加和自定义折线、柱形和盈亏迷你图。
keywords: Aspose.Cells, Java 库, 电子表格, 迷你图, 折线迷你图, 柱形迷你图, 盈亏迷你图, SparklineGroup, SparklineType
type: docs
weight: 195
url: /zh/java/creating-sparklines/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 支持在工作表单元格内创建迷你图。迷你图是适合放在单个单元格内的小型图表，可以快速直观地展示数据趋势。Aspose.Cells 支持折线、柱形和盈亏迷你图，每种类型都可以自定义颜色、线条粗细、高/低点和标记。

{{% /alert %}}

## **简介**

迷你图是单元格内的小型图表，当您希望在数据行或列旁边快速显示趋势而又不占用完整图表的空间时，它们非常有用。Excel 支持三种迷你图：**折线**、**柱形**和**盈亏**。Aspose.Cells 通过 `Aspose.Cells.Charts` 命名空间中的 `SparklineGroup` 和 `SparklineGroupCollection` API 提供了此功能。

在 Aspose.Cells 中，您添加的每个迷你图都是通过 `worksheet.getSparklineGroups().add(...)` 创建的，该方法返回一个 `SparklineGroup` 对象。然后您可以使用该对象来设置迷你图类型、数据区域、目标单元格以及视觉属性，例如线条颜色、线条粗细、标记和高/低点指示符。

{{% alert color="primary" %}}

单个 `SparklineGroup` 可以包含一个或多个共享相同样式的迷你图。当您调用 `add` 并传入一行数据和一个目标单元格时，该单元格内将生成一个迷你图。如果目标区域宽度超过一个单元格，则每个目标单元格中将绘制一个独立的迷你图，所有迷你图都使用相同的样式和数据区域。

{{% /alert %}}

本文将逐步介绍 Aspose.Cells 支持的三种迷你图类型——**折线**、**柱形**和**盈亏**——并演示如何添加它们、自定义其颜色以及保存生成的工作簿。

## **折线迷你图**

折线迷你图通过数据系列中的各个数据点绘制一条连续的线，是显示随时间变化趋势的最自然选择。在 Aspose.Cells 中，通过将 `SparklineType.LINE` 传递给 `add` 方法即可创建折线迷你图。

其工作流程与任何其他迷你图类型相同：

1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 在一行源数据（例如第 1 行，A 列到 E 列）中填充您要可视化的值。
3. 构建一个 `CellArea`，描述将绘制迷你图的目标单元格。
4. 调用 `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`。第三个参数 `false` 告诉 Aspose.Cells 数据区域是水平的（一行），而不是垂直的（一列）。
5. 可选地对返回的 `SparklineGroup` 进行自定义。对于折线迷你图，您可以使用 `group.getLine().setColor(...)`（它需要来自 `Aspose.Cells.Drawing` 的 `CellsColor`）设置线条颜色，调整线条粗细，并切换高/低点标记。
6. 保存工作簿。

以下示例创建一个工作簿，将值 5、-3、8、-2、6 写入单元格 A1 到 E1，并在单元格 F1 中添加一条折线迷你图来描绘这些值。它还将线条颜色自定义为红色，并启用高点和低点的标记。

```java
public class CodeRunner {
    public static void main(String[] args) {
        try {
            // 步骤 1：创建一个 Workbook 并获取第一个工作表
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.getWorksheets().get(0);
            Cells cells = worksheet.getCells();

            // 步骤 2：将示例值 5、-3、8、-2、6 写入单元格 A1:E1
            cells.get("A1").putValue(5);
            cells.get("B1").putValue(-3);
            cells.get("C1").putValue(8);
            cells.get("D1").putValue(-2);
            cells.get("E1").putValue(6);

            // 步骤 3：构建一个指向目标单元格 F1 的 CellArea
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // F 列（从 0 开始索引）
            dest.EndColumn = 5;
            dest.StartRow = 0;      // 第 1 行（从 0 开始索引）
            dest.EndRow = 0;

            // 步骤 4：从 A1:E1 添加一个 Line 迷你图到 F1
            // SparklineGroups.add 返回新添加分组的索引
            int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
            SparklineGroup group = worksheet.getSparklineGroups().get(index);

            // 步骤 5：创建一个红色的 CellsColor 并将其分配给迷你图线条颜色
            CellsColor red = workbook.createCellsColor();
            red.setColor(com.aspose.cells.Color.getRed());
            group.setSeriesColor(red);

            // 步骤 6：启用高点标记和低点标记
            group.setShowHighPoint(true);
            group.setShowLowPoint(true);

            // 步骤 7：保存工作簿
            workbook.save("output_line.xlsx");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

## **柱形迷你图**

柱形迷你图将每个数据点渲染为垂直条形。这使它非常适合那些数值大小具有意义的数据——例如每月销售额或计数。在 Aspose.Cells 中，通过将 `SparklineType.COLUMN` 传递给 `add` 方法即可创建柱形迷你图。

其步骤与折线迷你图示例相同：

1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 在同一源区域（A1:E1）中填充您要可视化的值。
3. 构建一个 `CellArea`，描述目标单元格。
4. 调用 `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`。
5. 可选地对生成的 `SparklineGroup` 进行自定义——例如，通过将 `group.getType()` 设置为确认类型，或调整条形颜色。
6. 将工作簿保存到单独的输出文件，以避免覆盖折线迷你图示例。

以下示例将值 5、-3、8、-2、6 写入 A1:E1，并在 F1 中渲染柱形迷你图。负值绘制为向下的条形，正值绘制为向上的条形，这样一眼就能轻松分辨出正值和负值的贡献。

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// 将示例值写入 A1:E1
int[] values = new int[] { 5, -3, 8, -2, 6 };
for (int i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// 构造一个指向 F1（列索引 5，行索引 0）的 CellArea
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// 在目标单元格添加一个柱形迷你图
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);

// 通过读取 group.Type 确认迷你图类型
System.out.println("Sparkline Type added: " + group.getType());

// 保存工作簿
workbook.save("output_column.xlsx");

System.out.println("Workbook saved as output_column.xlsx");
```

## **盈亏迷你图**

盈亏迷你图是柱形迷你图的一种特殊变体，用于仅显示两种结果：正值绘制为"上升"条形（赢），零或负值绘制为"下降"条形（亏）。盈亏迷你图通常用于可视化胜负序列、通过/失败结果或一段时间内的任何二元结果。

在 Aspose.Cells 中，通过将 `SparklineType.STACKED` 传递给 `add` 方法即可创建盈亏迷你图。（尽管名称如此，`SparklineType.STACKED` 是用于请求盈亏渲染的枚举值。）

其步骤与其他两种类型相同：

1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 填充源区域。由于盈亏迷你图将每个值视为赢或亏，因此值的大小无关紧要——只有其符号才重要。正值变为上升条形，非正值变为下降条形。
3. 构建一个 `CellArea`，描述目标单元格。
4. 调用 `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`。
5. 可选地对返回的 `SparklineGroup` 进行自定义，例如为盈亏条形设置强调颜色。
6. 使用不同的文件名保存工作簿，以便所有三个示例可以并存于磁盘上。

以下示例使用与前两节相同的输入数据。值 5、-3、8、-2、6 被解释为赢、亏、赢、亏、赢——在 F1 中绘制的迷你图准确反映了这一模式。

```java
import com.aspose.cells.*;
import com.aspose.cells.charts.*;
import com.aspose.cells.drawing.*;
import java.awt.Color;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");

// 填充示例数据
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// 构建一个指向 F1（第 5 列，第 0 行）的 CellArea
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// 添加一个 Win/Loss 迷你图（SparklineType.Stacked）
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);

// 自定义迷你图组
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// 将高点颜色设置为绿色
CellsColor highColor = workbook.createCellsColor();
highColor.setColor(Color.GREEN);
group.setHighPointColor(highColor);

// 将低点颜色设置为红色
CellsColor lowColor = workbook.createCellsColor();
lowColor.setColor(Color.RED);
group.setLowPointColor(lowColor);

// 将负点颜色设置为橙色
CellsColor negColor = workbook.createCellsColor();
negColor.setColor(Color.ORANGE);
group.setNegativePointsColor(negColor);

// 设置默认系列颜色（用于正条）
CellsColor seriesColor = workbook.createCellsColor();
seriesColor.setColor(new Color(70, 130, 180)); // 近似 SteelBlue 颜色
group.setSeriesColor(seriesColor);

// 保存工作簿
workbook.save("output_winloss.xlsx");

System.out.println("Workbook saved successfully: output_winloss.xlsx");
```

## **组合使用所有三种迷你图类型**

前三个示例各自生成一个工作簿，以便于单独检查输出文件。然而，在实际场景中，您通常会希望并排比较多个数据系列。最简洁的方法是将多个迷你图组放入同一个工作表中，每组使用不同的样式进行渲染。

您可以将多个 `SparklineGroup` 对象添加到同一个 `SparklineGroupCollection` 中，每组可以针对不同的目标单元格或不同的区域。例如，您可以在 F1 中放置折线迷你图，在 F2 中放置柱形迷你图，在 F3 中放置盈亏迷你图——所有这些都从第 1 行中的同一源数据读取——以便读者可以同时看到同一数字的三种不同可视化呈现。

下面的综合示例创建一个工作簿，在第 1 行中填充值 5、-3、8、-2、6，然后在 F1、F2 和 F3 单元格中添加三个迷你图组——每种类型一个——因此生成的文件一次性展示了所有三种迷你图样式。

```java
import com.aspose.cells.*;

// 第 1 步：创建一个 Workbook 并获取第一个工作表
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// 第 2 步：在第 1 行 (A1:E1) 填充示例数据
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// 第 3 步：在 F1 位置添加一个折线迷你图组
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5); // 修复：使用静态工厂方法
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// 通过 CellsColor 自定义折线迷你图颜色
CellsColor lineColor = workbook.createCellsColor();
lineColor.setColor(com.aspose.cells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);

// 第 4 步：在 F2 位置添加一个柱形迷你图组
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // 修复：使用静态工厂方法
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// 自定义柱形迷你图系列颜色
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);

// 第 5 步：在 F3 位置添加一个胜负（堆叠）迷你图组
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // 修复：使用静态工厂方法
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// 自定义胜负迷你图系列颜色
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);

// 第 6 步：保存工作簿
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

当您在单个工作表中组合多个迷你图组时，每个组都是独立的。它们可以共享同一源区域或使用不同的源区域，并且可以独立设置样式。这使得直接在现有工作表中构建一个小的单元格内可视化"仪表板"变得非常容易。

{{% /alert %}}

## **自定义迷你图外观**

一旦创建了 `SparklineGroup` 并将其添加到 `worksheet.getSparklineGroups()` 中，您可以在保存工作簿之前读取或修改其多个视觉属性。最常用的自定义属性包括：

- **`group.getType()`** —— `SparklineType`（LINE、COLUMN 或 STACKED）。在添加组时设置，但您可以读回以确认。
- **`group.getLine().setColor(...)`** —— 线条颜色，表示为通过 `workbook.createCellsColor()` 创建的 `CellsColor`。这是用于折线迷你图描边颜色的属性。
- **`group.getLine().setWeight(...)`** —— 线条粗细（以磅为单位）。值越大，线条越粗。
- **高/低点标记** —— 用于在最高和最低数据点上显示小标记的标志，对于强调极值非常有用。
- **首/末/负点标记** —— 用于在第一个、最后一个和负数据点上切换标记的标志。

要更改颜色，请始终创建一个 `CellsColor` 实例并将其分配给相关属性。不要直接将 `java.awt.Color` 分配给迷你图颜色属性——它们期望来自 `Aspose.Cells.Drawing` 的 `CellsColor` 类型。`add` 方法本身返回一个完全类型化的 `SparklineGroup` 对象，因此您可以在返回值上链式分配属性，或将其存储在本地变量中并在保存前进行自定义。



{{< app/cells/assistant language="java" >}}