---
title: 在透视表中显示值的方式
linktitle: 在透视表中显示值的方式
description: 使用 Aspose.Cells for Python via .NET，将透视表数据字段的值显示为占总计的百分比、相对于基项的差异、累计总计、排名等。
keywords: Aspose.Cells, 透视表, 显示值方式, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, show_values_as, base_field_index, base_item_index, Python
type: docs
weight: 145
url: /zh/python-net/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
透视表通常使用 `SUM`、`COUNT` 等聚合函数对每个数据字段进行汇总。Excel 的 **显示值方式** 功能会将每个显示结果替换为基于该聚合结果的二次计算——例如，占总计的百分比、累计总计、相对于选定基项的差异或排名——从而无需辅助公式或计算列即可进行比较分析。  
常见用法包括对行、列或总计的占比分析；在期间字段中使用累计总计进行累计报告；使用相对于基项的差异或百分比差异对基准项进行方差分析；以及将数值从最小到最大或从最大到最小进行排名。  
在 Aspose.Cells for Python via .NET 中，`PivotShowValuesAsType` 枚举用于选择二次计算。只读属性 `PivotField.show_values_setting` 返回一个 `PivotShowValuesSetting` 对象，其可写属性 `show_values_as`、`base_field_index` 和 `base_item_index` 用于配置行为；便利方法 `PivotField.show_values_as(...)` 可在一次调用中应用相同设置。将这些设置应用于通过 `PivotTable.data_fields` 获得的数据或值字段。

## **PivotShowValuesAsType 枚举成员**
数据字段保留其聚合函数（如 `SUM` 或 `COUNT`），而显示值方式仅改变聚合值的展示方式。  
除了直接写入 `PivotShowValuesSetting` 属性（请参见最后一节），还有一个一次性调用的便利方法可应用相同配置。该方法有两种形式——一种通过索引指定基字段和基项，另一种通过名称指定：

```python
from aspose.cells.pivot import PivotField, PivotShowValuesAsType
def show_values_as(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: int,
    base_item: int,
) -> None:
    pivot_field.show_values_as(
        show_values_as_type,
        base_field,
        base_item,
    )

def show_values_as_by_name(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: str,
    base_item: str,
) -> None:
    pivot_field.show_values_as(
        show_values_as_type,
        base_field,
        base_item,
    )
```

| 参数 | 含义 | 何时需要 |
| --- | --- | --- |
| `show_values_as_type` | 要应用的 `PivotShowValuesAsType` 二次计算。 | 始终。 |
| `base_field` | 基字段在透视表基字段集合中的零基索引（例如基项所属的行字段索引），或在名称形式下为基字段的名称。 | 对于以下八种基相对格式（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`、`RUNNING_TOTAL_IN`、`PERCENTAGE_OF_PARENT_TOTAL`、`PERCENTAGE_OF_RUNNING_TOTAL_IN`、`RANK_SMALLEST_TO_LARGEST`、`RANK_LARGEST_TO_SMALLEST`），需要提供；其它格式请传 `0`（名称形式下传 `None`）。 |
| `base_item` | 基项的零基索引，拥有两个哨兵：`PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM`（-1）表示前一个项，`PivotShowValuesSetting.NEXT_PIVOT_ITEM`（-2）表示下一个项。名称形式使用基项的标题，若所选格式不需要基项则传 `None`。 | 仅在三种基项格式（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`）中评估基项；其余五种字段相对格式（`RUNNING_TOTAL_IN`、`PERCENTAGE_OF_PARENT_TOTAL`、`PERCENTAGE_OF_RUNNING_TOTAL_IN`、两种排名）忽略基项——请传 `0` 或 `None`。 |

| 计算类型 | 行为 | 基项参数 |
| --- | --- | --- |
| `NORMAL` | 无二次计算；聚合值按原样显示（默认）。 | — |
| `DIFFERENCE_FROM` | 将值显示为相对于基字段中基项值的差异。 | `base_field` + `base_item`（索引、标题或前/后哨兵） |
| `PERCENTAGE_OF` | 将值显示为相对于基字段中基项值的百分比。 | `base_field` + `base_item`（索引、标题或前/后哨兵） |
| `PERCENTAGE_DIFFERENCE_FROM` | 将值显示为相对于基字段中基项值的百分比差异。 | `base_field` + `base_item`（索引、标题或前/后哨兵） |
| `RUNNING_TOTAL_IN` | 将值显示为基字段中连续项的累计总计。 | `base_field`（用于累加顺序的字段） |
| `PERCENTAGE_OF_ROW` | 将值显示为行总计的百分比。 | — |
| `PERCENTAGE_OF_COLUMN` | 将值显示为列总计的百分比。 | — |
| `PERCENTAGE_OF_TOTAL` | 将值显示为总计的百分比。 | — |
| `INDEX` | 使用 Excel 的 INDEX 公式 ((value * grand total) / (row total * column total)) 显示值。 | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | 将值显示为其父行总计的百分比（针对嵌套行字段）。 | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | 将值显示为其父列总计的百分比（针对嵌套列字段）。 | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | 将值显示为其父总计的百分比。 | `base_field`（父字段的总计作为参考） |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | 将值显示为基字段中累计总计的百分比。 | `base_field`（累加字段） |
| `RANK_SMALLEST_TO_LARGEST` | 将值排名从最小（1）到最大。 | `base_field`（定义排名范围的字段） |
| `RANK_LARGEST_TO_SMALLEST` | 将值排名从最大（1）到最小。 | `base_field`（定义排名范围的字段） |

{{% alert color="primary" %}}
`show_values_as(...)` 会写入 `PivotShowValuesSetting` 的属性（`show_values_as`、`base_field_index`、`base_item_index`）——该方法与属性对象是配置同一状态的两种方式，等价于 Excel “显示值方式”对话框中的基字段和基项选择器。
{{% /alert %}}

## **将值显示为总计的百分比**
调用 `PivotField.show_values_as` 并传入 `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL`，可将每个数据字段单元格（包括总计）转换为其在总计中的占比。此格式仅将每个值相对于总计进行衡量，无需基字段或基项——后置参数 (`0`, `0`) 仅为占位，格式本身会忽略它们，正如上表所示。

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotShowValuesAsType
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
# base arguments (0, 0) are placeholders the format ignores
data_field = pivot_table.data_fields[0]
data_field.show_values_as(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0)
pivot_table.calculate_data()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
```

## **获取并配置 PivotField.show_values_setting**
通过只读属性 `PivotField.show_values_setting` 可以读取当前配置：该属性返回字段的 `PivotShowValuesSetting` 对象，其属性描述了当前的显示值方式计算。若要修改配置，只需调用 `PivotField.show_values_as` 方法——一次调用即可写入所有设置，无需逐个赋值。  
`PivotShowValuesSetting` 对象公开的状态包括：
- `show_values_as`：选择 `PivotShowValuesAsType` 二次计算。
- `base_field_index`：基字段在透视字段集合中的零基索引，供基字段相关格式使用。
- `base_item_index`：基项的零基索引，或两种哨兵之一——`PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM`（-1）表示前一个项，`PivotShowValuesSetting.NEXT_PIVOT_ITEM`（-2）表示后一个项。供基项相关格式使用。
- `base_field_name` 与 `base_item_caption` 为只读视图，报告解析后的基字段名称和基项标题；例如，在选择前置哨兵后，`base_item_caption` 显示为 `(previous)`。
在调用 `show_values_as` 后，需再次调用 `PivotTable.calculate_data()`，以便重新计算并重新渲染透视表主体，应用更新后的配置。

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotShowValuesAsType, PivotShowValuesSetting
workbook = ac.Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.worksheets[1].pivot_tables[0]
data_field = pivot_table.data_fields[0]
# Read the current show-values settings
settings = data_field.show_values_setting
print(f"ShowValuesAs: {settings.show_values_as}")
print(f"BaseFieldIndex: {settings.base_field_index}")
print(f"BaseItemIndex: {settings.base_item_index}")
print(f"BaseFieldName: {settings.base_field_name}")
print(f"BaseItemCaption: {settings.base_item_caption}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.show_values_as(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivot_table.row_fields[0].base_index,
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM
)
pivot_table.calculate_data()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"ShowValuesAs now: {data_field.show_values_setting.show_values_as}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
```

## **相关文档**
- [管理透视表中的值字段](/cells/zh/python-net/manage-value-fields/)
- [刷新透视表](/cells/zh/python-net/refresh-pivot-table/)
- [为透视表应用样式](/cells/zh/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}