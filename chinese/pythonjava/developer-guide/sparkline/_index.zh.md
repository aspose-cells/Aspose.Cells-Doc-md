---
title: Aspose.Cells for Python via Java 中的迷你图
linktitle: Aspose.Cells for Python via Java 中的迷你图
description: Aspose.Cells 是一个用于处理电子表格文件的 Python via Java 库，支持创建迷你图——放置在工作表单元格内的微型图表。本文介绍如何使用 Aspose.Cells 库添加和自定义折线、柱形和盈亏迷你图。
keywords: Aspose.Cells, Python via Java 库, 电子表格, 迷你图, 折线迷你图, 柱形迷你图, 盈亏迷你图, SparklineGroup, SparklineType
type: docs
weight: 195
url: /zh/python-java/creating-sparklines/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持在工作表单元格内创建迷你图。迷你图是适合放在单个单元格中的微型图表，可以快速直观地展示数据趋势。Aspose.Cells 支持折线、柱形和盈亏迷你图，并且每种类型都可以针对颜色、线条粗细、高低点以及标记进行自定义。

## **简介**
迷你图是单元格内的小型图表，当您希望在数据行或列旁边显示快速趋势而又不占用完整图表的空间时，它们非常有用。Excel 支持三种迷你图：**折线**、**柱形**和**盈亏**。Aspose.Cells 通过 `Aspose.Cells.Charts` 命名空间中的 `SparklineGroup` 和 `SparklineGroupCollection` API 提供同样的功能。
在 Aspose.Cells 中，您添加的每个迷你图都是通过 `worksheet.getSparklineGroups().add(...)` 创建的，该方法会返回一个 `SparklineGroup` 对象。然后您可以使用该对象设置迷你图类型、数据区域、目标单元格以及视觉属性，如线条颜色、线条粗细、标记和最高/最低点指示器。
本文将逐一介绍 Aspose.Cells 支持的三种迷你图类型——**折线**、**柱形**和**盈亏**——并展示如何添加它们、自定义颜色以及保存生成的工作簿。

## **折线迷你图**
折线迷你图通过数据系列中的各数据点绘制一条连续的线条，是显示随时间变化趋势最自然的选择。在 Aspose.Cells 中，通过将 `SparklineType.LINE` 传递给 `add` 方法来创建折线迷你图。
1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 在一行源数据（例如第 1 行的 A 到 E 列）中填充您希望可视化的值。
3. 构建一个 `CellArea` 来描述将绘制迷你图的目标单元格。
4. 调用 `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`。第三个参数 `false` 告诉 Aspose.Cells 数据区域是水平方向（一行），而不是垂直方向（一列）。
5. 根据需要自定义返回的 `SparklineGroup`。对于折线迷你图，您可以使用 `group.getLine().getColor()` 设置线条颜色（该方法期望来自 `Aspose.Cells.Drawing` 的 `CellsColor`），调整线条粗细，并切换最高/最低点标记。
6. 保存工作簿。
下面的示例创建一个工作簿，将值 5、-3、8、-2、6 写入单元格 A1 到 E1，并在单元格 F1 中添加一条折线迷你图以描绘这些值。它还将线条颜色自定义为红色，并启用最高点和最低点的标记。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, SparklineType
from java.awt import Color
# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
# Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").putValue(5)
cells.get("B1").putValue(-3)
cells.get("C1").putValue(8)
cells.get("D1").putValue(-2)
cells.get("E1").putValue(6)
# Step 3: Build a CellArea pointing to destination cell F1
dest = CellArea()
dest.setStartColumn(5)  # column F (0-indexed)
dest.setEndColumn(5)
dest.setStartRow(0)     # row 1 (0-indexed)
dest.setEndRow(0)
# Step 4: Add a Line sparkline from A1:E1 into F1
# SparklineGroups.add returns the index of the newly added group
index = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(index)
# Step 5: Create a red CellsColor and assign it to the sparkline line color
red = workbook.createCellsColor()
red.setColor(Color.RED)
group.setSeriesColor(red)
# Step 6: Enable high-point and low-point markers
group.setShowHighPoint(True)
group.setShowLowPoint(True)
# Step 7: Save the workbook
workbook.save("output_line.xlsx")
jpype.shutdownJVM()
```

## **柱形迷你图**
柱形迷你图将每个数据点渲染为一个垂直条形。这使得它非常适合数据幅度有意义的场景，例如月度销售数字或计数。在 Aspose.Cells 中，通过将 `SparklineType.COLUMN` 传递给 `add` 方法来创建柱形迷你图。
其步骤与折线迷你图示例类似：
1. 创建一个新的 `Workbook` 并访问第一个工作表。
3. 构建一个 `CellArea` 来描述目标单元格。
4. 调用 `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`。
5. 根据需要自定义返回的 `SparklineGroup`——例如通过设置 `group.getType()` 来确认类型，或者调整柱形颜色。
6. 将工作簿保存到单独的输出文件，以免覆盖折线迷你图示例。
下面的示例将值 5、-3、8、-2、6 写入 A1:E1，并在 F1 中渲染一个柱形迷你图。负值被绘制为向下的柱形，正值被绘制为向上的柱形，这样可以一目了然地分辨出正向和负向贡献。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType
# 步骤 1: 创建一个 Workbook 并获取第一个工作表
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# 步骤 2: 将示例值写入 A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.getCells().get(0, i).putValue(values[i])
# 步骤 3: 构建一个指向 F1（列索引 5，行索引 0）的 CellArea
dest = CellArea()
dest.setStartColumn(5)
dest.setEndColumn(5)
dest.setStartRow(0)
dest.setEndRow(0)
# 步骤 4: 在目标单元格添加一个 Column 迷你图
idx = worksheet.getSparklineGroups().add(
    SparklineType.Column, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(idx)
# 步骤 5: 通过读取 group.Type 确认迷你图类型
print("Sparkline Type added: " + str(group.getType()))
# 步骤 6: 保存工作簿
workbook.save("output_column.xlsx")
print("Workbook saved as output_column.xlsx")
jpype.shutdownJVM()
```

## **盈亏迷你图**
盈亏迷你图是柱形迷你图的一种特殊变体，专为仅显示两种结果而设计：正值绘制为"向上"柱形（赢），零或负值绘制为"向下"柱形（亏）。盈亏迷你图通常用于可视化一系列的胜负、通过/未通过结果，或随时间变化的任何二元结果。
在 Aspose.Cells 中，通过将 `SparklineType.STACKED` 传递给 `add` 方法来创建盈亏迷你图。（尽管名称如此，`SparklineType.STACKED` 是用于请求盈亏渲染的枚举值。）
1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 填充源区域。因为盈亏迷你图将每个值视为赢或亏，所以值的大小并不重要，只有其符号才重要。正值变成向上柱形，非正值变成向下柱形。
3. 构建一个 `CellArea` 来描述目标单元格。
4. 调用 `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`。
5. 根据需要自定义返回的 `SparklineGroup`，例如为赢柱形和亏柱形设置强调色。
6. 使用不同的文件名保存工作簿，以便三个示例可以共存于磁盘上。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, CellsColor, Color
# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("WinLoss")
# Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)
# Step 3: Build a CellArea pointing to F1 (column 5, row 0)
dest = CellArea()
dest.setStartColumn(5)   # F
dest.setEndColumn(5)
dest.setStartRow(0)      # row 1
dest.setEndRow(0)
# Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
groupIndex = worksheet.getSparklineGroups().add(
    SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.getSparklineGroups().get(groupIndex)
# Step 5: Customize the sparkline group
# Enable high-point and low-point markers
group.setShowHighPoint(True)
group.setShowLowPoint(True)
group.setShowNegativePoints(True)
# Set the high-point color to green
highColor = workbook.createCellsColor()
highColor.setColor(Color.GREEN)
group.setHighPointColor(highColor)
# Set the low-point color to red
lowColor = workbook.createCellsColor()
lowColor.setColor(Color.RED)
group.setLowPointColor(lowColor)
# Set the negative-point color to orange
negColor = workbook.createCellsColor()
negColor.setColor(Color.ORANGE)
group.setNegativePointsColor(negColor)
# Set the default series color (used for positive bars)
seriesColor = workbook.createCellsColor()
seriesColor.setColor(Color.STEELBLUE)
group.setSeriesColor(seriesColor)
# Step 6: Save the workbook
workbook.save("output_winloss.xlsx")
print("Workbook saved successfully: output_winloss.xlsx")
jpype.shutdownJVM()
```

## **组合三种迷你图类型**
下面的组合示例创建一个工作簿，在第 1 行填充值 5、-3、8、-2、6，然后在单元格 F1、F2 和 F3 中添加三个迷你图组——每种类型各一个——这样生成的文件可以一次性展示所有三种迷你图样式。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, CellsColor, SparklineType
from java.awt import Color
# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Step 2: Populate sample data in row 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)
# Step 3: Add a Line sparkline group at F1
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", False, lineArea)
lineGroup = worksheet.getSparklineGroups().get(lineIdx)
# Customize the line sparkline color via CellsColor
lineColor = workbook.createCellsColor()
lineColor.setColor(Color.BLUE)
lineGroup.setSeriesColor(lineColor)
# Step 4: Add a Column sparkline group at F2
columnArea = CellArea()
columnArea.setStartColumn(5)
columnArea.setEndColumn(5)
columnArea.setStartRow(1)
columnArea.setEndRow(1)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", False, columnArea)
columnGroup = worksheet.getSparklineGroups().get(columnIdx)
# Customize the column sparkline series color
columnColor = workbook.createCellsColor()
columnColor.setColor(Color.GREEN)
columnGroup.setSeriesColor(columnColor)
# Step 5: Add a Win/Loss (Stacked) sparkline group at F3
stackedArea = CellArea()
stackedArea.setStartColumn(5)
stackedArea.setEndColumn(5)
stackedArea.setStartRow(2)
stackedArea.setEndRow(2)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", False, stackedArea)
stackedGroup = worksheet.getSparklineGroups().get(stackedIdx)
# Customize the win/loss sparkline series color
stackedColor = workbook.createCellsColor()
stackedColor.setColor(Color(255, 140, 0))  # DarkOrange
stackedGroup.setSeriesColor(stackedColor)
# Step 6: Save the workbook
workbook.save("output_all.xlsx")
jpype.shutdownJVM()
```

## **自定义迷你图外观**
创建 `SparklineGroup` 并将其添加到 `worksheet.getSparklineGroups()` 后，您可以在保存工作簿之前读取或修改其多个视觉属性。最常自定义的属性包括：
- **`group.getType()`** —— `SparklineType` 枚举（LINE、COLUMN 或 STACKED）。该属性在添加组时设置，但您可以读回它以确认。
- **`group.getLine().getColor()`** —— 线条颜色，以通过 `workbook.createCellsColor()` 创建的 `CellsColor` 表示。这是用于折线迷你图描边颜色的属性。
- **`group.getLine().getWeight()`** —— 以磅为单位的线条粗细。值越大，线条越粗。
- **最高/最低点标记** —— 用于在最高和最低数据点上打开小标记的标志，可用于突出极值。
- **首点/末点/负点标记** —— 用于在第一个、最后一个和负数据点上切换标记的标志。
要更改颜色，请始终创建 `CellsColor` 实例并将其分配给相关属性。不要直接将 `java.awt.Color` 分配给迷你图颜色属性——它们期望来自 `Aspose.Cells.Drawing` 的 `CellsColor` 类型。`add` 方法本身返回完全类型化的 `SparklineGroup` 对象，因此您可以在返回值上链式分配属性，或将其存储在局部变量中，在保存之前进行自定义。
{{% /alert %}}

{{< app/cells/assistant language="python" >}}