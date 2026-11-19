---
title: 向数据透视表添加条件格式
linktitle: 向数据透视表添加条件格式
description: 在 Aspose.Cells for Node.js via C++ 中为数据透视表添加条件格式 - 使用 applyTo 和 PivotConditionFormatScopeType 范围将规则锚定到数据区域，或使用 addCellArea 和 pivotAreas 定义目标，然后通过 formatConditions.addCondition 附加规则和样式。
keywords: Aspose.Cells for Node.js via C++, 数据透视表, 条件格式, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Node.js via C++
type: docs
weight: 30
url: /zh/nodejs-cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
父页面和兄弟页面中描述的样式是静态的——`PivotArea` 或 `CellArea` 区域仅被绘制一次，无论数值如何都保持其样式。条件格式是基于规则的对应方式——突出显示所有大于 200 的数额、为中间五十百分比着色或标记排名靠后的项目——并且在数据透视表重新计算或刷新时，突出显示会随数值变化而更新。
在 Aspose.Cells 中，数据透视表的条件格式位于 `pivotTable.getConditionalFormats()` 集合中。每个条目都是 `PivotConditionalFormat`，独立地回答两个问题：
- **规则适用范围是哪里？** 目标区域可以通过 `applyTo(row, column, scope)` 定义，它对应 Excel 用户界面的范围选择器，或者通过 `addCellArea(cellArea)` 以及 `pivotConditionalFormat.getPivotAreas()` 集合显式命名区域。
- **规则测试的内容是什么？** 通过 `pivotConditionalFormat.getFormatConditions()` 获取的 `formatConditions` 中可以添加一个或多个条件，使用 `formatConditions.addCondition(FormatConditionType type, OperatorType operatorType, string formula1, string formula2)`，并且每个条件通过 `getStyle()` 携带其自己的样式。

{{% alert color="primary" %}}
不要在数据透视表条件格式的 `formatConditions` 对象上调用 `formatConditions.add(cellArea, type, operatorType, formula1, formula2)` 或 `formatConditions.addArea(cellArea)`。这两个重载继承自普通工作表的条件格式 API，无法用于数据透视表——单元格区域永远不会转换为数据透视表区域，因此请求会被静默忽略。始终在 `pivotConditionalFormat` 对象本身上定义区域（`applyTo`、`addCellArea` 或 `getPivotAreas()`），并使用 `addCondition` 的任意重载来添加规则。
{{% /alert %}}

## **使用范围（Excel UI 方式）应用规则**
第一种方式按照 Excel 用户界面的方式定位规则。数据透视表的单元格通过其零基工作表坐标命名，`PivotConditionFormatScopeType` 范围告诉 Aspose.Cells 规则应从该单元格向外扩展多远：
- `PivotConditionFormatScopeType.DATA` - 数据透视表生成的所有数值单元格，包括总计。
- `PivotConditionFormatScopeType.FIELD` - 属于该单元格所标识字段的数值单元格，排除总计。该单元格必须是字段单元格，例如行字段标签；如果传入数值单元格会抛出异常。
- `PivotConditionFormatScopeType.SELECTION` - 仅该单元格所选交叉点的数值单元格，通常是单个数值单元格。
下面的示例构建了一个以 E3 为左上角的水果销售数据透视表，在单元格 F4（第 3 行，第 5 列）处使用 `DATA` 范围锚定条件格式，并将所有大于 200 的金额以红底白字加粗高亮显示。给定数值 Apple 220、Banana 330、Cherry 200，以及总计 750，规则会对 F4、F5 和 F7 进行着色——解析后的区域为整个数据列 F4:F7，只有满足规则的单元格会被点亮。

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

将相同的规则锚定在行字段标签 E4（第 3 行，第 4 列）并使用 `FIELD` 范围，则解析为 F4:F6——相同的数据列但不包括总计行——因为此范围描述的是 `Fruit` 字段而非整个数值区域。将 `SELECTION` 范围锚定在 F4 则仅解析为 F4 本身。

## **手动定义区域**
第二种方式跳过范围选择器，直接在 `PivotConditionalFormat` 上显式命名区域。

### **使用 addCellArea 定义工作表矩形**
`addCellArea(cellArea)` 将给定的矩形记录为规则的目标区域。坐标采用零基工作表坐标，区域恰好是提供的矩形——不会扩展到数据列，也不会包含总计逻辑。适用于感兴趣的单元格是当前数据透视布局中已知的固定矩形时。

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

### **使用 getPivotAreas 定义语义数据透视区域**
`pivotConditionalFormat.getPivotAreas()` 与兄弟页面用于静态样式的语义区域模型相同。创建一个 `PivotArea`，使用 `select` 或 `selectField` 选择字段或区域，然后通过 `pivotAreas.addPivotArea(pivotArea)` 添加。语义区域保持与其字段关联，因此在数据透视表刷新或布局变化时，条件格式会随字段一起移动。`pivotAreas.add(pivotArea)` 重载仍可编译但已标记为过时——推荐使用 `addPivotArea`。

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

## **规则的存储位置及其在重新加载后如何保持**
每次调用 `conditionalFormats.add()` 都会向数据透视表追加一个 `PivotConditionalFormat`。条件、公式及样式随工作簿一起保存——在下面示例中重新打开文件时，可看到相同的规则及其类型、运算符和公式保持完整，`getCellAreas()` 也报告相同的区域。未添加任何条件的条目在保存工作簿时会被丢弃，这与 Excel 丢弃没有规则的条件格式的方式相同。

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
// Format 0: 1 2 formula1=200   (type 1 = CellValue, operator 2 = GreaterThan)
//     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
```

## **相关文档**
- [为数据透视表应用样式](/cells/zh/nodejs-cpp/apply-style-to-pivot-table/)
- [格式化数据透视表的部分](/cells/zh/nodejs-cpp/format-part-of-pivot-table/)
- [数据透视表中的前 10 项显示或筛选](/cells/zh/nodejs-cpp/top-10-show-or-filter-in-pivot-table/)
- [按标签或数值筛选数据透视表](/cells/zh/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}