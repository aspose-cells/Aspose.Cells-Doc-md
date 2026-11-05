---
title: Add Conditional Formatting to a Pivot Table
description: Add conditional formatting to a pivot table in Aspose.Cells for Node.js via Java - anchor a rule to the data region with applyTo and a PivotConditionFormatScopeType scope, or define the target with addCellArea and getPivotAreas, then attach rules and styles through getFormatConditions().addCondition.
linktitle: Add Conditional Formatting to a Pivot Table
keywords: Aspose.Cells, pivot table, conditional formatting, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Node.js via Java
type: docs
weight: 30
url: /nodejs-java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
The styles described on the parent page and on the sibling page are static - a `PivotArea` or `CellArea` region is painted once and keeps its style no matter what the values are. Conditional formatting is the rule-driven counterpart - highlight every amount above 200, shade the middle fifty percent, or flag the bottom-ranked items - and the highlight follows the values whenever the pivot table is recalculated or refreshed.
In Aspose.Cells for Node.js via Java, pivot-table conditional formatting lives in the `pivotTable.getConditionalFormats()` collection. Each entry is a `PivotConditionalFormat` that answers two questions independently:
- **Where does the rule apply?** The target region is defined either through `applyTo(int row, int column, PivotConditionFormatScopeType scope)`, which mirrors the scope picker of the Excel user interface, or through `addCellArea(CellArea)` and the `getPivotAreas()` collection, which name the region explicitly.
- **What does the rule test?** One or more conditions are added to `getFormatConditions()` with `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, and each condition carries its own `getStyle()`.

{{% alert color="primary" %}}
Do not call `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` or `FormatConditionCollection.addArea(CellArea)` on the `getFormatConditions()` object of a pivot conditional format. These two overloads are inherited from the ordinary worksheet conditional-formatting API and do not work for pivot tables - the cell area is never converted to a pivot area, so the request is silently ignored. Always define the region on the `PivotConditionalFormat` itself (`applyTo`, `addCellArea`, or `getPivotAreas()`) and add the rule with one of the `addCondition` overloads.
{{% /alert %}}

## **Apply a Rule with a Scope (the Excel UI Way)**
The first way positions the rule the way the Excel user interface does. A cell of the pivot table is named by its zero-based worksheet coordinates, and a `PivotConditionFormatScopeType` scope tells Aspose.Cells how far the rule should reach from that cell:
- `PivotConditionFormatScopeType.DATA` - all value cells that the pivot table produces, including grand totals.
- `PivotConditionFormatScopeType.FIELD` - the value cells that belong to the field the cell identifies, excluding grand totals. The cell must be a field cell such as a row-field label; passing a value cell throws an exception.
- `PivotConditionFormatScopeType.SELECTION` - only the value cells at the intersection that the cell selects, typically a single value cell.
The example below builds a fruit-sales pivot table whose top-left corner is at E3, anchors a conditional format at cell F4 (row 3, column 5) with the `DATA` scope, and highlights every amount greater than 200 in bold white on red. With the values Apple 220, Banana 330, Cherry 200, and the grand total 750, the rule paints F4, F5, and F7 - the resolved region is the whole data column F4:F7, and only the cells whose value passes the rule light up.

```javascript
const AsposeCells = require("aspose.cells");
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
// Pivot table with its top-left corner at E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Anchor the conditional format at F4 (row 3, column 5) with the Data scope
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, AsposeCells.PivotConditionFormatScopeType.DATA);
// Rule - highlight amounts greater than 200
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.GREATER_THAN,
    "200",
    null
);
const style = workbook.createStyle();
style.getFont().setBold(true);
style.getFont().setColor(AsposeCells.Color.getWhite());
style.setForegroundColor(AsposeCells.Color.getRed());
style.setPattern(AsposeCells.BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

Anchoring the same rule at the row-field label E4 (row 3, column 4) with the `FIELD` scope resolves to F4:F6 instead - the same data column without the grand-total row - because the scope now describes the `Fruit` field rather than the whole values area. The `SELECTION` scope anchored at F4 resolves to F4 alone.

## **Define the Region Manually**
The second way skips the scope picker and names the region explicitly on the `PivotConditionalFormat`.

### **A worksheet rectangle with addCellArea**
`addCellArea(CellArea)` records the given rectangle as the target of the rule. The coordinates are zero-based worksheet coordinates, and the region is exactly the rectangle supplied - no expansion to the data column and no grand-total logic. Use it when the interesting cells are a known fixed rectangle of the current pivot layout.

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Target the rectangle F4:F6 (the value cells without the grand total)
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const cellArea = new AsposeCells.CellArea();
cellArea.StartRow = 3;
cellArea.StartColumn = 5;
cellArea.EndRow = 5;
cellArea.EndColumn = 5;
format.addCellArea(cellArea);
// Rule - italic on light yellow for amounts between 150 and 300
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.BETWEEN,
    "150",
    "300"
);
const style = workbook.createStyle();
style.getFont().setItalic(true);
style.setForegroundColor(AsposeCells.Color.fromArgb(0xFF, 255, 255, 224));
style.setPattern(AsposeCells.BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **A semantic pivot region with PivotAreas**
`getPivotAreas()` is the same semantic-region model that the sibling page uses for static styles. Build a `PivotArea`, select a field or region with `select` or `selectField`, and add it with `getPivotAreas().addPivotArea(PivotArea)`. A semantic region stays attached to its field, so the conditional format follows the field when the pivot table is refreshed and the layout shifts. The `getPivotAreas().add(PivotArea)` overload still compiles but is marked obsolete - prefer `addPivotArea`.

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Attach the rule to the Amount data field as a semantic region
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.PivotArea(pivotTable);
area.selectField(AsposeCells.PivotFieldType.DATA, "Amount");
format.getPivotAreas().addPivotArea(area);
// Rule - grey text for amounts below 150
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CELL_VALUE,
    AsposeCells.OperatorType.LESS_THAN,
    "150",
    null
);
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.getGray());
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **Where the Rules Are Stored and How They Survive a Reload**
Every `add()` call on `getConditionalFormats()` appends one `PivotConditionalFormat` to the pivot table. The conditions, their formulas, and their styles are saved with the workbook - reopening the file in the example below shows the same rule with its type, operator, and formula intact, and `getCellAreas()` reports the same regions. Entries that never received a condition are dropped when the workbook is saved, the same way Excel discards a conditional format that has no rule.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("PivotConditionalFormatData.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const conditionalFormats = pivotTable.getConditionalFormats();
console.log("Conditional formats: " + conditionalFormats.getCount());
for (let i = 0; i < conditionalFormats.getCount(); i++) {
    const format = conditionalFormats.get(i);
    const formatConditions = format.getFormatConditions();
    for (let j = 0; j < formatConditions.getCount(); j++) {
        const condition = formatConditions.get(j);
        console.log(`Format ${i}: ${condition.getType()} ${condition.getOperator()} formula1=${condition.getFormula1()}`);
    }
    const cellAreas = format.getCellAreas();
    for (let k = 0; k < cellAreas.length; k++) {
        const area = cellAreas[k];
        console.log(`    rows ${area.StartRow + 1}-${area.EndRow + 1}, columns ${area.StartColumn + 1}-${area.EndColumn + 1}`);
    }
}
// This prints:
// Conditional formats: 1
// Format 0: CellValue GreaterThan formula1==200
//     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
```

## **Related Articles**
- [Applying Style to Pivot Table](/cells/nodejs-java/apply-style-to-pivot-table/)
- [Format Part of a Pivot Table](/cells/nodejs-java/format-part-of-pivot-table/)
- [Top 10 Show or Filter in Pivot Table](/cells/nodejs-java/top-10-show-or-filter-in-pivot-table/)
- [Filtering Pivot Tables by Label or Value](/cells/nodejs-java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}