---
title: 向数据透视表添加条件格式
linktitle: 向数据透视表添加条件格式
description: 在 Aspose.Cells for C++ 中向数据透视表添加条件格式 - 使用 ApplyTo 和 PivotConditionFormatScopeType 范围将规则锚定到数据区域，或使用 AddCellArea 和 PivotAreas 定义目标，然后通过 FormatConditions.AddCondition 附加规则和样式。
keywords: Aspose.Cells for C++, 数据透视表, 条件格式, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C++
type: docs
weight: 30
url: /zh/cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
父页面和同级页面中描述的样式是静态的——`PivotArea` 或 `CellArea` 区域只会绘制一次，并且无论数值如何都会保持其样式。条件格式是规则驱动的对应方式——突出显示所有大于 200 的金额、为中间五十百分比着色，或标记排名最低的项目——并且在数据透视表重新计算或刷新时，突出显示会随数值变化而更新。
在 Aspose.Cells 中，数据透视表的条件格式位于 `pivotTable.GetConditionalFormats()` 集合中。每个条目都是一个 `PivotConditionalFormat`，它独立地回答两个问题：
- **规则适用于哪里？** 目标区域可以通过 `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)` 定义，该方法对应 Excel 用户界面的范围选择器，也可以通过 `AddCellArea(CellArea)` 并结合 `GetPivotAreas()` 集合显式命名区域。
- **规则测试的内容是什么？** 通过 `GetFormatConditions()` 使用 `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` 添加一个或多个条件，每个条件携带其自身的 `Style`。

{{% alert color="primary" %}}
不要在数据透视表条件格式的 `GetFormatConditions()` 对象上调用 `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` 或 `FormatConditionCollection.AddArea(CellArea)`。这两个重载来自普通工作表的条件格式 API，无法用于数据透视表——单元格区域永远不会转换为数据透视表区域，因此请求会被静默忽略。始终在 `PivotConditionalFormat` 本身上定义区域（`ApplyTo`、`AddCellArea` 或 `GetPivotAreas()`），并使用 `AddCondition` 的任意重载来添加规则。
{{% /alert %}}

## **使用范围应用规则（Excel UI 方式）**
第一种方式按照 Excel 用户界面的做法定位规则。数据透视表的单元格由其零基工作表坐标命名，`PivotConditionFormatScopeType` 范围告诉 Aspose.Cells 规则应从该单元格向外覆盖多远：
- `PivotConditionFormatScopeType::Data` - 数据透视表生成的所有值单元格，包括总计。
- `PivotConditionFormatScopeType::Field` - 属于该单元格标识的字段的值单元格，不包括总计。该单元格必须是字段单元格，例如行字段标签；传入值单元格会抛出异常。
- `PivotConditionFormatScopeType::Selection` - 仅该单元格选中的交叉处的值单元格，通常是单个值单元格。
下面的示例创建了一个左上角位于 E3 的水果销售数据透视表，在单元格 F4（第 3 行，第 5 列）使用 `Data` 范围锚定条件格式，并将所有大于 200 的金额以红底白字加粗显示。若数据为 Apple 220、Banana 330、Cherry 200，以及总计 750，则规则会为 F4、F5、F7 着色——解析后的区域是整个数据列 F4:F7，只有满足条件的单元格会被点亮。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    const char16_t* fruits[] = {u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry"};
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    int index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    format.ApplyTo(3, 5, PivotConditionFormatScopeType::Data);
    int conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue, OperatorType::GreaterThan, u"200", nullptr);
    Style style = workbook.CreateStyle();
    Font font = style.GetFont();
    font.SetIsBold(true);
    font.SetColor(Color::White());
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatData.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

将同一规则锚定在行字段标签 E4（第 3 行，第 4 列）并使用 `Field` 范围时，解析的区域变为 F4:F6——同一数据列但不包括总计行，因为此时范围描述的是 `Fruit` 字段而不是整个值区域。使用 `Selection` 范围锚定在 F4 时，仅解析为 F4 本身。

## **手动定义区域**
第二种方式跳过范围选择器，在 `PivotConditionalFormat` 上显式命名区域。

### **使用 AddCellArea 定义工作表矩形**
`AddCellArea(CellArea)` 将给定的矩形记录为规则的目标。坐标采用零基工作表坐标，区域正好是提供的矩形——不会扩展到数据列，也不会包含总计逻辑。当感兴趣的单元格是当前数据透视布局中已知的固定矩形时使用此方法。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    U16String fruits[] = {
        U16String(u"Apple"),
        U16String(u"Banana"),
        U16String(u"Apple"),
        U16String(u"Banana"),
        U16String(u"Cherry"),
        U16String(u"Cherry")
    };
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"Amount"));
    pivotTable.CalculateData();
    int32_t index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    CellArea area;
    area.StartRow = 3;
    area.EndRow = 5;
    area.StartColumn = 5;
    area.EndColumn = 5;
    format.AddCellArea(area);
    int32_t conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue,
        OperatorType::Between,
        u"150",
        u"300");
    Style style = workbook.CreateStyle();
    style.GetFont().SetIsItalic(true);
    style.SetForegroundColor(Color::LightYellow());
    style.SetPattern(BackgroundType::Solid);
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatCellArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### **使用 PivotAreas 定义语义数据透视区域**
`GetPivotAreas()` 提供了同级页面用于静态样式的语义区域模型。构建一个 `PivotArea`，使用 `Select` 或 `SelectField` 选择字段或区域，然后通过 `GetPivotAreas().AddPivotArea(PivotArea)` 添加。语义区域会绑定到其字段上，因此在数据透视表刷新并且布局变化时，条件格式会随字段移动。`GetPivotAreas().Add(PivotArea)` 重载仍可编译，但已标记为过时——推荐使用 `AddPivotArea`。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    const char16_t* fruits[] = {u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry"};
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    int index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    PivotArea area(pivotTable);
    area.SelectField(PivotFieldType::Data, u"Amount");
    format.GetPivotAreas().AddPivotArea(area);
    int conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue, OperatorType::LessThan, u"150", nullptr);
    Style style = workbook.CreateStyle();
    style.GetFont().SetColor(Color::Gray());
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatPivotArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **规则的存储位置及重新加载后的持久性**
每次调用 `pivotTable.GetConditionalFormats().Add()` 都会向数据透视表添加一个 `PivotConditionalFormat`。条件、公式以及样式随工作簿一起保存——在下面示例中重新打开文件时，仍然可以看到相同的规则及其类型、运算符和公式完整无缺，`GetCellAreas()` 亦返回相同的区域。那些从未添加条件的条目在工作簿保存时会被丢弃，就像 Excel 会丢弃没有规则的条件格式一样。

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
static const char* ToString(FormatConditionType type)
{
    switch (type)
    {
    case FormatConditionType::CellValue:
        return "CellValue";
    default:
        return "Unknown";
    }
}
static const char* ToString(OperatorType op)
{
    switch (op)
    {
    case OperatorType::GreaterThan:
        return "GreaterThan";
    default:
        return "Unknown";
    }
}
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook(u"PivotConditionalFormatData.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(0).GetPivotTables().Get(0);
    auto conditionalFormats = pivotTable.GetConditionalFormats();
    int formatCount = conditionalFormats.GetCount();
    std::cout << "Conditional formats: " << formatCount << std::endl;
    for (int i = 0; i < formatCount; ++i)
    {
        PivotConditionalFormat format = conditionalFormats.Get(i);
        auto formatConditions = format.GetFormatConditions();
        int conditionCount = formatConditions.GetCount();
        for (int j = 0; j < conditionCount; ++j)
        {
            FormatCondition condition = formatConditions.Get(j);
            std::cout << "Format " << i << ": "
                      << ToString(condition.GetType()) << " "
                      << ToString(condition.GetOperator())
                      << " formula1=" << condition.GetFormula1().ToUtf8()
                      << std::endl;
        }
        Vector<CellArea> areas = format.GetCellAreas();
        for (int k = 0; k < areas.GetLength(); ++k)
        {
            CellArea area = areas[k];
            std::cout << "    rows " << area.StartRow + 1 << "-" << area.EndRow + 1
                      << ", columns " << area.StartColumn + 1 << "-" << area.EndColumn + 1
                      << std::endl;
        }
    }
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **相关文档**
- [将样式应用于数据透视表](/cells/zh/cpp/apply-style-to-pivot-table/)
- [格式化数据透视表的部分](/cells/zh/cpp/format-part-of-pivot-table/)
- [在数据透视表中显示或筛选前 10 项](/cells/zh/cpp/top-10-show-or-filter-in-pivot-table/)
- [按标签或数值筛选数据透视表](/cells/zh/cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="cpp" >}}