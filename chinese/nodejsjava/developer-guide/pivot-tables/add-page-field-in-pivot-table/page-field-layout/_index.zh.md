---
title: 修改数据透视表中的页面字段布局
description: 学习如何使用 Aspose.Cells for Node.js via Java 控制数据透视表中页面字段区域的布局，包括设置数据透视表顶部页面字段的显示顺序、换行数以及字段顺序。
linktitle: 修改数据透视表中的页面字段布局
keywords: Aspose.Cells, Node.js via Java 库, 电子表格, 数据透视表, 页面字段, 页面字段顺序, 页面字段换行数, 移动页面字段
type: docs
weight: 191
url: /zh/nodejs-java/change-page-field-layout/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
本文是 **在数据透视表中添加页面字段** 主题的延续。它演示了如何控制页面字段区域的布局——即数据透视表顶部的筛选器控件条，包括显示顺序、换行数和字段重新排序。
{{% /alert %}}

## **介绍**
Microsoft Excel 中的数据透视表提供了一个专用的 **页面字段区域**，位于表的行/列/数据主体上方。该区域以筛选器下拉控件条的形式呈现（每个页面字段一个控件），终端用户通过单击它来按年份或区域等条件对数据透视表进行切片。Aspose.Cells 通过 `PivotTable.PageFields` 集合对该区域进行建模，并公开了三个属性来控制该控件条的视觉布局：
- `PivotTable.PageFieldOrder`（一个 `Aspose.Cells.PrintOrderType` 值）决定其他页面字段是放置在现有字段**旁边**还是**下方**。
- `PivotTable.PageFieldWrapCount` 设置每行或每列放置多少个页面字段后再换行。
- `PivotTable.PageFields.Move(currIndex, destIndex)` 重新排列页面字段，而不更改顺序模式。
本文通过三个代码示例演示了在同一数据集上的每种操作，以便您可以并排比较所产生的布局。

## **源数据**
下面的所有三个示例将这八行销售数据加载到名为 `PivotData` 的工作表中。数据包含两个页面字段候选（`Year`、`Region`）、一个行字段候选（`Fruit`）和一个度量值（`Amount`），这使得页面字段条便于查看。
每个代码示例都以相同的顺序填充所有八行，因此源数据在不同场景之间始终保持一致——只有页面字段的布局属性会发生变化。

## **示例 1：先横向后纵向**
在第一个场景中，我们将两个页面字段（`Year`、`Region`）配置为在数据透视表顶部**并排显示在一行中**。我们将 `Fruit` 分配到行轴，将 `Year` 放在页面轴的第一位，`Region` 放在第二位（`addFieldToArea` 调用的顺序决定起始索引），将 `Amount`（Sum）添加为数据字段，然后将 `PageFieldOrder` 设置为 `PrintOrderType.OVER_THEN_DOWN`，并将 `PageFieldWrapCount` 设置为 `2`。使用 `OVER_THEN_DOWN` 和换行数 2，两个页面字段在数据透视表顶部水平并排显示在一行中，因此该控件条占据宽度为二的一行。

```javascript
let dataDir = "output";
if (!fs.existsSync(dataDir)) fs.mkdirSync(dataDir, { recursive: true });
let workbook = new AsposeCells.Workbook();
let worksheets = workbook.getWorksheets();
let pivotDataIdx = worksheets.add("PivotData");
let pivotDataSheet = worksheets.get(pivotDataIdx);
let pivotDataCells = pivotDataSheet.getCells();
// 表头（第 0 行）
pivotDataCells.get(0, 0).putValue("Fruit");
pivotDataCells.get(0, 1).putValue("Year");
pivotDataCells.get(0, 2).putValue("Region");
pivotDataCells.get(0, 3).putValue("Amount");
// 第 1 行：Apple, 2022, North, 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);
// 第 2 行：Apple, 2023, North, 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);
// 第 3 行：Banana, 2022, South, 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);
// 第 4 行：Banana, 2023, South, 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);
// 第 5 行：Cherry, 2022, East, 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);
// 第 6 行：Cherry, 2023, East, 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);
// 第 7 行：Grape, 2022, West, 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);
// 第 8 行：Grape, 2023, West, 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);
// 添加 PivotTableReport 工作表
let pivotTableSheetIdx = worksheets.add("PivotTableReport");
let pivotTableSheet = worksheets.get(pivotTableSheetIdx);
let pivotTables = pivotTableSheet.getPivotTables();
// 创建数据源为 PivotData!A1:D9 的透视表，并放置在 PivotTableReport 的 A1 单元格
let pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);
// 添加字段
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // Fruit（水果）
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // Year（年份）
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // Region（地区）
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // Amount（金额）
pivotTable.getDataFields().get(0).setFunction(AsposeCells.ConsolidationFunction.Sum);
// 配置页面字段区域布局：先横向排列页面字段，每 2 个换行
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);
// 刷新并计算
pivotTable.calculateData();
// 保存
workbook.save(path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```

## **示例 2：先纵向后横向**
在本例中，我们将 `Fruit` 放在行轴上，将 `Year` 和 `Region` 放在页面轴上（`Year` 在前），并将 `Amount`（Sum）作为数据字段——与示例 1 完全相同。然后我们将 `PageFieldOrder` 设置为 `PrintOrderType.DOWN_THEN_OVER`，并将 `PageFieldWrapCount` 设置为 `2`。使用 `DOWN_THEN_OVER` 和换行数 2，两个页面字段垂直堆叠——`Year` 在顶部，`Region` 直接位于其下方——在数据透视表顶部形成单列。因此，该控件条占据宽度为一的两行，这与示例 1 形成对比。

```javascript
var workbook = new AsposeCells.Workbook();
var pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
var pivotReportIdx = workbook.getWorksheets().add("PivotTableReport");
var pivotReport = workbook.getWorksheets().get(pivotReportIdx);
var headers = ["Fruit", "Year", "Region", "Amount"];
for (var c = 0; c < headers.length; c++)
{
    pivotData.getCells().get(0, c).putValue(headers[c]);
}
var data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
];
for (var r = 0; r < data.length; r++)
{
    for (var c = 0; c < data[r].length; c++)
    {
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}
var idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
var pivotTable = pivotReport.getPivotTables().get(idx);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.DownThenOver);
pivotTable.setPageFieldWrapCount(2);
pivotTable.calculateData();
workbook.save("pageFieldLayout_downThenOver.xlsx");
```

## **示例 3：移动页面字段**
在第三个场景中，我们保留该数据集和字段分配，设置中性布局（`OVER_THEN_DOWN` 和换行数 `2`），然后演示 `PageFields.Move` 操作。`Move(0, 1)` 调用将索引 0 处的页面字段（`Year`）移动到位置 1，原来在位置 1 的页面字段（`Region`）则移动到位置 0。调用后，`Region` 成为第一个页面字段，`Year` 成为第二个。换行和顺序模式保持不变，因此该控件条仍以水平并排方式呈现——只是两个下拉控件的顺序已交换。

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const dataSheet = workbook.getWorksheets().get(0);
dataSheet.setName("PivotData");
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Year");
dataSheet.getCells().get("C1").putValue("Region");
dataSheet.getCells().get("D1").putValue("Amount");
dataSheet.getCells().get("A2").putValue("Apple");
dataSheet.getCells().get("B2").putValue(2022);
dataSheet.getCells().get("C2").putValue("North");
dataSheet.getCells().get("D2").putValue(150);
dataSheet.getCells().get("A3").putValue("Apple");
dataSheet.getCells().get("B3").putValue(2023);
dataSheet.getCells().get("C3").putValue("North");
dataSheet.getCells().get("D3").putValue(180);
dataSheet.getCells().get("A4").putValue("Banana");
dataSheet.getCells().get("B4").putValue(2022);
dataSheet.getCells().get("C4").putValue("South");
dataSheet.getCells().get("D4").putValue(120);
dataSheet.getCells().get("A5").putValue("Banana");
dataSheet.getCells().get("B5").putValue(2023);
dataSheet.getCells().get("C5").putValue("South");
dataSheet.getCells().get("D5").putValue(140);
dataSheet.getCells().get("A6").putValue("Cherry");
dataSheet.getCells().get("B6").putValue(2022);
dataSheet.getCells().get("C6").putValue("East");
dataSheet.getCells().get("D6").putValue(200);
dataSheet.getCells().get("A7").putValue("Cherry");
dataSheet.getCells().get("B7").putValue(2023);
dataSheet.getCells().get("C7").putValue("East");
dataSheet.getCells().get("D7").putValue(220);
dataSheet.getCells().get("A8").putValue("Grape");
dataSheet.getCells().get("B8").putValue(2022);
dataSheet.getCells().get("C8").putValue("West");
dataSheet.getCells().get("D8").putValue(90);
dataSheet.getCells().get("A9").putValue("Grape");
dataSheet.getCells().get("B9").putValue(2023);
dataSheet.getCells().get("C9").putValue("West");
dataSheet.getCells().get("D9").putValue(110);
const pivotSheetIdx = workbook.getWorksheets().add("PivotTableReport");
const pivotSheet = workbook.getWorksheets().get(pivotSheetIdx);
const pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable");
const pivotTable = pivotSheet.getPivotTables().get(pivotIdx);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.ROW, 0);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, 1);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, 2);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.DATA, 3);
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);
pivotTable.getPageFields().move(0, 1);
pivotTable.calculateData();
workbook.save("pageFieldLayout_move.xlsx");
```

## **相关文章**
- [在数据透视表中添加页面字段](/cells/zh/nodejs-java/add-page-field-in-pivot-table/) — 介绍如何向数据透视表添加页面字段的父页面。
- [数据透视表中的行和列字段](/cells/zh/nodejs-java/row-and-column-fields/) — 介绍如何将字段分配到行轴和列轴，作为本文页面轴工作的补充。
- [管理数据透视表中的值字段](/cells/zh/nodejs-java/manage-value-fields/) — 介绍如何配置数据（值）区域，包括本文使用的 `Sum` 聚合。
- [刷新数据透视表](/cells/zh/nodejs-java/refresh-pivot-table/) — 介绍 `refreshData` 和 `calculateData`，在重新排列页面字段后需要执行这些操作。
- [对数据透视表应用样式](/cells/zh/nodejs-java/apply-style-to-pivot-table/) — 展示在页面字段条布局完成后如何对渲染的数据透视表进行格式化。

{{< app/cells/assistant language="nodejs-java" >}}