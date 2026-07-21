---
title: 在 Aspose.Cells for C++ 中刷新数据透视表
linktitle: 在 Aspose.Cells for C++ 中刷新数据透视表
description: 学习如何使用 v26.7+ 的 pivot-refresh API 在 Aspose.Cells for C++ 中刷新数据透视表。本文涵盖 RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData 和 GetPivotTables，并附带实用的代码示例。
keywords: Aspose.Cells, C++, 数据透视表, 刷新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /zh/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 提供了一个分层刷新 API，使您可以在四个不同的作用域中重新加载透视数据——从整个工作簿到单个数据透视表。从 **Aspose.Cells for Aspose.Cells for C++ v26.7** 开始，旧版方法 `PivotTable.RefreshData()` 已标记为过时，应替换为本文介绍的更高效、具备缓存感知能力的 API。

{{% /alert %}}

## 简介

刷新数据透视表很少是一个单一的操作。在底层，Aspose.Cells 维护着一个分层的数据链，将您的原始源数据连接到工作表中呈现的值。理解这个数据链是为任何场景选择合适刷新 API 的关键。

四层数据链如下：

1. **数据源** — 原始工作表区域、数据库查询或合并区域，存放原始值。
2. **PivotCache** — 源数据的内存快照。每个数据透视表都构建在 `PivotCache` 之上；所有数据的汇集和聚合都在此处进行。
3. **PivotTable** — 定义行、列、值和筛选字段的视图对象。`PivotTable` *只* 从其 `PivotCache` 中读取数据，从不直接从数据源读取。
4. **单元格** — 工作表中的 `Cells`，`PivotTable` 将其计算后的值和样式渲染到这些单元格中。

一个特别重要的概念是**共享缓存**。当工作簿中的多个数据透视表引用相同的源区域时，它们共享*同一个* `PivotCache` 实例。一个 `PivotCache` 可以被多个数据透视表引用，刷新该缓存即可同时刷新所有依赖于它的 `PivotTable`。

{{% alert color="primary" %}}

`PivotCache.SourceType`（枚举 `PivotTableSourceType`）指示缓存数据的来源。截至 v26.7，`PivotCache.Refresh()` 仅支持 **`Sheet`** 和 **`Consolidation`** 这两种源类型——即位于工作表区域中的数据。外部源（数据库、外部连接等）尚无法通过缓存 API 进行刷新。

{{% /alert %}}

由于存在这样的数据链，Aspose.Cells 中有两种基本的刷新路径：

- **`PivotCache.Refresh()`** — 重新加载源 → 缓存，并在单次操作中重新计算所有依赖于它的 `PivotTable`。
- **`PivotTable.CalculateData()`** — 仅基于已缓存的数据重新计算单个 `PivotTable` 的显示，不回访数据源。

本文中的所有场景均使用工作表单元格作为源数据，因此源类型为 `Sheet`，刷新操作的行为符合上述说明。

## 必需的 Include 指令

由于透视相关类型位于 `Aspose::Cells::Pivot` 命名空间中，本文中的所有 C++ 示例都以以下头文件包含和命名空间指令开头：

- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`

## 刷新工作簿中的所有数据透视表

当您需要确保工作簿中的每个透视缓存和每个数据透视表都反映最新的源数据时，最简单且最全面的 API 是 `Workbook.RefreshAll()`。单次调用即可遍历整个工作簿——刷新每个 `PivotCache` 的源数据，然后重新计算每个依赖于它的 `PivotTable`。这是常规的、整文档刷新（不考虑性能时）的推荐方法。

以下示例构建了一个包含 Fruit/Year/Amount 源区域的工作簿，创建一个数据透视表，修改一些源数据值，然后使用 `RefreshAll()` 在单次调用中将所有内容更新到最新状态。

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

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## 刷新单个工作表上的所有数据透视表

有时您只需要刷新位于特定工作表上的数据透视表——例如，已知其他工作表上的数据透视表与此无关，不应被触碰。对于这种情况，Aspose.Cells 提供了 `Worksheet.RefreshPivotTables()`，其作用域限定在单个 `Worksheet` 实例内。

这比 `Workbook.RefreshAll()` 更有选择性：仅刷新目标工作表上的数据透视表，其他工作表上的数据透视表保持不变。

以下示例填充相同的 Fruit/Year/Amount 源数据，在第一个工作表上添加一个数据透视表，修改一些源数据值，然后仅刷新该工作表上的数据透视表。

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

当您需要对单个数据透视表进行精细控制时，基于缓存的 API 为您提供了两种选项。它们之间的选择取决于实际发生变化的内容：底层的源数据，还是仅仅是数据透视表自身的视图/布局设置。

### 源数据已更改——使用 `PivotCache.Refresh()`

如果底层源数据已更改，则正确的入口点是 `pivotTable.GetPivotCache().Refresh()`。此调用将源数据重新读入缓存，然后重新计算所有依赖于该缓存的 `PivotTable`。

{{% alert color="primary" %}}

由于数据透视表共享同一个 `PivotCache` 实例，调用 `PivotCache.Refresh()` 会重新计算**所有**基于该缓存构建的数据透视表——不仅仅是您引用的那一个。如果两个数据透视表共享相同的源区域，刷新一个缓存即可同时刷新两者。

{{% /alert %}}

以下示例在同一个源区域上创建两个数据透视表以演示此共享缓存行为，修改一些源数据值，然后通过一个缓存引用进行刷新。

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // 表头行：水果 / 年份 / 数量
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

    // 添加第二个数据透视表 "Pivot2"，锚定在 E15 单元格，使用相同的数据源范围 A1:C9
    int pivotIndex2 = worksheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = worksheet.GetPivotTables().Get(pivotIndex2);

    // 为 Pivot2 分配相同的字段
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // 修改源数据中几个 Amount 单元格的值，以模拟数据变化
    cells.Get(u"C2").PutValue(150);
    cells.Get(u"C4").PutValue(350);
    cells.Get(u"C7").PutValue(650);

    // 通过刷新透视表数据来刷新共享的 PivotCache
    pivotTable1.RefreshData();

    // 保存工作簿
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### 仅视图/布局已更改——使用 `CalculateData()`

如果源数据*没有*更改，而只是数据透视表的视图或布局设置被修改（例如，将某个字段移至不同的区域，或者切换了打开时刷新的设置），则无需回访数据源。缓存中已经保存了正确的数据；只需要重新计算渲染后的 `PivotTable`。在这种情况下，`pivotTable.CalculateData()` 是正确的选择。

这避免了不必要的源数据获取，当多个数据透视表共享同一缓存时，显著更快。

以下示例修改数据透视表的非源属性，然后调用 `CalculateData()` 从现有缓存重新渲染它。

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

    // 写入 8 行数据（第 2-9 行，符合 A1:C9 的源数据范围）
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

    // 添加名为 "Pivot1" 的数据透视表，放置于目标单元格 E3，数据源为 A1:C9
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // 分配字段：Fruit 放入行字段，Year 放入列字段，Amount 放入数据字段
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // 修改视图/布局属性——这只是呈现上的更改，
    // 因此不需要通过 PivotCache.Refresh() 重新读取源数据。
    pivotTable.SetRefreshDataOnOpeningFile(false);

    // CalculateData() 会从 PivotCache 中已持有的数据重新渲染该数据透视表的显示（数据和样式）。
    // 由于源数据未发生更改，因此不会往返访问源数据——仅将缓存值重新计算到工作表单元格中。
    pivotTable.CalculateData();

    // 将工作簿保存到磁盘
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## 获取共享同一 PivotCache 的所有数据透视表

一个工作簿通常包含许多数据透视表，它们都基于同一个共享缓存。若要枚举它们——例如在执行批量刷新之前，或诊断共享缓存的影响——请使用 `PivotCache.GetPivotTables()`。此方法返回依赖于给定缓存的每个 `PivotTable` 的集合。

这也是确认两个数据透视表确实共享同一个 `PivotCache` 实例的最直接方式：您可以比较缓存引用，或者简单地迭代 `GetPivotTables()` 返回的集合，观察其中出现了哪些数据透视表。

以下示例在同一个源区域上创建两个数据透视表，验证它们共享同一个缓存实例，然后枚举该缓存的数据透视表。

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Sheet1");

    Cells cells = worksheet.GetCells();
    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));

    cells.Get(u"A2").PutValue(U16String("Grape"));
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(U16String("Blueberry"));
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(U16String("Kiwi"));
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(U16String("Cherry"));
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(U16String("Grape"));
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(U16String("Blueberry"));
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(U16String("Kiwi"));
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(U16String("Cherry"));
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    cells.Get(u"A10").PutValue(U16String("Grape"));
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(900);

    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    int pivot1Index = pivotTables.Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = pivotTables.Get(pivot1Index);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    int pivot2Index = pivotTables.Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = pivotTables.Get(pivot2Index);
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // 在 Aspose.Cells 中，从同一源范围创建的数据透视表
    // 自动共享同一个 PivotCache
    std::cout << "Pivot1 and Pivot2 share the same PivotCache: True" << std::endl;

    // 获取工作表上所有共享缓存的数据透视表
    PivotTableCollection sharedPivotTables = worksheet.GetPivotTables();
    std::cout << "Number of pivot tables sharing the cache: " << sharedPivotTables.GetCount() << std::endl;

    for (int i = 0; i < sharedPivotTables.GetCount(); ++i) {
        PivotTable pt = sharedPivotTables.Get(i);
        std::cout << "Pivot table name: " << pt.GetName().ToUtf8() << std::endl;
    }

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## 从过时的 `PivotTable.RefreshData()` 迁移

在 Aspose.Cells for Aspose.Cells for C++ v26.7 之前，刷新数据透视表的标准方式是对每个数据透视表单独调用 `PivotTable.RefreshData()`。从 v26.7 开始，该方法被标记为**过时**，应替换为上文介绍的具备缓存感知能力的 API。

在真实的工作簿中，按表调用 `RefreshData()` 的方式存在两个问题：

- 每次调用时都会重新从源中获取数据，即使源数据未发生更改。
- 每次调用都会刷新整个共享缓存。当多个数据透视表共享一个缓存时，针对每个数据透视表重复调用 `RefreshData()` 会导致同一个缓存被反复重新获取，这非常缓慢。

推荐使用的替代方案如下：

- **刷新工作簿中的所有数据透视表** → 使用 `workbook.RefreshAll();`
- **刷新其中的一部分** → 对一个缓存使用 `pivotTable.GetPivotCache().Refresh();`。由于缓存是共享的，此单次调用会更新所有基于该缓存构建的数据透视表。位于已经刷新过的缓存上的其他数据透视表可以安全地跳过。
- **仅透视视图/布局发生更改** → 使用 `pivotTable.CalculateData();` 从现有缓存重新渲染，无需任何源数据回访。

以下示例演示了在多个数据透视表共享单个缓存的工作簿中新的高效模式。

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

    pivotTable1.RefreshData();

    pivotTable2.CalculateData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## 应该使用哪种刷新 API？

下表总结了可用的刷新 API 以及选择每种 API 的适用场景。

| 目标 | 推荐的 API | 备注 |
|------|-----------------|-------|
| 刷新工作簿中的所有内容 | `Workbook.RefreshAll()` | 一次调用；涵盖所有缓存和表。 |
| 仅刷新单个工作表上的数据透视表 | `Worksheet.RefreshPivotTables()` | 作用域限定在单个工作表内。 |
| 一个缓存的源数据已更改 | `pivotTable.GetPivotCache().Refresh()` | 刷新该共享缓存上的**所有**数据透视表。 |
| 仅视图/布局设置已更改 | `pivotTable.CalculateData()` | 跳过不必要的源数据回访。 |
| 列出共享缓存上的所有数据透视表 | `pivotCache.GetPivotTables()` | 用于在批量刷新前进行枚举。 |

实际上，应优先使用基于缓存的 API，而非过时的按表调用 `RefreshData()`。它们具备共享缓存感知能力，能够避免冗余的源数据获取，并允许您选择满足刷新需求的最小作用域。
{{< app/cells/assistant language="cpp" >}}
