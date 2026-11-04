---
title: Format Part of a Pivot Table
description: Format part of a pivot table in Aspose.Cells for C++ by applying styles to semantic PivotArea regions or CellArea rectangles through PivotTable.Format, with formats stored in PivotTable.GetPivotFormats and preserved when the pivot table is refreshed.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells, pivot table, format, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C++
type: docs
weight: 20
url: /cpp/format-part-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
`PivotTable.FormatAll` applies a single style to the entire pivot table and is covered on the parent page. It does not distinguish between labels, values, totals, or particular regions of the report.
In practice, only a portion of a pivot table usually needs to stand out. Common targets include the labels belonging to one row field, the value cells produced by one field, the grand-total row, or an arbitrary rectangle such as the first two item rows.
Applying a style directly to the worksheet cells of a pivot table is not equivalent. Excel stores pivot-table formatting as semantic `PivotArea` regions rather than as ordinary cell-style records. A pivot-area format stays attached to a region such as a field's labels or data values, and it is re-resolved when the pivot table is recalculated, refreshed, or expanded. A style written directly to a cell, on the other hand, belongs to that cell position and is not tracked by the pivot model.
Aspose.Cells exposes the complete `PivotTable.Format` overload family so that both kinds of formatting are available:
- `Format(const PivotArea&, const Style&)` anchors a style to a semantic region that is built with `PivotArea.Select` or `PivotArea.SelectField`.
- `Format(const CellArea&, const Style&)` anchors a style to a worksheet rectangle inside the pivot table.
- `Format(int32_t row, int32_t column, const Style&)` targets one cell.
- `FormatAll(const Style&)` formats the whole pivot table.

## **Format a Pivot Area**
The semantic-area workflow is the recommended approach when a highlight must follow a field or a region of the report.
1. Create a `PivotArea` with `PivotArea pivotArea(pivotTable);`. The object describes a semantic region that belongs to that specific pivot table.
1. Select a field by its zero-based position on a given axis with `PivotArea.Select(PivotFieldType axisType, int32_t fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType::DataAndLabel` selects both the labels and the data of the field.
   - `PivotTableSelectionType::LabelOnly` selects only the field's labels.
   - `PivotTableSelectionType::DataOnly` selects only the field's data cells.
1. Select a field by name with `PivotArea.SelectField(PivotFieldType axisType, const char16_t* fieldName)`. When a row field is selected by name, the region resolves to the value cells produced by that field's items.
1. Create a `Style` with `Workbook.CreateStyle()`, configure its font, foreground color, and solid background pattern, and pass the style to `PivotTable.Format(pivotArea, style)`.
1. Each call to the `PivotArea` overload appends one `PivotTableFormat` entry to `PivotTable.GetPivotFormats()`.
1. Field-anchored formats are painted when the pivot data is calculated. Therefore, call `PivotTable.CalculateData()` after applying the formats so that the styles become visible.
The following example builds a small fruit-sales pivot table, styles the `Fruit` row labels with `PivotArea.Select` and `PivotTableSelectionType::LabelOnly`, styles the value cells produced by that same row field with `PivotArea.SelectField`, and then recalculates the pivot table so both styles are painted.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Fruit sales data
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    // Pivot table with its top-left corner at E3
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Bold yellow fill on the row field's label cells
    Style labelStyle = workbook.CreateStyle();
    labelStyle.GetFont().SetIsBold(true);
    labelStyle.SetForegroundColor(Color::Yellow());
    labelStyle.SetPattern(BackgroundType::Solid);
    PivotArea labelArea(pivotTable);
    labelArea.Select(PivotFieldType::Row, 0, PivotTableSelectionType::LabelOnly);
    pivotTable.Format(labelArea, labelStyle);
    // Light green fill on the value cells the row field produces
    Style valueStyle = workbook.CreateStyle();
    valueStyle.SetForegroundColor(Color::LightGreen());
    valueStyle.SetPattern(BackgroundType::Solid);
    PivotArea valueArea(pivotTable);
    valueArea.SelectField(PivotFieldType::Row, u"Fruit");
    pivotTable.Format(valueArea, valueStyle);
    // Field-anchored formats are painted when the data is calculated
    pivotTable.CalculateData();
    // Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
    workbook.Save(u"FormatPivotArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Format a Cell Area of the Pivot Table**
Use `PivotTable.Format(const CellArea&, const Style&)` when the region of interest is a plain worksheet rectangle rather than a semantic pivot region.
A `CellArea` is described by the `StartRow`, `StartColumn`, `EndRow`, and `EndColumn` public fields. The values are zero-based worksheet coordinates, and the end coordinates identify the last row and column that are included in the rectangle, so the area covers the cells from the start position through the end position inclusive.
Unlike a field-anchored format, a `CellArea` format is applied to the cells immediately. Another call to `CalculateData()` is not needed for the style to appear.
A `CellArea` rectangle may contain label cells and value cells together. The next section describes how Aspose.Cells and Excel represent that rectangle internally.
The following example formats the rectangle `E4:F5` of the pivot table with an italic, light-blue style and saves the workbook without any further recalculation.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Highlight the first two fruit rows (the rectangle E4:F5)
    Style highlightStyle = workbook.CreateStyle();
    highlightStyle.GetFont().SetIsItalic(true);
    highlightStyle.SetForegroundColor(Color{ 0xFF, 0x99, 0xCC, 0xFF });
    highlightStyle.SetPattern(BackgroundType::Solid);
    CellArea rectangle;
    rectangle.StartRow = 3;
    rectangle.StartColumn = 4;
    rectangle.EndRow = 4;
    rectangle.EndColumn = 5;
    pivotTable.Format(rectangle, highlightStyle);
    // E4:F5 is italic on light blue immediately, no recalculation needed
    workbook.Save(u"FormatPivotCellArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **How Pivot Areas and Cell Areas Map**
Excel stores pivot-table formatting as `pivotArea` records rather than as ordinary worksheet cell-style records. The same model is used by Aspose.Cells, so a formatting request is translated into pivot areas when it is recorded.
The relationship between the `CellArea` supplied by the user and the pivot areas stored internally is many-to-many in both directions.
- One `CellArea` may produce several pivot areas. If the rectangle spans both label cells and value cells, it is decomposed into separate label and data rules, because the pivot model treats label formatting and data formatting independently.
- One pivot area may resolve to several disjoint `CellArea` instances. A semantic region such as a grand-total row, or a field whose items are not contiguous, can cover multiple rectangles. This is why `PivotArea.GetCellAreas()` returns a `Vector<CellArea>` instead of a single rectangle.
Every format operation performed through `PivotTable.Format` is recorded in `PivotTable.GetPivotFormats()`. Each `PivotTableFormat` entry exposes the associated `PivotArea` and the `Style` that is applied to it. The `PivotArea` overload adds exactly one entry per call, while a `CellArea` that contains different semantic regions can add multiple entries.
To distinguish the stored regions, each `PivotArea` exposes the `GetOnlyLabel()` and `GetOnlyData()` flags. The example below formats a single rectangle that covers both labels and values, inspects `PivotTable.GetPivotFormats()`, and prints the `CellArea` coordinates that each stored pivot area resolves to.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[] = { u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry" };
    int years[] = { 2024, 2024, 2025, 2025, 2024, 2025 };
    int amounts[] = { 100, 150, 120, 180, 90, 110 };
    for (int i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    Style highlightStyle = workbook.CreateStyle();
    highlightStyle.GetFont().SetIsItalic(true);
    highlightStyle.SetForegroundColor(Color{ 0xFF, 0x99, 0xCC, 0xFF });
    highlightStyle.SetPattern(BackgroundType::Solid);
    // ONE rectangle in...
    CellArea rectangle;
    rectangle.StartRow = 3;
    rectangle.StartColumn = 4;
    rectangle.EndRow = 4;
    rectangle.EndColumn = 5;
    pivotTable.Format(rectangle, highlightStyle);
    // ...TWO semantic pivot areas out: the label part and the data part are stored separately
    std::cout << "Stored formats: " << pivotTable.GetPivotFormats().GetCount() << std::endl;
    for (int i = 0; i < pivotTable.GetPivotFormats().GetCount(); i++)
    {
        PivotArea storedArea = pivotTable.GetPivotFormats().Get(i).GetPivotArea();
        std::cout << "Format " << i << ": OnlyLabel=" << (storedArea.GetOnlyLabel() ? "true" : "false")
                  << ", OnlyData=" << (storedArea.GetOnlyData() ? "true" : "false") << std::endl;
        Vector<CellArea> resolved = storedArea.GetCellAreas();
        for (int j = 0; j < resolved.GetLength(); j++)
        {
            std::cout << "    rows " << (resolved[j].StartRow + 1) << "-" << (resolved[j].EndRow + 1)
                      << ", columns " << (resolved[j].StartColumn + 1) << "-" << (resolved[j].EndColumn + 1) << std::endl;
        }
    }
    // This prints:
    // Stored formats: 2
    // Format 0: OnlyLabel=true, OnlyData=false
    //     rows 4-5, columns 5-5        (E4:E5, the label part)
    // Format 1: OnlyLabel=false, OnlyData=true
    //     rows 4-5, columns 6-6        (F4:F5, the data part)
    workbook.Save(u"FormatPivotAreasMap.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}
Because the formats are stored as pivot areas rather than as ordinary cell styles, they survive recalculation and refresh. When the pivot table is refreshed with `PivotTable.RefreshData`, recalculated with `CalculateData`, or saved and reloaded, every stored pivot area re-resolves to the current position of its region and its style is re-applied.
{{% /alert %}}

Use a `PivotArea` built with `Select` or `SelectField` when a highlight must remain attached to a field or a semantic region across refreshes, and use a `CellArea` when formatting a fixed rectangle in the current pivot-table layout is sufficient. The single-cell `Format(int32_t row, int32_t column, const Style&)` overload targets an individual cell. Use `FormatAll`, covered on the parent page, when the entire pivot table should be restyled at once.

## **Related Articles**
- [Applying Style to Pivot Table](/cells/cpp/apply-style-to-pivot-table/)
- [Adding Pivot Table Row and Column Fields](/cells/cpp/pivot-table-add-row-and-column-fields/)
- [Managing Value Fields in Pivot Table](/cells/cpp/manage-value-fields/)
- [Refreshing Pivot Table](/cells/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}