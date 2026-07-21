---
title: 在 Aspose.Cells for Python via .NET 中刷新数据透视表
linktitle: 在 Aspose.Cells for Python via .NET 中刷新数据透视表
description: 介绍如何使用 v26.7+ 的 pivot-refresh API 在 Aspose.Cells for Python via .NET 中刷新数据透视表。本文涵盖 RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData 和 GetPivotTables，并附带实用的代码示例
keywords: Aspose.Cells, Python via .NET, 数据透视表, 刷新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /zh/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 提供了一套分层刷新 API，使您能够在四个不同层级上重新加载数据透视数据——从整个工作簿到单个数据透视表。从 **Aspose.Cells for Python via .NET v26.7** 开始，旧方法 `PivotTable.refresh_data()` 已被标记为过时，应替换为本文中介绍的更高效、支持缓存的 API。

{{% /alert %}}

## 简介

刷新数据透视表很少是一个单一的操作。在后台，Aspose.Cells 维护着一套分层的数据链，将您的原始源数据连接到工作表中呈现的值。理解这条数据链是根据具体情况选择正确刷新 API 的关键。

四层数据链如下：

1. **数据源** — 原始工作表区域、数据库查询或合并区域，用于存放原始值。
2. **PivotCache** — 源数据在内存中的快照。每个数据透视表都构建在一个 `PivotCache` 之上；所有数据的汇总和聚合都在此处完成。
3. **数据透视表** — 定义行、列、值和筛选字段的视图对象。`PivotTable` *仅* 从其 `PivotCache` 读取数据，而不会直接从数据源读取。
4. **单元格** — 数据透视表将其计算后的值和样式渲染到的工作表 `Cells`。

一个特别重要的概念是**共享缓存**。当工作簿中的多个数据透视表引用相同的源区域时，它们共享*同一个* `PivotCache` 实例。一个 `PivotCache` 可以被多个数据透视表引用，刷新该缓存会一次性刷新所有依赖它的 `PivotTable`。

{{% alert color="primary" %}}

`PivotCache.source_type`（枚举 `PivotTableSourceType`）指示缓存数据来自何处。从 v26.7 开始，`PivotCache.refresh()` 仅支持 **`Sheet`** 和 **`Consolidation`** 源类型——即存放在工作表区域中的数据。外部源（数据库、外部连接等）目前还无法通过缓存 API 进行刷新。

{{% /alert %}}

由于存在这条数据链，Aspose.Cells 中有两种基本的刷新路径：

- **`PivotCache.refresh()`** — 在一次操作中重新加载源→缓存，并重新计算所有依赖的 `PivotTable`。
- **`PivotTable.calculate_data()`** — 从已缓存的数据重新计算单个 `PivotTable` 的显示，不回访数据源。

本文中的所有场景都使用工作表单元格作为源数据，因此源类型为 `Sheet`，刷新操作的行为如上所述。

## 所需的导入语句

本文中的所有 Python 示例都以以下三条导入语句开头，因为数据透视表相关的类型位于 `aspose.cells.pivot` 命名空间中：

- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## 刷新工作簿中的所有数据透视表

当您需要确保工作簿中的每个数据透视缓存和每个数据透视表都反映最新的源数据时，最简单、最全面的 API 是 `Workbook.refresh_all()`。单次调用会遍历整个工作簿——刷新每个 `PivotCache` 的源数据，然后重新计算每个依赖的 `PivotTable`。在对性能没有严格要求的常规、整文档刷新场景下，推荐使用此方法。

以下示例构建了一个包含 Fruit/Year/Amount 源区域的工作簿，创建一个数据透视表，修改一些源数据值，然后通过单次调用 `refresh_all()` 将所有内容更新到最新状态。

```python
import aspose.cells as ac

# 创建一个新的工作簿
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

# 添加一个数据透视表：数据源范围 "A1:C9"，目标单元格 "E3"，名称 "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# 分配数据透视字段：Fruit 到行，Year 到列，Amount 到数据
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# 修改源数据中的几个 Amount 值以模拟数据变更
worksheet.cells["C2"].put_value(55)
worksheet.cells["C5"].put_value(85)
worksheet.cells["C9"].put_value(125)

# 刷新工作簿中的所有数据透视表/数据透视缓存
workbook.refresh_all()

# 保存工作簿
workbook.save("output.xlsx")
```

## 刷新单个工作表上的所有数据透视表

有时您只需要刷新位于特定工作表上的数据透视表——例如，已知其他工作表上的数据透视表与此无关，无需触动。针对这种情况，Aspose.Cells 提供了 `Worksheet.refresh_pivot_tables()`，其作用范围限定为单个 `Worksheet` 实例。

与 `Workbook.refresh_all()` 相比，此方法更具选择性：仅刷新目标工作表上的数据透视表，其他工作表上的数据透视表保持不变。

以下示例填充相同的 Fruit/Year/Amount 源数据，在第一个工作表上添加一个数据透视表，修改一些源数据值，然后仅刷新该工作表上的数据透视表。

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

当您需要对单个数据透视表进行精细控制时，基于缓存的 API 提供了两种选择。两者之间的选择取决于实际发生变化的内容：底层源数据发生了变化，还是仅仅是数据透视表本身的视图/布局设置发生了变化。

### 源数据发生变化——使用 `PivotCache.refresh()`

如果底层源数据发生了变化，正确的入口点是 `pivot_table.pivot_cache.refresh()`。此调用会将源数据重新读入缓存，然后重新计算所有依赖该缓存的 `PivotTable`。

{{% alert color="primary" %}}

由于数据透视表共享同一个 `PivotCache` 实例，调用 `PivotCache.refresh()` 会重新计算构建在该缓存上的**所有**数据透视表——而不仅仅是您引用的那一个。如果两个数据透视表共享相同的源区域，刷新一个缓存会同时刷新两者。

{{% /alert %}}

以下示例在相同的源区域上创建两个数据透视表以演示这种共享缓存行为，修改一些源数据值，然后通过一个缓存引用执行刷新。

```python
import aspose.cells as ac

# 创建一个新工作簿并访问第一个工作表
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# 写入表头行：水果 / 年份 / 数量
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# 写入约 9 行数据（葡萄 / 蓝莓 / 猕猴桃 / 樱桃，跨 2020-2021 年）
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

# 添加第一个数据透视表 "Pivot1"，锚定在 E3 单元格，数据源范围为 A1:C9
pivotIndex1 = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.pivot_tables[pivotIndex1]

# 为 Pivot1 分配字段
pivotTable1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# 添加第二个数据透视表 "Pivot2"，锚定在 E15，使用相同的数据源范围 A1:C9
# 由于数据源范围相同，Pivot1 和 Pivot2 共享一个 PivotCache。
pivotIndex2 = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.pivot_tables[pivotIndex2]

# 为 Pivot2 分配相同的字段
pivotTable2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# 修改源数据中几个 Amount 单元格的值以模拟数据变更
worksheet.cells["C2"].put_value(150)
worksheet.cells["C4"].put_value(350)
worksheet.cells["C7"].put_value(650)

# 刷新共享的 PivotCache。
# 由于 Pivot1 和 Pivot2 共享同一个 PivotCache，此单次调用
# 会从更新后的数据源刷新两个数据透视表（数据 + 样式）。
pivotTable1.pivot_cache.refresh()

# 保存工作簿
workbook.save("output.xlsx")
```

### 仅视图/布局发生变化——使用 `calculate_data()`

如果源数据*没有*发生变化，而只是修改了数据透视表的视图或布局设置（例如，将某个字段移至不同的区域，或者切换了"打开文件时刷新"设置），则无需回访数据源。缓存中已经保存了正确的数据；只需要重新计算渲染后的 `PivotTable`。在这种情况下，`pivot_table.calculate_data()` 是正确的选择。

这避免了不必要的源数据获取，当许多数据透视表共享同一缓存时，速度显著提升。

以下示例修改数据透视表的非源属性，然后调用 `calculate_data()` 从现有缓存重新渲染。

```python
import aspose.cells as ac
import aspose.cells.pivot as acp

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# 写入 Fruit / Year / Amount 表头行
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# 写入 8 行数据（第 2-9 行，对应源数据范围 A1:C9）
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

# 添加名为 "Pivot1" 的数据透视表，放置在目标单元格 E3，数据源为 A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# 分配字段：Fruit 作为行，Year 作为列，Amount 作为数据
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")

# 修改视图/布局属性——这只是显示层面的更改，
# 因此不需要通过 PivotCache.Refresh() 重新读取源数据。
pivot_table.refresh_data_on_opening_file = False

# CalculateData() 会从 PivotCache 中已保存的数据重新渲染该数据透视表的显示（数据 + 样式）。
# 由于源数据未发生更改，因此不会执行与源数据的往返过程——仅将缓存中的值重新计算到工作表单元格中。
pivot_table.calculate_data()

# 将工作簿保存到磁盘
workbook.save("output.xlsx")
```

## 获取共享同一 PivotCache 的所有数据透视表

一个工作簿中通常包含许多构建在同一共享缓存之上的数据透视表。若要枚举它们——例如在执行批量刷新之前，或者诊断共享缓存的影响——可以使用 `PivotCache.get_pivot_tables()`。此方法返回依赖给定缓存的所有 `PivotTable` 的集合。

这也是确认两个数据透视表确实共享同一 `PivotCache` 实例的最直接方式：您可以比较缓存引用，或者简单地遍历 `get_pivot_tables()` 返回的集合，观察其中出现哪些数据透视表。

以下示例在相同的源区域上创建两个数据透视表，验证它们共享同一个缓存实例，然后枚举该缓存的数据透视表。

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

## 从已过时的 `PivotTable.refresh_data()` 迁移

在 Aspose.Cells for Python via .NET v26.7 之前，刷新数据透视表的标准方式是对每个数据透视表单独调用 `PivotTable.refresh_data()`。从 v26.7 开始，该方法被标记为**过时**，应替换为上文介绍的、支持缓存的 API。

逐表调用 `refresh_data()` 的方式在实际工作簿中存在两个问题：

- 它*每次*调用时都会重新从源获取数据，即使源数据并未发生变化。
- 每次调用都会刷新整个共享缓存。当多个数据透视表共享一个缓存时，反复对每个数据透视表调用 `refresh_data()` 会导致同一个缓存被反复重新获取，速度非常慢。

推荐使用的替代方式如下：

- **刷新工作簿中的所有数据透视表** → 使用 `workbook.refresh_all();`
- **刷新其中的部分数据透视表** → 对一个缓存使用 `pivot_table.pivot_cache.refresh();`。由于缓存是共享的，此单次调用会更新构建在该缓存上的所有数据透视表。其他已经构建在已刷新缓存上的数据透视表可以安全地跳过。
- **仅数据透视表的视图/布局发生变化** → 使用 `pivot_table.calculate_data();` 从现有缓存重新渲染，无需回访源。

以下示例演示了在多个数据透视表共享单一缓存的工作簿中新的高效模式。

```python
import aspose.cells as ac

# 创建一个新工作簿并访问第一个工作表
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# --- 构建源数据：水果 / 年份 / 金额（表头 + 9 行） ---
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

# --- 在目标单元格 E3 处添加第一个数据透视表（Pivot1） ---
idx1 = sheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = sheet.pivot_tables[idx1]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- 在同一源数据范围内添加第二个数据透视表（Pivot2） ---
# Pivot1 和 Pivot2 共享同一个底层 PivotCache。
# 这正是旧的逐表调用 RefreshData() 方法变得低效的场景：
# 刷新一个表会重新获取整个共享缓存，
# 因此刷新 N 个表会重复执行 N 次相同的昂贵获取操作。
idx2 = sheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = sheet.pivot_tables[idx2]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- 修改源数据中的几个 Amount 值 ---
sheet.cells["C2"].put_value(5000)   # 葡萄  2020
sheet.cells["C5"].put_value(7500)   # 樱桃 2020
sheet.cells["C9"].put_value(9500)   # 樱桃 2021

# --- 已废弃的模式（26.7 之前）— PivotTable.RefreshData() ---
# pivot_table1.refresh_data();  # 从源数据重新获取，刷新整个缓存
# pivot_table2.refresh_data();  # 再次重新获取——但缓存已经是新数据了！
# 每次调用都会重建共享缓存，因此 N 个表意味着 N 次冗余的获取操作。

# --- 新的 v26.7+ 模式：刷新缓存一次，然后根据需要重新渲染 ---
# 调用一次 PivotCache.Refresh() 即可将修改后的值拉入共享缓存，
# 并重新计算所有引用该缓存的数据透视表的显示结果。
# 由于 Pivot1 和 Pivot2 共享同一个 PivotCache，
# 这一调用即可同时更新两个表——无需再次访问源数据。
pivot_table1.pivot_cache.refresh()

# CalculateData() 仅根据缓存中已有的数据重新渲染数据透视表的显示（数据和样式），
# 它不会访问源数据。
# 此处对 Pivot2 调用该方法仅为演示 API：在缓存刷新一次之后，
# 任何依赖该缓存的表都可以在不重新访问源数据的情况下重新渲染。
# 仅当数据透视表的视图/布局设置发生变化、且缓存已是最新数据时，可单独使用 CalculateData()。
pivot_table2.calculate_data()

workbook.save("output.xlsx")
```

## 应该使用哪个刷新 API？

下表总结了可用的刷新 API 以及各自的适用场景。

| 目标 | 推荐的 API | 备注 |
|------|-----------------|-------|
| 刷新工作簿中的所有内容 | `Workbook.refresh_all()` | 单次调用，覆盖所有缓存和表。 |
| 仅刷新单个工作表上的数据透视表 | `Worksheet.refresh_pivot_tables()` | 限定为单个工作表。 |
| 一个缓存的源数据发生变化 | `pivot_table.pivot_cache.refresh()` | 刷新该共享缓存上的所有数据透视表。 |
| 仅视图/布局设置发生变化 | `pivot_table.calculate_data()` | 跳过不必要的源数据回访。 |
| 列出共享缓存上的所有数据透视表 | `pivot_cache.get_pivot_tables()` | 在批量刷新之前用于枚举。 |

在实际应用中，应优先使用基于缓存的 API，而非过时的逐表 `refresh_data()`。这些 API 能够识别共享缓存，可避免冗余的源数据获取，并允许您选择满足刷新需求的最小范围。
{{< app/cells/assistant language="python" >}}
