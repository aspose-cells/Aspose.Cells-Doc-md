---
title: 在数据透视表中显示数值为
linktitle: 在数据透视表中显示数值为
description: 使用 Aspose.Cells for Python via .NET 将数据透视表的数据字段值显示为总计的百分比、与基准项的差异、累计总和、排名等。
keywords: Aspose.Cells for Python via .NET, 数据透视表, 显示数值为, 数据展示格式, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Python
type: docs
weight: 145
url: /zh/python-net/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
数据透视表通常使用诸如 `SUM` 或 `COUNT` 等聚合函数对每个数据字段进行汇总。Excel 的 **Show Values As** 功能会用二次计算的结果替换每个显示的聚合值，例如总计的百分比、累计总和、与选定基准项的差异或排名，从而无需使用辅助公式或计算列即可进行对比分析。  
典型用法包括：占比分析（行、列或整体总计的百分比）；使用期间字段的累计总和进行累积报表；通过与基准项的差异或百分比差异进行基准分析；以及将数值按从小到大或从大到小进行排名。  
在 Aspose.Cells for Python via .NET 中，`PivotFieldDataDisplayFormat` 用于选择二次计算方式。只读属性 `PivotField.show_values_setting` 返回 `PivotShowValuesSetting` 对象，其可写属性 `calculation_type`、`base_field_index`、`base_item_position_type` 和 `base_item_index` 用于配置行为；便利方法 `PivotField.show_values_as(...)` 可一次性设置这四个属性。将这些设置应用于从 `PivotTable.data_fields` 获取的数据字段或数值字段。

## **PivotFieldDataDisplayFormat 枚举成员**
数据字段仍保留其聚合函数（如 `SUM` 或 `COUNT`），而 **Show Values As** 只改变聚合值的显示方式。  
除了直接写入 `PivotShowValuesSetting` 属性（参见最后一节），也可以通过一次调用的便利方法来完成相同的配置：

```python
from aspose.cells.pivot import PivotField, PivotFieldDataDisplayFormat, PivotItemPositionType
def show_values_as(
    pivot_field: PivotField,
    display_format: PivotFieldDataDisplayFormat,
    base_field: int,
    base_item_position_type: PivotItemPositionType,
    base_item: int,
) -> None:
    pivot_field.show_values_as(
        display_format,
        base_field,
        base_item_position_type,
        base_item,
    )
```

| 参数 | 含义 | 何时需要 |
| --- | --- | --- |
| `display_format` | 要应用的 `PivotFieldDataDisplayFormat` 二次计算方式。 | 始终需要。 |
| `base_field` | 基字段在数据透视表基字段集合中的零基索引（例如，基项所在的行字段索引）。 | 仅适用于以下六种基准相关格式（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`、`RUNNING_TOTAL_IN`、`PERCENTAGE_OF_RUNNING_TOTAL_IN`、`PERCENTAGE_OF_PARENT_TOTAL`）；其它格式均忽略。 |
| `base_item_position_type` | 基项相对于当前项的选择方式：`PivotItemPositionType.PREVIOUS`、`.NEXT` 或 `.CUSTOM`。 | 仅适用于三种基项格式（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`）；其它格式均忽略。 |
| `base_item` | 基项的零基索引。 | 仅当 `base_item_position_type` 为 `CUSTOM` 时使用（此时索引指向具体的基项）；`PREVIOUS` / `NEXT` 时及所有非基项格式请传 `0`。 |

| 计算类型 | 行为 | 基项参数 |
| --- | --- | --- |
| `NORMAL` | 不进行二次计算，直接显示聚合值（默认）。 | — |
| `DIFFERENCE_FROM` | 显示为相对于基字段中基项值的差额。 | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM`（`CUSTOM` 时需提供 `base_item`） |
| `PERCENTAGE_OF` | 显示为相对于基字段中基项值的百分比。 | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM`（`CUSTOM` 时需提供 `base_item`） |
| `PERCENTAGE_DIFFERENCE_FROM` | 显示为相对于基字段中基项值的百分比差额。 | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM`（`CUSTOM` 时需提供 `base_item`） |
| `RUNNING_TOTAL_IN` | 显示为基字段中连续项的累计总和。 | `base_field`（决定累计顺序的字段） |
| `PERCENTAGE_OF_ROW` | 显示为行总计的百分比。 | — |
| `PERCENTAGE_OF_COLUMN` | 显示为列总计的百分比。 | — |
| `PERCENTAGE_OF_TOTAL` | 显示为整体总计的百分比。 | — |
| `INDEX` | 使用 Excel 索引公式 ((value * grand total) / (row total * column total)) 显示。 | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | 显示为其父行总计的百分比（针对嵌套行字段）。 | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | 显示为其父列总计的百分比（针对嵌套列字段）。 | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | 显示为其父总计的百分比。 | `baseField`（作为参照的父字段） |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | 显示为基字段中累计总和的百分比。 | `base_field`（累计字段） |
| `RANK_SMALLEST_TO_LARGEST` | 将数值从最小（1）到最大进行排名。 | — |
| `RANK_LARGEST_TO_SMALLEST` | 将数值从最大（1）到最小进行排名。 | — |

{{% alert color="primary" %}}
`show_values_as(...)` 写入 `PivotShowValuesSetting` 属性（`calculation_type`、`base_field_index`、`base_item_position_type`、`base_item_index`）——方法和属性对象是配置同一状态的两种方式，映射了 Excel “显示数值为” 对话框中的基字段和基项选择器。
{{% /alert %}}

## **将数值显示为总计的百分比**
调用 `PivotField.show_values_as` 并传入 `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL`，即可将每个数据字段单元格（包括整体总计）转换为其在整体总计中的占比。这样显示的数字即为完整结果集的比例。此格式仅针对整体总计进行比较，无需基字段或基项——后面的参数 (`0`, `PivotItemPositionType.PREVIOUS`, `0`) 仅为占位符，格式本身会忽略它们，如上表所示。

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldDataDisplayFormat, PivotFieldType, PivotItemPositionType
# Load or create a workbook with source data
workbook = ac.Workbook()
data_sheet = workbook.worksheets[0]
data_sheet.cells.get("A1").put_value("Fruit")
data_sheet.cells.get("B1").put_value("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
amounts = [10, 20, 30, 40, 50, 60]
for i in range(len(fruits)):
    data_sheet.cells.get(i + 1, 0).put_value(fruits[i])
    data_sheet.cells.get(i + 1, 1).put_value(amounts[i])
# Add a pivot table on a new worksheet (worksheets.add() returns the sheet index)
pivot_sheet_index = workbook.worksheets.add()
pivot_table = workbook.worksheets[pivot_sheet_index].pivot_tables.add("=Sheet1!A1:B7", 2, 2)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Show the Amount data field as a percentage of the grand total with the
# one-call method; PercentageOfTotal takes no base item, so the trailing
# base arguments (0, Previous, 0) are placeholders the format ignores
data_field = pivot_table.data_fields[0]
data_field.show_values_as(
    PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL,
    0,
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculate_data()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
```

## **获取并配置 PivotField.show_values_setting**
通过只读属性 `PivotField.show_values_setting` 可以读取当前配置：该属性返回字段的 `PivotShowValuesSetting` 对象，四个属性描述了当前的 **Show Values As** 计算方式。若要修改配置，调用 `PivotField.show_values_as` 方法即可——一次调用会写入所有四个设置，无需逐个赋值。  
`PivotShowValuesSetting` 对象公开了 `show_values_as` 写入的四个属性：
- `calculation_type` 用于选择 `PivotFieldDataDisplayFormat` 的二次计算方式。  
- `base_field_index` 指定基字段在数据透视表字段集合中的零基索引，供基准相关格式使用。  
- `base_item_position_type` 确定基项相对于当前项的位置，可取 `PivotItemPositionType.NEXT`、`PivotItemPositionType.PREVIOUS` 或 `PivotItemPositionType.CUSTOM`。  
- `base_item_index` 指定零基的基项索引，仅在 `base_item_position_type` 为 `CUSTOM` 时使用。  
调用 `show_values_as` 后，请再次调用 `PivotTable.calculate_data()`，以便重新计算并重新渲染数据透视表主体，使新配置生效。

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldDataDisplayFormat, PivotFieldType, PivotItemPositionType
workbook = ac.Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.worksheets[1].pivot_tables[0]
data_field = pivot_table.data_fields[0]
# Read the current show-values settings
settings = data_field.show_values_setting
print(f"CalculationType: {settings.calculation_type}")
print(f"BaseFieldIndex: {settings.base_field_index}")
print(f"BaseItemPositionType: {settings.base_item_position_type}")
print(f"BaseItemIndex: {settings.base_item_index}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.show_values_as(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivot_table.row_fields[0].base_index,
    PivotItemPositionType.PREVIOUS,
    0
)
pivot_table.calculate_data()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"CalculationType now: {data_field.show_values_setting.calculation_type}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
```

## **相关文章**
- [管理数据透视表中的值字段](/cells/zh/python-net/manage-value-fields/)
- [刷新数据透视表](/cells/zh/python-net/refresh-pivot-table/)
- [对数据透视表应用样式](/cells/zh/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}