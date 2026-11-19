---
title: 在 Aspose.Cells for Node.js via C++ 中向数据透视表添加筛选字段
description: 学习如何使用 Aspose.Cells for Node.js via C++ 在数据透视表中添加和配置筛选字段，包括添加筛选字段、单选筛选以及多选筛选。
linktitle: 添加筛选字段
keywords: Aspose.Cells, Node.js via C++, 数据透视表, 筛选字段, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, 筛选
type: docs
weight: 250
url: /zh/nodejs-cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持数据透视表中筛选字段的完整生命周期。您可以通过高级便捷 API 或底层的 `PageFields` 集合来添加筛选字段，并且可以以单选模式驱动筛选器、清除筛选器以显示所有筛选项，或者将该字段切换到多选模式，以便用户能够通过 Excel 中的复选框 UI 同时选择多个筛选项。
{{% /alert %}}

## **简介**
筛选字段是一种数据透视字段，用于控制数据透视表主体所显示的源数据的哪个子集。终端用户在 Excel 中看到的是渲染后数据透视表顶部的一个下拉列表，从可用的筛选项中选择一个后，数据透视表主体会重新构建，使得仅属于该筛选项的记录被汇总。当某个数据透视字段被注册为 `PivotFieldType.Page`（而不是 `PivotFieldType.Row`、`PivotFieldType.Column` 或 `PivotFieldType.Data`）时，它就成为一个筛选字段。
筛选字段可以以两种行为方式运行。在默认的 **单选** 行为下，每次仅可见一个筛选项，因此数据透视表主体恰好汇总一个子集。在 **多选** 行为下，该字段会显示一个复选框列表，数据透视表主体会汇总所有勾选的筛选项的并集。同一源字段可以通过切换单个属性在这两种行为之间来回切换。
Aspose.Cells for Node.js via C++ 提供了两种等效的方式来注册筛选字段。高级 API 是 `PivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")`，它接受源列名称并通过一次调用添加该字段。底层 API 是 `PivotTable.pageFields.add(PivotField)`，它用于当您已经持有 `PivotField` 引用并希望将同一字段实例添加到筛选区域时使用。这两个 API 最终都会填充同一个 `PageFields` 集合，本文的其余部分将演示如何在它们之间进行选择以及如何驱动每种筛选模式。

## **添加筛选字段**
在筛选区域中注册数据透视字段有两种方式。高级调用接受源列名称作为字符串，是最常用的路径。底层调用接受一个已存在的 `PivotField` 实例，当同一字段对象必须跨多个数据透视区域重用时非常方便。两种调用都会将字段放入 `PivotTable.pageFields` 中，此后该字段便会作为渲染后数据透视表顶部的页面下拉列表出现。

### 使用 addFieldToArea 添加筛选字段
以下示例构建一个小的 Fruit / Year / Amount 数据集，在 E3 单元格处放置一个数据透视表，其中 `Fruit` 放在行区域，`Amount` 放在数据区域，`Year` 放在筛选区域，刷新数据透视表，然后保存工作簿。

```javascript
const AsposeCells = require("aspose.cells.node");
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
// Set up the header row
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Populate 9 rows of sample data: Fruit, Year, Amount
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
// Add a pivot table anchored at cell E3
var pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Add fields to their areas: Fruit as Row, Amount as Data, Year as Page field
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
// Refresh and calculate the pivot table data
pivotTable.calculateData();
// Save the workbook
workbook.save("pageFieldSample.xlsx");
```

### 使用 pageFields.add 添加筛选字段
当您已经在使用一个 `PivotField` 实例时，可以直接将其传递给 `PivotTable.pageFields.add`。数据透视表和筛选字段的构建方式与上一场景完全相同；只是最终的筛选区域注册被替换为底层 API 调用。

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
// Headers
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");
// Sample data (9 rows)
sheet.getCells().get("A2").putValue("apple");     sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");     sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");     sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");     sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");     sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");     sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);
// Add pivot table at E3 covering A1:C10
let pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4);
// Fruit -> Row, Amount -> Data (Year will go to Page below)
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Low-level approach: grab the existing Year PivotField from BaseFields
// and register it in the Page area via PageFields.Add(PivotField).
let yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);
// Refresh so the new page field is reflected in the saved workbook
pivotTable.calculateData();
workbook.save("output.xlsx");
```

## **单选筛选（显示一个筛选项）**
在默认的单选行为下，筛选字段呈现为单个下拉列表，`PivotField.currentPageItem` 整数用于选择哪个筛选项驱动数据透视表主体。赋一个具体的索引值会选中该单项；赋一个特殊的哨兵值 `0x7FFD`（十进制 32765）则会清除筛选器，从而一次性汇总所有筛选项。单选是默认行为，您无需显式启用。

### 显示所有项
将 `currentPageItem` 设置为特殊值 `0x7FFD` 等同于清除筛选器：数据透视表主体会汇总所有筛选项，就像没有应用筛选器一样。

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
// Populate Fruit/Year/Amount data
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");
let data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
];
for (let r = 0; r < data.length; r++) {
    for (let c = 0; c < data[r].length; c++) {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}
// Create pivot table at E3
let pivotTables = sheet.getPivotTables();
let pivotTable = pivotTables.add("=A1:C7", 2, 4);
// Configure pivot fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
pivotTable.calculateData();
// Clear the page filter so every item in the page field is visible.
// 0x7FFD (decimal 32765) is the special sentinel value that means "all items" —
// equivalent to selecting "(All)" in Excel's page-field dropdown.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD);
workbook.save("output.xlsx");
```

### 显示一个特定项
将 `currentPageItem` 设置为实际索引值即可选中那一个筛选项。该索引是筛选字段已排序项列表中的位置，因此例如 `1` 会在排序后选中第二项。

```javascript
const AsposeCells = require("aspose.cells.node");
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();
// Add sample data (Fruit/Year/Amount)
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
cells.get("A2").putValue("Apple");
cells.get("B2").putValue("2020");
cells.get("C2").putValue("100");
cells.get("A3").putValue("Apple");
cells.get("B3").putValue("2021");
cells.get("C3").putValue("150");
cells.get("A4").putValue("Banana");
cells.get("B4").putValue("2020");
cells.get("C4").putValue("200");
cells.get("A5").putValue("Banana");
cells.get("B5").putValue("2021");
cells.get("C5").putValue("250");
// Add pivot table at E3
var pivotTables = sheet.getPivotTables();
var pivotTable = pivotTables.add("A1:C5", 2, 4);
// Add fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
// Page-field-specific operations
pivotTable.getPageFields().get(0).setCurrentPageItem(1); // 1 = second item in sorted order (e.g. "2021")
// Refresh and calculate pivot table
pivotTable.calculateData();
workbook.save("output.xlsx");
```

## **多选筛选**
多选筛选将页面下拉列表转换为复选框列表，并允许终端用户同时选择多个筛选项。Aspose.Cells 公开了两个协同工作的属性。必须先将 `PivotField.isMultipleItemSelectionAllowed` 设置为 `true`，多选 UI 才会生效。启用之后，`PivotItem.isHidden` 控制哪些项出现在复选框列表中，因此您可以显示所有项，也可以仅白名单显示特定项。
下面的代码在场景 1a 中构建的同一 Year 筛选字段上启用多选，然后展示两种模式：A 部分通过对每个项保留 `isHidden` 为 `false` 来显示所有筛选项，而 B 部分通过 `switch (pivotItems[i].getStringValue())` 块仅白名单您选择的源值并隐藏其他所有项。

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
let cells = sheet.getCells();
// Sample data: Fruit | Year | Amount
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");
let data = [
    ["apple", "2019", "100"],
    ["apple", "2020", "150"],
    ["apple", "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape", "2019", "120"],
    ["grape", "2020", "170"],
    ["grape", "2021", "220"]
];
for (let i = 0; i < data.length; i++) {
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(parseInt(data[i][2]));
}
let pivotSheet = workbook.getWorksheets().add("Pivot");
let pivots = pivotSheet.getPivotTables();
let pivotTable = pivots.add("A1:C10", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
// — Enable multi-select on the page field
pivotTable.getPageFields().get(0).setIsMultipleItemSelectionAllowed(true);
// Part A — select ALL items (make every item visible)
let pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (let i = 0; i < pivotItems.getCount(); i++) {
    pivotItems.get(i).setIsHidden(false);
}
// Part B — select only specific items by source value
for (let i = 0; i < pivotItems.getCount(); i++) {
    switch (pivotItems.get(i).getStringValue()) {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setIsHidden(false);
            break;
        default:
            pivotItems.get(i).setIsHidden(true);
            break;
    }
}
pivotTable.calculateData();
workbook.save("output.xlsx");
```

> **注意：** 当通过 `PivotItem.isHidden` 使用多选筛选时，**必须至少有一个 `PivotItem` 保持可见**（`isHidden == false`）。如果所有项都被隐藏，Excel 在打开文件时要么崩溃，要么渲染一个空白的数据透视表。请始终确认您的多选白名单至少包含源数据中的一个项。

## **应该使用哪个 API 和哪种模式？**
下表汇总了在每种场景下应使用哪个 API 和哪种模式，使您无需阅读每个场景的细节即可选择正确的组合。
| 场景 / 用例 | 推荐的 API | 使用的属性 | 备注 |
|---|---|---|---|
| 按源列名称添加筛选字段（最常用） | `PivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | 高级、一行代码。除非需要 `PivotField` 引用，否则请使用此方式。 |
| 当您已经拥有 `PivotField` 对象时添加筛选字段 | `PivotTable.pageFields.add(PivotField)` | n/a | 在字段对象是从其他位置获得或需要重用时使用。 |
| 筛选到单个筛选项（默认模式） | `PivotField.currentPageItem` | 设置为具体索引 | 例如，`1` 显示已排序列表中的第二项。 |
| 显示所有项 / 清除筛选器 | `PivotField.currentPageItem` | 设置为 `0x7FFD` | 特殊值 `0x7FFD`（十进制 32765）是“所有项”的哨兵值。 |
| 在 Excel 中启用多选 UI | `PivotField.isMultipleItemSelectionAllowed` | 设置为 `true` | 在任何 `isHidden` 调用生效之前必须设置。 |
| 在多选列表中隐藏 / 显示各个项 | `PivotItem.isHidden` | 按项设置 | 至少必须有一个项保持可见（`isHidden == false`）。 |

{{% alert color="primary" %}}
在配置多选筛选时，请始终牢记可见性约束。如果多选筛选字段中的每个 `PivotItem` 都被隐藏，Excel 在打开时会崩溃或渲染空白的数据透视表。请根据源数据构建白名单，以确保至少有一个项保持可见，这样您保存的工作簿将在每台机器上可靠地打开。
{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}