---
title: 在数据透视表中显示或筛选前 10 项
linktitle: 在数据透视表中显示或筛选前 10 项
description: 了解如何使用 Aspose.Cells for Java 仅显示数据透视字段中排名最高或最低的项目。本文介绍 Excel 97-2003 Top10AutoShow 方法、如何通过 Top10AutoShowSettings 读取选项，以及如何通过 FilterTop10 实现 Excel 2007-365 前 10 项筛选。
keywords: Aspose.Cells, Java, 数据透视表, 前 10 项, 自动显示, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField
type: docs
weight: 20
url: /zh/java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
如果行字段包含数十个项目，列出所有项目的数据透视表可能难以阅读。前 10 项报表仅保留排名最高或最低的项目，恰好满足排名报表的需要，例如“按收入统计的前 5 个产品”或“按销售数量统计的后 3 个地区”。Aspose.Cells 支持两种机制，分别对应 Microsoft Excel 的两个版本系列。
- **Excel 97-2003 自动显示** — `PivotField.top10AutoShow()` 方法。这是经典的“显示前/后 N 项”设置，直接存储在数据透视字段上。由于它是初始数据透视表格式的一部分，因此适用于所有新旧 Excel 版本。
- **Excel 2007-365 前 10 项筛选** — `PivotField.filterTop10()` 方法。这是位于字段菜单“值筛选”下的现代“前 10 项”值筛选。它以附加到字段的 `PivotFilter` 对象存储，并支持按项目数或百分比进行排名。

## **Excel 97-2003 中的前 10 项显示（top10AutoShow）**
经典自动显示功能只需调用一次 `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)` 即可配置：
- `isAutoShow` — 启用或禁用字段上的自动显示设置。
- `isTop` — `true` 保留排名最高的项目（前），`false` 保留排名最低的项目（后）。
- `count` — 保留的项目数量，例如经典前 10 项报表中为 10。
- `rankBy` — 值字段的索引（从 0 开始），该字段的值用于对项目进行排名。传入 -1 后可按字段自身对项目进行排名。
排名依据可以是值字段，也可以是字段本身。下面介绍两种常用方式。

### **按值字段排名**
按普通值字段（例如 Sales 的总和）对行字段中的项目进行排名。以下示例构建一个包含一个行字段 (`Sport`) 和一个值字段 (`Sales`) 的数据透视表，然后显示销售额排名前 2 的运动项目。由于“Sales 的总和”是索引 0 处的值字段，因此 `rankBy` 为 0。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// 按“Sales 之和”排名显示前 2 个项目（数据字段索引为 0）
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");
```

### **按字段自身排名**
字段也可以按自身进行排名——将 -1 作为 `rankBy` 传入。此变体无需额外的值字段；只需将该字段放在行（或列）区域。以下示例显示按字段自身排名的后 3 个运动项目。保存此设置时，数据透视表 XML 中会省略 `rankBy` 属性，因为 -1 是该格式的默认值，而 `Top10AutoShowSettings.getRankBy()` 的读取结果为 -1。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// 显示按字段本身排名的底部 3 个项目（rankBy = -1）
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");
```

## **读取当前选项（Top10AutoShowSettings）**
`PivotField.getTop10AutoShowSettings()` 方法返回一个 `PivotFieldTop10AutoShowSettings` 对象，可用于获取字段中当前存储的自动显示选项。您可以使用它检查现有工作簿或刚配置的数据透视表将显示哪些项目，也适用于从文件加载的工作簿。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("output-top10-by-value-field.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
PivotField sportField = pivotTable.getRowFields().get(0);
PivotFieldTop10AutoShowSettings settings = sportField.getTop10AutoShowSettings();
System.out.println("AutoShow enabled: " + settings.isAutoShow());
System.out.println("Direction: " + (settings.isTop() ? "Top" : "Bottom"));
System.out.println("Item count: " + settings.getAutoShowCount());
System.out.println("Ranking data field index: " + settings.getRankBy());
```

这四个属性对应于写入数据透视表 XML 的经典自动显示属性（`autoShow`、`topAutoShow`、`itemPageCount`、`rankBy`），因此读回的值就是所有 Excel 版本都会采用的值。

## **注意**

{{% alert color="primary" %}}
- `PivotField` 中直接通过 `isAutoShow()`、`isAscendShow()`、`getAutoShowCount()` 和 `getAutoShowField()` 公开的属性均已标记为过时。请改用 `Top10AutoShowSettings` 对象：`Top10AutoShowSettings.isAutoShow()` 取代 `PivotField.isAutoShow()`，`Top10AutoShowSettings.isTop()` 取代 `PivotField.isAscendShow()`，`Top10AutoShowSettings.getAutoShowCount()` 取代 `PivotField.getAutoShowCount()`，`Top10AutoShowSettings.getRankBy()` 取代 `PivotField.getAutoShowField()`。修改这些设置时，应使用受支持的 `PivotField.top10AutoShow()` 方法。
- `top10AutoShow` 适用于行字段和列字段。仅位于页（筛选）区域的字段无法通过这种方式进行排名，因为其中的项目不会排列在数据透视表主体中。
{{% /alert %}}

## **Excel 2007-365：前 10 项筛选（filterTop10）**
现代 Excel 版本会在字段菜单的“值筛选”下提供“前 10 项...”值筛选。Aspose.Cells 使用 `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)` 方法实现此筛选，该方法返回已创建的 `PivotFilter`：
- `valueFieldIndex` — 值字段的索引（从 0 开始），该字段的汇总值用于对项目进行排名。
- `type` — 指定 `itemCount` 的含义。`PivotFilterType.COUNT` 保留固定数量的项目（对话框中的“项目数”选项）。`PivotFilterType.PERCENT` 保留项目总数的一定百分比，因此 `itemCount` 即百分比值；例如，30 表示保留排名前 30% 的项目。`PivotFilterType.SUM` 按累计值覆盖率进行排名。
- `isTop` — `true` 表示前，`false` 表示后。
- `itemCount` — “前 N 项”中的 N，其单位取决于 `type`。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// 前 10 项筛选——按“Sales 汇总”保留前 2 个项目（数据字段索引 0）
sportField.filterTop10(0, PivotFilterType.COUNT, true, 2);
// 若改用基于百分比的筛选，则保留前 30% 的项目：
// sportField.filterTop10(0, PivotFilterType.PERCENT, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");
```

{{% alert color="primary" %}}
`top10AutoShow` 和 `filterTop10` 是两个独立的功能。自动显示会将经典 `autoShow` 属性写入数据透视字段的设置中，从 Excel 97 开始的所有 Excel 版本都会采用该设置。`filterTop10` 会写入现代 `PivotFilter` 条目，该条目需要 Excel 2007 或更高版本。使用现代筛选器的数据透视表在较旧 Excel 版本中打开时，会退化为显示所有项目。对于必须通过旧版工具链进行往返处理的工作簿，应优先使用 `top10AutoShow`；对于现代工作簿，应优先使用 `filterTop10`，因为它可以与其他值筛选结合使用。
{{% /alert %}}

## **相关文章**
- [按标签或值筛选数据透视表](/cells/zh/java/filter-by-label-or-value-of-pivot-table/)
- [添加数据透视表行字段和列字段](/cells/zh/java/pivot-table-add-row-and-column-fields/)
- [对数据透视表中的数据透视字段进行分组](/cells/zh/java/group-pivot-fields-in-the-pivot-table/)
- [刷新数据透视表](/cells/zh/java/refresh-pivot-table/)
- [在数据透视表中添加页字段](/cells/zh/java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="java" >}}