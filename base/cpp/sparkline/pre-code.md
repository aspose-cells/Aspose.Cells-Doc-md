---
title: Sparklines in Aspose.Cells for C++
description: Aspose.Cells is a C++ library for working with spreadsheet files that supports creating sparklines — miniature charts placed inside worksheet cells. This article explains how to add and customize line, column, and win/loss sparklines using the Aspose.Cells library.
keywords: Aspose.Cells, C++ library, spreadsheet, sparklines, line sparkline, column sparkline, win/loss sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /cpp/creating-sparklines/
---

{{% alert color="primary" %}}

Aspose.Cells supports creating sparklines inside worksheet cells. Sparklines are miniature charts that fit within a single cell, providing a quick visual representation of data trends. Aspose.Cells supports line, column, and win/loss sparklines, and each can be customized with respect to color, line weight, high/low points, and markers.

{{% /alert %}}

## **Introduction**

Sparklines are tiny in-cell charts that are useful when you want to display a quick trend next to a row or column of data without taking up the space of a full chart. Excel supports three kinds of sparklines: **line**, **column**, and **win/loss**. Aspose.Cells mirrors this capability through the `SparklineGroup` and `SparklineGroupCollection` APIs found in the `Aspose.Cells.Charts` namespace.

In Aspose.Cells, every sparkline you add is created through `worksheet.SparklineGroups.Add(...)`, which returns a `SparklineGroup` object. You can then use that object to set the sparkline type, the data range, the destination cell, and visual properties such as line color, line weight, markers, and high/low point indicators.

{{% alert color="primary" %}}

A single `SparklineGroup` can contain one or more sparklines that share the same style. When you call `Add` and pass a row of data plus a single destination cell, you get one sparkline inside that cell. If your destination range is wider than one cell, a separate sparkline is drawn in each destination cell, all using the same style and data range.

{{% /alert %}}

This article walks through each of the three sparkline types supported by Aspose.Cells — **Line**, **Column**, and **Win/Loss** — and shows how to add them, customize their colors, and save the resulting workbook.

## **Line Sparklines**

A line sparkline draws a continuous line through the data points in a series, making it the most natural choice for showing trends over time. In Aspose.Cells, a line sparkline is created by passing `SparklineType.Line` to the `SparklineGroups.Add` method.

The workflow is the same as for any other sparkline type:

1. Create a new `Workbook` and access the first worksheet.
2. Populate a row of source data (for example, row 1, columns A through E) with the values you want to visualize.
3. Build a `CellArea` describing the destination cell where the sparkline will be drawn.
4. Call `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. The third argument — `false` — tells Aspose.Cells that the data range is horizontal (a row), not vertical (a column).
5. Optionally customize the returned `SparklineGroup`. For a line sparkline you can set the line color using `group.Line.Color` (which expects a `CellsColor` from `Aspose.Cells.Drawing`), adjust the line weight, and toggle high/low point markers.
6. Save the workbook.

The following example creates a workbook, writes the values 5, -3, 8, -2, 6 into cells A1 through E1, and adds a line sparkline in cell F1 that traces those values. It also customizes the line color to red and enables markers for the high and low points.

<!-- CODE_BLOCK:0:Line Sparklines example in C++ -->

## **Column Sparklines**

A column sparkline renders each data point as a vertical bar. This makes it well suited to data whose magnitude is meaningful — for example, monthly sales figures or counts. In Aspose.Cells, you create a column sparkline by passing `SparklineType.Column` to the `SparklineGroups.Add` method.

The procedure mirrors the line sparkline example:

1. Create a new `Workbook` and access the first worksheet.
2. Populate the same source range (A1:E1) with the values you want to visualize.
3. Build a `CellArea` describing the destination cell.
4. Call `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.
5. Optionally customize the resulting `SparklineGroup` — for example, by setting `group.Type` to confirm the type, or by tweaking the bar color.
6. Save the workbook to a separate output file so it does not overwrite the line sparkline example.

The example below writes the values 5, -3, 8, -2, 6 into A1:E1 and renders a column sparkline in F1. Negative values are drawn as bars going downward and positive values as bars going upward, which makes positive and negative contributions easy to spot at a glance.

<!-- CODE_BLOCK:1:Column Sparklines example in C++ -->

## **Win/Loss Sparklines**

A win/loss sparkline is a special variant of the column sparkline designed to show only two outcomes: a positive value is drawn as an "up" bar (a win) and a zero or negative value is drawn as a "down" bar (a loss). Win/loss sparklines are commonly used to visualize sequences of wins and losses, pass/fail results, or any binary outcome over time.

In Aspose.Cells, a win/loss sparkline is created by passing `SparklineType.Stacked` to the `SparklineGroups.Add` method. (Despite the name, `SparklineType.Stacked` is the enum value used to request the win/loss rendering.)

The procedure is the same as the other two types:

1. Create a new `Workbook` and access the first worksheet.
2. Populate the source range. Because win/loss sparklines treat every value as either a win or a loss, the magnitude of the value does not matter — only its sign does. Positive values become up bars and non-positive values become down bars.
3. Build a `CellArea` describing the destination cell.
4. Call `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Optionally customize the returned `SparklineGroup`, for example by setting accent colors for the win and loss bars.
6. Save the workbook under a distinct filename so all three examples can coexist on disk.

The example below uses the same input data as the previous two sections. The values 5, -3, 8, -2, 6 are interpreted as win, loss, win, loss, win — and the sparkline drawn in F1 reflects exactly that pattern.

<!-- CODE_BLOCK:2:Win/Loss Sparklines example in C++ -->

## **Combining All Three Sparkline Types**

The previous three examples each produce their own workbook so that the output files are easy to inspect in isolation. In a real-world scenario, however, you will often want to compare several data series side by side. The cleanest way to do that is to put more than one sparkline group into the same worksheet, with each group rendering a different style.

You can add multiple `SparklineGroup` objects to the same `SparklineGroupCollection`, and each group can target a different destination cell or a different range. For example, you might place a line sparkline in F1, a column sparkline in F2, and a win/loss sparkline in F3 — all reading from the same source data in row 1 — so that the reader can see three different visual treatments of the same numbers.

The combined example below creates a single workbook, populates row 1 with the values 5, -3, 8, -2, 6, and then adds three sparkline groups in cells F1, F2, and F3 — one of each type — so that the resulting file demonstrates all three sparkline styles at once.

<!-- CODE_BLOCK:3:Combining All Three Sparkline Types example in C++ -->

{{% alert color="primary" %}}

When you combine multiple sparkline groups in a single worksheet, each group is independent. They can share the same source range or use different source ranges, and they can be styled independently. This makes it easy to build a small "dashboard" of in-cell visualizations directly inside an existing worksheet.

{{% /alert %}}

## **Customizing Sparkline Appearance**

Once a `SparklineGroup` has been created and added to `worksheet.SparklineGroups`, you can read or modify several of its visual properties before saving the workbook. The most commonly customized properties are:

- **`group.Type`** — the `SparklineType` (Line, Column, or Stacked). It is set when the group is added, but you can read it back to confirm.
- **`group.Line.Color`** — the line color, expressed as a `CellsColor` created via `workbook.CreateCellsColor()`. This is the property to use for line sparkline stroke color.
- **`group.Line.Weight`** — the line weight in points. Higher values produce thicker lines.
- **High/Low point markers** — flags that turn on small markers on the highest and lowest data points, useful for emphasizing extremes.
- **First/Last/Negative point markers** — flags that toggle markers on the first, last, and negative data points.

To change a color, always create a `CellsColor` instance and assign it to the relevant property. Do not assign a raw color value directly to sparkline color properties — they expect the `CellsColor` type from `Aspose.Cells.Drawing`. The `SparklineGroups.Add` method itself returns a fully typed `SparklineGroup` object, so you can chain property assignments on the return value or store it in a local variable and customize it before saving.



{{< app/cells/assistant language="cpp" >}}