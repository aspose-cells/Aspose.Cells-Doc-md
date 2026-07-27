---
title: 在 Aspose.Cells for Node.js via Java 中刷新数据透视表
linktitle: 在 Aspose.Cells for Node.js via Java 中刷新数据透视表
description: 学习如何使用 v26.7+ 的 pivot-refresh API 在 Aspose.Cells for Node.js via Java 中刷新数据透视表。本文涵盖 RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData 和 GetPivotTables，并附有实用代码示例。
keywords: Aspose.Cells, Node.js, Java, 数据透视表, 刷新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /zh/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


- ```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2021);
worksheet.getCells().get("C3").putValue(150);

worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);

worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2021);
worksheet.getCells().get("C5").putValue(120);

worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(180);

worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2020);
worksheet.getCells().get("C7").putValue(130);

worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(220);

worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2020);
worksheet.getCells().get("C9").putValue(140);

let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);

worksheet.refreshPivotTables();

workbook.save("output.xlsx");
```
- ```javascript
const AsposeCells = require("aspose.cells");

// 创建一个新工作簿并访问第一个工作表
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// 写入表头行：水果 / 年份 / 金额
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 写入大约 9 行数据（葡萄 / 蓝莓 / 猕猴桃 / 樱桃，跨 2020-2021 年）
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

// 添加第一个数据透视表 "Pivot1"，锚定在单元格 E3，源数据区域为 A1:C9
const pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// 为 Pivot1 分配字段
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 添加第二个数据透视表 "Pivot2"，锚定在 E15，使用相同的源数据区域 A1:C9
// 由于源数据区域相同，Pivot1 和 Pivot2 共享同一个 PivotCache（透视缓存）。
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// 为 Pivot2 分配相同的字段
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 修改源数据中几个 Amount 单元格的值，以模拟数据变化
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// 刷新共享的 PivotCache。
// 因为 Pivot1 和 Pivot2 共享同一个 PivotCache，所以这一行调用
// 会同时刷新两个数据透视表（数据和样式），从更新后的源数据中获取。
pivotTable1.getPivotCache().refresh();

// 保存工作簿
workbook.save("output.xlsx");
```
- ```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// 写入 Fruit / Year / Amount 表头行
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 写入 8 行数据（第 2-9 行，匹配源数据范围 A1:C9）
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);

- ```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- 构建源数据：水果 / 年份 / 金额（表头 + 9 行数据）---
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000);
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500);
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500);
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000);
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800);
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200);
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700);

// --- 在目标单元格 E3 处添加第一个数据透视表（Pivot1）---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- 在同一源数据范围上添加第二个数据透视表（Pivot2）---
// Pivot1 和 Pivot2 共用一个底层的 PivotCache（透视缓存）。
// 这正是一个典型的场景：在这种场景下，旧版逐表调用 RefreshData()
// 的方式会变得非常低效——刷新其中一个表会重新获取整个共享缓存，
// 因此刷新 N 个表就会执行 N 次同样昂贵的获取操作。
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- 修改源数据中的若干 Amount 值 ---
sheet.getCells().get("C2").putValue(5000);   // Grape  2020
sheet.getCells().get("C5").putValue(7500);   // Cherry 2020
sheet.getCells().get("C9").putValue(9500);   // Cherry 2021

// --- 已废弃的写法（26.7 版本之前）—— PivotTable.RefreshData() ---
// pivotTable1.refreshData();  // 从源数据重新获取，并刷新整个缓存
// pivotTable2.refreshData();  // 再次重新获取——缓存其实已经是新的了！
// 每次调用都会重建共享缓存，因此 N 个表就会产生 N 次冗余的获取操作。

// --- 新版 v26.7+ 写法：只需刷新缓存一次，然后按需重新渲染 ---
// 调用一次 PivotCache.Refresh() 即可将修改后的值拉取到共享缓存中，
// 并重新计算所有引用该缓存的数据透视表的显示结果。
// 由于 Pivot1 和 Pivot2 共用一个 PivotCache，这一次性调用就能
// 同时更新两个表——无需再次回到源数据去拉取。
pivotTable1.getPivotCache().refresh();

// CalculateData() 仅根据缓存中已有的数据重新渲染数据透视表的显示
// （数据 + 样式），并不会访问源数据。
// 这里对 Pivot2 调用它纯粹是为了演示该 API：缓存刷新一次之后，
// 任何依赖该缓存的表都可以重新渲染，而无需再次访问源数据。
// 当只有数据透视表的视图/布局设置发生更改、而缓存仍然是最新的
// 情况下，可以单独使用 CalculateData()。
pivotTable2.calculateData();

workbook.save("output.xlsx");javascript
const AsposeCells = require("aspose.cells");

// 创建一个新的工作簿
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// 将表头行写入单元格 A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 将数据行写入单元格 A2:C9（2020 和 2021 年共 8 行水果数据）
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(50);

worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(60);

worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(70);

worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(80);

worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(90);

worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(100);

worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(110);

worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(120);

// 添加数据透视表：源区域 "A1:C9"，目标单元格 "E3"，名称 "Pivot1"
const pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

// 分配透视字段：Fruit 到行，Year 到列，Amount 到数据
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 修改源数据中的几个 Amount 值以模拟变化
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// 刷新工作簿中的每个数据透视表/透视缓存
workbook.refreshAll();

// 保存工作簿
workbook.save("output.xlsx");javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2021);
worksheet.getCells().get("C3").putValue(150);

worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);

worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2021);
worksheet.getCells().get("C5").putValue(120);

worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(180);

worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2020);
worksheet.getCells().get("C7").putValue(130);

worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(220);

worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2020);
worksheet.getCells().get("C9").putValue(140);

let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);

worksheet.refreshPivotTables();

workbook.save("output.xlsx");javascript
const AsposeCells = require("aspose.cells");

// 创建一个新工作簿并访问第一个工作表
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// 写入表头行：水果 / 年份 / 金额
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 写入大约 9 行数据（葡萄 / 蓝莓 / 猕猴桃 / 樱桃，跨 2020-2021 年）
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

// 添加第一个数据透视表 "Pivot1"，锚定在单元格 E3，源数据区域为 A1:C9
const pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// 为 Pivot1 分配字段
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 添加第二个数据透视表 "Pivot2"，锚定在 E15，使用相同的源数据区域 A1:C9
// 由于源数据区域相同，Pivot1 和 Pivot2 共享同一个 PivotCache（透视缓存）。
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// 为 Pivot2 分配相同的字段
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 修改源数据中几个 Amount 单元格的值，以模拟数据变化
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// 刷新共享的 PivotCache。
// 因为 Pivot1 和 Pivot2 共享同一个 PivotCache，所以这一行调用
// 会同时刷新两个数据透视表（数据和样式），从更新后的源数据中获取。
pivotTable1.getPivotCache().refresh();

// 保存工作簿
workbook.save("output.xlsx");javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// 写入 Fruit / Year / Amount 表头行
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 写入 8 行数据（第 2-9 行，匹配源数据范围 A1:C9）
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Sheet1");

worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);

let pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = worksheet.getPivotTables().get(pivot1Index);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let sameCache = pivotTable1.getPivotCache() === pivotTable2.getPivotCache();

let sharedPivotTables = pivotTable1.getPivotCache().getPivotTables();
console.log("Number of pivot tables sharing the cache: " + sharedPivotTables.length);

for (let pt of sharedPivotTables) {
    console.log("Pivot table name: " + pt.getName());
}

workbook.save("output.xlsx");javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- 构建源数据：水果 / 年份 / 金额（表头 + 9 行数据）---
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000);
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500);
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500);
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000);
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800);
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200);
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700);

// --- 在目标单元格 E3 处添加第一个数据透视表（Pivot1）---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- 在同一源数据范围上添加第二个数据透视表（Pivot2）---
// Pivot1 和 Pivot2 共用一个底层的 PivotCache（透视缓存）。
// 这正是一个典型的场景：在这种场景下，旧版逐表调用 RefreshData()
// 的方式会变得非常低效——刷新其中一个表会重新获取整个共享缓存，
// 因此刷新 N 个表就会执行 N 次同样昂贵的获取操作。
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- 修改源数据中的若干 Amount 值 ---
sheet.getCells().get("C2").putValue(5000);   // Grape  2020
sheet.getCells().get("C5").putValue(7500);   // Cherry 2020
sheet.getCells().get("C9").putValue(9500);   // Cherry 2021

// --- 已废弃的写法（26.7 版本之前）—— PivotTable.RefreshData() ---
// pivotTable1.refreshData();  // 从源数据重新获取，并刷新整个缓存
// pivotTable2.refreshData();  // 再次重新获取——缓存其实已经是新的了！
// 每次调用都会重建共享缓存，因此 N 个表就会产生 N 次冗余的获取操作。

// --- 新版 v26.7+ 写法：只需刷新缓存一次，然后按需重新渲染 ---
// 调用一次 PivotCache.Refresh() 即可将修改后的值拉取到共享缓存中，
// 并重新计算所有引用该缓存的数据透视表的显示结果。
// 由于 Pivot1 和 Pivot2 共用一个 PivotCache，这一次性调用就能
// 同时更新两个表——无需再次回到源数据去拉取。
pivotTable1.getPivotCache().refresh();

// CalculateData() 仅根据缓存中已有的数据重新渲染数据透视表的显示
// （数据 + 样式），并不会访问源数据。
// 这里对 Pivot2 调用它纯粹是为了演示该 API：缓存刷新一次之后，
// 任何依赖该缓存的表都可以重新渲染，而无需再次访问源数据。
// 当只有数据透视表的视图/布局设置发生更改、而缓存仍然是最新的
// 情况下，可以单独使用 CalculateData()。
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## 应该使用哪个刷新 API？

下表汇总了可用的刷新 API 以及何时选择每一个。

| 目标 | 推荐的 API | 备注 |
|------|-----------------|-------|
| 刷新工作簿中的所有内容 | `Workbook.RefreshAll()` | 一次调用；涵盖所有缓存和表。 |
| 仅刷新单个工作表上的数据透视表 | `Worksheet.RefreshPivotTables()` | 范围限定于一个工作表。 |
| 一个缓存的源数据已更改 | `pivotTable.PivotCache.Refresh()` | 刷新该共享缓存上的所有数据透视表。 |
| 仅视图/布局设置已更改 | `pivotTable.CalculateData()` | 跳过不必要的源往返。 |
| 列出共享缓存上的所有数据透视表 | `pivotCache.GetPivotTables()` | 用于在批量刷新之前进行枚举。 |

在实践中，应优先选择基于缓存的 API，而不是过时的按表调用 `RefreshData()`。它们能够感知共享缓存，避免冗余的源获取，并允许您选择满足刷新需求的最小范围。{{< app/cells/assistant language="javascript" >}}
