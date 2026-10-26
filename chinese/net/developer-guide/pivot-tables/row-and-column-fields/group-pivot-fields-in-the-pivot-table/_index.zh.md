---
title: 在数据透视表中分组数据透视字段
description: 学习如何使用 PivotField.Group 和 PivotFieldGroupOptions 在 Aspose.Cells for .NET 中将数据透视表的行和列数据透视字段分组为日期周期（如月和季度）以及数值范围。
linktitle: 分组数据透视字段
keywords: Aspose.Cells, 数据透视表, 数据透视字段分组, PivotField.Group, PivotFieldGroupOptions, 日期分组, 数值分组, 月份, 季度, 数值范围, C#
type: docs
weight: 80
url: /zh/net/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
- 当数据透视表的行或列字段包含许多不同的项时（例如包含数百个日期的日期字段或包含许多分散值的数值字段），对数据透视字段进行分组非常有用。分组会将这些项折叠为有意义的区段：日期折叠为月、季度和年，数值折叠为范围，例如 0-1、2-3、4-5。这使得大型数据透视表更加紧凑、更易于分析。Aspose.Cells 通过 `PivotField.Group()` 方法（按数据类型自动分组）和 `PivotField.Group(PivotFieldGroupOptions)`（自定义分组选项）提供此功能。
- 日期分组将各个日期汇总为更大的周期，例如日、月、季度和年，并构建一个时间层次结构（例如年、季度、月）。随时间变化的趋势一目了然，每个周期级别都会成为数据透视表行区域或列区域中的独立数据透视字段。
- 分组仅适用于放置在数据透视表 ROW（行）或 COLUMN（列）区域中的字段。数据（值）字段不能直接分组。若要对此类字段进行分组，必须先将其添加到数据透视表的行区域或列区域。

## **自动分组数据透视字段**
无参数的 `PivotField.Group()` 重载会检查字段的数据类型并进行自动分组。仅包含日期（和空白）的字段按月分组。仅包含数字（和空白）的字段使用自动间隔分组为数值范围。

```csharp
using Aspose.Cells.Pivot;
// 加载示例工作簿
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// 访问第二个工作表及其数据透视表
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// 自动分组第一个行字段。
// 该字段包含日期，因此按月份分组。
PivotField field = pt.RowFields[0];
field.Group();
// 计算数据透视表数据并保存输出文件
pt.CalculateData();
wb.Save("outputAutoGroupPivotField.xlsx");
```

## **使用自定义选项分组数据透视字段**
`PivotFieldGroupOptions` 类提供自定义分组配置。对于日期字段，需设置 `StartDate`、`EndDate` 和 `GroupTypes`。对于数值字段，需设置 `StartNumber`、`EndNumber` 和 `Interval`。`NewPivotField` 属性用于控制分组是否在原始字段旁边创建新的数据透视字段（请参阅本文末尾的"备注"部分）。

### **按月和季度分组日期字段**
以下示例在开始日期和结束日期之间，按月和季度对示例数据透视表的日期行字段进行分组。代码加载[示例 Excel 文件](sampleGroupPivotFieldsInPivotTable.xlsx)，执行分组操作，计算数据透视表数据，并保存分组结果。屏幕截图显示了效果：日期行字段现在已按季度和月进行分组。
请注意，`options.GroupTypes` 中值的顺序将被忽略。无论组类型按何种顺序列出，分组后的字段始终按从最大周期到最小周期的顺序显示：年、季度、月、日、小时、分钟、秒。在本示例中，`options.GroupTypes` 中月份的列出顺序在季度之前，但季度显示为外层级别，月份显示为内层级别。

```csharp
using Aspose.Cells.Pivot;
// 加载示例工作簿
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// 访问第二个工作表及其数据透视表
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// 按月份和季度对第一个行字段（日期字段）进行分组
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.StartDate = new DateTime(2008, 1, 1);
options.EndDate = new DateTime(2008, 9, 5);
options.GroupTypes = new PivotGroupByType[] { PivotGroupByType.Months, PivotGroupByType.Quarters };
pt.RowFields[0].Group(options);
// 计算数据透视表数据并保存输出文件
pt.CalculateData();
wb.Save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![按月和季度分组的数据透视表](group-pivot-fields-in-the-pivot-table_1.png)

### **将数值字段分组为范围**
示例数据透视表的 `FieldTwo` 最初是一个数据（值）字段。由于仅行或列字段可被分组，代码首先调用 `PivotTable.AddFieldToArea(PivotFieldType.Row, "FieldTwo")` 将 `FieldTwo` 移到行区域，刷新数据透视表，然后使用 `StartNumber = 0`、`EndNumber = 5` 和 `Interval = 2` 将该数值字段分组为 0-1、2-3 和 4-5 的范围。

```csharp
using Aspose.Cells.Pivot;
// 加载示例工作簿
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// 访问第二个工作表及其数据透视表
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// FieldTwo 是一个数据字段：首先将其移动到行区域，
// 因为只有行/列字段可以进行分组
pt.AddFieldToArea(PivotFieldType.Row, "FieldTwo");
pt.CalculateData();
// 将数字字段分组为 0-1、2-3、4-5 范围
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.StartNumber = 0;
options.EndNumber = 5;
options.Interval = 2;
pt.RowFields[1].Group(options);
// 计算数据透视表数据并保存输出文件
pt.CalculateData();
wb.Save("outputNumberGroupPivotField.xlsx");
```

## **备注**

{{% alert color="primary" %}}
- `PivotField.GroupBy()` 方法重载已被弃用，并从 API 表面中移除。`PivotField.Group()` 和 `PivotField.Group(PivotFieldGroupOptions)` 是替代方法。
- 在 Microsoft Excel 中，对数值字段进行分组会使用分组后的范围**替换**原始数据透视字段，而对日期字段进行分组会在原始字段旁边**创建新的**数据透视字段（每个分组级别一个，例如季度和月）。从 Aspose.Cells 26.10 开始，`PivotField.Group()` 方法遵循与 Excel 相同的行为。`PivotFieldGroupOptions.NewPivotField` 属性是为了与旧版本兼容而存在的：数值分组时默认为 false，日期时间分组时默认为 true；若希望日期分组替换原始数据透视字段而不是创建新的数据透视字段，可将其设置为 false。
- `PivotFieldGroupOptions.Interval` 属性仅对数值分组以及按天进行日期分组（例如将日期分组为 7 天周期）有效；当日期按月、季度或年分组时，该属性将被忽略。
{{% /alert %}}

## **相关文章**
- [在数据透视表中添加行和列字段](/cells/zh/net/pivot-table-add-row-and-column-fields/)
- [按标签或值筛选数据透视表](/cells/zh/net/filter-by-label-or-value-of-pivot-table/)
- [在数据透视表中添加页面字段](/cells/zh/net/add-page-field-in-pivot-table/)
- [向数据透视表应用样式](/cells/zh/net/apply-style-to-pivot-table/)
- [刷新数据透视表](/cells/zh/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}