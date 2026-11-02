---
title: 在 Aspose.Cells for C++ 的透视表中显示值的方式
description: 使用 Aspose.Cells for C++ 将透视表数据字段值显示为总计的百分比、相对于基准项的差异、累计总计、排名等。
linktitle: Show Values As
keywords: Aspose.Cells, C++, 数据透视表, 显示值方式, 数据显示格式, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /zh/cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
透视表通常使用诸如 `Sum` 或 `Count` 等聚合函数对每个数据字段进行汇总。Excel 的 **显示值方式** 功能会用从该聚合结果派生的二次计算替换每个显示的结果——例如，总计的百分比、累计总计、相对于选定基准项的差异或排名——从而无需辅助公式或计算列即可进行比较分析。  
常见的使用包括：基于总计的份额分析（行、列或整体总计的百分比）；在期间字段中使用累计总计进行累积报告；通过相对于基准项的差异或百分比差异进行方差分析；以及将数值从最小到最大或从最大到最小进行排名。  
在 Aspose.Cells for C++ 中，`PivotFieldDataDisplayFormat` 用于选择二次计算。`PivotField.GetShowValuesSetting()` 访问器返回一个 `PivotShowValuesSetting` 对象，其 `SetCalculationType`、`SetBaseFieldIndex`、`SetBaseItemPositionType` 和 `SetBaseItemIndex` 方法用于配置行为；便利方法 `PivotField.ShowValuesAs(...)` 可在一次调用中设置这四个属性。将这些设置应用于通过 `PivotTable.GetDataFields()` 获取的数据或数值字段。

## **PivotFieldDataDisplayFormat 枚举成员**
数据字段保留其聚合函数（如 Sum 或 Count），而 **显示值方式** 仅改变聚合值的显示方式。  
除了直接写入 `PivotShowValuesSetting` 值（参见最后一节），一次调用的便利方法可应用相同的配置：

```cpp
void ShowValuesAs(PivotFieldDataDisplayFormat displayFormat, int32_t baseField, PivotItemPositionType baseItemPositionType, int32_t baseItem);
```

| 参数 | 含义 | 何时必需 |
| --- | --- | --- |
| `displayFormat` | 要应用的 `PivotFieldDataDisplayFormat` 二次计算方式。 | 始终。 |
| `baseField` | 透视表基字段的零基索引（例如基项所属的行字段索引）。 | 仅适用于以下六种基准相关格式（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`、`RunningTotalIn`、`PercentageOfRunningTotalIn`、`PercentageOfParentTotal`）；其它格式均忽略。 |
| `baseItemPositionType` | 基项相对于当前项的选择方式：`PivotItemPositionType::Previous`、`::Next` 或 `::Custom`。 | 仅适用于三种基项格式（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`）；其它格式均忽略。 |
| `baseItem` | 基项的零基索引。 | 仅当 `baseItemPositionType` 为 `Custom` 时需要（此时索引指定精确的基项）；`Previous` / `Next` 以及所有非基项格式均忽略——请传 `0`。 |

| 计算类型 | 行为 | 基项参数 |
| --- | --- | --- |
| `Normal` | 无二次计算；聚合值按原样显示（默认）。 | — |
| `DifferenceFrom` | 将数值显示为相对于基字段中基项的差值。 | `baseField` + `Previous`/`Next`/`Custom`（仅在 `Custom` 时使用 `baseItem`） |
| `PercentageOf` | 将数值显示为相对于基字段中基项的百分比。 | `baseField` + `Previous`/`Next`/`Custom`（仅在 `Custom` 时使用 `baseItem`） |
| `PercentageDifferenceFrom` | 将数值显示为相对于基字段中基项的百分比差异。 | `baseField` + `Previous`/`Next`/`Custom`（仅在 `Custom` 时使用 `baseItem`） |
| `RunningTotalIn` | 将数值显示为基字段中后续项的累计总计。 | `baseField`（决定累计顺序的字段） |
| `PercentageOfRow` | 将数值显示为行总计的百分比。 | — |
| `PercentageOfColumn` | 将数值显示为列总计的百分比。 | — |
| `PercentageOfTotal` | 将数值显示为整体总计的百分比。 | — |
| `Index` | 使用 Excel 索引公式 ((value * grand total) / (row total * column total)) 显示数值。 | — |
| `PercentageOfParentRowTotal` | 将数值显示为其父行总计的百分比（针对嵌套行字段）。 | — |
| `PercentageOfParentColumnTotal` | 将数值显示为其父列总计的百分比（针对嵌套列字段）。 | — |
| `PercentageOfParentTotal` | 将数值显示为其父总计的百分比。 | `baseField`（作为参照的父字段） |
| `PercentageOfRunningTotalIn` | 将数值显示为基字段中累计总计的百分比。 | `baseField`（累计字段） |
| `RankSmallestToLargest` | 将数值按从最小（1）到最大进行排名。 | — |
| `RankLargestToSmallest` | 将数值按从最大（1）到最小进行排名。 | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` 写入 `PivotShowValuesSetting` 值（`CalculationType`、`BaseFieldIndex`、`BaseItemPositionType`、`BaseItemIndex`）——该方法与设置对象是配置相同状态的两种方式，映射到 Excel “显示值方式”对话框中的基字段和基项选择器。
{{% /alert %}}

## **将值显示为总计的百分比**
调用 `PivotField.ShowValuesAs` 并传入 `PivotFieldDataDisplayFormat::PercentageOfTotal`，即可将每个数据字段单元格（包括总计）转换为其在整体总计中的占比。显示的数字因此成为完整结果集的比例。此格式仅相对于整体总计进行衡量，无需基字段或基项——后置参数 (`0`、`PivotItemPositionType::Previous`、`0`) 仅为占位，格式本身会忽略它们，如上表所示。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Load or create a workbook with source data
    Workbook workbook;
    Worksheet dataSheet = workbook.GetWorksheets().Get(0);
    Cells cells = dataSheet.GetCells();
    cells.Get(0, 0).PutValue(U16String("Fruit"));
    cells.Get(0, 1).PutValue(U16String("Amount"));
    const char* fruits[6] = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
    int32_t amounts[6] = { 10, 20, 30, 40, 50, 60 };
    for (int32_t i = 0; i < 6; i++)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(amounts[i]);
    }
    // Add a pivot table on a new worksheet
    int32_t pivotSheetIndex = workbook.GetWorksheets().Add();
    PivotTable pivotTable = workbook.GetWorksheets().Get(pivotSheetIndex).GetPivotTables().Add(u"=Sheet1!A1:B7", 2, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    // Show the Amount data field as a percentage of the grand total with the
    // one-call method; PercentageOfTotal takes no base item, so the trailing
    // base arguments (0, Previous, 0) are placeholders the format ignores
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    dataField.ShowValuesAs(PivotFieldDataDisplayFormat::PercentageOfTotal, 0, PivotItemPositionType::Previous, 0);
    pivotTable.CalculateData();
    // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
    workbook.Save(u"ShowValuesAsPercentageOfTotal.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **获取和配置 PivotField.ShowValuesSetting**
通过 `PivotField.GetShowValuesSetting()` 读取当前配置：该访问器返回字段的 `PivotShowValuesSetting` 对象，其四个 getter 方法描述正在使用的 “显示值方式” 计算。若要更改配置，调用 `PivotField.ShowValuesAs` 方法——一次调用即可写入全部四个设置，无需逐个赋值。  
`PivotShowValuesSetting` 对象公开了 `ShowValuesAs` 写入的四个值：
- `GetCalculationType()` / `SetCalculationType()` 选择 `PivotFieldDataDisplayFormat` 二次计算方式。  
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` 指定基字段在透视字段集合中的零基索引，供基准相关格式使用。  
- `GetBaseItemPositionType()` / `SetBaseItemPositionType()` 确定基项相对于当前项的定位方式，接受 `PivotItemPositionType::Next`、`PivotItemPositionType::Previous` 或 `PivotItemPositionType::Custom`。  
- `GetBaseItemIndex()` / `SetBaseItemIndex()` 指定零基基项索引，仅在定位类型为 `Custom` 时使用。  
调用 `ShowValuesAs` 后，请再次调用 `PivotTable.CalculateData()`，以便重新计算并重新渲染透视表主体，使更新后的配置生效。

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"ShowValuesAsPercentageOfTotal.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(1).GetPivotTables().Get(0);
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    // Read the current show-values settings
    PivotShowValuesSetting settings = dataField.GetShowValuesSetting();
    std::cout << "CalculationType: " << static_cast<int32_t>(settings.GetCalculationType()) << std::endl;
    std::cout << "BaseFieldIndex: " << settings.GetBaseFieldIndex() << std::endl;
    std::cout << "BaseItemPositionType: " << static_cast<int32_t>(settings.GetBaseItemPositionType()) << std::endl;
    std::cout << "BaseItemIndex: " << settings.GetBaseItemIndex() << std::endl;
    // Switch to a base-item calculation with the one-call method: difference
    // from the value of the previous item in the row field
    dataField.ShowValuesAs(PivotFieldDataDisplayFormat::DifferenceFrom,
        pivotTable.GetRowFields().Get(0).GetBaseIndex(), PivotItemPositionType::Previous, 0);
    pivotTable.CalculateData();
    // Note: the percentage number format saved by the previous example still
    // clings to the data field cells; the underlying values are now differences
    // Re-read the applied configuration
    std::cout << "CalculationType now: " << static_cast<int32_t>(dataField.GetShowValuesSetting().GetCalculationType()) << std::endl;
    workbook.Save(u"ShowValuesAsDifferenceFrom.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **相关文章**
- [在透视表中管理数值字段](/cells/zh/cpp/manage-value-fields/)
- [刷新透视表](/cells/zh/cpp/refresh-pivot-table/)
- [在透视表中应用样式](/cells/zh/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}