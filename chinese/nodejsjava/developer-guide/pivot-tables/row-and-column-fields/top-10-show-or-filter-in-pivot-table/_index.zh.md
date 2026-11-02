---
title: 在数据透视表中显示或筛选前 10 项
linktitle: 在数据透视表中显示或筛选前 10 项
description: 了解如何使用 Aspose.Cells for Node.js via Java 仅显示数据透视字段中排名最高或最低的项目。本文介绍 Excel 97-2003 的 Top10AutoShow 方法、如何使用 Top10AutoShowSettings 读取选项，以及如何通过 FilterTop10 实现 Excel 2007-365 前 10 项筛选。
keywords: Aspose.Cells, Node.js via Java, 数据透视表, 前 10 项, 自动显示, top10AutoShow, getTop10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, JavaScript
type: docs
weight: 20
url: /zh/nodejs-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的用法场景**
当行字段包含数十个成员时，列出所有项目的数据透视表可能难以阅读。前 10 项报表仅保留排名最高或最低的项目，这正是排名报表所需的功能，例如“按收入排名前 5 的产品”或“按销售数量排名后 3 的地区”。Aspose.Cells 支持两种机制，分别对应 Microsoft Excel 的两代版本。
- **Excel 97-2003 自动显示（AutoShow）** — `PivotField.top10AutoShow()` 方法。这是经典的“显示前/后 N 个项目”设置，直接存储在数据透视字段上。由于它是原始数据透视表格式的一部分，因此适用于包括旧版和新版在内的所有 Excel 版本。
- **Excel 2007-365 前 10 项筛选（Top 10 Filter）** — `PivotField.filterTop10()` 方法。这是位于字段菜单“值筛选”选项下的现代前 10 项值筛选。它以 `PivotFilter` 对象的形式存储并附加到字段，支持按项目数或百分比进行排名。

## **Excel 97-2003 中的前 10 项显示（Top10AutoShow）**
只需调用一次 `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)` 即可配置经典 AutoShow：
- `isAutoShow` — 启用或禁用字段上的 AutoShow 设置。
- `isTop` — `true` 保留排名最高的项目（前 N 项），`false` 保留排名最低的项目（后 N 项）。
- `count` — 要保留的项目数量，例如，设为 10 可用于经典的前 10 项报表。
- `rankBy` — **数据字段**的索引（从 0 开始），该字段的值将用于对项目进行排名。传入 -1 可按字段本身对项目进行排名。
项目的排名既可以依据值字段，也可以依据字段本身。下面介绍两种常见用法。

### **按值字段排名**
可使用普通值字段（例如 `Sales` 之和）对行字段中的项目进行排名。以下示例创建一个包含一个行字段（`Sport`）和一个数据字段（`Sales`）的数据透视表，然后显示按销售额排名前 2 的运动项目。由于 `Sales` 之和是索引为 0 的数据字段，因此 `rankBy` 为 0。

```javascript
const AsposeCells = require("aspose.cells");

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");```

```

### **按字段本身排名**
字段也可以按自身进行排名，只需将 -1 作为 `rankBy` 传入。此变体无需额外的数据字段；该字段只需位于行（或列）区域。以下示例显示按字段本身排名的后 3 个运动项目。保存此设置时，数据透视表 XML 中会省略 `rankBy` 属性，因为 -1 是该格式的默认值，而 `getTop10AutoShowSettings().getRankBy()` 读取的结果为 -1。

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the bottom 3 items ranked by the field itself (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");```
```

## **读取当前选项（Top10AutoShowSettings）**
`PivotField.getTop10AutoShowSettings()` 方法返回一个 `PivotFieldTop10AutoShowSettings` 对象，该对象提供对字段当前存储的 AutoShow 选项的访问。可使用它来检查现有工作簿或刚配置的数据透视表将如何显示其中的项目；这也适用于从文件加载的工作簿。

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("output-top10-by-value-field.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const sportField = pivotTable.getRowFields().get(0);
const settings = sportField.getTop10AutoShowSettings();
console.log("AutoShow enabled: " + settings.isAutoShow());
console.log("Direction: " + (settings.isTop() ? "Top" : "Bottom"));
console.log("Item count: " + settings.getAutoShowCount());
console.log("Ranking data field index: " + settings.getRankBy());
```

`isAutoShow()`、`isTop()`、`getAutoShowCount()` 和 `getRankBy()` 等读取方法对应于写入数据透视表 XML 的经典 AutoShow 属性（`autoShow`、`topAutoShow`、`itemPageCount`、`rankBy`），因此读回的数值就是所有 Excel 版本都会遵循的数值。

## **注意**

{{% alert color="primary" %}}
- `PivotField` 的直接读取方法 `isAutoShow()`、`isAscendShow()`、`getAutoShowCount()` 和 `getAutoShowField()` 已标记为过时。请改用 `getTop10AutoShowSettings()` 返回的对象：`isAutoShow()` 对应 `getTop10AutoShowSettings().isAutoShow()`，`isAscendShow()` 对应 `getTop10AutoShowSettings().isTop()`，`getAutoShowCount()` 对应 `getTop10AutoShowSettings().getAutoShowCount()`，`getAutoShowField()` 对应 `getTop10AutoShowSettings().getRankBy()`。修改这些设置时，应使用受支持的 `top10AutoShow()` 方法。
- `top10AutoShow()` 可用于行字段和列字段。仅位于筛选区域中的字段无法通过这种方式排名，因为其项目不会显示在数据透视表主体中。
{{% /alert %}}

## **Excel 2007-365：前 10 项筛选（FilterTop10）**
现代 Excel 版本在字段菜单中提供“值筛选”选项，其中包含“前 10 项...”筛选。Aspose.Cells 通过 `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)` 方法实现此筛选，该方法返回已创建的 `PivotFilter`：
- `valueFieldIndex` — 数据字段的索引（从 0 开始），该字段的汇总值将用于对项目进行排名。
- `type` — 指定 `itemCount` 的含义。`PivotFilterType.COUNT` 保留固定数量的项目（对应对话框中的“项目数”选项）。`PivotFilterType.PERCENT` 保留项目的一定百分比，因此 `itemCount` 本身就是百分比值——30 表示保留前 30%。`PivotFilterType.SUM` 根据累计值覆盖的比例进行排名。
- `isTop` — `true` 表示前 N 项，`false` 表示后 N 项。
- `itemCount` — “前 N 项”中的 N；其单位取决于 `type`。

```javascript
const AsposeCells = require("aspose.cells");

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
const filter = sportField.filterTop10(0, AsposeCells.PivotFilterType.COUNT, true, 2);
// For a percentage-based filter instead, keep the top 30 percent of the items:
// sportField.filterTop10(0, AsposeCells.PivotFilterType.PERCENT, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");```

```

{{% alert color="primary" %}}
`top10AutoShow()` 和 `filterTop10()` 是两个彼此独立的功能。AutoShow 会将经典 `autoShow` 属性写入数据透视字段，并且从 Excel 97 起的所有 Excel 版本均支持这组设置。`filterTop10()` 会写入现代 `PivotFilter` 条目，该功能要求 Excel 2007 或更高版本。使用较旧 Excel 版本打开工作簿时，使用现代筛选器的数据透视表将改为显示所有项目。对于必须通过旧版工具进行往返处理的文档，建议优先使用 `top10AutoShow()`；对于现代工作簿，建议优先使用 `filterTop10()`，因为它可与其他值筛选器结合使用。
{{% /alert %}}

## **相关文章**
- [按标签或值筛选数据透视表](/cells/zh/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [添加数据透视表行字段和列字段](/cells/zh/nodejs-java/pivot-table-add-row-and-column-fields/)
- [对数据透视表中的数据透视字段进行分组](/cells/zh/nodejs-java/group-pivot-fields-in-the-pivot-table/)
- [刷新数据透视表](/cells/zh/nodejs-java/refresh-pivot-table/)
- [在数据透视表中添加页字段](/cells/zh/nodejs-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}