---
title: 向数据透视表添加条件格式
linktitle: 向数据透视表添加条件格式
description: 在 Aspose.Cells for .NET 中向数据透视表添加条件格式 —— 使用 ApplyTo 和 PivotConditionFormatScopeType 作用域将规则锚定到数据区域，或使用 AddCellArea 和 PivotAreas 定义目标，然后通过 FormatConditions.AddCondition 附加规则和样式。
keywords: Aspose.Cells, 数据透视表, 条件格式, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, 数据, 字段, 选取, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C#
type: docs
weight: 30
url: /zh/net/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
父页面和兄弟页面中描述的样式是静态的——`PivotArea` 或 `CellArea` 区域仅绘制一次，无论数值如何都会保持其样式。条件格式是规则驱动的对应方式——突出显示所有大于 200 的金额、为中间 50% 的数据着色，或标记排名靠后的项目——并且在数据透视表重新计算或刷新时，突出显示会随数值变化而更新。  
在 Aspose.Cells 中，数据透视表的条件格式位于 `PivotTable.ConditionalFormats` 集合中。每个条目都是一个 `PivotConditionalFormat`，它独立回答以下两个问题：
- **规则适用于哪里？** 目标区域可以通过 `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)` 定义，该方法映射了 Excel 用户界面中的作用域选择器；或者通过 `AddCellArea(CellArea)` 以及 `PivotAreas` 集合显式命名区域。
- **规则测试什么？** 使用 `FormatConditions` 的 `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, string formula1, string formula2)` 添加一个或多个条件，每个条件携带自己的 `Style`。

{{% alert color="primary" %}}
不要在数据透视表条件格式的 `FormatConditions` 对象上调用 `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, string formula1, string formula2)` 或 `FormatConditionCollection.AddArea(CellArea)`。这两个重载来自普通工作表的条件格式 API，不能用于数据透视表——单元格区域永远不会转换为数据透视表区域，请求会被静默忽略。请始终在 `PivotConditionalFormat` 本身上定义区域（`ApplyTo`、`AddCellArea` 或 `PivotAreas`），并使用 `AddCondition` 的任意重载添加规则。
{{% /alert %}}

## **使用作用域应用规则（Excel UI 方式）**
第一种方式与 Excel 用户界面的操作方式相同。数据透视表的单元格以零基工作表坐标命名，`PivotConditionFormatScopeType` 作用域告诉 Aspose.Cells 规则应从该单元格向外扩展的区域：
- `PivotConditionFormatScopeType.Data` —— 数据透视表生成的所有值单元格，包括总计。
- `PivotConditionFormatScopeType.Field` —— 属于该单元格标识字段的值单元格，不包括总计。该单元格必须是字段单元格（例如行字段标签），传入值单元格会抛出异常。
- `PivotConditionFormatScopeType.Selection` —— 仅该单元格选中的交叉处的值单元格，通常为单个值单元格。
下面的示例构建了一个水果销售数据透视表，左上角位于 E3，在单元格 F4（第 3 行，第 5 列）使用 `Data` 作用域锚定条件格式，并将所有大于 200 的金额以白字红底加粗显示。给定 Apple 220、Banana 330、Cherry 200 和总计 750，规则会为 F4、F5、F7 着色——实际解析的区域是整个数据列 F4:F7，只有满足条件的单元格会被点亮。

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Anchor the conditional format at F4 (row 3, column 5) with the Data scope
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
format.ApplyTo(3, 5, PivotConditionFormatScopeType.Data);
// Rule - highlight amounts greater than 200
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.GreaterThan, "200", null);
Style style = workbook.CreateStyle();
style.Font.IsBold = true;
style.Font.Color = Color.White;
style.ForegroundColor = Color.Red;
style.Pattern = BackgroundType.Solid;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatData.xlsx");
```

将相同规则锚定在行字段标签 E4（第 3 行，第 4 列）并使用 `Field` 作用域时，解析区域为 F4:F6——同一数据列但不包括总计行，因为此时作用域描述的是 `Fruit` 字段而非整个值区域。`Selection` 作用域锚定在 F4 时，仅解析为 F4 本身。

## **手动定义区域**
第二种方式跳过作用域选择器，直接在 `PivotConditionalFormat` 上显式命名区域。

### **使用 AddCellArea 定义工作表矩形**
`AddCellArea(CellArea)` 将给定的矩形记录为规则的目标。坐标使用零基工作表坐标，区域恰好是提供的矩形——没有扩展到数据列，也没有总计逻辑。当感兴趣的单元格是当前数据透视表布局中已知的固定矩形时使用此方式。

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Target the rectangle F4:F6 (the value cells without the grand total)
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
format.AddCellArea(new CellArea { StartRow = 3, StartColumn = 5, EndRow = 5, EndColumn = 5 });
// Rule - italic on light yellow for amounts between 150 and 300
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.Between, "150", "300");
Style style = workbook.CreateStyle();
style.Font.IsItalic = true;
style.ForegroundColor = Color.LightYellow;
style.Pattern = BackgroundType.Solid;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatCellArea.xlsx");
```

### **使用 PivotAreas 定义语义数据透视区域**
`PivotAreas` 与兄弟页面用于静态样式的语义区域模型相同。创建 `PivotArea`，使用 `Select` 或 `SelectField` 选取字段或区域，然后通过 `PivotAreas.AddPivotArea(PivotArea)` 添加。语义区域会随其字段保持绑定，因此在数据透视表刷新并且布局变化时，条件格式会随字段一起移动。`PivotAreas.Add(PivotArea)` 重载仍然可以编译，但已标记为过时——请使用 `AddPivotArea`。

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Attach the rule to the Amount data field as a semantic region
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
PivotArea area = new PivotArea(pivotTable);
area.SelectField(PivotFieldType.Data, "Amount");
format.PivotAreas.AddPivotArea(area);
// Rule - grey text for amounts below 150
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.LessThan, "150", null);
Style style = workbook.CreateStyle();
style.Font.Color = Color.Gray;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatPivotArea.xlsx");
```

## **规则的存储位置及其在重新加载后的持久性**
每次调用 `ConditionalFormats.Add()` 都会向数据透视表追加一个 `PivotConditionalFormat`。条件、其公式以及样式会随工作簿一起保存——下面示例中重新打开文件后，仍然可以看到规则及其类型、运算符和公式完整无缺，`GetCellAreas()` 也会返回相同的区域。未曾添加任何条件的条目在工作簿保存时会被删除，这与 Excel 在没有规则的情况下丢弃条件格式的行为一致。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("PivotConditionalFormatData.xlsx");
PivotTable pivotTable = workbook.Worksheets[0].PivotTables[0];
Console.WriteLine("Conditional formats: " + pivotTable.ConditionalFormats.Count);
for (int i = 0; i < pivotTable.ConditionalFormats.Count; i++)
{
    PivotConditionalFormat format = pivotTable.ConditionalFormats[i];
    for (int j = 0; j < format.FormatConditions.Count; j++)
    {
        FormatCondition condition = format.FormatConditions[j];
        Console.WriteLine($"Format {i}: {condition.Type} {condition.Operator} formula1={condition.Formula1}");
    }
    foreach (CellArea area in format.GetCellAreas())
        Console.WriteLine($"    rows {area.StartRow + 1}-{area.EndRow + 1}, columns {area.StartColumn + 1}-{area.EndColumn + 1}");
}
// This prints:
// Conditional formats: 1
// Format 0: CellValue GreaterThan formula1==200
//     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
```

## **相关文章**
- [向数据透视表应用样式](/cells/zh/net/apply-style-to-pivot-table/)
- [格式化数据透视表的部分](/cells/zh/net/format-part-of-pivot-table/)
- [在数据透视表中显示或筛选前 10](/cells/zh/net/top-10-show-or-filter-in-pivot-table/)
- [按标签或数值筛选数据透视表](/cells/zh/net/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="csharp" >}}