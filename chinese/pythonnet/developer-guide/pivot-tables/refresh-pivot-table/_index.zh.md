---
title: 在 Aspose.Cells for Python via .NET 中刷新数据透视表
linktitle: 在 Aspose.Cells for Python via .NET 中刷新数据透视表
description: 学习如何使用 v26.7+ 数据透视表刷新 API 在 Aspose.Cells for Python via .NET 中刷新数据透视表。本文涵盖 RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData 和 GetPivotTables，并附有实用的代码示例。
keywords: Aspose.Cells, Python via .NET, 数据透视表, 刷新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /zh/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells 提供了一个分层刷新 API，允许您在四个不同的范围内重新加载透视数据——从整个工作簿到单个数据透视表。从 **Aspose.Cells for Python via .NET v26.7** 开始，旧方法 `PivotTable.refresh_data()` 被标记为过时，应替换为本文描述的更高效、感知缓存的 API。
{{% /alert %}}
## 简介
刷新数据透视表很少是单一操作。在后台，Aspose.Cells 维护了一个分层的数据链，将您的原始源数据连接到工作表中呈现的值。理解这个数据链是为任何场景选择正确的刷新 API 的关键。
四层数据链如下：
1. **数据源** — 原始工作表区域、数据库查询或合并区域，其中存放着原始值。
2. **PivotCache** — 源数据的内存快照。每个数据透视表都构建在 `PivotCache` 之上；所有数据都在此处进行收集和聚合。
3. **PivotTable** — 定义行、列、值和筛选字段的视图对象。`PivotTable` 仅从其 `PivotCache` 读取数据，从不直接从数据源读取。
4. **Cells** — 工作表的 `Cells`，`PivotTable` 将其计算值和样式呈现到这些单元格中。
一个特别重要的概念是**共享缓存**。当工作簿中的多个数据透视表引用相同的源区域时，它们共享*同一个* `PivotCache` 实例。一个 `PivotCache` 可以被多个数据透视表引用，刷新该缓存会一次性刷新每个依赖的 `PivotTable`。
{{% alert color="primary" %}}
`PivotCache.source_type`（枚举类型 `PivotTableSourceType`）指示缓存数据来自何处。从 v26.7 开始，`PivotCache.refresh()` 仅支持 **`Sheet`** 和 **`Consolidation`** 源类型——即存放在工作表区域中的数据。外部源（数据库、外部连接等）尚无法通过缓存 API 进行刷新。
{{% /alert %}}
由于这个数据链的存在，Aspose.Cells 中有两条基本的刷新路径：
- **`PivotCache.refresh()`** — 在单个操作中重新加载源 → 缓存并重新计算所有依赖的 `PivotTable`。
- **`PivotTable.calculate_data()`** — 从已缓存的数据重新计算一个 `PivotTable` 的显示，无需回溯到数据源。
本文中的所有场景都使用工作表单元格源数据，因此源类型为 `Sheet`，刷新操作如描述的那样执行。
## 必需的导入
本文中的所有 Python 示例都以以下三条导入语句开头，因为透视类型位于 `aspose.cells.pivot` 命名空间中：
## 刷新工作簿中的所有数据透视表
当您需要确保工作簿中的每个数据透视缓存和每个数据透视表都反映最新的源数据时，最简单和最全面的 API 是 `Workbook.refresh_all()`。单次调用即可遍历整个工作簿——从其源刷新每个 `PivotCache`，然后重新计算每个依赖的 `PivotTable`。对于性能不是问题的一般性、全文档刷新，推荐使用此方法。
以下示例构建了一个包含 Fruit/Year/Amount 源区域的工作簿，创建一个数据透视表，修改一些源值，然后使用 `refresh_all()` 通过单次调用使所有内容保持最新。
```python
import aspose.cells as ac

# 创建一个新工作簿
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# 将表头行写入单元格 A1:C1
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# 将数据行写入单元格 A2:C9（2020 和 2021 年共 8 行水果数据）
worksheet.cells["A2"].put_value("grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(50)

worksheet.cells["A3"].put_value("blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(60)

worksheet.cells["A4"].put_value("kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(70)

worksheet.cells["A5"].put_value("cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(80)

worksheet.cells["A6"].put_value("grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(90)

worksheet.cells["A7"].put_value("blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(100)

worksheet.cells["A8"].put_value("kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(110)

worksheet.cells["A9"].put_value("cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(120)

# 添加数据透视表：数据源区域为 "A1:C9"，目标单元格为 "E3"，名称为 "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# 分配透视字段：Fruit 到行，Year 到列，Amount 到数据
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# 修改源数据中的几个 Amount 值以模拟数据变化
worksheet.cells["C2"].put_value(55)
worksheet.cells["C5"].put_value(85)
worksheet.cells["C9"].put_value(125)

# 刷新工作簿中的所有数据透视表/透视缓存
workbook.refresh_all()

# 保存工作簿
workbook.save("output.xlsx")
```
## 刷新单个工作表上的所有数据透视表
有时您只需要刷新位于特定工作表上的数据透视表——例如，当已知其他工作表上的数据透视表与之无关且不应被触碰时。对于这种情况，Aspose.Cells 提供了 `Worksheet.refresh_pivot_tables()`，其范围限定在单个 `Worksheet` 实例。
这比 `Workbook.refresh_all()` 更有选择性：仅刷新目标工作表上的数据透视表，其他工作表上的任何数据透视表都不会被触碰。
以下示例填充相同的 Fruit/Year/Amount 源数据，在第一个工作表上添加一个数据透视表，修改一些源值，然后仅刷新该工作表上的数据透视表。
```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("blueberry")
worksheet.cells["B3"].put_value(2021)
worksheet.cells["C3"].put_value(150)

worksheet.cells["A4"].put_value("kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(200)

worksheet.cells["A5"].put_value("cherry")
worksheet.cells["B5"].put_value(2021)
worksheet.cells["C5"].put_value(120)

worksheet.cells["A6"].put_value("grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(180)

worksheet.cells["A7"].put_value("blueberry")
worksheet.cells["B7"].put_value(2020)
worksheet.cells["C7"].put_value(130)

worksheet.cells["A8"].put_value("kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(220)

worksheet.cells["A9"].put_value("cherry")
worksheet.cells["B9"].put_value(2020)
worksheet.cells["C9"].put_value(140)

pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

worksheet.cells["C2"].put_value(300)
worksheet.cells["C5"].put_value(250)
worksheet.cells["C9"].put_value(400)

worksheet.refresh_pivot_tables()

workbook.save("output.xlsx")
```
## 刷新单个数据透视表
当您希望对单个数据透视表进行细粒度控制时，基于缓存的 API 为您提供了两个选项。它们之间的选择取决于实际更改的内容：底层源数据，还是仅数据透视表本身的视图/布局设置。
### 源数据已更改 — 使用 `PivotCache.refresh()`
如果底层源数据已更改，正确的入口点是 `pivot_table.pivot_cache.refresh()`。此调用会将源数据重新读取到缓存中，然后重新计算依赖于该缓存的每个 `PivotTable`。
{{% alert color="primary" %}}
由于数据透视表共享同一个 `PivotCache` 实例，调用 `PivotCache.refresh()` 会重新计算基于该相同缓存构建的**所有**数据透视表——而不仅仅是您引用的那一个。如果两个数据透视表共享相同的源区域，刷新一个缓存将同时刷新两者。
{{% /alert %}}
以下示例在同一源区域上创建两个数据透视表以演示这种共享缓存行为，修改一些源值，然后通过一个缓存引用进行刷新。
```python
import aspose.cells as ac

# 创建一个新工作簿并访问第一个工作表
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# 写入表头行：水果 / 年份 / 数量
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# 写入大约9行数据（2020-2021年间的葡萄/蓝莓/猕猴桃/樱桃）
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

# 添加第一个数据透视表"Pivot1"，锚定在E3单元格，源数据范围为A1:C9
pivotIndex1 = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.pivot_tables[pivotIndex1]

# 为Pivot1分配字段
pivotTable1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# 添加第二个数据透视表"Pivot2"，锚定在E15单元格，使用相同的源数据范围A1:C9
# 因为源数据范围相同，Pivot1和Pivot2共享同一个PivotCache。
pivotIndex2 = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.pivot_tables[pivotIndex2]

# 为Pivot2分配相同的字段
pivotTable2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# 修改源数据中几个数量单元格的值以模拟数据变化
worksheet.cells["C2"].put_value(150)
worksheet.cells["C4"].put_value(350)
worksheet.cells["C7"].put_value(650)

# 刷新共享的PivotCache。
# 因为Pivot1和Pivot2共享同一个PivotCache，所以这一次调用
# 会从更新后的源数据同时刷新两个数据透视表（数据+样式）。
pivotTable1.pivot_cache.refresh()

# 保存工作簿
workbook.save("output.xlsx")
```
### 仅视图/布局已更改 — 使用 `calculate_data()`
如果源数据*没有*更改，但仅修改了数据透视表的视图或布局设置（例如，将字段移动到不同的区域，或切换打开文件时刷新的设置），则无需回溯到数据源。缓存已经保存了正确的数据；只需要重新计算呈现的 `PivotTable`。在这种情况下，`pivot_table.calculate_data()` 是正确的选择。
这避免了不必要的源获取，当多个数据透视表共享同一缓存时，速度会显著加快。
以下示例修改数据透视表的非源属性，然后调用 `calculate_data()` 从现有缓存重新呈现它。
```python
import aspose.cells as ac
import aspose.cells.pivot as acp

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# 写入 Fruit / Year / Amount 表头行
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# 写入 8 行数据（第 2-9 行，对应源数据区域 A1:C9）
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(150)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(250)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(350)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(450)

# 添加一个名为 "Pivot1" 的数据透视表，目标单元格为 E3，数据源为 A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# 分配字段：Fruit 放入行字段，Year 放入列字段，Amount 放入数据字段
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")

# 修改视图/布局属性——这仅是外观层面的更改，
# 因此不需要通过 PivotCache.Refresh() 重新读取源数据。
pivot_table.refresh_data_on_opening_file = False

# CalculateData() 会从 PivotCache 中已缓存的数据重新渲染该数据透视表的显示（数据和样式）。
# 由于源数据未发生更改，不会执行与源的往返交互——只会将缓存的值重新计算到工作表单元格中。
pivot_table.calculate_data()

# 将工作簿保存到磁盘
workbook.save("output.xlsx")
```
## 获取共享同一 PivotCache 的所有数据透视表
一个工作簿通常包含许多都基于同一共享缓存的数据透视表。要枚举它们——例如，在执行批量刷新之前，或诊断共享缓存的影响——请使用 `PivotCache.get_pivot_tables()`。此方法返回依赖于给定缓存的每个 `PivotTable` 的集合。
这也是确认两个数据透视表确实共享同一 `PivotCache` 实例的最直接方法：您可以比较缓存引用，或简单地遍历 `get_pivot_tables()` 返回的集合，观察其中出现的数据透视表。
以下示例在同一源区域上创建两个数据透视表，验证它们共享同一缓存实例，然后枚举缓存的数据透视表。
```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Sheet1"

worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(900)

pivot1_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = worksheet.pivot_tables[pivot1_index]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

pivot2_index = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = worksheet.pivot_tables[pivot2_index]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

same_cache = pivot_table1.pivot_cache is pivot_table2.pivot_cache
print("Pivot1 and Pivot2 share the same PivotCache: " + str(same_cache))

shared_pivot_tables = pivot_table1.pivot_cache.get_pivot_tables()
print("Number of pivot tables sharing the cache: " + str(len(shared_pivot_tables)))

for pt in shared_pivot_tables:
    print("Pivot table name: " + pt.name)

workbook.save("output.xlsx")
```
## 从过时的 `PivotTable.refresh_data()` 迁移
在 Aspose.Cells for Python via .NET v26.7 之前，刷新数据透视表的标准方法是对每个数据透视表单独调用 `PivotTable.refresh_data()`。从 v26.7 开始，该方法被标记为**过时**，应替换为上述感知缓存的 API。
在真实工作簿中，按表调用的 `refresh_data()` 方法存在两个问题：
- 每次调用时都会从源重新获取数据，即使源没有更改也是如此。
- 每次调用都会刷新整个共享缓存。当多个数据透视表共享一个缓存时，重复对每个数据透视表调用 `refresh_data()` 会导致同一缓存被反复重新获取，这非常慢。
推荐的替代方案是：
- **刷新工作簿中的所有数据透视表** → 使用 `workbook.refresh_all();`
- **刷新其中的一部分** → 对一个缓存使用 `pivot_table.pivot_cache.refresh();`。由于缓存是共享的，此单次调用会更新构建在该缓存之上的每个数据透视表。位于已刷新缓存上的其他数据透视表可以安全地跳过。
- **仅透视视图/布局已更改** → 使用 `pivot_table.calculate_data();` 从现有缓存重新呈现，无需任何源回溯。
以下示例演示了针对多个共享单个缓存的数据透视表工作簿的新高效模式。
```python
import aspose.cells as ac

# 创建一个新工作簿并访问第一个工作表
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# --- 构建源数据：Fruit / Year / Amount（表头 + 9 行数据）---
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

sheet.cells["A2"].put_value("Grape")      ; sheet.cells["B2"].put_value(2020); sheet.cells["C2"].put_value(1000)
sheet.cells["A3"].put_value("Blueberry")  ; sheet.cells["B3"].put_value(2020); sheet.cells["C3"].put_value(2000)
sheet.cells["A4"].put_value("Kiwi")       ; sheet.cells["B4"].put_value(2020); sheet.cells["C4"].put_value(1500)
sheet.cells["A5"].put_value("Cherry")     ; sheet.cells["B5"].put_value(2020); sheet.cells["C5"].put_value(2500)
sheet.cells["A6"].put_value("Grape")      ; sheet.cells["B6"].put_value(2021); sheet.cells["C6"].put_value(3000)
sheet.cells["A7"].put_value("Blueberry")  ; sheet.cells["B7"].put_value(2021); sheet.cells["C7"].put_value(1800)
sheet.cells["A8"].put_value("Kiwi")       ; sheet.cells["B8"].put_value(2021); sheet.cells["C8"].put_value(2200)
sheet.cells["A9"].put_value("Cherry")     ; sheet.cells["B9"].put_value(2021); sheet.cells["C9"].put_value(2700)

# --- 在目标单元格 E3 处添加第一个数据透视表（Pivot1）---
idx1 = sheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = sheet.pivot_tables[idx1]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- 在同一源数据范围上添加第二个数据透视表（Pivot2）---
# Pivot1 和 Pivot2 共享同一个底层的 PivotCache。
# 这正是旧版逐表调用 RefreshData() 方式效率低下的典型场景：
# 刷新一个表会重新获取整个共享缓存，
# 因此刷新 N 个表就会执行 N 次同样昂贵的获取操作。
idx2 = sheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = sheet.pivot_tables[idx2]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- 修改源数据中的若干 Amount 值 ---
sheet.cells["C2"].put_value(5000)   # Grape  2020
sheet.cells["C5"].put_value(7500)   # Cherry 2020
sheet.cells["C9"].put_value(9500)   # Cherry 2021

# --- 已过时的模式（26.7 之前）— PivotTable.RefreshData() ---
# pivot_table1.refresh_data();  # 从源数据重新获取，并刷新整个缓存
# pivot_table2.refresh_data();  # 再次重新获取 — 此时缓存其实已经是最新的了！
# 每次调用都会重建共享缓存，因此 N 个表就意味着 N 次冗余的获取操作。

# --- 新的 v26.7+ 模式：只需刷新缓存一次，然后按需重新渲染 ---
# 只需调用一次 PivotCache.Refresh()，即可将修改后的值加载到共享缓存中，
# 并重新计算所有引用该缓存的数据透视表的显示内容。
# 由于 Pivot1 和 Pivot2 共享同一个 PivotCache，这一个调用即可同时更新
# 两个表 —— 无需再次访问源数据。
pivot_table1.pivot_cache.refresh()

# CalculateData() 仅根据缓存中已有的数据重新渲染数据透视表的显示
# （数据 + 样式），不会访问源数据。
# 这里在 Pivot2 上调用它纯粹是为了演示 API：在缓存刷新一次之后，
# 任何依赖该缓存的表都可以无需回访源数据即可重新渲染。
# 当仅更改了数据透视表的视图/布局设置且缓存为最新状态时，
# 可单独使用 CalculateData()。
pivot_table2.calculate_data()

workbook.save("output.xlsx")
```
## 应该使用哪种刷新 API？
下表总结了可用的刷新 API 以及何时选择每个 API。
| 目标 | 推荐 API | 备注 |
|------|-----------------|-------|
| 刷新工作簿中的所有内容 | `Workbook.refresh_all()` | 单次调用；涵盖所有缓存和表。 |
| 仅刷新单个工作表上的数据透视表 | `Worksheet.refresh_pivot_tables()` | 范围限定于一个工作表。 |
| 一个缓存的源数据已更改 | `pivot_table.pivot_cache.refresh()` | 刷新该共享缓存上的所有数据透视表。 |
| 仅视图/布局设置已更改 | `pivot_table.calculate_data()` | 跳过不必要的源回溯。 |
| 列出共享缓存上的所有数据透视表 | `pivot_cache.get_pivot_tables()` | 用于在批量刷新前枚举。 |
在实践中，应优先使用基于缓存的 API，而不是过时的按表 `refresh_data()`。它们了解共享缓存，避免冗余的源获取，并允许您选择满足刷新要求的最小范围。
## 相关文章
- [Aspose.Cells for Python via .NET 中的迷你图](/cells/zh/python-net/sparkline/)
{{< app/cells/assistant language="python" >}}