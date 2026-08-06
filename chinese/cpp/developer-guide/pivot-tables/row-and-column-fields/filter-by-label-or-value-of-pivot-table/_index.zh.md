---
title: 按标签或值筛选数据透视表
linktitle: 按标签或值筛选数据透视表
description: Aspose.Cells for C++ 支持全面的数据透视表筛选功能。本文介绍如何使用标签筛选、日期筛选、值筛选、前 10 筛选以及通过隐藏或显示数据透视项来筛选数据透视表数据。
keywords: Aspose.Cells, C++ 库, 电子表格, 数据透视表, 筛选, 标签筛选, 值筛选, 日期筛选, 前 10 筛选, 数据透视项, 隐藏数据透视项
type: docs
weight: 10
url: /zh/cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells 提供了五种实用的策略来筛选数据透视表中显示的数据。您可以对基于文本的行或列字段应用标签筛选，在字段仅包含日期时间单元格或空值时使用日期筛选，对聚合数值应用值筛选，使用前 10 筛选按值字段排序，或者通过 `IsHidden` 属性手动隐藏和显示各个数据透视项。每种策略都通过 `PivotField` 和 `PivotItem` 类上专门的 API 来实现。
{{% /alert %}}
## **简介**
数据透视表是强大的分析工具，但原始汇总通常包含比您需要展示的信息多得多的内容。筛选是缩小数据透视表范围、只保留特定报告所需的行、列或值的主要机制。Aspose.Cells for C++ 完全镜像了 Microsoft Excel 中提供的筛选功能，并将其以编程方式公开，从而可以完全自动化报告生成过程。
本文涵盖以下筛选策略：
1. **标签筛选** — 根据文本标签筛选行或列字段项。
2. **日期筛选** — 筛选仅包含日期时间值（或空值）的行或列字段。
3. **值筛选** — 根据数据字段的聚合值筛选项。
4. **前 10 筛选** — 仅显示按值字段排序的前 N 项或后 N 项。
5. **隐藏/显示数据透视项** — 手动控制字段中每个单独项的可见性。
每种方法都使用 `PivotField` 类上的不同方法或 `PivotItem` 类上的属性。应用任何筛选后，必须在数据透视表上调用 `RefreshData()` 和 `CalculateData()`，以便缓存数据和计算值反映新的筛选状态。
## **标签筛选**
标签筛选允许您通过将行或列字段项的文本标题与模式进行比较来筛选这些项。当您只想显示名称以特定字母开头、包含特定单词或符合其他基于标题条件的项时，此功能非常有用。
Aspose.Cells 通过 `PivotField.FilterByLabel(PivotFilterType, const char16_t*)` 方法公开标签筛选功能。`PivotFilterType` 枚举包含以下值：`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` 等。第二个参数提供用于比较的标签字符串。
下面的示例加载包含现有数据透视表的工作簿，应用标签筛选使只有标题以指定前缀开头的项可见，刷新数据透视表，并保存结果。
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");

    // 加载包含数据透视表的现有工作簿
    Workbook wb(fileName);

    // 通过索引访问工作表（第一个工作表）
    Worksheet ws = wb.GetWorksheets().Get(0);

    // 通过索引访问数据透视表
    PivotTable pt = ws.GetPivotTables().Get(0);

    // 检索第一个行透视字段
    PivotField rowField = pt.GetRowFields().Get(0);

    // 应用标签筛选器 —— 仅显示标签以所提供前缀开头的行项
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));

    // 刷新并重新计算数据透视表数据，使筛选器生效
    pt.RefreshData();

    // 将工作簿保存回磁盘
    wb.Save(fileName);

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **日期筛选**
日期筛选允许您根据基于日期的条件（如今天、上周、本月、下个季度或特定日期范围）来缩小数据透视表的范围。它们是专用筛选，仅对存储日期时间信息的字段有效。
{{% alert color="primary" %}}
日期筛选仅在行区域或列区域仅包含日期时间单元格或空值时才有效。如果底层字段包含其他数据类型（如数字或文本），日期筛选将无法产生预期结果。在应用此筛选之前，请确保字段格式设置为日期，并且所有值都是有效的 `DateTime` 实例或空单元格。
{{% /alert %}}
Aspose.Cells 通过 `PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)` 方法公开日期筛选功能。`PivotFilterType` 枚举包含专门的日期值，例如 `Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear` 和 `Between`。根据所选的筛选类型，您传入一个或两个 `DateTime` 值（对于 `Between`，传入起始日期和结束日期）。
下面的示例加载一个数据透视表的行区域中包含日期字段的工作簿，应用日期筛选将可见项限制在特定日期范围内，刷新数据透视表，并保存工作簿。
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
        // 未找到源工作簿。
        Aspose::Cells::Cleanup();
        return -1;
    }

    // 加载包含数据透视表的现有工作簿
    Workbook workbook(U16String(inputPath.c_str()));

    // 通过索引访问包含数据透视表的工作表
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // 通过索引访问数据透视表
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // 从行区域获取日期透视字段
    PivotField dateField = pivotTable.GetRowFields().Get(0);

    // 定义 Between 筛选器的日期条件
    Date startDate{2020, 1, 1, 0, 0, 0, 0};
    Date endDate{2020, 12, 31, 0, 0, 0, 0};

    // 在透视字段上应用日期筛选器
    dateField.FilterByDate(PivotFilterType::DateBetween, startDate, endDate);

    // 刷新并重新计算数据透视表以使筛选器生效
    // 保存工作簿
    workbook.Save(U16String(outputPath.c_str()));

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **值筛选**
值筛选对数据透视表在数据区域中计算的聚合值进行操作。它们不匹配文本标签，而是将数值总数与阈值进行比较。典型用例包括仅显示销售总额超过目标金额的产品，或仅显示交易计数在某个范围内的区域。
Aspose.Cells 通过 `PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)` 方法公开值筛选功能。`filterType` 参数使用以下值：`ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual` 和 `ValueLessThanOrEqual`。`valueField` 参数指定应评估哪个数据字段，最后一个参数（或多个参数）提供阈值。
下面的示例加载一个包含数据透视表的工作簿，应用值筛选仅保留聚合销售额超过数值阈值的项，刷新数据透视表，并保存工作簿。
```cpp
#include "Aspose.Cells.h"
#include <cfloat>

using namespace Aspose::Cells;

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

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **前 10 筛选**
前 10 筛选是值筛选的一种专用形式，仅保留基于所选值字段的最高或最低 N 项。它通常用于排名报告，例如"按收入排名的前 10 个产品"或"按销售数量排名的后 5 个区域"。
{{% alert color="primary" %}}
前 10 筛选仅在数据透视表的数据区域中具有一个或多个值数据透视字段时才有效。如果没有至少一个值字段，则没有可用来对项进行排名的聚合度量，筛选将无法应用。
{{% /alert %}}
Aspose.Cells 通过 `PivotField.FilterTop10(int32_t itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)` 方法公开前 10 筛选功能。`itemCount` 参数定义要保留的项数，`isTop` 指示是保留顶部项（true）还是底部项（false），`valueField` 引用用于排名的数据字段，`filterType` 控制如何计算值（通常为 `Sum`，也可以是 `Count` 和 `Percent`）。
下面的示例加载一个包含具有值字段的数据透视表的工作簿，应用前 10 筛选仅保留按销售额总和排名的最高 10 项，刷新数据透视表，并保存工作簿。
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

    rowField.FilterTop10(10, PivotFilterType::Sum, true, valueFieldIndex);

    workbook.Save(outputPath);

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **通过隐藏或显示数据透视项进行筛选**
除了结构化的筛选 API 外，Aspose.Cells 还允许您直接控制每个单独数据透视项的可见性。通过遍历 `PivotField` 的 `PivotItems` 集合并切换 `IsHidden` 属性，您可以选择性地隐藏特定项，而无需应用基于公式的筛选。设置 `IsHidden = true` 会从数据透视表中隐藏该项；设置 `IsHidden = false` 会取消隐藏并使其再次可见。
当筛选规则不规则或特定于项时，此方法非常有用，例如隐藏不应出现在特定报告中的少量命名类别。下面的示例加载一个数据透视表，按名称隐藏特定项，演示如何取消隐藏它，刷新数据透视表，并保存工作簿。
```cpp
#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // 加载包含数据透视表的现有工作簿
    Workbook workbook(u"pivot_table_sample.xlsx");

    // 访问包含数据透视表的第一个工作表
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // 通过索引访问数据透视表（工作表上的第一个数据透视表）
    PivotTable pivotTable = sheet.GetPivotTables().Get(0);

    // 检索目标 PivotField（我们将在其中隐藏/显示项目的第一行标签字段）
    PivotField pivotField = pivotTable.GetRowFields().Get(0);

    // 遍历所选 PivotField 的 PivotItems 集合
    int itemCount = pivotField.GetPivotItems().GetCount();
    for (int i = 0; i < itemCount; i++)
    {
        PivotItem item = pivotField.GetPivotItems().Get(i);

        U16String name = item.GetName();
        std::string nameStr = name.ToUtf8();

        // 隐藏符合特定名称/条件的数据透视表项
        if (nameStr == "Item1" || nameStr == "Item2")
        {
            item.SetIsHidden(true);
        }

        // 演示取消隐藏：重新显示之前隐藏的数据透视表项
        if (nameStr == "Item3")
        {
            item.SetIsHidden(false);
        }
    }

    // 刷新并重新计算数据透视表以使更改生效
    pivotTable.CalculateData();

    // 保存工作簿 — 隐藏的项目保留在底层数据中
    // 但从显示的数据透视表输出中排除
    workbook.Save(u"output_pivot_filtered.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **总结**
Aspose.Cells for C++ 提供了一整套与 Microsoft Excel 中所提供的数据透视表筛选功能相匹配的功能。标签筛选、日期筛选和值筛选涵盖了最常见的分析场景，而前 10 筛选处理排名报告。当筛选规则不规则时，`PivotItem.IsHidden` 属性提供了一种灵活的、项级别的备用方案。结合这些策略——例如先应用标签筛选然后隐藏特定项——您可以完全从代码构建精准定位的数据透视表报告。
{{< app/cells/assistant language="cpp" >}}