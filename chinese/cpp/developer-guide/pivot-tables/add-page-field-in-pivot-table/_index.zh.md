---
title: 在 Aspose.Cells for C++ 中向数据透视表添加筛选字段
linktitle: 添加筛选字段
description: 学习如何使用 Aspose.Cells for C++ 在数据透视表中添加和配置筛选字段，包括添加筛选字段、单选筛选和多选筛选。
keywords: Aspose.Cells, C++, 数据透视表, 筛选字段, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, 筛选
type: docs
weight: 250
url: /zh/cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持数据透视表中筛选字段的完整生命周期。您可以通过高级便捷 API 或通过底层的 `PageFields` 集合来添加筛选字段，并且可以以单选模式驱动筛选器、清除筛选器以显示每个筛选项，或者将字段切换为多选模式，以便用户通过 Excel 中的复选框界面一次选择多个筛选项。
{{% /alert %}}

## **简介**

筛选字段是一种数据透视字段，用于控制数据透视表主体显示源数据的哪个子集。最终用户在 Excel 中看到的是一个位于渲染数据透视表顶部的下拉列表，选择一个可用的筛选项后，数据透视表主体将重新构建，以便仅汇总属于该筛选项的记录。当数据透视字段注册为 `PivotFieldType.Page` 而非 `PivotFieldType.Row`、`PivotFieldType.Column` 或 `PivotFieldType.Data` 时，它就成为筛选字段。

筛选字段可以以两种行为方式运行。在默认的**单选**行为下，一次只能显示一个筛选项，因此数据透视表主体恰好汇总一个子集。在**多选**行为下，该字段会显示一个复选框列表，数据透视表主体汇总每个被勾选筛选项的并集。通过切换单个属性，可以将同一源字段在这些行为之间来回切换。

Aspose.Cells for C++ 提供了两种等效的方式来注册筛选字段。高级 API 是 `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")`，它接受源列名并通过一次调用添加字段。底层 API 是 `PivotTable.PageFields.Add(PivotField)`，当您已经持有 `PivotField` 引用并希望将同一字段实例添加到筛选区域时使用。这两个 API 最终都会填充相同的 `PageFields` 集合，本文余下部分将演示如何在它们之间进行选择以及如何驱动每种筛选模式。

## **添加筛选字段**

在筛选区域中注册数据透视字段有两种方法。高级调用将源列名作为字符串传入，是最常用的方式。底层调用接受现有的 `PivotField` 实例，当同一字段对象需要在多个数据透视区域中复用时非常方便。两次调用都会将该字段放入 `PivotTable.PageFields`，之后它会显示在渲染数据透视表顶部的页面下拉列表中。

### 使用 AddFieldToArea 添加筛选字段

以下示例构建了一个小的 Fruit / Year / Amount 数据集，在单元格 E3 处放置数据透视表，将 `Fruit` 放在行区域，`Amount` 放在数据区域，`Year` 放在筛选区域，刷新数据透视表，然后保存工作簿。

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    // 创建新的工作簿
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    Cells cells = worksheet.GetCells();

    // 设置表头行
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // 填充 9 行示例数据：水果、年份、数量
    const char* fruits[] = { "apple", "banana", "apple", "grape", "orange", "banana", "grape", "apple", "orange" };
    int years[]   = { 2020, 2021, 2021, 2020, 2022, 2020, 2021, 2022, 2021 };
    int amounts[] = { 100, 200, 150, 120, 180, 90, 130, 170, 110 };

    for (int i = 0; i < 9; ++i)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }

    // 添加锚定在单元格 E3 的数据透视表
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"PivotTable1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // 将字段添加到相应区域：水果作为行字段，数量作为数据字段，年份作为页字段
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");

    // 刷新并计算数据透视表数据
    pivotTable.CalculateData();

    // 保存工作簿
    workbook.Save(u"pageFieldSample.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### 使用 PageFields.Add 添加筛选字段

当您已经使用 `PivotField` 实例时，可以将其直接传递给 `PivotTable.PageFields.Add`。数据透视表和筛选字段的构造方式与上一场景完全相同；只是最后一步的筛选区域注册被替换为底层 API 调用。

```cpp
#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // 表头
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // 示例数据（9 行）
    cells.Get(u"A2").PutValue(u"apple");     cells.Get(u"B2").PutValue(u"2020"); cells.Get(u"C2").PutValue(100);
    cells.Get(u"A3").PutValue(u"apple");     cells.Get(u"B3").PutValue(u"2021"); cells.Get(u"C3").PutValue(150);
    cells.Get(u"A4").PutValue(u"apple");     cells.Get(u"B4").PutValue(u"2022"); cells.Get(u"C4").PutValue(200);
    cells.Get(u"A5").PutValue(u"grape");     cells.Get(u"B5").PutValue(u"2020"); cells.Get(u"C5").PutValue(300);
    cells.Get(u"A6").PutValue(u"grape");     cells.Get(u"B6").PutValue(u"2021"); cells.Get(u"C6").PutValue(400);
    cells.Get(u"A7").PutValue(u"grape");     cells.Get(u"B7").PutValue(u"2022"); cells.Get(u"C7").PutValue(500);
    cells.Get(u"A8").PutValue(u"blueberry"); cells.Get(u"B8").PutValue(u"2020"); cells.Get(u"C8").PutValue(250);
    cells.Get(u"A9").PutValue(u"blueberry"); cells.Get(u"B9").PutValue(u"2021"); cells.Get(u"C9").PutValue(350);
    cells.Get(u"A10").PutValue(u"blueberry");cells.Get(u"B10").PutValue(u"2022");cells.Get(u"C10").PutValue(450);

    // 在 E3 处添加数据透视表，覆盖 A1:C10
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(U16String(u"E3"), U16String(u"A1:C10"), U16String(u"PivotTable1"));
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    // Fruit -> 行，Amount -> 数据
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"Amount"));

    // 底层方法：在 BaseFields 中定位已存在的 Year PivotField，
    // 然后通过 PageFields.Add(PivotField) 将其注册到页面区域。
    PivotFieldCollection baseFields = pivotTable.GetBaseFields();
    int baseFieldCount = baseFields.GetCount();
    for (int i = 0; i < baseFieldCount; ++i) {
        PivotField f = baseFields.Get(i);
        if (f.GetName().ToUtf8() == "Year") {
            pivotTable.GetPageFields().Add(f);
            break;
        }
    }

    // 刷新，以便在保存的工作簿中反映新增的页面字段
    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **单选筛选（显示一个筛选项）**

在默认的单选行为下，筛选字段呈现为单个下拉列表，`PivotField.CurrentPageItem` 整数用于选择哪个筛选项驱动数据透视表主体。分配一个特定索引会选择该单个项；分配特殊标记值 `0x7FFD`（十进制 32765）则会清除筛选器，以便一次汇总所有筛选项。单选是默认模式，无需显式启用。

### 显示所有项

将 `CurrentPageItem` 设置为魔术值 `0x7FFD` 等同于清除筛选器：数据透视表主体汇总所有筛选项，就好像未应用任何筛选器一样。

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    U16String fruits[6] = {u"Apple", u"Apple", u"Banana", u"Banana", u"Cherry", u"Cherry"};
    int years[6] = {2022, 2023, 2022, 2023, 2022, 2023};
    int amounts[6] = {100, 150, 80, 120, 200, 250};

    for (int r = 0; r < 6; r++) {
        cells.Get(r + 1, 0).PutValue(fruits[r]);
        cells.Get(r + 1, 1).PutValue(years[r]);
        cells.Get(r + 1, 2).PutValue(amounts[r]);
    }

    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int index = pivotTables.Add(u"=A1:C7", u"E3", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(index);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");

    pivotTable.CalculateData();

    pivotTable.GetPageFields().Get(0).SetCurrentPageItem(0x7FFD);

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### 显示一个特定项

将 `CurrentPageItem` 设置为真实索引将仅选择该单个筛选项。索引是筛选字段已排序项列表中该项的位置，例如 `1` 选择排序后的第二个项。

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));

    cells.Get(u"A2").PutValue(U16String("Apple"));
    cells.Get(u"B2").PutValue(U16String("2020"));
    cells.Get(u"C2").PutValue(U16String("100"));

    cells.Get(u"A3").PutValue(U16String("Apple"));
    cells.Get(u"B3").PutValue(U16String("2021"));
    cells.Get(u"C3").PutValue(U16String("150"));

    cells.Get(u"A4").PutValue(U16String("Banana"));
    cells.Get(u"B4").PutValue(U16String("2020"));
    cells.Get(u"C4").PutValue(U16String("200"));

    cells.Get(u"A5").PutValue(U16String("Banana"));
    cells.Get(u"B5").PutValue(U16String("2021"));
    cells.Get(u"C5").PutValue(U16String("250"));

    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(U16String("A1:C5"), U16String("E3"), U16String("PivotTable1"));
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String("Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String("Amount"));
    pivotTable.AddFieldToArea(PivotFieldType::Page, U16String("Year"));

    pivotTable.GetPageFields().Get(0).SetCurrentPageItem(1);

    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **多选筛选**

多选筛选将页面下拉列表转换为复选框列表，允许最终用户同时选择多个筛选项。Aspose.Cells 公开了两个协同工作的属性。必须先将 `PivotField.IsMultipleItemSelectionAllowed` 设置为 `true`，多选 UI 才能生效。启用后，`PivotItem.IsHidden` 控制哪些项出现在复选框列表中，因此您既可以显示所有项，也可以仅将特定项列入白名单。

下面的代码在场景 1a 中构建的同一 Year 筛选字段上启用多选，然后展示两种模式：A 部分通过将每个项的 `IsHidden` 保持为 `false` 来显示所有筛选项，而 B 部分仅将您选择的源值列入白名单，并通过 `switch (pivotItems[i].GetStringValue())` 块隐藏所有其他项。

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <vector>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // 示例数据: 水果 | 年份 | 数量
    cells.Get(0, 0).PutValue(u"Fruit");
    cells.Get(0, 1).PutValue(u"Year");
    cells.Get(0, 2).PutValue(u"Amount");

    std::vector<std::vector<std::string>> data = {
        {"apple",  "2019", "100"},
        {"apple",  "2020", "150"},
        {"apple",  "2021", "200"},
        {"banana", "2019", "110"},
        {"banana", "2020", "160"},
        {"banana", "2021", "210"},
        {"grape",  "2019", "120"},
        {"grape",  "2020", "170"},
        {"grape",  "2021", "220"}
    };

    for (int i = 0; i < (int)data.size(); i++) {
        cells.Get(i + 1, 0).PutValue(U16String(data[i][0].c_str()));
        cells.Get(i + 1, 1).PutValue(std::stoi(data[i][1]));
        cells.Get(i + 1, 2).PutValue(std::stoi(data[i][2]));
    }

    Worksheet pivotSheet = workbook.GetWorksheets().Add(u"Pivot");
    PivotTableCollection pivots = pivotSheet.GetPivotTables();
    int pivotIndex = pivots.Add(u"E3", u"A1:C10", u"PivotTable1");
    PivotTable pivotTable = pivots.Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");

    // — 启用页面字段的多选功能
    pivotTable.GetPageFields().Get(0).SetIsMultipleItemSelectionAllowed(true);

    // 第一部分 — 选择所有项（使每个项可见）
    PivotItemCollection pivotItems = pivotTable.GetPageFields().Get(0).GetPivotItems();
    int itemCount = pivotItems.GetCount();
    for (int i = 0; i < itemCount; i++) {
        pivotItems.Get(i).SetIsHidden(false);
    }

    // 第二部分 — 仅按源值选择特定项
    for (int i = 0; i < itemCount; i++) {
        U16String val = pivotItems.Get(i).GetStringValue();
        std::string s = val.ToUtf8();
        if (s == "2020" || s == "grape" || s == "blueberry") {
            pivotItems.Get(i).SetIsHidden(false);
        } else {
            pivotItems.Get(i).SetIsHidden(true);
        }
    }

    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

> **注意：** 通过 `PivotItem.IsHidden` 使用多选筛选时，**必须至少保留一个 `PivotItem` 可见**（`IsHidden == false`）。如果所有项都被隐藏，Excel 在打开文件时可能会崩溃或呈现空白的数据透视表。始终确保您的多选白名单包含源数据中至少一个项。

## **应该使用哪种 API 和哪种模式？**

下表汇总了何时使用每个 API 和模式，以便您无需详细阅读每个场景即可选择正确的组合。

| 场景 / 用例 | 推荐 API | 使用的属性 | 备注 |
|---|---|---|---|
| 通过源列名添加筛选字段（最常见） | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | 高级 API，一行代码完成。除非需要 `PivotField` 引用，否则请使用此方法。 |
| 当您已有 `PivotField` 对象时添加筛选字段 | `PivotTable.PageFields.Add(PivotField)` | n/a | 当字段对象是从其他地方获取或需要复用时使用。 |
| 筛选到单个筛选项（默认模式） | `PivotField.CurrentPageItem` | 设置为特定索引 | 例如，`1` 显示已排序列表中的第二个项。 |
| 显示所有项 / 清除筛选器 | `PivotField.CurrentPageItem` | 设置为 `0x7FFD` | 魔术值 `0x7FFD`（十进制 32765）是"所有项"的标记值。 |
| 在 Excel 中启用多选 UI | `PivotField.IsMultipleItemSelectionAllowed` | 设置为 `true` | 在任何 `IsHidden` 调用生效之前必须设置。 |
| 在多选列表中隐藏 / 显示单个项 | `PivotItem.IsHidden` | 针对每个项设置 | 必须至少保留一个项可见（`IsHidden == false`）。 |

{{% alert color="primary" %}}
配置多选筛选时，请始终牢记可见性约束。如果多选筛选字段中的每个 `PivotItem` 都被隐藏，Excel 在打开时会崩溃或呈现空白的数据透视表。请根据源数据构建白名单，确保至少一个项保持可见，这样保存的工作簿将在每台机器上可靠打开。
{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}
