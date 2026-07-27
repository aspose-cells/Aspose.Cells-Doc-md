---
title: 在 Aspose.Cells for .NET 中添加数据透视表的行字段和列字段
linktitle: 行字段和列字段
description: 学习如何在 Aspose.Cells for Java 中向数据透视表的行和列区域添加基础字段，并使用 PivotField.setSubtotals 控制数据透视字段的小计。
keywords: Aspose.Cells, Java, 数据透视表, 行字段, 列字段, PivotField, setSubtotals, PivotFieldSubtotalType, 小计
type: docs
weight: 220
url: /zh/java/pivot-table-add-row-column-fields/
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

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

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

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

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
int pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);

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

上述三个场景共享相同的数据集和数据透视表结构。它们之间唯一的区别是应用于外层 `Category` 行字段的 `setSubtotals` 调用。请记住双字段规则：区域中的单个字段之间没有可供小计的内容，因此，当您希望 `setSubtotals` 产生可见效果时，请始终在行或列区域中放置至少两个字段。

## **相关文章**

- [数据透视表中的页面字段](/cells/zh/java/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for Java 中刷新数据透视表](/cells/zh/java/refresh-pivot-table/)
- [向数据透视表应用样式](/cells/zh/java/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
