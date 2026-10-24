---
title: 在数据透视表中分组透视字段
linktitle: 在数据透视表中分组透视字段
description: 了解如何使用 PivotField.Group 和 PivotFieldGroupOptions 在 Aspose.Cells for Node.js via C++ 中将数据透视表的行和列透视字段分组为日期周期(如月份和季度)和数值区域。
keywords: Aspose.Cells, 数据透视表, 分组透视字段, PivotField.Group, PivotFieldGroupOptions, 日期分组, 数字分组, 月份, 季度, 数值区域, JavaScript
type: docs
weight: 80
url: /zh/nodejs-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
- 当数据透视表的行或列字段包含许多不同的项(例如包含数百个日期的日期字段或包含许多分散数值的数值字段)时,对透视字段进行分组非常有用。分组会将它们折叠为有意义的区段:将日期折叠为月份、季度和年份,将数值折叠为 0-1、2-3、4-5 等区域。这使大型数据透视表变得紧凑且更易于分析。Aspose.Cells 通过 `pivotField.group()` 方法(按数据类型自动分组)和 `pivotField.group(PivotFieldGroupOptions)`(自定义分组选项)提供此功能。
- 日期分组将各个日期汇总为更大的周期,如天、月、季度和年,并构建时间层次结构(例如年、季度、月)。一段时间内的趋势一目了然,每个周期级别都会成为数据透视表行或列区域中的一个独立透视字段。
- 分组仅适用于放置在数据透视表的行或列区域中的字段。数据(值)字段不能直接分组。要对这样的字段进行分组,必须先将其添加到数据透视表的行或列区域。

## **自动分组透视字段**
无参数的 `pivotField.group()` 重载会检查字段的数据类型并自动分组。仅包含日期(和空白)的字段按月份分组。仅包含数字(和空白)的字段使用自动间隔分组到数值区域。

```javascript
const AsposeCells = require("aspose.cells.node");
// 加载示例工作簿
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// 访问第二个工作表及其数据透视表
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// 自动分组第一个行字段
// 该字段包含日期,因此按月分组
const field = pt.getRowFields().get(0);
field.group();
// 计算数据透视表数据并保存输出文件
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **使用自定义选项分组透视字段**
`PivotFieldGroupOptions` 类提供自定义分组配置。对于日期字段,请设置 `startDate`、`endDate` 和 `groupTypes`。对于数值字段,请设置 `startNumber`、`endNumber` 和 `interval`。`newPivotField` 属性控制分组是否在原始字段旁边创建新的透视字段(请参阅本文末尾的"注意"部分)。

### **按月份和季度对日期字段进行分组**
以下示例按开始和结束日期之间的月份和季度对示例数据透视表的日期行字段进行分组。代码加载[示例 Excel 文件](sampleGroupPivotFieldsInPivotTable.xlsx),执行分组,计算数据透视表数据,然后保存分组结果。截图显示了效果:日期行字段现在按季度和月份分组。
请注意,`options.groupTypes` 中值的顺序将被忽略。无论以何种顺序列出分组类型,分组字段始终按从最大周期到最小周期的顺序显示:年、季度、月、天、小时、分钟、秒。在本例中,虽然月份在 `options.groupTypes` 中列在季度之前,但季度显示为外部级别,月份显示为内部级别。

```javascript
const AsposeCells = require("aspose.cells.node");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// 访问第二个工作表及其数据透视表
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// 按月和季度对第一个行字段(日期字段)进行分组
let options = new AsposeCells.PivotFieldGroupOptions();
options.setStartDate(new Date(2008, 0, 1));
options.setEndDate(new Date(2008, 8, 5));
options.setGroupTypes([AsposeCells.PivotGroupByType.Months, AsposeCells.PivotGroupByType.Quarters]);
pt.getRowFields().get(0).group(options);
// 计算数据透视表数据并保存输出文件
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![按月份和季度分组的数据透视表](group-pivot-fields-in-the-pivot-table_1.png)

### **将数值字段分组到区域中**
示例数据透视表的 `FieldTwo` 最初是一个数据(值)字段。由于只能对行或列字段进行分组,因此代码首先调用 `pivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` 将 `FieldTwo` 移动到行区域,刷新数据透视表,然后使用 `startNumber = 0`、`endNumber = 5` 和 `interval = 2` 将数值字段分组为 0-1、2-3 和 4-5 等区域。

```javascript
const AsposeCells = require("aspose.cells.node");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// 访问第二个工作表及其数据透视表
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo 是数据字段:首先将其移动到行区域,
// 因为只有行/列字段才能进行分组
pt.addFieldToArea(AsposeCells.PivotFieldType.Row, "FieldTwo");
pt.calculateData();
// 将数值字段分组为范围 0-1、2-3、4-5
let options = new AsposeCells.PivotFieldGroupOptions();
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
- `pivotField.groupBy()` 方法重载已弃用并从 API 表面中移除。`pivotField.group()` 和 `pivotField.group(PivotFieldGroupOptions)` 是替代方法。
- 在 Microsoft Excel 中,对数值字段进行分组会用分组区域替换原始字段;而对日期字段进行分组会在原始字段旁边创建新的透视字段(每个分组级别一个,例如季度和月份)。从 Aspose.Cells 26.10 开始,`pivotField.group()` 方法遵循与 Excel 相同的行为。`pivotFieldGroupOptions.newPivotField` 属性是为了与旧版本兼容而存在的:对于数值分组默认为 false,对于日期时间分组默认为 true;如果希望日期分组替换原始字段而不是创建新的透视字段,请将其设置为 false。
- `pivotFieldGroupOptions.interval` 属性仅对数值分组和按天对日期进行分组(例如将日期分组为 7 天的周期)有效;当按月、季度或年对日期进行分组时,该属性将被忽略。
{{% /alert %}}

## **相关文章**
- [在数据透视表中添加行和列字段](/cells/zh/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [按标签或值筛选数据透视表](/cells/zh/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [在数据透视表中添加页面字段](/cells/zh/nodejs-cpp/add-page-field-in-pivot-table/)
- [将样式应用于数据透视表](/cells/zh/nodejs-cpp/apply-style-to-pivot-table/)
- [刷新数据透视表](/cells/zh/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}