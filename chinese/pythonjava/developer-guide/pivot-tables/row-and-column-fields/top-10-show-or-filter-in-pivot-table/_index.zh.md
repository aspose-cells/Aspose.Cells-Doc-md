---
title: 数据透视表中的前10显示或过滤
linktitle: 数据透视表中的前10显示或过滤
description: 了解如何在 Aspose.Cells for Python via Java 中仅显示数据透视表字段的最高或最低排名项，本文介绍了 Excel 97-2003 的 top10AutoShow 方法、使用 Top10AutoShowSettings 读取选项，以及 Excel 2007-365 通过 filterTop10 实现的前10过滤
keywords: Aspose.Cells for Python via Java, 数据透视表, 前10, 自动显示, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /zh/python-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
当行字段拥有数十个成员时，列出该字段每个项目的数据透视表可能难以阅读。前10报告仅保留最高或最低排名的项目，这正是排名报告所需的——例如“按收入排名前5的产品”或“按销售计数排名底部3的地区”。Aspose.Cells 支持两种实现方式，它们对应 Microsoft Excel 的两个版本。
- **Excel 97-2003 AutoShow** — `PivotField.top10AutoShow()` 方法。这是经典的“显示前/后 N 项”设置，直接存储在数据透视表字段上。由于它是原始数据透视表格式的一部分，在所有 Excel 版本（包括旧版和新版）均可工作。
- **Excel 2007-365 Top 10 Filter** — `PivotField.filterTop10()` 方法。这是位于字段菜单“值筛选”下的现代前10值筛选。它以附加到字段的 `PivotFilter` 对象存储，并提供基于项目计数或百分比的排名方式。

## **Excel 97-2003 中的前10显示（top10AutoShow）**
经典的 AutoShow 通过一次调用 `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)` 来配置：
- `isAutoShow` — 启用或禁用该字段的 AutoShow 设置。
- `isTop` — `True` 保留最高排名的项目（前），`False` 保留最低排名的项目（后）。
- `count` — 要保留的项目数量，例如经典的前10报告即为 10 项。
- `rankBy` — 用于对项目进行排名的 **数据字段** 的零基索引。传入 -1 表示按字段本身进行排名。

排名可以由数值字段驱动，也可以由字段本身驱动。下面展示两种常见变体。

### **按数值字段排名**
按普通数值字段（例如“销售额求和”）对行字段的项目进行排名。以下示例构建了一个包含行字段 (`Sport`) 和数据字段 (`Sales`) 的数据透视表，然后显示按销售额排名前 2 项的运动项目。`rankBy` 为 0，因为 “Sales” 是索引为 0 的数据字段。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sport")
worksheet.getCells().get("B1").putValue("Quarter")
worksheet.getCells().get("C1").putValue("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.getCells().get(row, 0).putValue(sport)
        worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
        row += 1
pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
pivot_table.calculateData()
sport_field = pivot_table.getRowFields().get(0)
sport_field.top10AutoShow(True, True, 2, 0)
pivot_table.calculateData()
workbook.save("output-top10-by-value-field.xlsx")
jpype.shutdownJVM()
```

### **按字段本身排名**
字段也可以按自身排名——将 `rankBy` 设为 -1。此变体不需要额外的数据字段；字段只需位于行（或列）区域。以下示例显示按字段本身排名的底部 3 项运动。当此设置保存时，`rankBy` 属性会从数据透视表 XML 中省略，因为 -1 是格式的默认值，`Top10AutoShowSettings.getRankBy()` 会读取回 -1。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sport")
worksheet.getCells().get("B1").putValue("Quarter")
worksheet.getCells().get("C1").putValue("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.getCells().get(row, 0).putValue(sport)
        worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
        row += 1
pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
pivot_table.calculateData()
sport_field = pivot_table.getRowFields().get(0)
# Show the bottom 3 items ranked by the field itself (rankBy = -1)
sport_field.top10AutoShow(True, False, 3, -1)
pivot_table.calculateData()
workbook.save("output-top10-by-field-itself.xlsx")
jpype.shutdownJVM()
```

## **读取当前选项（Top10AutoShowSettings）**
`PivotField.getTop10AutoShowSettings()` 方法返回一个 `PivotFieldTop10AutoShowSettings` 对象，公开当前存储在字段上的 AutoShow 选项。可使用它检查现有工作簿或刚配置的数据透视表将如何呈现其项目——包括从文件加载的工作簿。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
workbook = Workbook("output-top10-by-value-field.xlsx")
pivot_table = workbook.getWorksheets().get(0).getPivotTables().get(0)
sport_field = pivot_table.getRowFields()[0]
settings = sport_field.getTop10AutoShowSettings()
print("AutoShow enabled: " + str(settings.isAutoShow()))
print("Direction: " + ("Top" if settings.isTop() else "Bottom"))
print("Item count: " + str(settings.getAutoShowCount()))
print("Ranking data field index: " + str(settings.getRankBy()))
jpype.shutdownJVM()
```

这四个属性映射到写入数据透视表 XML 的经典 AutoShow 属性（`autoShow`、`topAutoShow`、`itemPageCount`、`rankBy`），因此读取回的值是所有 Excel 版本都会遵守的值。

## **注意**

{{% alert color="primary" %}}
- 直接的 `PivotField` 访问器 `isAutoShow()`、`isAscendShow()`、`getAutoShowCount()` 和 `getAutoShowField()` 已标记为过时。请改用 `Top10AutoShowSettings` 对象：`PivotField.isAutoShow()` 对应 `Top10AutoShowSettings.isAutoShow()`，`PivotField.isAscendShow()` 对应 `Top10AutoShowSettings.isTop()`，`PivotField.getAutoShowCount()` 对应 `Top10AutoShowSettings.getAutoShowCount()`，`PivotField.getAutoShowField()` 对应 `Top10AutoShowSettings.getRankBy()`。`top10AutoShow()` 方法本身仍是修改设置的受支持方式。
- `top10AutoShow` 可用于行字段和列字段。仅位于页面（筛选）区域的字段无法通过此方式进行排名，因为其项目未在数据透视表主体中布局。
{{% /alert %}}

## **Excel 2007-365：前10过滤（filterTop10）**
现代 Excel 版本在字段菜单的值筛选中提供前10过滤（Value Filters → Top 10…）。Aspose.Cells 使用 `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)` 方法建模，并返回创建的 `PivotFilter`：
- `valueFieldIndex` — 用于对项目进行排名的聚合值所在数据字段的零基索引。
- `type` — `itemCount` 的含义。`PivotFilterType.COUNT` 保留固定数量的项目（对话框的 Items 选项）。`PivotFilterType.PERCENT` 保留一定比例的项目，`itemCount` 即该比例，如 30 代表保留前 30%。`PivotFilterType.SUM` 按累计值覆盖率进行排名。
- `isTop` — `True` 表示前（Top），`False` 表示后（Bottom）。
- `itemCount` — 前 N 项中的 N；其单位取决于 `type`。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PivotFilterType
try:
    workbook = Workbook()
    worksheet = workbook.getWorksheets().get(0)
    worksheet.getCells().get("A1").putValue("Sport")
    worksheet.getCells().get("B1").putValue("Quarter")
    worksheet.getCells().get("C1").putValue("Sales")
    sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
    row = 2
    for sport in sports:
        for quarter in range(1, 4):
            worksheet.getCells().get(row, 0).putValue(sport)
            worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
            worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
            row += 1
    pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
    pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
    pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
    pivot_table.calculateData()
    sport_field = pivot_table.getRowFields().get(0)
    # Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
    filter = sport_field.filterTop10(0, PivotFilterType.COUNT, True, 2)
    # For a percentage-based filter instead, keep the top 30 percent of the items:
    # sport_field.filterTop10(0, PivotFilterType.PERCENT, True, 30)
    pivot_table.getPivotCache().refresh()
    pivot_table.calculateData()
    workbook.save("output-top10-filter.xlsx")
finally:
    jpype.shutdownJVM()
```

{{% alert color="primary" %}}
`top10AutoShow` 与 `filterTop10` 是两个独立的功能。AutoShow 将经典的 `autoShow` 属性写入数据透视表字段，所有从 Excel 97 起的 Excel 版本均支持。`filterTop10` 写入现代的 `PivotFilter` 条目，需 Excel 2007 及以上版本。当工作簿在较旧的 Excel 版本中打开时，使用现代过滤器的数据透视表会回退为显示所有项目。对于必须在旧工具间往返的文档，建议使用 `top10AutoShow`；对于现代工作簿，建议使用 `filterTop10`，因为它可与其他值筛选共同使用。
{{% /alert %}}

## **相关文档**
- [通过标签或数值过滤数据透视表](/cells/zh/python-java/filter-by-label-or-value-of-pivot-table/)
- [添加数据透视表的行和列字段](/cells/zh/python-java/pivot-table-add-row-and-column-fields/)
- [在数据透视表中对数据透视字段进行分组](/cells/zh/python-java/group-pivot-fields-in-the-pivot-table/)
- [刷新数据透视表](/cells/zh/python-java/refresh-pivot-table/)
- [在数据透视表中添加页面字段](/cells/zh/python-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python" >}}