---
title: Sparklines in Aspose.Cells for Python via .NET
linktitle: Sparklines
description: Aspose.Cells is a Python library for working with spreadsheet files that supports creating sparklines — miniature charts placed inside worksheet cells. This article explains how to add and customize line, column, and win/loss sparklines using the Aspose.Cells library.
keywords: Aspose.Cells, Python library, spreadsheet, sparklines, line sparkline, column sparkline, win/loss sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /python-net/creating-sparklines/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supports creating sparklines inside worksheet cells. Sparklines are miniature charts that fit within a single cell, providing a quick visual representation of data trends. Aspose.Cells supports line, column, and win/loss sparklines, and each can be customized with respect to color, line weight, high/low points, and markers.

{{% /alert %}}

## **Introduction**

Sparklines are tiny in-cell charts that are useful when you want to display a quick trend next to a row or column of data without taking up the space of a full chart. Excel supports three kinds of sparklines: **line**, **column**, and **win/loss**. Aspose.Cells mirrors this capability through the `SparklineGroup` and `SparklineGroupCollection` APIs found in the `aspose.cells.charts` namespace.

In Aspose.Cells, every sparkline you add is created through `worksheet.sparkline_groups.add(...)`, which returns a `SparklineGroup` object. You can then use that object to set the sparkline type, the data range, the destination cell, and visual properties such as line color, line weight, markers, and high/low point indicators.

{{% alert color="primary" %}}

A single `SparklineGroup` can contain one or more sparklines that share the same style. When you call `add` and pass a row of data plus a single destination cell, you get one sparkline inside that cell. If your destination range is wider than one cell, a separate sparkline is drawn in each destination cell, all using the same style and data range.

{{% /alert %}}

This article walks through each of the three sparkline types supported by Aspose.Cells — **Line**, **Column**, and **Win/Loss** — and shows how to add them, customize their colors, and save the resulting workbook.

## **Line Sparklines**

A line sparkline draws a continuous line through the data points in a series, making it the most natural choice for showing trends over time. In Aspose.Cells, a line sparkline is created by passing `SparklineType.Line` to the `sparkline_groups.add` method.

The workflow is the same as for any other sparkline type:

1. Create a new `Workbook` and access the first worksheet.
2. Populate a row of source data (for example, row 1, columns A through E) with the values you want to visualize.
3. Build a `CellArea` describing the destination cell where the sparkline will be drawn.
4. Call `worksheet.sparkline_groups.add(SparklineType.Line, "A1:E1", False, dest)`. The third argument — `False` — tells Aspose.Cells that the data range is horizontal (a row), not vertical (a column).
5. Optionally customize the returned `SparklineGroup`. For a line sparkline you can set the line color using `group.line.color` (which expects a `CellsColor` from `aspose.cells.drawing`), adjust the line weight, and toggle high/low point markers.
6. Save the workbook.

The following example creates a workbook, writes the values 5, -3, 8, -2, 6 into cells A1 through E1, and adds a line sparkline in cell F1 that traces those values. It also customizes the line color to red and enables markers for the high and low points.

```python
import aspose.cells as ac
import System.Drawing

# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells

# Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells["A1"].put_value(5)
cells["B1"].put_value(-3)
cells["C1"].put_value(8)
cells["D1"].put_value(-2)
cells["E1"].put_value(6)

# Step 3: Build a CellArea pointing to destination cell F1
dest = ac.CellArea()
dest.start_column = 5   # column F (0-indexed)
dest.end_column = 5
dest.start_row = 0      # row 1 (0-indexed)
dest.end_row = 0

# Step 4: Add a Line sparkline from A1:E1 into F1
# SparklineGroups.Add returns the index of the newly added group
index = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, dest)
group = worksheet.sparkline_groups[index]

# Step 5: Create a red CellsColor and assign it to the sparkline line color
red = workbook.create_cells_color()
red.color = System.Drawing.Color.Red
group.series_color = red

# Step 6: Enable high-point and low-point markers
group.show_high_point = True
group.show_low_point = True

# Step 7: Save the workbook
workbook.save("output_line.xlsx")
```

## **Column Sparklines**

A column sparkline renders each data point as a vertical bar. This makes it well suited to data whose magnitude is meaningful — for example, monthly sales figures or counts. In Aspose.Cells, you create a column sparkline by passing `SparklineType.Column` to the `sparkline_groups.add` method.

The procedure mirrors the line sparkline example:

1. Create a new `Workbook` and access the first worksheet.
2. Populate the same source range (A1:E1) with the values you want to visualize.
3. Build a `CellArea` describing the destination cell.
4. Call `worksheet.sparkline_groups.add(SparklineType.Column, "A1:E1", False, dest)`.
5. Optionally customize the resulting `SparklineGroup` — for example, by setting `group.type` to confirm the type, or by tweaking the bar color.
6. Save the workbook to a separate output file so it does not overwrite the line sparkline example.

The example below writes the values 5, -3, 8, -2, 6 into A1:E1 and renders a column sparkline in F1. Negative values are drawn as bars going downward and positive values as bars going upward, which makes positive and negative contributions easy to spot at a glance.

```python
import aspose.cells as ac

# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Step 2: Write sample values into A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.cells[0, i].put_value(values[i])

# Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
dest = ac.CellArea()
dest.start_column = 5
dest.end_column = 5
dest.start_row = 0
dest.end_row = 0

# Step 4: Add a Column sparkline to the destination cell
idx = worksheet.sparkline_groups.add(
    ac.SparklineType.COLUMN, "A1:E1", False, dest)
group = worksheet.sparkline_groups[idx]

# Step 5: Confirm the sparkline type by reading group.Type
print("Sparkline Type added: " + str(group.type))

# Step 6: Save the workbook
workbook.save("output_column.xlsx")

print("Workbook saved as output_column.xlsx")
```

## **Win/Loss Sparklines**

A win/loss sparkline is a special variant of the column sparkline designed to show only two outcomes: a positive value is drawn as an "up" bar (a win) and a zero or negative value is drawn as a "down" bar (a loss). Win/loss sparklines are commonly used to visualize sequences of wins and losses, pass/fail results, or any binary outcome over time.

In Aspose.Cells, a win/loss sparkline is created by passing `SparklineType.Stacked` to the `sparkline_groups.add` method. (Despite the name, `SparklineType.Stacked` is the enum value used to request the win/loss rendering.)

The procedure is the same as the other two types:

1. Create a new `Workbook` and access the first worksheet.
2. Populate the source range. Because win/loss sparklines treat every value as either a win or a loss, the magnitude of the value does not matter — only its sign does. Positive values become up bars and non-positive values become down bars.
3. Build a `CellArea` describing the destination cell.
4. Call `worksheet.sparkline_groups.add(SparklineType.Stacked, "A1:E1", False, dest)`.
5. Optionally customize the returned `SparklineGroup`, for example by setting accent colors for the win and loss bars.
6. Save the workbook under a distinct filename so all three examples can coexist on disk.

The example below uses the same input data as the previous two sections. The values 5, -3, 8, -2, 6 are interpreted as win, loss, win, loss, win — and the sparkline drawn in F1 reflects exactly that pattern.

```python
import aspose.cells as ac
import System.Drawing

# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "WinLoss"

# Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Step 3: Build a CellArea pointing to F1 (column 5, row 0)
dest = ac.CellArea()
dest.start_column = 5   # F
dest.end_column = 5
dest.start_row = 0      # row 1
dest.end_row = 0

# Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
group_index = worksheet.sparkline_groups.add(
    ac.SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.sparkline_groups[group_index]

# Step 5: Customize the sparkline group
# Enable high-point and low-point markers
group.show_high_point = True
group.show_low_point = True
group.show_negative_points = True

# Set the high-point color to green
high_color = workbook.create_cells_color()
high_color.color = System.Drawing.Color.Green
group.high_point_color = high_color

# Set the low-point color to red
low_color = workbook.create_cells_color()
low_color.color = System.Drawing.Color.Red
group.low_point_color = low_color

# Set the negative-point color to orange
neg_color = workbook.create_cells_color()
neg_color.color = System.Drawing.Color.Orange
group.negative_points_color = neg_color

# Set the default series color (used for positive bars)
series_color = workbook.create_cells_color()
series_color.color = System.Drawing.Color.SteelBlue
group.series_color = series_color

# Step 6: Save the workbook
workbook.save("output_winloss.xlsx")

print("Workbook saved successfully: output_winloss.xlsx")
```

## **Combining All Three Sparkline Types**

The previous three examples each produce their own workbook so that the output files are easy to inspect in isolation. In a real-world scenario, however, you will often want to compare several data series side by side. The cleanest way to do that is to put more than one sparkline group into the same worksheet, with each group rendering a different style.

You can add multiple `SparklineGroup` objects to the same `SparklineGroupCollection`, and each group can target a different destination cell or a different range. For example, you might place a line sparkline in F1, a column sparkline in F2, and a win/loss sparkline in F3 — all reading from the same source data in row 1 — so that the reader can see three different visual treatments of the same numbers.

The combined example below creates a single workbook, populates row 1 with the values 5, -3, 8, -2, 6, and then adds three sparkline groups in cells F1, F2, and F3 — one of each type — so that the resulting file demonstrates all three sparkline styles at once.

```python
import aspose.cells as ac
import System.Drawing

# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Step 2: Populate sample data in row 1 (A1:E1)
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Step 3: Add a Line sparkline group at F1
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)
line_group = worksheet.sparkline_groups[line_idx]

# Customize the line sparkline color via CellsColor
line_color = workbook.create_cells_color()
line_color.color = System.Drawing.Color.Blue
line_group.series_color = line_color

# Step 4: Add a Column sparkline group at F2
column_area = ac.CellArea()
column_area.start_column = 5
column_area.end_column = 5
column_area.start_row = 1
column_area.end_row = 1
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)
column_group = worksheet.sparkline_groups[column_idx]

# Customize the column sparkline series color
column_color = workbook.create_cells_color()
column_color.color = System.Drawing.Color.Green
column_group.series_color = column_color

# Step 5: Add a Win/Loss (Stacked) sparkline group at F3
stacked_area = ac.CellArea()
stacked_area.start_column = 5
stacked_area.end_column = 5
stacked_area.start_row = 2
stacked_area.end_row = 2
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)
stacked_group = worksheet.sparkline_groups[stacked_idx]

# Customize the win/loss sparkline series color
stacked_color = workbook.create_cells_color()
stacked_color.color = System.Drawing.Color.DarkOrange
stacked_group.series_color = stacked_color

# Step 6: Save the workbook
workbook.save("output_all.xlsx")
```

{{% alert color="primary" %}}

When you combine multiple sparkline groups in a single worksheet, each group is independent. They can share the same source range or use different source ranges, and they can be styled independently. This makes it easy to build a small "dashboard" of in-cell visualizations directly inside an existing worksheet.

{{% /alert %}}

## **Customizing Sparkline Appearance**

Once a `SparklineGroup` has been created and added to `worksheet.sparkline_groups`, you can read or modify several of its visual properties before saving the workbook. The most commonly customized properties are:

- **`group.type`** — the `SparklineType` (Line, Column, or Stacked). It is set when the group is added, but you can read it back to confirm.
- **`group.line.color`** — the line color, expressed as a `CellsColor` created via `workbook.create_cells_color()`. This is the property to use for line sparkline stroke color.
- **`group.line.weight`** — the line weight in points. Higher values produce thicker lines.
- **High/Low point markers** — flags that turn on small markers on the highest and lowest data points, useful for emphasizing extremes.
- **First/Last/Negative point markers** — flags that toggle markers on the first, last, and negative data points.

To change a color, always create a `CellsColor` instance and assign it to the relevant property. Sparkline color properties expect the `CellsColor` type from `aspose.cells.drawing` — do not assign a raw color value directly to them. The `sparkline_groups.add` method itself returns a fully typed `SparklineGroup` object, so you can chain property assignments on the return value or store it in a local variable and customize it before saving.



{{< app/cells/assistant language="python" >}}