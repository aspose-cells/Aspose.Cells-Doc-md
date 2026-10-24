---
title: 在数据透视表中对透视字段分组
linktitle: 在数据透视表中对透视字段分组
description: 学习如何使用 Aspose.Cells for C++ 中的 PivotField.Group 和 PivotFieldGroupOptions 将数据透视表的行和列透视字段按日期周期（如月份和季度）以及数值范围进行分组。
keywords: Aspose.Cells, 数据透视表, 透视字段分组, PivotField.Group, PivotFieldGroupOptions, 日期分组, 数字分组, 月份, 季度, 数值范围, C++
type: docs
weight: 80
url: /zh/cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的用途场景**
- 对透视字段分组非常有用，当数据透视表的行或列字段包含许多不同的项目时，例如包含数百个日期的日期字段或包含许多分散值的数字字段。分组会将这些项目合并为有意义的分段：日期合并为月份、季度和年份，数字合并为诸如 0-1、2-3、4-5 的范围。这使得大型数据透视表更紧凑、更易于分析。Aspose.Cells 通过 `PivotField.Group()` 方法（按数据类型自动分组）和 `PivotField.Group(PivotFieldGroupOptions)`（自定义分组选项）提供此功能。
- 日期分组会将单个日期汇总到更大的周期，例如天、月、季度和年，并构建时间层次结构（例如年、季度、月）。随时间变化的趋势可以一目了然，每个周期级别在数据透视表的行或列区域中成为其自己的透视字段。
- 分组仅适用于放置在数据透视表行或列区域中的字段。数据（值）字段不能直接分组。要对这样的字段进行分组，必须先将其添加到数据透视表的行或列区域。

## **自动对透视字段分组**
无参数的 `PivotField.Group()` 重载会检查字段的数据类型并自动对其进行分组。仅包含日期（和空白）的字段按月份分组。仅包含数字（和空白）的字段使用自动间隔分组为数值区域。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    PivotField field = pt.GetRowFields().Get(0);
    field.Group();
    pt.CalculateData();
    wb.Save(u"outputAutoGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **使用自定义选项对透视字段分组**
`PivotFieldGroupOptions` 类提供自定义分组配置。对于日期字段，请设置 `StartDate`、`EndDate` 和 `GroupTypes`。对于数字字段，请设置 `StartNumber`、`EndNumber` 和 `Interval`。`NewPivotField` 属性控制分组是否在原始透视字段旁边创建新的透视字段（请参阅本文末尾的注意部分）。

### **按月和季度对日期字段分组**
以下示例将示例数据透视表的日期行字段按月份和季度在开始日期和结束日期之间进行分组。代码加载[示例 Excel 文件](sampleGroupPivotFieldsInPivotTable.xlsx)，执行分组，计算数据透视表数据，并保存分组结果。截图显示效果：日期行字段现在按季度和月份分组。
请注意，`options.GroupTypes` 中值的顺序将被忽略。无论组类型以何种顺序列出，分组字段始终从最大周期显示到最小周期：年、季度、月、日、小时、分钟、秒。在此示例中，月份在 `options.GroupTypes` 中列于季度之前，但季度显示为外部级别，月份显示为内部级别。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // 加载示例工作簿
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    // 访问第二个工作表及其数据透视表
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    // 按月份和季度对第一个行字段（日期字段）进行分组
    PivotFieldGroupOptions options;
    Date startDate{2008, 1, 1, 0, 0, 0, 0};
    Date endDate{2008, 9, 5, 0, 0, 0, 0};
    options.SetStartDate(startDate);
    options.SetEndDate(endDate);
    // 设置分组类型：月份和季度
    ArrayPtr<PivotGroupByType> groupTypes = ArrayPtr<PivotGroupByType>(new PivotGroupByType[2]{ PivotGroupByType::Months, PivotGroupByType::Quarters });
    options.SetGroupTypes(groupTypes);
    // 对第一个行字段应用分组
    PivotField rowField = pt.GetRowFields().Get(0);
    rowField.Group(options);
    // 计算数据透视表数据并保存输出文件
    pt.CalculateData();
    wb.Save(u"outputGroupPivotFieldsInPivotTable.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

![按月和季度分组的数据透视表](group-pivot-fields-in-the-pivot-table_1.png)

### **将数字字段分组到区域中**
示例数据透视表的 `FieldTwo` 最初是数据（值）字段。因为只有行或列字段可以分组，所以代码首先调用 `PivotTable.AddFieldToArea(PivotFieldType.Row, "FieldTwo")` 将 `FieldTwo` 移动到行区域，刷新数据透视表，然后使用 `StartNumber = 0`、`EndNumber = 5` 和 `Interval = 2` 将数字字段分组到 0-1、2-3 和 4-5 的区域中。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    pt.AddFieldToArea(PivotFieldType::Row, U16String("FieldTwo"));
    pt.CalculateData();
    PivotFieldGroupOptions options;
    options.SetStartNumber(0);
    options.SetEndNumber(5);
    options.SetInterval(2);
    pt.GetRowFields().Get(1).Group(options);
    pt.CalculateData();
    wb.Save(u"outputNumberGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **注意**

{{% alert color="primary" %}}
- `PivotField.GroupBy()` 方法重载已过时并从 API 中移除。`PivotField.Group()` 和 `PivotField.Group(PivotFieldGroupOptions)` 是替代方法。
- 在 Microsoft Excel 中，对数字字段进行分组会用分组区域替换原始透视字段，而对日期字段进行分组会在原始字段旁边创建新的透视字段（每个组级别一个，例如季度和月份）。从 Aspose.Cells 26.10 开始，`PivotField.Group()` 方法遵循与 Excel 相同的行为。`PivotFieldGroupOptions.NewPivotField` 属性用于与旧版本兼容：数字分组默认为 false，日期时间分组默认为 true；如果您希望日期分组替换原始透视字段而不是创建新的透视字段，请将其设置为 false。
- `PivotFieldGroupOptions.Interval` 属性仅对数字分组和按天分组的日期分组（例如将日期分组为 7 天周期）有效；当日期按月、季度或年分组时，该属性将被忽略。
{{% /alert %}}

## **相关文章**
- [在数据透视表中添加行和列字段](/cells/zh/cpp/pivot-table-add-row-and-column-fields/)
- [按标签或值筛选数据透视表](/cells/zh/cpp/filter-by-label-or-value-of-pivot-table/)
- [在数据透视表中添加页面字段](/cells/zh/cpp/add-page-field-in-pivot-table/)
- [对数据透视表应用样式](/cells/zh/cpp/apply-style-to-pivot-table/)
- [刷新数据透视表](/cells/zh/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}