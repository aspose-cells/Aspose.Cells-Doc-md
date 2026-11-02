---
title: 在数据透视表中显示或筛选前 10 名
linktitle: 在数据透视表中显示或筛选前 10 名
description: 了解如何使用 Aspose.Cells for Node.js via C++，在数据透视字段中仅显示排名最高或最低的项目。本文介绍 Excel 97-2003 的 Top10AutoShow 方法、如何通过 Top10AutoShowSettings 读取选项，以及如何使用 FilterTop10 实现 Excel 2007-365 的前 10 名筛选。
keywords: Aspose.Cells, Node.js via C++, 数据透视表, 前 10 名, 自动显示, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, Node.js
type: docs
weight: 20
url: /zh/nodejs-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的适用场景**
当行字段包含数十个项目时，列出所有项目的数据透视表可能难以阅读。前 10 名报表仅保留排名最高或最低的项目，正好满足排名报表的需求，例如“按收入排名前 5 的产品”或“按销售数量排名后 3 的地区”。Aspose.Cells 支持两种机制，分别对应 Microsoft Excel 的两个版本阶段。
- **Excel 97-2003 AutoShow** — `pivotField.top10AutoShow()` 方法。这是经典的“显示前/后 N 个项目”设置，直接存储在数据透视字段上。由于它是原始数据透视表格式的一部分，因此适用于所有新旧 Excel 版本。
- **Excel 2007-365 前 10 名筛选** — `pivotField.filterTop10()` 方法。这是字段菜单“值筛选”下的现代前 10 名值筛选器。它以附加到字段的 `PivotFilter` 对象形式存储，并支持按项目数或百分比进行排名。

## **在 Excel 97-2003 中显示前 10 名（top10AutoShow）**
只需调用一次 `pivotField.top10AutoShow(isAutoShow, isTop, count, rankBy)` 即可配置经典 AutoShow：
- `isAutoShow` — 在字段上启用或禁用 AutoShow 设置。
- `isTop` — `true` 保留排名最高的项目（前 N 项），`false` 保留排名最低的项目（后 N 项）。
- `count` — 要保留的项目数量，例如经典前 10 名报表中设为 10。
- `rankBy` — **数据字段**的零基索引，该字段的值用于对项目进行排名。传入 -1 时，按字段自身对项目进行排名。
排名依据可以是值字段，也可以是字段自身。下面介绍两种常用变体。

### **按值字段排名**
使用普通值字段（例如 Sales 总和）对行字段的项目进行排名。以下示例创建一个包含一个行字段（`Sport`）和一个数据字段（`Sales`）的数据透视表，并显示销售额排名前 2 的运动项目。由于 Sales 总和是索引 0 处的数据字段，因此 `rankBy` 为 0。

```javascript
const AsposeCells = require("aspose.cells.node");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");```

```

### **按字段自身排名**
字段也可以按自身进行排名——将 -1 作为 `rankBy` 传入。此变体无需额外的数据字段；该字段只需位于行（或列）区域。以下示例显示按字段自身排名的后 3 个运动项目。保存此设置时，数据透视表 XML 中会省略 `rankBy` 属性，因为 -1 是该格式的默认值，而 `top10AutoShowSettings.getRankBy()` 读取到的值为 -1。

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the bottom 3 items ranked by the field itself (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");```
```

## **读取当前选项（Top10AutoShowSettings）**
`pivotField.getTop10AutoShowSettings()` getter 返回一个 `PivotFieldTop10AutoShowSettings` 对象，该对象公开字段当前存储的 AutoShow 选项。可使用它检查现有工作簿或刚配置的数据透视表将如何显示其中的项目，包括从文件加载的工作簿。

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("output-top10-by-value-field.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const sportField = pivotTable.getRowFields().get(0);
const settings = sportField.getTop10AutoShowSettings();
console.log("AutoShow enabled: " + settings.isAutoShow);
console.log("Direction: " + (settings.isTop ? "Top" : "Bottom"));
console.log("Item count: " + settings.getAutoShowCount());
console.log("Ranking data field index: " + settings.getRankBy());
```

这四个属性分别对应写入数据透视表 XML 的经典 AutoShow 属性（`autoShow`、`topAutoShow`、`itemPageCount`、`rankBy`），因此读取到的值也是所有 Excel 版本都会采用的值。

## **注意**

{{% alert color="primary" %}}
- `PivotField` 的直接 getter `isAutoShow`、`getIsAscendShow()`、`getAutoShowCount()` 和 `getAutoShowField()` 已标记为过时。请改用 `Top10AutoShowSettings` 对象：`pivotField.isAutoShow` 改为 `top10AutoShowSettings.isAutoShow`，`pivotField.getIsAscendShow()` 改为 `top10AutoShowSettings.isTop`，`pivotField.getAutoShowCount()` 改为 `top10AutoShowSettings.getAutoShowCount()`，`pivotField.getAutoShowField()` 改为 `top10AutoShowSettings.getRankBy()`。`pivotField.top10AutoShow()` 方法本身是受支持的设置修改方式。
- `top10AutoShow()` 可用于行字段和列字段。仅位于页字段（筛选）区域的字段无法以此方式排名，因为其项目不会显示在数据透视表主体中。
{{% /alert %}}

## **Excel 2007-365：前 10 名筛选（filterTop10）**
现代 Excel 版本在字段菜单中提供“前 10 名”值筛选器（“值筛选”、“前 10 名...”）。Aspose.Cells 使用 `pivotField.filterTop10(valueFieldIndex, type, isTop, itemCount)` 方法实现此筛选功能，该方法返回创建的 `PivotFilter`：
- `valueFieldIndex` — 数据字段的零基索引，该字段的汇总值将作为项目排名的依据。
- `type` — `itemCount` 的含义。`PivotFilterType.Count` 保留固定数量的项目（对应对话框中的“项目数”选项）。`PivotFilterType.Percent` 保留项目的一定百分比，因此 `itemCount` 本身即为百分比；例如，30 表示保留前 30%。`PivotFilterType.SUM` 按累计值覆盖率进行排名。
- `isTop` — `true` 表示保留排名最高的项目，`false` 表示保留排名最低的项目。
- `itemCount` — “前 N 名”中的 N；其单位取决于 `type`。

```javascript
const AsposeCells = require("aspose.cells.node");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
const filter = sportField.filterTop10(0, AsposeCells.PivotFilterType.Count, true, 2);
// For a percentage-based filter instead, keep the top 30 percent of the items:
// sportField.filterTop10(0, AsposeCells.PivotFilterType.Percent, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");```

```

{{% alert color="primary" %}}
`top10AutoShow` 和 `filterTop10` 是两个彼此独立的功能。AutoShow 会写入设置在数据透视字段上的经典 `autoShow` 属性组，并受到从 Excel 97 开始的所有 Excel 版本支持。`filterTop10` 会写入现代 `PivotFilter` 条目，该功能需要 Excel 2007 或更高版本。在较旧的 Excel 版本中打开使用现代筛选器的数据透视表时，将回退为显示所有项目。对于需要通过旧版工具打开并重新保存的文档，请优先使用 `top10AutoShow`；对于现代工作簿，请优先使用 `filterTop10`，因为它可以与其他值筛选器组合使用。
{{% /alert %}}

## **相关文章**
- [按标签或值筛选数据透视表](/cells/zh/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [添加数据透视表行字段和列字段](/cells/zh/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [对数据透视表中的数据透视字段进行分组](/cells/zh/nodejs-cpp/group-pivot-fields-in-the-pivot-table/)
- [刷新数据透视表](/cells/zh/nodejs-cpp/refresh-pivot-table/)
- [在数据透视表中添加页字段](/cells/zh/nodejs-cpp/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}