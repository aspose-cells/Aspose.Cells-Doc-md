---
title: 在 Aspose.Cells for Java 中添加数据透视表的行字段和列字段
description: 学习如何在 Aspose.Cells for Java 中向数据透视表的行和列区域添加基础字段，并使用 PivotField.setSubtotals 控制数据透视字段的小计。
linktitle: 行字段和列字段
keywords: Aspose.Cells, Java, 数据透视表, 行字段, 列字段, PivotField, setSubtotals, PivotFieldSubtotalType, 小计
type: docs
weight: 220
url: /zh/java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **向行或列区域添加字段**
`PivotTable.addFieldToArea(int fieldType, String fieldName)` 方法可将基础字段从源数据移至四个数据透视区域之一。`fieldType` 参数接受以下 `PivotFieldType` 值之一。
- `ROW` — 垂直放置在左侧的字段
- `COLUMN` — 水平放置在顶部的字段
- `DATA` — 其值被聚合的字段
- `PAGE` — 用作报表筛选器的字段
添加字段后，可以通过 `PivotTable.getRowFields()` 和 `PivotTable.getColumnFields()` 属性访问它们。每个属性都返回一个 `PivotFieldCollection`。`RowFields` 中索引为 0 的字段是最外层的行字段，后续索引表示嵌套在其中的字段。相同的索引约定也适用于 `ColumnFields`。
字段嵌套顺序很重要。先将 `Category` 添加到行区域，然后再添加 `Item`，将生成一个外部分组为 `Category`、内部分组为 `Item` 的数据透视表。反转顺序则会反转层次结构。

## **数据透视字段小计**
`PivotField.setSubtotals(int subtotalType, boolean shown)` 方法控制数据透视字段显示哪些小计行。每次调用独立切换一种小计类型。传递 `shown = true` 会显示小计，而 `shown = false` 则会隐藏它。由于每次调用只影响一种类型，因此使用不同的 `subtotalType` 值多次调用该方法可构建自定义的小计子集。
`PivotFieldSubtotalType` 枚举定义了可用的小计种类。
- `AUTOMATIC` — Aspose.Cells 选择默认选项（通常对数值字段为 `SUM`）
- `NONE` — 抑制所有小计行
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
仅当行区域（或列区域）中有两个或更多数据透视字段时，小计才会呈现。单个字段之间没有有意义的内容可供小计，因此在这种情况下 `setSubtotals` 调用没有可见效果。因此，本文在每个示例中都放置两个行字段（外层 `Category`，内层 `Item`），以便每个 `Category` 组之间的小计边界可见。
{{% /alert %}}

## **场景 1 — 自动（默认）小计**
如果完全不调用 `setSubtotals`，Aspose.Cells 会将 `AUTOMATIC` 选择应用于数值字段。以下示例通过在外层 `Category` 行字段上调用 `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` 来显式确认此行为。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");
worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);
worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);
worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);
worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);
worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);
worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);
worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);
worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);
PivotTable pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
PivotField categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true);
pivotTable.calculateData();
workbook.save("output_automatic.xlsx");
```

## **场景 2 — 抑制所有小计（None）**
调用 `setSubtotals(PivotFieldSubtotalType.NONE, true)` 会从数据透视表中移除所有小计行，仅保留字段行和底部的总计。当您希望获取原始分组数据而不包含任何汇总行时，这非常有用。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
String[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.length; j++)
{
    worksheet.getCells().get(0, j).putValue(headers[j]);
}
Object[][] data = {
    { "Fruit",     "Apple",  2020, 100 },
    { "Fruit",     "Apple",  2021, 150 },
    { "Fruit",     "Banana", 2020, 80  },
    { "Fruit",     "Banana", 2021, 90  },
    { "Vegetable", "Carrot", 2020, 50  },
    { "Vegetable", "Carrot", 2021, 60  },
    { "Vegetable", "Daikon", 2020, 40  },
    { "Vegetable", "Daikon", 2021, 45  }
};
for (int i = 0; i < data.length; i++)
{
    for (int j = 0; j < data[i].length; j++)
    {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
PivotField categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(PivotFieldSubtotalType.NONE, true);
pivotTable.calculateData();
workbook.save("output_none.xlsx");
```

## **场景 3 — 自定义小计子集（Sum + Average）**
您并不局限于单一的小计类型。每个 `setSubtotals` 调用独立地作用于一种类型，因此调用该方法两次（一次使用 `SUM`，一次使用 `AVERAGE`）会为每个 `Category` 组生成两个小计行的自定义子集。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
worksheet.getCells().get("A1").putValue("Category");
worksheet.getCells().get("B1").putValue("Item");
worksheet.getCells().get("C1").putValue("Year");
worksheet.getCells().get("D1").putValue("Amount");
worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);
worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);
worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);
worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);
worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);
worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);
worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);
worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);
PivotTableCollection pivotTables = worksheet.getPivotTables();
PivotTable pivotTable = pivotTables.add("A1:D9", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
PivotField categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(PivotFieldSubtotalType.SUM, true);
categoryField.setSubtotals(PivotFieldSubtotalType.AVERAGE, true);
pivotTable.calculateData();
workbook.save("output_custom.xlsx");
```

## **回顾**
三种场景的区别仅在于 `setSubtotals` 调用方式不同；其余部分——数据集、字段及其所分配的区域——均完全相同，这使得各布局之间可直接进行比较。
- **字段放置。** `PivotTable.addFieldToArea(PivotFieldType.ROW, fieldName)` 将源列移入某一区域。在同一区域内，调用顺序即为显示顺序，因此首次调用会形成最外层分组。小计功能要求同一区域内至少存在两个字段；若仅有一个字段，则组间无内容可进行小计。
- **场景 1——自动小计。** 若不调用 `setSubtotals`，则由 Excel 自行决定采用默认小计方式，即对数值字段应用其内置默认小计。调用 `setSubtotals` 并传入 `PivotFieldSubtotalType.AUTOMATIC` 则显式记录该选择，而非仅保持隐式默认。
- **场景 2——无小计。** `setSubtotals` 配合 `PivotFieldSubtotalType.NONE` 可关闭默认小计，此时透视表保留字段行与总计行，但移除 Excel 默认在字段行之间插入的小计行。
- **场景 3——选择特定子集。** 每次调用仅切换一种小计类型，且调用累加而非相互覆盖。例如，先以 `PivotFieldSubtotalType.SUM` 调用一次，再以 `PivotFieldSubtotalType.AVERAGE` 调用一次，则两者均被启用，透视表将渲染出“求和”小计、“平均值”小计和总计行。

{{% alert color="primary" %}}
小计功能并不局限于行区域。对从 `PivotTable.ColumnFields` 获取的字段执行相同的 `setSubtotals` 调用，可在列轴上生成相同的三种布局，因为该设置属于透视字段本身，而与其所处的轴无关。
{{% /alert %}}

## **相关文章**
- [数据透视表中的页字段](/cells/zh/java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Java 中刷新数据透视表](/cells/zh/java/refresh-pivot-table/)
- [为数据透视表应用样式](/cells/zh/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}