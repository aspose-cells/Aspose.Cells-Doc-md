---
title: 在 Aspose.Cells for .NET 中向数据透视表添加筛选字段
linktitle: 添加筛选字段
description: 学习如何使用 Aspose.Cells for .NET 在数据透视表中添加和配置筛选字段，包括添加筛选字段、单选过滤和多选过滤。
keywords: Aspose.Cells, .NET, 数据透视表, 筛选字段, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, 过滤
type: docs
weight: 250
url: /zh/net/add-filter-field-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持数据透视表中筛选字段的完整生命周期。您可以通过高级便捷 API 或较低级别的 `PageFields` 集合添加筛选字段，并且可以以单选模式驱动筛选器、清除筛选器以显示所有筛选项，或者将该字段切换为多选模式，以便用户通过 Excel 中的复选框 UI 一次选择多个筛选项。
{{% /alert %}}

## **介绍**

筛选字段是一种数据透视字段，它控制 *哪些子集* 的源数据会显示在数据透视主体中。最终用户在 Excel 中看到的是渲染后数据透视表顶部的下拉框，从可用的筛选项中选择一个后，数据透视主体会重新构建，仅汇总属于该筛选项的记录。当数据透视字段被注册为 `PivotFieldType.Page` 而不是 `PivotFieldType.Row`、`PivotFieldType.Column` 或 `PivotFieldType.Data` 时，它就成为筛选字段。

筛选字段可以采用两种行为方式运行。在默认的 **单选** 行为下，一次只能显示一个筛选项，因此数据透视主体恰好汇总一个子集。在 **多选** 行为下，该字段会显示一个复选框列表，数据透视主体汇总所有勾选的筛选项的并集。同一源字段可以通过切换单个属性在这两种行为之间来回移动。

Aspose.Cells for .NET 提供了两种等效的方式来注册筛选字段。高级 API 是 `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")`，它接受源列名并通过一次调用添加字段。较低级别的 API 是 `PivotTable.PageFields.Add(PivotField)`，当您已经持有 `PivotField` 引用并希望将同一字段实例添加到筛选区域时使用。这两种 API 最终都会填充相同的 `PageFields` 集合，本文的其余部分将演示如何在它们之间进行选择以及如何驱动每种过滤模式。

## **添加筛选字段**

在筛选区域中注册数据透视字段有两种方法。高级调用接受源列名作为字符串，是最常用的路径。较低级别的调用接受现有的 `PivotField` 实例，当同一字段对象必须在多个数据透视区域中复用时非常方便。两种调用都会将字段放入 `PivotTable.PageFields`，之后它会作为页面下拉框显示在已渲染数据透视的顶部。

### 使用 AddFieldToArea 添加筛选字段

以下示例构建一个小的 Fruit / Year / Amount 数据集，在单元格 E3 处放置一个数据透视表，其中 `Fruit` 位于行区域，`Amount` 位于数据区域，`Year` 位于筛选区域，刷新数据透视表并保存工作簿。

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// 创建一个新的工作簿
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

// 设置表头行
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// 填充 9 行示例数据：水果、年份、数量
object[,] data = new object[,]
{
    { "apple", 2020, 100 },
    { "banana", 2021, 200 },
    { "apple", 2021, 150 },
    { "grape", 2020, 120 },
    { "orange", 2022, 180 },
    { "banana", 2020, 90 },
    { "grape", 2021, 130 },
    { "apple", 2022, 170 },
    { "orange", 2021, 110 }
};

for (int i = 0; i < data.GetLength(0); i++)
{
    worksheet.Cells[i + 1, 0].PutValue(data[i, 0]);
    worksheet.Cells[i + 1, 1].PutValue(data[i, 1]);
    worksheet.Cells[i + 1, 2].PutValue(data[i, 2]);
}

// 在单元格 E3 处添加数据透视表
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// 将字段添加到相应区域：水果作为行，数量作为数据，年份作为页字段
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// 刷新并计算数据透视表数据
pivotTable.RefreshData();
pivotTable.CalculateData();

// 保存工作簿
workbook.Save("pageFieldSample.xlsx");
```

### 使用 PageFields.Add 添加筛选字段

当您已经处理 `PivotField` 实例时，可以将其直接传递给 `PivotTable.PageFields.Add`。数据透视表和筛选字段的构建方式与前面的场景完全相同；只是最后的筛选区域注册被替换为较低级别的 API 调用。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// — 透视表和页面字段的构建方式与场景 1a 完全相同
//   （Fruit/Year/Amount 数据，透视表位于 E3，Fruit→行，
//   Amount→数据）。下面我们从 BaseFields 集合中
//   获取 Year PivotField，并将其传递给 PageFields.Add —
//   这是 AddFieldToArea 的低级替代方案。其结果
//   在功能上与场景 1a 相同。

Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// 表头
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");

// 示例数据（9 行）
sheet.Cells["A2"].PutValue("apple");    sheet.Cells["B2"].PutValue("2020"); sheet.Cells["C2"].PutValue(100);
sheet.Cells["A3"].PutValue("apple");    sheet.Cells["B3"].PutValue("2021"); sheet.Cells["C3"].PutValue(150);
sheet.Cells["A4"].PutValue("apple");    sheet.Cells["B4"].PutValue("2022"); sheet.Cells["C4"].PutValue(200);
sheet.Cells["A5"].PutValue("grape");    sheet.Cells["B5"].PutValue("2020"); sheet.Cells["C5"].PutValue(300);
sheet.Cells["A6"].PutValue("grape");    sheet.Cells["B6"].PutValue("2021"); sheet.Cells["C6"].PutValue(400);
sheet.Cells["A7"].PutValue("grape");    sheet.Cells["B7"].PutValue("2022"); sheet.Cells["C7"].PutValue(500);
sheet.Cells["A8"].PutValue("blueberry"); sheet.Cells["B8"].PutValue("2020"); sheet.Cells["C8"].PutValue(250);
sheet.Cells["A9"].PutValue("blueberry"); sheet.Cells["B9"].PutValue("2021"); sheet.Cells["C9"].PutValue(350);
sheet.Cells["A10"].PutValue("blueberry");sheet.Cells["B10"].PutValue("2022"); sheet.Cells["C10"].PutValue(450);

// 在 E3 处添加透视表，覆盖 A1:C10
int pivotIndex = sheet.PivotTables.Add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];

// Fruit → 行，Amount → 数据（Year 将进入下面的 Page 区域）
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// 底层方法：从 BaseFields 中获取现有的 Year PivotField，
// 并通过 PageFields.Add(PivotField) 将其注册到 Page 区域。
PivotField yearField = pivotTable.BaseFields["Year"];
pivotTable.PageFields.Add(yearField);

// 刷新以使新的页面字段反映在保存的工作簿中
pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

## **单选过滤（显示一个筛选项）**

在默认的单选行为下，筛选字段呈现为单个下拉框，`PivotField.CurrentPageItem` 整数选择哪个筛选项驱动数据透视主体。分配特定索引会选择该单项；分配特殊哨兵值 `0x7FFD`（十进制 32765）会清除筛选器，从而一次性汇总所有筛选项。单选是默认行为，您无需显式启用它。

### 显示所有项

将 `CurrentPageItem` 设置为魔术值 `0x7FFD` 等同于清除筛选器：数据透视主体会汇总所有筛选项，就像未应用任何筛选器一样。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

class Program
{
    static void Main()
    {
        // 创建一个新的工作簿
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];

        // 填充 Fruit/Year/Amount 数据
        sheet.Cells["A1"].PutValue("Fruit");
        sheet.Cells["B1"].PutValue("Year");
        sheet.Cells["C1"].PutValue("Amount");

        object[,] data = new object[,]
        {
            {"Apple", 2022, 100},
            {"Apple", 2023, 150},
            {"Banana", 2022, 80},
            {"Banana", 2023, 120},
            {"Cherry", 2022, 200},
            {"Cherry", 2023, 250}
        };

        for (int r = 0; r < data.GetLength(0); r++)
        {
            for (int c = 0; c < data.GetLength(1); c++)
            {
                sheet.Cells[r + 1, c].PutValue(data[r, c]);
            }
        }

        // 在 E3 创建数据透视表
        var pivotTables = sheet.PivotTables;
        int index = pivotTables.Add("=A1:C7", "E3", "PivotTable1");
        PivotTable pivotTable = pivotTables[index];

        // 配置数据透视字段:Fruit→行,Amount→数据,Year→页
        pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
        pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
        pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

        pivotTable.RefreshData();
        pivotTable.CalculateData();

        // 清除页面筛选器,以便页面字段中的每个项都可见。
        // 0x7FFD(十进制 32765)是表示"所有项"的特殊哨兵值 —
        // 相当于在 Excel 的页字段下拉菜单中选择"(全部)"。
        pivotTable.PageFields[0].CurrentPageItem = 0x7FFD;

        workbook.Save("output.xlsx");
    }
}
```

### 显示一个特定项

将 `CurrentPageItem` 设置为真实索引将仅选择该单个筛选项。该索引是筛选字段排序项列表中项的位置，因此例如 `1` 选择排序后的第二个项。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// 创建工作簿
var workbook = new Workbook();
var sheet = workbook.Worksheets[0];
var cells = sheet.Cells;

// 添加示例数据（水果/年份/金额）
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");

cells["A2"].PutValue("Apple");
cells["B2"].PutValue("2020");
cells["C2"].PutValue("100");

cells["A3"].PutValue("Apple");
cells["B3"].PutValue("2021");
cells["C3"].PutValue("150");

cells["A4"].PutValue("Banana");
cells["B4"].PutValue("2020");
cells["C4"].PutValue("200");

cells["A5"].PutValue("Banana");
cells["B5"].PutValue("2021");
cells["C5"].PutValue("250");

// 在 E3 处添加数据透视表
var pivotTables = sheet.PivotTables;
int pivotIndex = pivotTables.Add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables[pivotIndex];

// 添加字段：水果→行，金额→数据，年份→页
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// 页字段特定操作
pivotTable.PageFields[0].CurrentPageItem = 1; // 1 = 排序顺序中的第二个项目（例如"2021"）

// 刷新并计算数据透视表
pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

## **多选过滤**

多选过滤将页面下拉框转换为复选框列表，并允许最终用户同时选择多个筛选项。Aspose.Cells 公开了两个协同工作的属性。必须先将 `PivotField.IsMultipleItemSelectionAllowed` 设置为 `true`，多选 UI 才会生效。启用后，`PivotItem.IsHidden` 控制哪些项显示在复选框列表中，因此您可以显示所有项或仅将特定项加入白名单。

下面的代码在场景 1a 中构建的同一 Year 筛选字段上启用多选，然后展示两种模式：A 部分通过对每个条目将 `IsHidden` 设置为 `false` 来显示所有筛选项，而 B 部分通过 `switch (pivotItems[i].GetStringValue())` 块将您选择的源值加入白名单并隐藏所有其他项。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// — 透视表和页面字段的构建方式与场景 1a 完全相同
//   （Fruit/Year/Amount 数据，透视表位于 E3，Fruit→行，
//   Amount→数据，Year→页面（通过 AddFieldToArea））。
//   下面我们对页面字段应用多选筛选。

Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;

// 示例数据：Fruit | Year | Amount
cells[0, 0].PutValue("Fruit");
cells[0, 1].PutValue("Year");
cells[0, 2].PutValue("Amount");

string[,] data = new string[,]
{
    { "apple",  "2019", "100" },
    { "apple",  "2020", "150" },
    { "apple",  "2021", "200" },
    { "banana", "2019", "110" },
    { "banana", "2020", "160" },
    { "banana", "2021", "210" },
    { "grape",  "2019", "120" },
    { "grape",  "2020", "170" },
    { "grape",  "2021", "220" }
};

for (int i = 0; i < data.GetLength(0); i++)
{
    cells[i + 1, 0].PutValue(data[i, 0]);
    cells[i + 1, 1].PutValue(Convert.ToInt32(data[i, 1]));
    cells[i + 1, 2].PutValue(Convert.ToInt32(data[i, 2]));
}

Worksheet pivotSheet = workbook.Worksheets.Add("Pivot");
PivotTableCollection pivots = pivotSheet.PivotTables;
int pivotIndex = pivots.Add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = pivots[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// — 在页面字段上启用多选
pivotTable.PageFields[0].IsMultipleItemSelectionAllowed = true;

// A 部分 — 选择所有项（使每个项都可见）
PivotItemCollection pivotItems = pivotTable.PageFields[0].PivotItems;
for (int i = 0; i < pivotItems.Count; i++)
{
    pivotItems[i].IsHidden = false;
}

// B 部分 — 仅按源值选择特定的项
for (int i = 0; i < pivotItems.Count; i++)
{
    switch (pivotItems[i].GetStringValue())
    {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems[i].IsHidden = false;
            break;
        default:
            pivotItems[i].IsHidden = true;
            break;
    }
}

pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

> **注意：** 当通过 `PivotItem.IsHidden` 使用多选过滤时，**必须至少保留一个 `PivotItem` 可见**（`IsHidden == false`）。如果所有项都被隐藏，Excel 在打开文件时会崩溃或呈现空白的数据透视表。请始终验证您的多选白名单至少包含源数据中的一个项。

## **应该使用哪种 API 和哪种模式？**

下表汇总了何时使用每种 API 和模式，以便您无需阅读每个场景的详细信息即可选择正确的组合。

| 场景 / 用例 | 推荐 API | 使用的属性 | 备注 |
|---|---|---|---|
| 按源列名添加筛选字段（最常见） | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | 高级，一行代码。除非需要 `PivotField` 引用，否则请使用此方法。 |
| 在已有 `PivotField` 对象时添加筛选字段 | `PivotTable.PageFields.Add(PivotField)` | n/a | 在字段对象在其他地方获得或需要复用时使用。 |
| 过滤到单个筛选项（默认模式） | `PivotField.CurrentPageItem` | 设置为特定索引 | 例如，`1` 显示排序列表中的第二个项。 |
| 显示所有项 / 清除筛选器 | `PivotField.CurrentPageItem` | 设置为 `0x7FFD` | 魔术值 `0x7FFD`（十进制 32765）是"所有项"的哨兵值。 |
| 在 Excel 中启用多选 UI | `PivotField.IsMultipleItemSelectionAllowed` | 设置为 `true` | 在任何 `IsHidden` 调用生效之前必需。 |
| 在多选列表中隐藏 / 显示单个项 | `PivotItem.IsHidden` | 按项设置 | 必须至少保留一个项可见（`IsHidden == false`）。 |

{{% alert color="primary" %}}
在配置多选过滤时，请始终记住可见性约束。如果多选筛选字段中的每个 `PivotItem` 都被隐藏，Excel 在打开时会崩溃或呈现空白的数据透视表。针对您的源数据构建白名单，确保至少有一个项保持可见，这样保存的工作簿将在每台机器上可靠打开。
{{% /alert %}}



## **相关文章**

- [Refreshing Pivot Tables in Aspose.Cells for .NET](/cells/zh/net/refresh-pivot-table/)
- [Splitting Excel Files into Multiple Files](/cells/zh/net/splitting-excel-files-into-multiple-files/)
- [Applying Styles to Pivot Tables](/cells/zh/net/apply-style-to-pivot-table/)
- [Converting Excel to OFD Format](/cells/zh/net/ofd/)
- [SmartMarker Single Cell Array Rendering | Aspose.Cells .NET](/cells/zh/net/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="csharp" >}}
