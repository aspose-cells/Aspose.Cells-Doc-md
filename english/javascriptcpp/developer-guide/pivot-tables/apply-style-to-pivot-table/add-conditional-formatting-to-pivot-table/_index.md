---
title: Add Conditional Formatting to a Pivot Table
description: Add conditional formatting to a pivot table in Aspose.Cells for JavaScript via C++ - anchor a rule to the data region with applyTo and a PivotConditionFormatScopeType scope, or define the target with addCellArea and pivotAreas, then attach rules and styles through formatConditions.addCondition.
linktitle: Add Conditional Formatting to a Pivot Table
keywords: Aspose.Cells for JavaScript via C++, pivot table, conditional formatting, PivotConditionalFormat, ConditionalFormats, applyTo, PivotConditionFormatScopeType, Data, Field, Selection, addCellArea, pivotAreas, addPivotArea, formatConditions, addCondition, FormatConditionType
type: docs
weight: 30
url: /javascript-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
The styles described on the parent page and on the sibling page are static - a `PivotArea` or `CellArea` region is painted once and keeps its style no matter what the values are. Conditional formatting is the rule-driven counterpart - highlight every amount above 200, shade the middle fifty percent, or flag the bottom-ranked items - and the highlight follows the values whenever the pivot table is recalculated or refreshed.
In Aspose.Cells, pivot-table conditional formatting lives in the `pivotTable.conditionalFormats` collection. Each entry is a `PivotConditionalFormat` that answers two questions independently:
- **Where does the rule apply?** The target region is defined either through `applyTo(row, column, scope)`, which mirrors the scope picker of the Excel user interface, or through `addCellArea(cellArea)` and the `pivotAreas` collection, which name the region explicitly.
- **What does the rule test?** One or more conditions are added to `formatConditions` with `addCondition(type, operatorType, formula1, formula2)`, and each condition carries its own `style`.

{{% alert color="primary" %}}
Do not call `formatConditions.add(cellArea, type, operatorType, formula1, formula2)` or `formatConditions.addArea(cellArea)` on the `formatConditions` object of a pivot conditional format. These two overloads are inherited from the ordinary worksheet conditional-formatting API and do not work for pivot tables - the cell area is never converted to a pivot area, so the request is silently ignored. Always define the region on the `PivotConditionalFormat` itself (`applyTo`, `addCellArea`, or `pivotAreas`) and add the rule with one of the `addCondition` overloads.
{{% /alert %}}

## **Apply a Rule with a Scope (the Excel UI Way)**
The first way positions the rule the way the Excel user interface does. A cell of the pivot table is named by its zero-based worksheet coordinates, and a `PivotConditionFormatScopeType` scope tells Aspose.Cells how far the rule should reach from that cell:
- `PivotConditionFormatScopeType.Data` - all value cells that the pivot table produces, including grand totals.
- `PivotConditionFormatScopeType.Field` - the value cells that belong to the field the cell identifies, excluding grand totals. The cell must be a field cell such as a row-field label; passing a value cell throws an exception.
- `PivotConditionFormatScopeType.Selection` - only the value cells at the intersection that the cell selects, typically a single value cell.
The example below builds a fruit-sales pivot table whose top-left corner is at E3, anchors a conditional format at cell F4 (row 3, column 5) with the `Data` scope, and highlights every amount greater than 200 in bold white on red. With the values Apple 220, Banana 330, Cherry 200, and the grand total 750, the rule paints F4, F5, and F7 - the resolved region is the whole data column F4:F7, and only the cells whose value passes the rule light up.

```js
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType, PivotConditionFormatScopeType,
        FormatConditionType, OperatorType, Color, BackgroundType } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Anchor the conditional format at F4 (row 3, column 5) with the Data scope
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    format.applyTo(3, 5, PivotConditionFormatScopeType.Data);
    // Rule - highlight amounts greater than 200
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.GreaterThan, "200", null);
    const style = workbook.createStyle();
    style.font.isBold = true;
    style.font.color = Color.White;
    style.foregroundColor = Color.Red;
    style.pattern = BackgroundType.Solid;
    format.formatConditions.get(conditionIndex).style = style;
    // wb.save(SaveFormat.Xlsx) returns the file as bytes
    fs.writeFileSync("PivotConditionalFormatData.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule paints F4, F5, and F7");
    process.exit(0);
});
```

Anchoring the same rule at the row-field label E4 (row 3, column 4) with the `Field` scope resolves to F4:F6 instead - the same data column without the grand-total row - because the scope now describes the `Fruit` field rather than the whole values area. The `Selection` scope anchored at F4 resolves to F4 alone.

## **Define the Region Manually**
The second way skips the scope picker and names the region explicitly on the `PivotConditionalFormat`.

### **A worksheet rectangle with addCellArea**
`addCellArea(cellArea)` records the given rectangle as the target of the rule. The coordinates are zero-based worksheet coordinates, and the region is exactly the rectangle supplied - no expansion to the data column and no grand-total logic. Use it when the interesting cells are a known fixed rectangle of the current pivot layout.

```js
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType,
        FormatConditionType, OperatorType, Color, BackgroundType, CellArea } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Target the rectangle F4:F6 (the value cells without the grand total)
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    const area = new CellArea();
    area.startRow = 3;
    area.startColumn = 5;
    area.endRow = 5;
    area.endColumn = 5;
    format.addCellArea(area);
    // Rule - italic on light yellow for amounts between 150 and 300
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.Between, "150", "300");
    const style = workbook.createStyle();
    style.font.isItalic = true;
    style.foregroundColor = Color.LightYellow;
    style.pattern = BackgroundType.Solid;
    format.formatConditions.get(conditionIndex).style = style;
    fs.writeFileSync("PivotConditionalFormatCellArea.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule paints F4 and F6");
    process.exit(0);
});
```

### **A semantic pivot region with pivotAreas**
`pivotAreas` is the same semantic-region model that the sibling page uses for static styles. Build a `PivotArea`, select a field or region with `select` or `selectField`, and add it with `pivotAreas.addPivotArea(pivotArea)`. A semantic region stays attached to its field, so the conditional format follows the field when the pivot table is refreshed and the layout shifts. The `pivotAreas.add(pivotArea)` overload still runs but is marked obsolete - prefer `addPivotArea`.

```js
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
const { Workbook, SaveFormat, PivotFieldType, PivotArea,
        FormatConditionType, OperatorType, Color } = AsposeCells;
AsposeCells.onReady().then(() => {
    const workbook = new Workbook();
    const sheet = workbook.worksheets.get(0);
    const cells = sheet.cells;
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
    const pivotTable = sheet.pivotTables.add("=A1:C7", 2, 4);
    pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit");
    pivotTable.addFieldToArea(PivotFieldType.Data, "Amount");
    pivotTable.calculateData();
    // Attach the rule to the Amount data field as a semantic region
    const index = pivotTable.conditionalFormats.add();
    const format = pivotTable.conditionalFormats.get(index);
    const area = new PivotArea(pivotTable);
    area.selectField(PivotFieldType.Data, "Amount");
    format.pivotAreas.addPivotArea(area);
    // Rule - grey text for amounts below 150
    const conditionIndex = format.formatConditions.addCondition(
        FormatConditionType.CellValue, OperatorType.LessThan, "150", null);
    const style = workbook.createStyle();
    style.font.color = Color.Gray;
    format.formatConditions.get(conditionIndex).style = style;
    fs.writeFileSync("PivotConditionalFormatPivotArea.xlsx", workbook.save(SaveFormat.Xlsx));
    console.log("Done; the rule is attached to the Amount value cells");
    process.exit(0);
});
```

## **Where the Rules Are Stored and How They Survive a Reload**
Every `conditionalFormats.add()` call appends one `PivotConditionalFormat` to the pivot table. The conditions, their formulas, and their styles are saved with the workbook - reopening the file saved by the first example in Node shows the same rule with its type, operator, and formula intact, and `getCellAreas()` reports the same region. On this platform the `type` and `operator` properties of a condition surface as the numeric enum values. Entries that never received a condition are dropped when the workbook is saved, the same way Excel discards a conditional format that has no rule.

```js
const fs = require("fs");
const { AsposeCells } = require("aspose.cells.js");
AsposeCells.onReady().then(() => {
    // Reload the file written by the first example
    const workbook = new Workbook(new Uint8Array(fs.readFileSync("PivotConditionalFormatData.xlsx")));
    const pivotTable = workbook.worksheets.get(0).pivotTables.get(0);
    console.log("Conditional formats: " + pivotTable.conditionalFormats.count);
    for (let i = 0; i < pivotTable.conditionalFormats.count; i++) {
        const format = pivotTable.conditionalFormats.get(i);
        for (let j = 0; j < format.formatConditions.count; j++) {
            const condition = format.formatConditions.get(j);
            console.log("Format " + i + ": " + condition.type + " " + condition.operator + " formula1=" + condition.formula1);
        }
        const areas = format.getCellAreas();
        for (const area of areas)
            console.log("    rows " + (area.startRow + 1) + "-" + (area.endRow + 1) +
                        ", columns " + (area.startColumn + 1) + "-" + (area.endColumn + 1));
    }
    // This prints:
    // Conditional formats: 1
    // Format 0: 1 2 formula1==200   (type 1 = CellValue, operator 2 = GreaterThan)
    //     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
    process.exit(0);
});
```

## **Related Articles**
- [Applying Style to Pivot Table](/cells/javascript-cpp/apply-style-to-pivot-table/)
- [Format Part of a Pivot Table](/cells/javascript-cpp/format-part-of-pivot-table/)
- [Top 10 Show or Filter in Pivot Table](/cells/javascript-cpp/top-10-show-or-filter-in-pivot-table/)
- [Filtering Pivot Tables by Label or Value](/cells/javascript-cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}