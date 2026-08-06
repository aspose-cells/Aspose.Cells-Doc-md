---
title: 修改数据透视表中的页面字段布局
linktitle: 修改数据透视表中的页面字段布局
description: 了解如何使用 Aspose.Cells for Node.js via C++ 控制数据透视表中页面字段区域的布局，包括设置页面字段的显示顺序、换行数量和字段顺序。
keywords: Aspose.Cells, Node.js via C++ 库, 电子表格, 数据透视表, 页面字段, 页面字段顺序, 页面字段换行数, 移动页面字段
type: docs
weight: 191
url: /zh/nodejs-cpp/change-page-field-layout/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
本文是 **在数据透视表中添加页面字段** 主题的延续。它演示了如何控制页面字段区域的布局——即数据透视表顶部的筛选控件条，包括显示顺序、换行数量和字段重新排序。
{{% /alert %}}
## **简介**
Microsoft Excel 中的数据透视表有一个专用的**页面字段区域**，位于数据透视表的行/列/数据主体之上。该区域呈现为一行下拉筛选控件（每个页面字段一个），是终端用户点击按年份或地区等条件对数据透视表进行切片的地方。Aspose.Cells for Node.js via C++ 通过 `pivotTable.pageFields` 集合对此区域进行建模，并公开了三个属性来控制该区域的视觉布局：
- `pivotTable.pageFieldOrder`（一个 `Aspose.Cells.PrintOrderType` 值）决定其他页面字段是放置在现有字段*旁边*还是*下方*。
- `pivotTable.pageFieldWrapCount` 设置在换行之前每行或每列放置多少个页面字段。
- `pivotTable.pageFields.move(currIndex, destIndex)` 用于在不更改顺序模式的情况下重新排序页面字段。
本文通过三个代码示例演示了这些操作，每个示例都使用同一数据集，以便您可以并排比较生成的布局。
## **源数据**
下面的所有示例都将这八行销售数据加载到名为 `PivotData` 的工作表中。数据包含两个页面字段候选（`Year`、`Region`）、一个行字段候选（`Fruit`）和一个度量（`Amount`），这使得页面字段条值得检查。
在每个代码示例中，所有八行都以相同的顺序填充，因此各个场景之间的源数据没有差异——唯一的区别是页面字段布局属性。
## **示例 1：先行后列**
在第一个场景中，我们将两个页面字段（`Year`、`Region`）配置为出现在数据透视表顶部的**单行并排**。我们将 `Fruit` 分配到行轴，先将 `Year` 放在页面轴上，再将 `Region` 放在第二位（`addFieldToArea` 调用的顺序决定了起始索引），将 `Amount`（Sum）作为数据字段，然后将 `pageFieldOrder` 设为 `PrintOrderType.OverThenDown`，并设置 `pageFieldWrapCount = 2`。使用 `OverThenDown` 和换行数为 2 时，两个页面字段在数据透视表顶部以单行水平并排布局，因此该条带占用宽度为 2 的一行。
```javascript
let dataDir = "output";
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true });
}

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

// 第1行：Apple，2022年，北方，150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);

// 第2行：Apple，2023年，北方，180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);

// 第3行：Banana，2022年，南方，120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);

// 第4行：Banana，2023年，南方，140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);

// 第5行：Cherry，2022年，东方，200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);

// 第6行：Cherry，2023年，东方，220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);

// 第7行：Grape，2022年，西方，90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);

// 第8行：Grape，2023年，西方，110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);

// 添加透视表报表工作表
let pivotTableSheetIdx = worksheets.add("PivotTableReport");
let pivotTableSheet = worksheets.get(pivotTableSheetIdx);
let pivotTables = pivotTableSheet.getPivotTables();

// 创建数据源为PivotData!A1:D9的透视表，放在PivotTableReport的A1位置
let pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);

// 添加字段
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // 水果
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // 年份
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // 地区
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // 金额
pivotTable.getDataFields().get(0).setFunction(AsposeCells.ConsolidationFunction.Sum);

// 配置页字段区域布局：先横向排列页字段，每2个换行
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);

// 刷新和计算
pivotTable.calculateData();

// 保存
workbook.save(path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```
## **示例 2：先列后行**
在此示例中，我们将 `Fruit` 放在行轴上，将 `Year` 和 `Region` 放在页面轴上（`Year` 在前），并将 `Amount`（Sum）作为数据字段——与示例 1 完全相同。然后我们将 `pageFieldOrder` 设为 `PrintOrderType.DownThenOver`，并将 `pageFieldWrapCount` 设为 `2`。使用 `DownThenOver` 和换行数为 2 时，两个页面字段垂直堆叠——`Year` 在顶部，`Region` 直接在其下方，形成一个位于数据透视表顶部的单列。因此，与示例 1 相比，该条带占用宽度为 1 的两行。
```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
const pivotReportIdx = workbook.getWorksheets().add("PivotTableReport");
const pivotReport = workbook.getWorksheets().get(pivotReportIdx);

const headers = ["Fruit", "Year", "Region", "Amount"];
for (let c = 0; c < headers.length; c++) {
    pivotData.getCells().get(0, c).putValue(headers[c]);
}

const data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
];

for (let r = 0; r < data.length; r++) {
    for (let c = 0; c < data[r].length; c++) {
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

const idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
const pivotTable = pivotReport.getPivotTables().get(idx);

pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, 3);

pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.DownThenOver);
pivotTable.setPageFieldWrapCount(2);

pivotTable.calculateData();

workbook.save("pageFieldLayout_downThenOver.xlsx");
```
## **示例 3：移动页面字段**
在第三个场景中，我们保留此数据集和字段分配，设置中性布局（`OverThenDown` 与换行数 `2`），然后演示 `pageFields.move` 操作。`move(0, 1)` 调用将索引 0 处的页面字段（`Year`）移动到位置 1，原来位于位置 1 的页面字段（`Region`）移至位置 0。调用后，`Region` 成为第一个页面字段，`Year` 成为第二个页面字段。换行和顺序模式不变，因此该条带仍以水平并排方式呈现——只是两个下拉框的顺序被交换了。
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

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);

pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);

pivotTable.getPageFields().move(0, 1);

pivotTable.calculateData();

workbook.save("pageFieldLayout_move.xlsx");
```
## **相关文章**
- [在数据透视表中添加页面字段](/cells/zh/nodejs-cpp/add-page-field-in-pivot-table/) — 介绍如何将页面字段添加到数据透视表的父页面。
- [数据透视表中的行和列字段](/cells/zh/nodejs-cpp/row-and-column-fields/) — 介绍如何将字段分配到行和列轴，是对本文页面轴相关内容的补充。
- [管理数据透视表中的值字段](/cells/zh/nodejs-cpp/manage-value-fields/) — 介绍如何配置数据（值）区域，包括本文中使用的 `Sum` 聚合。
- [刷新数据透视表](/cells/zh/nodejs-cpp/refresh-pivot-table/) — 解释 `refreshData` 和 `calculateData` 的用法，在重新排序页面字段后需要用到这两个操作。
- [将样式应用于数据透视表](/cells/zh/nodejs-cpp/apply-style-to-pivot-table/) — 展示在页面字段条布局完成后如何对已渲染的数据透视表进行格式化。
{{< app/cells/assistant language="nodejs-cpp" >}}