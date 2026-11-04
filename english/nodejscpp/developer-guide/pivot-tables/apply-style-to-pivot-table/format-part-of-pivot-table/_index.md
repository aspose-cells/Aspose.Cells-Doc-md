---
title: Format Part of a Pivot Table
description: Format part of a pivot table in Aspose.Cells for Node.js via C++ by applying styles to semantic PivotArea regions or CellArea rectangles through PivotTable.format, with formats stored in PivotTable.getPivotFormats() and preserved when the pivot table is refreshed.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells, Node.js via C++, pivot table, format, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, selectField, formatAll
type: docs
weight: 20
url: /nodejs-cpp/format-part-of-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
`PivotTable.formatAll` applies a single style to the entire pivot table and is covered on the parent page. It does not distinguish between labels, values, totals, or particular regions of the report.
In practice, only a portion of a pivot table usually needs to stand out. Common targets include the labels belonging to one row field, the value cells produced by one field, the grand-total row, or an arbitrary rectangle such as the first two item rows.
Applying a style directly to the worksheet cells of a pivot table is not equivalent. Excel stores pivot-table formatting as semantic `PivotArea` regions rather than as ordinary cell-style records. A pivot-area format stays attached to a region such as a field's labels or data values, and it is re-resolved when the pivot table is recalculated, refreshed, or expanded. A style written directly to a cell, on the other hand, belongs to that cell position and is not tracked by the pivot model.
Aspose.Cells exposes the complete `PivotTable.format` overload family so that both kinds of formatting are available:
- `format(PivotArea, Style)` anchors a style to a semantic region that is built with `PivotArea.select` or `PivotArea.selectField`.
- `format(CellArea, Style)` anchors a style to a worksheet rectangle inside the pivot table.
- `format(number row, number column, Style)` targets one cell.
- `formatAll(Style)` formats the whole pivot table.

## **Format a Pivot Area**
The semantic-area workflow is the recommended approach when a highlight must follow a field or a region of the report.
1. Create a `PivotArea` with `new PivotArea(pivotTable)`. The object describes a semantic region that belongs to that specific pivot table.
1. Select a field by its zero-based position on a given axis with `PivotArea.select(PivotFieldType axisType, number fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DataAndLabel` selects both the labels and the data of the field.
   - `PivotTableSelectionType.LabelOnly` selects only the field's labels.
   - `PivotTableSelectionType.DataOnly` selects only the field's data cells.
1. Select a field by name with `PivotArea.selectField(PivotFieldType axisType, string fieldName)`. When a row field is selected by name, the region resolves to the value cells produced by that field's items.
1. Create a `Style` with `workbook.createStyle()`, configure its font, foreground color, and solid background pattern, and pass the style to `pivotTable.format(area, style)`.
1. Each call to the `PivotArea` overload appends one `PivotTableFormat` entry to `pivotTable.getPivotFormats()`.
1. Field-anchored formats are painted when the pivot data is calculated. Therefore, call `pivotTable.calculateData()` after applying the formats so that the styles become visible.
The following example builds a small fruit-sales pivot table, styles the `Fruit` row labels with `PivotArea.select` and `PivotTableSelectionType.LabelOnly`, styles the value cells produced by that same row field with `PivotArea.selectField`, and then recalculates the pivot table so both styles are painted.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
// Fruit sales data
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
const labelStyle = workbook.createStyle();
labelStyle.getFont().setIsBold(true);
labelStyle.setForegroundColor(AsposeCells.Color.Yellow);
labelStyle.setPattern(AsposeCells.BackgroundType.Solid);
const labelArea = new AsposeCells.PivotArea(pivotTable);
labelArea.select(
    AsposeCells.PivotFieldType.Row,
    0,
    AsposeCells.PivotTableSelectionType.LabelOnly
);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
const valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(AsposeCells.Color.LightGreen);
valueStyle.setPattern(AsposeCells.BackgroundType.Solid);
const valueArea = new AsposeCells.PivotArea(pivotTable);
valueArea.selectField(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **Format a Cell Area of the Pivot Table**
Use `PivotTable.format(CellArea, Style)` when the region of interest is a plain worksheet rectangle rather than a semantic pivot region.
A `CellArea` is described by its `startRow`, `startColumn`, `endRow`, and `endColumn` properties. The values are zero-based worksheet coordinates, and the end coordinates identify the last row and column that are included in the rectangle, so the area covers the cells from the start position through the end position inclusive.
Unlike a field-anchored format, a `CellArea` format is applied to the cells immediately. Another call to `pivotTable.calculateData()` is not needed for the style to appear.
A `CellArea` rectangle may contain label cells and value cells together. The next section describes how Aspose.Cells and Excel represent that rectangle internally.
The following example formats the rectangle `E4:F5` of the pivot table with an italic, light-blue style and saves the workbook without any further recalculation.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setIsItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.LightBlue);
highlightStyle.setPattern(AsposeCells.BackgroundType.Solid);
const rectangle = new AsposeCells.CellArea();
rectangle.startRow = 3;
rectangle.startColumn = 4;
rectangle.endRow = 4;
rectangle.endColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **How Pivot Areas and Cell Areas Map**
Excel stores pivot-table formatting as `pivotArea` records rather than as ordinary worksheet cell-style records. The same model is used by Aspose.Cells, so a formatting request is translated into pivot areas when it is recorded.
The relationship between the `CellArea` supplied by the user and the pivot areas stored internally is many-to-many in both directions.
- One `CellArea` may produce several pivot areas. If the rectangle spans both label cells and value cells, it is decomposed into separate label and data rules, because the pivot model treats label formatting and data formatting independently.
- One pivot area may resolve to several disjoint `CellArea` instances. A semantic region such as a grand-total row, or a field whose items are not contiguous, can cover multiple rectangles. This is why `PivotArea.getCellAreas()` returns a collection instead of a single rectangle.
Every format operation performed through `pivotTable.format()` is recorded in `pivotTable.getPivotFormats()`. Each `PivotTableFormat` entry exposes the associated `PivotArea` and the `Style` that is applied to it. The `PivotArea` overload adds exactly one entry per call, while a `CellArea` that contains different semantic regions can add multiple entries.
To distinguish the stored regions, each `PivotArea` exposes the `getOnlyLabel()` and `getOnlyData()` flags. The example below formats a single rectangle that covers both labels and values, inspects `pivotTable.getPivotFormats()`, and prints the `CellArea` coordinates that each stored pivot area resolves to.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();
const fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"];
const years = [2024, 2024, 2025, 2025, 2024, 2025];
const amounts = [100, 150, 120, 180, 90, 110];
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (let i = 0; i < fruits.length; i++) {
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
const highlightStyle = workbook.createStyle();
highlightStyle.getFont().setIsItalic(true);
highlightStyle.setForegroundColor(AsposeCells.Color.LightBlue);
highlightStyle.setPattern(AsposeCells.BackgroundType.Solid);
// ONE rectangle in...
const rectangle = new AsposeCells.CellArea();
rectangle.startRow = 3;
rectangle.startColumn = 4;
rectangle.endRow = 4;
rectangle.endColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
console.log("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (let i = 0; i < pivotTable.getPivotFormats().getCount(); i++) {
    const storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    console.log(
        `Format ${i}: OnlyLabel=${storedArea.getOnlyLabel()}, OnlyData=${storedArea.getOnlyData()}`
    );
    const resolvedAreas = storedArea.getCellAreas();
    for (const resolved of resolvedAreas) {
        console.log(
            `    rows ${resolved.startRow + 1}-${resolved.endRow + 1}, ` +
            `columns ${resolved.startColumn + 1}-${resolved.endColumn + 1}`
        );
    }
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=true, OnlyData=false
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=false, OnlyData=true
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
Because the formats are stored as pivot areas rather than as ordinary cell styles, they survive recalculation and refresh. When the pivot table is refreshed with `pivotTable.refreshData()`, recalculated with `pivotTable.calculateData()`, or saved and reloaded, every stored pivot area re-resolves to the current position of its region and its style is re-applied.
{{% /alert %}}

Use a `PivotArea` built with `select` or `selectField` when a highlight must remain attached to a field or a semantic region across refreshes, and use a `CellArea` when formatting a fixed rectangle in the current pivot-table layout is sufficient. The single-cell `format(number row, number column, Style)` overload targets an individual cell. Use `formatAll`, covered on the parent page, when the entire pivot table should be restyled at once.

## **Related Articles**
- [Applying Style to Pivot Table](/cells/nodejs-cpp/apply-style-to-pivot-table/)
- [Adding Pivot Table Row and Column Fields](/cells/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Managing Value Fields in Pivot Table](/cells/nodejs-cpp/manage-value-fields/)
- [Refreshing Pivot Table](/cells/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}