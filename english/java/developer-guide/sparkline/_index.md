---
title: Sparklines in Aspose.Cells for Java
linktitle: Sparklines
description: Aspose.Cells is a Java library for working with spreadsheet files that supports creating sparklines — miniature charts placed inside worksheet cells. This article explains how to add and customize line, column, and win/loss sparklines using the Aspose.Cells library.
keywords: Aspose.Cells, Java library, spreadsheet, sparklines, line sparkline, column sparkline, win/loss sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /java/creating-sparklines/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supports creating sparklines inside worksheet cells. Sparklines are miniature charts that fit within a single cell, providing a quick visual representation of data trends. Aspose.Cells supports line, column, and win/loss sparklines, and each can be customized with respect to color, line weight, high/low points, and markers.

{{% /alert %}}

## **Introduction**

Sparklines are tiny in-cell charts that are useful when you want to display a quick trend next to a row or column of data without taking up the space of a full chart. Excel supports three kinds of sparklines: **line**, **column**, and **win/loss**. Aspose.Cells mirrors this capability through the `SparklineGroup` and `SparklineGroupCollection` APIs found in the `Aspose.Cells.Charts` namespace.

In Aspose.Cells, every sparkline you add is created through `worksheet.getSparklineGroups().add(...)`, which returns a `SparklineGroup` object. You can then use that object to set the sparkline type, the data range, the destination cell, and visual properties such as line color, line weight, markers, and high/low point indicators.

{{% alert color="primary" %}}

A single `SparklineGroup` can contain one or more sparklines that share the same style. When you call `add` and pass a row of data plus a single destination cell, you get one sparkline inside that cell. If your destination range is wider than one cell, a separate sparkline is drawn in each destination cell, all using the same style and data range.

{{% /alert %}}

This article walks through each of the three sparkline types supported by Aspose.Cells — **Line**, **Column**, and **Win/Loss** — and shows how to add them, customize their colors, and save the resulting workbook.

## **Line Sparklines**

A line sparkline draws a continuous line through the data points in a series, making it the most natural choice for showing trends over time. In Aspose.Cells, a line sparkline is created by passing `SparklineType.LINE` to the `add` method.

The workflow is the same as for any other sparkline type:

1. Create a new `Workbook` and access the first worksheet.
2. Populate a row of source data (for example, row 1, columns A through E) with the values you want to visualize.
3. Build a `CellArea` describing the destination cell where the sparkline will be drawn.
4. Call `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. The third argument — `false` — tells Aspose.Cells that the data range is horizontal (a row), not vertical (a column).
5. Optionally customize the returned `SparklineGroup`. For a line sparkline you can set the line color using `group.getLine().setColor(...)` (which expects a `CellsColor` from `Aspose.Cells.Drawing`), adjust the line weight, and toggle high/low point markers.
6. Save the workbook.

The following example creates a workbook, writes the values 5, -3, 8, -2, 6 into cells A1 through E1, and adds a line sparkline in cell F1 that traces those values. It also customizes the line color to red and enables markers for the high and low points.

```java
public class CodeRunner {
    public static void main(String[] args) {
        try {
            // Step 1: Create a Workbook and get the first worksheet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.getWorksheets().get(0);
            Cells cells = worksheet.getCells();

            // Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
            cells.get("A1").putValue(5);
            cells.get("B1").putValue(-3);
            cells.get("C1").putValue(8);
            cells.get("D1").putValue(-2);
            cells.get("E1").putValue(6);

            // Step 3: Build a CellArea pointing to destination cell F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // column F (0-indexed)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // row 1 (0-indexed)
            dest.EndRow = 0;

            // Step 4: Add a Line sparkline from A1:E1 into F1
            // SparklineGroups.add returns the index of the newly added group
            int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
            SparklineGroup group = worksheet.getSparklineGroups().get(index);

            // Step 5: Create a red CellsColor and assign it to the sparkline line color
            CellsColor red = workbook.createCellsColor();
            red.setColor(com.aspose.cells.Color.getRed());
            group.setSeriesColor(red);

            // Step 6: Enable high-point and low-point markers
            group.setShowHighPoint(true);
            group.setShowLowPoint(true);

            // Step 7: Save the workbook
            workbook.save("output_line.xlsx");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

## **Column Sparklines**

A column sparkline renders each data point as a vertical bar. This makes it well suited to data whose magnitude is meaningful — for example, monthly sales figures or counts. In Aspose.Cells, you create a column sparkline by passing `SparklineType.COLUMN` to the `add` method.

The procedure mirrors the line sparkline example:

1. Create a new `Workbook` and access the first worksheet.
2. Populate the same source range (A1:E1) with the values you want to visualize.
3. Build a `CellArea` describing the destination cell.
4. Call `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
5. Optionally customize the resulting `SparklineGroup` — for example, by setting `group.getType()` to confirm the type, or by tweaking the bar color.
6. Save the workbook to a separate output file so it does not overwrite the line sparkline example.

The example below writes the values 5, -3, 8, -2, 6 into A1:E1 and renders a column sparkline in F1. Negative values are drawn as bars going downward and positive values as bars going upward, which makes positive and negative contributions easy to spot at a glance.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Write sample values into A1:E1
int[] values = new int[] { 5, -3, 8, -2, 6 };
for (int i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// Build a CellArea pointing to F1 (column index 5, row index 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// Add a Column sparkline to the destination cell
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);

// Confirm the sparkline type by reading group.Type
System.out.println("Sparkline Type added: " + group.getType());

// Save the workbook
workbook.save("output_column.xlsx");

System.out.println("Workbook saved as output_column.xlsx");
```

## **Win/Loss Sparklines**

A win/loss sparkline is a special variant of the column sparkline designed to show only two outcomes: a positive value is drawn as an "up" bar (a win) and a zero or negative value is drawn as a "down" bar (a loss). Win/loss sparklines are commonly used to visualize sequences of wins and losses, pass/fail results, or any binary outcome over time.

In Aspose.Cells, a win/loss sparkline is created by passing `SparklineType.STACKED` to the `add` method. (Despite the name, `SparklineType.STACKED` is the enum value used to request the win/loss rendering.)

The procedure is the same as the other two types:

1. Create a new `Workbook` and access the first worksheet.
2. Populate the source range. Because win/loss sparklines treat every value as either a win or a loss, the magnitude of the value does not matter — only its sign does. Positive values become up bars and non-positive values become down bars.
3. Build a `CellArea` describing the destination cell.
4. Call `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. Optionally customize the returned `SparklineGroup`, for example by setting accent colors for the win and loss bars.
6. Save the workbook under a distinct filename so all three examples can coexist on disk.

The example below uses the same input data as the previous two sections. The values 5, -3, 8, -2, 6 are interpreted as win, loss, win, loss, win — and the sparkline drawn in F1 reflects exactly that pattern.

```java
import com.aspose.cells.*;
import com.aspose.cells.charts.*;
import com.aspose.cells.drawing.*;
import java.awt.Color;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");

// Populate sample data
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Build a CellArea pointing to F1 (column 5, row 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// Add a Win/Loss sparkline (SparklineType.Stacked)
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);

// Customize the sparkline group
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// Set the high-point color to green
CellsColor highColor = workbook.createCellsColor();
highColor.setColor(Color.GREEN);
group.setHighPointColor(highColor);

// Set the low-point color to red
CellsColor lowColor = workbook.createCellsColor();
lowColor.setColor(Color.RED);
group.setLowPointColor(lowColor);

// Set the negative-point color to orange
CellsColor negColor = workbook.createCellsColor();
negColor.setColor(Color.ORANGE);
group.setNegativePointsColor(negColor);

// Set the default series color (used for positive bars)
CellsColor seriesColor = workbook.createCellsColor();
seriesColor.setColor(new Color(70, 130, 180)); // SteelBlue approximation
group.setSeriesColor(seriesColor);

// Save the workbook
workbook.save("output_winloss.xlsx");

System.out.println("Workbook saved successfully: output_winloss.xlsx");
```

## **Combining All Three Sparkline Types**

The previous three examples each produce their own workbook so that the output files are easy to inspect in isolation. In a real-world scenario, however, you will often want to compare several data series side by side. The cleanest way to do that is to put more than one sparkline group into the same worksheet, with each group rendering a different style.

You can add multiple `SparklineGroup` objects to the same `SparklineGroupCollection`, and each group can target a different destination cell or a different range. For example, you might place a line sparkline in F1, a column sparkline in F2, and a win/loss sparkline in F3 — all reading from the same source data in row 1 — so that the reader can see three different visual treatments of the same numbers.

The combined example below creates a single workbook, populates row 1 with the values 5, -3, 8, -2, 6, and then adds three sparkline groups in cells F1, F2, and F3 — one of each type — so that the resulting file demonstrates all three sparkline styles at once.

```java
import com.aspose.cells.*;

// Step 1: Create a Workbook and get the first worksheet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Step 2: Populate sample data in row 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Step 3: Add a Line sparkline group at F1
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5); // Fix: Use static factory method
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// Customize the line sparkline color via CellsColor
CellsColor lineColor = workbook.createCellsColor();
lineColor.setColor(com.aspose.cells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);

// Step 4: Add a Column sparkline group at F2
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // Fix: Use static factory method
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// Customize the column sparkline series color
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);

// Step 5: Add a Win/Loss (Stacked) sparkline group at F3
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // Fix: Use static factory method
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Customize the win/loss sparkline series color
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);

// Step 6: Save the workbook
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

When you combine multiple sparkline groups in a single worksheet, each group is independent. They can share the same source range or use different source ranges, and they can be styled independently. This makes it easy to build a small "dashboard" of in-cell visualizations directly inside an existing worksheet.

{{% /alert %}}

## **Customizing Sparkline Appearance**

Once a `SparklineGroup` has been created and added to `worksheet.getSparklineGroups()`, you can read or modify several of its visual properties before saving the workbook. The most commonly customized properties are:

- **`group.getType()`** — the `SparklineType` (LINE, COLUMN, or STACKED). It is set when the group is added, but you can read it back to confirm.
- **`group.getLine().setColor(...)`** — the line color, expressed as a `CellsColor` created via `workbook.createCellsColor()`. This is the property to use for line sparkline stroke color.
- **`group.getLine().setWeight(...)`** — the line weight in points. Higher values produce thicker lines.
- **High/Low point markers** — flags that turn on small markers on the highest and lowest data points, useful for emphasizing extremes.
- **First/Last/Negative point markers** — flags that toggle markers on the first, last, and negative data points.

To change a color, always create a `CellsColor` instance and assign it to the relevant property. Do not assign a `java.awt.Color` directly to sparkline color properties — they expect the `CellsColor` type from `Aspose.Cells.Drawing`. The `add` method itself returns a fully typed `SparklineGroup` object, so you can chain property assignments on the return value or store it in a local variable and customize it before saving.



{{< app/cells/assistant language="java" >}}