---
title: 在 Aspose.Cells for Python via Java 中刷新数据透视表
linktitle: 在 Aspose.Cells for Python via Java 中刷新数据透视表
description: 了解如何使用 v26.7+ 的 pivot-refresh API 在 Aspose.Cells for Python via Java 中刷新数据透视表。本文涵盖 RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData 和 GetPivotTables，并提供实用的代码示例。
keywords: Aspose.Cells, Python via Java, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /zh/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 提供了一个分层刷新 API，允许您在四个不同的范围内重新加载透视数据 —— 从整个工作簿到单个数据透视表。从 **Aspose.Cells for Python via Java v26.7** 开始，旧方法 `PivotTable.refreshData()` 被标记为已过时，应替换为本文中描述的更高效的、支持缓存感知的 API。

{{% /alert %}}

## 简介

刷新数据透视表很少是单一的操作。在后台，Aspose.Cells 维护着一个分层的数据链，将您的原始数据源连接到您在工作表中看到的呈现值。理解这个数据链是为任何情况选择正确刷新 API 的关键。

四层数据链如下：

1. **数据源（Data Source）** — 原始数据所在的工作表区域、数据库查询或合并区域。
2. **PivotCache** — 源数据的内存快照。每个数据透视表都建立在 `PivotCache` 之上；所有数据都在此处收集和聚合。
3. **PivotTable** — 定义行、列、值和筛选字段的视图对象。`PivotTable` 仅从其 `PivotCache` 读取数据，*从不*直接从数据源读取。
4. **单元格（Cells）** — `PivotTable` 将其计算的值和样式呈现到的工作表 `Cells`。

一个特别重要的概念是**共享缓存（shared cache）**。当工作簿中的多个数据透视表引用相同的源区域时，它们共享*同一个* `PivotCache` 实例。一个 `PivotCache` 可以被许多数据透视表引用，刷新该缓存将一次性刷新所有依赖的 `PivotTable`。

{{% alert color="primary" %}}

`PivotCache.getSourceType()`（枚举 `PivotTableSourceType`）指示缓存数据的来源。截至 v26.7，`PivotCache.refresh()` 仅支持 **`SHEET`** 和 **`CONSOLIDATION`** 源类型 —— 即存在于工作表区域中的数据。外部源（数据库、外部连接等）尚无法通过缓存 API 进行刷新。

{{% /alert %}}

由于这种链式结构，Aspose.Cells 中存在两条基本的刷新路径：

- **`PivotCache.refresh()`** — 在单个操作中重新加载源 → 缓存并重新计算所有依赖的 `PivotTable`。
- **`PivotTable.calculateData()`** — 从已缓存的数据重新计算单个 `PivotTable` 的显示，无需回溯到数据源。

本文中的所有场景都使用工作表单元格源数据，因此源类型为 `SHEET`，刷新操作按所述方式工作。

## 所需的导入

本文中的所有 Python 示例都依赖以下导入，因为透视类型位于 `aspose.cells.pivot` 命名空间中：

- `import jpype`
- `import aspose.cells as cells`

`jpype` 模块用于引导 JVM，而 `aspose.cells` 公开了贯穿全文使用的工作簿/工作表/单元格/透视类型。

## 刷新工作簿中的所有数据透视表

当您需要确保工作簿中的每个数据透视缓存和每个数据透视表都反映最新的源数据时，最简单、最全面的 API 是 `Workbook.refreshAll()`。单次调用会遍历整个工作簿 —— 刷新每个 `PivotCache` 的源数据，然后重新计算每个依赖的 `PivotTable`。对于不关心性能的一般性、全文档刷新，这是推荐的方法。

下面的示例构建一个包含 Fruit/Year/Amount 源区域的工作簿，创建一个数据透视表，修改一些源值，然后使用 `refreshAll()` 通过单次调用将所有内容更新到最新状态。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# 创建一个新工作簿
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# 将表头行写入单元格 A1:C1
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# 将数据行写入单元格 A2:C9 (跨 2020 和 2021 共 8 行水果数据)
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

# 添加数据透视表:数据源范围 "A1:C9",目标单元格 "E3",名称 "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# 分配数据透视表字段:水果到行,年份到列,数量到数据
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# 修改源数据中的几个数量值以模拟数据变化
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)

# 刷新工作簿中的所有数据透视表/数据透视缓存
workbook.refreshAll()

# 保存工作簿
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## 刷新单个工作表上的所有数据透视表

有时您只需要刷新位于特定工作表上的数据透视表 —— 例如，当已知其他工作表上的数据透视表不相关且不应被触碰时。针对这种情况，Aspose.Cells 提供了 `Worksheet.refreshPivotTables()`，它限定在单个 `Worksheet` 实例范围内。

这比 `Workbook.refreshAll()` 更有选择性：只刷新目标工作表上的数据透视表，不影响其他工作表上的任何数据透视表。

下面的示例填充相同的 Fruit/Year/Amount 源数据，在第一个工作表上添加一个数据透视表，修改一些源值，然后仅刷新该工作表上的数据透视表。

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

## 刷新单个数据透视表

当您希望对单个数据透视表进行细粒度控制时，基于缓存的 API 为您提供了两个选项。它们之间的选择取决于实际更改的内容：底层源数据，还是仅仅是数据透视表本身的视图/布局设置。

### 源数据已更改 — 使用 `PivotCache.refresh()`

如果底层源数据已更改，正确的入口点是 `pivotTable.getPivotCache().refresh()`。此调用将源数据重新读入缓存，然后重新计算依赖于该缓存的每个 `PivotTable`。

{{% alert color="primary" %}}

由于数据透视表共享单个 `PivotCache` 实例，调用 `PivotCache.refresh()` 会重新计算基于该同一缓存构建的**所有**数据透视表 —— 而不仅仅是您引用的那一个。如果两个数据透视表共享相同的源区域，刷新一个缓存会同时刷新两者。

{{% /alert %}}

下面的示例在同一源区域上创建两个数据透视表以演示此共享缓存行为，修改一些源值，然后通过一个缓存引用进行刷新。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# 创建一个新的工作簿并访问第一个工作表
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# 写入表头行：Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# 写入约 9 行数据（grape / blueberry / kiwi / cherry，跨 2020-2021 年）
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
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

# 添加第一个数据透视表 "Pivot1"，锚定在单元格 E3，源数据范围为 A1:C9
pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivotIndex1)

# 为 Pivot1 分配字段
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# 添加第二个数据透视表 "Pivot2"，锚定在 E15，使用相同的源数据范围 A1:C9
# 由于源数据范围相同，Pivot1 和 Pivot2 共享同一个 PivotCache。
pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivotIndex2)

# 为 Pivot2 分配相同的字段
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# 修改源数据中若干 Amount 单元格的值以模拟数据变化
worksheet.getCells().get("C2").putValue(150)
worksheet.getCells().get("C4").putValue(350)
worksheet.getCells().get("C7").putValue(650)

# 刷新共享的 PivotCache。
# 由于 Pivot1 和 Pivot2 共享同一个 PivotCache，此单次调用
# 可同时根据更新后的源数据刷新两个数据透视表（数据 + 样式）。
pivotTable1.getPivotCache().refresh()

# 保存工作簿
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### 仅视图/布局已更改 — 使用 `calculateData()`

如果源数据*未*更改，而只是数据透视表的视图或布局设置已被修改（例如，字段被移动到不同的区域，或者已切换"打开文件时刷新"设置），则无需回溯到数据源。缓存已包含正确的数据；只需重新计算 `PivotTable` 的呈现结果即可。在这种情况下，`pivotTable.calculateData()` 是正确的选择。

这避免了不必要的源获取，并且当许多数据透视表共享同一缓存时，速度明显更快。

下面的示例修改数据透视表的非源属性，然后调用 `calculateData()` 从现有缓存重新呈现它。

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

# 写入 8 行数据（第 2-9 行，匹配源区域 A1:C9）
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

# 添加一个名为 "Pivot1" 的数据透视表，放置在目标单元格 E3，数据源为 A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# 分配字段：Fruit 分配到行，Year 分配到列，Amount 分配到数据
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# 修改视图/布局属性 —— 这只是外观上的更改，
# 因此不需要通过 PivotCache.Refresh() 重新读取源数据。
pivotTable.setRefreshDataOnOpeningFile(False)

# CalculateData() 从 PivotCache 中已保存的数据重新渲染此数据透视表的显示（数据 + 样式）。
# 由于源数据未发生变化，不会执行对源的往返读取 —— 仅将缓存的值重新计算
# 写入工作表单元格中。
pivotTable.calculateData()

# 将工作簿保存到磁盘
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## 获取共享同一 PivotCache 的所有数据透视表

一个工作簿通常包含许多数据透视表，它们都位于一个共享缓存之上。要枚举它们 —— 例如，在执行批量刷新之前，或诊断共享缓存的影响 —— 使用 `PivotCache.getPivotTables()`。此方法返回依赖于给定缓存的每个 `PivotTable` 的集合。

这也是确认两个数据透视表确实共享同一 `PivotCache` 实例的最直接方式：您可以比较缓存引用，或者简单地迭代 `getPivotTables()` 返回的集合并观察其中出现哪些数据透视表。

下面的示例在同一源区域上创建两个数据透视表，验证它们共享同一缓存实例，然后枚举该缓存的数据透视表。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotFieldType

# 移植的代码
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Sheet1")

worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

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
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(900)

pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivot1Index)
pivotTable1.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable1.addFieldToArea(PivotFieldType.DATA, "Amount")

pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivot2Index)
pivotTable2.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable2.addFieldToArea(PivotFieldType.DATA, "Amount")

sameCache = pivotTable1.getPivotCache() is pivotTable2.getPivotCache()
print("Pivot1 and Pivot2 share the same PivotCache: " + str(sameCache))

sharedPivotTables = pivotTable1.getPivotCache().getPivotTables()
print("Number of pivot tables sharing the cache: " + str(len(sharedPivotTables)))

for pt in sharedPivotTables:
    print("Pivot table name: " + pt.getName())

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## 从已过时的 `PivotTable.refreshData()` 迁移

在 Aspose.Cells for Python via Java v26.7 之前，刷新数据透视表的标准方式是对每个数据透视表单独调用 `PivotTable.refreshData()`。从 v26.7 开始，该方法被标记为**已过时**，应替换为上述支持缓存感知的 API。

在现实工作簿中，逐表 `refreshData()` 方法存在两个问题：

- 每次调用时都会从源*重新*获取数据，即使源未发生更改。
- 每次调用都会刷新整个共享缓存。当许多数据透视表共享一个缓存时，重复地对每个数据透视表调用 `refreshData()` 会导致同一缓存被反复重新获取，这非常慢。

推荐的替代方案是：

- **刷新工作簿中的所有数据透视表** → 使用 `workbook.refreshAll();`
- **刷新其中一些** → 对一个缓存使用 `pivotTable.getPivotCache().refresh();`。由于缓存是共享的，此单次调用会更新建立在该缓存之上的每个数据透视表。可以安全地跳过那些基于已刷新缓存的数据透视表。
- **仅数据透视视图/布局已更改** → 使用 `pivotTable.calculateData();` 从现有缓存重新呈现，无需任何源往返。

下面的示例演示了具有多个共享单一缓存的数据透视表的工作簿的新高效模式。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# 创建新工作簿并访问第一个工作表
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# --- 构建源数据：水果 / 年份 / 金额（表头 + 9 行）---
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000)
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000)
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500)
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500)
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000)
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800)
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200)
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700)

# --- 在目标单元格 E3 处添加第一个数据透视表（Pivot1）---
idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = sheet.getPivotTables().get(idx1)
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# --- 在同一源数据范围内添加第二个数据透视表（Pivot2）---
# Pivot1 和 Pivot2 共享同一个底层 PivotCache。
# 这正是旧版按表调用 RefreshData() 方式变得低效的场景：
# 刷新一个表会重新获取整个共享缓存，
# 因此刷新 N 个表就会执行 N 次相同的昂贵获取操作。
idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = sheet.getPivotTables().get(idx2)
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# --- 修改源数据中的若干 Amount 值 ---
sheet.getCells().get("C2").putValue(5000)   # 葡萄 2020
sheet.getCells().get("C5").putValue(7500)   # 樱桃 2020
sheet.getCells().get("C9").putValue(9500)   # 樱桃 2021

# --- 已过时的模式（26.7 之前）— PivotTable.RefreshData() ---
# pivotTable1.RefreshData();  // 从源数据重新获取，刷新整个缓存
# pivotTable2.RefreshData();  // 再次重新获取 — 但缓存已经是新的了！
# 每次调用都会重建共享缓存，因此 N 个表 = N 次冗余获取。

# --- 新的 v26.7+ 模式：刷新缓存一次，然后根据需要重新渲染 ---
# 一次调用 PivotCache.Refresh() 即可将修改后的值拉入共享缓存，
# 并重新计算引用该缓存的所有数据透视表的显示。
# 由于 Pivot1 和 Pivot2 共享同一个 PivotCache，因此这一调用即可更新
# 两个表 — 无需第二次往返源数据。
pivotTable1.getPivotCache().refresh()

# CalculateData() 仅根据缓存中已持有的数据重新渲染数据透视表的显示（数据和样式），
# 不会访问源数据。
# 这里对 Pivot2 调用它纯粹是为了演示 API：缓存刷新一次后，
# 任何依赖该缓存的表都可以重新渲染，无需返回源数据。
# 仅当数据透视表的视图/布局设置发生变化而缓存仍为最新时，
# 才单独使用 CalculateData()。
pivotTable2.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## 我应该使用哪个刷新 API？

下表总结了可用的刷新 API 以及何时选择每个 API。

| 目标 | 推荐的 API | 备注 |
|------|-----------------|-------|
| 刷新工作簿中的所有内容 | `Workbook.refreshAll()` | 单次调用；涵盖所有缓存和表。 |
| 仅刷新单个工作表上的数据透视表 | `Worksheet.refreshPivotTables()` | 限定于单个工作表。 |
| 一个缓存的源数据已更改 | `pivotTable.getPivotCache().refresh()` | 刷新该共享缓存上的所有数据透视表。 |
| 仅视图/布局设置已更改 | `pivotTable.calculateData()` | 跳过不必要的源往返。 |
| 列出共享缓存上的所有数据透视表 | `pivotCache.getPivotTables()` | 用于在批量刷新前进行枚举。 |

实际上，应优先使用基于缓存的 API，而不是已过时的逐表 `refreshData()`。它们能感知共享缓存，避免冗余的源获取，并允许您选择满足刷新需求的最小范围。

{{< app/cells/assistant language="python" >}}