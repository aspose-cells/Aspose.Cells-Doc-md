---
title: 在 Aspose.Cells for .NET 中添加数据透视表的行字段和列字段
linktitle: 行字段和列字段
description: 了解如何在 Aspose.Cells for .NET 中将基本字段添加到数据透视表的行区域和列区域，以及如何使用 PivotField.SetSubtotals 与 PivotFieldSubtotalType 控制数据透视字段的小计。
keywords: Aspose.Cells, .NET, 数据透视表, 行字段, 列字段, PivotField, SetSubtotals, PivotFieldSubtotalType, 小计, C#, Excel 数据透视表
type: docs
weight: 220
url: /zh/net/pivot-table-add-row-column-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **向行区域或列区域添加字段**

`PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` 方法将基本字段从源数据移动到四个数据透视表区域之一。`fieldType` 参数接受以下 `PivotFieldType` 值之一。

- `Row` — 垂直放置在左侧的字段
- `Column` — 水平放置在顶部的字段
- `Data` — 其值被聚合的字段
- `Page` — 用作报表筛选器的字段

添加字段后，可以通过 `PivotTable.RowFields` 和 `PivotTable.ColumnFields` 属性访问它们。每个属性返回一个 `PivotFieldCollection`。`RowFields` 中索引 0 处的字段是最外层行字段，后续索引表示嵌套在其内部的字段。相同的索引约定也适用于 `ColumnFields`。

字段嵌套顺序很重要。先将 `Category` 添加到行区域，然后再添加 `Item`，会生成一个外部分组为 `Category` 而内部分组为 `Item` 的数据透视表。反转顺序则会反转层级关系。

## **数据透视字段小计**

`PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` 方法控制数据透视字段显示哪些小计行。每次调用独立切换单个小计类型。传入 `shown = true` 显示小计，而 `shown = false` 则隐藏它。由于每次调用仅影响一个类型，因此使用不同的 `subtotalType` 值多次调用该方法可以构建自定义的小计子集。

`PivotFieldSubtotalType` 枚举定义了可用的小计种类。

- `Automatic` — Aspose.Cells 选择默认选项（数值字段通常为 `Sum`）
- `None` — 抑制所有小计行
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
仅当行区域（或列区域）中存在两个或更多数据透视字段时，小计才会呈现。单个字段没有可供小计的有意义内容，因此在这种情况下 `SetSubtotals` 调用没有可见效果。所以，本文在每个示例中都放置了两个行字段（外层 `Category`，内层 `Item`），以便每个 `Category` 组之间的小计边界可见。
{{% /alert %}}

## **场景 1 — 自动（默认）小计**

当您完全不调用 `SetSubtotals` 时，Aspose.Cells 会将 `Automatic` 选择应用于数值字段。以下示例通过对最外层 `Category` 行字段调用 `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` 来明确确认此行为。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

worksheet.Cells[0, 0].PutValue("Category");
worksheet.Cells[0, 1].PutValue("Item");
worksheet.Cells[0, 2].PutValue("Year");
worksheet.Cells[0, 3].PutValue("Amount");

worksheet.Cells[1, 0].PutValue("Fruit");
worksheet.Cells[1, 1].PutValue("Apple");
worksheet.Cells[1, 2].PutValue(2020);
worksheet.Cells[1, 3].PutValue(100);

worksheet.Cells[2, 0].PutValue("Fruit");
worksheet.Cells[2, 1].PutValue("Apple");
worksheet.Cells[2, 2].PutValue(2021);
worksheet.Cells[2, 3].PutValue(150);

worksheet.Cells[3, 0].PutValue("Fruit");
worksheet.Cells[3, 1].PutValue("Banana");
worksheet.Cells[3, 2].PutValue(2020);
worksheet.Cells[3, 3].PutValue(80);

worksheet.Cells[4, 0].PutValue("Fruit");
worksheet.Cells[4, 1].PutValue("Banana");
worksheet.Cells[4, 2].PutValue(2021);
worksheet.Cells[4, 3].PutValue(90);

worksheet.Cells[5, 0].PutValue("Vegetable");
worksheet.Cells[5, 1].PutValue("Carrot");
worksheet.Cells[5, 2].PutValue(2020);
worksheet.Cells[5, 3].PutValue(50);

worksheet.Cells[6, 0].PutValue("Vegetable");
worksheet.Cells[6, 1].PutValue("Carrot");
worksheet.Cells[6, 2].PutValue(2021);
worksheet.Cells[6, 3].PutValue(60);

worksheet.Cells[7, 0].PutValue("Vegetable");
worksheet.Cells[7, 1].PutValue("Daikon");
worksheet.Cells[7, 2].PutValue(2020);
worksheet.Cells[7, 3].PutValue(40);

worksheet.Cells[8, 0].PutValue("Vegetable");
worksheet.Cells[8, 1].PutValue("Daikon");
worksheet.Cells[8, 2].PutValue(2021);
worksheet.Cells[8, 3].PutValue(45);

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.Automatic, true);

pivotTable.CalculateData();

workbook.Save("output_automatic.xlsx");
```

## **场景 2 — 抑制所有小计 (None)**

调用 `SetSubtotals(PivotFieldSubtotalType.None, true)` 会从数据透视表中移除所有小计行，仅保留字段行和底部的总计行。当您希望获取不含任何汇总行的原始分组数据时，此功能非常有用。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

string[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.Length; j++)
{
    worksheet.Cells[0, j].PutValue(headers[j]);
}

object[,] data = {
    { "Fruit",     "Apple",  2020, 100 },
    { "Fruit",     "Apple",  2021, 150 },
    { "Fruit",     "Banana", 2020, 80  },
    { "Fruit",     "Banana", 2021, 90  },
    { "Vegetable", "Carrot", 2020, 50  },
    { "Vegetable", "Carrot", 2021, 60  },
    { "Vegetable", "Daikon", 2020, 40  },
    { "Vegetable", "Daikon", 2021, 45  }
};

for (int i = 0; i < data.GetLength(0); i++)
{
    for (int j = 0; j < data.GetLength(1); j++)
    {
        worksheet.Cells[i + 1, j].PutValue(data[i, j]);
    }
}

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.None, true);
pivotTable.CalculateData();

workbook.Save("output_none.xlsx");
```

## **场景 3 — 自定义小计子集 (Sum + Average)**

您不限于使用单一的小计类型。每次 `SetSubtotals` 调用独立作用于一个类型，因此调用该方法两次（一次使用 `Sum`，一次使用 `Average`）会为每个 `Category` 组生成两个小计行的自定义子集。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

worksheet.Cells["A1"].PutValue("Category");
worksheet.Cells["B1"].PutValue("Item");
worksheet.Cells["C1"].PutValue("Year");
worksheet.Cells["D1"].PutValue("Amount");

worksheet.Cells[1, 0].PutValue("Fruit");
worksheet.Cells[1, 1].PutValue("Apple");
worksheet.Cells[1, 2].PutValue(2020);
worksheet.Cells[1, 3].PutValue(100);

worksheet.Cells[2, 0].PutValue("Fruit");
worksheet.Cells[2, 1].PutValue("Apple");
worksheet.Cells[2, 2].PutValue(2021);
worksheet.Cells[2, 3].PutValue(150);

worksheet.Cells[3, 0].PutValue("Fruit");
worksheet.Cells[3, 1].PutValue("Banana");
worksheet.Cells[3, 2].PutValue(2020);
worksheet.Cells[3, 3].PutValue(80);

worksheet.Cells[4, 0].PutValue("Fruit");
worksheet.Cells[4, 1].PutValue("Banana");
worksheet.Cells[4, 2].PutValue(2021);
worksheet.Cells[4, 3].PutValue(90);

worksheet.Cells[5, 0].PutValue("Vegetable");
worksheet.Cells[5, 1].PutValue("Carrot");
worksheet.Cells[5, 2].PutValue(2020);
worksheet.Cells[5, 3].PutValue(50);

worksheet.Cells[6, 0].PutValue("Vegetable");
worksheet.Cells[6, 1].PutValue("Carrot");
worksheet.Cells[6, 2].PutValue(2021);
worksheet.Cells[6, 3].PutValue(60);

worksheet.Cells[7, 0].PutValue("Vegetable");
worksheet.Cells[7, 1].PutValue("Daikon");
worksheet.Cells[7, 2].PutValue(2020);
worksheet.Cells[7, 3].PutValue(40);

worksheet.Cells[8, 0].PutValue("Vegetable");
worksheet.Cells[8, 1].PutValue("Daikon");
worksheet.Cells[8, 2].PutValue(2021);
worksheet.Cells[8, 3].PutValue(45);

PivotTableCollection pivotTables = worksheet.PivotTables;
int pivotIndex = pivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = pivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.Sum, true);
categoryField.SetSubtotals(PivotFieldSubtotalType.Average, true);

pivotTable.CalculateData();

workbook.Save("output_custom.xlsx");
```

## **小结**

上述三个场景使用相同的数据集和数据透视表结构。它们之间唯一的区别是对最外层 `Category` 行字段应用的 `SetSubtotals` 调用。请记住两字段规则：区域中单个字段之间没有内容可进行小计，因此当您希望 `SetSubtotals` 产生可见效果时，始终在行或列区域中放置至少两个字段。

## **相关文章**

- [数据透视表中的页面字段](/cells/zh/net/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for .NET 中刷新数据透视表](/cells/zh/net/refresh-pivot-table/)
- [向数据透视表应用样式](/cells/zh/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
