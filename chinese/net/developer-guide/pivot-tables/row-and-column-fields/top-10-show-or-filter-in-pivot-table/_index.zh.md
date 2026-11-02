---
title: 在数据透视表中显示或筛选前 10 项
linktitle: 在数据透视表中显示或筛选前 10 项
description: 了解如何在 Aspose.Cells for .NET 中仅显示数据透视字段中排名最高或最低的项目。本文介绍 Excel 97-2003 的 Top10AutoShow 方法、使用 Top10AutoShowSettings 读取选项，以及通过 FilterTop10 实现 Excel 2007-365 的前 10 项筛选。
keywords: Aspose.Cells, .NET, 数据透视表, 前 10 项, 自动显示, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, C#
type: docs
weight: 20
url: /zh/net/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的适用场景**
如果行字段包含数十个成员，列出该字段中所有项目的数据透视表可能难以阅读。前 10 项报表仅保留排名最高或最低的项目，正好满足排名报表的需要，例如“按收入排名前 5 的产品”或“按销售数量排名后 3 的区域”。Aspose.Cells 支持两种机制，分别对应两代 Microsoft Excel。
- **Excel 97-2003 自动显示** — `PivotField.Top10AutoShow()` 方法。这是经典的“显示前/后 N 项”设置，直接存储在数据透视字段上。由于它是最初的数据透视表格式的一部分，因此适用于所有 Excel 版本，无论新旧。
- **Excel 2007-365 前 10 项筛选** — `PivotField.FilterTop10()` 方法。这是位于字段菜单“值筛选”下的现代“前 10 项”值筛选。它以附加到字段的 `PivotFilter` 对象存储，并支持基于项目数或百分比的排名筛选。

## **Excel 97-2003 中的前 10 项显示（Top10AutoShow）**
经典自动显示功能只需调用一次 `PivotField.Top10AutoShow(bool isAutoShow, bool isTop, int count, int rankBy)` 即可配置：
- `isAutoShow` — 启用或禁用字段上的自动显示设置。
- `isTop` — `true` 保留排名最高的项目，`false` 保留排名最低的项目。
- `count` — 要保留的项目数量，例如在经典前 10 项报表中为 10。
- `rankBy` — **数据字段**的从零开始索引，该字段的值用于对项目进行排名。传入 -1 可按字段自身对项目进行排名。
排名可以依据值字段，也可以依据字段自身。下面介绍两种常见用法。

### **按值字段排名**
使用普通值字段（例如“Sales 总计”）对行字段的项目进行排名。以下示例构建一个数据透视表，其中包含一个行字段 (`Sport`) 和一个数据字段 (`Sales`)，然后按销售额显示排名前 2 的运动项目。由于“Sales 总计”是索引为 0 的数据字段，因此 `rankBy` 为 0。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// 显示按“Sales 总计”排名的前 2 个项目（数据字段索引 0）
sportField.Top10AutoShow(true, true, 2, 0);
pivotTable.CalculateData();
workbook.Save("output-top10-by-value-field.xlsx");
```

### **按字段自身排名**
字段也可以按自身进行排名——将 -1 作为 `rankBy` 传入。此变体无需额外的数据字段；该字段只需位于行（或列）区域。以下示例显示按字段自身排名后 3 的运动项目。保存此设置时，数据透视表 XML 中会省略 `rankBy` 属性，因为 -1 是该格式的默认值，而 `Top10AutoShowSettings.RankBy` 读取时会返回 -1。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// 显示按字段本身排名的最低 3 个项目（rankBy = -1）
sportField.Top10AutoShow(true, false, 3, -1);
pivotTable.CalculateData();
workbook.Save("output-top10-by-field-itself.xlsx");
```

## **读取当前选项（Top10AutoShowSettings）**
`PivotField.Top10AutoShowSettings` 属性返回一个 `PivotFieldTop10AutoShowSettings` 对象，该对象提供对当前存储在字段上的自动显示选项的访问。可使用它检查现有工作簿或刚完成配置的数据透视表将如何呈现其中的项目，包括从文件加载的工作簿。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("output-top10-by-value-field.xlsx");
PivotTable pivotTable = workbook.Worksheets[0].PivotTables[0];
PivotField sportField = pivotTable.RowFields[0];
PivotFieldTop10AutoShowSettings settings = sportField.Top10AutoShowSettings;
Console.WriteLine("AutoShow enabled: " + settings.IsAutoShow);
Console.WriteLine("Direction: " + (settings.IsTop ? "Top" : "Bottom"));
Console.WriteLine("Item count: " + settings.AutoShowCount);
Console.WriteLine("Ranking data field index: " + settings.RankBy);
```

这四个属性与写入数据透视表 XML 的经典自动显示属性（`autoShow`、`topAutoShow`、`itemPageCount`、`rankBy`）一一对应，因此读回的值就是所有 Excel 版本都会采用的值。

## **注意**

{{% alert color="primary" %}}
- `PivotField` 的直接属性 `IsAutoShow`、`IsAscendShow`、`AutoShowCount` 和 `AutoShowField` 已标记为过时。请改用 `Top10AutoShowSettings` 对象：`IsAutoShow` 对应 `Top10AutoShowSettings.IsAutoShow`，`IsAscendShow` 对应 `Top10AutoShowSettings.IsTop`，`AutoShowCount` 对应 `Top10AutoShowSettings.AutoShowCount`，`AutoShowField` 对应 `Top10AutoShowSettings.RankBy`。修改这些设置时，请使用 `Top10AutoShow()` 方法。
- `Top10AutoShow` 适用于行字段和列字段。仅位于报表筛选（页面）区域中的字段无法通过这种方式进行排名，因为其项目未排列在数据透视表主体中。
{{% /alert %}}

## **Excel 2007-365：前 10 项筛选（FilterTop10）**
现代 Excel 版本在字段菜单中提供“前 10 项”值筛选（“值筛选”、“前 10 项...”）。Aspose.Cells 使用 `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)` 方法实现此功能，该方法返回创建的 `PivotFilter`：
- `valueFieldIndex` — 数据字段的从零开始索引，该字段的汇总值用于对项目进行排名。
- `type` — `itemCount` 的含义。`PivotFilterType.Count` 保留固定数量的项目（对应对话框中的“项目”选项）。`PivotFilterType.Percent` 保留一定百分比的项，因此 `itemCount` 本身就是百分比，例如 30 表示保留前 30%。`PivotFilterType.Sum` 按累计值覆盖比例进行排名。
- `isTop` — `true` 表示排名前 N 项，`false` 表示排名后 N 项。
- `itemCount` — “前 N 项”中的 N；其单位取决于 `type`。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// 前 10 项筛选——按“Sales 总计”保留前 2 个项目（数据字段索引 0）
PivotFilter filter = sportField.FilterTop10(0, PivotFilterType.Count, true, 2);
// 如果改用基于百分比的筛选，则保留前 30% 的项目：
// sportField.FilterTop10(0, PivotFilterType.Percent, true, 30);
pivotTable.PivotCache.Refresh();
pivotTable.CalculateData();
workbook.Save("output-top10-filter.xlsx");
```

{{% alert color="primary" %}}
`Top10AutoShow` 和 `FilterTop10` 是两个彼此独立的功能。自动显示功能会写入设置在数据透视字段上的经典 `autoShow` 属性，所有从 Excel 97 开始的 Excel 版本都会采用该设置。`FilterTop10` 会写入现代 `PivotFilter` 条目，该条目要求使用 Excel 2007 或更高版本。使用旧版 Excel 打开工作簿时，使用现代筛选器的数据透视表会回退为显示所有项目。对于必须通过旧版工具进行往返处理的文档，请优先使用 `Top10AutoShow`；对于现代工作簿，请优先使用 `FilterTop10`，因为它可以与其他值筛选结合使用。
{{% /alert %}}

## **相关文章**
- [按标签或值筛选数据透视表](/cells/zh/net/filter-by-label-or-value-of-pivot-table/)
- [添加数据透视表行字段和列字段](/cells/zh/net/pivot-table-add-row-and-column-fields/)
- [对数据透视表中的数据透视字段进行分组](/cells/zh/net/group-pivot-fields-in-the-pivot-table/)
- [刷新数据透视表](/cells/zh/net/refresh-pivot-table/)
- [在数据透视表中添加页字段](/cells/zh/net/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="csharp" >}}