---
title: 在 Aspose.Cells for .NET 中向数据透视表添加筛选字段
linktitle: 添加筛选字段
description: 学习如何使用 Aspose.Cells for Node.js via Java 在数据透视表中添加和配置筛选字段，包括添加筛选字段、单选过滤和多选过滤。
keywords: Aspose.Cells, Node.js via Java, 数据透视表, 筛选字段, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, 过滤
type: docs
weight: 250
url: /zh/nodejs-java/add-filter-field-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持数据透视表中筛选字段的完整生命周期。您可以通过高级便捷 API 或通过低级别的 `PageFields` 集合来添加筛选字段，并且可以以单选模式驱动页面过滤器、清除它以显示每个筛选项，或者将字段切换为多选模式，以便用户能够通过 Excel 中的复选框 UI 一次选择多个筛选项。
{{% /alert %}}

## **介绍**

筛选字段是一种数据透视字段，它控制数据透视表主体显示源数据的*哪个子集*。最终用户在 Excel 中将其视为已渲染数据透视表顶部的下拉列表，选择可用的筛选项之一后，数据透视表主体会重新构建，以便仅汇总属于该筛选项的记录。当数据透视字段注册为 `PivotFieldType.Page` 而非 `PivotFieldType.Row`、`PivotFieldType.Column` 或 `PivotFieldType.Data` 时，它就成为筛选字段。

筛选字段可以以两种行为运行。在默认的**单选**行为下，一次仅显示一个筛选项，因此数据透视表主体仅汇总一个子集。在**多选**行为下，该字段显示一个复选框列表，数据透视表主体汇总所有已勾选筛选项的并集。通过切换单个属性，相同的源字段可以在这些行为之间来回切换。

Aspose.Cells for Node.js via Java 提供了两种等效的方式来注册筛选字段。高级 API 是 `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")`，它接受源列名并在单次调用中添加该字段。低级 API 是 `pivotTable.getPageFields().add(PivotField)`，当您已经持有 `PivotField` 引用并希望将同一字段实例添加到筛选区域时使用。这两个 API 最终都会填充相同的 `PageFields` 集合，本文的其余部分将演示如何在这两者之间进行选择以及如何驱动每种过滤模式。

## **添加筛选字段**

有两种方法可以在筛选区域中注册数据透视字段。高级调用接受源列名称作为字符串，是最常用的路径。低级调用接受现有的 `PivotField` 实例，当必须在多个数据透视区域中重用同一字段对象时非常方便。这两个调用都会将字段放入 `pivotTable.getPageFields()`，之后该字段将作为已渲染数据透视表顶部的页面下拉列表显示。

### 使用 addFieldToArea 添加筛选字段

以下示例构建一个小的 Fruit / Year / Amount 数据集，在 E3 单元格处放置一个数据透视表，其中 `Fruit` 位于行区域，`Amount` 位于数据区域，`Year` 位于筛选区域，刷新数据透视表并保存工作簿。

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// 设置表头行
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 填充 9 行示例数据：Fruit、Year、Amount
var data = [
    [ "apple", 2020, 100 ],
    [ "banana", 2021, 200 ],
    [ "apple", 2021, 150 ],
    [ "grape", 2020, 120 ],
    [ "orange", 2022, 180 ],
    [ "banana", 2020, 90 ],
    [ "grape", 2021, 130 ],
    [ "apple", 2022, 170 ],
    [ "orange", 2021, 110 ]
];

for (var i = 0; i < data.length; i++)
{
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0]);
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1]);
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2]);
}

// 在单元格 E3 处添加数据透视表
var pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// 将字段添加到相应区域：Fruit 作为行字段，Amount 作为数据字段，Year 作为页字段
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// 刷新并计算数据透视表数据
pivotTable.calculateData();

// 保存工作簿
workbook.save("pageFieldSample.xlsx");
```

### 使用 getPageFields().add 添加筛选字段

当您已经使用 `PivotField` 实例时，可以将其直接传递给 `pivotTable.getPageFields().add`。数据透视表和筛选字段的构造方式与前面的场景完全相同；仅最终的筛选区域注册被替换为低级 API 调用。

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// 表头
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

// 示例数据（9行）
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);

// 在E3位置添加数据透视表，覆盖A1:C10
let pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// 水果 -> 行，金额 -> 数据（年份将放在下面的页面区域）
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 底层方法：从BaseFields中获取现有的年份透视字段
// 并通过PageFields.Add(PivotField)将其注册到页面区域
let yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// 刷新数据，使新的页面字段在保存的工作簿中生效
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **单选过滤（显示一个筛选项）**

在默认的单选行为下，筛选字段呈现为单个下拉列表，`PivotField.CurrentPageItem` 整数选择哪个筛选项驱动数据透视表主体。分配特定索引会选取该单项；分配特殊哨兵值 `0x7FFD`（十进制 32765）会清除过滤器，从而一次性汇总每个筛选项。单选是默认行为；您无需显式启用它。

### 显示所有项

将 `CurrentPageItem` 设置为魔术值 `0x7FFD` 等同于清除页面过滤器，数据透视表主体将汇总每个筛选项，就好像没有应用过滤器一样。

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);

// 填充 Fruit/Year/Amount 数据
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

var data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
];

for (var r = 0; r < data.length; r++) {
    for (var c = 0; c < data[r].length; c++) {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// 在 E3 创建数据透视表
var pivotTables = sheet.getPivotTables();
var index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
var pivotTable = pivotTables.get(index);

// 配置透视字段：Fruit→行，Amount→数据，Year→页
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

pivotTable.calculateData();

// 清除页面筛选，以便页面字段中的每个项都可见。
// 0x7FFD（十进制 32765）是表示"所有项"的特殊哨兵值 —
// 相当于在 Excel 的页面字段下拉列表中选择"(全部)"。
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD);

workbook.save("output.xlsx");
```

### 显示一个特定项

将 `CurrentPageItem` 设置为实际索引会仅选取该单个筛选项。该索引是项目在筛选字段排序项列表中的位置，因此例如 `1` 选择排序后的第二项。

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// 添加示例数据（水果/年份/金额）
cells.get("A1").setValue("Fruit");
cells.get("B1").setValue("Year");
cells.get("C1").setValue("Amount");

cells.get("A2").setValue("Apple");
cells.get("B2").setValue("2020");
cells.get("C2").setValue("100");

cells.get("A3").setValue("Apple");
cells.get("B3").setValue("2021");
cells.get("C3").setValue("150");

cells.get("A4").setValue("Banana");
cells.get("B4").setValue("2020");
cells.get("C4").setValue("200");

cells.get("A5").setValue("Banana");
cells.get("B5").setValue("2021");
cells.get("C5").setValue("250");

// 在 E3 处添加数据透视表
var pivotTables = sheet.getPivotTables();
var pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables.get(pivotIndex);

// 添加字段：水果→行，金额→数据，年份→页
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// 页字段特定操作
pivotTable.getPageFields().get(0).setCurrentPageItem(1); // 1 = 排序顺序中的第二项（例如"2021"）

// 刷新并计算数据透视表
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **多选过滤**

多选过滤将页面下拉列表转换为复选框列表，并允许最终用户同时选择多个筛选项。Aspose.Cells 公开了两个协同工作的属性。必须先将 `PivotField.IsMultipleItemSelectionAllowed` 设置为 `true`，多选 UI 才会生效。启用后，`PivotItem.IsHidden` 控制哪些项出现在复选框列表中，因此您可以显示每个项或仅将特定项加入白名单。

以下代码在场景 1a 中构建的同一 Year 筛选字段上启用多选，然后展示两种模式：Part A 通过将每个条目的 `IsHidden` 设置为 `false` 来显示每个筛选项，而 Part B 通过 `switch (pivotItems[i].getStringValue())` 块仅将您选择的源值加入白名单并隐藏其他所有项。

```javascript
const AsposeCells = require("aspose.cells");

// — 数据透视表和页面字段的构建与场景 1a 完全相同
//   （水果/年份/金额数据，数据透视表位于 E3，水果→行，
//   金额→数据，年份→通过 AddFieldToArea 设置为页面字段）。
//   下面我们在页面字段上应用多选过滤。

const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().get(0);
const cells = sheet.getCells();

// 示例数据：水果 | 年份 | 金额
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");

const data = [
    ["apple",  "2019", "100"],
    ["apple",  "2020", "150"],
    ["apple",  "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape",  "2019", "120"],
    ["grape",  "2020", "170"],
    ["grape",  "2021", "220"]
];

for (let i = 0; i < data.length; i++) {
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(parseInt(data[i][2]));
}

const pivotSheet = workbook.getWorksheets().add("Pivot");
const pivots = pivotSheet.getPivotTables();
const pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
const pivotTable = pivots.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, "Year");

// — 在页面字段上启用多选
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);

// 部分 A — 选择所有项目（使每个项目可见）
const pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (let i = 0; i < pivotItems.getCount(); i++) {
    pivotItems.get(i).setHidden(false);
}

// 部分 B — 仅按源值选择特定项目
for (let i = 0; i < pivotItems.getCount(); i++) {
    switch (pivotItems.get(i).getStringValue()) {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setHidden(false);
            break;
        default:
            pivotItems.get(i).setHidden(true);
            break;
    }
}

pivotTable.calculateData();

workbook.save("output.xlsx");
```

> **注意：** 通过 `PivotItem.IsHidden` 使用多选过滤时，**必须至少保留一个 `PivotItem` 可见**（`IsHidden == false`）。如果每个项都被隐藏，Excel 在打开文件时会崩溃或呈现空白的数据透视表。始终验证您的多选白名单至少包含源数据中的一项。

## **应该使用哪个 API 和哪种模式？**

下表总结了何时使用每个 API 和模式，以便您无需详细阅读每个场景即可选择正确的组合。

| 场景 / 用例 | 推荐 API | 使用的属性 | 备注 |
|---|---|---|---|
| 按源列名添加筛选字段（最常见） | `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | 高级单行 API。除非需要 `PivotField` 引用，否则请使用此方法。 |
| 在已拥有 `PivotField` 对象时添加筛选字段 | `pivotTable.getPageFields().add(PivotField)` | n/a | 当字段对象是从其他位置获取或需要重用时使用。 |
| 过滤到单个筛选项（默认模式） | `PivotField.CurrentPageItem` | 设置为特定索引 | 例如，`1` 显示排序列表中的第二项。 |
| 显示所有项 / 清除页面过滤器 | `PivotField.CurrentPageItem` | 设置为 `0x7FFD` | 魔术值 `0x7FFD`（十进制 32765）是 "所有项" 的哨兵值。 |
| 在 Excel 中启用多选 UI | `PivotField.IsMultipleItemSelectionAllowed` | 设置为 `true` | 在任何 `IsHidden` 调用生效之前必需。 |
| 在多选列表中隐藏 / 显示各个项 | `PivotItem.IsHidden` | 按项设置 | 至少必须保留一项可见（`IsHidden == false`）。 |

{{% alert color="primary" %}}
配置多选过滤时，请始终记住可见性约束。如果多选筛选字段中的每个 `PivotItem` 都被隐藏，Excel 在打开时崩溃或呈现空白的数据透视表。根据源数据构建您的白名单，使至少一项保持可见，这样您保存的工作簿将在每台机器上可靠地打开。
{{% /alert %}}


{{< app/cells/assistant language="javascript" >}}
