---
title: 在数据透视表中使用值显示方式
description: 使用 Aspose.Cells for Python via Java，将数据透视表数据字段的值显示为占总计的百分比、与基准项的差异、累计总计、排名等。
linktitle: 值显示方式
keywords: Aspose.Cells, 数据透视表, 值显示方式, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex, Python
type: docs
weight: 145
url: /zh/python-java/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的用法场景**
数据透视表通常使用 `SUM` 或 `COUNT` 等聚合函数汇总每个数据字段。Excel 的 **值显示方式** 功能会用基于该聚合值计算得出的二次计算结果替换每个显示结果，例如占总计的百分比、累计总计、与选定基准项的差异或排名，因此无需辅助公式或计算列即可完成比较分析。
常见用途包括：分析各项占总计的份额，包括行总计、列总计或总计的百分比；使用期间字段中的累计总计进行累计报告；使用与基准项的差异或与基准项的百分比差异对照基准项进行差异分析；以及按值从小到大或从大到小进行排名。
在 Aspose.Cells for Python via Java 中，`PivotShowValuesAsType` 枚举用于选择二次计算。只读的 `PivotField.getShowValuesSetting()` 方法返回一个 `PivotShowValuesSetting` 对象，其 `setShowValuesAs(...)`、`setBaseFieldIndex(...)` 和 `setBaseItemIndex(...)` 方法用于配置行为；便捷方法 `PivotField.showValuesAs(...)` 通过一次调用应用相同的设置。请将这些设置应用到通过 `PivotTable.getDataFields()` 获取的数据字段或值字段。

## **PivotShowValuesAsType 枚举成员**
数据字段仍保留其聚合函数（如 `SUM` 或 `COUNT`），而值显示方式仅改变聚合值的显示方式。
除了直接使用 `PivotShowValuesSetting` 的设置方法（见最后一节）之外，还可以使用一次调用的便捷方法应用相同的配置。该方法有两种形式：一种通过索引指定基准字段和基准项，另一种通过名称指定：

```python
from asposecells.api import PivotField, PivotShowValuesAsType
def show_values_as(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: int,
    base_item: int,
):
    pivot_field.showValuesAs(show_values_as_type, base_field, base_item)

def show_values_as_by_name(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: str,
    base_item: str,
):
    pivot_field.showValuesAs(show_values_as_type, base_field, base_item)
```

| 参数 | 含义 | 何时需要 |
| --- | --- | --- |
| `show_values_as_type` | 要应用的 `PivotShowValuesAsType` 二次计算类型。 | 始终需要。 |
| `base_field` | 基准字段在数据透视表各基准字段中的从零开始索引（例如基准项所属行字段的索引），或者在名称形式中指定基准字段的名称。 | 下列八种相对于基准的格式（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`、`RUNNING_TOTAL_IN`、`PERCENTAGE_OF_PARENT_TOTAL`、`PERCENTAGE_OF_RUNNING_TOTAL_IN`、`RANK_SMALLEST_TO_LARGEST`、`RANK_LARGEST_TO_SMALLEST`）需要此参数；对于其他所有格式，请传入 `0`（或在名称形式中传入 `None`）。 |
| `base_item` | 基准项的从零开始索引，另有两个哨兵值：`PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) 表示前一项，`PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) 表示后一项。名称形式改为采用基准项的标题，并在所选格式不需要基准项时传入 `None`。 | 仅以下三种基于基准项的格式（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`）会计算基准项；以下五种相对于字段的格式（`RUNNING_TOTAL_IN`、`PERCENTAGE_OF_PARENT_TOTAL`、`PERCENTAGE_OF_RUNNING_TOTAL_IN`、`RANK_SMALLEST_TO_LARGEST`、`RANK_LARGEST_TO_SMALLEST`）会忽略此参数——请传入 `0` 或 `None`。 |

| 计算类型 | 行为 | 基准项参数 |
| --- | --- | --- |
| `NORMAL` | 不进行二次计算；按原样显示聚合值（默认值）。 | — |
| `DIFFERENCE_FROM` | 将值显示为与基准字段中某个基准项的值之间的差异。 | `base_field` + `base_item`（索引或标题，或前一项/后一项哨兵值） |
| `PERCENTAGE_OF` | 将值显示为基准字段中某个基准项值的百分比。 | `base_field` + `base_item`（索引或标题，或前一项/后一项哨兵值） |
| `PERCENTAGE_DIFFERENCE_FROM` | 将值显示为与基准字段中某个基准项的值之间的百分比差异。 | `base_field` + `base_item`（索引或标题，或前一项/后一项哨兵值） |
| `RUNNING_TOTAL_IN` | 将值显示为基准字段中连续项目的累计总计。 | `base_field`（其项目顺序决定累积方式的字段） |
| `PERCENTAGE_OF_ROW` | 将值显示为占行总计的百分比。 | — |
| `PERCENTAGE_OF_COLUMN` | 将值显示为占列总计的百分比。 | — |
| `PERCENTAGE_OF_TOTAL` | 将值显示为占总计的百分比。 | — |
| `INDEX` | 使用 Excel 索引公式 `(value * grand total) / (row total * column total)` 显示该值。 | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | 将值显示为占其父级行总计的百分比（适用于嵌套行字段）。 | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | 将值显示为占其父级列总计的百分比（适用于嵌套列字段）。 | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | 将值显示为占其父级总计的百分比。 | `base_field`（作为参考的父级字段） |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | 将值显示为占基准字段中累计总计的百分比。 | `base_field`（累积字段） |
| `RANK_SMALLEST_TO_LARGEST` | 对值进行排名，从最小值（1）到最大值。 | `base_field`（其项目定义排名范围的字段） |
| `RANK_LARGEST_TO_SMALLEST` | 对值进行排名，从最大值（1）到最小值。 | `base_field`（其项目定义排名范围的字段） |

{{% alert color="primary" %}}
`showValuesAs(...)` 通过 `setShowValuesAs`、`setBaseFieldIndex` 和 `setBaseItemIndex` 写入 `PivotShowValuesSetting` 的值——该方法与设置对象是配置同一状态的两种方式，对应 Excel“值显示方式”对话框中的基准字段和基准项选择器。
{{% /alert %}}

## **将值显示为总计的百分比**
调用 `PivotField.showValuesAs` 方法并传入 `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL`，即可将每个数据字段单元格（包括总计）转换为其在总计中所占的份额。因此，显示的数字表示其占完整结果集的比例。此格式仅以总计为参照来衡量每个值，因此不需要基准字段或基准项——末尾参数（`0`、`0`）只是该格式会忽略的占位符，正如上面的参数表所述。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotFieldType,
    PivotShowValuesAsType,
)
# Load or create a workbook with source data
workbook = Workbook()
data_sheet = workbook.getWorksheets().get(0)
data_sheet.getCells().get("A1").putValue("Fruit")
data_sheet.getCells().get("B1").putValue("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
# float literals keep putValue on the double overload (an untyped Python int is ambiguous between putValue(boolean/int/Object) overloads)
amounts = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0]
for i in range(len(fruits)):
    data_sheet.getCells().get(i + 1, 0).putValue(fruits[i])
    data_sheet.getCells().get(i + 1, 1).putValue(amounts[i])
# Add a pivot table on a new worksheet (getWorksheets().add() returns the sheet index)
pivot_sheet_index = workbook.getWorksheets().add()
pivot_table = workbook.getWorksheets().get(pivot_sheet_index).getPivotTables().add("=Sheet1!A1:B7", 2, 2)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Show the Amount data field as a percentage of the grand total with the
# one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
# base arguments (0, 0) are placeholders the format ignores
data_field = pivot_table.getDataFields().get(0)
data_field.showValuesAs(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0)
pivot_table.calculateData()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
jpype.shutdownJVM()
```

## **获取并配置 PivotField.getShowValuesSetting()**
通过 `PivotField.getShowValuesSetting()` 读取当前配置：该只读方法返回字段的 `PivotShowValuesSetting` 对象，其属性描述当前启用的值显示方式计算。若要更改配置，请调用 `PivotField.showValuesAs` 方法——该方法一次调用即可写入所有设置，因此无需逐项设置属性。
`PivotShowValuesSetting` 对象公开 `showValuesAs` 写入的状态：
- `getShowValuesAs()` 返回 `PivotShowValuesAsType` 二次计算类型，而 `setShowValuesAs(...)` 用于更改该类型。
- `getBaseFieldIndex()` 和 `setBaseFieldIndex(...)` 指定基准字段在数据透视字段中的从零开始索引。相对于基准的格式会使用此索引。
- `getBaseItemIndex()` 和 `setBaseItemIndex(...)` 指定基准项：可以是特定数据透视表项的从零开始索引，也可以是两个哨兵值之一，即表示前一项的 `PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) 或表示后一项的 `PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2)。基于基准项的格式会使用此值。
- `getBaseFieldName()` 和 `getBaseItemCaption()` 是只读视图，用于返回解析后的基准字段名称和基准项标题；例如，选择上一项哨兵值后，`getBaseItemCaption()` 返回 `(previous)`。
调用 `showValuesAs` 后，再次调用 `PivotTable.calculateData()`，以便根据更新后的配置重新计算并重新呈现数据透视表主体。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotShowValuesAsType,
    PivotShowValuesSetting,
)
workbook = Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.getWorksheets().get(1).getPivotTables().get(0)
data_field = pivot_table.getDataFields().get(0)
# Read the current show-values settings
settings = data_field.getShowValuesSetting()
print(f"ShowValuesAs: {settings.getShowValuesAs()}")
print(f"BaseFieldIndex: {settings.getBaseFieldIndex()}")
print(f"BaseItemIndex: {settings.getBaseItemIndex()}")
print(f"BaseFieldName: {settings.getBaseFieldName()}")
print(f"BaseItemCaption: {settings.getBaseItemCaption()}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.showValuesAs(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivot_table.getRowFields().get(0).getBaseIndex(),
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM,
)
pivot_table.calculateData()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"ShowValuesAs now: {data_field.getShowValuesSetting().getShowValuesAs()}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
jpype.shutdownJVM()
```

## **相关文章**
- [管理数据透视表中的值字段](/cells/zh/python-java/manage-value-fields/)
- [刷新数据透视表](/cells/zh/python-java/refresh-pivot-table/)
- [为数据透视表应用样式](/cells/zh/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}