---
title: 格式化数据透视表的部分
linktitle: 格式化数据透视表的部分
description: 在 Aspose.Cells for .NET 中，通过 PivotTable.Format 将样式应用于语义 PivotArea 区域或 CellArea 矩形，以对数据透视表的部分进行格式化，格式会存储在 PivotTable.PivotFormats 中，并在刷新数据透视表时保持不变。
keywords: Aspose.Cells, 数据透视表, 格式化, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C#
type: docs
weight: 20
url: /zh/net/format-part-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
`PivotTable.FormatAll` 对整个数据透视表应用单一样式，相关内容已在父页面说明。它不会区分标签、数值、合计或报表的特定区域。  
实际上，通常只需要突出显示数据透视表的一部分。常见的目标包括属于某行字段的标签、某字段生成的数值单元格、总计行，或诸如前两行项目的任意矩形区域。  
将样式直接应用于数据透视表所在工作表的单元格并不等价。Excel 将数据透视表的格式存储为语义 `PivotArea` 区域，而非普通单元格样式记录。PivotArea 格式会附着在诸如字段标签或数据值的区域上，并在数据透视表重新计算、刷新或展开时重新解析。相反，直接写入单元格的样式只属于该单元格位置，未被数据透视表模型跟踪。  
Aspose.Cells 提供完整的 `PivotTable.Format` 重载系列，以支持上述两种格式化方式：
- `Format(PivotArea, Style)` 将样式锚定到使用 `PivotArea.Select` 或 `PivotArea.SelectField` 构建的语义区域。
- `Format(CellArea, Style)` 将样式锚定到数据透视表内部的工作表矩形。
- `Format(int row, int column, Style)` 目标为单个单元格。
- `FormatAll(Style)` 格式化整个数据透视表。

## **格式化 PivotArea**
当需要让突出显示随字段或报表区域保持一致时，推荐使用语义区域的工作流。  
1. 使用 `new PivotArea(pivotTable)` 创建 `PivotArea`。该对象描述了属于该特定数据透视表的语义区域。  
2. 使用 `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)` 按给定轴上基于零起始位置的索引选择字段。  
   - `PivotTableSelectionType.DataAndLabel` 同时选择该字段的标签和数据。  
   - `PivotTableSelectionType.LabelOnly` 仅选择该字段的标签。  
   - `PivotTableSelectionType.DataOnly` 仅选择该字段的数据单元格。  
3. 使用 `PivotArea.SelectField(PivotFieldType axisType, string fieldName)` 按名称选择字段。当按名称选择行字段时，区域会解析为该字段各项生成的数值单元格。  
4. 使用 `Workbook.CreateStyle()` 创建 `Style`，配置其字体、前景色和实线填充模式，然后将该样式传递给 `PivotTable.Format(area, style)`。  
5. 每次调用 `PivotArea` 重载都会向 `PivotTable.PivotFormats` 添加一条 `PivotTableFormat` 条目。  
6. 字段锚定的格式会在计算数据透视表时绘制。因此，在应用格式后调用 `PivotTable.CalculateData()`，使样式可见。  
下面示例创建了一个小型水果销售数据透视表，使用 `PivotArea.Select` 与 `PivotTableSelectionType.LabelOnly` 为 `Fruit` 行标签设置样式，使用 `PivotArea.SelectField` 为同一行字段生成的数值单元格设置样式，然后重新计算数据透视表，使两种样式均被绘制。

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
// Fruit sales data
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
// Bold yellow fill on the row field's label cells
Style labelStyle = workbook.CreateStyle();
labelStyle.Font.IsBold = true;
labelStyle.ForegroundColor = Color.Yellow;
labelStyle.Pattern = BackgroundType.Solid;
PivotArea labelArea = new PivotArea(pivotTable);
labelArea.Select(PivotFieldType.Row, 0, PivotTableSelectionType.LabelOnly);
pivotTable.Format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
Style valueStyle = workbook.CreateStyle();
valueStyle.ForegroundColor = Color.LightGreen;
valueStyle.Pattern = BackgroundType.Solid;
PivotArea valueArea = new PivotArea(pivotTable);
valueArea.SelectField(PivotFieldType.Row, "Fruit");
pivotTable.Format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.CalculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.Save("FormatPivotArea.xlsx");
```

## **格式化数据透视表的 CellArea**
当关注的区域是普通工作表矩形而非语义数据透视区域时，使用 `PivotTable.Format(CellArea, Style)`。  
`CellArea` 由 `StartRow`、`StartColumn`、`EndRow` 和 `EndColumn` 属性描述。其数值为基于零的工作表坐标，结束坐标标识矩形中包含的最后一行和最后一列，因此该区域覆盖从起始位置到结束位置（含）的单元格。  
不同于字段锚定的格式，`CellArea` 格式会立即应用于单元格，无需再次调用 `CalculateData()` 即可显示样式。  
`CellArea` 矩形可能同时包含标签单元格和数值单元格。下一节说明 Aspose.Cells 与 Excel 在内部如何表示该矩形。  
下面示例使用斜体、浅蓝色样式格式化数据透视表的矩形 `E4:F5`，并在无需进一步重新计算的情况下保存工作簿。

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
// Highlight the first two fruit rows (the rectangle E4:F5)
Style highlightStyle = workbook.CreateStyle();
highlightStyle.Font.IsItalic = true;
highlightStyle.ForegroundColor = Color.FromArgb(0xFF, 0x99, 0xCC, 0xFF);
highlightStyle.Pattern = BackgroundType.Solid;
CellArea rectangle = new CellArea { StartRow = 3, StartColumn = 4, EndRow = 4, EndColumn = 5 };
pivotTable.Format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.Save("FormatPivotCellArea.xlsx");
```

## **Pivot Areas 与 Cell Areas 的映射方式**
Excel 将数据透视表的格式存储为 `pivotArea` 记录，而非普通工作表单元格样式记录。Aspose.Cells 使用相同的模型，因此在记录格式化请求时会将其转换为 PivotArea。  
用户提供的 `CellArea` 与内部存储的 PivotArea 之间的关系是双向多对多的。  
- 一个 `CellArea` 可能生成多个 PivotArea。如果矩形同时包含标签单元格和数值单元格，它会被拆分为分别的标签规则和数据规则，因为数据透视模型对标签格式和数据格式是独立处理的。  
- 一个 PivotArea 可能对应多个不相连的 `CellArea` 实例。诸如总计行的语义区域，或项不连续的字段，可能覆盖多个矩形。这就是 `PivotArea.GetCellAreas()` 返回集合而非单一矩形的原因。  
通过 `PivotTable.Format` 执行的每一次格式化操作都会记录在 `PivotTable.PivotFormats` 中。每个 `PivotTableFormat` 条目公开其关联的 `PivotArea` 以及应用的 `Style`。`PivotArea` 重载每次调用仅添加一条记录，而包含不同语义区域的 `CellArea` 则可能添加多条记录。  
为区分已存储的区域，每个 `PivotArea` 提供 `OnlyLabel` 和 `OnlyData` 标志。下面示例格式化一个同时覆盖标签和数值的矩形，检查 `PivotTable.PivotFormats`，并打印每个已存储 PivotArea 解析得到的 `CellArea` 坐标。

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
Style highlightStyle = workbook.CreateStyle();
highlightStyle.Font.IsItalic = true;
highlightStyle.ForegroundColor = Color.FromArgb(0xFF, 0x99, 0xCC, 0xFF);
highlightStyle.Pattern = BackgroundType.Solid;
// ONE rectangle in...
CellArea rectangle = new CellArea { StartRow = 3, StartColumn = 4, EndRow = 4, EndColumn = 5 };
pivotTable.Format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
Console.WriteLine("Stored formats: " + pivotTable.PivotFormats.Count);
for (int i = 0; i < pivotTable.PivotFormats.Count; i++)
{
    PivotArea storedArea = pivotTable.PivotFormats[i].PivotArea;
    Console.WriteLine($"Format {i}: OnlyLabel={storedArea.OnlyLabel}, OnlyData={storedArea.OnlyData}");
    foreach (CellArea resolved in storedArea.GetCellAreas())
        Console.WriteLine($"    rows {resolved.StartRow + 1}-{resolved.EndRow + 1}, columns {resolved.StartColumn + 1}-{resolved.EndColumn + 1}");
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=True, OnlyData=False
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=False, OnlyData=True
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.Save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
由于格式是以 PivotArea 而非普通单元格样式存储的，它们在重新计算和刷新后仍然存在。无论是使用 `PivotTable.RefreshData` 刷新数据透视表、使用 `CalculateData` 重新计算，还是保存后重新加载，所有已存储的 PivotArea 都会重新解析到其当前所在位置并重新应用样式。
{{% /alert %}}

当需要在刷新后保持突出显示附着于字段或语义区域时，使用通过 `Select` 或 `SelectField` 构建的 `PivotArea`；若只需在当前数据透视表布局中格式化固定矩形，则使用 `CellArea`。单元格级别的 `Format(int row, int column, Style)` 重载用于定位单个单元格。若要一次性重新设置整个数据透视表的样式，请使用父页面中介绍的 `FormatAll`。

## **Related Articles**
- [将样式应用于数据透视表](/cells/zh/net/apply-style-to-pivot-table/)
- [添加数据透视表的行和列字段](/cells/zh/net/pivot-table-add-row-and-column-fields/)
- [管理数据透视表中的数值字段](/cells/zh/net/manage-value-fields/)
- [刷新数据透视表](/cells/zh/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}