---
title: 在 Aspose.Cells for C++ 中刷新数据透视表
linktitle: 在 Aspose.Cells for C++ 中刷新数据透视表
description: 学习如何使用 v26.7+ 数据透视表刷新 API 在 Aspose.Cells for C++ 中刷新数据透视表。本文涵盖 RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData 和 GetPivotTables，并附有实用的代码示例。
keywords: Aspose.Cells, C++, 数据透视表, 刷新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /zh/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供了一套分层的刷新 API，可让您按四种不同的粒度重新加载数据透视表数据——从整个工作簿到单个数据透视表。从 **Aspose.Cells for C++ v26.7** 起，旧方法 `PivotTable.RefreshData()` 已标记为过时，应替换为本文介绍的更高效、感知缓存的 API。
{{% /alert %}}
## 简介
刷新数据透视表很少只是一个单一的操作。在幕后，Aspose.Cells 维护着一个分层的数据链，它将您的原始源数据与您在工作表中看到的渲染值连接起来。理解这个数据链是针对任何情况选择正确刷新 API 的关键。
四层数据链如下：
1. **数据源**——原始的工作表区域、数据库查询或合并区域，原始数据存放在此处。
2. **PivotCache**——源数据的内存快照。每个数据透视表都构建在一个 `PivotCache` 之上；所有数据都在这里进行收集和聚合。
3. **PivotTable**——定义行、列、值和筛选字段的视图对象。`PivotTable` *仅* 从其 `PivotCache` 读取数据，从不直接从数据源读取。
4. **单元格**——工作表中的 `Cells`，`PivotTable` 将其计算后的值和样式渲染到这些单元格中。
一个特别重要的概念是**共享缓存**。当工作簿中的多个数据透视表引用相同的源区域时，它们共享*同一个* `PivotCache` 实例。一个 `PivotCache` 可以被多个数据透视表引用，刷新该缓存会同时刷新所有依赖的 `PivotTable`。
{{% alert color="primary" %}}
`PivotCache.SourceType`（枚举 `PivotTableSourceType`）指示缓存数据的来源。自 v26.7 起，`PivotCache.Refresh()` 仅支持 **`Sheet`** 和 **`Consolidation`** 源类型——即位于工作表区域中的数据。外部源（数据库、外部连接等）目前尚无法通过缓存 API 进行刷新。
{{% /alert %}}
由于这种数据链，Aspose.Cells 中存在两条基本的刷新路径：
- **`PivotCache.Refresh()`**——在一次操作中重新加载源 → 缓存，并重新计算所有依赖的 `PivotTable`。
- **`PivotTable.CalculateData()`**——从已缓存的数据重新计算单个 `PivotTable` 的显示，不往返于数据源。
本文中的所有场景都使用工作表单元格源数据，因此源类型为 `Sheet`，刷新操作按所述方式运行。
## 必需的 Include 指令
由于数据透视表类型位于 `Aspose::Cells::Pivot` 命名空间中，本文中的所有 C++ 示例都以以下头文件和命名空间指令开头：
## 刷新工作簿中的所有数据透视表
当您需要确保工作簿中的每个数据透视缓存和每个数据透视表都反映最新的源数据时，最简单、最全面的 API 是 `Workbook.RefreshAll()`。单次调用即可遍历整个工作簿——从其源刷新每个 `PivotCache`，然后重新计算每个依赖的 `PivotTable`。这是对性能要求不高的常规全文档刷新的推荐方法。
下面的示例构建了一个包含 Fruit/Year/Amount 源区域的工作簿，创建一个数据透视表，修改一些源值，然后使用 `RefreshAll()` 在一次调用中使所有数据保持最新。
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));

    cells.Get(u"A2").PutValue(U16String("grape"));
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(50);

    cells.Get(u"A3").PutValue(U16String("blueberry"));
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(60);

    cells.Get(u"A4").PutValue(U16String("kiwi"));
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(70);

    cells.Get(u"A5").PutValue(U16String("cherry"));
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(80);

    cells.Get(u"A6").PutValue(U16String("grape"));
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(90);

    cells.Get(u"A7").PutValue(U16String("blueberry"));
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(100);

    cells.Get(u"A8").PutValue(U16String("kiwi"));
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(110);

    cells.Get(u"A9").PutValue(U16String("cherry"));
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(120);

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    cells.Get(u"C2").PutValue(55);
    cells.Get(u"C5").PutValue(85);
    cells.Get(u"C9").PutValue(125);

    pivotTable.CalculateData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## 刷新单个工作表上的所有数据透视表
有时您只需要刷新位于特定工作表上的数据透视表——例如，当已知其他工作表上的数据透视表与此无关且不应被触动时。针对这种情况，Aspose.Cells 提供了 `Worksheet.RefreshPivotTables()`，它限定在单个 `Worksheet` 实例范围内。
这比 `Workbook.RefreshAll()` 更有选择性：仅刷新目标工作表上的数据透视表，其他工作表上的数据透视表保持不变。
下面的示例填充相同的 Fruit/Year/Amount 源数据，在第一个工作表上添加一个数据透视表，修改一些源值，然后仅刷新该工作表上的数据透视表。
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");

    worksheet.GetCells().Get(u"A2").PutValue(u"grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(100);

    worksheet.GetCells().Get(u"A3").PutValue(u"blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2021);
    worksheet.GetCells().Get(u"C3").PutValue(150);

    worksheet.GetCells().Get(u"A4").PutValue(u"kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(200);

    worksheet.GetCells().Get(u"A5").PutValue(u"cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2021);
    worksheet.GetCells().Get(u"C5").PutValue(120);

    worksheet.GetCells().Get(u"A6").PutValue(u"grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(180);

    worksheet.GetCells().Get(u"A7").PutValue(u"blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2020);
    worksheet.GetCells().Get(u"C7").PutValue(130);

    worksheet.GetCells().Get(u"A8").PutValue(u"kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(220);

    worksheet.GetCells().Get(u"A9").PutValue(u"cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2020);
    worksheet.GetCells().Get(u"C9").PutValue(140);

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    worksheet.GetCells().Get(u"C2").PutValue(300);
    worksheet.GetCells().Get(u"C5").PutValue(250);
    worksheet.GetCells().Get(u"C9").PutValue(400);

    worksheet.RefreshPivotTables();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## 刷新单个数据透视表
当您需要对单个数据透视表进行细粒度控制时，基于缓存的 API 为您提供了两种选项。两者之间的选择取决于实际发生变化的内容：是底层源数据，还是数据透视表本身的视图/布局设置。
### 源数据已更改——使用 `PivotCache.Refresh()`
如果底层源数据已更改，则正确的入口点是 `pivotTable.GetPivotCache().Refresh()`。此调用将源数据重新读取到缓存中，然后重新计算依赖于该缓存的每个 `PivotTable`。
{{% alert color="primary" %}}
由于数据透视表共享单个 `PivotCache` 实例，调用 `PivotCache.Refresh()` 会重新计算构建于**该**共享缓存上的**所有**数据透视表——而不仅仅是您引用的那一个。如果两个数据透视表共享相同的源区域，刷新其中一个缓存会同时刷新两者。
{{% /alert %}}
下面的示例在同一源区域上创建两个数据透视表以演示这种共享缓存行为，修改一些源值，然后通过一个缓存引用进行刷新。
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // 表头行：水果 / 年份 / 金额
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // 数据行
    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    // 添加第一个数据透视表 "Pivot1"，锚定在 E3 单元格，数据源范围为 A1:C9
    int pivotIndex1 = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = worksheet.GetPivotTables().Get(pivotIndex1);

    // 为 Pivot1 分配字段
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // 添加第二个数据透视表 "Pivot2"，锚定在 E15，使用相同的数据源范围 A1:C9
    int pivotIndex2 = worksheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = worksheet.GetPivotTables().Get(pivotIndex2);

    // 为 Pivot2 分配相同的字段
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // 修改源数据中的几个金额单元格值，以模拟数据变化
    cells.Get(u"C2").PutValue(150);
    cells.Get(u"C4").PutValue(350);
    cells.Get(u"C7").PutValue(650);

    // 通过刷新数据透视表数据来刷新共享的透视缓存
    pivotTable1.RefreshData();

    // 保存工作簿
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
### 仅视图/布局已更改——使用 `CalculateData()`
如果源数据*未*更改，但仅修改了数据透视表的视图或布局设置（例如，将某个字段移至其他区域，或切换了打开文件时刷新的设置），则无需往返于数据源。缓存已包含正确的数据；只需重新计算渲染的 `PivotTable`。在这种情况下，`pivotTable.CalculateData()` 是正确的选择。
这避免了不必要的源数据获取，当许多数据透视表共享同一个缓存时，速度显著加快。
下面的示例修改数据透视表的非源属性，然后调用 `CalculateData()` 从现有缓存重新渲染它。
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // 写入 Fruit / Year / Amount 表头行
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");

    // 写入 8 行数据(第 2-9 行,匹配源数据范围 A1:C9)
    worksheet.GetCells().Get(u"A2").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(100);

    worksheet.GetCells().Get(u"A3").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2020);
    worksheet.GetCells().Get(u"C3").PutValue(200);

    worksheet.GetCells().Get(u"A4").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(300);

    worksheet.GetCells().Get(u"A5").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2020);
    worksheet.GetCells().Get(u"C5").PutValue(400);

    worksheet.GetCells().Get(u"A6").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(150);

    worksheet.GetCells().Get(u"A7").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2021);
    worksheet.GetCells().Get(u"C7").PutValue(250);

    worksheet.GetCells().Get(u"A8").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(350);

    worksheet.GetCells().Get(u"A9").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2021);
    worksheet.GetCells().Get(u"C9").PutValue(450);

    // 添加一个名为 "Pivot1" 的数据透视表,放置在目标单元格 E3,数据源为 A1:C9
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // 分配字段:Fruit 分配到行,Year 分配到列,Amount 分配到数据区
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // 修改视图/布局属性——这只是显示上的更改,
    // 因此不需要通过 PivotCache.Refresh() 重新读取源数据。
    pivotTable.SetRefreshDataOnOpeningFile(false);

    // CalculateData() 从 PivotCache 中已有的数据重新渲染此数据透视表的显示(数据 + 样式)。
    // 由于源数据未发生变化,不会执行对源数据的往返访问——仅重新计算
    // 缓存值并将其写入工作表单元格。
    pivotTable.CalculateData();

    // 将工作簿保存到磁盘
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## 获取共享同一 PivotCache 的所有数据透视表
工作簿通常包含许多数据透视表，它们都位于一个共享缓存之上。要枚举它们——例如，在执行批量刷新之前，或诊断共享缓存的影响——请使用 `PivotCache.GetPivotTables()`。此方法返回依赖于给定缓存的每个 `PivotTable` 的集合。
这也是确认两个数据透视表确实共享同一 `PivotCache` 实例的最直接方法：您可以比较缓存引用，或简单地遍历 `GetPivotTables()` 返回的集合并观察其中出现的数据透视表。
下面的示例在同一源区域上创建两个数据透视表，验证它们共享同一缓存实例，然后枚举该缓存的数据透视表。

## 从已过时的 `PivotTable.RefreshData()` 进行迁移
在 Aspose.Cells for C++ v26.7 之前，刷数据透视表的标准方法是对每个数据透视表单独调用 `PivotTable.RefreshData()`。自 v26.7 起，该方法被标记为**过时**，应替换为上文介绍的感知缓存的 API。
在真实的工作簿中，每表 `RefreshData()` 方法存在两个问题：
- 每次调用时都会从源*重新*获取数据，即使源数据未发生更改。
- 每次调用都会刷新整个共享缓存。当许多数据透视表共享一个缓存时，对每个数据透视表重复调用 `RefreshData()` 会导致同一个缓存被反复重新获取，速度非常慢。
推荐的替换方法如下：
- **刷新工作簿中的所有数据透视表** → 使用 `workbook.RefreshAll();`
- **刷新其中的一部分** → 使用 `pivotTable.GetPivotCache().Refresh();` 刷新单个缓存。由于缓存是共享的，此单次调用会更新构建于该缓存之上的每个数据透视表。位于已刷新缓存之上的其他数据透视表可以安全地跳过。
- **仅数据透视表视图/布局已更改** → 使用 `pivotTable.CalculateData();` 从现有缓存重新渲染，无需任何源数据往返。
下面的示例演示了多个数据透视表共享单个缓存的工作簿的新的高效模式。
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    sheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    sheet.GetCells().Get(u"B1").PutValue(u"Year");
    sheet.GetCells().Get(u"C1").PutValue(u"Amount");

    sheet.GetCells().Get(u"A2").PutValue(u"Grape");      sheet.GetCells().Get(u"B2").PutValue(2020); sheet.GetCells().Get(u"C2").PutValue(1000);
    sheet.GetCells().Get(u"A3").PutValue(u"Blueberry");  sheet.GetCells().Get(u"B3").PutValue(2020); sheet.GetCells().Get(u"C3").PutValue(2000);
    sheet.GetCells().Get(u"A4").PutValue(u"Kiwi");       sheet.GetCells().Get(u"B4").PutValue(2020); sheet.GetCells().Get(u"C4").PutValue(1500);
    sheet.GetCells().Get(u"A5").PutValue(u"Cherry");     sheet.GetCells().Get(u"B5").PutValue(2020); sheet.GetCells().Get(u"C5").PutValue(2500);
    sheet.GetCells().Get(u"A6").PutValue(u"Grape");      sheet.GetCells().Get(u"B6").PutValue(2021); sheet.GetCells().Get(u"C6").PutValue(3000);
    sheet.GetCells().Get(u"A7").PutValue(u"Blueberry");  sheet.GetCells().Get(u"B7").PutValue(2021); sheet.GetCells().Get(u"C7").PutValue(1800);
    sheet.GetCells().Get(u"A8").PutValue(u"Kiwi");       sheet.GetCells().Get(u"B8").PutValue(2021); sheet.GetCells().Get(u"C8").PutValue(2200);
    sheet.GetCells().Get(u"A9").PutValue(u"Cherry");     sheet.GetCells().Get(u"B9").PutValue(2021); sheet.GetCells().Get(u"C9").PutValue(2700);

    int idx1 = sheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = sheet.GetPivotTables().Get(idx1);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    int idx2 = sheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = sheet.GetPivotTables().Get(idx2);
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    sheet.GetCells().Get(u"C2").PutValue(5000);
    sheet.GetCells().Get(u"C5").PutValue(7500);
    sheet.GetCells().Get(u"C9").PutValue(9500);


    pivotTable2.CalculateData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## 应该使用哪个刷新 API？
下表总结了可用的刷新 API 以及何时选择每个 API。
| 目标 | 推荐的 API | 备注 |
|------|-----------------|-------|
| 刷新工作簿中的所有内容 | `Workbook.RefreshAll()` | 一次调用；覆盖所有缓存和数据透视表。 |
| 仅刷新单个工作表上的数据透视表 | `Worksheet.RefreshPivotTables()` | 限定于一个工作表。 |
| 一个缓存的源数据已更改 | `pivotTable.GetPivotCache().Refresh()` | 刷新该共享缓存上的所有数据透视表。 |
| 仅视图/布局设置已更改 | `pivotTable.CalculateData()` | 跳过不必要的源数据往返。 |
| 列出共享缓存上的所有数据透视表 | `pivotCache.GetPivotTables()` | 用于在批量刷新之前进行枚举。 |
实际上，请优先使用基于缓存的 API，而不是过时的每表 `RefreshData()`。它们能够感知共享缓存，可避免冗余的源数据获取，并允许您选择满足刷新需求的最小粒度。

{{< app/cells/assistant language="cpp" >}}
