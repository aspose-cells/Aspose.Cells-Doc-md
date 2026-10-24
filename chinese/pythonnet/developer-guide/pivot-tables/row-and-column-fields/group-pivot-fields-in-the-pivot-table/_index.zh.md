---
title: 在数据透视表中分组透视字段
linktitle: 在数据透视表中分组透视字段
description: 学习如何使用 PivotField.Group 和 PivotFieldGroupOptions 在 Aspose.Cells for Python via .NET 中将数据透视表的行和列透视字段分组为日期期间（如月份和季度）以及数值区域。
keywords: Aspose.Cells, 数据透视表, 分组透视字段, PivotField.Group, PivotFieldGroupOptions, 日期分组, 数值分组, 月份, 季度, 数值区域, Python via .NET
type: docs
weight: 80
url: /zh/python-net/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
- 当数据透视表的行或列字段包含许多不同项时，分组透视字段非常有用，例如包含数百个日期的日期字段或包含许多分散值的数字字段。分组将这些项折叠为有意义的分组：日期折叠为月份、季度和年份，数字折叠为 0-1、2-3、4-5 等区域。这使得大型数据透视表更加紧凑并易于分析。Aspose.Cells for Python via .NET 通过 `pivot_field.group()` 方法（按数据类型自动分组）和 `pivot_field.group(pivot_field_group_options)`（自定义分组选项）提供此功能。
- 日期分组将各个日期汇总为更大的期间，例如天、月、季度和年，并构建时间层次结构（例如年、季度、月）。一段时间内的趋势一目了然，每个期间级别都成为数据透视表行区域或列区域中自己的透视字段。
- 分组仅适用于放置在数据透视表的行或列区域中的字段。数据（值）字段不能直接分组。要对这样的字段进行分组，必须先将其添加到数据透视表的行或列区域。

## **自动分组透视字段**
无参数的 `pivot_field.group()` 重载会检查字段的数据类型并自动对其进行分组。仅包含日期（和空白）的字段按月分组。仅包含数字（和空白）的字段使用自动间隔分组到数值区域中。

```python
import aspose.cells as ac
# 加载示例工作簿
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# 访问第二个工作表及其数据透视表
pt = wb.worksheets[1].pivot_tables[0]
# 自动分组第一个行字段。
# 该字段包含日期，因此按月份分组。
field = pt.row_fields[0]
field.group()
# 计算数据透视表数据并保存输出文件
pt.calculate_data()
wb.save("outputAutoGroupPivotField.xlsx")
```

## **使用自定义选项分组透视字段**
`PivotFieldGroupOptions` 类提供自定义分组配置。对于日期字段，设置 `start_date`、`end_date` 和 `group_types`。对于数值字段，设置 `start_number`、`end_number` 和 `interval`。`new_pivot_field` 属性控制分组是否在原始字段旁边创建新的透视字段（请参阅本文末尾的“注意”部分）。

### **按月和季度分组日期字段**
以下示例按开始日期和结束日期之间的月和季度对示例数据透视表的日期行字段进行分组。代码加载 [示例 Excel 文件](sampleGroupPivotFieldsInPivotTable.xlsx)，执行分组，计算数据透视表数据，并保存分组结果。屏幕截图显示了效果：日期行字段现已按季度和月份分组。
请注意，`options.group_types` 中值的顺序将被忽略。无论按什么顺序列出分组类型，分组字段始终从最大期间显示到最小期间：年、季度、月、天、小时、分钟、秒。在本例中，月份在 `options.group_types` 中列在季度之前，但季度显示为外部级别，月份显示为内部级别。

```python
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import PivotGroupByType
from aspose.cells.pivot import PivotFieldGroupOptions
# 加载示例工作簿
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# 访问第二个工作表及其数据透视表
pt = wb.worksheets[1].pivot_tables[0]
# 按月份和季度对第一个行字段（日期字段）进行分组
options = PivotFieldGroupOptions()
options.start_date = datetime(2008, 1, 1)
options.end_date = datetime(2008, 9, 5)
options.group_types = [PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS]
pt.row_fields[0].group(options)
# 计算数据透视表数据并保存输出文件
pt.calculate_data()
wb.save("outputGroupPivotFieldsInPivotTable.xlsx")
```

![按月份和季度分组的数据透视表](group-pivot-fields-in-the-pivot-table_1.png)

### **将数值字段分组为区域**
示例数据透视表的 `FieldTwo` 最初是数据（值）字段。由于只能对行或列字段进行分组，因此代码首先调用 `pivot_table.add_field_to_area(PivotFieldType.ROW, "FieldTwo")` 将 `FieldTwo` 移动到行区域，刷新数据透视表，然后使用 `start_number=0`、`end_number=5` 和 `interval=2` 将数值字段分组为 0-1、2-3 和 4-5 这些区域。

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldGroupOptions
# 加载示例工作簿
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# 访问第二个工作表及其数据透视表
pt = wb.worksheets[1].pivot_tables[0]
# FieldTwo 是一个数据字段：先将其移动到行区域，
# 因为只有行/列字段才能进行分组
pt.add_field_to_area(PivotFieldType.ROW, "FieldTwo")
pt.calculate_data()
# 将数字字段分组为 0-1、2-3、4-5 的区间
options = PivotFieldGroupOptions()
options.start_number = 0.0
options.end_number = 5.0
options.interval = 2.0
pt.row_fields[1].group(options)
# 计算数据透视表数据并保存输出文件
pt.calculate_data()
wb.save("outputNumberGroupPivotField.xlsx")
```

## **注意**

{{% alert color="primary" %}}
- `pivot_field.group_by()` 方法重载已弃用并从 API 接口中移除。`pivot_field.group()` 和 `pivot_field.group(pivot_field_group_options)` 是替代方法。
- 在 Microsoft Excel 中，对数值字段进行分组会用分组区域替换原始透视字段，而对日期字段进行分组会在原始字段旁边创建新的透视字段（每个分组级别各一个，例如季度和月份）。从 Aspose.Cells 26.10 开始，`pivot_field.group()` 方法遵循与 Excel 相同的行为。`PivotFieldGroupOptions.new_pivot_field` 属性是为了与旧版本兼容而存在的：对于数值分组，默认值为 false，对于日期时间分组，默认值为 true；如果希望日期分组替换原始透视字段而不是创建新的透视字段，请将其设置为 false。
- `PivotFieldGroupOptions.interval` 属性仅对数值分组和按天进行日期分组（例如，将日期分组为 7 天周期）有效；当按月、季度或年对日期进行分组时，该属性将被忽略。
{{% /alert %}}

## **相关文章**
- [在数据透视表中添加行和列字段](/cells/zh/python-net/pivot-table-add-row-and-column-fields/)
- [按标签或值筛选数据透视表](/cells/zh/python-net/filter-by-label-or-value-of-pivot-table/)
- [在数据透视表中添加页面字段](/cells/zh/python-net/add-page-field-in-pivot-table/)
- [对数据透视表应用样式](/cells/zh/python-net/apply-style-to-pivot-table/)
- [刷新数据透视表](/cells/zh/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}