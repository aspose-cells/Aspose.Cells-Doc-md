---
title: Modify Page Field Layout in Pivot Table
linktitle: Modify Page Field Layout in Pivot Table
description: Learn how to control the page field area layout in a pivot table using Aspose.Cells for C++, including setting the display order, wrap count, and field order of the page fields at the top of the pivot table.
keywords: Aspose.Cells, C++ library, spreadsheet, pivot table, page field, page field order, page field wrap count, move page field
type: docs
weight: 191
url: /cpp/change-page-field-layout/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

This article is a continuation of the **Add Page Field in Pivot Table** topic. It demonstrates how to control the layout of the page field area — the strip of filter controls at the top of a pivot table — including display order, wrap count, and field reordering.

{{% /alert %}}

## **Introduction**

A pivot table in Microsoft Excel exposes a dedicated **page field area** that sits above the row/column/data body of the table. This area is rendered as a strip of dropdown filter controls (one per page field) and is what end-users click to slice the pivot by criteria such as year or region. Aspose.Cells for C++ models this area through the `PivotTable.PageFields` collection and exposes three properties that control how the strip is visually laid out:

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

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "output";
    if (!std::filesystem::exists(dataDir)) {
        std::filesystem::create_directories(dataDir);
    }

    Workbook workbook;
    WorksheetCollection worksheets = workbook.GetWorksheets();

    Worksheet pivotDataSheet = worksheets.Add(u"PivotData");
    Cells pivotDataCells = pivotDataSheet.GetCells();

    // Headers (row 0)
    pivotDataCells.Get(0, 0).PutValue(u"Fruit");
    pivotDataCells.Get(0, 1).PutValue(u"Year");
    pivotDataCells.Get(0, 2).PutValue(u"Region");
    pivotDataCells.Get(0, 3).PutValue(u"Amount");

    // Row 1: Apple, 2022, North, 150
    pivotDataCells.Get(1, 0).PutValue(u"Apple");
    pivotDataCells.Get(1, 1).PutValue(2022);
    pivotDataCells.Get(1, 2).PutValue(u"North");
    pivotDataCells.Get(1, 3).PutValue(150);

    // Row 2: Apple, 2023, North, 180
    pivotDataCells.Get(2, 0).PutValue(u"Apple");
    pivotDataCells.Get(2, 1).PutValue(2023);
    pivotDataCells.Get(2, 2).PutValue(u"North");
    pivotDataCells.Get(2, 3).PutValue(180);

    // Row 3: Banana, 2022, South, 120
    pivotDataCells.Get(3, 0).PutValue(u"Banana");
    pivotDataCells.Get(3, 1).PutValue(2022);
    pivotDataCells.Get(3, 2).PutValue(u"South");
    pivotDataCells.Get(3, 3).PutValue(120);

    // Row 4: Banana, 2023, South, 140
    pivotDataCells.Get(4, 0).PutValue(u"Banana");
    pivotDataCells.Get(4, 1).PutValue(2023);
    pivotDataCells.Get(4, 2).PutValue(u"South");
    pivotDataCells.Get(4, 3).PutValue(140);

    // Row 5: Cherry, 2022, East, 200
    pivotDataCells.Get(5, 0).PutValue(u"Cherry");
    pivotDataCells.Get(5, 1).PutValue(2022);
    pivotDataCells.Get(5, 2).PutValue(u"East");
    pivotDataCells.Get(5, 3).PutValue(200);

    // Row 6: Cherry, 2023, East, 220
    pivotDataCells.Get(6, 0).PutValue(u"Cherry");
    pivotDataCells.Get(6, 1).PutValue(2023);
    pivotDataCells.Get(6, 2).PutValue(u"East");
    pivotDataCells.Get(6, 3).PutValue(220);

    // Row 7: Grape, 2022, West, 90
    pivotDataCells.Get(7, 0).PutValue(u"Grape");
    pivotDataCells.Get(7, 1).PutValue(2022);
    pivotDataCells.Get(7, 2).PutValue(u"West");
    pivotDataCells.Get(7, 3).PutValue(90);

    // Row 8: Grape, 2023, West, 110
    pivotDataCells.Get(8, 0).PutValue(u"Grape");
    pivotDataCells.Get(8, 1).PutValue(2023);
    pivotDataCells.Get(8, 2).PutValue(u"West");
    pivotDataCells.Get(8, 3).PutValue(110);

    // Add PivotTableReport sheet
    Worksheet pivotTableSheet = worksheets.Add(u"PivotTableReport");
    PivotTableCollection pivotTables = pivotTableSheet.GetPivotTables();

    // Create pivot table sourced from PivotData!A1:D9 placed at A1 on PivotTableReport
    int pivotIndex = pivotTables.Add(u"PivotData!A1:D9", u"A1", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    // Add fields
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);   // Fruit
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);  // Year
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);  // Region
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);  // Amount
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    // Configure page field area layout: place page fields across first, wrap after every 2
    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);

    // Refresh and calculate
    pivotTable.CalculateData();

    // Save
    std::string filePath = dataDir + "/pageFieldLayout_overThenDown.xlsx";
    workbook.Save(U16String(filePath.c_str()));

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Example 2: Down Then Over**

In this example we place `Fruit` on the row axis, `Year` and `Region` on the page axis (with `Year` first), and `Amount` (Sum) as the data field — exactly as in Example 1. We then set `PageFieldOrder` to `PrintOrderType.DownThenOver` and `PageFieldWrapCount` to `2`. With `DownThenOver` and a wrap count of 2, the two page fields are stacked vertically — `Year` on top, `Region` directly below — forming a single column at the top of the pivot table. The strip therefore occupies two rows of width one, in contrast to Example 1.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet pivotData = workbook.GetWorksheets().Get(0);
    pivotData.SetName(u"PivotData");
    Worksheet pivotReport = workbook.GetWorksheets().Add(u"PivotTableReport");

    const char* headers[] = { "Fruit", "Year", "Region", "Amount" };
    for (int c = 0; c < 4; c++)
    {
        pivotData.GetCells().Get(0, c).PutValue(U16String(headers[c]));
    }

    struct DataRow {
        U16String fruit;
        int year;
        U16String region;
        int amount;
    };

    DataRow data[] = {
        {U16String("Apple"),  2022, U16String("North"), 150},
        {U16String("Apple"),  2023, U16String("North"), 180},
        {U16String("Banana"), 2022, U16String("South"), 120},
        {U16String("Banana"), 2023, U16String("South"), 140},
        {U16String("Cherry"), 2022, U16String("East"),  200},
        {U16String("Cherry"), 2023, U16String("East"),  220},
        {U16String("Grape"),  2022, U16String("West"),  90},
        {U16String("Grape"),  2023, U16String("West"),  110}
    };

    for (int r = 0; r < 8; r++)
    {
        pivotData.GetCells().Get(r + 1, 0).PutValue(data[r].fruit);
        pivotData.GetCells().Get(r + 1, 1).PutValue(data[r].year);
        pivotData.GetCells().Get(r + 1, 2).PutValue(data[r].region);
        pivotData.GetCells().Get(r + 1, 3).PutValue(data[r].amount);
    }

    int idx = pivotReport.GetPivotTables().Add(u"PivotData!A1:D9", u"A1", u"PivotTable");
    PivotTable pivotTable = pivotReport.GetPivotTables().Get(idx);

    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);

    pivotTable.SetPageFieldOrder(PrintOrderType::DownThenOver);
    pivotTable.SetPageFieldWrapCount(2);

    pivotTable.CalculateData();

    workbook.Save(u"pageFieldLayout_downThenOver.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Example 3: Move a Page Field**

In the third scenario we keep this dataset and field allocation, set a neutral layout (`OverThenDown` with wrap count `2`), and then demonstrate the `PageFields.Move` operation. The `Move(0, 1)` call moves the page field at index 0 (`Year`) to position 1, and the page field that was at position 1 (`Region`) shifts to position 0. After this call, `Region` is the first page field and `Year` is the second. The wrap and order mode are unchanged, so the strip is still rendered horizontally side-by-side — only the order of the two dropdowns has been swapped.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;

    Worksheet dataSheet = wb.GetWorksheets().Get(0);
    dataSheet.SetName(u"PivotData");

    Cells dataCells = dataSheet.GetCells();

    dataCells.Get(u"A1").PutValue(u"Fruit");
    dataCells.Get(u"B1").PutValue(u"Year");
    dataCells.Get(u"C1").PutValue(u"Region");
    dataCells.Get(u"D1").PutValue(u"Amount");

    dataCells.Get(u"A2").PutValue(u"Apple");
    dataCells.Get(u"B2").PutValue(2022);
    dataCells.Get(u"C2").PutValue(u"North");
    dataCells.Get(u"D2").PutValue(150);

    dataCells.Get(u"A3").PutValue(u"Apple");
    dataCells.Get(u"B3").PutValue(2023);
    dataCells.Get(u"C3").PutValue(u"North");
    dataCells.Get(u"D3").PutValue(180);

    dataCells.Get(u"A4").PutValue(u"Banana");
    dataCells.Get(u"B4").PutValue(2022);
    dataCells.Get(u"C4").PutValue(u"South");
    dataCells.Get(u"D4").PutValue(120);

    dataCells.Get(u"A5").PutValue(u"Banana");
    dataCells.Get(u"B5").PutValue(2023);
    dataCells.Get(u"C5").PutValue(u"South");
    dataCells.Get(u"D5").PutValue(140);

    dataCells.Get(u"A6").PutValue(u"Cherry");
    dataCells.Get(u"B6").PutValue(2022);
    dataCells.Get(u"C6").PutValue(u"East");
    dataCells.Get(u"D6").PutValue(200);

    dataCells.Get(u"A7").PutValue(u"Cherry");
    dataCells.Get(u"B7").PutValue(2023);
    dataCells.Get(u"C7").PutValue(u"East");
    dataCells.Get(u"D7").PutValue(220);

    dataCells.Get(u"A8").PutValue(u"Grape");
    dataCells.Get(u"B8").PutValue(2022);
    dataCells.Get(u"C8").PutValue(u"West");
    dataCells.Get(u"D8").PutValue(90);

    dataCells.Get(u"A9").PutValue(u"Grape");
    dataCells.Get(u"B9").PutValue(2023);
    dataCells.Get(u"C9").PutValue(u"West");
    dataCells.Get(u"D9").PutValue(110);

    Worksheet pivotSheet = wb.GetWorksheets().Add(u"PivotTableReport");

    int32_t pivotIndex = pivotSheet.GetPivotTables().Add(u"PivotData!A1:D9", u"A3", u"PivotTable");
    PivotTable pivotTable = pivotSheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);

    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);

    pivotTable.GetPageFields().Move(0, 1);

    pivotTable.CalculateData();

    wb.Save(u"pageFieldLayout_move.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Related Articles**

- [Add Page Field in Pivot Table](/cells/cpp/add-page-field-in-pivot-table/) — the parent page that introduces how page fields are added to a pivot table.
- [Row and Column Fields in Pivot Table](/cells/cpp/row-and-column-fields/) — covers allocating fields to the row and column axes, complementing the page-axis work shown here.
- [Manage Value Fields in Pivot Table](/cells/cpp/manage-value-fields/) — describes how to configure the data (value) area, including the `Sum` aggregation used in this article.
- [Refresh Pivot Table](/cells/cpp/refresh-pivot-table/) — explains `RefreshData` and `CalculateData`, which are required after reordering page fields.
- [Apply Style to Pivot Table](/cells/cpp/apply-style-to-pivot-table/) — shows how to format the rendered pivot table after the page-field strip has been laid out.

{{< app/cells/assistant language="" >}}