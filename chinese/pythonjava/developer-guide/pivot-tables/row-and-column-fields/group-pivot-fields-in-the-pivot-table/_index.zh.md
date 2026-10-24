---
title: 在数据透视表中分组数据透视字段
linktitle: 在数据透视表中分组数据透视字段
description: 学习如何使用 PivotField.group 和 PivotFieldGroupOptions 在 Aspose.Cells for Python via Java 中将数据透视表中的行和列数据透视字段分组为月份、季度等日期周期以及数值区域。
keywords: Aspose.Cells, 数据透视表, 分组数据透视字段, PivotField.group, PivotFieldGroupOptions, 日期分组, 数值分组, 月份, 季度, 数值区域, Python
type: docs
weight: 80
url: /zh/python-java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的用法场景**
- 当数据透视表的行或列字段包含许多不同的项（例如包含数百个日期的日期字段，或包含许多分散值的数值字段）时，分组数据透视字段非常有用。分组会将这些项归并为有意义的区段：日期分为月、季度和年，数字分为 0-1、2-3、4-5 等区域。这样可以使大型数据透视表更加紧凑、更易于分析。Aspose.Cells 通过 `PivotField.group()` 方法（按数据类型自动分组）和 `PivotField.group(PivotFieldGroupOptions)`（自定义分组选项）提供此功能。
- 日期分组将各个日期汇总为更大的周期，例如天、月、季度和年，并构建时间层次结构（例如年、季度、月）。随时间变化的趋势一目了然，每个周期级别都会成为数据透视表行或列区域中独立的数据透视字段。
- 分组仅适用于放置在数据透视表行或列区域中的字段。数据（值）字段无法直接分组。要对这类字段进行分组，必须先将其添加到数据透视表的行或列区域中。

## **自动分组数据透视字段**
无参数的 `PivotField.group()` 重载会检查字段的数据类型并自动对其进行分组。仅包含日期（以及空白）的字段按月分组。仅包含数字（以及空白）的字段则使用自动间隔分组为数值区域。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# 加载示例工作簿
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# 访问第二个工作表及其数据透视表
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# 自动对第一个行字段进行分组
# 该字段包含日期，因此按月份进行分组
field = pt.getRowFields().get(0)
field.group()
# 计算数据透视表数据并保存输出文件
pt.calculateData()
wb.save("outputAutoGroupPivotField.xlsx")
jpype.shutdownJVM()
```

## **使用自定义选项分组数据透视字段**
`PivotFieldGroupOptions` 类提供自定义分组配置。对于日期字段，需设置 `StartDate`、`EndDate` 和 `GroupTypes`。对于数值字段，需设置 `StartNumber`、`EndNumber` 和 `Interval`。`NewPivotField` 属性用于控制分组是否在原始字段旁边创建新的数据透视字段（请参阅本文末尾的"注意"部分）。

### **按月和季度分组日期字段**
以下示例将示例数据透视表的日期行字段在指定的开始日期与结束日期之间按月和季度分组。代码加载[示例 Excel 文件](sampleGroupPivotFieldsInPivotTable.xlsx)，执行分组，计算数据透视表数据，并保存分组后的结果。屏幕截图显示了效果：日期行字段现在已按季度和月进行分组。
请注意，`options.GroupTypes` 中值的排列顺序会被忽略。无论组类型以何种顺序列出，分组后的字段始终按照从最大周期到最小周期的顺序显示：年、季度、月、天、小时、分钟、秒。在本示例中，月份在 `options.GroupTypes` 中列于季度之前，但季度仍显示为外层，月份显示为内层。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldGroupOptions, PivotGroupByType, DateTime
# 加载示例工作簿
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# 访问第二个工作表及其数据透视表
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# 按月份和季度对第一个行字段（日期字段）进行分组
options = PivotFieldGroupOptions()
options.setStartDate(DateTime(2008, 1, 1))
options.setEndDate(DateTime(2008, 9, 5))
options.setGroupTypes([PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS])
pt.getRowFields().get(0).group(options)
# 计算数据透视表数据并保存输出文件
pt.calculateData()
wb.save("outputGroupPivotFieldsInPivotTable.xlsx")
jpype.shutdownJVM()
```

![按月和季度分组的数据透视表](group-pivot-fields-in-the-pivot-table_1.png)

### **将数值字段分组为区域**
示例数据透视表中的 `FieldTwo` 最初是一个数据（值）字段。由于只有行或列字段可以进行分组，代码首先调用 `pivotTable.addFieldToArea(PivotFieldType.ROW, "FieldTwo")` 将 `FieldTwo` 移动到行区域，刷新数据透视表，然后使用 `StartNumber = 0`、`EndNumber = 5` 和 `Interval = 2` 将该数值字段分组为 0-1、2-3 和 4-5 区域。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, PivotFieldGroupOptions
# 加载示例工作簿
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# 访问第二个工作表及其数据透视表
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# FieldTwo 是一个数据字段：首先将其移动到行区域，
# 因为只有行/列字段才能进行分组
pt.addFieldToArea(PivotFieldType.ROW, "FieldTwo")
pt.calculateData()
# 将数值字段分组为 0-1、2-3、4-5 的区间
options = PivotFieldGroupOptions()
options.setStartNumber(0)
options.setEndNumber(5)
options.setInterval(2)
pt.getRowFields().get(1).group(options)
# 计算数据透视表数据并保存输出文件
pt.calculateData()
wb.save("outputNumberGroupPivotField.xlsx")
jpype.shutdownJVM()
```

## **注意**

{{% alert color="primary" %}}
- `PivotField.groupBy()` 方法的重载已被弃用，并已从 API 中移除。`PivotField.group()` 和 `PivotField.group(PivotFieldGroupOptions)` 是其替代方法。
- 在 Microsoft Excel 中，对数值字段进行分组会用分组后的区域**替换**原始数据透视字段，而对日期字段进行分组则会在原始字段旁边**新建**数据透视字段（每个组级别各一个，例如季度和月）。从 Aspose.Cells 26.10 开始，`PivotField.group()` 方法遵循与 Excel 相同的行为。`PivotFieldGroupOptions.NewPivotField` 属性是为了兼容旧版本而保留的：数值分组默认为 false，日期时间分组默认为 true；如果希望日期分组替换原始数据透视字段而不是创建新的数据透视字段，可将其设置为 false。
- `PivotFieldGroupOptions.Interval` 属性仅对数值分组以及按天进行的日期分组（例如将日期分组为 7 天周期）有效；当按月、季度或年对日期进行分组时，该属性将被忽略。
{{% /alert %}}

## **相关文章**
- [在数据透视表中添加行和列字段](/cells/zh/python-java/pivot-table-add-row-and-column-fields/)
- [按标签或值过滤数据透视表](/cells/zh/python-java/filter-by-label-or-value-of-pivot-table/)
- [在数据透视表中添加页面字段](/cells/zh/python-java/add-page-field-in-pivot-table/)
- [对数据透视表应用样式](/cells/zh/python-java/apply-style-to-pivot-table/)
- [刷新数据透视表](/cells/zh/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}