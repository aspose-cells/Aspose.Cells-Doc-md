---
title: Format Part of a Pivot Table
description: Format part of a pivot table in Aspose.Cells for Java by applying styles to semantic PivotArea regions or CellArea rectangles through PivotTable.format, with formats stored in PivotTable.getPivotFormats and preserved when the pivot table is refreshed.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells for Java, pivot table, format, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Java
type: docs
weight: 20
url: /java/format-part-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
`PivotTable.formatAll` applies a single style to the entire pivot table and is covered on the parent page. It does not distinguish between labels, values, totals, or particular regions of the report.
In practice, only a portion of a pivot table usually needs to stand out. Common targets include the labels belonging to one row field, the value cells produced by one field, the grand-total row, or an arbitrary rectangle such as the first two item rows.
Applying a style directly to the worksheet cells of a pivot table is not equivalent. Excel stores pivot-table formatting as semantic `PivotArea` regions rather than as ordinary cell-style records. A pivot-area format stays attached to a region such as a field's labels or data values, and it is re-resolved when the pivot table is recalculated, refreshed, or expanded. A style written directly to a cell, on the other hand, belongs to that cell position and is not tracked by the pivot model.
Aspose.Cells exposes the complete `PivotTable.format` overload family so that both kinds of formatting are available:
- `format(PivotArea, Style)` anchors a style to a semantic region that is built with `PivotArea.select` or `PivotArea.selectField`.
- `format(CellArea, Style)` anchors a style to a worksheet rectangle inside the pivot table.
- `format(int row, int column, Style)` targets one cell.
- `formatAll(Style)` formats the whole pivot table.

## **Format a Pivot Area**
The semantic-area workflow is the recommended approach when a highlight must follow a field or a region of the report.
1. Create a `PivotArea` with `new PivotArea(pivotTable)`. The object describes a semantic region that belongs to that specific pivot table.
1. Select a field by its zero-based position on a given axis with `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DATA_AND_LABEL` selects both the labels and the data of the field.
   - `PivotTableSelectionType.LABEL_ONLY` selects only the field's labels.
   - `PivotTableSelectionType.DATA_ONLY` selects only the field's data cells.
1. Select a field by name with `PivotArea.selectField(PivotFieldType axisType, String fieldName)`. When a row field is selected by name, the region resolves to the value cells produced by that field's items.
1. Create a `Style` with `Workbook.createStyle()`, configure its font, foreground color, and solid background pattern, and pass the style to `PivotTable.format(area, style)`.
1. Each call to the `PivotArea` overload appends one `PivotTableFormat` entry to `PivotTable.getPivotFormats()`.
1. Field-anchored formats are painted when the pivot data is calculated. Therefore, call `PivotTable.calculateData()` after applying the formats so that the styles become visible.
The following example builds a small fruit-sales pivot table, styles the `Fruit` row labels with `PivotArea.select` and `PivotTableSelectionType.LABEL_ONLY`, styles the value cells produced by that same row field with `PivotArea.selectField`, and then recalculates the pivot table so both styles are painted.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Fruit sales data
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
Style labelStyle = workbook.createStyle();
labelStyle.getFont().setBold(true);
labelStyle.setForegroundColor(Color.getYellow());
labelStyle.setPattern(BackgroundType.SOLID);
PivotArea labelArea = new PivotArea(pivotTable);
labelArea.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
Style valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(Color.getLightGreen());
valueStyle.setPattern(BackgroundType.SOLID);
PivotArea valueArea = new PivotArea(pivotTable);
valueArea.selectField(PivotFieldType.ROW, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **Format a Cell Area of the Pivot Table**
Use `PivotTable.format(CellArea, Style)` when the region of interest is a plain worksheet rectangle rather than a semantic pivot region.
A `CellArea` is described by the `getStartRow()`, `getStartColumn()`, `getEndRow()`, and `getEndColumn()` properties. The values are zero-based worksheet coordinates, and the end coordinates identify the last row and column that are included in the rectangle, so the area covers the cells from the start position through the end position inclusive.
Unlike a field-anchored format, a `CellArea` format is applied to the cells immediately. Another call to `calculateData()` is not needed for the style to appear.
A `CellArea` rectangle may contain label cells and value cells together. The next section describes how Aspose.Cells and Excel represent that rectangle internally.
The following example formats the rectangle `E4:F5` of the pivot table with an italic, light-blue style and saves the workbook without any further recalculation.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
Style highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(BackgroundType.SOLID);
CellArea rectangle = new CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **How Pivot Areas and Cell Areas Map**
Excel stores pivot-table formatting as `pivotArea` records rather than as ordinary worksheet cell-style records. The same model is used by Aspose.Cells, so a formatting request is translated into pivot areas when it is recorded.
The relationship between the `CellArea` supplied by the user and the pivot areas stored internally is many-to-many in both directions.
- One `CellArea` may produce several pivot areas. If the rectangle spans both label cells and value cells, it is decomposed into separate label and data rules, because the pivot model treats label formatting and data formatting independently.
- One pivot area may resolve to several disjoint `CellArea` instances. A semantic region such as a grand-total row, or a field whose items are not contiguous, can cover multiple rectangles. This is why `PivotArea.getCellAreas()` returns a collection instead of a single rectangle.
Every format operation performed through `PivotTable.format` is recorded in `PivotTable.getPivotFormats()`. Each `PivotTableFormat` entry exposes the associated `PivotArea` and the `Style` that is applied to it. The `PivotArea` overload adds exactly one entry per call, while a `CellArea` that contains different semantic regions can add multiple entries.
To distinguish the stored regions, each `PivotArea` exposes the `getOnlyLabel()` and `getOnlyData()` flags. The example below formats a single rectangle that covers both labels and values, inspects `PivotTable.getPivotFormats()`, and prints the `CellArea` coordinates that each stored pivot area resolves to.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
Style highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(BackgroundType.SOLID);
// ONE rectangle in...
CellArea rectangle = new CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
System.out.println("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (int i = 0; i < pivotTable.getPivotFormats().getCount(); i++)
{
    PivotArea storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    System.out.println("Format " + i + ": OnlyLabel=" + storedArea.getOnlyLabel()
            + ", OnlyData=" + storedArea.getOnlyData());
    for (CellArea resolved : storedArea.getCellAreas())
    {
        System.out.println("    rows " + (resolved.StartRow + 1) + "-" + (resolved.EndRow + 1)
                + ", columns " + (resolved.StartColumn + 1) + "-" + (resolved.EndColumn + 1));
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
Because the formats are stored as pivot areas rather than as ordinary cell styles, they survive recalculation and refresh. When the pivot table is refreshed with `PivotTable.refreshData`, recalculated with `calculateData`, or saved and reloaded, every stored pivot area re-resolves to the current position of its region and its style is re-applied.
{{% /alert %}}

Use a `PivotArea` built with `select` or `selectField` when a highlight must remain attached to a field or a semantic region across refreshes, and use a `CellArea` when formatting a fixed rectangle in the current pivot-table layout is sufficient. The single-cell `format(int row, int column, Style)` overload targets an individual cell. Use `formatAll`, covered on the parent page, when the entire pivot table should be restyled at once.

## **Related Articles**
- [Applying Style to Pivot Table](/cells/java/apply-style-to-pivot-table/)
- [Adding Pivot Table Row and Column Fields](/cells/java/pivot-table-add-row-and-column-fields/)
- [Managing Value Fields in Pivot Table](/cells/java/manage-value-fields/)
- [Refreshing Pivot Table](/cells/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}