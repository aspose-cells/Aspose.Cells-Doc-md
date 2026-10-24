---
title: 在数据透视表中分组数据透视字段
linktitle: 在数据透视表中分组数据透视字段
description: 了解如何使用 PivotField.group 和 PivotFieldGroupOptions 在 Aspose.Cells for Node.js via Java 中将数据透视表中的行和列透视字段分组为日期周期（如月份和季度）以及数值区域。
keywords: Aspose.Cells, 数据透视表, 分组数据透视字段, PivotField.group, PivotFieldGroupOptions, 日期分组, 数值分组, 月份, 季度, 数值区域, Node.js
type: docs
weight: 80
url: /zh/nodejs-java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的用法场景**
- 当数据透视表的行字段或列字段包含许多不同的项时,分组数据透视字段非常有用,例如包含数百个日期的日期字段或包含许多分散值的数值字段。分组将这些项归并为有意义的区段:日期归并为月份、季度和年份,数值归并为 0-1、2-3、4-5 这样的区域。这使得大型数据透视表变得紧凑且更易于分析。Aspose.Cells for Node.js via Java 通过 `PivotField.group()` 方法（按数据类型自动分组）和 `PivotField.group(PivotFieldGroupOptions)`（自定义分组选项）提供此功能。
- 日期分组将各个日期汇总为更大的周期,例如天、月、季度和年,并构建时间层次结构（例如年份、季度、月份）。随时间变化的趋势一目了然,每个周期级别都成为数据透视表行区域或列区域中的独立数据透视字段。
- 分组仅适用于放置在数据透视表 ROW 或 COLUMN 区域中的字段。数据（值）字段不能直接分组。要对这样的字段进行分组,必须先将其添加到数据透视表的行区域或列区域中。

## **自动分组数据透视字段**
无参数的 `PivotField.group()` 重载会检查字段的数据类型并自动对其分组。仅包含日期（和空白）的字段按月份分组。仅包含数字（和空白）的字段使用自动间隔分组为数值区域。

```javascript
const AsposeCells = require("aspose.cells");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// 访问第二个工作表及其数据透视表
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// 自动分组第一个行字段。
// 该字段包含日期，因此按月份分组。
let field = pt.getRowFields().get(0);
field.group();
// 计算数据透视表数据并保存输出文件
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **使用自定义选项分组数据透视字段**
`PivotFieldGroupOptions` 类提供自定义分组配置。对于日期字段,请设置 `StartDate`、`EndDate` 和 `GroupTypes`。对于数值字段,请设置 `StartNumber`、`EndNumber` 和 `Interval`。`NewPivotField` 属性控制分组是否在原始字段旁创建新的数据透视字段（请参阅本文末尾的“注意”部分）。

### **按月份和季度对日期字段进行分组**
以下示例在开始日期和结束日期之间按月份和季度对示例数据透视表的日期行字段进行分组。代码加载[示例 Excel 文件](sampleGroupPivotFieldsInPivotTable.xlsx),执行分组,计算数据透视表数据,然后保存分组结果。截图显示了效果:日期行字段现在按季度和月份进行分组。
请注意,`options.GroupTypes` 中值的顺序会被忽略。无论以何种顺序列出分组类型,分组字段始终按从最大周期到最小周期的顺序显示:年、季度、月、日、小时、分钟、秒。在本示例中,`options.GroupTypes` 中月份排在季度之前,但季度显示为外层级别,月份显示为内层级别。

```javascript
const AsposeCells = require("aspose.cells");
// 加载示例工作簿
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// 访问第二个工作表及其数据透视表
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// 按月和季度对第一个行字段（日期字段）进行分组
const options = new AsposeCells.PivotFieldGroupOptions();
options.setStartDate(new Date(2008, 0, 1));
options.setEndDate(new Date(2008, 8, 5));
options.setGroupTypes([AsposeCells.PivotGroupByType.MONTHS, AsposeCells.PivotGroupByType.QUARTERS]);
pt.getRowFields().get(0).group(options);
// 计算数据透视表数据并保存输出文件
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![按月份和季度分组的数据透视表](group-pivot-fields-in-the-pivot-table_1.png)

### **将数值字段分组为区域**
示例数据透视表的 `FieldTwo` 最初是数据（值）字段。由于只能对行字段或列字段进行分组,代码首先调用 `pivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` 将 `FieldTwo` 移动到行区域,刷新数据透视表,然后使用 `StartNumber = 0`、`EndNumber = 5` 和 `Interval = 2` 将数值字段分组为 0-1、2-3 和 4-5 区域。

```javascript
const AsposeCells = require("aspose.cells");
// 加载示例工作簿
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// 访问第二个工作表及其数据透视表
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo 是一个数据字段：先将其移到行区域，
// 因为只有行/列字段可以进行分组
pt.addFieldToArea(AsposeCells.PivotFieldType.ROW, "FieldTwo");
pt.calculateData();
// 将数值字段分组为 0-1、2-3、4-5 的区间
const options = new AsposeCells.PivotFieldGroupOptions();
options.setStartNumber(0);
options.setEndNumber(5);
options.setInterval(2);
pt.getRowFields().get(1).group(options);
// 计算数据透视表数据并保存输出文件
pt.calculateData();
wb.save("outputNumberGroupPivotField.xlsx");
```

## **注意**

{{% alert color="primary" %}}
- `PivotField.GroupBy()` 方法重载已弃用并从 API 表面中移除。`PivotField.group()` 和 `PivotField.group(PivotFieldGroupOptions)` 是替代方法。
- 在 Microsoft Excel 中,对数值字段进行分组会用分组区域替换原始数据透视字段,而对日期字段进行分组会在原始字段旁创建新的数据透视字段（每个分组级别对应一个,例如季度和月份）。从 Aspose.Cells for Node.js via Java 26.10 开始,`PivotField.group()` 方法遵循与 Excel 相同的行为。`PivotFieldGroupOptions.NewPivotField` 属性用于与旧版本兼容:数值分组默认为 false,日期时间分组默认为 true;如果希望日期分组替换原始数据透视字段而不是创建新的数据透视字段,请将其设置为 false。
- `PivotFieldGroupOptions.Interval` 属性仅对数值分组和按天进行的日期分组（例如将日期分组为 7 天周期）有效;当日期按月、季度或年分组时,该属性将被忽略。
{{% /alert %}}

## **相关文章**
- [在数据透视表中添加行和列字段](/cells/zh/nodejs-java/pivot-table-add-row-and-column-fields/)
- [按标签或值筛选数据透视表](/cells/zh/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [在数据透视表中添加页面字段](/cells/zh/nodejs-java/add-page-field-in-pivot-table/)
- [对数据透视表应用样式](/cells/zh/nodejs-java/apply-style-to-pivot-table/)
- [刷新数据透视表](/cells/zh/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}