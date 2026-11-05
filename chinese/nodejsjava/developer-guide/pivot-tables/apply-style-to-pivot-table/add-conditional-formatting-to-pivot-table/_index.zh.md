---
title: 向数据透视表添加条件格式
linktitle: 向数据透视表添加条件格式
description: 在 Aspose.Cells for Node.js via Java 中向数据透视表添加条件格式 - 使用 applyTo 和 PivotConditionFormatScopeType 范围将规则锚定到数据区域，或使用 addCellArea 和 getPivotAreas 定义目标，然后通过 getFormatConditions().addCondition 附加规则和样式。
keywords: Aspose.Cells, 数据透视表, 条件格式, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Node.js via Java
type: docs
weight: 30
url: /zh/nodejs-java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
父页面和兄弟页面上描述的样式是静态的——`PivotArea` 或 `CellArea` 区域只绘制一次，无论数值如何都会保持其样式。条件格式是基于规则的对应方式——突出显示所有大于 200 的金额，为中间五十百分比着色，或标记排名最低的项目——并且在数据透视表重新计算或刷新时，突出显示会随数值变化。
在 Aspose.Cells for Node.js via Java 中，数据透视表的条件格式位于 `pivotTable.getConditionalFormats()` 集合中。每个条目都是一个 `PivotConditionalFormat`，它独立回答以下两个问题：
- **规则适用于哪个区域？** 目标区域可以通过 `applyTo(int row, int column, PivotConditionFormatScopeType scope)` 定义，它对应 Excel 用户界面中的范围选择器，亦可通过 `addCellArea(CellArea)` 和 `getPivotAreas()` 集合显式命名区域。
- **规则检测什么条件？** 使用 `getFormatConditions()` 并调用 `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` 添加一个或多个条件，每个条件都有各自的 `getStyle()`。

{{% alert color="primary" %}}
不要在数据透视条件格式的 `getFormatConditions()` 对象上调用 `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` 或 `FormatConditionCollection.addArea(CellArea)`。这两个重载继承自普通工作表条件格式 API，无法用于数据透视表——单元格区域永远不会转换为数据透视区域，请求会被静默忽略。请始终在 `PivotConditionalFormat` 本身上定义区域（`applyTo`、`addCellArea` 或 `getPivotAreas()`），并使用 `addCondition` 系列的重载添加规则。
{{% /alert %}}

## **使用范围应用规则（Excel UI 方式）**
第一种方式按照 Excel 用户界面的方式定位规则。数据透视表的单元格以其基于零的工作表坐标命名，`PivotConditionFormatScopeType` 范围告诉 Aspose.Cells 规则应从该单元格扩展多大范围：
- `PivotConditionFormatScopeType.DATA` - 所有数据透视表生成的数值单元格，包括总计。
- `PivotConditionFormatScopeType.FIELD` - 属于该单元格标识的字段的数值单元格，不包括总计。单元格必须是字段单元格（例如行字段标签）；如果传入数值单元格会抛出异常。
- `PivotConditionFormatScopeType.SELECTION` - 仅限该单元格选中的交叉处的数值单元格，通常只有单个数值单元格。
下面的示例创建了一个水果销量数据透视表，左上角位于 E3，在单元格 F4（第 3 行，第 5 列）使用 `DATA` 范围锚定条件格式，并将所有大于 200 的金额以粗体白字红底高亮。对于 Apple 220、Banana 330、Cherry 200 以及总计 750，规则会为 F4、F5、F7 着色——解析后的区域是整列数据 F4:F7，只有满足条件的单元格会点亮。

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

将相同规则锚定在行字段标签 E4（第 3 行，第 4 列）并使用 `FIELD` 范围时，解析区域为 F4:F6——同一数据列但不包含总计行，因为此时范围描述的是 `Fruit` 字段而不是整个数值区域。`SELECTION` 范围锚定在 F4 时，仅解析为 F4 本身。

## **手动定义区域**
第二种方式跳过范围选择器，直接在 `PivotConditionalFormat` 上显式命名区域。

### **使用 addCellArea 定义工作表矩形**
`addCellArea(CellArea)` 将给定的矩形记录为规则的目标。坐标采用基于零的工作表坐标，区域正好是提供的矩形——不会扩展到数据列，也不会进行总计逻辑。当感兴趣的单元格是当前数据透视布局中已知的固定矩形时使用此方式。

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

### **使用 PivotAreas 定义语义数据透视区域**
`getPivotAreas()` 与兄弟页面用于静态样式的语义区域模型相同。创建 `PivotArea`，使用 `select` 或 `selectField` 选择字段或区域，然后通过 `getPivotAreas().addPivotArea(PivotArea)` 添加。语义区域会附着在其字段上，因而在数据透视表刷新且布局改变时，条件格式会随字段移动。`getPivotAreas().add(PivotArea)` 重载仍可编译，但已标记为过时——推荐使用 `addPivotArea`。

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

## **规则的存储位置及其在重新加载后的保持方式**
对 `getConditionalFormats()` 的每一次 `add()` 调用都会向数据透视表追加一个 `PivotConditionalFormat`。条件、公式以及样式随工作簿一起保存——在下面示例中重新打开文件时，可看到相同的规则以及它们的类型、运算符和公式保持不变，`getCellAreas()` 也报告相同的区域。未收到任何条件的条目在保存工作簿时会被删除，这与 Excel 丢弃没有规则的条件格式的行为相同。

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

## **相关文档**
- [向数据透视表应用样式](/cells/zh/nodejs-java/apply-style-to-pivot-table/)
- [格式化数据透视表的部分](/cells/zh/nodejs-java/format-part-of-pivot-table/)
- [数据透视表的前 10 显示或筛选](/cells/zh/nodejs-java/top-10-show-or-filter-in-pivot-table/)
- [按标签或数值筛选数据透视表](/cells/zh/nodejs-java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}