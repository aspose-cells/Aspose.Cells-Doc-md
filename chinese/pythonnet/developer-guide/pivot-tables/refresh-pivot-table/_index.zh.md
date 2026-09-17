---
title: 在 Aspose.Cells for Python via .NET 中刷新数据透视表和数据透视缓存
linktitle: 在 Aspose.Cells for Python via .NET 中刷新数据透视表和数据透视缓存
description: 学习如何使用 v26.7+ 的数据透视刷新 API 在 Aspose.Cells for Python via .NET 中刷新数据透视表。本文涵盖 RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData 以及 GetPivotTables，并附带实用的代码示例。
keywords: Aspose.Cells, Python via .NET, 数据透视表, 刷新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /zh/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供了一套分层刷新 API，允许您在四个不同的范围内重新加载数据透视数据——从整个工作簿到单个数据透视表。从 **Aspose.Cells for Python via .NET v26.7** 起，旧版方法 `PivotTable.refresh_data()` 已被标记为过时，应替换为本文中介绍的更高效、支持缓存的 API。
{{% /alert %}}

## 简介
刷新数据透视表很少是一个单一的操作。在后台，Aspose.Cells 维护着一套分层的数据链，将原始源数据与工作表中呈现的数值连接起来。理解这条数据链是针对不同场景选择合适刷新 API 的关键。
这条四层数据链包括：
1. **数据源（Data Source）** —— 原始工作表区域、数据库查询或合并区域，原始数据就存放在这里。
2. **PivotCache** —— 源数据在内存中的快照。每个数据透视表都建立在某个 `PivotCache` 之上；所有数据的汇总与聚合都在此处完成。
3. **PivotTable** —— 视图对象，用于定义行、列、值和筛选字段。`PivotTable` *仅* 从其 `PivotCache` 读取数据，从不直接访问数据源。
4. **Cells** —— 工作表中的 `Cells`，`PivotTable` 将计算结果和样式渲染到这些单元格中。

{{% alert color="primary" %}}
`PivotCache.source_type`（枚举 `PivotTableSourceType`）用于指示缓存数据的来源。自 v26.7 起，`PivotCache.refresh()` 仅支持 **`Sheet`** 和 **`Consolidation`** 这两种源类型——也就是说，仅支持来自工作表区域的数据。外部源（数据库、外部连接等）目前尚无法通过缓存 API 进行刷新。
{{% /alert %}}

由于存在这条数据链，Aspose.Cells 中存在两条根本不同的刷新路径：
- **`PivotTable.calculate_data()`** —— 仅基于已缓存的数据重新计算单个 `PivotTable` 的显示结果，不会回访数据源。
本文中的所有场景都使用工作表单元格作为源数据，因此源类型为 `Sheet`，刷新操作的行为也符合上述说明。

## 快速上手
如果您只需要用尽可能少的代码来刷新工作簿中所有的数据透视表，那么一次调用就够了：

```python
import aspose.cells as ac
# 创建一个新的工作簿
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# 将表头行写入单元格 A1:C1
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
# 将数据行写入单元格 A2:C9（2020 年和 2021 年的 8 行水果数据）
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
# 添加数据透视表：数据源区域 "A1:C9"，目标单元格 "E3"，名称 "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# 分配数据透视字段：Fruit 到行，Year 到列，Amount 到数据
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
# 修改数据源中的若干 Amount 值以模拟变化
worksheet.cells["C2"].put_value(55)
worksheet.cells["C5"].put_value(85)
worksheet.cells["C9"].put_value(125)
# 刷新工作簿中的所有数据透视表 / 数据透视缓存
workbook.refresh_all()
# 保存工作簿
workbook.save("output.xlsx")
```

本文其余部分将解释在何时应该改用范围更窄的 API。

## 必需的导入语句
本文中所有 Python 示例都以以下三条导入语句开头，因为相关的数据透视类型位于 `aspose.cells.pivot` 命名空间下：
- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## 刷新工作簿中的所有数据透视表
当您需要确保工作簿中的每个数据透视缓存和每个数据透视表都反映最新的源数据时，最简单、最全面的 API 是 `Workbook.refresh_all()`。一次调用即可遍历整个工作簿——刷新每个 `PivotCache` 的源数据，然后重新计算所有依赖的 `PivotTable`。对于一般的、全文档范围的刷新（不考虑性能），这是推荐的做法。
下面的示例构建了一个包含 Fruit/Year/Amount 源区域的工作簿，创建一个数据透视表，修改部分源数据，然后通过 `refresh_all()` 一次性将所有内容更新到最新状态。

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

## 刷新单个工作表上的所有数据透视表
有时您只需要刷新位于某一特定工作表上的数据透视表——例如，已知其他工作表上的数据透视表与此无关，不应被影响。针对这种情况，Aspose.Cells 提供了 `Worksheet.refresh_pivot_tables()`，其作用范围仅限于单个 `Worksheet` 实例。

```python
import aspose.cells as ac
import aspose.cells.pivot as acp
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# 写入 Fruit / Year / Amount 表头行
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
# 写入 8 行数据（第 2-9 行，匹配数据源区域 A1:C9）
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
# 添加名为 "Pivot1" 的数据透视表，目标单元格为 E3，数据源为 A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# 分配字段：Fruit 到行，Year 到列，Amount 到数据
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")
# 修改视图/布局属性 — 这只是显示上的更改，
# 因此不需要通过 PivotCache.Refresh() 重新读取源数据。
pivot_table.refresh_data_on_opening_file = False
# CalculateData() 重新渲染此数据透视表的显示（数据和样式），使用
# PivotCache 中已持有的数据。因为源数据没有变化，
# 不会执行到源数据的往返 — 只有缓存值会被重新计算
# 到工作表单元格中。
pivot_table.calculate_data()
# 将工作簿保存到磁盘
workbook.save("output.xlsx")
```

## 刷新单个数据透视表
当您希望对单个数据透视表进行细粒度控制时，基于缓存的 API 为您提供了两种选择。选择哪种取决于实际变更的内容：是底层源数据发生了变更，还是仅仅是数据透视表自身的视图或布局设置发生了变化。

### 源数据发生变更 —— 使用 `PivotCache.refresh()`
如果底层源数据发生了变更，正确的入口是 `pivot_table.pivot_cache.refresh()`。该调用会将源数据重新读入缓存，然后重新计算所有依赖该缓存的 `PivotTable`。

### 仅视图或布局发生变更 —— 使用 `calculate_data()`
如果源数据 *没有* 发生变化，而只是修改了数据透视表的视图或布局设置（例如，将某个字段移动到不同区域，或者切换了"打开时刷新"设置），那么无需回访数据源。缓存中已经保存了正确的数据；只需重新计算呈现的 `PivotTable` 即可。在这种情况下，`pivot_table.calculate_data()` 是正确的选择。
下面的示例修改了数据透视表的一个非源属性，然后调用 `calculate_data()`，从已有缓存中重新渲染该数据透视表。
一个工作簿中常常包含多个数据透视表，它们都建立在同一个共享缓存之上。若要枚举这些数据透视表——例如在执行批量刷新之前，或用于诊断共享缓存的影响——可以使用 `PivotCache.get_pivot_tables()`。该方法返回所有依赖于指定缓存的 `PivotTable` 集合。

## 从已弃用的 `PivotTable.refresh_data()` 进行迁移
在 Aspose.Cells for Python via .NET v26.7 之前，刷新数据透视表的标准方式是对每个数据透视表单独调用 `PivotTable.refresh_data()`。从 v26.7 起，该方法被标记为 **已弃用**，应替换为上文介绍的、支持缓存的 API。
在真实的工作簿场景中，逐表调用 `refresh_data()` 的方式存在两个问题：
- 它 *每次* 调用都会重新从源获取数据，即使源数据并未发生变化。
推荐使用的替代方法如下：
下面的示例演示了当工作簿中存在多个共享同一缓存的数据透视表时，新的高效模式。

## 应该使用哪种刷新 API？
下表汇总了可用的刷新 API 以及各自的适用场景。
| 目标 | 推荐 API | 说明 |
|------|-----------------|-------|
| 刷新工作簿中的全部内容 | `Workbook.refresh_all()` | 一次调用，覆盖所有缓存和数据透视表。 |
| 仅刷新单个工作表上的数据透视表 | `Worksheet.refresh_pivot_tables()` | 范围限定于单个工作表。 |
| 某个缓存的源数据发生变更 | `pivot_table.pivot_cache.refresh()` | 刷新该共享缓存上的所有数据透视表。 |
| 仅视图或布局设置发生变更 | `pivot_table.calculate_data()` | 跳过不必要的源数据回访。 |
| 列出共享缓存上的所有数据透视表 | `pivot_cache.get_pivot_tables()` | 用于在批量刷新前进行枚举。 |
在实际应用中，应优先使用基于缓存的 API，而不是已弃用的逐表 `refresh_data()`。这些 API 知道共享缓存的存在，可以避免冗余的源数据获取，并允许您选择满足刷新需求的最小范围。

## 常见陷阱
- **在保存前忘记刷新。** 数据透视表仅在其数据链被刷新后才会将呈现值写入工作表。如果修改了源单元格，请在 `Workbook.save()` 之前调用 `PivotCache.Refresh()`（或 `Workbook.RefreshAll()`），否则保存的文件中仍然包含旧的聚合值。
- **对每个表调用已弃用的 `RefreshData()`。** 在 v26.7 中，`PivotTable.RefreshData()` 已被标记为过时，并且每次调用都会重新获取源数据。当多个数据透视表共享同一缓存时，这意味着会产生 N 次冗余的源数据获取。应替换为对缓存执行一次 `PivotCache.Refresh()`，然后对每个数据透视表执行 `CalculateData()`。
- **仅布局变更时仍然进行刷新。** 如果只是修改了数据透视表的视图（列顺序、`ConsolidationFunction` 等），而未触碰源数据，那么 `PivotCache.Refresh()` 既不必要也会很慢。应调用 `pivotTable.CalculateData()`，从已有缓存重新渲染。
- **`PivotCache.Refresh()` 不支持外部源。** 如果数据透视表的源来自外部连接（数据库、OLAP 多维数据集等），在 v26.7 中 `PivotCache.Refresh()` 无法对其进行刷新——目前仅支持 `Sheet` 和 `Consolidation` 两种源类型。对于外部源，请重新打开工作簿或从源端重建缓存。

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="python-net" >}}