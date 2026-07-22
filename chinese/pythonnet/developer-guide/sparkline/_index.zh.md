---
title: Aspose.Cells for Python via .NET 中的迷你图
linktitle: 迷你图
description: Aspose.Cells 是一个用于处理电子表格文件的 Python 库，支持创建迷你图——嵌入工作表单元格内的微型图表。本文介绍如何使用 Aspose.Cells 库添加和自定义折线、柱形和盈亏迷你图。
keywords: Aspose.Cells, Python 库, 电子表格, 迷你图, 折线迷你图, 柱形迷你图, 盈亏迷你图, SparklineGroup, SparklineType
type: docs
weight: 195
url: /zh/python-net/creating-sparklines/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 支持在工作表单元格内创建迷你图。迷你图是适合放置在单个单元格内的微型图表，可快速直观地展现数据趋势。Aspose.Cells 支持折线、柱形和盈亏三种迷你图，并且每种都可以从颜色、线条粗细、高低点以及标记等方面进行自定义。

{{% /alert %}}

## **简介**

迷你图是单元格内的小型图表，当您希望在数据行或列旁边快速显示趋势而又不占用完整图表的空间时，它非常有用。Excel 支持三种迷你图：**折线**、**柱形**和**盈亏**。Aspose.Cells 通过 `aspose.cells.charts` 命名空间中的 `SparklineGroup` 和 `SparklineGroupCollection` API 提供了对应功能。

在 Aspose.Cells 中，您添加的每个迷你图都是通过 `worksheet.sparkline_groups.add(...)` 创建的，该方法会返回一个 `SparklineGroup` 对象。然后您可以使用该对象设置迷你图类型、数据区域、目标单元格以及视觉属性，例如线条颜色、线条粗细、标记和最高/最低点指示符。

{{% alert color="primary" %}}

单个 `SparklineGroup` 可以包含一个或多个共享相同样式的迷你图。当您调用 `add` 并传入一行数据以及一个目标单元格时，您将在该单元格内获得一个迷你图。如果目标区域宽度超过一个单元格，则会在每个目标单元格中分别绘制一个迷你图，所有这些迷你图都使用相同的样式和数据区域。

{{% /alert %}}

本文将逐一介绍 Aspose.Cells 支持的三种迷你图类型——**折线**、**柱形**和**盈亏**——并展示如何添加它们、自定义颜色以及保存生成的工作簿。

## **折线迷你图**

折线迷你图通过数据序列中的各个数据点绘制一条连续的线条，是随时间展示趋势时最自然的选择。在 Aspose.Cells 中，通过将 `SparklineType.Line` 传递给 `sparkline_groups.add` 方法即可创建折线迷你图。

其操作流程与其他迷你图类型相同：

1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 在源数据的一行（例如第 1 行，A 到 E 列）中填充您要可视化的值。
3. 构造一个 `CellArea` 来描述绘制迷你图的目标单元格。
4. 调用 `worksheet.sparkline_groups.add(SparklineType.Line, "A1:E1", False, dest)`。第三个参数 `False` 用于告知 Aspose.Cells 数据区域是水平方向（一行），而非垂直方向（一列）。
5. 可选地对返回的 `SparklineGroup` 进行自定义。对于折线迷你图，您可以使用 `group.line.color`（该属性需要 `aspose.cells.drawing` 中的 `CellsColor`）设置线条颜色，调整线条粗细，并切换最高/最低点标记的显示。
6. 保存工作簿。

下面的示例创建一个工作簿，将值 5、-3、8、-2、6 写入单元格 A1 到 E1，并在单元格 F1 中添加一个追踪这些值的折线迷你图。同时将线条颜色自定义为红色，并启用最高点和最低点的标记。

```python
import aspose.cells as ac
import System.Drawing

# 步骤 1：创建一个 Workbook 并获取第一个工作表
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells

# 步骤 2：将示例值 5、-3、8、-2、6 写入单元格 A1:E1
cells["A1"].put_value(5)
cells["B1"].put_value(-3)
cells["C1"].put_value(8)
cells["D1"].put_value(-2)
cells["E1"].put_value(6)

# 步骤 3：构建一个指向目标单元格 F1 的 CellArea
dest = ac.CellArea()
dest.start_column = 5   # F 列（0 索引）
dest.end_column = 5
dest.start_row = 0      # 第 1 行（0 索引）
dest.end_row = 0

# 步骤 4：从 A1:E1 向 F1 添加一个 Line 迷你图
# SparklineGroups.Add 返回新添加分组的索引
index = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, dest)
group = worksheet.sparkline_groups[index]

# 步骤 5：创建一个红色的 CellsColor 并将其分配给迷你图线条颜色
red = workbook.create_cells_color()
red.color = System.Drawing.Color.Red
group.series_color = red

# 步骤 6：启用高点标记和低点标记
group.show_high_point = True
group.show_low_point = True

# 步骤 7：保存工作簿
workbook.save("output_line.xlsx")
```

## **柱形迷你图**

柱形迷你图将每个数据点呈现为一个垂直条形。这种方式非常适合数值大小本身具有意义的数据，例如月度销售数据或计数。在 Aspose.Cells 中，通过将 `SparklineType.Column` 传递给 `sparkline_groups.add` 方法即可创建柱形迷你图。

其操作步骤与折线迷你图的示例类似：

1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 在相同的源区域（A1:E1）中填充您要可视化的值。
3. 构造一个 `CellArea` 来描述目标单元格。
4. 调用 `worksheet.sparkline_groups.add(SparklineType.Column, "A1:E1", False, dest)`。
5. 可选地对生成的 `SparklineGroup` 进行自定义——例如，通过设置 `group.type` 来确认类型，或者调整条形颜色。
6. 将工作簿保存到单独的输出文件，以免覆盖折线迷你图示例。

下面的示例将值 5、-3、8、-2、6 写入 A1:E1，并在 F1 中绘制一个柱形迷你图。负值会绘制为向下的条形，正值会绘制为向上的条形，这样可以一眼看出正负贡献。

```python
import aspose.cells as ac

# 步骤 1：创建工作簿并获取第一个工作表
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# 步骤 2：将样本值写入 A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.cells[0, i].put_value(values[i])

# 步骤 3：构建指向 F1 的 CellArea（列索引 5，行索引 0）
dest = ac.CellArea()
dest.start_column = 5
dest.end_column = 5
dest.start_row = 0
dest.end_row = 0

# 步骤 4：向目标单元格添加柱形迷你图
idx = worksheet.sparkline_groups.add(
    ac.SparklineType.COLUMN, "A1:E1", False, dest)
group = worksheet.sparkline_groups[idx]

# 步骤 5：通过读取 group.Type 确认迷你图类型
print("Sparkline Type added: " + str(group.type))

# 步骤 6：保存工作簿
workbook.save("output_column.xlsx")

print("Workbook saved as output_column.xlsx")
```

## **盈亏迷你图**

盈亏迷你图是柱形迷你图的一种特殊变体，仅用于展示两种结果：正值绘制为“向上”的条形（即“盈”），零或负值绘制为“向下”的条形（即“亏”）。盈亏迷你图常用于可视化一连串的胜负、通过/未通过结果，或任何随时间变化的二元结果。

在 Aspose.Cells 中，通过将 `SparklineType.Stacked` 传递给 `sparkline_groups.add` 方法即可创建盈亏迷你图。（尽管名称如此，`SparklineType.Stacked` 实际上是用于请求盈亏渲染的枚举值。）

其操作流程与其他两种类型相同：

1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 填充源区域。由于盈亏迷你图将每个值都视为“盈”或“亏”，因此数值的大小无关紧要，只有其符号才有意义。正值变为向上的条形，非正值变为向下的条形。
3. 构造一个 `CellArea` 来描述目标单元格。
4. 调用 `worksheet.sparkline_groups.add(SparklineType.Stacked, "A1:E1", False, dest)`。
5. 可选地对返回的 `SparklineGroup` 进行自定义，例如为盈亏条形设置强调色。
6. 使用不同的文件名保存工作簿，以便三个示例可以共存于磁盘上。

下面的示例使用与前两节相同的输入数据。值 5、-3、8、-2、6 被分别解释为盈、亏、盈、亏、盈——在 F1 中绘制的迷你图正好反映了这种模式。

```python
import aspose.cells as ac
import System.Drawing

# 步骤 1: 创建一个工作簿并获取第一个工作表
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "WinLoss"

# 步骤 2: 在第 1 行填充示例数据：A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# 步骤 3: 构建一个指向 F1 的 CellArea（第 5 列，第 0 行）
dest = ac.CellArea()
dest.start_column = 5   # F
dest.end_column = 5
dest.start_row = 0      # 第 1 行
dest.end_row = 0

# 步骤 4: 添加一个 Win/Loss 迷你图（SparklineType.Stacked）
group_index = worksheet.sparkline_groups.add(
    ac.SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.sparkline_groups[group_index]

# 步骤 5: 自定义迷你图组
# 启用高点和低点标记
group.show_high_point = True
group.show_low_point = True
group.show_negative_points = True

# 将高点颜色设置为绿色
high_color = workbook.create_cells_color()
high_color.color = System.Drawing.Color.Green
group.high_point_color = high_color

# 将低点颜色设置为红色
low_color = workbook.create_cells_color()
low_color.color = System.Drawing.Color.Red
group.low_point_color = low_color

# 将负点颜色设置为橙色
neg_color = workbook.create_cells_color()
neg_color.color = System.Drawing.Color.Orange
group.negative_points_color = neg_color

# 设置默认系列颜色（用于正数柱）
series_color = workbook.create_cells_color()
series_color.color = System.Drawing.Color.SteelBlue
group.series_color = series_color

# 步骤 6: 保存工作簿
workbook.save("output_winloss.xlsx")

print("Workbook saved successfully: output_winloss.xlsx")
```

## **组合使用三种迷你图类型**

前面三个示例分别生成各自的工作簿，以便于独立查看输出文件。然而在实际场景中，您通常希望并排比较多个数据序列。最清晰的做法是在同一工作表中放入多个迷你图组，每组呈现不同的样式。

您可以将多个 `SparklineGroup` 对象添加到同一个 `SparklineGroupCollection` 中，每组可以指向不同的目标单元格或不同的区域。例如，您可以在 F1 放置折线迷你图，在 F2 放置柱形迷你图，在 F3 放置盈亏迷你图——所有这些都从第 1 行中的同一组源数据读取——这样读者可以同时看到同一组数字的三种不同可视化效果。

下面的组合示例创建一个工作簿，在第 1 行填充值 5、-3、8、-2、6，然后在 F1、F2 和 F3 单元格中添加三个迷你图组（每种类型各一个），最终生成的文件一次性展示所有三种迷你图样式。

```python
import aspose.cells as ac
import System.Drawing

# 步骤 1：创建一个 Workbook 并获取第一个工作表
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# 步骤 2：在第 1 行 (A1:E1) 填充示例数据
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# 步骤 3：在 F1 单元格添加折线迷你图组
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)
line_group = worksheet.sparkline_groups[line_idx]

# 通过 CellsColor 自定义折线迷你图的颜色
line_color = workbook.create_cells_color()
line_color.color = System.Drawing.Color.Blue
line_group.series_color = line_color

# 步骤 4：在 F2 单元格添加柱形迷你图组
column_area = ac.CellArea()
column_area.start_column = 5
column_area.end_column = 5
column_area.start_row = 1
column_area.end_row = 1
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)
column_group = worksheet.sparkline_groups[column_idx]

# 自定义柱形迷你图系列的颜色
column_color = workbook.create_cells_color()
column_color.color = System.Drawing.Color.Green
column_group.series_color = column_color

# 步骤 5：在 F3 单元格添加盈亏（堆叠）迷你图组
stacked_area = ac.CellArea()
stacked_area.start_column = 5
stacked_area.end_column = 5
stacked_area.start_row = 2
stacked_area.end_row = 2
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)
stacked_group = worksheet.sparkline_groups[stacked_idx]

# 自定义盈亏迷你图系列的颜色
stacked_color = workbook.create_cells_color()
stacked_color.color = System.Drawing.Color.DarkOrange
stacked_group.series_color = stacked_color

# 步骤 6：保存工作簿
workbook.save("output_all.xlsx")
```

{{% alert color="primary" %}}

当您在单个工作表中组合多个迷你图组时，每个组都是独立的。它们可以共享同一源区域，也可以使用不同的源区域，并且可以独立设置样式。这使得您可以直接在现有工作表中轻松构建一个由单元格内可视化效果组成的小型“仪表板”。

{{% /alert %}}

## **自定义迷你图外观**

在创建 `SparklineGroup` 并将其添加到 `worksheet.sparkline_groups` 之后，您可以在保存工作簿之前读取或修改其多个视觉属性。最常自定义的属性包括：

- **`group.type`**——`SparklineType`（Line、Column 或 Stacked）。该属性在添加组时设置，但您可以读回它以确认类型。
- **`group.line.color`**——线条颜色，通过 `workbook.create_cells_color()` 创建的 `CellsColor` 表示。对于折线迷你图，应使用此属性设置描边颜色。
- **`group.line.weight`**——以磅为单位的线条粗细。值越大，线条越粗。
- **最高/最低点标记**——用于在最高和最低数据点处显示小型标记的标志，便于突出极值。
- **首/尾/负值点标记**——用于在第一个、最后一个和负值数据点处切换标记显示的标志。

若要更改颜色，请始终创建一个 `CellsColor` 实例并将其分配给相关属性。迷你图的颜色属性需要 `aspose.cells.drawing` 中的 `CellsColor` 类型——请勿直接将原始颜色值分配给这些属性。`sparkline_groups.add` 方法本身会返回一个完整类型的 `SparklineGroup` 对象，因此您可以在返回值上链式调用属性赋值，或者将其保存在局部变量中，在保存前进行自定义。

{{< app/cells/assistant language="python" >}}