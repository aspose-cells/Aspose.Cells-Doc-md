---
title: Aspose.Cells for Python via Java 中的迷你图
linktitle: Sparklines
description: Aspose.Cells 是一个用于处理电子表格文件的 Python via Java 库，支持创建迷你图——放置在工作表单元格内的小型图表。本文介绍如何使用 Aspose.Cells 库添加和自定义折线、柱形和盈亏迷你图。
keywords: Aspose.Cells, Python via Java 库, 电子表格, 迷你图, 折线迷你图, 柱形迷你图, 盈亏迷你图, SparklineGroup, SparklineType
type: docs
weight: 195
url: /zh/python-java/creating-sparklines/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 支持在工作表单元格内创建迷你图。迷你图是适合放在单个单元格内的小型图表，可以快速直观地展示数据趋势。Aspose.Cells 支持折线、柱形和盈亏迷你图，并且每种类型都可以自定义颜色、线条粗细、高/低点和标记。

{{% /alert %}}

## **简介**

迷你图是单元格内的小型图表，当您希望在数据行或列旁边快速显示趋势而又不占用完整图表空间时非常有用。Excel 支持三种迷你图：**折线**、**柱形**和**盈亏**。Aspose.Cells 通过 `Aspose.Cells.Charts` 命名空间中的 `SparklineGroup` 和 `SparklineGroupCollection` API 提供了同样的功能。

在 Aspose.Cells 中，您添加的每个迷你图都是通过 `worksheet.getSparklineGroups().add(...)` 创建的，该方法返回一个 `SparklineGroup` 对象。然后，您可以使用该对象设置迷你图类型、数据区域、目标单元格以及线条颜色、线条粗细、标记和高/低点指示符等视觉属性。

{{% alert color="primary" %}}

单个 `SparklineGroup` 可以包含一个或多个共享相同样式的迷你图。当您调用 `add` 并传入一行数据和一个目标单元格时，您将在该单元格内获得一个迷你图。如果您的目标区域宽度大于一个单元格，则会在每个目标单元格中分别绘制一个迷你图，所有迷你图都使用相同的样式和数据区域。

{{% /alert %}}

本文将逐步介绍 Aspose.Cells 支持的三种迷你图类型——**折线**、**柱形**和**盈亏**——并演示如何添加它们、自定义颜色以及保存生成的工作簿。

## **折线迷你图**

折线迷你图通过连续线条连接序列中的数据点，是显示随时间变化趋势的最自然选择。在 Aspose.Cells 中，通过将 `SparklineType.LINE` 传递给 `add` 方法来创建折线迷你图。

操作流程与其他迷你图类型相同：

1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 用要可视化的值填充一行源数据（例如，第 1 行，A 到 E 列）。
3. 构建一个 `CellArea`，描述将要绘制迷你图的目标单元格。
4. 调用 `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`。第三个参数 `false` 告诉 Aspose.Cells 数据区域是水平方向（一行），而不是垂直方向（一列）。
5. 可选地自定义返回的 `SparklineGroup`。对于折线迷你图，您可以使用 `group.getLine().getColor()` 设置线条颜色（该方法需要来自 `Aspose.Cells.Drawing` 的 `CellsColor`），调整线条粗细，并切换高/低点标记。
6. 保存工作簿。

以下示例创建一个工作簿，将值 5、-3、8、-2、6 写入单元格 A1 到 E1，并在单元格 F1 中添加一个折线迷你图来跟踪这些值。它还会将线条颜色自定义为红色，并启用高/低点的标记。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, SparklineType
from java.awt import Color

# 步骤 1：创建一个 Workbook 并获取第一个工作表
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()

# 步骤 2：将示例值 5、-3、8、-2、6 写入单元格 A1:E1
cells.get("A1").putValue(5)
cells.get("B1").putValue(-3)
cells.get("C1").putValue(8)
cells.get("D1").putValue(-2)
cells.get("E1").putValue(6)

# 步骤 3：构建一个指向目标单元格 F1 的 CellArea
dest = CellArea()
dest.setStartColumn(5)  # F 列（从 0 开始索引）
dest.setEndColumn(5)
dest.setStartRow(0)     # 第 1 行（从 0 开始索引）
dest.setEndRow(0)

# 步骤 4：在 A1:E1 区域添加一个折线迷你图，并将其放入 F1
# SparklineGroups.add 返回新添加分组的索引
index = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(index)

# 步骤 5：创建一个红色的 CellsColor，并将其分配给迷你图折线颜色
red = workbook.createCellsColor()
red.setColor(Color.RED)
group.setSeriesColor(red)

# 步骤 6：启用高点标记和低点标记
group.setShowHighPoint(True)
group.setShowLowPoint(True)

# 步骤 7：保存工作簿
workbook.save("output_line.xlsx")

jpype.shutdownJVM()
```

## **柱形迷你图**

柱形迷你图将每个数据点呈现为垂直条形。这种方式非常适合数据量值有意义的场景——例如每月销售数据或计数。在 Aspose.Cells 中，通过将 `SparklineType.COLUMN` 传递给 `add` 方法来创建柱形迷你图。

该过程与折线迷你图示例相同：

1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 用要可视化的值填充相同的源区域 (A1:E1)。
3. 构建一个 `CellArea` 来描述目标单元格。
4. 调用 `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`。
5. 可选地自定义生成的 `SparklineGroup`——例如，通过设置 `group.getType()` 确认类型，或调整条形颜色。
6. 将工作簿保存到单独的输出文件，以免覆盖折线迷你图示例。

下面的示例将值 5、-3、8、-2、6 写入 A1:E1，并在 F1 中渲染柱形迷你图。负值绘制为向下的条形，正值绘制为向上的条形，这样一眼就能区分正负贡献。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType

# 步骤 1：创建一个 Workbook 并获取第一个工作表
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# 步骤 2：将示例值写入 A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.getCells().get(0, i).putValue(values[i])

# 步骤 3：构建一个指向 F1（列索引 5，行索引 0）的 CellArea
dest = CellArea()
dest.setStartColumn(5)
dest.setEndColumn(5)
dest.setStartRow(0)
dest.setEndRow(0)

# 步骤 4：向目标单元格添加一个 Column 类型的迷你图
idx = worksheet.getSparklineGroups().add(
    SparklineType.Column, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(idx)

# 步骤 5：通过读取 group.Type 来确认迷你图类型
print("Sparkline Type added: " + str(group.getType()))

# 步骤 6：保存工作簿
workbook.save("output_column.xlsx")

print("Workbook saved as output_column.xlsx")

jpype.shutdownJVM()
```

## **盈亏迷你图**

盈亏迷你图是柱形迷你图的一种特殊变体，用于仅显示两种结果：正值绘制为"上升"条形（盈），零或负值绘制为"下降"条形（亏）。盈亏迷你图通常用于可视化胜负序列、通过/未通过结果，或任何随时间变化的二元结果。

在 Aspose.Cells 中，通过将 `SparklineType.STACKED` 传递给 `add` 方法来创建盈亏迷你图。（尽管名称如此，`SparklineType.STACKED` 实际是用于请求盈亏渲染的枚举值。）

该过程与其他两种类型相同：

1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 填充源区域。因为盈亏迷你图将每个值视为盈或亏，所以值的大小并不重要——只有其符号才有意义。正值变为上升条形，非正值变为下降条形。
3. 构建一个 `CellArea` 来描述目标单元格。
4. 调用 `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`。
5. 可选地自定义返回的 `SparklineGroup`，例如为盈亏条形设置强调色。
6. 使用不同的文件名保存工作簿，以便所有三个示例可以同时存在于磁盘上。

下面的示例使用与前两节相同的输入数据。值 5、-3、8、-2、6 被解释为盈、亏、盈、亏、盈——在 F1 中绘制的迷你图正好反映了该模式。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, CellsColor, Color

# 步骤 1：创建 Workbook 并获取第一个工作表
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("WinLoss")

# 步骤 2：在第 1 行填充示例数据：A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# 步骤 3：构建一个指向 F1 的 CellArea（第 5 列，第 0 行）
dest = CellArea()
dest.setStartColumn(5)   # F
dest.setEndColumn(5)
dest.setStartRow(0)      # 第 1 行
dest.setEndRow(0)

# 步骤 4：添加 Win/Loss 迷你图（SparklineType.Stacked）
groupIndex = worksheet.getSparklineGroups().add(
    SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.getSparklineGroups().get(groupIndex)

# 步骤 5：自定义迷你图组
# 启用最高点和最低点标记
group.setShowHighPoint(True)
group.setShowLowPoint(True)
group.setShowNegativePoints(True)

# 将最高点颜色设置为绿色
highColor = workbook.createCellsColor()
highColor.setColor(Color.GREEN)
group.setHighPointColor(highColor)

# 将最低点颜色设置为红色
lowColor = workbook.createCellsColor()
lowColor.setColor(Color.RED)
group.setLowPointColor(lowColor)

# 将负点颜色设置为橙色
negColor = workbook.createCellsColor()
negColor.setColor(Color.ORANGE)
group.setNegativePointsColor(negColor)

# 设置默认系列颜色（用于正值条）
seriesColor = workbook.createCellsColor()
seriesColor.setColor(Color.STEELBLUE)
group.setSeriesColor(seriesColor)

# 步骤 6：保存工作簿
workbook.save("output_winloss.xlsx")

print("Workbook saved successfully: output_winloss.xlsx")

jpype.shutdownJVM()
```

## **组合使用三种迷你图类型**

前三个示例各自生成一个工作簿，这样输出文件易于单独查看。然而，在实际场景中，您通常会希望并排比较多个数据序列。最简洁的方法是在同一工作表中放置多个迷你图组，每组呈现不同的样式。

您可以将多个 `SparklineGroup` 对象添加到同一个 `SparklineGroupCollection` 中，每组可以针对不同的目标单元格或不同的区域。例如，您可以在 F1 中放置折线迷你图，在 F2 中放置柱形迷你图，在 F3 中放置盈亏迷你图——全部读取第 1 行中相同的源数据——这样读者就可以看到同一组数字的三种不同视觉呈现方式。

下面的组合示例创建一个工作簿，将第 1 行填充为值 5、-3、8、-2、6，然后在单元格 F1、F2 和 F3 中添加三个迷你图组——每种类型各一个——以便生成的文件能同时展示所有三种迷你图样式。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, CellsColor, SparklineType
from java.awt import Color

# 步骤 1：创建工作簿并获取第一个工作表
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# 步骤 2：在第 1 行 (A1:E1) 填充示例数据
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# 步骤 3：在 F1 位置添加折线迷你图组
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", False, lineArea)
lineGroup = worksheet.getSparklineGroups().get(lineIdx)

# 通过 CellsColor 自定义折线迷你图颜色
lineColor = workbook.createCellsColor()
lineColor.setColor(Color.BLUE)
lineGroup.setSeriesColor(lineColor)

# 步骤 4：在 F2 位置添加柱形迷你图组
columnArea = CellArea()
columnArea.setStartColumn(5)
columnArea.setEndColumn(5)
columnArea.setStartRow(1)
columnArea.setEndRow(1)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", False, columnArea)
columnGroup = worksheet.getSparklineGroups().get(columnIdx)

# 自定义柱形迷你图系列颜色
columnColor = workbook.createCellsColor()
columnColor.setColor(Color.GREEN)
columnGroup.setSeriesColor(columnColor)

# 步骤 5：在 F3 位置添加盈亏（堆叠）迷你图组
stackedArea = CellArea()
stackedArea.setStartColumn(5)
stackedArea.setEndColumn(5)
stackedArea.setStartRow(2)
stackedArea.setEndRow(2)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", False, stackedArea)
stackedGroup = worksheet.getSparklineGroups().get(stackedIdx)

# 自定义盈亏迷你图系列颜色
stackedColor = workbook.createCellsColor()
stackedColor.setColor(Color(255, 140, 0))  # 深橙色
stackedGroup.setSeriesColor(stackedColor)

# 步骤 6：保存工作簿
workbook.save("output_all.xlsx")

jpype.shutdownJVM()
```

{{% alert color="primary" %}}

当您在单个工作表中组合多个迷你图组时，每组都是独立的。它们可以共享相同的源区域或使用不同的源区域，并且可以独立设置样式。这使得在现有工作表中直接构建一个单元格内可视化的"小型仪表板"变得非常容易。

{{% /alert %}}

## **自定义迷你图外观**

创建 `SparklineGroup` 并将其添加到 `worksheet.getSparklineGroups()` 后，您可以在保存工作簿之前读取或修改其若干视觉属性。最常自定义的属性包括：

- **`group.getType()`** — `SparklineType` 类型（LINE、COLUMN 或 STACKED）。它在添加组时设置，但您可以读取以确认。
- **`group.getLine().getColor()`** — 线条颜色，通过 `workbook.createCellsColor()` 创建的 `CellsColor` 表示。这是用于设置折线迷你图描边颜色的属性。
- **`group.getLine().getWeight()`** — 线条粗细（以磅为单位）。值越大线条越粗。
- **高/低点标记** — 用于在最高和最低数据点上显示小标记的标志，适合强调极值。
- **首/尾/负值点标记** — 用于在第一个、最后一个和负数据点上切换标记的标志。

要更改颜色，请始终创建 `CellsColor` 实例并将其分配给相关属性。不要将 `java.awt.Color` 直接分配给迷你图颜色属性——它们需要来自 `Aspose.Cells.Drawing` 的 `CellsColor` 类型。`add` 方法本身返回一个完整类型的 `SparklineGroup` 对象，因此您可以在返回值上链接属性赋值，或将其存储在本地变量中，在保存之前进行自定义。



{{< app/cells/assistant language="python" >}}