---
title: 在 Aspose.Cells for C++ 中刷新数据透视表和数据透视缓存
linktitle: 在 Aspose.Cells for C++ 中刷新数据透视表和数据透视缓存
description: 学习如何使用 v26.7+ 的数据透视刷新 API 在 Aspose.Cells for C++ 中刷新数据透视表。本文涵盖 RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData 以及 GetPivotTables，并配有实用的代码示例。
keywords: Aspose.Cells, C++, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /zh/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供了一套分层刷新 API，允许您在不同级别上重新加载数据透视数据——从整个工作簿一直细化到单个数据透视表。从 **Aspose.Cells for C++ v26.7** 开始，旧方法 `PivotTable.RefreshData()` 已被标记为过时，应替换为本文所述的更高效、支持缓存的 API。
{{% /alert %}}

## 简介
刷新数据透视表很少是单一操作。在底层，Aspose.Cells 维护一条分层数据链，将您的原始数据源与在工作表中呈现的数值连接起来。理解这条链是针对任何情况选择合适刷新 API 的关键。
该数据链包含四个层次：
1. **数据源（Data Source）**——原始工作表区域、数据库查询或合并区域，原始数据即保存在这里。
2. **PivotCache**——数据源在内存中的快照。每个数据透视表都建立在某个 `PivotCache` 之上；所有数据在这里被收集和聚合。
3. **数据透视表（PivotTable）**——定义行、列、值和筛选字段的视图对象。`PivotTable` *仅*从其 `PivotCache` 读取数据，从不直接读取数据源。
4. **Cells**——工作表的 `Cells`，数据透视表将计算后的数值和样式渲染到其中。

{{% alert color="primary" %}}
`PivotCache.SourceType`（枚举 `PivotTableSourceType`）用于指明缓存数据的来源。自 v26.7 起，`PivotCache.Refresh()` 仅支持 **`Sheet`（工作表）** 和 **`Consolidation`（合并）** 两种源类型——即数据位于工作表区域内的情形。外部数据源（数据库、外部连接等）目前尚无法通过缓存 API 进行刷新。
{{% /alert %}}

由于存在这一数据链，Aspose.Cells 中实际上有两条基本的刷新路径：
- **`PivotTable.CalculateData()`**——根据已经缓存的数据重新计算某个 `PivotTable` 的显示，不回访数据源。
本文中所有场景均使用工作表单元格作为源数据，因此源类型为 `Sheet`，刷新操作的行为与所述一致。

## 快速入门
如果您只需要用最少的代码刷新工作簿中的所有数据透视表，那么一次调用即可：

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

本文后续内容将解释何时应改用范围更小的 API。

## 必需的 Include 指令
由于数据透视表相关类型位于 `Aspose::Cells::Pivot` 命名空间中，本文中的所有 C++ 示例都以以下头文件和命名空间指令开头：
- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`

## 刷新工作簿中所有数据透视表
当您需要确保工作簿中每一个数据透视缓存和每一个数据透视表都反映最新的源数据时，最简单且覆盖面最广的 API 是 `Workbook.RefreshAll()`。单次调用即可遍历整个工作簿——刷新每个 `PivotCache` 的源数据，然后重新计算所有依赖的 `PivotTable`。对于一般性的完整文档刷新（对性能没有特殊要求），推荐使用该方法。
下面的示例构建一个包含 Fruit/Year/Amount 源区域的工作簿，创建一个数据透视表，修改部分源数据，然后通过 `RefreshAll()` 一次调用将所有内容同步到最新状态。

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

## 刷新单个工作表上的所有数据透视表
有时您只需刷新位于特定工作表上的数据透视表——例如，已知其他工作表上的数据透视表与此无关，不应被触碰。针对这种情况，Aspose.Cells 提供了 `Worksheet.RefreshPivotTables()`，其作用范围限定在单个 `Worksheet` 实例内。

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
    // 写入 8 行数据（第 2-9 行，匹配源区域 A1:C9）
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
    // 添加一个名为 "Pivot1" 的数据透视表，放置在目标单元格 E3，数据源为 A1:C9
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    // 分配字段：Fruit 放入行字段，Year 放入列字段，Amount 放入数据字段
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // 修改一个视图/布局属性——这只是外观显示上的更改，
    // 因此不需要通过 PivotCache.Refresh() 重新读取源数据。
    pivotTable.SetRefreshDataOnOpeningFile(false);
    // CalculateData() 会根据 PivotCache 中已有的数据重新呈现当前数据透视表的显示（数据和样式）。
    // 由于源数据未发生更改，因此不会执行到源的往返操作——只会将缓存中的值重新计算到工作表单元格中。
    pivotTable.CalculateData();
    // 将工作簿保存到磁盘
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## 刷新单个数据透视表
当您需要对单个数据透视表进行细粒度控制时，基于缓存的 API 为您提供了两种选项。两者之间的选择取决于实际发生变化的内容：是底层源数据，还是仅仅是数据透视表本身的视图/布局设置。

### 源数据已变更——使用 `PivotCache.Refresh()`
如果底层源数据已经发生变化，正确的入口是 `pivotTable.GetPivotCache().Refresh()`。该调用会重新读取源数据到缓存中，然后重新计算所有依赖该缓存的 `PivotTable`。

### 仅视图/布局发生变化——使用 `CalculateData()`
如果源数据 *并未* 发生变化，仅数据透视表的视图或布局设置被修改（例如，某个字段被移动到不同区域，或切换了打开时刷新的设置），则无需回访数据源。缓存中已经保存着正确的数据；只需要重新计算呈现出来的 `PivotTable`。在这种情况下，`pivotTable.CalculateData()` 是正确的选择。
下面的示例修改数据透视表的某个非源属性，然后调用 `CalculateData()` 依据现有缓存重新渲染该数据透视表。

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

一个工作簿中常常包含多个数据透视表，它们都建立在同一个共享缓存之上。若要枚举它们——例如，在执行批量刷新之前，或诊断共享缓存影响时——可以使用 `PivotCache.GetPivotTables()`。该方法返回所有依赖于指定缓存的 `PivotTable` 集合。

## 从过时的 `PivotTable.RefreshData()` 迁移
在 Aspose.Cells for C++ v26.7 之前，刷新数据透视表的标准方法是对每个数据透视表单独调用 `PivotTable.RefreshData()`。自 v26.7 起，该方法已被标记为 **过时**，应替换为上文所述的、基于缓存的 API。
在真实的工作簿场景中，按表调用 `RefreshData()` 的做法存在两个问题：
- 每次调用都会从源 *重新获取* 数据，即使源数据并没有改变。
推荐的替代方案是：
下面的示例展示了当工作簿中存在多个共享同一缓存的数据透视表时，新的高效模式。

## 应该使用哪种刷新 API？
下表汇总了可用的刷新 API 以及各自适用的场景。
| 目标 | 推荐 API | 说明 |
|------|-----------------|-------|
| 刷新工作簿中的所有内容 | `Workbook.RefreshAll()` | 单次调用；涵盖所有缓存和表。 |
| 仅刷新单个工作表上的数据透视表 | `Worksheet.RefreshPivotTables()` | 作用范围限定于单个工作表。 |
| 单个缓存的源数据已变更 | `pivotTable.GetPivotCache().Refresh()` | 刷新该共享缓存上的 *所有* 数据透视表。 |
| 仅视图/布局设置发生变化 | `pivotTable.CalculateData()` | 跳过不必要的源数据往返。 |
| 列出共享缓存上的所有数据透视表 | `pivotCache.GetPivotTables()` | 用于在批量刷新前枚举。 |
实际应用中，应优先选择基于缓存的 API，而非过时的逐表 `RefreshData()`。这些 API 能够识别共享缓存，可避免冗余的源数据获取，并允许您选择能够满足刷新需求的最小作用域。

## 常见陷阱
- **保存前忘记刷新。** 只有在数据透视表的数据链被刷新后，它才会将渲染后的值写入工作表。如果修改了源单元格，在调用 `Workbook.Save()` 之前应调用 `PivotCache.Refresh()`（或 `Workbook.RefreshAll()`），否则保存的文件仍将包含旧的聚合值。
- **仍按表调用过时的 `RefreshData()`。** 在 v26.7 中，`PivotTable.RefreshData()` 已被标记为过时，并且每次调用都会重新获取源数据。当多个数据透视表共享同一缓存时，这意味着会产生 N 次冗余的源数据获取。应替换为对共享缓存调用一次 `PivotCache.Refresh()`，再对每个表调用 `CalculateData()`。
- **仅布局变化时仍然执行刷新。** 如果只是修改了数据透视表的视图（列顺序、`ConsolidationFunction` 等），而未触碰源数据，那么 `PivotCache.Refresh()` 既不必要也会拖慢性能。请调用 `pivotTable.CalculateData()` 依据已有缓存重新渲染即可。
- **外部数据源不受 `PivotCache.Refresh()` 支持。** 如果数据透视表的源数据来自外部连接（数据库、OLAP 多维数据集等），则在 v26.7 中 `PivotCache.Refresh()` 无法刷新它——目前仅支持 `Sheet` 和 `Consolidation` 两种源类型。对于外部数据源，请重新打开工作簿或从源端重建缓存。

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="cpp" >}}