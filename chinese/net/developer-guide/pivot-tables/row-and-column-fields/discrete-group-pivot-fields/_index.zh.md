---
title: 数据透视表字段项目的离散分组
description: 了解如何使用 DiscreteGroupItem 和 PivotFieldGroupOptions.DiscreteGroupItems 在 Aspose.Cells for .NET 中将数据透视表字段项目划分为自定义命名组，例如水果和蔬菜。
linktitle: 离散分组
keywords: Aspose.Cells, 数据透视表, 离散分组, DiscreteGroupItem, PivotFieldGroupOptions, 对数据透视表项目分组, 自定义组, PivotField.Group, C#, Excel 数据透视表
type: docs
weight: 90
url: /zh/net/discrete-group-pivot-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的适用场景**
- 自动分组根据数据类型收集项目，例如将日期归入月份和季度，或将数字归入数值区间。离散分组解决的是相反的问题，它将特定的、互不相关的项目收集到自定义命名组中，例如将产品归入水果和蔬菜组、将商店归入区域组或将账户归入分区组。Aspose.Cells 通过 `DiscreteGroupItem` 类和 `PivotFieldGroupOptions.DiscreteGroupItems` 属性提供离散分组功能。
- `DiscreteGroupItem` 由一个组名及属于该组的项目组成。可以通过两种方式标识这些项目：按名称（`new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" })`），或按其在源数据中的从零开始的位置（`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`）。两种形式会产生相同的结果。
- 通过将选项传递给 `PivotField.Group(PivotFieldGroupOptions)`，可对数据透视表行区域或列区域中的字段应用离散分组。

## **按项目名称对数据透视表字段项目进行分组**
以下示例构建一个小型销售列表（产品、日期和金额），并基于该列表创建数据透视表：将 `product` 放在行区域，将 `date` 放在列区域，将 `amount` 放在数据区域；然后按项目名称定义两个自定义组，即水果（葡萄、樱桃）和蔬菜（胡萝卜、土豆）。结果采用两级行布局：组名位于外层级别，原始项目嵌套在其下，从而可以按自定义组和单个项目分别查看趋势。

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook wb = new Workbook();
Worksheet sheet = wb.Worksheets[0];
Cells cells = sheet.Cells;
cells[0, 0].Value = "product";
cells[1, 0].Value = "grape";
cells[2, 0].Value = "carrot";
cells[3, 0].Value = "potato";
cells[4, 0].Value = "cherry";
Style dateStyle = wb.CreateStyle();
dateStyle.Custom = "m/d/yyyy";
cells[0, 1].Value = "date";
cells[1, 1].Value = new DateTime(2021, 2, 5);
cells[2, 1].Value = new DateTime(2022, 3, 8);
cells[3, 1].Value = new DateTime(2023, 4, 10);
cells[4, 1].Value = new DateTime(2024, 5, 16);
for (int r = 1; r <= 4; r++) cells[r, 1].SetStyle(dateStyle);
cells[0, 2].Value = "amount";
cells[1, 2].Value = 50;
cells[2, 2].Value = 60;
cells[3, 2].Value = 70;
cells[4, 2].Value = 80;
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.PivotTables.Add("=Sheet1!A1:C5", 11, 0);
pivotTable.AddFieldToArea(PivotFieldType.Row, "product");
pivotTable.AddFieldToArea(PivotFieldType.Column, "date");
pivotTable.AddFieldToArea(PivotFieldType.Data, "amount");
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleMedium10;
// Group specific items into custom groups by item names
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new string[] { "carrot", "potato" });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.DiscreteGroupItems = new DiscreteGroupItem[] { fruit, vegetable };
pivotTable.RowFields[0].Group(groupOptions);
pivotTable.CalculateData();
wb.Save("outputDiscreteGroupPivotField.xlsx");
```

执行 `CalculateData()` 后，数据透视表的行区域显示水果（葡萄 50、樱桃 80）和蔬菜（胡萝卜 60、土豆 70），总计为 260；列标签仍保留四个日期（2/5/2021、3/8/2022、4/10/2023、5/16/2024）。

## **按项目索引对数据透视表字段项目进行分组**
当项目名称较长或已经本地化时，可以使用 `DiscreteGroupItem` 的第二个构造函数按索引标识项目。这些索引是项目在源数据中出现顺序下的从零开始的位置，而不是按字母顺序排列的位置。在上述示例数据中，葡萄是项目 0，胡萝卜是项目 1，土豆是项目 2，樱桃是项目 3，因此水果组为 `{ 0, 3 }`，蔬菜组为 `{ 1, 2 }`。结果与按名称分组的示例完全相同。

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook wb = new Workbook();
Worksheet sheet = wb.Worksheets[0];
Cells cells = sheet.Cells;
cells[0, 0].Value = "product";
cells[1, 0].Value = "grape";
cells[2, 0].Value = "carrot";
cells[3, 0].Value = "potato";
cells[4, 0].Value = "cherry";
Style dateStyle = wb.CreateStyle();
dateStyle.Custom = "m/d/yyyy";
cells[0, 1].Value = "date";
cells[1, 1].Value = new DateTime(2021, 2, 5);
cells[2, 1].Value = new DateTime(2022, 3, 8);
cells[3, 1].Value = new DateTime(2023, 4, 10);
cells[4, 1].Value = new DateTime(2024, 5, 16);
for (int r = 1; r <= 4; r++) cells[r, 1].SetStyle(dateStyle);
cells[0, 2].Value = "amount";
cells[1, 2].Value = 50;
cells[2, 2].Value = 60;
cells[3, 2].Value = 70;
cells[4, 2].Value = 80;
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.PivotTables.Add("=Sheet1!A1:C5", 11, 0);
pivotTable.AddFieldToArea(PivotFieldType.Row, "product");
pivotTable.AddFieldToArea(PivotFieldType.Column, "date");
pivotTable.AddFieldToArea(PivotFieldType.Data, "amount");
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleMedium10;
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data)
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new int[] { 0, 3 });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new int[] { 1, 2 });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.DiscreteGroupItems = new DiscreteGroupItem[] { fruit, vegetable };
pivotTable.RowFields[0].Group(groupOptions);
pivotTable.CalculateData();
wb.Save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **注意**

{{% alert color="primary" %}}
- 未分配到任何自定义组的项目不会丢失。它们仍保留在数据透视表中，与自定义组处于同一级别，每个项目均作为独立的单项目条目存在。在上述示例中，仅定义水果组时，胡萝卜和土豆仍会作为独立条目保留在行区域中，并与水果组并列。
- `PivotFieldGroupOptions.NewPivotField` 属性控制离散分组的布局。其默认值为 true，此时会将分组后的字段作为新的外层字段添加到原字段旁边，从而产生上述两级布局（`RowFields` 增至 2）。将其设为 false 则会改为替换原字段，此时行区域仅显示一个级别，其中只包含组名及其汇总值，即水果 130（50 + 80）和蔬菜 130（60 + 70）。
- `DiscreteGroupItem` 基于名称和基于索引的构造函数可以在同一个 `DiscreteGroupItems` 数组中混合使用。
{{% /alert %}}

## **相关文章**
- [在数据透视表中对字段进行分组](/cells/zh/net/group-pivot-fields-in-the-pivot-table/)
- [在数据透视表中添加行字段和列字段](/cells/zh/net/pivot-table-add-row-and-column-fields/)
- [按标签或值筛选数据透视表](/cells/zh/net/filter-by-label-or-value-of-pivot-table/)
- [为数据透视表应用样式](/cells/zh/net/apply-style-to-pivot-table/)
- [刷新数据透视表](/cells/zh/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}