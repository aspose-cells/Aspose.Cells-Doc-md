---
title: 在数据透视表中显示值方式
linktitle: 在数据透视表中显示值方式
description: 使用 Aspose.Cells for Java 将数据透视表的数据字段值显示为总计的百分比、相对于基准项的差异、运行总计、排名等。
keywords: Aspose.Cells, 数据透视表, 显示值方式, 数据展示格式, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Java
type: docs
weight: 145
url: /zh/java/show-values-as-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
数据透视表通常会使用诸如 `Sum` 或 `Count` 等聚合函数对每个数据字段进行汇总。Excel 的 **Show Values As** 功能会将每个显示结果替换为基于该聚合值的二次计算——例如，总计的百分比、运行总计、相对于选定基准项的差异或排名——从而无需辅助公式或计算列即可进行比较分析。常见的使用场景包括：按行、列或整体总计的百分比进行份额分析；在周期字段中使用运行总计进行累计报表；通过相对于基准项的差异或百分比差异进行基准分析；以及将数值从最小到最大或从最大到最小进行排名。
在 Aspose.Cells for Java 中，`PivotFieldDataDisplayFormat` 用于选择二次计算方式。只读的 `PivotField.getShowValuesSetting()` 获取器返回一个 `PivotShowValuesSetting` 对象，其 `setCalculationType(...)`、`setBaseFieldIndex(...)`、`setBaseItemPositionType(...)`、`setBaseItemIndex(...)` 方法用于配置行为；便利方法 `PivotField.showValuesAs(...)` 可在一次调用中应用这四个设置。将这些设置应用于通过 `PivotTable.getDataFields()` 获取的数据或数值字段。

## **PivotFieldDataDisplayFormat 枚举成员**
数据字段仍然保持其聚合函数（如 Sum 或 Count），而 **Show Values As** 仅改变聚合值的显示方式。除了直接使用 `PivotShowValuesSetting` 的 setter（见最后一节），也可以通过一次调用的便利方法来完成相同的配置：

```java
public class CodeRunner
{
    public void showValuesAs(PivotFieldDataDisplayFormat displayFormat, int baseField,
                             PivotItemPositionType baseItemPositionType, int baseItem)
    {
    }
}
```

| 参数 | 含义 | 何时必填 |
| --- | --- | --- |
| `displayFormat` | 要应用的 `PivotFieldDataDisplayFormat` 二次计算方式。 | 始终必填。 |
| `baseField` | 基准字段在数据透视表基准字段集合中的零基索引（例如，基准项所属的行字段索引）。 | 仅适用于以下六种基准相关格式（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`、`RUNNING_TOTAL_IN`、`PERCENTAGE_OF_RUNNING_TOTAL_IN`、`PERCENTAGE_OF_PARENT_TOTAL`）；其它格式均忽略。 |
| `baseItemPositionType` | 基准项相对于当前项的选择方式：`PivotItemPositionType.PREVIOUS`、`NEXT` 或 `CUSTOM`。 | 仅适用于三种基项格式（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`）；其它格式均忽略。 |
| `baseItem` | 基准项的零基索引。 | 仅当 `baseItemPositionType` 为 `CUSTOM` 时使用（此时索引用于精确指定基准项）；`PREVIOUS` / `NEXT` 及所有非基准格式请传 `0`。 |

| 计算类型 | 行为 | 基准项参数 |
| --- | --- | --- |
| `NORMAL` | 无二次计算，聚合值原样显示（默认）。 | — |
| `DIFFERENCE_FROM` | 将值显示为相对于基准字段中基准项值的差异。 | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM`（仅 `CUSTOM` 时需提供 `baseItem`） |
| `PERCENTAGE_OF` | 将值显示为相对于基准字段中基准项值的百分比。 | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM`（仅 `CUSTOM` 时需提供 `baseItem`） |
| `PERCENTAGE_DIFFERENCE_FROM` | 将值显示为相对于基准字段中基准项值的百分比差异。 | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM`（仅 `CUSTOM` 时需提供 `baseItem`） |
| `RUNNING_TOTAL_IN` | 将值显示为基准字段中连续项的运行总计。 | `baseField`（用于决定累计顺序的字段） |
| `PERCENTAGE_OF_ROW` | 将值显示为行总计的百分比。 | — |
| `PERCENTAGE_OF_COLUMN` | 将值显示为列总计的百分比。 | — |
| `PERCENTAGE_OF_TOTAL` | 将值显示为整体总计的百分比。 | — |
| `INDEX` | 使用 Excel 的索引公式 ((value * grand total) / (row total * column total)) 显示值。 | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | 将值显示为其父行总计的百分比（适用于嵌套的行字段）。 | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | 将值显示为其父列总计的百分比（适用于嵌套的列字段）。 | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | 将值显示为其父总计的百分比。 | `baseField`（作为参照的父字段） |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | 将值显示为基准字段中运行总计的百分比。 | `baseField`（累计字段） |
| `RANK_SMALLEST_TO_LARGEST` | 按从最小（1）到最大进行排名。 | — |
| `RANK_LARGEST_TO_SMALLEST` | 按从最大（1）到最小进行排名。 | — |

{{% alert color="primary" %}}
`showValuesAs(...)` 通过调用 `setCalculationType(...)`、`setBaseFieldIndex(...)`、`setBaseItemPositionType(...)` 与 `setBaseItemIndex(...)`，一次性设置 `PivotShowValuesSetting` 值——该方法与属性对象提供了两种配置相同状态的方式，映射了 Excel “显示值方式”对话框中的基准字段和基准项选择器。
{{% /alert %}}

## **将值显示为总计的百分比**
调用 `PivotField.showValuesAs(...)` 并传入 `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL`，即可将每个数据字段单元格（包括整体总计）转换为其在整体总计中的占比。显示的数字因此成为完整结果集的比例。此格式仅相对于整体总计进行计算，无需基准字段或基准项——后置参数（`0`, `PivotItemPositionType.PREVIOUS`, `0`）在该格式下会被忽略，如上表所示。

```java
import com.aspose.cells.*;
// Load or create a workbook with source data
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.getWorksheets().get(0);
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Amount");
String[] fruits = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
int[] amounts = { 10, 20, 30, 40, 50, 60 };
for (int i = 0; i < fruits.length; i++)
{
    dataSheet.getCells().get(i + 1, 0).putValue(fruits[i]);
    dataSheet.getCells().get(i + 1, 1).putValue(amounts[i]);
}
// Add a pivot table on a new worksheet
int pivotSheetIndex = workbook.getWorksheets().add();
PivotTable pivotTable = workbook.getWorksheets().get(pivotSheetIndex).getPivotTables()
        .add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
// base arguments (0, PREVIOUS, 0) are placeholders the format ignores
PivotField dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL, 0,
        PivotItemPositionType.PREVIOUS, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **获取并配置 PivotField.getShowValuesSetting**
通过 `PivotField.getShowValuesSetting()` 读取当前配置：只读的 getter 返回该字段的 `PivotShowValuesSetting` 对象，其四个属性描述了已激活的 **Show Values As** 计算方式。若需更改配置，调用 `PivotField.showValuesAs(...)` 方法即可——一次调用即可写入全部四个设置，无需逐个属性赋值。
`PivotShowValuesSetting` 对象公开以下四个属性（由 `showValuesAs(...)` 写入）：
- `getCalculationType()` / `setCalculationType(...)` 用于选择 `PivotFieldDataDisplayFormat` 二次计算方式。
- `getBaseFieldIndex()` / `setBaseFieldIndex(...)` 指定基准字段在数据透视表字段集合中的零基索引，供基准相关格式使用。
- `getBaseItemPositionType()` / `setBaseItemPositionType(...)` 确定基准项相对于当前项的定位方式，接受 `PivotItemPositionType.NEXT`、`PivotItemPositionType.PREVIOUS` 或 `PivotItemPositionType.CUSTOM`。
- `getBaseItemIndex()` / `setBaseItemIndex(...)` 指定零基的基准项索引，仅在 `BaseItemPositionType` 为 `CUSTOM` 时使用。
在调用 `showValuesAs(...)` 之后，请再次调用 `PivotTable.calculateData()`，使数据透视表主体重新计算并根据更新后的配置重新渲染。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.getShowValuesSetting();
System.out.println("CalculationType: " + settings.getCalculationType());
System.out.println("BaseFieldIndex: " + settings.getBaseFieldIndex());
System.out.println("BaseItemPositionType: " + settings.getBaseItemPositionType());
System.out.println("BaseItemIndex: " + settings.getBaseItemIndex());
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    PivotItemPositionType.PREVIOUS,
    0
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
System.out.println("CalculationType now: " + dataField.getShowValuesSetting().getCalculationType());
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **相关文章**
- [在数据透视表中管理数值字段](/cells/zh/java/manage-value-fields/)
- [刷新数据透视表](/cells/zh/java/refresh-pivot-table/)
- [对数据透视表应用样式](/cells/zh/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}