---
title: 添加条件格式到数据透视表
linktitle: 添加条件格式到数据透视表
description: 在 Aspose.Cells for Java 中向数据透视表添加条件格式 - 使用 applyTo 和 PivotConditionFormatScopeType 作用域将规则锚定到数据区域，或使用 addCellArea 和 getPivotAreas 定义目标，然后通过 FormatConditions.addCondition 附加规则和样式
keywords: Aspose.Cells for Java, 数据透视表, 条件格式, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Java
type: docs
weight: 30
url: /zh/java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
父页面和兄弟页面中描述的样式是静态的——`PivotArea` 或 `CellArea` 区域只会被绘制一次，无论数值如何都会保持其样式。条件格式是基于规则的对应方式——突出显示所有大于 200 的数额、给中间五十百分比着色，或标记排名靠后的项目——且在数据透视表重新计算或刷新时，突出显示会随数值变化而更新。
在 Aspose.Cells 中，数据透视表的条件格式位于 `PivotTable.getConditionalFormats()` 集合中。每个条目都是 `PivotConditionalFormat`，它独立地回答两个问题：
- **规则适用范围？** 目标区域可以通过 `applyTo(int row, int column, PivotConditionFormatScopeType scope)` 定义，这与 Excel 用户界面的作用域选择器相对应；也可以通过 `addCellArea(CellArea)` 和 `getPivotAreas()` 集合显式命名区域。
- **规则检测什么？** 使用 `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` 向 `getFormatConditions()` 添加一个或多个条件，每个条件都有其自己的 `Style`。

{{% alert color="primary" %}}
不要在数据透视表条件格式的 `getFormatConditions()` 集合上调用 `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` 或 `FormatConditionCollection.addArea(CellArea)`。这两个重载来自普通工作表条件格式 API，无法用于数据透视表——单元格区域永远不会转换为数据透视表区域，导致请求被静默忽略。始终在 `PivotConditionalFormat` 本身上定义区域（`applyTo`、`addCellArea` 或 `getPivotAreas()`），并使用 `addCondition` 的任一重载添加规则。
{{% /alert %}}

## **使用范围应用规则（Excel UI 方式）**
第一种方式按照 Excel 用户界面的方式定位规则。数据透视表的单元格通过其从零开始的工作表坐标命名，`PivotConditionFormatScopeType` 作用域告诉 Aspose.Cells 规则应从该单元格延伸多远：
- `PivotConditionFormatScopeType.DATA` - 数据透视表生成的所有值单元格，包括总计。
- `PivotConditionFormatScopeType.FIELD` - 属于该单元格标识的字段的值单元格，排除总计。单元格必须是字段单元格，例如行字段标签；如果传入值单元格会抛出异常。
- `PivotConditionFormatScopeType.SELECTION` - 仅该单元格所选交叉处的值单元格，通常为单个值单元格。
下面的示例创建了一个以 E3 为左上角的水果销售数据透视表，在单元格 F4（第 3 行，第 5 列）使用 `DATA` 作用域锚定条件格式，并将所有大于 200 的金额以粗体白字红底突出显示。对于值 Apple 220、Banana 330、Cherry 200，以及总计 750，规则会绘制 F4、F5 和 F7 ——解析后的区域为整个数据列 F4:F7，只有满足规则的单元格会被点亮。

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
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.getPivotTables().add("A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Anchor the conditional format at F4 (row 3, column 5) with the Data scope
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, PivotConditionFormatScopeType.DATA);
// Rule - highlight amounts greater than 200
int conditionIndex = format.getFormatConditions().addCondition(
        FormatConditionType.CELL_VALUE, OperatorType.GREATER_THAN, "200", null);
Style style = workbook.createStyle();
style.getFont().setBold(true);
style.getFont().setColor(Color.getWhite());
style.setForegroundColor(Color.getRed());
style.setPattern(BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

如果将同一规则锚定在行字段标签 E4（第 3 行，第 4 列）并使用 `FIELD` 作用域，则解析结果为 F4:F6 ——同一数据列但不包括总计行，因为此范围描述的是 `Fruit` 字段而非整个值区域。将 `SELECTION` 作用域锚定在 F4 则仅解析为 F4 本身。

## **手动定义区域**
第二种方式跳过范围选择器，直接在 `PivotConditionalFormat` 上显式命名区域。

### **使用 addCellArea 定义工作表矩形**
`addCellArea(CellArea)` 将给定的矩形记录为规则的目标。坐标采用从零开始的工作表坐标，区域正好是提供的矩形——不会扩展到数据列，也没有总计逻辑。当感兴趣的单元格是当前数据透视布局中已知的固定矩形时使用它。

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
// Target the rectangle F4:F6 (the value cells without the grand total)
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
CellArea cellArea = new CellArea();
cellArea.StartRow = 3;
cellArea.StartColumn = 5;
cellArea.EndRow = 5;
cellArea.EndColumn = 5;
format.addCellArea(cellArea);
// Rule - italic on light yellow for amounts between 150 and 300
int conditionIndex = format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE, OperatorType.BETWEEN, "150", "300");
Style style = workbook.createStyle();
style.getFont().setItalic(true);
style.setForegroundColor(Color.getLightYellow());
style.setPattern(BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **使用 getPivotAreas 定义语义数据透视区域**
`getPivotAreas()` 返回与兄弟页面用于静态样式相同的语义区域模型。构建一个 `PivotArea`，使用 `select` 或 `selectField` 选择字段或区域，然后通过 `getPivotAreas().addPivotArea(PivotArea)` 添加。语义区域会附着在其字段上，因此在数据透视表刷新且布局变动时，条件格式会随字段移动。`getPivotAreas().add(PivotArea)` 重载仍能编译，但已标记为过时——推荐使用 `addPivotArea`。

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
// Attach the rule to the Amount data field as a semantic region
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
PivotArea area = new PivotArea(pivotTable);
area.selectField(PivotFieldType.DATA, "Amount");
format.getPivotAreas().addPivotArea(area);
// Rule - grey text for amounts below 150
int conditionIndex = format.getFormatConditions().addCondition(
        FormatConditionType.CELL_VALUE, OperatorType.LESS_THAN, "150", null);
Style style = workbook.createStyle();
style.getFont().setColor(Color.getGray());
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **规则的存储位置及其在重新加载时的持久性**
每次调用 `getConditionalFormats().add()` 都会向数据透视表追加一个 `PivotConditionalFormat`。条件、其公式以及样式会随工作簿一起保存——在下面示例中重新打开文件时，仍能看到相同的规则及其类型、运算符和公式保持完整，`getCellAreas()` 也报告相同的区域。未获得任何条件的条目在保存工作簿时会被删除，这与 Excel 丢弃没有规则的条件格式的方式相同。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("PivotConditionalFormatData.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
System.out.println("Conditional formats: " + pivotTable.getConditionalFormats().getCount());
for (int i = 0; i < pivotTable.getConditionalFormats().getCount(); i++)
{
    PivotConditionalFormat format = pivotTable.getConditionalFormats().get(i);
    for (int j = 0; j < format.getFormatConditions().getCount(); j++)
    {
        FormatCondition condition = format.getFormatConditions().get(j);
        System.out.println("Format " + i + ": " + condition.getType() + " " + condition.getOperator() + " formula1=" + condition.getFormula1());
    }
    for (CellArea area : format.getCellAreas())
    {
        System.out.println("    rows " + (area.StartRow + 1) + "-" + (area.EndRow + 1)
                + ", columns " + (area.StartColumn + 1) + "-" + (area.EndColumn + 1));
    }
}
// This prints:
// Conditional formats: 1
// Format 0: CellValue GreaterThan formula1==200
//     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
```

## **Related Articles**
- [在数据透视表中应用样式](/cells/zh/java/apply-style-to-pivot-table/)
- [格式化数据透视表的部分](/cells/zh/java/format-part-of-pivot-table/)
- [数据透视表的前10名显示或筛选](/cells/zh/java/top-10-show-or-filter-in-pivot-table/)
- [按标签或数值筛选数据透视表](/cells/zh/java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="java" >}}