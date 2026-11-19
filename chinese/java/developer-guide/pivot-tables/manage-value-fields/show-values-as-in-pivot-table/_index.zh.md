---
title: 数据透视表中的值显示方式
linktitle: 数据透视表中的值显示方式
description: 使用 Aspose.Cells for Java 将数据透视表数据字段值显示为占总计的百分比、与基准项的差异、累计总计、排名等。
keywords: Aspose.Cells, 数据透视表, 值显示方式, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex, Java
type: docs
weight: 145
url: /zh/java/show-values-as-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
数据透视表通常使用 `Sum` 或 `Count` 等聚合函数对每个数据字段进行聚合。Excel 的 **“值显示方式”** 功能会将每个显示结果替换为根据该聚合值计算得出的派生结果，例如占总计的百分比、累计总计、与选定基准项的差异或排名，从而无需辅助公式或计算列即可进行对比分析。
常见用途包括占比分析（包括占行、列或总计的百分比）、通过在期间字段中使用累计总计生成累计报表、使用“与基准项的差异”或“与基准项的百分比差异”以基准项为参照进行差异分析，以及按值从小到大或从大到小进行排名。
在 Aspose.Cells for Java 中，`PivotShowValuesAsType` 枚举用于选择派生计算类型。只读访问器 `PivotField.getShowValuesSetting()` 返回一个 `PivotShowValuesSetting` 对象，其 `setShowValuesAs(...)`、`setBaseFieldIndex(...)` 和 `setBaseItemIndex(...)` 方法用于配置行为；便捷方法 `PivotField.showValuesAs(...)` 通过一次调用即可应用相同的设置。将这些设置应用于从 `PivotTable.getDataFields()` 获取的数据字段或值字段。

## **`PivotShowValuesAsType` 枚举成员**
数据字段保留其聚合函数，例如 `Sum` 或 `Count`，而“值显示方式”仅改变聚合值的显示方式。
除直接使用 `PivotShowValuesSetting` 的设置方法（见最后一节）外，还可使用便捷方法通过一次调用应用相同的配置。该方法有两个重载：一个按索引指定基准字段和基准项，另一个按名称指定：

```java
public class CodeRunner
{
    public void showValuesAs(PivotShowValuesAsType showValuesAsType, int baseField, int baseItem)
    {
    }

    public void showValuesAs(PivotShowValuesAsType showValuesAsType, String baseField, String baseItem)
    {
    }
}
```

| 参数 | 含义 | 何时必需 |
| --- | --- | --- |
| `showValuesAsType` | 要应用的 `PivotShowValuesAsType` 派生计算类型。 | 始终需要。 |
| `baseField` | 基准字段在数据透视表中的索引（从 0 开始，例如基准项所属行字段的索引），或者在 `String` 重载中指定基准字段的名称。 | 以下八种基于基准的格式（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`、`RUNNING_TOTAL_IN`、`PERCENTAGE_OF_PARENT_TOTAL`、`PERCENTAGE_OF_RUNNING_TOTAL_IN`、`RANK_SMALLEST_TO_LARGEST`、`RANK_LARGEST_TO_SMALLEST`）需要此参数；对于其他所有格式，请传入 `0`（或在 `String` 重载中传入 `null`）。 |
| `baseItem` | 基准项的索引（从 0 开始），另有两个哨兵值：`PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) 用于选择前一项，`PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) 用于选择后一项。在 `String` 重载中改为指定基准项的标题；当选定格式不需要基准项时，指定 `null`。 | 仅以下三种基于基准项的格式（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`）会使用基准项；以下五种相对于字段的格式（`RUNNING_TOTAL_IN`、`PERCENTAGE_OF_PARENT_TOTAL`、`PERCENTAGE_OF_RUNNING_TOTAL_IN`、`RANK_SMALLEST_TO_LARGEST`、`RANK_LARGEST_TO_SMALLEST`）会忽略该参数——请传入 `0` 或 `null`。 |

| 计算类型 | 行为 | 基准项参数 |
| --- | --- | --- |
| `NORMAL` | 不执行派生计算；按原样显示聚合值（默认值）。 | — |
| `DIFFERENCE_FROM` | 将值显示为与基准字段中某个基准项的值之差。 | `baseField` + `baseItem`（索引或标题，或前一项/后一项哨兵值） |
| `PERCENTAGE_OF` | 将值显示为占基准字段中某个基准项值的百分比。 | `baseField` + `baseItem`（索引或标题，或前一项/后一项哨兵值） |
| `PERCENTAGE_DIFFERENCE_FROM` | 将值显示为相对于基准字段中某个基准项值的百分比差异。 | `baseField` + `baseItem`（索引或标题，或前一项/后一项哨兵值） |
| `RUNNING_TOTAL_IN` | 将值显示为基准字段中连续各项的累计总计。 | `baseField`（其项目顺序决定累计算法的字段） |
| `PERCENTAGE_OF_ROW` | 将值显示为占行总计的百分比。 | — |
| `PERCENTAGE_OF_COLUMN` | 将值显示为占列总计的百分比。 | — |
| `PERCENTAGE_OF_TOTAL` | 将值显示为占总计的百分比。 | — |
| `INDEX` | 使用 Excel 索引公式显示该值（(值 * 总计) / (行总计 * 列总计)）。 | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | 将值显示为占父级行总计的百分比（适用于嵌套行字段）。 | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | 将值显示为占父级列总计的百分比（适用于嵌套列字段）。 | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | 将值显示为占父级总计的百分比。 | `baseField`（以总计值为参考的父字段） |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | 将值显示为占基准字段中累计总计的百分比。 | `baseField`（执行累计的字段） |
| `RANK_SMALLEST_TO_LARGEST` | 对值从小到大进行排名，最小值为 1。 | `baseField`（其各项用于确定排名对象） |
| `RANK_LARGEST_TO_SMALLEST` | 对值从大到小进行排名，最大值为 1。 | `baseField`（其各项用于确定排名对象） |

{{% alert color="primary" %}}
`showValuesAs(...)` 通过 `setShowValuesAs(...)`、`setBaseFieldIndex(...)` 和 `setBaseItemIndex(...)` 设置 `PivotShowValuesSetting` 的状态。该方法与 `PivotShowValuesSetting` 对象是配置相同状态的两种方式，对应 Excel 的“值显示方式”对话框中的基准字段和基准项选择器。
{{% /alert %}}

## **将值显示为总计的百分比**
调用 `PivotField.showValuesAs(...)` 方法并传入 `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL`，可将每个数据字段单元格（包括总计单元格）转换为占总计的比例。因此，显示的数字表示各值在完整结果集中的占比。此格式仅以总计为参照计算每个值，因此不需要基准字段或基准项。末尾参数（`0`、`0`）只是占位参数；如上表所述，此格式会忽略这些参数。

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
// base arguments (0, 0) are placeholders the format ignores
PivotField dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **获取并配置 `PivotField.getShowValuesSetting()`**
调用 `PivotField.getShowValuesSetting()` 读取当前配置。只读访问器返回该字段的 `PivotShowValuesSetting` 对象，其属性描述当前生效的“值显示方式”计算。若要更改配置，请调用 `PivotField.showValuesAs(...)` 方法。该方法一次调用即可写入所有设置，因此无需逐个设置属性。
`PivotShowValuesSetting` 对象公开了 `showValuesAs(...)` 所写入的状态：
- `getShowValuesAs()` / `setShowValuesAs(...)` 用于选择 `PivotShowValuesAsType` 派生计算类型。
- `getBaseFieldIndex()` / `setBaseFieldIndex(...)` 指定基准字段在数据透视表字段中的索引（从 0 开始）。该索引用于基于基准的格式。
- `getBaseItemIndex()` / `setBaseItemIndex(...)` 指定基准项：特定数据透视表项的索引（从 0 开始），或两个哨兵值之一——`PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) 用于选择前一项，`PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) 用于选择后一项。该索引用于基于基准项的格式。
- `getBaseFieldName()` 和 `getBaseItemCaption()` 是只读方法，分别返回解析后的基准字段名称和基准项标题；例如，选择前一项哨兵值后，`getBaseItemCaption()` 返回 `(previous)`。
调用 `showValuesAs(...)` 后，再次调用 `PivotTable.calculateData()`，以便根据更新后的配置重新计算并重新呈现数据透视表主体。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.getShowValuesSetting();
System.out.println("ShowValuesAs: " + settings.getShowValuesAs());
System.out.println("BaseFieldIndex: " + settings.getBaseFieldIndex());
System.out.println("BaseItemIndex: " + settings.getBaseItemIndex());
System.out.println("BaseFieldName: " + settings.getBaseFieldName());
System.out.println("BaseItemCaption: " + settings.getBaseItemCaption());
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
System.out.println("ShowValuesAs now: " + dataField.getShowValuesSetting().getShowValuesAs());
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **相关文章**
- [管理数据透视表中的值字段](/cells/zh/java/manage-value-fields/)
- [刷新数据透视表](/cells/zh/java/refresh-pivot-table/)
- [为数据透视表应用样式](/cells/zh/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}