---
title: Modify Page Field Layout in Pivot Table
linktitle: Modify Page Field Layout in Pivot Table
description: Learn how to control the page field area layout in a pivot table using Aspose.Cells for Java, including setting the display order, wrap count, and field order of the page fields at the top of the pivot table.
keywords: Aspose.Cells, Java library, spreadsheet, pivot table, page field, page field order, page field wrap count, move page field
type: docs
weight: 191
url: /java/change-page-field-layout/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

This article is a continuation of the **Add Page Field in Pivot Table** topic. It demonstrates how to control the layout of the page field area — the strip of filter controls at the top of a pivot table — including display order, wrap count, and field reordering.

{{% /alert %}}

## **Introduction**

A pivot table in Microsoft Excel exposes a dedicated **page field area** that sits above the row/column/data body of the table. This area is rendered as a strip of dropdown filter controls (one per page field) and is what end-users click to slice the pivot by criteria such as year or region. Aspose.Cells models this area through the `pivotTable.getPageFields()` collection and exposes three properties that control how the strip is visually laid out:

- `pivotTable.getPageFieldOrder()` (an `Aspose.Cells.PrintOrderType` value) decides whether additional page fields are placed *next to* the existing ones or *below* them.
- `pivotTable.getPageFieldWrapCount()` sets how many page fields are placed per row or column before wrapping.
- `pivotTable.getPageFields().move(currIndex, destIndex)` reorders the page fields without changing the order mode.

This article walks through three code examples that demonstrate each of these operations on a shared dataset, so that you can compare the resulting layouts side-by-side.

## **Source Data**

All three examples below load these eight rows of sales data into a worksheet named `PivotData`. The data contains two page-field candidates (`Year`, `Region`), one row-field candidate (`Fruit`), and one measure (`Amount`), which makes the page-field strip meaningful to inspect.

| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |

All eight rows are populated in every code example, in identical order, so the source data never differs between scenarios — only the page-field layout properties do.

## **Example 1: Over Then Down**

In the first scenario we configure the two page fields (`Year`, `Region`) to appear **side-by-side in a single row** at the top of the pivot table. We assign `Fruit` to the row axis, place `Year` first and `Region` second on the page axis (the order of `addFieldToArea` calls determines the starting index), add `Amount` (Sum) as the data field, and then set `pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)` with `pivotTable.setPageFieldWrapCount(2)`. With `OVER_THEN_DOWN` and a wrap count of 2, the two page fields are laid out horizontally side-by-side in a single row at the top of the pivot table, so the strip occupies one row of width two.

```java
import com.aspose.cells.*;
import java.io.File;

String dataDir = "output";
if (!new File(dataDir).exists()) new File(dataDir).mkdirs();

Workbook workbook = new Workbook();
WorksheetCollection worksheets = workbook.getWorksheets();

Worksheet pivotDataSheet = worksheets.add("PivotData");
Cells pivotDataCells = pivotDataSheet.getCells();

// Headers (row 0)
pivotDataCells.get(0, 0).putValue("Fruit");
pivotDataCells.get(0, 1).putValue("Year");
pivotDataCells.get(0, 2).putValue("Region");
pivotDataCells.get(0, 3).putValue("Amount");

// Row 1: Apple, 2022, North, 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);

// Row 2: Apple, 2023, North, 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);

// Row 3: Banana, 2022, South, 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);

// Row 4: Banana, 2023, South, 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);

// Row 5: Cherry, 2022, East, 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);

// Row 6: Cherry, 2023, East, 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);

// Row 7: Grape, 2022, West, 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);

// Row 8: Grape, 2023, West, 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);

// Add PivotTableReport sheet
Worksheet pivotTableSheet = worksheets.add("PivotTableReport");
PivotTableCollection pivotTables = pivotTableSheet.getPivotTables();

// Create pivot table sourced from PivotData!A1:D9 placed at A1 on PivotTableReport
int pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);

// Add fields
pivotTable.addFieldToArea(PivotFieldType.ROW, 0);   // Fruit
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);  // Year
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);  // Region
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);  // Amount
pivotTable.getDataFields().get(0).setFunction(ConsolidationFunction.SUM);

// Configure page field area layout: place page fields across first, wrap after every 2
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);

// Refresh and calculate
pivotTable.calculateData();

// Save
workbook.save(dataDir + "/pageFieldLayout_overThenDown.xlsx");
```

## **Example 2: Down Then Over**

In this example we place `Fruit` on the row axis, `Year` and `Region` on the page axis (with `Year` first), and `Amount` (Sum) as the data field — exactly as in Example 1. We then set `pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER)` and `pivotTable.setPageFieldWrapCount(2)`. With `DOWN_THEN_OVER` and a wrap count of 2, the two page fields are stacked vertically — `Year` on top, `Region` directly below — forming a single column at the top of the pivot table. The strip therefore occupies two rows of width one, in contrast to Example 1.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
int pivotReportIdx = workbook.getWorksheets().add();
Worksheet pivotReport = workbook.getWorksheets().get(pivotReportIdx);
pivotReport.setName("PivotTableReport");

String[] headers = new String[] { "Fruit", "Year", "Region", "Amount" };
for (int c = 0; c < headers.length; c++)
{
    pivotData.getCells().get(0, c).putValue(headers[c]);
}

Object[][] data = new Object[][]
{
    {"Apple", 2022, "North", 150},
    {"Apple", 2023, "North", 180},
    {"Banana", 2022, "South", 120},
    {"Banana", 2023, "South", 140},
    {"Cherry", 2022, "East", 200},
    {"Cherry", 2023, "East", 220},
    {"Grape", 2022, "West", 90},
    {"Grape", 2023, "West", 110}
};

for (int r = 0; r < data.length; r++)
{
    for (int c = 0; c < data[r].length; c++)
    {
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

int idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
PivotTable pivotTable = pivotReport.getPivotTables().get(idx);

pivotTable.addFieldToArea(PivotFieldType.ROW, 0);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);

pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER);
pivotTable.setPageFieldWrapCount(2);

pivotTable.calculateData();

workbook.save("pageFieldLayout_downThenOver.xlsx");
```

## **Example 3: Move a Page Field**

In the third scenario we keep this dataset and field allocation, set a neutral layout (`OVER_THEN_DOWN` with wrap count `2`), and then demonstrate the `pageFields.move` operation. The `move(0, 1)` call moves the page field at index 0 (`Year`) to position 1, and the page field that was at position 1 (`Region`) shifts to position 0. After this call, `Region` is the first page field and `Year` is the second. The wrap and order mode are unchanged, so the strip is still rendered horizontally side-by-side — only the order of the two dropdowns has been swapped.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();

Worksheet dataSheet = workbook.getWorksheets().get(0);
dataSheet.setName("PivotData");

dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Year");
dataSheet.getCells().get("C1").putValue("Region");
dataSheet.getCells().get("D1").putValue("Amount");

dataSheet.getCells().get("A2").putValue("Apple");
dataSheet.getCells().get("B2").putValue(2022);
dataSheet.getCells().get("C2").putValue("North");
dataSheet.getCells().get("D2").putValue(150);

dataSheet.getCells().get("A3").putValue("Apple");
dataSheet.getCells().get("B3").putValue(2023);
dataSheet.getCells().get("C3").putValue("North");
dataSheet.getCells().get("D3").putValue(180);

dataSheet.getCells().get("A4").putValue("Banana");
dataSheet.getCells().get("B4").putValue(2022);
dataSheet.getCells().get("C4").putValue("South");
dataSheet.getCells().get("D4").putValue(120);

dataSheet.getCells().get("A5").putValue("Banana");
dataSheet.getCells().get("B5").putValue(2023);
dataSheet.getCells().get("C5").putValue("South");
dataSheet.getCells().get("D5").putValue(140);

dataSheet.getCells().get("A6").putValue("Cherry");
dataSheet.getCells().get("B6").putValue(2022);
dataSheet.getCells().get("C6").putValue("East");
dataSheet.getCells().get("D6").putValue(200);

dataSheet.getCells().get("A7").putValue("Cherry");
dataSheet.getCells().get("B7").putValue(2023);
dataSheet.getCells().get("C7").putValue("East");
dataSheet.getCells().get("D7").putValue(220);

dataSheet.getCells().get("A8").putValue("Grape");
dataSheet.getCells().get("B8").putValue(2022);
dataSheet.getCells().get("C8").putValue("West");
dataSheet.getCells().get("D8").putValue(90);

dataSheet.getCells().get("A9").putValue("Grape");
dataSheet.getCells().get("B9").putValue(2023);
dataSheet.getCells().get("C9").putValue("West");
dataSheet.getCells().get("D9").putValue(110);

Worksheet pivotSheet = workbook.getWorksheets().add("PivotTableReport");

int pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable");
PivotTable pivotTable = pivotSheet.getPivotTables().get(pivotIdx);

pivotTable.addFieldToArea(PivotFieldType.ROW, 0);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);

pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);

pivotTable.getPageFields().move(0, 1);

pivotTable.calculateData();

workbook.save("pageFieldLayout_move.xlsx");
```

## **Related Articles**

- [Add Page Field in Pivot Table](/cells/java/add-page-field-in-pivot-table/) — the parent page that introduces how page fields are added to a pivot table.
- [Row and Column Fields in Pivot Table](/cells/java/row-and-column-fields/) — covers allocating fields to the row and column axes, complementing the page-axis work shown here.
- [Manage Value Fields in Pivot Table](/cells/java/manage-value-fields/) — describes how to configure the data (value) area, including the `Sum` aggregation used in this article.
- [Refresh Pivot Table](/cells/java/refresh-pivot-table/) — explains `refreshData()` and `calculateData()`, which are required after reordering page fields.
- [Apply Style to Pivot Table](/cells/java/apply-style-to-pivot-table/) — shows how to format the rendered pivot table after the page-field strip has been laid out.

{{< app/cells/assistant language="java" >}}