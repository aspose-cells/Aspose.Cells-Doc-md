---
title: 在 Aspose.Cells for Node.js via C++ 中刷新数据透视表
linktitle: 在 Aspose.Cells for Node.js via C++ 中刷新数据透视表
description: 学习如何使用 v26.7+ 的数据透视刷新 API 在 Aspose.Cells for Node.js via C++ 中刷新数据透视表，本文涵盖 RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData 和 GetPivotTables，并配有实用的代码示例
keywords: Aspose.Cells, Node.js via C++, 数据透视表, 刷新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /zh/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells 提供了一个分层的刷新 API，允许您在四个不同的范围内重新加载透视数据——从整个工作簿到单个数据透视表。从 **Aspose.Cells for Node.js via C++ v26.7** 开始，旧版方法 `PivotTable.RefreshData()` 已标记为过时，应替换为本文介绍的更高效、支持缓存的 API。
{{% /alert %}}
## 概述
刷新数据透视表很少是一项单一的操作。在后台，Aspose.Cells 维护着一个分层的数据链，它将您的原始源数据连接到您在工作表中看到的呈现值。理解这条数据链是为任何场景选择正确的刷新 API 的关键。
四层数据链如下：
1. **数据源 (Data Source)** — 原始的工作表区域、数据库查询或合并区域，原始值就保存在这里。
2. **PivotCache** — 源数据的内存快照。每个数据透视表都构建在 `PivotCache` 之上；所有数据都在这里进行收集和聚合。
3. **PivotTable** — 定义行、列、值和筛选字段的视图对象。`PivotTable` 仅从其 `PivotCache` 读取数据，*不*直接从数据源读取。
4. **Cells** — 工作表中 `PivotTable` 将其计算后的值和样式渲染到的工作表 `Cells`。
一个特别重要的概念是**共享缓存 (shared cache)**。当工作簿中的多个数据透视表引用同一个源区域时，它们共享*一个* `PivotCache` 实例。单个 `PivotCache` 可以被多个数据透视表引用，刷新该缓存会同时刷新所有依赖于它的 `PivotTable`。
{{% alert color="primary" %}}
`PivotCache.SourceType`（枚举 `PivotTableSourceType`）指示缓存数据的来源。截至 v26.7，`PivotCache.Refresh()` 仅支持 **`Sheet`** 和 **`Consolidation`** 源类型，即保存在工作表区域中的数据。外部源（数据库、外部连接等）尚无法通过缓存 API 进行刷新。
{{% /alert %}}
由于这种链式结构，Aspose.Cells 中存在两条基本的刷新路径：
- **`PivotCache.Refresh()`** — 在单次操作中重新加载源 → 缓存，并重新计算所有依赖的 `PivotTable`。
- **`PivotTable.CalculateData()`** — 从已缓存的数据重新计算某个 `PivotTable` 的显示，无需回溯到数据源。
本文中所有场景均使用工作表单元格源数据，因此源类型为 `Sheet`，刷新操作的行为如上文所述。
## 所需的导入
本文中所有 JavaScript 示例均假定 Aspose.Cells for Node.js via C++ 模块已加载，并且透视类型位于 `Aspose.Cells.Pivot` 命名空间中。典型的设置如下：
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;`（或者通过 `AsposeCells.Pivot.PivotFieldType` 访问）
## 刷新工作簿中的所有数据透视表
当您需要确保工作簿中的每个透视缓存和每个数据透视表都反映最新的源数据时，最简单且最全面的 API 是 `Workbook.RefreshAll()`。单次调用即可遍历整个工作簿——从其源刷新每个 `PivotCache`，然后重新计算每个依赖的 `PivotTable`。对于一般性的完整文档刷新（对性能没有特别要求时），这是推荐的方法。
以下示例构建一个包含 Fruit/Year/Amount 源区域的工作簿，创建一个数据透视表，修改某些源值，然后使用 `RefreshAll()` 在一次调用中将所有内容更新到最新状态。
```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// 将表头行写入 A1:C1 单元格
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 将数据行写入 A2:C9 单元格(8 行水果数据,跨越 2020 和 2021 两年)
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

// 添加数据透视表:源数据区域为 "A1:C9",目标单元格为 "E3",名称为 "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// 设置数据透视表字段:Fruit 放入行字段,Year 放入列字段,Amount 放入数据字段
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 修改源数据中几个 Amount 的值以模拟数据变化
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// 刷新工作簿中的所有数据透视表/透视缓存
workbook.refreshAll();

// 保存工作簿
workbook.save("output.xlsx");
```
## 刷新单个工作表上的所有数据透视表
有时您只需要刷新位于某个特定工作表上的数据透视表——例如，当其他工作表上的透视表已知与本次刷新无关且不应被触动时。针对这种情况，Aspose.Cells 提供了 `Worksheet.RefreshPivotTables()`，其作用范围限定在单个 `Worksheet` 实例内。
这比 `Workbook.RefreshAll()` 更加有选择性：仅刷新目标工作表上的数据透视表，其他工作表上的任何数据透视表均保持不变。
以下示例填充相同的 Fruit/Year/Amount 源数据，在第一个工作表上添加一个数据透视表，修改某些源值，然后仅刷新该工作表上的数据透视表。
```javascript
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
## 刷新单个数据透视表
当您需要对单个数据透视表进行细粒度控制时，基于缓存的 API 为您提供了两种选择。两者之间的选择取决于实际发生变化的内容：底层的源数据，还是仅仅是数据透视表本身的视图/布局设置。
### 源数据已更改 — 使用 `PivotCache.Refresh()`
如果底层的源数据已发生更改，正确的入口是 `pivotTable.PivotCache.Refresh()`。此调用会重新读取源数据到缓存中，然后重新计算依赖于该缓存的每个 `PivotTable`。
{{% alert color="primary" %}}
由于数据透视表共享同一个 `PivotCache` 实例，调用 `PivotCache.Refresh()` 会重新计算基于同一缓存构建的**所有**数据透视表，而不仅仅是您所引用的那一个。如果两个数据透视表共享同一个源区域，刷新其中一个缓存会同时刷新两者。
{{% /alert %}}
以下示例在同一源区域上创建两个数据透视表以演示这种共享缓存行为，修改某些源值，然后通过一个缓存引用进行刷新。
```javascript
const AsposeCells = require("aspose.cells");

// 创建新的工作簿并访问第一个工作表
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// 写入表头行：水果 / 年份 / 数量
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 写入大约 9 行数据（葡萄 / 蓝莓 / 猕猴桃 / 樱桃，分布在 2020-2021 年）
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

// 添加第一个数据透视表 "Pivot1"，锚定在 E3 单元格，源数据区域为 A1:C9
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
// 由于 Pivot1 和 Pivot2 共享同一个 PivotCache，因此这一调用
// 会同时刷新这两个数据透视表（数据和样式）以反映更新后的源数据。
pivotTable1.getPivotCache().refresh();

// 保存工作簿
workbook.save("output.xlsx");
```
### 仅视图/布局已更改 — 使用 `CalculateData()`
如果源数据*没有*发生更改，只是数据透视表的视图或布局设置被修改（例如，一个字段被移动到了不同的区域，或者切换了“打开时刷新”设置），则无需回溯到数据源。缓存中已经保存了正确的数据；只需要重新计算呈现的 `PivotTable`。在这种情况下，`pivotTable.CalculateData()` 是正确的选择。
这样可以避免不必要的源数据获取，并且在多个数据透视表共享同一缓存时，效率提升尤为显著。
以下示例修改数据透视表的某个非源属性，然后调用 `CalculateData()` 从现有缓存重新渲染该透视表。
```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// 写入 Fruit / Year / Amount 表头行
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 写入 8 行数据（第 2-9 行，匹配源数据范围 A1:C9）
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
worksheet.getCells().get("C6").putValue(150);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(250);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(350);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(450);

// 添加一个名为 "Pivot1" 的数据透视表，放置在目标单元格 E3，源数据范围为 A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// 分配字段：Fruit 到行字段，Year 到列字段，Amount 到数据字段
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

// 修改视图/布局属性 —— 这只是展示性的更改，
// 因此不需要通过 PivotCache.Refresh() 重新读取源数据。
pivotTable.setRefreshDataOnOpeningFile(false);

// CalculateData() 会根据透视缓存中已有的数据重新渲染此透视表的显示（数据 + 样式）。
// 由于源数据未发生变化，因此不会执行与源的往返操作——只会将缓存的值重新计算到工作表单元格中。
pivotTable.calculateData();

// 将工作簿保存到磁盘
workbook.save("output.xlsx");
```
## 获取共享同一 PivotCache 的所有数据透视表
工作簿中常常包含许多数据透视表，它们都构建在一个共享缓存之上。若要枚举它们——例如，在执行批量刷新之前，或诊断共享缓存的影响——可以使用 `PivotCache.GetPivotTables()`。此方法返回依赖于该缓存的所有 `PivotTable` 的集合。
这也是确认两个数据透视表确实共享同一个 `PivotCache` 实例的最直接方式：您可以比较缓存引用，或简单地遍历 `GetPivotTables()` 返回的集合，观察其中包含哪些数据透视表。
以下示例在同一源区域上创建两个数据透视表，验证它们共享同一个缓存实例，然后枚举该缓存的数据透视表。
```javascript
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
pivotTable1.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

let pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

let sameCache = pivotTable1.getPivotCache() === pivotTable2.getPivotCache();
console.log("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

let sharedPivotTables = pivotTable1.getPivotCache().getPivotTables();
console.log("Number of pivot tables sharing the cache: " + sharedPivotTables.length);

for (let pt of sharedPivotTables) {
    console.log("Pivot table name: " + pt.getName());
}

workbook.save("output.xlsx");
```
## 从过时的 `PivotTable.RefreshData()` 迁移
在 Aspose.Cells for Node.js via C++ v26.7 之前，刷新数据透视表的标准方式是对每个数据透视表分别调用 `PivotTable.RefreshData()`。从 v26.7 起，该方法被标记为**过时**，应替换为上文介绍的缓存感知型 API。
在真实业务工作簿中，对每个表分别调用 `RefreshData()` 的方式存在两个问题：
- 它在每次调用时都会*重新*从源获取数据，即使源数据并未发生更改。
- 每次调用都会刷新整个共享缓存。当多个数据透视表共享同一个缓存时，逐个对每个数据透视表反复调用 `RefreshData()` 会导致同一个缓存被反复重新获取，速度非常慢。
推荐替换方式如下：
- **刷新工作簿中的所有数据透视表** → 使用 `workbook.refreshAll();`
- **刷新其中一部分** → 对其中一个缓存使用 `pivotTable.PivotCache.Refresh();`。由于缓存是共享的，这单次调用会更新基于该缓存构建的所有数据透视表。已经基于已刷新缓存的其他数据透视表可以安全地跳过。
- **仅透视视图/布局发生变化** → 使用 `pivotTable.CalculateData();`，从现有缓存重新渲染，无需任何源回溯。
以下示例演示了针对多个数据透视表共享单个缓存的工作簿的新型高效模式。
```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- 构建源数据：水果 / 年份 / 金额（表头 + 9 行数据） ---
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

// --- 在目标单元格 E3 处添加第一个数据透视表（Pivot1） ---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- 在同一个源数据范围内添加第二个数据透视表（Pivot2） ---
// Pivot1 和 Pivot2 共用一个底层的 PivotCache（透视缓存）。
// 这正是一个典型的场景：在这种场景下，旧版的逐表调用 RefreshData()
// 方法效率很低：刷新一个表会重新拉取整个共享缓存，
// 因此刷新 N 个表就需要重复 N 次这种昂贵的拉取操作。
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- 修改源数据中的几个金额值 ---
sheet.getCells().get("C2").putValue(5000);   // 葡萄 2020
sheet.getCells().get("C5").putValue(7500);   // 樱桃 2020
sheet.getCells().get("C9").putValue(9500);   // 樱桃 2021

// --- 已废弃的模式（26.7 版本之前）— PivotTable.RefreshData() ---
// pivotTable1.RefreshData();  // 从源数据重新拉取，刷新整个缓存
// pivotTable2.RefreshData();  // 再次重新拉取 —— 但缓存此时已经是新的了！
// 每次调用都会重建共享缓存，因此 N 个表 = N 次冗余拉取。

// --- v26.7+ 新模式：只需刷新一次缓存，然后按需重新渲染 ---
// 只需调用一次 PivotCache.Refresh() 即可将修改后的值拉取到共享缓存中，
// 同时重新计算所有引用该缓存的数据透视表的显示。
// 因为 Pivot1 和 Pivot2 共享同一个 PivotCache，所以这一次调用就能更新
// 两个表 —— 无需再次访问源数据。
pivotTable1.getPivotCache().refresh();

// CalculateData() 仅重新渲染数据透视表的显示（数据和样式），
// 它使用的是缓存中已有的数据 —— 并不会访问源数据。
// 此处对 Pivot2 调用该方法纯粹是为了演示该 API：在缓存被刷新一次之后，
// 任何依赖该缓存的表都可以被重新渲染，而无需
// 再次访问源数据。当仅有透视表的视图/布局设置发生变化、且缓存为最新时，
// 可以单独使用 CalculateData() 方法。
pivotTable2.calculateData();

workbook.save("output.xlsx");
```
## 应该使用哪个刷新 API？
下表汇总了可用的刷新 API 及其适用场景。
| 目标 | 推荐 API | 备注 |
|------|-----------------|-------|
| 刷新工作簿中的所有内容 | `Workbook.RefreshAll()` | 一次调用，覆盖所有缓存和表格。 |
| 仅刷新单个工作表上的数据透视表 | `Worksheet.RefreshPivotTables()` | 作用范围限定为一个工作表。 |
| 一个缓存的源数据已更改 | `pivotTable.PivotCache.Refresh()` | 刷新该共享缓存上的**所有**数据透视表。 |
| 仅视图/布局设置发生更改 | `pivotTable.CalculateData()` | 跳过不必要的源回溯。 |
| 列出共享缓存上的所有数据透视表 | `pivotCache.GetPivotTables()` | 用于在批量刷新之前枚举。 |
在实际使用中，应优先选择基于缓存的 API，而非过时的逐表 `RefreshData()`。它们能够感知共享缓存，可避免冗余的源获取，并允许您选择满足刷新需求的最小作用范围。
## 相关文章
- [向单元格中插入图片](/cells/zh/nodejs-cpp/inserting-an-image-into-a-cell/)
- [读写 DBF 文件](/cells/zh/nodejs-cpp/dbf/)
- [将 Excel 文件拆分为多个文件](/cells/zh/nodejs-cpp/splitting-excel-files-into-multiple-files/)
- [Aspose.Cells for Node.js via C++ 中的迷你图（Sparkline）](/cells/zh/nodejs-cpp/sparkline/)
{{< app/cells/assistant language="javascript" >}}