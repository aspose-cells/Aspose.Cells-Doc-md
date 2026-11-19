---
title: 按标签或值筛选数据透视表
linktitle: 按标签或值筛选数据透视表
description: Aspose.Cells for C++ 支持全面的数据透视表筛选功能。本文介绍如何使用标签筛选、日期筛选、值筛选、前 10 项筛选，以及通过隐藏或取消隐藏数据透视项来筛选数据透视表中的数据。
keywords: Aspose.Cells, C++ 库, 电子表格, 数据透视表, 筛选, 标签筛选, 值筛选, 日期筛选, 前 10 项筛选, 数据透视项, 隐藏数据透视项
type: docs
weight: 10
url: /zh/cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供五种实用策略，用于筛选数据透视表中显示的数据。您可以对基于文本的行字段或列字段应用标签筛选；当字段仅包含日期时间单元格或空白值时使用日期筛选；根据汇总数值应用值筛选；使用前 10 项筛选按值字段对项目进行排名；或使用 `IsHidden` 属性手动隐藏和取消隐藏单个数据透视项。每种策略均通过 `PivotField` 和 `PivotItem` 类上的专用 API 提供。
{{% /alert %}}

## **简介**
数据透视表是功能强大的分析工具，但未经筛选的汇总结果通常包含的信息远超实际展示所需。筛选是将数据透视表限定为特定报表所需行、列或值的主要机制。Aspose.Cells for C++ 提供与 Microsoft Excel 相同的筛选功能，并通过编程接口开放这些功能，从而实现报表生成的完全自动化。
本文介绍以下筛选策略：
1. **标签筛选** — 根据文本标签筛选行字段或列字段中的项目。
2. **日期筛选** — 筛选仅包含日期时间值（或空白值）的行字段或列字段。
3. **值筛选** — 根据数据字段的汇总值筛选项目。
4. **前 10 项筛选** — 仅显示按值字段排名的前 N 个或后 N 个项目。
5. **隐藏/取消隐藏数据透视项** — 手动控制字段中各个项目的可见性。
每种方法均使用 `PivotField` 类上的不同方法或 `PivotItem` 类上的属性。应用任一筛选后，必须在数据透视表上调用 `GetPivotCache().Refresh()`，以使缓存数据和计算值反映新的筛选状态。

## **标签筛选**
标签筛选器允许您通过将行字段或列字段中项目的文本标题与模式进行比较来筛选项目。当您希望仅显示名称以特定字母开头、包含特定单词或符合其他基于标题条件的项目时，此功能非常有用。
Aspose.Cells 通过 `PivotField.FilterByLabel(PivotFilterType, const char16_t*)` 方法提供标签筛选功能。`PivotFilterType` 枚举包含 `CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` 等值。第二个参数提供用于比较的标签字符串。
以下示例加载一个包含现有数据透视表的工作簿，应用标签筛选器，使标题以指定前缀开头的项目保持可见，刷新数据透视表并保存结果。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");
    // Load the existing workbook containing a pivot table
    Workbook wb(fileName);
    // Access the worksheet by index (first worksheet)
    Worksheet ws = wb.GetWorksheets().Get(0);
    // Access the pivot table by index
    PivotTable pt = ws.GetPivotTables().Get(0);
    // Retrieve the first row PivotField
    PivotField rowField = pt.GetRowFields().Get(0);
    // Apply the label filter — show only row items whose labels begin with the supplied prefix
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));
    // Refresh and recalculate the pivot table data so the filter takes effect
    pt.GetPivotCache().Refresh();
    // Save the workbook back to disk
    wb.Save(fileName);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **日期筛选**
日期筛选器可让您根据今天、上周、本月、下个季度或特定日期范围等日期条件筛选数据透视表。它们仅适用于存储日期时间信息的字段。

{{% alert color="primary" %}}
日期筛选器仅适用于行区域或列区域只包含日期时间单元格或空白值的情况。如果基础字段包含数字或文本等其他数据类型，日期筛选器将不会产生预期结果。应用此筛选器前，请确保字段已设置为日期格式，且所有值均为有效的 `DateTime` 实例或空单元格。
Aspose.Cells 通过 `PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)` 方法提供日期筛选功能。`PivotFilterType` 枚举包含 `Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear` 和 `Between` 等专用日期值。根据所选筛选器类型，传入一个或两个 `DateTime` 值（对于 `Between`，传入开始日期和结束日期）。
以下示例加载一个工作簿，其中数据透视表的行区域包含日期字段；随后应用日期筛选器，将可见项目限定在特定日期范围内，刷新数据透视表并保存工作簿。
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    std::string inputPath = "sample.xlsx";
    std::string outputPath = "output_filtered.xlsx";
    if (!std::filesystem::exists(inputPath))
    {
        // Source workbook not found.
        Aspose::Cells::Cleanup();
        return -1;
    }
    // Load the existing workbook that contains the pivot table
    Workbook workbook(U16String(inputPath.c_str()));
    // Access the worksheet that holds the pivot table (by index)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Access the pivot table by index
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    // Retrieve the date PivotField from the row area
    PivotField dateField = pivotTable.GetRowFields().Get(0);
    // Define the date criterion for the Between filter
    Date startDate{2020, 1, 1, 0, 0, 0, 0};
    Date endDate{2020, 12, 31, 0, 0, 0, 0};
    // Apply the date filter on the pivot field
    dateField.FilterByDate(PivotFilterType::DateBetween, startDate, endDate);
    // Refresh and recalculate the pivot table so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    // Persist the workbook
    workbook.Save(U16String(outputPath.c_str()));
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **值筛选**
值筛选器根据数据透视表在数据区域中计算的汇总值进行筛选。它们不匹配文本标签，而是将数值总计与阈值进行比较。典型用例包括仅显示销售总额超过目标金额的产品，或仅显示交易次数落在一定数值范围内的区域。
Aspose.Cells 通过 `PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)` 方法提供值筛选功能。`filterType` 参数可取 `ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual` 和 `ValueLessThanOrEqual` 等值。`valueField` 参数指定要评估的数据字段，最后一个参数提供用于比较的阈值。
以下示例加载一个包含数据透视表的工作簿，应用值筛选器，仅保留汇总销售额超过数值阈值的项目，刷新数据透视表并保存工作簿。

```cpp
#include "Aspose.Cells.h"
#include <cfloat>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sample.xlsx");
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    PivotField rowField = pivotTable.GetRowFields().Get(0);
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    int dataFieldIndex = -1;
    int dataFieldCount = pivotTable.GetDataFields().GetCount();
    for (int i = 0; i < dataFieldCount; i++)
    {
        PivotField current = pivotTable.GetDataFields().Get(i);
        if (current.GetName() == dataField.GetName())
        {
            dataFieldIndex = i;
            break;
        }
    }
    if (dataFieldIndex >= 0)
    {
        rowField.FilterByValue(dataFieldIndex, PivotFilterType::ValueGreaterThan, 5000, DBL_MAX);
    }
    // Refresh and recalculate the pivot table so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **前 10 项筛选**
前 10 项筛选器是值筛选器的一种专用形式，它根据选定的值字段，仅保留汇总值最高或最低的 N 个项目。常用于生成“按收入排名前 10 的产品”或“按销售数量排名后 5 的区域”等排名报表。

{{% alert color="primary" %}}
前 10 项筛选器仅在数据透视表的数据区域中至少包含一个值字段时有效。如果不存在值字段，就没有可用于对项目进行排名的汇总度量，因而无法应用该筛选器。
Aspose.Cells 通过 `PivotField.FilterTop10(int32_t valueFieldIndex, PivotFilterType type, bool isTop, int32_t itemCount)` 方法提供前 10 项筛选功能。`valueFieldIndex` 参数是数据字段的索引，其汇总值用于对项目进行排名；`type` 指定 `itemCount` 的单位（`PivotFilterType::Count` 保留固定数量的项目，`PivotFilterType::Percent` 保留项目的一定百分比，因此 `itemCount` 本身就是百分比）；`isTop` 指示保留排名靠前的项目（true）还是排名靠后的项目（false）；`itemCount` 定义要保留的项目数量或百分比。
以下示例加载一个工作簿，其中数据透视表包含值字段；随后应用前 10 项筛选器，仅保留按销售总额排名前 10 的项目，刷新数据透视表并保存工作簿。
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <stdexcept>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    U16String inputPath(u"input.xlsx");
    U16String outputPath(u"output.xlsx");
    Workbook workbook(inputPath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    if (pivotTable.GetDataFields().GetCount() == 0) {
        throw std::runtime_error("Pivot table has no value (data) PivotField.");
    }
    PivotField valueField = pivotTable.GetDataFields().Get(0);
    PivotField rowField = pivotTable.GetRowFields().Get(0);
    int valueFieldIndex = 0;
    rowField.FilterTop10(valueFieldIndex, PivotFilterType::Count, true, 10);
    // Refresh the pivot table data and recalculate it so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    workbook.Save(outputPath);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **通过隐藏或取消隐藏数据透视项进行筛选**
除结构化筛选 API 外，Aspose.Cells 还允许您直接控制每个数据透视项的可见性。通过遍历 `PivotField` 的 `PivotItems` 集合并切换 `IsHidden` 属性，您可以在不应用基于公式的筛选器的情况下，选择性地隐藏特定项目。将 `IsHidden = true` 会从数据透视表中隐藏该项目；将 `IsHidden = false` 会取消隐藏该项目，使其重新可见。
当筛选规则因项目而异或不符合标准筛选模式时，此方法非常有用。例如，可以隐藏不应出现在特定报表中的少量指定类别。下面的示例加载一个包含数据透视表的工作簿，按名称隐藏特定项目，演示如何取消隐藏该项目，刷新数据透视表并保存工作簿。

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Load an existing workbook containing a pivot table
    Workbook workbook(u"pivot_table_sample.xlsx");
    // Access the first worksheet which contains the pivot table
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    // Access the pivot table by index (the first pivot table on the sheet)
    PivotTable pivotTable = sheet.GetPivotTables().Get(0);
    // Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
    PivotField pivotField = pivotTable.GetRowFields().Get(0);
    // Iterate through the PivotItems collection of the selected PivotField
    int itemCount = pivotField.GetPivotItems().GetCount();
    for (int i = 0; i < itemCount; i++)
    {
        PivotItem item = pivotField.GetPivotItems().Get(i);
        U16String name = item.GetName();
        std::string nameStr = name.ToUtf8();
        // Hide pivot items that match a specific name/criterion
        if (nameStr == "Item1" || nameStr == "Item2")
        {
            item.SetIsHidden(true);
        }
        // Demonstrate unhiding: re-show a previously hidden pivot item
        if (nameStr == "Item3")
        {
            item.SetIsHidden(false);
        }
    }
    // Refresh and recalculate the pivot table so changes take effect
    pivotTable.GetPivotCache().Refresh();
    // Save the workbook — hidden items stay in the underlying data
    // but are excluded from the displayed pivot table output
    workbook.Save(u"output_pivot_filtered.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **总结**
Aspose.Cells for C++ 提供了一套完整的数据透视表筛选功能，与 Microsoft Excel 中的功能一致。标签筛选、日期筛选和值筛选涵盖最常见的分析场景，前 10 项筛选则用于排名报表。当筛选规则因项目而异或不符合标准筛选模式时，`PivotItem.IsHidden` 属性提供按项目控制的灵活替代方案。将这些策略结合使用（例如，先应用标签筛选，再隐藏特定项目），您便可以通过代码构建内容精确、面向特定目标的数据透视表报表。

## 相关文章
- [插入数据透视表](/cells/zh/cpp/create-pivot-table/)
- [在 Aspose.Cells for C++ 中添加数据透视表行字段和列字段](/cells/zh/cpp/pivot-table-add-row-and-column-fields/)
- [在 Aspose.Cells for C++ 中向数据透视表添加筛选字段](/cells/zh/cpp/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for C++ 中管理数据透视表值字段](/cells/zh/cpp/manage-value-fields/)
- [在 Aspose.Cells for C++ 中刷新数据透视表和数据透视缓存](/cells/zh/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}