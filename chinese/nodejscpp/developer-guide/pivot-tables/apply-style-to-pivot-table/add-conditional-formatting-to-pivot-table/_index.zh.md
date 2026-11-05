---
title: 向数据透视表添加条件格式
linktitle: 向数据透视表添加条件格式
description: 在 Aspose.Cells for Node.js via C++ 中向数据透视表添加条件格式——使用 applyTo 和 PivotConditionFormatScopeType 范围将规则锚定到数据区域，或使用 addCellArea 和 pivotAreas 定义目标，然后通过 formatConditions.addCondition 附加规则和样式。
keywords: Aspose.Cells for Node.js via C++, 数据透视表, 条件格式, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Node.js via C++
type: docs
weight: 30
url: /zh/nodejs-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
父页面和兄弟页面中描述的样式都是静态的——`PivotArea` 或 `CellArea` 区域仅绘制一次，无论数值如何都会保持其样式。条件格式是基于规则的对应方式——高亮所有大于 200 的金额、为中间 50% 的数据着色，或标记排名最低的项——并且在透视表重新计算或刷新时，突出显示会随数值变化而更新。

{{% alert color="primary" %}}
请勿在透视条件格式的 `formatConditions` 对象上调用 `formatConditions.add(cellArea, type, operatorType, formula1, formula2)` 或 `formatConditions.addArea(cellArea)`。这两个重载来自普通工作表条件格式 API，无法用于透视表——单元格区域永远不会转换为透视区域，请求会被静默忽略。请始终在 `pivotConditionalFormat` 对象本身上定义区域（`applyTo`、`addCellArea` 或 `getPivotAreas()`），并使用 `addCondition` 系列的重载添加规则。
{{% /alert %}}

## **使用范围应用规则（Excel UI 方式）**
第一种方式按照 Excel 用户界面的方式定位规则。透视表的单元格使用基于零的工作表坐标命名，`PivotConditionFormatScopeType` 范围告诉 Aspose.Cells 规则应从该单元格延伸多远：
- `PivotConditionFormatScopeType.DATA` - 透视表生成的所有值单元格，包括总计。
- `PivotConditionFormatScopeType.FIELD` - 属于该单元格所标识字段的值单元格，不包括总计。单元格必须是字段标签（如行字段标签），传入值单元格会抛出异常。
- `PivotConditionFormatScopeType.SELECTION` - 仅选中的交叉点值单元格，通常为单个值单元格。
下面的示例创建一个以 E3 为左上角的水果销售透视表，在单元格 F4（第 3 行，第 5 列）以 `DATA` 范围锚定条件格式，并将所有大于 200 的金额以红底白字加粗方式高亮。示例数据为 Apple 220、Banana 330、Cherry 200，以及总计 750，规则会为 F4、F5、F7 着色——解析后的区域为整列数据 F4:F7，只有满足条件的单元格会点亮。

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
// Pivot table with its top-left corner at E3
const pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Anchor the conditional format at F4 (row 3, column 5) with the Data scope
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, AsposeCells.PivotConditionFormatScopeType.Data);
// Rule - highlight amounts greater than 200
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.GreaterThan,
    "200",
    null
);
const style = workbook.createStyle();
style.getFont().setIsBold(true);
style.getFont().setColor(AsposeCells.Color.White);
style.setForegroundColor(AsposeCells.Color.Red);
style.setPattern(AsposeCells.BackgroundType.Solid);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

将同一规则锚定在行字段标签 E4（第 3 行，第 4 列）并使用 `FIELD` 范围时，解析结果为 F4:F6——即相同的数据列但不包含总计行，因为此时范围描述的是 `Fruit` 字段而非整个值区域。使用 `SELECTION` 范围锚定在 F4 时，仅解析为 F4 本身。

## **手动定义区域**
第二种方式不使用范围选择器，而是直接在 `PivotConditionalFormat` 上显式命名区域。

### **使用 addCellArea 定义工作表矩形**
`addCellArea(cellArea)` 将给定的矩形记录为规则的目标。坐标采用基于零的工作表坐标，区域恰好等于提供的矩形——不会自动扩展到数据列，也没有总计逻辑。适用于感兴趣的单元格已知为当前透视布局的固定矩形的情况。

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
// Target the rectangle F4:F6 (the value cells without the grand total)
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.CellArea();
area.startRow = 3;
area.startColumn = 5;
area.endRow = 5;
area.endColumn = 5;
format.addCellArea(area);
// Rule - italic on light yellow for amounts between 150 and 300
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.Between,
    "150",
    "300"
);
const style = workbook.createStyle();
style.getFont().setIsItalic(true);
style.setForegroundColor(AsposeCells.Color.LightYellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **使用 getPivotAreas 定义语义透视区域**
`pivotConditionalFormat.getPivotAreas()` 使用与兄弟页面静态样式相同的语义区域模型。构建 `PivotArea`，通过 `select` 或 `selectField` 选择字段或区域，然后使用 `pivotAreas.addPivotArea(pivotArea)` 添加。语义区域会随其所属字段绑定，当透视表刷新且布局变化时，条件格式会随字段移动。`pivotAreas.add(pivotArea)` 重载仍可编译但已标记为过时——推荐使用 `addPivotArea`。

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
// Attach the rule to the Amount data field as a semantic region
const index = pivotTable.getConditionalFormats().add();
const format = pivotTable.getConditionalFormats().get(index);
const area = new AsposeCells.PivotArea(pivotTable);
area.selectField(AsposeCells.PivotFieldType.Data, "Amount");
format.getPivotAreas().addPivotArea(area);
// Rule - grey text for amounts below 150
const conditionIndex = format.getFormatConditions().addCondition(
    AsposeCells.FormatConditionType.CellValue,
    AsposeCells.OperatorType.LessThan,
    "150",
    null
);
const style = workbook.createStyle();
style.getFont().setColor(AsposeCells.Color.Gray);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **规则存储位置及重新加载后的持久化**
每次调用 `conditionalFormats.add()` 都会向透视表追加一个 `PivotConditionalFormat`。条件、公式以及样式会随工作簿一起保存——在下面的示例中重新打开文件后，仍能看到相同的规则及其类型、运算符和公式，`getCellAreas()` 也会返回相同的区域。未为 `PivotConditionalFormat` 添加任何条件的条目在工作簿保存时会被删除，这与 Excel 丢弃没有规则的条件格式的行为一致。

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("PivotConditionalFormatData.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
console.log("Conditional formats: " + pivotTable.getConditionalFormats().getCount());
for (let i = 0; i < pivotTable.getConditionalFormats().getCount(); i++) {
    const format = pivotTable.getConditionalFormats().get(i);
    for (let j = 0; j < format.getFormatConditions().getCount(); j++) {
        const condition = format.getFormatConditions().get(j);
        console.log(`Format ${i}: ${condition.getType()} ${condition.getOperator()} formula1=${condition.getFormula1()}`);
    }
    for (const area of format.getCellAreas()) {
        console.log(`    rows ${area.startRow + 1}-${area.endRow + 1}, columns ${area.startColumn + 1}-${area.endColumn + 1}`);
    }
}
// This prints:
// Conditional formats: 1
// Format 0: CellValue GreaterThan formula1==200
//     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
```

## **相关文档**
- [向数据透视表应用样式](/cells/zh/nodejs-cpp/apply-style-to-pivot-table/)
- [格式化数据透视表的部分](/cells/zh/nodejs-cpp/format-part-of-pivot-table/)
- [数据透视表的前 10 项显示或筛选](/cells/zh/nodejs-cpp/top-10-show-or-filter-in-pivot-table/)
- [按标签或数值筛选数据透视表](/cells/zh/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}