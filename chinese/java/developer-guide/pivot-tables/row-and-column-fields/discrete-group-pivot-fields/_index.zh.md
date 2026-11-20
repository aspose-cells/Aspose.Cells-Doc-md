---
title: 数据透视表字段项目的离散分组
linktitle: 离散分组
description: 了解如何使用 DiscreteGroupItem 和 PivotFieldGroupOptions.DiscreteGroupItems 在 Aspose.Cells for Java 中将数据透视表字段项目分组为水果和蔬菜等自定义命名组。
keywords: Aspose.Cells for Java, 数据透视表, 离散分组, DiscreteGroupItem, PivotFieldGroupOptions, 对数据透视表项目进行分组, 自定义组, PivotField.group, Java, Excel 数据透视表
type: docs
weight: 90
url: /zh/java/discrete-group-pivot-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
- 自动分组按数据类型对项目进行归类，例如将日期按月份和季度分组，或将数字按值范围分组。离散分组则解决相反的问题，即将特定的、彼此无关的项目归入自定义命名组，例如将产品分为水果和蔬菜、将门店归入地区，或将账户归入分区。Aspose.Cells 通过 `DiscreteGroupItem` 类和 `PivotFieldGroupOptions.getDiscreteGroupItems()` 属性提供离散分组功能。
- `DiscreteGroupItem` 由组名以及归属于该组的项目组成。可以通过两种方式标识这些项目：按名称标识（`new DiscreteGroupItem("fruit", new String[] { "grape", "cherry" })`），或按其在源数据中从 0 开始的位置标识（`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`）。这两种形式都会产生相同的结果。
- 通过将选项传递给 `PivotField.group(PivotFieldGroupOptions)`，可以将离散分组应用到数据透视表行区域或列区域中的字段。

## **按项目名称对数据透视表字段项目进行分组**
以下示例创建一个小型销售列表（产品、日期和金额），并基于该列表创建数据透视表，其中 `product` 位于行区域，`date` 位于列区域，`amount` 位于数据区域。随后按项目名称定义两个自定义组，即水果（葡萄、樱桃）和蔬菜（胡萝卜、土豆）。结果呈现两级行布局：组名作为外层级别，原始项目嵌套在其下，从而可按自定义组和单个项目查看趋势。

```java
import com.aspose.cells.*;
Workbook wb = new Workbook();
Worksheet sheet = wb.getWorksheets().get(0);
Cells cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
Style dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(new DateTime(2021, 2, 5));
cells.get(2, 1).putValue(new DateTime(2022, 3, 8));
cells.get(3, 1).putValue(new DateTime(2023, 4, 10));
cells.get(4, 1).putValue(new DateTime(2024, 5, 16));
for (int r = 1; r <= 4; r++) cells.get(r, 1).setStyle(dateStyle);
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
// Group specific items into custom groups by item names
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new String[] { "grape", "cherry" });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new String[] { "carrot", "potato" });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems(new DiscreteGroupItem[] { fruit, vegetable });
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

调用 `calculateData()` 后，数据透视表的行区域显示水果（葡萄 50、樱桃 80）和蔬菜（胡萝卜 60、土豆 70），总计为 260；列标签仍保留四个日期（2/5/2021、3/8/2022、4/10/2023、5/16/2024）。

## **按项目索引对数据透视表字段项目进行分组**
当项目名称较长或已本地化时，可使用 `DiscreteGroupItem` 的第二个构造函数，通过索引标识项目。索引从 0 开始，对应项目在源数据中的出现顺序，而非按字母顺序排列。在上述示例数据中，葡萄是项目 0，胡萝卜是项目 1，土豆是项目 2，樱桃是项目 3，因此水果为 `{ 0, 3 }`，蔬菜为 `{ 1, 2 }`。结果与基于名称的示例完全相同。

```java
import com.aspose.cells.*;
Workbook wb = new Workbook();
Worksheet sheet = wb.getWorksheets().get(0);
Cells cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
Style dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(new DateTime(2021, 2, 5));
cells.get(2, 1).putValue(new DateTime(2022, 3, 8));
cells.get(3, 1).putValue(new DateTime(2023, 4, 10));
cells.get(4, 1).putValue(new DateTime(2024, 5, 16));
for (int r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
PivotTable pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new int[] { 0, 3 });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new int[] { 1, 2 });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems(new DiscreteGroupItem[] { fruit, vegetable });
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **注意**

{{% alert color="primary" %}}
- 未分配到任何自定义组的项目不会丢失。它们仍保留在数据透视表中，与自定义组处于同一层级，每个项目均作为单独的条目保留。在上述示例中，如果仅定义水果组，胡萝卜和土豆仍会作为独立条目保留在行区域中，并与水果组并列显示。
- `PivotFieldGroupOptions.getNewPivotField()` 属性控制离散分组的布局。其默认值为 true，这会在原始字段旁将分组字段作为新的外层字段添加，从而生成上述两级布局（`getRowFields()` 增至 2）。调用 `setNewPivotField(false)` 可将其设置为 false，以替换原始字段。此时，行区域仅显示一个层级，其中只包含组名及其汇总值，即水果 130（50 + 80）和蔬菜 130（60 + 70）。
- 可以在同一个 `getDiscreteGroupItems()` 数组中混合使用基于名称和基于索引的 `DiscreteGroupItem` 构造函数。
{{% /alert %}}

## **相关文章**
- [在数据透视表中对数据透视字段进行分组](/cells/zh/java/group-pivot-fields-in-the-pivot-table/)
- [在数据透视表中添加行和列字段](/cells/zh/java/pivot-table-add-row-and-column-fields/)
- [按标签或值筛选数据透视表](/cells/zh/java/filter-by-label-or-value-of-pivot-table/)
- [将样式应用于数据透视表](/cells/zh/java/apply-style-to-pivot-table/)
- [刷新数据透视表](/cells/zh/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}