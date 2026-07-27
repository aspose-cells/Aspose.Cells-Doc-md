---
title: 在 Aspose.Cells for Python via Java 中刷新数据透视表
linktitle: 在 Aspose.Cells for Python via Java 中刷新数据透视表
description: 了解如何使用 v26.7+ 透视刷新 API 在 Aspose.Cells for Python via Java 中刷新数据透视表。本文涵盖 RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData 和 GetPivotTables，并附有实用的代码示例。
keywords: Aspose.Cells, Python via Java, 数据透视表, 刷新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /zh/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 提供了一套分层刷新 API，使您能够在四个不同的作用域内重新加载透视数据 — 从整个工作簿到单个数据透视表。从 **Aspose.Cells for Python via Java v26.7** 起，旧版方法 `PivotTable.refreshData()` 已被标记为过时，应替换为本文中介绍的更高效、感知缓存的 API。

{{% /alert %}}

## 简介

刷新数据透视表很少是一个单一的操作。在后台，Aspose.Cells 维护着一个分层的数据链，该链将您的原始源数据连接到您在工作表中看到的渲染值。理解这条数据链是针对任何情况选择合适刷新 API 的关键。

四层数据链如下：

1. **数据源** — 原始数据所在的工作表区域、数据库查询或合并区域。
2. **PivotCache** — 源数据的内存快照。每个数据透视表都构建在一个 `PivotCache` 之上；这是所有数据被收集和聚合的位置。
3. **数据透视表 (PivotTable)** — 定义行、列、值和筛选字段的视图对象。`PivotTable` 仅从其 `PivotCache` 读取数据，从不直接从数据源读取。
4. **单元格 (Cells)** — `PivotTable` 将其计算后的值和样式渲染到的工作表 `Cells`。

一个特别重要的概念是 **共享缓存**。当工作簿中的多个数据透视表引用相同的源区域时，它们共享 *一个* `PivotCache` 实例。一个 `PivotCache` 可以被多个数据透视表引用，刷新该缓存即可一次性刷新所有依赖的 `PivotTable`。

{{% alert color="primary" %}}

`PivotCache.getSourceType()`（枚举 `PivotTableSourceType`）指示缓存数据的来源。自 v26.7 起，`PivotCache.refresh()` 仅支持 **`SHEET`** 和 **`CONSOLIDATION`** 两种源类型，即存储在工作表区域中的数据。外部源（数据库、外部连接等）目前尚无法通过缓存 API 进行刷新。

{{% /alert %}}

由于这种链式结构，Aspose.Cells 中存在两条基本的刷新路径：

- **`PivotCache.refresh()`** — 重新加载源数据到缓存，并在一次操作中重新计算所有依赖的 `PivotTable`。
- **`PivotTable.calculateData()`** — 仅基于已缓存的数据重新计算单个 `PivotTable` 的显示，无需回访数据源。

本文中的所有场景均使用工作表单元格作为源数据，因此源类型为 `SHEET`，刷新操作的行为如上所述。

## 必需的导入

本文中的所有 Python 示例都依赖于以下导入，因为透视表相关类型位于 `aspose.cells.pivot` 命名空间中：

- `import jpype`
- `import aspose.cells as cells`

`jpype` 模块用于引导 JVM，而 `aspose.cells` 提供了贯穿全文所用的 workbook/worksheet/cell/pivot 类型。

## 刷新工作簿中的所有数据透视表

当您需要确保工作簿中的每个透视缓存和每个数据透视表都反映最新的源数据时，最简单且最全面的 API 是 `Workbook.refreshAll()`。一次调用即可遍历整个工作簿 — 从每个 `PivotCache` 的源刷新数据，然后重新计算每个依赖的 `PivotTable`。在对性能没有特别要求的一般性、全文档刷新场景下，推荐使用此方法。

以下示例构建一个包含 Fruit/Year/Amount 源区域的工作簿，创建一个数据透视表，修改部分源值，然后使用 `refreshAll()` 一次调用即可使所有内容保持最新。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# 创建一个新的工作簿
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# 将表头行写入单元格 A1:C1
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# 将数据行写入单元格 A2:C9 (2020 和 2021 年的 8 行水果数据)
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

# 添加数据透视表: 源区域 "A1:C9", 目标单元格 "E3", 名称 "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# 分配数据透视字段: Fruit 到行, Year 到列, Amount 到数据
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# 修改源数据中几个 Amount 的值以模拟更改
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)

# 刷新工作簿中的所有数据透视表 / 数据透视缓存
workbook.refreshAll()

# 保存工作簿
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## 刷新单个工作表上的所有数据透视表

有时您只需要刷新位于特定工作表上的数据透视表 — 例如，当其他工作表上的数据透视表已知与之无关且不应被刷新时。对于这种情况，Aspose.Cells 提供了 `Worksheet.refreshPivotTables()`，其作用范围限定在单个 `Worksheet` 实例上。

这比 `Workbook.refreshAll()` 更加具有针对性：仅刷新目标工作表上的数据透视表，其他工作表上的数据透视表保持不变。

以下示例填充相同的 Fruit/Year/Amount 源数据，在第一个工作表上添加一个数据透视表，修改部分源值，然后仅刷新该工作表上的数据透视表。

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

当您需要对单个数据透视表进行细粒度控制时，基于缓存的 API 提供了两种选项。它们之间的选择取决于实际发生变化的内容：是底层源数据，还是仅数据透视表本身的视图/布局设置。

### 源数据已更改 — 使用 `PivotCache.refresh()`

如果底层源数据已更改，正确的入口是 `pivotTable.getPivotCache().refresh()`。此调用将源数据重新读取到缓存中，然后重新计算依赖于该缓存的所有 `PivotTable`。

{{% alert color="primary" %}}

由于数据透视表共享同一个 `PivotCache` 实例，调用 `PivotCache.refresh()` 会重新计算基于同一缓存构建的 **所有** 数据透视表 — 而不仅仅是您引用的那个。如果两个数据透视表共享相同的源区域，刷新一个缓存即可同时刷新两者。

{{% /alert %}}

以下示例在同一源区域上创建两个数据透视表，以演示这种共享缓存行为，修改部分源值，然后通过一个缓存引用进行刷新。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# 创建新工作簿并访问第一个工作表
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# 写入表头行：水果 / 年份 / 金额
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# 写入大约 9 行数据（葡萄 / 蓝莓 / 猕猴桃 / 樱桃，跨 2020-2021 年）
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

# 添加第一个数据透视表 "Pivot1"，锚定在 E3 单元格，源数据区域为 A1:C9
pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivotIndex1)

# 为 Pivot1 分配字段
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# 添加第二个数据透视表 "Pivot2"，锚定在 E15，使用相同的源数据区域 A1:C9
# 由于源数据区域相同，Pivot1 和 Pivot2 共享同一个 PivotCache。
pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivotIndex2)

# 为 Pivot2 分配相同的字段
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# 修改源数据中若干金额单元格的值，以模拟数据变化
worksheet.getCells().get("C2").putValue(150)
worksheet.getCells().get("C4").putValue(350)
worksheet.getCells().get("C7").putValue(650)

# 刷新共享的 PivotCache。
# 由于 Pivot1 和 Pivot2 共享同一个 PivotCache，这一个调用
# 会同时刷新两个数据透视表（数据和样式）的源数据。
pivotTable1.getPivotCache().refresh()

# 保存工作簿
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### 仅视图/布局已更改 — 使用 `calculateData()`

如果源数据 *未* 发生更改，但仅修改了数据透视表的视图或布局设置（例如，某个字段被移动到不同的区域，或切换了打开文件时刷新的设置），则无需回访数据源。缓存中已包含正确的数据；只需重新计算已渲染的 `PivotTable`。在这种情况下，`pivotTable.calculateData()` 是正确的选择。

这样可以避免不必要的源数据获取，当多个数据透视表共享同一个缓存时，速度提升尤为明显。

以下示例修改数据透视表的非源属性，然后调用 `calculateData()` 从现有缓存重新渲染。

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

# 写入 8 行数据（第 2-9 行，与源数据范围 A1:C9 对应）
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

# 添加一个名为 "Pivot1" 的数据透视表，目标单元格为 E3，源数据范围为 A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# 分配字段：Fruit 到行，Year 到列，Amount 到数据
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# 修改视图/布局属性 —— 这只是显示上的更改，
# 因此不需要通过 PivotCache.Refresh() 重新读取源数据。
pivotTable.setRefreshDataOnOpeningFile(False)

# CalculateData() 会从 PivotCache 中已缓存的数据重新渲染当前数据透视表的显示（数据 + 样式）。
# 由于源数据没有更改，不会执行与源数据的往返操作 —— 只会将缓存值重新计算到工作表单元格中。
pivotTable.calculateData()

# 将工作簿保存到磁盘
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## 获取共享同一个 PivotCache 的所有数据透视表

一个工作簿通常包含许多数据透视表，它们都建立在同一个共享缓存之上。要枚举它们 — 例如，在执行批量刷新之前，或诊断共享缓存影响 — 请使用 `PivotCache.getPivotTables()`。此方法返回依赖于给定缓存的所有 `PivotTable` 的集合。

这也是确认两个数据透视表确实共享同一个 `PivotCache` 实例的最直接方式：您可以比较缓存引用，或者简单地遍历 `getPivotTables()` 返回的集合，观察其中包含哪些数据透视表。

以下示例在同一源区域上创建两个数据透视表，验证它们共享同一个缓存实例，然后枚举该缓存下的数据透视表。

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

## 从过时的 `PivotTable.refreshData()` 迁移

在 Aspose.Cells for Python via Java v26.7 之前，刷新数据透视表的标准方式是对每个数据透视表单独调用 `PivotTable.refreshData()`。自 v26.7 起，该方法已被标记为 **过时**，应替换为上文所述的基于缓存的 API。

在真实工作簿中，按表调用 `refreshData()` 的方式存在两个问题：

- 每次调用时都会从源 *重新* 获取数据，即使源数据未发生变化。
- 每次调用都会刷新整个共享缓存。当多个数据透视表共享一个缓存时，对每个数据透视表反复调用 `refreshData()` 会导致同一缓存被反复重新获取，速度非常慢。

推荐使用的替代方案如下：

- **刷新工作簿中的所有数据透视表** → 使用 `workbook.refreshAll();`
- **刷新其中部分数据透视表** → 针对一个缓存使用 `pivotTable.getPivotCache().refresh();`。由于缓存是共享的，这一次性调用即可更新基于该缓存构建的所有数据透视表。位于已刷新缓存上的其他数据透视表可以安全地跳过。
- **仅数据透视表的视图/布局发生更改** → 使用 `pivotTable.calculateData();` 从现有缓存重新渲染，无需任何源数据往返。

以下示例演示了在多个数据透视表共享单个缓存的工作簿中使用新的高效模式。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# 创建一个新工作簿并访问第一个工作表
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# --- 构建源数据：水果 / 年份 / 金额 (表头 + 9 行) ---
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

# --- 在目标单元格 E3 添加第一个数据透视表 (Pivot1) ---
idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = sheet.getPivotTables().get(idx1)
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# --- 在同一源范围上添加第二个数据透视表 (Pivot2) ---
# Pivot1 和 Pivot2 共享同一个底层 PivotCache。
# 这正是每个表调用 RefreshData() 的旧式方法
# 变得低效的场景：刷新一个表会重新获取整个
# 共享缓存，因此刷新 N 个表会执行 N 次相同的昂贵获取操作。
idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = sheet.getPivotTables().get(idx2)
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# --- 修改源数据中的几个金额值 ---
sheet.getCells().get("C2").putValue(5000)   # 葡萄  2020
sheet.getCells().get("C5").putValue(7500)   # 樱桃 2020
sheet.getCells().get("C9").putValue(9500)   # 樱桃 2021

# --- 旧模式 (26.7 之前) — PivotTable.RefreshData() ---
# pivotTable1.RefreshData();  // 从源重新获取数据，刷新整个缓存
# pivotTable2.RefreshData();  // 再次重新获取 — 缓存已经是新的！
# 每次调用都重建共享缓存，因此 N 个表 = N 次冗余获取。

# --- 新版 v26.7+ 模式：仅刷新一次缓存，然后根据需要重新渲染 ---
# 一次调用 PivotCache.Refresh() 将修改后的值拉取到共享
# 缓存中，并重新计算引用它的每个数据透视表的显示。
# 因为 Pivot1 和 Pivot2 共享一个 PivotCache，所以这单个调用会更新
# 两个表 — 无需第二次往返源数据。
pivotTable1.getPivotCache().refresh()

# CalculateData() 仅重新渲染数据透视表的显示（数据和样式）
# 来自缓存中已保存的数据 — 它不会触及源。
# 我们在这里对 Pivot2 调用它纯粹是为了演示 API：在缓存
# 已刷新一次之后，任何依赖表都可以被重新渲染，
# 而无需返回源。仅当数据透视表的视图/布局设置
# 发生更改且缓存是最新的时，才单独使用 CalculateData()。
pivotTable2.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## 应该使用哪种刷新 API？

下表总结了可用的刷新 API 以及每种 API 的适用场景。

| 目标 | 推荐的 API | 说明 |
|------|-----------------|-------|
| 刷新工作簿中的所有内容 | `Workbook.refreshAll()` | 一次调用即可覆盖所有缓存和数据透视表。 |
| 仅刷新单个工作表上的数据透视表 | `Worksheet.refreshPivotTables()` | 作用范围限定在单个工作表内。 |
| 一个缓存的源数据已更改 | `pivotTable.getPivotCache().refresh()` | 刷新该共享缓存上的所有数据透视表。 |
| 仅视图/布局设置已更改 | `pivotTable.calculateData()` | 跳过不必要的源数据往返。 |
| 列出共享缓存上的所有数据透视表 | `pivotCache.getPivotTables()` | 用于在批量刷新前进行枚举。 |

在实际应用中，建议优先使用基于缓存的 API，而不是已过时的按表调用 `refreshData()`。这些 API 感知共享缓存，可避免冗余的源数据获取，并允许您选择满足刷新需求的最小作用域。

## 相关文章

- [向单元格中插入图像](/cells/zh/python-java/inserting-an-image-into-a-cell/)
- [读取和写入 DBF 文件](/cells/zh/python-java/dbf/)
- [将 Excel 文件拆分为多个文件](/cells/zh/python-java/splitting-excel-files-into-multiple-files/)
- [Aspose.Cells for Python via Java 中的迷你图](/cells/zh/python-java/sparkline/)

{{< app/cells/assistant language="python" >}}