---
title: 向数据透视表添加条件格式
linktitle: 向数据透视表添加条件格式
description: 在 Aspose.Cells for JavaScript via C++ 中向数据透视表添加条件格式 — 使用 applyTo 和 PivotConditionFormatScopeType 范围将规则锚定到数据区域，或使用 addCellArea 和 pivotAreas 定义目标，然后通过 formatConditions.addCondition 附加规则和样式。
keywords: Aspose.Cells for JavaScript via C++, 数据透视表, 条件格式, PivotConditionalFormat, ConditionalFormats, applyTo, PivotConditionFormatScopeType, Data, Field, Selection, addCellArea, pivotAreas, addPivotArea, formatConditions, addCondition, FormatConditionType
type: docs
weight: 30
url: /zh/javascript-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
父页面和兄弟页面中描述的样式是静态的——`PivotArea` 或 `CellArea` 区域只会被绘制一次，无论数值如何都会保持其样式。条件格式是规则驱动的对应方式——突出显示所有大于 200 的金额，对中间 50% 的数据进行着色，或标记排名最低的项目——并且当数据透视表重新计算或刷新时，突出显示会随数值自动更新。
在 Aspose.Cells 中，数据透视表的条件格式位于 `pivotTable.conditionalFormats` 集合中。每个条目都是一个 `PivotConditionalFormat`，它独立地回答以下两个问题：
- **规则应用于哪里？**  
  目标区域可以通过 `applyTo(row, column, scope)` 定义，它对应 Excel 用户界面的范围选择器；也可以通过 `addCellArea(cellArea)` 以及 `pivotAreas` 集合显式命名区域。
- **规则测试什么？**  
  使用 `addCondition(type, operatorType, formula1, formula2)` 向 `formatConditions` 添加一个或多个条件，每个条件都携带其各自的 `style`。

{{% alert color="primary" %}}
不要在 `PivotConditionalFormat` 的 `formatConditions` 对象上调用 `formatConditions.add(cellArea, type, operatorType, formula1, formula2)` 或 `formatConditions.addArea(cellArea)`。这两个重载来自普通工作表的条件格式 API，不能用于数据透视表——单元格区域永远不会转换为透视区域，请求将被静默忽略。始终在 `PivotConditionalFormat` 本身上定义区域（`applyTo`、`addCellArea` 或 `pivotAreas`），并使用 `addCondition` 的任意重载来添加规则。
{{% /alert %}}

## **使用范围应用规则（Excel UI 方式）**
第一种方式按照 Excel 用户界面的方式定位规则。数据透视表的单元格使用其零基工作表坐标命名，`PivotConditionFormatScopeType` 范围告诉 Aspose.Cells 规则应从该单元格延伸多远：
- `PivotConditionFormatScopeType.Data` - 数据透视表生成的所有数值单元格，包括总计。
- `PivotConditionFormatScopeType.Field` - 属于该单元格所标识字段的数值单元格，不包括总计。该单元格必须是字段单元格（例如行字段标签），传入数值单元格会抛出异常。
- `PivotConditionFormatScopeType.Selection` - 仅该单元格所选交叉处的数值单元格，通常是单个数值单元格。
下面的示例构建了一个水果销售数据透视表，左上角位于 E3，使用 `Data` 范围在单元格 F4（第 3 行，第 5 列）锚定条件格式，并将所有大于 200 的金额以红底白字加粗显示。给定 Apple 220、Banana 330、Cherry 200，以及总计 750，规则会为 F4、F5、F7 着色——解析后的区域是整个数据列 F4:F7，只有满足规则的单元格会被点亮。

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

如果在行字段标签 E4（第 3 行，第 4 列）使用 `Field` 范围锚定相同的规则，则解析结果为 F4:F6——同一数据列但不包括总计行——因为此范围描述的是 `Fruit` 字段而非整个数值区域。将 `Selection` 范围锚定在 F4 则仅解析为 F4 本身。

## **手动定义区域**
第二种方式跳过范围选择器，直接在 `PivotConditionalFormat` 上显式命名区域。

### **使用 addCellArea 定义工作表矩形**
`addCellArea(cellArea)` 将给定的矩形记录为规则的目标区域。坐标使用零基工作表坐标，区域恰好为提供的矩形——不会扩展到数据列，也不会包含总计逻辑。当感兴趣的单元格是当前数据透视布局的已知固定矩形时使用此方式。

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

### **使用 pivotAreas 定义语义透视区域**
`pivotAreas` 与兄弟页面用于静态样式的语义区域模型相同。创建一个 `PivotArea`，使用 `select` 或 `selectField` 选择字段或区域，然后通过 `pivotAreas.addPivotArea(pivotArea)` 添加。语义区域会关联到其字段，因此当数据透视表刷新或布局变化时，条件格式会随字段移动。`pivotAreas.add(pivotArea)` 重载仍可运行，但已标记为过时——建议使用 `addPivotArea`。

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

## **规则存储位置及重新加载后的持久性**
每次调用 `conditionalFormats.add()` 都会向数据透视表追加一个 `PivotConditionalFormat`。条件、其公式以及样式随工作簿一起保存——在 Node 中重新打开第一个示例保存的文件时，可看到相同的规则以及其类型、运算符和公式保持完整，`getCellAreas()` 也返回相同的区域。在此平台上，条件的 `type` 和 `operator` 属性以数值枚举形式呈现。未设置任何条件的条目在保存工作簿时会被删除，行为与 Excel 对没有规则的条件格式的舍弃相同。

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
- [向数据透视表应用样式](/cells/zh/javascript-cpp/apply-style-to-pivot-table/)
- [格式化数据透视表的部分区域](/cells/zh/javascript-cpp/format-part-of-pivot-table/)
- [在数据透视表中显示或筛选前 10 项](/cells/zh/javascript-cpp/top-10-show-or-filter-in-pivot-table/)
- [按标签或数值筛选数据透视表](/cells/zh/javascript-cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}