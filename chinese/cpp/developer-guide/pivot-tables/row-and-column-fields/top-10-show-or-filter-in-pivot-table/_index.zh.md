---
title: 在数据透视表中显示或筛选前 10 项
linktitle: 在数据透视表中显示或筛选前 10 项
description: 了解如何使用 Aspose.Cells for C++ 仅显示数据透视表字段中排名最高或最低的项。本文介绍 Excel 97-2003 Top10AutoShow 方法、使用 GetTop10AutoShowSettings 读取选项，以及通过 FilterTop10 实现 Excel 2007-365 前 10 项筛选。
keywords: Aspose.Cells, C++, 数据透视表, 前 10 项, 自动显示, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, GetTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField
type: docs
weight: 20
url: /zh/cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
如果行字段包含数十个项，列出该字段所有项的数据透视表可能难以阅读。“前 10 项”报表仅保留排名最高或最低的项，这正符合排名分析报告的需求，例如“按收入排名前 5 的产品”或“销售量排名后 3 的地区”。Aspose.Cells 支持两种机制来实现此目的，分别对应 Microsoft Excel 的两代版本。
- **Excel 97-2003 自动显示** — `PivotField.Top10AutoShow()` 方法。这是直接存储在数据透视表字段上的经典“显示前/后 N 项”设置。由于它是原始数据透视表格式的一部分，因此在所有新旧 Excel 版本中均可用。
- **Excel 2007-365 前 10 项筛选** — `PivotField.FilterTop10()` 方法。这是字段菜单“值筛选”下的现代“前 10 项”值筛选。它以 `PivotFilter` 对象的形式存储并附加到字段，支持按项数或百分比进行排名。

## **Excel 97-2003 中显示前 10 项（Top10AutoShow）**
通过一次调用 `PivotField.Top10AutoShow(bool isAutoShow, bool isTop, int32_t count, int32_t rankBy)` 即可配置经典自动显示功能：
- `isAutoShow` — 启用或禁用字段上的自动显示设置。
- `isTop` — `true` 保留排名最高的项（前），`false` 保留排名最低的项（后）。
- `count` — 要保留的项数，例如经典前 10 项报表使用 10。
- `rankBy` — 用于依据其值对各项进行排名的**数据字段**的从零开始的索引。传入 -1 后，可依据字段自身对各项进行排名。
排名依据可以是值字段，也可以是字段自身。以下介绍两种常见用法。

### **按值字段排名**
可使用常规值字段（例如 `Sales` 的总和）对行字段中的项进行排名。以下示例构建一个包含一个行字段 (`Sport`) 和一个数据字段 (`Sales`) 的数据透视表，然后显示销售额排名前 2 的运动项目。由于“`Sales` 的总和”是索引为 0 的数据字段，因此 `rankBy` 为 0。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // 显示按“Sales 的总和”排名前 2 的项目（数据字段索引 0）
    sportField.Top10AutoShow(true, true, 2, 0);
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-by-value-field.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### **按字段自身排名**
字段本身也可以作为排名依据——只需将 -1 作为 `rankBy` 传入。此变体不需要额外的数据字段；该字段只需位于行（或列）区域。以下示例显示按字段自身进行排名后排名最低的 3 个运动项目。保存此设置时，数据透视表 XML 中会省略 `rankBy` 属性，因为 -1 是该格式的默认值，并且 `GetTop10AutoShowSettings().GetRankBy()` 返回 -1。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // 显示按字段本身排名的后 3 个项目（rankBy = -1）
    sportField.Top10AutoShow(true, false, 3, -1);
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-by-field-itself.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **读取当前选项（GetTop10AutoShowSettings）**
`PivotField.GetTop10AutoShowSettings()` 方法返回一个 `PivotFieldTop10AutoShowSettings` 对象，该对象提供字段中当前存储的自动显示选项。可使用该对象检查现有工作簿或刚配置的数据透视表将如何显示其中的项；同样可以使用这种方式检查从文件加载的工作簿。

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"output-top10-by-value-field.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(0).GetPivotTables().Get(0);
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    PivotFieldTop10AutoShowSettings settings = sportField.GetTop10AutoShowSettings();
    std::cout << "AutoShow enabled: " << settings.IsAutoShow() << std::endl;
    std::cout << "Direction: " << (settings.IsTop() ? "Top" : "Bottom") << std::endl;
    std::cout << "Item count: " << settings.GetAutoShowCount() << std::endl;
    std::cout << "Ranking data field index: " << settings.GetRankBy() << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

这四个成员分别对应写入数据透视表 XML 的经典自动显示属性（`autoShow`、`topAutoShow`、`itemPageCount`、`rankBy`），因此读取的值就是所有 Excel 版本都会遵循的值。

## **注意**

{{% alert color="primary" %}}
- `PivotField` 的直接属性 `IsAutoShow`、`IsAscendShow`、`GetAutoShowCount` 和 `GetAutoShowField` 已弃用。请改用 `PivotFieldTop10AutoShowSettings` 对象：`IsAutoShow` 对应 `GetTop10AutoShowSettings().IsAutoShow()`，`IsAscendShow` 对应 `GetTop10AutoShowSettings().IsTop()`，`GetAutoShowCount` 对应 `GetTop10AutoShowSettings().GetAutoShowCount()`，`GetAutoShowField` 对应 `GetTop10AutoShowSettings().GetRankBy()`。更改设置时，请使用受支持的 `Top10AutoShow()` 方法。
- `Top10AutoShow` 适用于行字段和列字段。仅位于页字段（筛选）区域中的字段无法通过这种方式进行排名，因为其中的项不会排列在数据透视表主体中。
{{% /alert %}}

## **Excel 2007-365：前 10 项筛选（FilterTop10）**
现代 Excel 版本在字段菜单（“值筛选”、“前 10 项……”）中提供前 10 项值筛选。Aspose.Cells 使用 `PivotField.FilterTop10(int32_t valueFieldIndex, PivotFilterType type, bool isTop, int32_t itemCount)` 方法实现此筛选，该方法返回创建的 `PivotFilter`：
- `valueFieldIndex` — 用于根据聚合值对项进行排名的数据字段的从零开始的索引。
- `type` — 指定 `itemCount` 的含义。`PivotFilterType::Count` 保留固定数量的项（对应对话框中的“项目”选项）。`PivotFilterType::Percent` 保留指定百分比的项，因此 `itemCount` 就是该百分比——例如，30 表示保留前 30% 的项。`PivotFilterType::Sum` 按累计值覆盖率进行排名。
- `isTop` — `true` 表示“前”，`false` 表示“后”。
- `itemCount` — 表示“前 N 项”中的 N；其单位取决于 `type`。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // 前 10 项筛选——按“销售总和”（数据字段索引 0）保留前 2 个项
    PivotFilter filter = sportField.FilterTop10(0, PivotFilterType::Count, true, 2);
    // 如果改用基于百分比的筛选，则保留前 30% 的项：
    // sportField.FilterTop10(0, PivotFilterType::Percent, true, 30);
    pivotTable.GetPivotCache().Refresh();
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-filter.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}
`Top10AutoShow` 和 `FilterTop10` 是两个彼此独立的功能。自动显示会将经典 `autoShow` 属性写入数据透视表字段，并且从 Excel 97 开始的所有 Excel 版本都会遵循该属性。`FilterTop10` 会写入现代 `PivotFilter` 条目，这需要 Excel 2007 或更高版本。在较旧 Excel 版本中打开工作簿时，使用现代筛选器的数据透视表会回退为显示所有项。对于必须通过旧版工具进行往返读写的文档，应优先使用 `Top10AutoShow`；对于现代工作簿，应优先使用 `FilterTop10`，因为它可与其他值筛选组合使用。
{{% /alert %}}

## **相关文章**
- [按标签或值筛选数据透视表](/cells/zh/cpp/filter-by-label-or-value-of-pivot-table/)
- [添加数据透视表行字段和列字段](/cells/zh/cpp/pivot-table-add-row-and-column-fields/)
- [在数据透视表中对数据透视表字段进行分组](/cells/zh/cpp/group-pivot-fields-in-the-pivot-table/)
- [刷新数据透视表](/cells/zh/cpp/refresh-pivot-table/)
- [在数据透视表中添加页字段](/cells/zh/cpp/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="cpp" >}}