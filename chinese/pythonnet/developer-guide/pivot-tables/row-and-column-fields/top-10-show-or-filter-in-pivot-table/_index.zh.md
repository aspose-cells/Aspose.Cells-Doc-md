---
title: 在数据透视表中显示或筛选前 10 项
linktitle: 在数据透视表中显示或筛选前 10 项
description: 了解如何通过 .NET 使用 Aspose.Cells for Python，仅显示数据透视字段中排名最高或最低的项目。本文介绍 Excel 97-2003 的 top_10_auto_show 方法、使用 top_10_auto_show_settings 读取选项，以及通过 filter_top10 实现 Excel 2007-365 前 10 项筛选。
keywords: Aspose.Cells, Python via .NET, 数据透视表, 前 10 项, 自动显示, top_10_auto_show, top_10_auto_show_settings, PivotFieldTop10AutoShowSettings, filter_top10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /zh/python-net/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
当行字段包含数十个项目时，列出所有项目的数据透视表可能难以阅读。前 10 项报表仅保留排名最高或最低的项目，这正符合排名报表的需求，例如“按收入排名前 5 的产品”或“销售数量最低的 3 个地区”。Aspose.Cells 支持两种机制，分别对应 Microsoft Excel 的两个版本代次。
- **Excel 97-2003 自动显示** — `PivotField.top_10_auto_show()` 方法。这是经典的“显示前/后 N 个项目”设置，直接存储在数据透视字段上。由于它属于最初的数据透视表格式的一部分，因此适用于所有新旧 Excel 版本。
- **Excel 2007-365 前 10 项筛选** — `PivotField.filter_top10()` 方法。这是字段菜单“值筛选”下的现代前 10 项值筛选。它以附加到字段的 `PivotFilter` 对象形式存储，支持按项目数或百分比进行排名。

## **Excel 97-2003 中的前 10 项显示（top_10_auto_show）**
只需调用一次 `PivotField.top_10_auto_show(bool is_auto_show, bool is_top, int count, int rank_by)`，即可配置经典自动显示功能：
- `is_auto_show` — 启用或禁用字段上的自动显示设置。
- `is_top` — `True` 保留排名最高的项目（前），`False` 保留排名最低的项目（后）。
- `count` — 要保留的项目数量，例如经典前 10 项报表可设为 10。
- `rank_by` — 数据字段的从 0 开始的索引，该字段的值用于对项目进行排名。传入 -1 表示按字段自身进行排名。
排名依据可以是值字段，也可以是字段本身。下面介绍两种常用方式。

### **按值字段进行排名**
可使用常规值字段（例如“销售额合计”）对行字段中的项目进行排名。以下示例创建一个数据透视表，其中包含一个行字段（`Sport`）和一个数据字段（`Sales`），然后按销售额显示排名前 2 的体育项目。由于“销售额合计”是索引为 0 的数据字段，因此 `rank_by` 为 0。

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
# 显示按“Sum of Sales”排名的前 2 个项目（数据字段索引 0）
sport_field.top_10_auto_show(True, True, 2, 0)
pivot_table.calculate_data()
workbook.save("output-top10-by-value-field.xlsx")
```

### **按字段自身进行排名**
字段也可以按自身进行排名——将 -1 作为 `rank_by` 传入。此变体不需要额外的数据字段；该字段只需位于行（或列）区域即可。以下示例显示按字段自身进行排名的后 3 个体育项目。保存此设置时，数据透视表 XML 中会省略 `rank_by` 属性，因为 -1 是该格式的默认值，而 `top_10_auto_show_settings.rank_by` 会读回 -1。

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
sport_field.top_10_auto_show(True, False, 3, -1)
pivot_table.calculate_data()
workbook.save("output-top10-by-field-itself.xlsx")
```

## **读取当前选项（top_10_auto_show_settings）**
`PivotField.top_10_auto_show_settings` 属性返回一个 `PivotFieldTop10AutoShowSettings` 对象，该对象提供对字段中当前存储的自动显示选项的访问。可使用它检查现有工作簿或刚配置的数据透视表在显示项目时将采用的设置，包括检查从文件加载的工作簿。

```python
import aspose.cells as ac
workbook = ac.Workbook("output-top10-by-value-field.xlsx")
pivot_table = workbook.worksheets[0].pivot_tables[0]
sport_field = pivot_table.row_fields[0]
settings = sport_field.top_10_auto_show_settings
print("AutoShow enabled: " + str(settings.is_auto_show))
print("Direction: " + ("Top" if settings.is_top else "Bottom"))
print("Item count: " + str(settings.auto_show_count))
print("Ranking data field index: " + str(settings.rank_by))
```

这四个属性与写入数据透视表 XML 的经典自动显示属性（`autoShow`、`topAutoShow`、`itemPageCount`、`rankBy`）一一对应，因此读回的值就是所有 Excel 版本都会采用的值。

## **注意**

{{% alert color="primary" %}}
- `PivotField` 的直接属性 `is_auto_show`、`is_ascend_show`、`auto_show_count` 和 `auto_show_field` 已标记为过时。请改用 `top_10_auto_show_settings` 对象：`is_auto_show` 对应 `top_10_auto_show_settings.is_auto_show`，`is_ascend_show` 对应 `top_10_auto_show_settings.is_top`，`auto_show_count` 对应 `top_10_auto_show_settings.auto_show_count`，`auto_show_field` 对应 `top_10_auto_show_settings.rank_by`。若要修改这些设置，请调用受支持的 `top_10_auto_show()` 方法。
- `top_10_auto_show` 适用于行字段和列字段。仅位于页（筛选）区域中的字段不能通过这种方式排名，因为其项目不会布置在数据透视表主体中。
{{% /alert %}}

## **Excel 2007-365：前 10 项筛选（filter_top10）**
现代 Excel 版本会在字段菜单中提供“值筛选”下的“前 10...”值筛选。Aspose.Cells 使用 `PivotField.filter_top10(int value_field_index, PivotFilterType type, bool is_top, int item_count)` 方法表示此筛选，该方法返回所创建的 `PivotFilter`：
- `value_field_index` — 数据字段的从 0 开始的索引，其汇总值用于对项目进行排名。
- `type` — `item_count` 的含义。`PivotFilterType.COUNT` 保留固定数量的项目（对应对话框中的“项目”选项）。`PivotFilterType.PERCENT` 保留指定百分比的项，因此 `item_count` 本身就是百分比值——30 表示保留前 30%。`PivotFilterType.SUM` 按累计值覆盖范围进行排名。
- `is_top` — `True` 表示前 N 项，`False` 表示后 N 项。
- `item_count` — 前 N 项中的 N，其单位取决于 `type`。

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotFilterType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
# 前 10 项筛选——按“Sales 总计”（数据字段索引 0）保留前 2 个项
filter = sport_field.filter_top10(0, PivotFilterType.COUNT, True, 2)
# 如果改用基于百分比的筛选，则保留前 30% 的项：
# sport_field.filter_top10(0, PivotFilterType.PERCENT, True, 30)
pivot_table.pivot_cache.refresh()
pivot_table.calculate_data()
workbook.save("output-top10-filter.xlsx")
```

{{% alert color="primary" %}}
`top_10_auto_show` 和 `filter_top10` 是两个彼此独立的功能。自动显示会在数据透视字段上写入经典 `autoShow` 属性，并且从 Excel 97 开始的所有 Excel 版本都支持该设置。`filter_top10` 会写入现代 `PivotFilter` 条目，该功能需要 Excel 2007 或更高版本。在较旧的 Excel 版本中打开工作簿时，使用现代筛选的数据透视表将改为显示所有项目。对于必须使用旧版工具进行往返转换的文档，应优先使用 `top_10_auto_show`；对于现代工作簿，应优先使用 `filter_top10`，因为它可与其他值筛选功能组合使用。
{{% /alert %}}

## **相关文章**
- [按标签或值筛选数据透视表](/cells/zh/python-net/filter-by-label-or-value-of-pivot-table/)
- [添加数据透视表行字段和列字段](/cells/zh/python-net/pivot-table-add-row-and-column-fields/)
- [对数据透视表中的数据透视字段进行分组](/cells/zh/python-net/group-pivot-fields-in-the-pivot-table/)
- [刷新数据透视表](/cells/zh/python-net/refresh-pivot-table/)
- [在数据透视表中添加页字段](/cells/zh/python-net/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python-net" >}}