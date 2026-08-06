---
title: Modify Page Field Layout in Pivot Table
linktitle: Modify Page Field Layout in Pivot Table
description: Learn how to control the page field area layout in a pivot table using Aspose.Cells for .NET, including setting the display order, wrap count, and field order of the page fields at the top of the pivot table.
keywords: Aspose.Cells, NET library, spreadsheet, pivot table, page field, page field order, page field wrap count, move page field
type: docs
weight: 191
url: /net/change-page-field-layout/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

This article is a continuation of the **Add Page Field in Pivot Table** topic. It demonstrates how to control the layout of the page field area — the strip of filter controls at the top of a pivot table — including display order, wrap count, and field reordering.

{{% /alert %}}

## **Introduction**

A pivot table in Microsoft Excel exposes a dedicated **page field area** that sits above the row/column/data body of the table. This area is rendered as a strip of dropdown filter controls (one per page field) and is what end-users click to slice the pivot by criteria such as year or region. Aspose.Cells models this area through the `PivotTable.PageFields` collection and exposes three properties that control how the strip is visually laid out:

- `PivotTable.PageFieldOrder` (an `Aspose.Cells.PrintOrderType` value) decides whether additional page fields are placed *next to* the existing ones or *below* them.
- `PivotTable.PageFieldWrapCount` sets how many page fields are placed per row or column before wrapping.
- `PivotTable.PageFields.Move(currIndex, destIndex)` reorders the page fields without changing the order mode.

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

In the first scenario we configure the two page fields (`Year`, `Region`) to appear **side-by-side in a single row** at the top of the pivot table. We assign `Fruit` to the row axis, place `Year` first and `Region` second on the page axis (the order of `AddFieldToArea` calls determines the starting index), add `Amount` (Sum) as the data field, and then set `PageFieldOrder` to `PrintOrderType.OverThenDown` with `PageFieldWrapCount = 2`. With `OverThenDown` and a wrap count of 2, the two page fields are laid out horizontally side-by-side in a single row at the top of the pivot table, so the strip occupies one row of width two.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

string dataDir = "output";
if (!Directory.Exists(dataDir)) Directory.CreateDirectory(dataDir);

Workbook workbook = new Workbook();
WorksheetCollection worksheets = workbook.Worksheets;

int pivotDataIdx = worksheets.Add("PivotData");
Worksheet pivotDataSheet = worksheets[pivotDataIdx];
Cells pivotDataCells = pivotDataSheet.Cells;

// Headers (row 0)
pivotDataCells[0, 0].PutValue("Fruit");
pivotDataCells[0, 1].PutValue("Year");
pivotDataCells[0, 2].PutValue("Region");
pivotDataCells[0, 3].PutValue("Amount");

// Row 1: Apple, 2022, North, 150
pivotDataCells[1, 0].PutValue("Apple");
pivotDataCells[1, 1].PutValue(2022);
pivotDataCells[1, 2].PutValue("North");
pivotDataCells[1, 3].PutValue(150);

// Row 2: Apple, 2023, North, 180
pivotDataCells[2, 0].PutValue("Apple");
pivotDataCells[2, 1].PutValue(2023);
pivotDataCells[2, 2].PutValue("North");
pivotDataCells[2, 3].PutValue(180);

// Row 3: Banana, 2022, South, 120
pivotDataCells[3, 0].PutValue("Banana");
pivotDataCells[3, 1].PutValue(2022);
pivotDataCells[3, 2].PutValue("South");
pivotDataCells[3, 3].PutValue(120);

// Row 4: Banana, 2023, South, 140
pivotDataCells[4, 0].PutValue("Banana");
pivotDataCells[4, 1].PutValue(2023);
pivotDataCells[4, 2].PutValue("South");
pivotDataCells[4, 3].PutValue(140);

// Row 5: Cherry, 2022, East, 200
pivotDataCells[5, 0].PutValue("Cherry");
pivotDataCells[5, 1].PutValue(2022);
pivotDataCells[5, 2].PutValue("East");
pivotDataCells[5, 3].PutValue(200);

// Row 6: Cherry, 2023, East, 220
pivotDataCells[6, 0].PutValue("Cherry");
pivotDataCells[6, 1].PutValue(2023);
pivotDataCells[6, 2].PutValue("East");
pivotDataCells[6, 3].PutValue(220);

// Row 7: Grape, 2022, West, 90
pivotDataCells[7, 0].PutValue("Grape");
pivotDataCells[7, 1].PutValue(2022);
pivotDataCells[7, 2].PutValue("West");
pivotDataCells[7, 3].PutValue(90);

// Row 8: Grape, 2023, West, 110
pivotDataCells[8, 0].PutValue("Grape");
pivotDataCells[8, 1].PutValue(2023);
pivotDataCells[8, 2].PutValue("West");
pivotDataCells[8, 3].PutValue(110);

// Add PivotTableReport sheet
int pivotTableSheetIdx = worksheets.Add("PivotTableReport");
Worksheet pivotTableSheet = worksheets[pivotTableSheetIdx];
PivotTableCollection pivotTables = pivotTableSheet.PivotTables;

// Create pivot table sourced from PivotData!A1:D9 placed at A1 on PivotTableReport
int pivotIndex = pivotTables.Add("PivotData!A1:D9", "A1", "PivotTable1");
PivotTable pivotTable = pivotTables[pivotIndex];

// Add fields
pivotTable.AddFieldToArea(PivotFieldType.Row, 0);   // Fruit
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);  // Year
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);  // Region
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);  // Amount
pivotTable.DataFields[0].Function = ConsolidationFunction.Sum;

// Configure page field area layout: place page fields across first, wrap after every 2
pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;

// Refresh and calculate
pivotTable.CalculateData();

// Save
workbook.Save(Path.Combine(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```

## **Example 2: Down Then Over**

In this example we place `Fruit` on the row axis, `Year` and `Region` on the page axis (with `Year` first), and `Amount` (Sum) as the data field — exactly as in Example 1. We then set `PageFieldOrder` to `PrintOrderType.DownThenOver` and `PageFieldWrapCount` to `2`. With `DownThenOver` and a wrap count of 2, the two page fields are stacked vertically — `Year` on top, `Region` directly below — forming a single column at the top of the pivot table. The strip therefore occupies two rows of width one, in contrast to Example 1.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook();
var pivotData = workbook.Worksheets[0];
pivotData.Name = "PivotData";
int pivotReportIdx = workbook.Worksheets.Add("PivotTableReport");
var pivotReport = workbook.Worksheets[pivotReportIdx];

var headers = new[] { "Fruit", "Year", "Region", "Amount" };
for (int c = 0; c < headers.Length; c++)
{
    pivotData.Cells[0, c].PutValue(headers[c]);
}

var data = new object[,]
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

for (int r = 0; r < data.GetLength(0); r++)
{
    for (int c = 0; c < data.GetLength(1); c++)
    {
        pivotData.Cells[r + 1, c].PutValue(data[r, c]);
    }
}

int idx = pivotReport.PivotTables.Add("PivotData!A1:D9", "A1", "PivotTable");
var pivotTable = pivotReport.PivotTables[idx];

pivotTable.AddFieldToArea(PivotFieldType.Row, 0);
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);

pivotTable.PageFieldOrder = PrintOrderType.DownThenOver;
pivotTable.PageFieldWrapCount = 2;

pivotTable.CalculateData();

workbook.Save("pageFieldLayout_downThenOver.xlsx");
```

## **Example 3: Move a Page Field**

In the third scenario we keep this dataset and field allocation, set a neutral layout (`OverThenDown` with wrap count `2`), and then demonstrate the `PageFields.Move` operation. The `Move(0, 1)` call moves the page field at index 0 (`Year`) to position 1, and the page field that was at position 1 (`Region`) shifts to position 0. After this call, `Region` is the first page field and `Year` is the second. The wrap and order mode are unchanged, so the strip is still rendered horizontally side-by-side — only the order of the two dropdowns has been swapped.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();

Worksheet dataSheet = workbook.Worksheets[0];
dataSheet.Name = "PivotData";

dataSheet.Cells["A1"].PutValue("Fruit");
dataSheet.Cells["B1"].PutValue("Year");
dataSheet.Cells["C1"].PutValue("Region");
dataSheet.Cells["D1"].PutValue("Amount");

dataSheet.Cells["A2"].PutValue("Apple");
dataSheet.Cells["B2"].PutValue(2022);
dataSheet.Cells["C2"].PutValue("North");
dataSheet.Cells["D2"].PutValue(150);

dataSheet.Cells["A3"].PutValue("Apple");
dataSheet.Cells["B3"].PutValue(2023);
dataSheet.Cells["C3"].PutValue("North");
dataSheet.Cells["D3"].PutValue(180);

dataSheet.Cells["A4"].PutValue("Banana");
dataSheet.Cells["B4"].PutValue(2022);
dataSheet.Cells["C4"].PutValue("South");
dataSheet.Cells["D4"].PutValue(120);

dataSheet.Cells["A5"].PutValue("Banana");
dataSheet.Cells["B5"].PutValue(2023);
dataSheet.Cells["C5"].PutValue("South");
dataSheet.Cells["D5"].PutValue(140);

dataSheet.Cells["A6"].PutValue("Cherry");
dataSheet.Cells["B6"].PutValue(2022);
dataSheet.Cells["C6"].PutValue("East");
dataSheet.Cells["D6"].PutValue(200);

dataSheet.Cells["A7"].PutValue("Cherry");
dataSheet.Cells["B7"].PutValue(2023);
dataSheet.Cells["C7"].PutValue("East");
dataSheet.Cells["D7"].PutValue(220);

dataSheet.Cells["A8"].PutValue("Grape");
dataSheet.Cells["B8"].PutValue(2022);
dataSheet.Cells["C8"].PutValue("West");
dataSheet.Cells["D8"].PutValue(90);

dataSheet.Cells["A9"].PutValue("Grape");
dataSheet.Cells["B9"].PutValue(2023);
dataSheet.Cells["C9"].PutValue("West");
dataSheet.Cells["D9"].PutValue(110);

int pivotSheetIdx = workbook.Worksheets.Add("PivotTableReport");
Worksheet pivotSheet = workbook.Worksheets[pivotSheetIdx];

int pivotIdx = pivotSheet.PivotTables.Add("PivotData!A1:D9", "A3", "PivotTable");
PivotTable pivotTable = pivotSheet.PivotTables[pivotIdx];

pivotTable.AddFieldToArea(PivotFieldType.Row, 0);
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);

pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;

pivotTable.PageFields.Move(0, 1);

pivotTable.CalculateData();

workbook.Save("pageFieldLayout_move.xlsx");
```

## **Related Articles**

- [Add Page Field in Pivot Table](/cells/net/add-page-field-in-pivot-table/) — the parent page that introduces how page fields are added to a pivot table.
- [Row and Column Fields in Pivot Table](/cells/net/pivot-table-add-row-and-column-fields/) — covers allocating fields to the row and column axes, complementing the page-axis work shown here.
- [Manage Value Fields in Pivot Table](/cells/net/manage-value-fields/) — describes how to configure the data (value) area, including the `Sum` aggregation used in this article.
- [Refresh Pivot Table](/cells/net/refresh-pivot-table/) — explains `RefreshData` and `CalculateData`, which are required after reordering page fields.
- [Apply Style to Pivot Table](/cells/net/apply-style-to-pivot-table/) — shows how to format the rendered pivot table after the page-field strip has been laid out.

{{< app/cells/assistant language="csharp" >}}