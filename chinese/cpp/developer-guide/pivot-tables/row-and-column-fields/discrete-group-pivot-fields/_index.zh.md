---
title: 数据透视表字段项目的离散分组
linktitle: 离散分组
description: 了解如何在 Aspose.Cells for C++ 中使用 DiscreteGroupItem 和 PivotFieldGroupOptions.DiscreteGroupItems，将数据透视表字段项目分组为水果和蔬菜等自定义命名组。
keywords: Aspose.Cells for C++, 数据透视表, 离散分组, DiscreteGroupItem, PivotFieldGroupOptions, 分组数据透视表项目, 自定义组, PivotField.Group, C++, Excel 数据透视表
type: docs
weight: 90
url: /zh/cpp/discrete-group-pivot-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的用法场景**
- 自动分组根据数据类型对项目进行归类，例如将日期按月份和季度分组，或将数字归入数值区间。离散分组解决的是相反的问题：将特定的、互不相关的项目归入自定义命名组，例如将产品分为水果和蔬菜、将商店按地区分组，或将账户按分区分组。Aspose.Cells 通过 `DiscreteGroupItem` 类和 `PivotFieldGroupOptions.DiscreteGroupItems` 属性提供离散分组功能。
- `DiscreteGroupItem` 包含一个组名称以及归属于该组的项目。可以通过两种方式标识这些项目：按名称（`DiscreteGroupItem("fruit", { "grape", "cherry" })`）或按其在源数据中从 0 开始的位置（`DiscreteGroupItem("fruit", { 0, 3 })`）。两种形式产生的结果相同。
- 要对数据透视表行区域或列区域中的字段应用离散分组，只需将选项传递给 `PivotField.Group(PivotFieldGroupOptions)`。

## **按项目名称对数据透视表字段项目进行分组**
以下示例构建一个小型销售列表（产品、日期和金额），并基于该列表创建数据透视表，其中 `product` 位于行区域，`date` 位于列区域，`amount` 位于数据区域；随后按项目名称定义两个自定义组，即水果（葡萄、樱桃）和蔬菜（胡萝卜、土豆）。结果呈现两级行布局：组名称位于外层，原始项目嵌套在其下，因此可以按自定义组和单个项目分别查看趋势。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(0, 0).PutValue(u"product");
    cells.Get(1, 0).PutValue(u"grape");
    cells.Get(2, 0).PutValue(u"carrot");
    cells.Get(3, 0).PutValue(u"potato");
    cells.Get(4, 0).PutValue(u"cherry");
    Style dateStyle = wb.CreateStyle();
    dateStyle.SetCustom(u"m/d/yyyy");
    cells.Get(0, 1).PutValue(u"date");
    cells.Get(1, 1).PutValue(Date{2021, 2, 5, 0, 0, 0, 0});
    cells.Get(2, 1).PutValue(Date{2022, 3, 8, 0, 0, 0, 0});
    cells.Get(3, 1).PutValue(Date{2023, 4, 10, 0, 0, 0, 0});
    cells.Get(4, 1).PutValue(Date{2024, 5, 16, 0, 0, 0, 0});
    for (int r = 1; r <= 4; ++r) {
        cells.Get(r, 1).SetStyle(dateStyle);
    }
    cells.Get(0, 2).PutValue(u"amount");
    cells.Get(1, 2).PutValue(50);
    cells.Get(2, 2).PutValue(60);
    cells.Get(3, 2).PutValue(70);
    cells.Get(4, 2).PutValue(80);
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=Sheet1!A1:C5", 11, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"product"));
    pivotTable.AddFieldToArea(PivotFieldType::Column, U16String(u"date"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"amount"));
    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleMedium10);
    DiscreteGroupItem fruit(u"fruit", Vector<U16String>{u"grape", u"cherry"});
    DiscreteGroupItem vegetable(u"vegetable", Vector<U16String>{u"carrot", u"potato"});
    PivotFieldGroupOptions groupOptions;
    groupOptions.SetDiscreteGroupItems(Vector<DiscreteGroupItem>{fruit, vegetable});
    pivotTable.GetRowFields().Get(0).Group(groupOptions);
    pivotTable.CalculateData();
    wb.Save(u"outputDiscreteGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

调用 `CalculateData()` 后，数据透视表的行区域显示水果（葡萄 50、樱桃 80）和蔬菜（胡萝卜 60、土豆 70），总计为 260；列标签仍显示四个日期（2/5/2021、3/8/2022、4/10/2023、5/16/2024）。

## **按项目索引对数据透视表字段项目进行分组**
当项目名称较长或已本地化时，可以使用 `DiscreteGroupItem` 的第二个构造函数，通过索引标识项目。这些索引是项目在源数据中按出现顺序排列且从 0 开始的位置，而不是按字母顺序排列的位置。在上述示例数据中，葡萄对应项目 0，胡萝卜对应项目 1，土豆对应项目 2，樱桃对应项目 3，因此水果组对应 `{ 0, 3 }`，蔬菜组对应 `{ 1, 2 }`。结果与基于名称的示例完全相同。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(0, 0).PutValue(u"product");
    cells.Get(1, 0).PutValue(u"grape");
    cells.Get(2, 0).PutValue(u"carrot");
    cells.Get(3, 0).PutValue(u"potato");
    cells.Get(4, 0).PutValue(u"cherry");
    Style dateStyle = wb.CreateStyle();
    dateStyle.SetCustom(u"m/d/yyyy");
    cells.Get(0, 1).PutValue(u"date");
    Date firstDate{2021, 2, 5, 0, 0, 0, 0};
    Date secondDate{2022, 3, 8, 0, 0, 0, 0};
    Date thirdDate{2023, 4, 10, 0, 0, 0, 0};
    Date fourthDate{2024, 5, 16, 0, 0, 0, 0};
    cells.Get(1, 1).PutValue(firstDate);
    cells.Get(2, 1).PutValue(secondDate);
    cells.Get(3, 1).PutValue(thirdDate);
    cells.Get(4, 1).PutValue(fourthDate);
    for (int r = 1; r <= 4; ++r) {
        cells.Get(r, 1).SetStyle(dateStyle);
    }
    cells.Get(0, 2).PutValue(u"amount");
    cells.Get(1, 2).PutValue(50);
    cells.Get(2, 2).PutValue(60);
    cells.Get(3, 2).PutValue(70);
    cells.Get(4, 2).PutValue(80);
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=Sheet1!A1:C5", 11, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"product");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"date");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"amount");
    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleMedium10);
    DiscreteGroupItem fruit(u"fruit", Vector<int32_t>{0, 3});
    DiscreteGroupItem vegetable(u"vegetable", Vector<int32_t>{1, 2});
    PivotFieldGroupOptions groupOptions;
    groupOptions.SetDiscreteGroupItems(Vector<DiscreteGroupItem>{fruit, vegetable});
    pivotTable.GetRowFields().Get(0).Group(groupOptions);
    pivotTable.CalculateData();
    wb.Save(u"outputDiscreteGroupPivotFieldByIndex.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **注意**

{{% alert color="primary" %}}
- 未分配到任何自定义组的项目不会丢失。它们仍会保留在数据透视表中，与自定义组处于同一层级，每项均作为独立的单项条目显示。在上述示例中，仅定义水果组时，胡萝卜和土豆仍会作为独立条目保留在行区域中，与水果组并列。
- `PivotFieldGroupOptions.NewPivotField` 属性控制离散分组的布局。默认值为 `true`，此时会在原字段旁将分组字段添加为新的外层字段，从而生成上述两级布局（`RowFields` 增至 2）。将其设为 `false` 后将替换原字段；此时，行区域仅显示一个层级，其中只包含组名称及其汇总值，即水果 130（50 + 80）和蔬菜 130（60 + 70）。
- 基于名称和基于索引的 `DiscreteGroupItem` 构造函数可以在同一个 `DiscreteGroupItems` 集合中混用。
{{% /alert %}}

## **相关文章**
- [在数据透视表中对透视字段进行分组](/cells/zh/cpp/group-pivot-fields-in-the-pivot-table/)
- [在数据透视表中添加行字段和列字段](/cells/zh/cpp/pivot-table-add-row-and-column-fields/)
- [按标签或值筛选数据透视表](/cells/zh/cpp/filter-by-label-or-value-of-pivot-table/)
- [对数据透视表应用样式](/cells/zh/cpp/apply-style-to-pivot-table/)
- [刷新数据透视表](/cells/zh/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}