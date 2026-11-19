---
title: 在 Aspose.Cells for C++ 的数据透视表中使用“值显示方式”
linktitle: 在 Aspose.Cells for C++ 的数据透视表中使用“值显示方式”
description: 使用 Aspose.Cells for C++ 将数据透视表的值字段显示为占总计的百分比、与基准项的差异、累计总计、排名等。
keywords: Aspose.Cells, C++, 数据透视表, 值显示方式, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, ShowValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /zh/cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
数据透视表通常使用 `Sum` 或 `Count` 等汇总函数对每个值字段进行汇总。Excel 的 **值显示方式** 功能会将每个显示结果替换为基于该汇总结果执行的二次计算，例如占总计的百分比、累计总计、与所选基准项的差异或排名，从而无需使用辅助公式或计算列即可执行比较分析。
典型用途包括占比分析，例如显示占行总计、列总计或总计的百分比；在期间字段中使用累计总计进行累计报告；针对基准项使用“与基准项的差异”或“与基准项的百分比差异”进行差异分析；以及按从小到大或从大到小对值进行排名。
在 Aspose.Cells for C++ 中，`PivotShowValuesAsType` 枚举用于选择二次计算。`PivotField.GetShowValuesSetting()` 访问器返回 `PivotShowValuesSetting` 对象，其 `SetShowValuesAs`、`SetBaseFieldIndex` 和 `SetBaseItemIndex` 方法用于配置相应行为；便捷方法 `PivotField.ShowValuesAs(...)` 通过一次调用应用相同的设置。请将这些设置应用于通过 `PivotTable.GetDataFields()` 获取的值字段（或数据字段）。

## **`PivotShowValuesAsType` 枚举成员**
值字段保留其汇总函数，例如 `Sum` 或 `Count`，而“值显示方式”仅改变汇总值的显示方式。
除了直接写入 `PivotShowValuesSetting` 的各项值（见最后一节）外，还有一个通过一次调用即可应用相同配置的便捷方法。该方法有两种形式：一种通过索引指定基准字段和基准项，另一种通过名称指定：

```cpp
void ShowValuesAs(PivotShowValuesAsType showValuesAsType, int32_t baseField, int32_t baseItem);
void ShowValuesAs(PivotShowValuesAsType showValuesAsType, const U16String& baseField, const U16String& baseItem);
// index form: PivotShowValuesAsType::PercentageOfTotal, 0, 0
// name form:  PivotShowValuesAsType::PercentageOf, u"Fruit", u"Apple"
```

| 参数 | 含义 | 何时必需 |
| --- | --- | --- |
| `showValuesAsType` | 要应用的 `PivotShowValuesAsType` 二次计算。 | 始终需要。 |
| `baseField` | 基准字段在数据透视表基准字段中的从零开始的索引（例如基准项所属行字段的索引），或者在使用名称的形式下指定基准字段的名称。 | 以下八种基于基准的格式（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`、`RunningTotalIn`、`PercentageOfParentTotal`、`PercentageOfRunningTotalIn`、`RankSmallestToLargest`、`RankLargestToSmallest`）；对于其他所有格式，请传入 `0`（在使用名称的形式下则传入空的 `U16String`）。 |
| `baseItem` | 基准项的从零开始的索引，其中包含两个哨兵值：`-1` 表示前一项，`-2` 表示后一项（C++ API 未为这些哨兵值定义命名常量，请传入字面值）。在使用名称的形式下，应改为传入基准项的标题；当所选格式不需要基准项时，传入空的 `U16String`。 | 只有三种基于基准项的格式（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`）会使用基准项进行计算；五种基于字段的格式（`RunningTotalIn`、`PercentageOfParentTotal`、`PercentageOfRunningTotalIn` 和两种排名格式）会忽略该参数——请传入 `0` 或空的 `U16String`。 |

| 计算类型 | 行为 | 基准项参数 |
| --- | --- | --- |
| `Normal` | 不执行二次计算；按原值显示汇总值（默认）。 | — |
| `DifferenceFrom` | 将值显示为与基准字段中基准项的值之差。 | `baseField` + `baseItem`（索引或标题，或前一/后一项哨兵值） |
| `PercentageOf` | 将值显示为基准字段中基准项值的百分比。 | `baseField` + `baseItem`（索引或标题，或前一/后一项哨兵值） |
| `PercentageDifferenceFrom` | 将值显示为与基准字段中基准项的值之间的百分比差异。 | `baseField` + `baseItem`（索引或标题，或前一/后一项哨兵值） |
| `RunningTotalIn` | 按基准字段中项目的顺序显示累计总计。 | `baseField`（其项目顺序决定累计算方式的字段） |
| `PercentageOfRow` | 将值显示为行总计的百分比。 | — |
| `PercentageOfColumn` | 将值显示为列总计的百分比。 | — |
| `PercentageOfTotal` | 将值显示为总计的百分比。 | — |
| `Index` | 使用 Excel 索引公式（(值 * 总计) / (行总计 * 列总计)）显示该值。 | — |
| `PercentageOfParentRowTotal` | 将值显示为其父级行总计的百分比（适用于嵌套行字段）。 | — |
| `PercentageOfParentColumnTotal` | 将值显示为其父级列总计的百分比（适用于嵌套列字段）。 | — |
| `PercentageOfParentTotal` | 将值显示为其父级总计的百分比。 | `baseField`（作为总计参考值的父级字段） |
| `PercentageOfRunningTotalIn` | 将值显示为基准字段中累计总计的百分比。 | `baseField`（累计字段） |
| `RankSmallestToLargest` | 按值从小到大进行排名，最小值为 1。 | `baseField`（其项目定义排名范围的字段） |
| `RankLargestToSmallest` | 按值从大到小进行排名，最大值为 1。 | `baseField`（其项目定义排名范围的字段） |

{{% alert color="primary" %}}
`ShowValuesAs(...)` 会写入 `PivotShowValuesSetting` 对象中的各项值（`ShowValuesAs`、`BaseFieldIndex` 和 `BaseItemIndex`）——该方法与设置对象是配置同一状态的两种方式，对应于 Excel“值显示方式”对话框中的基准字段和基准项选择器。
{{% /alert %}}

## **将值显示为总计的百分比**
调用 `PivotField.ShowValuesAs` 方法并传入 `PivotShowValuesAsType::PercentageOfTotal`，即可将每个值字段单元格（包括总计单元格）转换为其在总计中所占的份额。因此，显示的数字表示其在完整结果集中的比例。此格式仅以总计为基准衡量每个值，因此不需要基准字段或基准项——末尾参数（`0`、`0`）只是占位符，该格式会忽略它们，如上表所示。

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
    // base arguments (0, 0) are placeholders the format ignores
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    dataField.ShowValuesAs(PivotShowValuesAsType::PercentageOfTotal, 0, 0);
    pivotTable.CalculateData();
    // Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
    workbook.Save(u"ShowValuesAsPercentageOfTotal.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **获取并配置 `PivotField.ShowValuesSetting`**
通过 `PivotField.GetShowValuesSetting()` 读取当前配置：该访问器返回该字段的 `PivotShowValuesSetting` 对象，其读取方法描述当前生效的“值显示方式”计算。要更改配置，请调用 `PivotField.ShowValuesAs` 方法——该方法一次调用即可写入所有设置，因此无需逐项设置各值。
`PivotShowValuesSetting` 对象公开 `ShowValuesAs` 写入的状态：
- `GetShowValuesAs()` / `SetShowValuesAs()` 用于选择 `PivotShowValuesAsType` 二次计算。
- `GetBaseFieldIndex()` / `SetBaseFieldIndex()` 用于指定基准字段在数据透视表字段中的从零开始的索引。基于基准的格式会使用该索引。
- `GetBaseItemIndex()` / `SetBaseItemIndex()` 用于指定基准项：可以是特定数据透视表项的从零开始的索引，也可以是两个哨兵值之一——`-1` 表示前一项，`-2` 表示后一项（C++ API 未为这些哨兵值定义命名常量）。基于基准项的格式会使用该值。
- `GetBaseFieldName()` 和 `GetBaseItemCaption()` 是只读视图，用于报告解析后的基准字段名称和基准项标题；例如，选择前一项哨兵值后，`GetBaseItemCaption()` 返回 `(previous)`。
调用 `ShowValuesAs` 后，再次调用 `PivotTable.CalculateData()`，以便使用更新后的配置重新计算并重新呈现数据透视表主体。

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
    std::cout << "ShowValuesAs: " << static_cast<int32_t>(settings.GetShowValuesAs()) << std::endl;
    std::cout << "BaseFieldIndex: " << settings.GetBaseFieldIndex() << std::endl;
    std::cout << "BaseItemIndex: " << settings.GetBaseItemIndex() << std::endl;
    std::cout << "BaseFieldName: " << settings.GetBaseFieldName().ToUtf8() << std::endl;
    std::cout << "BaseItemCaption: " << settings.GetBaseItemCaption().ToUtf8() << std::endl;
    // Switch to a base-item calculation with the one-call method: difference
    // from the value of the previous item in the row field
    // (-1 is the previous-item sentinel; no named constant exists in C++)
    dataField.ShowValuesAs(PivotShowValuesAsType::DifferenceFrom,
        pivotTable.GetRowFields().Get(0).GetBaseIndex(), -1);
    pivotTable.CalculateData();
    // Note: the percentage number format saved by the previous example still
    // clings to the data field cells; the underlying values are now differences
    // Re-read the applied configuration
    std::cout << "ShowValuesAs now: " << static_cast<int32_t>(dataField.GetShowValuesSetting().GetShowValuesAs()) << std::endl;
    std::cout << "BaseItemCaption now: " << dataField.GetShowValuesSetting().GetBaseItemCaption().ToUtf8() << std::endl;
    workbook.Save(u"ShowValuesAsDifferenceFrom.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **相关文章**
- [管理数据透视表中的值字段](/cells/zh/cpp/manage-value-fields/)
- [刷新数据透视表](/cells/zh/cpp/refresh-pivot-table/)
- [为数据透视表应用样式](/cells/zh/cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="cpp" >}}