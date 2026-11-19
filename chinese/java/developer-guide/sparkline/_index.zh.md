---
title: Aspose.Cells for Java 中的迷你图
linktitle: 迷你图
description: Aspose.Cells 是一个用于处理电子表格文件的 Java 库，支持在单元格内创建迷你图 —— 一种放置在单元格中的小型图表。本文介绍如何使用 Aspose.Cells 库添加和自定义折线、柱形和涨/跌迷你图。
keywords: Aspose.Cells, Java 库, 电子表格, 迷你图, 折线迷你图, 柱形迷你图, 涨/跌迷你图, SparklineGroup, SparklineType
type: docs
weight: 195
url: /zh/java/creating-sparklines/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持在工作表单元格内创建迷你图。迷你图是适合放置在单个单元格内的小型图表，能够快速直观地呈现数据趋势。Aspose.Cells 支持折线、柱形和涨/跌迷你图，并且每种类型都可以在颜色、线宽、最高/最低点和标记方面进行自定义。
{{% /alert %}}

## **简介**
迷你图是单元格内的小型图表，当您希望在数据行或列旁边快速显示趋势而又不占用完整图表的空间时非常有用。Excel 支持三种迷你图：**折线**、**柱形** 和 **涨/跌**。Aspose.Cells 通过 `Aspose.Cells.Charts` 命名空间中的 `SparklineGroup` 和 `SparklineGroupCollection` API 实现了这一功能。
在 Aspose.Cells 中，您添加的每个迷你图都是通过 `worksheet.getSparklineGroups().add(...)` 创建的，该方法返回一个 `SparklineGroup` 对象。然后您可以使用该对象来设置迷你图类型、数据区域、目标单元格以及视觉属性，例如线条颜色、线宽、标记和最高/最低点指示符。
本文将逐一介绍 Aspose.Cells 支持的三种迷你图类型 —— **折线**、**柱形** 和 **涨/跌** —— 并展示如何添加它们、自定义它们的颜色以及保存生成的工作簿。

## **折线迷你图**
折线迷你图通过数据系列中的各个数据点绘制一条连续的线条，是显示随时间变化趋势的最自然选择。在 Aspose.Cells 中，通过将 `SparklineType.LINE` 传递给 `add` 方法即可创建折线迷你图。
1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 在一行源数据中（例如第 1 行，A 到 E 列）填充您要可视化的值。
3. 构建一个 `CellArea`，用于描述迷你图将要绘制的目标单元格。
4. 调用 `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`。第三个参数 `false` 告诉 Aspose.Cells 数据区域是水平的（行）而不是垂直的（列）。
5. 可选择对返回的 `SparklineGroup` 进行自定义。对于折线迷你图，您可以使用 `group.getLine().setColor(...)`（该方法接受来自 `Aspose.Cells.Drawing` 的 `CellsColor`）设置线条颜色、调整线宽，并切换最高/最低点标记。
6. 保存工作簿。
以下示例创建一个工作簿，将值 5、-3、8、-2、6 写入 A1 到 E1 单元格，并在 F1 单元格中添加一个折线迷你图来跟踪这些值。该示例还将线条颜色自定义为红色，并启用最高和最低点的标记。

```java
import com.aspose.cells.*;
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
```

## **柱形迷你图**
柱形迷你图将每个数据点渲染为一个垂直条形。这使得它非常适合数值大小具有意义的场景 —— 例如每月销售额或计数。在 Aspose.Cells 中，通过将 `SparklineType.COLUMN` 传递给 `add` 方法即可创建柱形迷你图。
该过程与折线迷你图的示例类似：
1. 创建一个新的 `Workbook` 并访问第一个工作表。
3. 构建一个 `CellArea`，用于描述目标单元格。
4. 调用 `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`。
5. 可选择对生成的 `SparklineGroup` 进行自定义 —— 例如，通过设置 `group.getType()` 来确认类型，或调整条形颜色。
6. 将工作簿保存到单独的输出文件，以免覆盖折线迷你图的示例。
以下示例将值 5、-3、8、-2、6 写入 A1:E1，并在 F1 中渲染柱形迷你图。负值以向下的条形绘制，正值以向上的条形绘制，这使得正负贡献一目了然。

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
dest.StartColumn = 5;
dest.EndColumn = 5;
dest.StartRow = 0;
dest.EndRow = 0;
// Add a Column sparkline to the destination cell
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);
// Confirm the sparkline type by reading group.Type
System.out.println("Sparkline Type added: " + group.getType());
// Save the workbook
workbook.save("output_column.xlsx");
System.out.println("Workbook saved as output_column.xlsx");
```

## **涨/跌迷你图**
涨/跌迷你图是柱形迷你图的一种特殊变体，专为仅显示两种结果而设计：正值绘制为"上升"条形（赢），零或负值绘制为"下降"条形（输）。涨/跌迷你图通常用于可视化胜负序列、通过/未通过结果，或任何随时间变化的二元结果。
在 Aspose.Cells 中，通过将 `SparklineType.STACKED` 传递给 `add` 方法即可创建涨/跌迷你图。（尽管名称如此，`SparklineType.STACKED` 实际上是用于请求涨/跌渲染的枚举值。）
1. 创建一个新的 `Workbook` 并访问第一个工作表。
2. 填充源区域。因为涨/跌迷你图将每个值视为赢或输，值的大小并不重要 —— 重要的是其符号。正值变为上升条形，非正值变为下降条形。
3. 构建一个 `CellArea`，用于描述目标单元格。
4. 调用 `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`。
5. 可选择对返回的 `SparklineGroup` 进行自定义，例如为赢和输条形设置强调颜色。
6. 使用不同的文件名保存工作簿，以便所有三个示例可以在磁盘上共存。

```java
import com.aspose.cells.*;
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
dest.StartColumn = 5;
dest.EndColumn = 5;
dest.StartRow = 0;
dest.EndRow = 0;
// Add a Win/Loss sparkline (SparklineType.Stacked)
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);
// Customize the sparkline group
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Set the high-point color to green
CellsColor highColor = workbook.createCellsColor();
highColor.setColor(Color.getGreen());
group.setHighPointColor(highColor);
// Set the low-point color to red
CellsColor lowColor = workbook.createCellsColor();
lowColor.setColor(Color.getRed());
group.setLowPointColor(lowColor);
// Set the negative-point color to orange
CellsColor negColor = workbook.createCellsColor();
negColor.setColor(Color.getOrange());
group.setNegativePointsColor(negColor);
// Set the default series color (used for positive bars)
CellsColor seriesColor = workbook.createCellsColor();
seriesColor.setColor(Color.fromArgb(70, 130, 180)); // SteelBlue approximation
group.setSeriesColor(seriesColor);
// Save the workbook
workbook.save("output_winloss.xlsx");
System.out.println("Workbook saved successfully: output_winloss.xlsx");
```

## **合并所有三种迷你图类型**
以下组合示例创建一个工作簿，在第 1 行填充值 5、-3、8、-2、6，然后在 F1、F2 和 F3 单元格中添加三个迷你图组 —— 每种类型各一个 —— 使得生成的文件能够一次性演示所有三种迷你图样式。

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

## **自定义迷你图外观**
一旦创建了 `SparklineGroup` 并将其添加到 `worksheet.getSparklineGroups()`，您可以在保存工作簿之前读取或修改其多个视觉属性。最常自定义的属性包括：
- **`group.getType()`** —— `SparklineType`（LINE、COLUMN 或 STACKED）。它在组添加时设置，但您可以读回它以进行确认。
- **`group.getLine().setColor(...)`** —— 线条颜色，表示为通过 `workbook.createCellsColor()` 创建的 `CellsColor`。这是用于折线迷你图描边颜色的属性。
- **`group.getLine().setWeight(...)`** —— 以磅为单位的线宽。值越大，线条越粗。
- **最高/最低点标记** —— 用于在最高和最低数据点上开启小标记的标志，便于强调极值。
- **首点/末点/负点标记** —— 用于在第一个、最后一个和负数据点上切换标记的标志。
要更改颜色，请始终创建一个 `CellsColor` 实例并将其分配给相关属性。不要直接将 `java.awt.Color` 分配给迷你图颜色属性 —— 它们期望来自 `Aspose.Cells.Drawing` 的 `CellsColor` 类型。`add` 方法本身会返回一个完全类型化的 `SparklineGroup` 对象，因此您可以在返回值上链式调用属性赋值，或将其存储在局部变量中并在保存前进行自定义。

{{< app/cells/assistant language="java" >}}