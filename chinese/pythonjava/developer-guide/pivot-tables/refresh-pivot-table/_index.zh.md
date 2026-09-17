---
title: 在 Aspose.Cells for Python via Java 中刷新数据透视表和数据透视缓存
linktitle: 在 Aspose.Cells for Python via Java 中刷新数据透视表和数据透视缓存
description: 了解如何使用 v26.7+ 数据透视刷新 API 在 Aspose.Cells for Python via Java 中刷新数据透视表。本文涵盖 RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData 和 GetPivotTables，并附有实用的代码示例。
keywords: Aspose.Cells, Python via Java, 数据透视表, 刷新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /zh/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供了一个分层刷新 API，使您可以在四个不同的范围内重新加载透视数据——从整个工作簿到单个数据透视表。从 **Aspose.Cells for Python via Java v26.7** 开始，旧方法 `PivotTable.refreshData()` 已被标记为过时，应替换为本文中介绍的更高效、支持缓存的 API。
{{% /alert %}}

## 简介
刷新数据透视表很少是单一操作。在后台，Aspose.Cells 维护着一个分层的数据链，将您的原始数据源连接到工作表中呈现的数值。理解这条数据链是为任何场景选择正确刷新 API 的关键。
四层数据链如下：
1. **数据源** — 原始的工作表区域、数据库查询或合并区域，原始值存放在此。
2. **PivotCache** — 数据源在内存中的快照。每个数据透视表都构建在一个 `PivotCache` 之上；所有数据都在这里进行收集和聚合。
3. **PivotTable** — 定义行、列、值和筛选字段的视图对象。`PivotTable` *仅* 从其 `PivotCache` 读取数据，从不直接从数据源读取。
4. **Cells** — 工作表的 `Cells`，`PivotTable` 将其计算后的值和样式渲染到这些单元格中。

{{% alert color="primary" %}}
`PivotCache.getSourceType()`（枚举 `PivotTableSourceType`）指示缓存数据的来源。截至 v26.7，`PivotCache.refresh()` 仅支持 **`SHEET`** 和 **`CONSOLIDATION`** 源类型——即存放在工作表区域中的数据。外部数据源（数据库、外部连接等）目前尚无法通过缓存 API 进行刷新。
{{% /alert %}}

由于这种数据链，Aspose.Cells 中存在两条基本的刷新路径：
- **`PivotTable.calculateData()`** — 使用已缓存的数据重新计算单个 `PivotTable` 的显示，无需往返数据源。
本文中的所有场景均使用工作表单元格作为源数据，因此源类型为 `SHEET`，刷新操作的行为如所述。

## 快速开始
如果您只需要用尽可能短的代码来刷新工作簿中的每个数据透视表，那么一次调用就足够了：

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
# 创建一个新的工作簿
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# 将表头行写入 A1:C1 单元格
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# 将数据行写入 A2:C9 单元格（2020 和 2021 年 8 行水果数据）
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(50)
worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(60)
worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(70)
worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(80)
worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(90)
worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(100)
worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(110)
worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(120)
# 添加数据透视表：数据源范围 "A1:C9"，目标单元格 "E3"，名称 "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# 分配数据透视字段：Fruit 到行，Year 到列，Amount 到数据
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
# 修改源数据中的几个 Amount 值以模拟变化
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)
# 刷新工作簿中的所有数据透视表 / 数据透视缓存
workbook.refreshAll()
# 保存工作簿
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

本文其他部分将解释何时应选择范围更窄的 API。

## 所需导入
本文中的所有 Python 示例都依赖于以下导入，因为透视类型位于 `aspose.cells.pivot` 命名空间中：
- `import jpype`
- `import aspose.cells as cells`
`jpype` 模块用于引导 JVM，而 `aspose.cells` 提供了贯穿全文使用的工作簿/工作表/单元格/透视类型。

## 刷新工作簿中的所有数据透视表
当您需要确保工作簿中的每个数据透视缓存和每个数据透视表都反映最新的源数据时，最简单且最全面的 API 是 `Workbook.refreshAll()`。单次调用即可遍历整个工作簿——刷新每个 `PivotCache` 的数据源，然后重新计算每个依赖的 `PivotTable`。对于一般性的、不在意性能的全文档刷新，推荐使用此方法。
下面的示例构建了一个包含 Fruit/Year/Amount 源区域的工作簿，创建一个数据透视表，修改一些源值，然后使用 `refreshAll()` 通过一次调用使所有内容保持最新。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2021)
worksheet.getCells().get("C3").putValue(150)
worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)
worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2021)
worksheet.getCells().get("C5").putValue(120)
worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(180)
worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2020)
worksheet.getCells().get("C7").putValue(130)
worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(220)
worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2020)
worksheet.getCells().get("C9").putValue(140)
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
worksheet.getCells().get("C2").putValue(300)
worksheet.getCells().get("C5").putValue(250)
worksheet.getCells().get("C9").putValue(400)
worksheet.refreshPivotTables()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## 刷新单个工作表上的所有数据透视表
有时您只需要刷新位于特定工作表上的数据透视表——例如，当已知其他工作表上的数据透视表与此无关且不应被触碰时。对于这种情况，Aspose.Cells 提供了 `Worksheet.refreshPivotTables()`，其范围限定于单个 `Worksheet` 实例。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# 写入 Fruit / Year / Amount 表头行
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# 写入 8 行数据（第 2-9 行，匹配源数据范围 A1:C9）
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(150)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(250)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(350)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(450)
# 添加一个名为 "Pivot1" 的数据透视表，目标单元格为 E3，数据源为 A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# 分配字段：Fruit 到行，Year 到列，Amount 到数据
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
# 修改视图/布局属性——这只是一个表现层的更改，
# 因此不需要通过 PivotCache.Refresh() 重新读取源数据。
pivotTable.setRefreshDataOnOpeningFile(False)
# CalculateData() 会从 PivotCache 中已保存的数据
# 重新渲染此数据透视表的显示（数据 + 样式）。由于源数据未发生变化，
# 不会回溯到源数据——只将缓存中的值重新计算
# 输出到工作表单元格中。
pivotTable.calculateData()
# 将工作簿保存到磁盘
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## 刷新单个数据透视表
当您希望对单个数据透视表进行细粒度控制时，基于缓存的 API 为您提供了两种选择。选择哪一种取决于实际更改的内容：底层源数据，还是仅数据透视表本身的视图/布局设置。

### 源数据已更改 — 使用 `PivotCache.refresh()`
如果底层源数据已更改，则正确的入口点是 `pivotTable.getPivotCache().refresh()`。此调用会将源数据重新读取到缓存中，然后重新计算依赖于该缓存的每个 `PivotTable`。

### 仅视图/布局已更改 — 使用 `calculateData()`
如果源数据*未*更改，但仅修改了数据透视表的视图或布局设置（例如，将某个字段移动到不同的区域，或切换了打开时刷新设置），则无需往返数据源。缓存中已包含正确的数据；只需重新计算呈现的 `PivotTable`。在这种情况下，`pivotTable.calculateData()` 是正确的选择。
下面的示例修改了数据透视表的非源属性，然后调用 `calculateData()` 从现有缓存中重新渲染它。
一个工作簿通常包含许多共享同一缓存的数据透视表。要枚举它们——例如在执行批量刷新之前，或诊断共享缓存的影响——请使用 `PivotCache.getPivotTables()`。此方法返回依赖于给定缓存的每个 `PivotTable` 的集合。

## 从已过时的 `PivotTable.refreshData()` 迁移
在 Aspose.Cells for Python via Java v26.7 之前，刷新数据透视表的标准方法是对每个数据透视表分别调用 `PivotTable.refreshData()`。从 v26.7 开始，该方法被标记为**过时**，应替换为上文介绍的、支持缓存的 API。
在真实工作簿中，逐表调用 `refreshData()` 的方法存在两个问题：
- 每次调用时都会从源*重新*获取数据，即使源未发生更改。
推荐使用的替代方法如下：
下面的示例演示了对于多个共享单一缓存的数据透视表的工作簿，使用新的高效模式。

## 应使用哪种刷新 API？
下表总结了可用的刷新 API 以及选择每种 API 的时机。
| 目标 | 推荐的 API | 备注 |
|------|-----------------|-------|
| 刷新工作簿中的所有内容 | `Workbook.refreshAll()` | 一次调用；涵盖所有缓存和数据透视表。 |
| 仅刷新单个工作表上的数据透视表 | `Worksheet.refreshPivotTables()` | 范围限定于单个工作表。 |
| 一个缓存的源数据已更改 | `pivotTable.getPivotCache().refresh()` | 刷新该共享缓存上的所有数据透视表。 |
| 仅视图/布局设置已更改 | `pivotTable.calculateData()` | 跳过不必要的源数据往返。 |
| 列出共享缓存上的所有数据透视表 | `pivotCache.getPivotTables()` | 用于在批量刷新前进行枚举。 |
在实践中，应优先使用基于缓存的 API，而非已过时的逐表 `refreshData()`。它们能够识别共享缓存，可避免冗余的源数据获取，并允许您选择满足刷新需求的最小范围。

## 常见陷阱
- **保存前忘记刷新。** 数据透视表仅在其数据链被刷新后才会将其呈现的值写入工作表。如果您修改了源单元格，请在 `Workbook.save()` 之前调用 `PivotCache.Refresh()`（或 `Workbook.RefreshAll()`），否则保存的文件仍将包含旧的聚合值。
- **对每个表调用已过时的 `RefreshData()`。** 在 v26.7 中，`PivotTable.RefreshData()` 已被标记为过时，并且每次调用都会重新获取源数据。当多个数据透视表共享一个缓存时，这意味着 N 次冗余的源数据获取。应替换为对每个表进行一次 `PivotCache.Refresh()`，然后对每个表调用 `CalculateData()`。
- **仅布局更改时进行刷新。** 如果您仅更改了数据透视表的视图（列顺序、`ConsolidationFunction` 等）而未触及源数据，则 `PivotCache.Refresh()` 不必要且速度较慢。调用 `pivotTable.CalculateData()` 从现有缓存重新渲染。
- **外部源不受 `PivotCache.Refresh()` 支持。** 如果数据透视表的源来自外部连接（数据库、OLAP 多维数据集等），则在 v26.7 中 `PivotCache.Refresh()` 无法刷新它——它目前仅支持 `Sheet` 和 `Consolidation` 源类型。对于外部源，请重新打开工作簿或从源重建缓存。

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="python" >}}