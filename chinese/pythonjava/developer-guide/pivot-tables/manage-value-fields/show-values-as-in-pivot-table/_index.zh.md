---
title: 在数据透视表中显示值的方式
description: 在数据透视表中将数据字段值显示为总计的百分比、相对于基准项的差额、累计总和、排名等，使用 Aspose.Cells for Python via Java。
linktitle: Show Values As
keywords: Aspose.Cells, 数据透视表, 显示值方式, 数据显示格式, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Python via Java
type: docs
weight: 145
url: /zh/python-java/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
数据透视表通常使用诸如 `Sum` 或 `Count` 等聚合函数对每个数据字段进行汇总。Excel 的 **Show Values As** 功能会将每个显示的结果替换为基于该聚合结果的二次计算——例如，总计的百分比、累计总和、相对于选定基准项的差额或排名——从而无需辅助公式或计算列即可进行对比分析。  
典型的使用包括：按行、列或总计的百分比进行份额分析；在期间字段中使用累计总和进行累计报表；通过相对于基准项的差额或百分比差额进行方差分析；以及将数值从最小到最大或从最大到最小进行排序。  
在 Aspose.Cells for Python via Java 中，`PivotFieldDataDisplayFormat` 用于选择二次计算。只读方法 `PivotField.getShowValuesSetting()` 返回一个 `PivotShowValuesSetting` 对象，其可写的 `setCalculationType`、`setBaseFieldIndex`、`setBaseItemPositionType` 和 `setBaseItemIndex` 方法用于配置行为；便利方法 `PivotField.showValuesAs(...)` 在一次调用中应用相同的四个设置。将这些设置应用于通过 `PivotTable.getDataFields()` 获取的数据或值字段。

## **PivotFieldDataDisplayFormat 枚举成员**
数据字段保持其聚合函数（如 Sum 或 Count），而 Show Values As 仅改变聚合值的显示方式。  
除了直接设置 `PivotShowValuesSetting` 属性（参见最后一节），一次调用的便利方法也会应用相同的配置：

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    PivotField,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
def show_values_as(
    pivot_field: PivotField,
    display_format: PivotFieldDataDisplayFormat,
    base_field: int,
    base_item_position_type: PivotItemPositionType,
    base_item: int,
) -> None:
    pivot_field.showValuesAs(
        display_format,
        base_field,
        base_item_position_type,
        base_item,
    )
jpype.shutdownJVM()
```

| 参数 | 含义 | 何时必需 |
| --- | --- | --- |
| `displayFormat` | 要应用的 `PivotFieldDataDisplayFormat` 二次计算。 | 始终。 |
| `baseField` | 基准字段在数据透视表基准字段集合中的零基索引（例如，基准项所属的行字段索引）。 | 仅适用于以下六种基准相关格式（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`、`RunningTotalIn`、`PercentageOfRunningTotalIn`、`PercentageOfParentTotal`）；其它格式均忽略。 |
| `baseItemPositionType` | 基准项相对于当前项的选择方式：`PivotItemPositionType.Previous`、`.Next` 或 `.Custom`。 | 仅适用于三种基项格式（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`）；其它格式均忽略。 |
| `baseItem` | 基准项的零基索引。 | 仅当 `baseItemPositionType` 为 `Custom` 时使用（此时索引指向确切的基准项）；`Previous`/`Next` 以及所有非基准格式均忽略 —— 传入 `0`。 |

| 计算类型 | 行为 | 基项参数 |
| --- | --- | --- |
| `Normal` | 无二次计算；聚合值直接显示（默认）。 | — |
| `DifferenceFrom` | 将值显示为相对于基准字段中基准项值的差额。 | `baseField` + `Previous`/`Next`/`Custom`（仅 `Custom` 时需 `baseItem`） |
| `PercentageOf` | 将值显示为相对于基准字段中基准项值的百分比。 | `baseField` + `Previous`/`Next`/`Custom`（仅 `Custom` 时需 `baseItem`） |
| `PercentageDifferenceFrom` | 将值显示为相对于基准字段中基准项值的百分比差额。 | `baseField` + `Previous`/`Next`/`Custom`（仅 `Custom` 时需 `baseItem`） |
| `RunningTotalIn` | 将值显示为基准字段中连续项的累计总和。 | `baseField`（决定累计顺序的字段） |
| `PercentageOfRow` | 将值显示为行总计的百分比。 | — |
| `PercentageOfColumn` | 将值显示为列总计的百分比。 | — |
| `PercentageOfTotal` | 将值显示为总体总计的百分比。 | — |
| `Index` | 使用 Excel 索引公式 ((value * total) / (row total * column total)) 显示值。 | — |
| `PercentageOfParentRowTotal` | 将值显示为其父行总计的百分比（用于嵌套行字段）。 | — |
| `PercentageOfParentColumnTotal` | 将值显示为其父列总计的百分比（用于嵌套列字段）。 | — |
| `PercentageOfParentTotal` | 将值显示为其父总计的百分比。 | `baseField`（作为参照的父字段） |
| `PercentageOfRunningTotalIn` | 将值显示为基准字段中累计总和的百分比。 | `baseField`（累计字段） |
| `RankSmallestToLargest` | 按从最小（1）到最大进行排名。 | — |
| `RankLargestToSmallest` | 按从最大（1）到最小进行排名。 | — |

{{% alert color="primary" %}}
`showValuesAs(...)` 通过 `setCalculationType`、`setBaseFieldIndex`、`setBaseItemPositionType` 和 `setBaseItemIndex` 写入 `PivotShowValuesSetting` 值——该方法和设置对象是配置同一状态的两种方式，体现了 Excel “显示值为” 对话框中基准字段和基准项选择器的行为。
{{% /alert %}}

## **将值显示为总计的百分比**
调用 `PivotField.showValuesAs` 并传入 `PivotFieldDataDisplayFormat.PercentageOfTotal`，即可将每个数据字段单元格（包括总计）转换为其在总体总计中的占比。显示的数字因此代表完整结果集的比例。此格式仅相对于总体总计进行计算，无需基准字段或基准项——后置参数 (`0`、`PivotItemPositionType.Previous`、`0`) 仅为占位符，格式本身会忽略它们，如上表所示。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    PivotTable,
    PivotField,
    PivotFieldType,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
# Load or create a workbook with source data
workbook = Workbook()
data_sheet = workbook.getWorksheets().get(0)
data_sheet.getCells().get("A1").putValue("Fruit")
data_sheet.getCells().get("B1").putValue("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
amounts = [10, 20, 30, 40, 50, 60]
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
# one-call method; PercentageOfTotal takes no base item, so the trailing
# base arguments (0, Previous, 0) are placeholders the format ignores
data_field = pivot_table.getDataFields().get(0)
data_field.showValuesAs(
    PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL,
    0,
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculateData()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
jpype.shutdownJVM()
```

## **获取并配置 PivotField.getShowValuesSetting()**
通过只读方法 `PivotField.getShowValuesSetting()` 读取当前配置：该方法返回字段的 `PivotShowValuesSetting` 对象，其四个属性描述了正在使用的 “显示值为” 计算。若要更改配置，调用 `PivotField.showValuesAs` 方法——一次调用即可写入全部四个设置，无需逐一赋值。  
`PivotShowValuesSetting` 对象公开以下四个属性：
- `getCalculationType()` 返回 `PivotFieldDataDisplayFormat` 二次计算，`setCalculationType(...)` 可更改它。
- `getBaseFieldIndex()` 和 `setBaseFieldIndex(...)` 指定基准字段在透视字段集合中的零基索引，供基准相关格式使用。
- `getBaseItemPositionType()` 和 `setBaseItemPositionType(...)` 确定基准项相对于当前项的定位方式，接受 `PivotItemPositionType.Next`、`PivotItemPositionType.Previous` 或 `PivotItemPositionType.Custom`。
- `getBaseItemIndex()` 和 `setBaseItemIndex(...)` 指定零基的基准项索引，仅在 `BaseItemPositionType` 为 `Custom` 时使用。
调用 `showValuesAs` 后，请再次调用 `PivotTable.calculateData()`，使透视表主体重新计算并使用更新的配置重新渲染。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
workbook = Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.getWorksheets().get(1).getPivotTables().get(0)
data_field = pivot_table.getDataFields().get(0)
# Read the current show-values settings
settings = data_field.getShowValuesSetting()
print(f"CalculationType: {settings.getCalculationType()}")
print(f"BaseFieldIndex: {settings.getBaseFieldIndex()}")
print(f"BaseItemPositionType: {settings.getBaseItemPositionType()}")
print(f"BaseItemIndex: {settings.getBaseItemIndex()}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.showValuesAs(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivot_table.getRowFields().get(0).getBaseIndex(),
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculateData()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"CalculationType now: {data_field.getShowValuesSetting().getCalculationType()}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
jpype.shutdownJVM()
```

## **相关文章**
- [管理数据透视表中的值字段](/cells/zh/python-java/manage-value-fields/)
- [刷新数据透视表](/cells/zh/python-java/refresh-pivot-table/)
- [为数据透视表应用样式](/cells/zh/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}