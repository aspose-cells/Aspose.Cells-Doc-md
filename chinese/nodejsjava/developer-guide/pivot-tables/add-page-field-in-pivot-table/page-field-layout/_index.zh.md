---
title: 修改数据透视表中的页面字段布局
linktitle: 修改数据透视表中的页面字段布局
description: 学习如何使用 Aspose.Cells for Node.js via Java 控制数据透视表中页面字段区域的布局，包括设置数据透视表顶部页面字段的显示顺序、换行数以及字段顺序。
keywords: Aspose.Cells, Node.js via Java 库, 电子表格, 数据透视表, 页面字段, 页面字段顺序, 页面字段换行数, 移动页面字段
type: docs
weight: 191
url: /zh/nodejs-java/change-page-field-layout/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
本文是 **在数据透视表中添加页面字段** 主题的延续。它演示了如何控制页面字段区域（即数据透视表顶部的一行筛选器控件）的布局，包括显示顺序、换行数和字段重排序。
{{% /alert %}}
## **简介**
在 Microsoft Excel 中，数据透视表会在表的行/列/数据主体之上提供一个专门的 **页面字段区域**。该区域呈现为一行下拉筛选器控件（每个页面字段对应一个），最终用户通过点击这些控件按年份或区域等条件对透视表进行切片。Aspose.Cells 通过 `PivotTable.PageFields` 集合对该区域进行建模，并提供三个属性来控制该行控件的视觉布局：
- `PivotTable.PageFieldOrder`（一个 `Aspose.Cells.PrintOrderType` 枚举值）决定新增加的页面字段是 *放置在* 已有字段 *旁边* 还是 *下方*。
- `PivotTable.PageFieldWrapCount` 设置每行或每列放置多少个页面字段后进行换行。
- `PivotTable.PageFields.Move(currIndex, destIndex)` 重排页面字段的顺序，但不改变排序模式。
本文将通过三个代码示例，在同一份共享数据集上演示上述各项操作，便于您并排比较所产生的不同布局效果。
## **源数据**
下面的所有三个示例都会将这八行销售数据加载到名为 `PivotData` 的工作表中。数据包含两个页面字段候选（`Year`、`Region`）、一个行字段候选（`Fruit`）以及一个度量值（`Amount`），这使得检查页面字段控件行具有实际意义。
在每个代码示例中，这八行数据均按相同顺序填入，因此各场景之间的源数据始终保持一致——不同的仅是页面字段的布局属性。
## **示例 1：先行后列（Over Then Down）**
在第一种场景中，我们将两个页面字段（`Year`、`Region`）配置为 **并排显示在数据透视表顶部的同一行** 中。我们将 `Fruit` 分配到行轴，将 `Year` 放在页面轴的第一位、`Region` 放在第二位（`addFieldToArea` 调用的顺序决定了起始索引），将 `Amount`（Sum）添加为数据字段，然后将 `PageFieldOrder` 设置为 `PrintOrderType.OVER_THEN_DOWN`，并将 `PageFieldWrapCount` 设置为 `2`。使用 `OVER_THEN_DOWN` 且换行数为 2 时，两个页面字段将在数据透视表顶部水平并排显示于同一行，因此该控件行占据宽度为 2 的一行。
```javascript
let dataDir = "output";
if (!fs.existsSync(dataDir)) fs.mkdirSync(dataDir, { recursive: true });

let workbook = new AsposeCells.Workbook();
let worksheets = workbook.getWorksheets();

let pivotDataIdx = worksheets.add("PivotData");
let pivotDataSheet = worksheets.get(pivotDataIdx);
let pivotDataCells = pivotDataSheet.getCells();

// 表头（第0行）
pivotDataCells.get(0, 0).putValue("Fruit");
pivotDataCells.get(0, 1).putValue("Year");
pivotDataCells.get(0, 2).putValue("Region");
pivotDataCells.get(0, 3).putValue("Amount");

// 第1行：苹果，2022年，北方，150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);

// 第2行：苹果，2023年，北方，180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);

// 第3行：香蕉，2022年，南方，120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);

// 第4行：香蕉，2023年，南方，140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);

// 第5行：樱桃，2022年，东方，200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);

// 第6行：樱桃，2023年，东方，220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);

// 第7行：葡萄，2022年，西方，90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);

// 第8行：葡萄，2023年，西方，110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);

// 添加 PivotTableReport 工作表
let pivotTableSheetIdx = worksheets.add("PivotTableReport");
let pivotTableSheet = worksheets.get(pivotTableSheetIdx);
let pivotTables = pivotTableSheet.getPivotTables();

// 在 PivotTableReport 的 A1 位置创建数据源为 PivotData!A1:D9 的数据透视表
let pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);

// 添加字段
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // 水果
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // 年份
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // 地区
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // 金额
pivotTable.getDataFields().get(0).setFunction(AsposeCells.ConsolidationFunction.Sum);

// 配置页字段区域布局：先横向排列页字段，每 2 个换行
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);

// 刷新并计算
pivotTable.calculateData();

// 保存
workbook.save(path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```
## **示例 2：先列后行（Down Then Over）**
在本示例中，我们将 `Fruit` 放在行轴上，将 `Year` 和 `Region` 放在页面轴上（`Year` 在前），并将 `Amount`（Sum）作为数据字段——与示例 1 完全一致。随后，我们将 `PageFieldOrder` 设置为 `PrintOrderType.DOWN_THEN_OVER`，并将 `PageFieldWrapCount` 设置为 `2`。使用 `DOWN_THEN_OVER` 且换行数为 2 时，两个页面字段将垂直堆叠——`Year` 在上，`Region` 紧接其下方——形成位于数据透视表顶部的一列。因此，该控件行占据宽度为 1 的两行，与示例 1 形成对照。
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
在第三种场景中，我们沿用相同的数据集和字段分配，先设置一个中性布局（`OVER_THEN_DOWN`，换行数为 `2`），然后演示 `PageFields.Move` 操作。`Move(0, 1)` 调用会将索引 0 处的页面字段（`Year`）移动到位置 1，而原本位于位置 1 的页面字段（`Region`）则会移动到位置 0。调用之后，`Region` 成为第一个页面字段，`Year` 成为第二个页面字段。换行和排序模式保持不变，因此该控件行仍以水平并排方式呈现——仅有这两个下拉控件的先后顺序被调换。
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
- [在数据透视表中添加页面字段](/cells/zh/nodejs-java/add-page-field-in-pivot-table/) — 父级页面，介绍如何向数据透视表添加页面字段。
- [数据透视表中的行字段和列字段](/cells/zh/nodejs-java/row-and-column-fields/) — 介绍如何将字段分配到行轴和列轴，作为本文所讨论的页面字段轴内容的补充。
- [管理数据透视表中的值字段](/cells/zh/nodejs-java/manage-value-fields/) — 说明如何配置数据（值）区域，包括本文使用的 `Sum` 聚合方式。
- [刷新数据透视表](/cells/zh/nodejs-java/refresh-pivot-table/) — 解释 `refreshData` 和 `calculateData`，这是在重排页面字段之后必须执行的操作。
- [为数据透视表应用样式](/cells/zh/nodejs-java/apply-style-to-pivot-table/) — 展示在页面字段控件行的布局确定后，如何为渲染后的数据透视表设置格式。
{{< app/cells/assistant language="nodejs-java" >}}