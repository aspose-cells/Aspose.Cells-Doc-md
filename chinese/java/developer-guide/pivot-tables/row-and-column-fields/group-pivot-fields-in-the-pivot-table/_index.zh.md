---
title: 在数据透视表中对数据透视字段分组
linktitle: 在数据透视表中对数据透视字段分组
description: 学习如何使用 PivotField.group 和 PivotFieldGroupOptions 在 Aspose.Cells for Java 中将数据透视表中的行和列数据透视字段按日期周期（如月份和季度）和数值范围进行分组。
keywords: Aspose.Cells, 数据透视表, 对数据透视字段分组, PivotField.group, PivotFieldGroupOptions, 日期分组, 数字分组, 月份, 季度, 数值范围, Java
type: docs
weight: 80
url: /zh/java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
- 当数据透视表的行或列字段包含许多不同的项时，对数据透视字段分组非常有用，例如包含数百个日期的日期字段或包含许多离散值的数值字段。分组会将这些项折叠为有意义的区段：日期折叠为月份、季度和年份，数字折叠为 0-1、2-3、4-5 等范围。这使得大型数据透视表更加紧凑、更易于分析。Aspose.Cells 通过 `PivotField.group()` 方法（按数据类型自动分组）和 `PivotField.group(PivotFieldGroupOptions)`（自定义分组选项）提供此功能。
- 日期分组将各个日期聚合为更大的周期，例如天、月、季度和年，并构建一个时间层次结构（例如年份、季度、月份）。时间趋势一目了然，每个周期级别都会成为数据透视表行区域或列区域中的独立数据透视字段。
- 分组仅适用于放置在数据透视表 ROW 或 COLUMN 区域中的字段。数据（值）字段无法直接分组。若要对此类字段进行分组，必须先将其添加到数据透视表的行或列区域中。

## **自动对数据透视字段分组**
无参数的 `PivotField.group()` 重载会检查字段的数据类型并自动对其分组。仅包含日期（和空白）的字段按月份分组。仅包含数字（和空白）的字段使用自动间隔分组为数值区域。

```java
import com.aspose.cells.*;
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
PivotField field = pt.getRowFields().get(0);
field.group();
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **使用自定义选项对数据透视字段分组**
`PivotFieldGroupOptions` 类提供自定义分组配置。对于日期字段，请设置 `startDate`、`endDate` 和 `groupTypes`。对于数值字段，请设置 `startNumber`、`endNumber` 和 `interval`。`newPivotField` 属性控制分组是否在原始字段旁边创建新的数据透视字段（请参阅本文末尾的"说明"部分）。

### **按月份和季度对日期字段分组**
下面的示例将示例数据透视表的日期行字段按起始和结束日期之间的月份和季度分组。代码加载[示例 Excel 文件](sampleGroupPivotFieldsInPivotTable.xlsx)，执行分组，计算数据透视表数据，并保存分组后的结果。截图显示了效果：日期行字段现已按季度和月份分组。
请注意，`options.groupTypes` 中值的顺序会被忽略。无论组类型的列出顺序如何，分组字段始终按从最大周期到最小周期的顺序显示：年、季度、月、天、小时、分钟、秒。在本示例中，`options.groupTypes` 中月份的列出顺序在季度之前，但季度显示为外部级别，月份显示为内部级别。

```java
import com.aspose.cells.*;
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.setStartDate(new com.aspose.cells.DateTime(2008, 1, 1));
options.setEndDate(new com.aspose.cells.DateTime(2008, 9, 5));
options.setGroupTypes(new int[] { PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS });
pt.getRowFields().get(0).group(options);
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![按月份和季度分组的数据透视表](group-pivot-fields-in-the-pivot-table_1.png)

### **将数值字段分组为范围**
示例数据透视表的 `FieldTwo` 最初是一个数据（值）字段。由于只能对行或列字段进行分组，因此代码首先调用 `PivotTable.addFieldToArea(PivotFieldType.ROW, "FieldTwo")` 将 `FieldTwo` 移动到行区域，刷新数据透视表，然后使用 `startNumber = 0`、`endNumber = 5` 和 `interval = 2` 将数值字段分组为 0-1、2-3 和 4-5 的范围。

```java
import com.aspose.cells.*;
// 加载示例工作簿
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// 访问第二个工作表及其数据透视表
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo 是一个数据字段：首先将其移动到行区域，
// 因为只有行/列字段可以分组
pt.addFieldToArea(PivotFieldType.ROW, "FieldTwo");
pt.calculateData();
// 将数值字段分组为 0-1、2-3、4-5 范围
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.setStartNumber(0);
options.setEndNumber(5);
options.setInterval(2);
pt.getRowFields().get(1).group(options);
// 计算数据透视表数据并保存输出文件
pt.calculateData();
wb.save("outputNumberGroupPivotField.xlsx");
```

## **说明**

{{% alert color="primary" %}}
- `PivotField.groupBy()` 方法重载已弃用，并已从 API 中移除。`PivotField.group()` 和 `PivotField.group(PivotFieldGroupOptions)` 是替代方法。
- 在 Microsoft Excel 中，对数值字段进行分组会用分组后的范围替换原始数据透视字段，而对日期字段进行分组会在原始字段旁边创建新的数据透视字段（每个组级别一个，例如季度和月份）。从 Aspose.Cells 26.10 开始，`PivotField.group()` 方法遵循与 Excel 相同的行为。`PivotFieldGroupOptions.newPivotField` 属性是为了与旧版本兼容而存在的：对于数值分组默认为 false，对于日期时间分组默认为 true；如果希望日期分组替换原始数据透视字段而不是创建新数据透视字段，请将其设置为 false。
- `PivotFieldGroupOptions.interval` 属性仅对数值分组和按天的日期分组生效（例如将日期分组为 7 天周期）；当日期按月、季度或年分组时，该属性将被忽略。
{{% /alert %}}

## **相关文章**
- [在数据透视表中添加行和列字段](/cells/zh/java/pivot-table-add-row-and-column-fields/)
- [按标签或值筛选数据透视表](/cells/zh/java/filter-by-label-or-value-of-pivot-table/)
- [在数据透视表中添加页面字段](/cells/zh/java/add-page-field-in-pivot-table/)
- [向数据透视表应用样式](/cells/zh/java/apply-style-to-pivot-table/)
- [刷新数据透视表](/cells/zh/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}