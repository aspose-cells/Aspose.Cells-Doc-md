---
title: 数据透视表中的前 10 项显示或筛选
linktitle: 数据透视表中的前 10 项显示或筛选
description: 了解如何使用 Aspose.Cells for Python via Java 仅显示数据透视表字段中排名最高或最低的项目。本文介绍 Excel 97-2003 的 top10AutoShow 方法、使用 Top10AutoShowSettings 读取选项，以及通过 filterTop10 实现 Excel 2007-365 前 10 项筛选。
keywords: Aspose.Cells for Python via Java, 数据透视表, 前 10 项, 自动显示, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /zh/python-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
当行字段包含数十个成员时，列出所有成员的数据透视表可能难以阅读。前 10 项报表仅保留排名最高或最低的项目，这正是排名报表所需的功能，例如“收入排名前 5 的产品”或“销售数量排名最低的 3 个地区”。Aspose.Cells 为此支持两种机制，分别对应 Microsoft Excel 的两个版本代次。
- **Excel 97-2003 自动显示** — `PivotField.top10AutoShow()` 方法。这是直接存储在数据透视表字段上的经典“显示前/后 N 个项目”设置。由于该设置属于原始数据透视表格式的一部分，因此适用于所有新旧 Excel 版本。
- **Excel 2007-365 前 10 项筛选** — `PivotField.filterTop10()` 方法。这是位于字段菜单“值筛选”下的现代“前 10 项”值筛选。它以 `PivotFilter` 对象的形式附加到字段上并存储，支持按项目数量或百分比进行排名。

## **Excel 97-2003 中的前 10 项显示（top10AutoShow）**
只需调用一次 `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)` 即可配置经典自动显示功能：
- `isAutoShow` — 在字段上启用或禁用自动显示设置。
- `isTop` — `True` 保留排名最高的项目（前 N 项），`False` 保留排名最低的项目（后 N 项）。
- `count` — 要保留的项目数量，例如经典前 10 项报表中可设为 10。
- `rankBy` — 根据数据字段的值对项目进行排名时，该数据字段的索引（从 0 开始）。传入 -1 表示按字段自身对项目进行排名。
排名既可以依据值字段，也可以依据字段自身。下面介绍两种常用方式。

### **按值字段排名**
使用“销售量之和”等普通值字段对行字段中的项目进行排名。以下示例构建了一个包含一个行字段（`Sport`）和一个数据字段（`Sales`）的数据透视表，然后显示按销售量排名前 2 的运动项目。由于“销售量之和”是索引为 0 的数据字段，因此 `rankBy` 为 0。

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
sport_field.setAutoShow(True)
sport_field.setAutoShowCount(2)
sport_field.setAutoShowField(2)
pivot_table.calculateData()
workbook.save("output-top10-by-value-field.xlsx")
jpype.shutdownJVM()
```

### **按字段自身排名**
数据透视表字段也可以按自身进行排名——将 `rankBy` 设为 -1。此变体无需额外的数据字段；只需将该字段放在行（或列）区域中。以下示例显示按字段自身排在后 3 位的运动项目。保存此设置时，由于 -1 是该格式的默认值，数据透视表 XML 中将省略 `rankBy` 属性，而 `Top10AutoShowSettings.getRankBy()` 将返回 -1。

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
# 显示按字段自身排名的前 3 个项目（rankBy = -1）
sport_field.top10AutoShow(True, False, 3, -1)
pivot_table.calculateData()
workbook.save("output-top10-by-field-itself.xlsx")
jpype.shutdownJVM()
```

## **读取当前选项（Top10AutoShowSettings）**
`PivotField.getTop10AutoShowSettings()` 方法返回一个 `PivotFieldTop10AutoShowSettings` 对象，该对象提供当前存储在字段上的自动显示选项。使用该对象可检查现有工作簿或刚配置的数据透视表将如何呈现其中的项目，包括从文件加载的工作簿。

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

这四个属性分别对应写入数据透视表 XML 的经典自动显示属性（`autoShow`、`topAutoShow`、`itemPageCount`、`rankBy`），因此读回的数值就是所有 Excel 版本都会遵循的值。

## **注意**

{{% alert color="primary" %}}
- `PivotField` 上的直接访问器 `isAutoShow()`、`isAscendShow()`、`getAutoShowCount()` 和 `getAutoShowField()` 已标记为过时。请改用 `Top10AutoShowSettings` 对象：`PivotField.isAutoShow()` 映射为 `Top10AutoShowSettings.isAutoShow()`，`PivotField.isAscendShow()` 映射为 `Top10AutoShowSettings.isTop()`，`PivotField.getAutoShowCount()` 映射为 `Top10AutoShowSettings.getAutoShowCount()`，`PivotField.getAutoShowField()` 映射为 `Top10AutoShowSettings.getRankBy()`。如需更改这些设置，请使用受支持的 `top10AutoShow()` 方法。
- `top10AutoShow` 适用于行字段和列字段。仅位于页面（筛选）区域中的字段无法通过这种方式排名，因为其项目不会显示在数据透视表主体区域中。
{{% /alert %}}

## **Excel 2007-365：前 10 项筛选（filterTop10）**
现代 Excel 版本在字段菜单中提供“前 10 项”值筛选（值筛选、前 10 项...）。Aspose.Cells 通过 `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)` 方法实现此筛选，该方法返回已创建的 `PivotFilter`：
- `valueFieldIndex` — 根据聚合值对项目进行排名的数据字段的索引（从 0 开始）。
- `type` — 指定 `itemCount` 的含义。`PivotFilterType.COUNT` 保留固定数量的项目（对应对话框中的“项目”选项）。`PivotFilterType.PERCENT` 保留指定百分比的项目，因此 `itemCount` 本身即为百分比值——30 表示保留前 30% 的项目。`PivotFilterType.SUM` 按累计值覆盖度进行排名。
- `isTop` — `True` 表示前 N 项，`False` 表示后 N 项。
- `itemCount` — 前 N 项中的 N，其单位取决于 `type`。

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
    # 前 10 项筛选——按“Sales 总和”保留前 2 个项目（数据字段索引为 0）
    filter = sport_field.filterTop10(0, PivotFilterType.COUNT, True, 2)
    # 如果改用基于百分比的筛选，则保留前 30% 的项目：
    # sport_field.filterTop10(0, PivotFilterType.PERCENT, True, 30)
    pivot_table.getPivotCache().refresh()
    pivot_table.calculateData()
    workbook.save("output-top10-filter.xlsx")
finally:
    jpype.shutdownJVM()
```

{{% alert color="primary" %}}
`top10AutoShow` 和 `filterTop10` 是两个彼此独立的功能。自动显示会写入数据透视表字段上的经典 `autoShow` 属性设置，并且从 Excel 97 开始的所有 Excel 版本都支持该设置。`filterTop10` 会写入现代 `PivotFilter` 条目，该条目需要 Excel 2007 或更高版本。如果在较旧的 Excel 版本中打开工作簿，使用现代筛选的数据透视表将回退为显示所有项目。对于需要在旧版工具中往返读写的文档，应优先使用 `top10AutoShow`；对于现代工作簿，应优先使用 `filterTop10`，因为它可与其他值筛选功能组合使用。
{{% /alert %}}

## **相关文章**
- [按标签或值筛选数据透视表](/cells/zh/python-java/filter-by-label-or-value-of-pivot-table/)
- [添加数据透视表行字段和列字段](/cells/zh/python-java/pivot-table-add-row-and-column-fields/)
- [对数据透视表中的透视字段进行分组](/cells/zh/python-java/group-pivot-fields-in-the-pivot-table/)
- [刷新数据透视表](/cells/zh/python-java/refresh-pivot-table/)
- [在数据透视表中添加页面字段](/cells/zh/python-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python" >}}