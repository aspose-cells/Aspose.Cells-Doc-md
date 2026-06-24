---
title: Sparklines in Aspose.Cells for C++
linktitle: Sparklines
description: Aspose.Cells is a C++ library for working with spreadsheet files that supports creating sparklines — miniature charts placed inside worksheet cells. This article explains how to add and customize line, column, and win/loss sparklines using the Aspose.Cells library.
keywords: Aspose.Cells, C++ library, spreadsheet, sparklines, line sparkline, column sparkline, win/loss sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /cpp/creating-sparklines/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
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

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Step 1: Create a Workbook and get the first worksheet
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
    cells.Get(u"A1").PutValue(5);
    cells.Get(u"B1").PutValue(-3);
    cells.Get(u"C1").PutValue(8);
    cells.Get(u"D1").PutValue(-2);
    cells.Get(u"E1").PutValue(6);

    // Step 3: Build a CellArea pointing to destination cell F1
    CellArea dest;
    dest.StartColumn = 5;   // column F (0-indexed)
    dest.EndColumn = 5;
    dest.StartRow = 0;      // row 1 (0-indexed)
    dest.EndRow = 0;

    // Step 4: Add a Line sparkline from A1:E1 into F1
    int index = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(index);

    // Step 5: Create a red CellsColor and assign it to the sparkline line color
    CellsColor red = workbook.CreateCellsColor();
    red.SetColor(Color::Red());
    group.SetSeriesColor(red);

    // Step 6: Enable high-point and low-point markers
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);

    // Step 7: Save the workbook
    workbook.Save(u"output_line.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

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

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Step 1: Create a Workbook and get the first worksheet
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Step 2: Write sample values into A1:E1
    int values[5] = { 5, -3, 8, -2, 6 };
    Cells cells = worksheet.GetCells();
    for (int i = 0; i < 5; i++) {
        cells.Get(0, i).PutValue(values[i]);
    }

    // Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
    CellArea dest;
    dest.StartColumn = 5;
    dest.EndColumn = 5;
    dest.StartRow = 0;
    dest.EndRow = 0;

    // Step 4: Add a Column sparkline to the destination cell
    int idx = worksheet.GetSparklineGroups().Add(
        SparklineType::Column, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(idx);

    // Step 5: Confirm the sparkline type by reading group.Type
    std::cout << "Sparkline Type added: " << static_cast<int>(group.GetType()) << std::endl;

    // Step 6: Save the workbook
    wb.Save(u"output_column.xlsx");

    std::cout << "Workbook saved as output_column.xlsx" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

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

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Step 1: Create a Workbook and get the first worksheet
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"WinLoss");

    // Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    // Step 3: Build a CellArea pointing to F1 (column 5, row 0)
    CellArea dest;
    dest.StartColumn = 5;   // F
    dest.EndColumn = 5;
    dest.StartRow = 0;      // row 1
    dest.EndRow = 0;

    // Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
    int groupIndex = worksheet.GetSparklineGroups().Add(
        SparklineType::Stacked,
        u"A1:E1",
        false,
        dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(groupIndex);

    // Step 5: Customize the sparkline group
    // Enable high-point and low-point markers
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.SetShowNegativePoints(true);

    // Set the high-point color to green
    CellsColor highColor = workbook.CreateCellsColor();
    highColor.SetColor(Color::Green());
    group.SetHighPointColor(highColor);

    // Set the low-point color to red
    CellsColor lowColor = workbook.CreateCellsColor();
    lowColor.SetColor(Color::Red());
    group.SetLowPointColor(lowColor);

    // Set the negative-point color to orange
    CellsColor negColor = workbook.CreateCellsColor();
    negColor.SetColor(Color::Orange());
    group.SetNegativePointsColor(negColor);

    // Set the default series color (used for positive bars)
    CellsColor seriesColor = workbook.CreateCellsColor();
    seriesColor.SetColor(Color::SteelBlue());
    group.SetSeriesColor(seriesColor);

    // Step 6: Save the workbook
    workbook.Save(u"output_winloss.xlsx");

    std::cout << "Workbook saved successfully: output_winloss.xlsx" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Combining All Three Sparkline Types**

The previous three examples each produce their own workbook so that the output files are easy to inspect in isolation. In a real-world scenario, however, you will often want to compare several data series side by side. The cleanest way to do that is to put more than one sparkline group into the same worksheet, with each group rendering a different style.

You can add multiple `SparklineGroup` objects to the same `SparklineGroupCollection`, and each group can target a different destination cell or a different range. For example, you might place a line sparkline in F1, a column sparkline in F2, and a win/loss sparkline in F3 — all reading from the same source data in row 1 — so that the reader can see three different visual treatments of the same numbers.

The combined example below creates a single workbook, populates row 1 with the values 5, -3, 8, -2, 6, and then adds three sparkline groups in cells F1, F2, and F3 — one of each type — so that the resulting file demonstrates all three sparkline styles at once.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Step 1: Create a Workbook and get the first worksheet
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Step 2: Populate sample data in row 1 (A1:E1)
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    // Step 3: Add a Line sparkline group at F1
    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, lineArea);
    SparklineGroup lineGroup = worksheet.GetSparklineGroups().Get(lineIdx);

    // Customize the line sparkline color via CellsColor
    CellsColor lineColor = workbook.CreateCellsColor();
    lineColor.SetColor(Color::Blue());
    lineGroup.SetSeriesColor(lineColor);

    // Step 4: Add a Column sparkline group at F2
    CellArea columnArea;
    columnArea.StartColumn = 5;
    columnArea.EndColumn = 5;
    columnArea.StartRow = 1;
    columnArea.EndRow = 1;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, u"A1:E1", false, columnArea);
    SparklineGroup columnGroup = worksheet.GetSparklineGroups().Get(columnIdx);

    // Customize the column sparkline series color
    CellsColor columnColor = workbook.CreateCellsColor();
    columnColor.SetColor(Color::Green());
    columnGroup.SetSeriesColor(columnColor);

    // Step 5: Add a Win/Loss (Stacked) sparkline group at F3
    CellArea stackedArea;
    stackedArea.StartColumn = 5;
    stackedArea.EndColumn = 5;
    stackedArea.StartRow = 2;
    stackedArea.EndRow = 2;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, u"A1:E1", false, stackedArea);
    SparklineGroup stackedGroup = worksheet.GetSparklineGroups().Get(stackedIdx);

    // Customize the win/loss sparkline series color
    CellsColor stackedColor = workbook.CreateCellsColor();
    stackedColor.SetColor(Color::FromArgb(0xFF8C00));
    stackedGroup.SetSeriesColor(stackedColor);

    // Step 6: Save the workbook
    workbook.Save(u"output_all.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

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