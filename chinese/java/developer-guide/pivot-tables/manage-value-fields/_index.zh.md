---
title: Aspose.Cells for Java 中的值字段
linktitle: Aspose.Cells for Java 中的值字段
description: 学习如何在 Aspose.Cells for Java 中将基础字段添加到数据透视表的数据区域，使用 PivotField.Function 更改汇总函数，以及将值字段绘制到行轴或列轴上。
keywords: Aspose.Cells, Java, 数据透视表, 值字段, PivotField, PivotField.Function, 数据字段, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /zh/java/manage-value-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## 将字段添加到数据区域
将基础字段添加到数据（值）区域是塑造数据透视表如何汇总源数据的第一步。Aspose.Cells 公开了 `PivotTable.addFieldToArea(PivotFieldType, String)` 重载方法，该方法接受常量 `PivotFieldType.DATA` 和源列名称作为参数。字段被添加到数据区域后，API 会通过 `PivotTable.getDataFields()` 集合按字段添加的顺序将其公开。默认情况下，数值型源列使用 `ConsolidationFunction.SUM` 进行汇总，而非数值型列默认使用 `COUNT`。

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// A1:D1 中的表头
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// A2:D9 中的数据行，使用嵌套循环根据 j 进行分支
for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j < 4; j++)
 {
 switch (j)
 {
 case 0:
 worksheet.getCells().get(i, j).putValue(i <= 4 ? "Fruit" : "Vegetable");
 break;
 case 1:
 if (i == 1 || i == 2) worksheet.getCells().get(i, j).putValue("Apple");
 else if (i == 3 || i == 4) worksheet.getCells().get(i, j).putValue("Banana");
 else if (i == 5 || i == 6) worksheet.getCells().get(i, j).putValue("Carrot");
 else worksheet.getCells().get(i, j).putValue("Daikon");
 break;
 case 2:
 worksheet.getCells().get(i, j).putValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) worksheet.getCells().get(i, j).putValue(100);
 else if (i == 2) worksheet.getCells().get(i, j).putValue(150);
 else if (i == 3) worksheet.getCells().get(i, j).putValue(80);
 else if (i == 4) worksheet.getCells().get(i, j).putValue(90);
 else if (i == 5) worksheet.getCells().get(i, j).putValue(50);
 else if (i == 6) worksheet.getCells().get(i, j).putValue(60);
 else if (i == 7) worksheet.getCells().get(i, j).putValue(40);
 else worksheet.getCells().get(i, j).putValue(45);
 break;
 }
 }
}

// 在 F3 处添加名称为 PivotTable1 的数据透视表
int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// 数据透视表布局：Category 和 Item 作为行，Year 作为列，Amount 作为数据字段
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## 更改汇总函数
数据区域中的每个字段在内部都被包装为 `PivotField` 实例，其 `getFunction()` 属性返回 `ConsolidationFunction` 枚举中的一个值。同一 `setFunction(...)` setter 允许您在可用的汇总函数之间切换，包括 `SUM`、`COUNT`、`AVERAGE`、`MAX`、`MIN`、`PRODUCT`、`STD_DEV`、`STD_DEVP`、`VAR` 和 `VARP`。
{{% alert color="primary" %}}
更改 `Function` 仅影响汇总方式，源列不会改变。
{{% /alert %}}
因此，您可以在同一个数据透视表中保留一个 `SUM` 的数据字段，同时添加第二个针对同一源列但使用 `COUNT` 或 `AVERAGE` 的数据字段。

```java
import com.aspose.cells.*;
import com.aspose.cells.pivot.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

String[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.length; j++) {
 worksheet.getCells().get(0, j).putValue(headers[j]);
}

Object[][] data = {
 { "Fruit", "Apple", 2020, 100 },
 { "Fruit", "Apple", 2021, 150 },
 { "Fruit", "Banana", 2020, 80 },
 { "Fruit", "Banana", 2021, 90 },
 { "Vegetable", "Carrot", 2020, 50 },
 { "Vegetable", "Carrot", 2021, 60 },
 { "Vegetable", "Daikon", 2020, 40 },
 { "Vegetable", "Daikon", 2021, 45 }
};

for (int i = 0; i < data.length; i++) {
 for (int j = 0; j < data[i].length; j++) {
 worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
 }
}

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");

pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

PivotField countField = pivotTable.getDataFields().get(1);
countField.setFunction(ConsolidationFunction.COUNT);

pivotTable.calculateData();
workbook.save("output_function.xlsx");
```

## 将值字段绘制到行轴或列轴
当数据透视表包含两个或更多数据字段时，Aspose.Cells 会公开一个名为 `PivotTable.getValuesField()` 的额外虚拟字段。该虚拟字段表示数据区域中每个数据字段的汇总。您可以将其作为基础数据透视字段拖到行区域或列区域，这对于并排排列多个度量值非常有用。
{{% alert color="primary" %}}
如果没有值字段或仅有一个值字段，`PivotTable.getValuesField()` 不起作用。
{{% /alert %}}
以下场景通过三个端到端示例演示了上述每个功能，这些示例都针对相同的数据透视结构。

```java
import com.aspose.cells.*;
import com.aspose.cells.pivot.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

String[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.length; j++) {
 worksheet.getCells().get(0, j).putValue(headers[j]);
}

Object[][] data = {
 { "Fruit", "Apple", 2020, 100 },
 { "Fruit", "Apple", 2021, 150 },
 { "Fruit", "Banana", 2020, 80 },
 { "Fruit", "Banana", 2021, 90 },
 { "Vegetable", "Carrot", 2020, 50 },
 { "Vegetable", "Carrot", 2021, 60 },
 { "Vegetable", "Daikon", 2020, 40 },
 { "Vegetable", "Daikon", 2021, 45 }
};

for (int i = 0; i < data.length; i++) {
 for (int j = 0; j < data[i].length; j++) {
 worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
 }
}

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.getDataFields().get(1).setFunction(ConsolidationFunction.COUNT);

pivotTable.addFieldToArea(PivotFieldType.COLUMN, pivotTable.getValuesField());

pivotTable.calculateData();
workbook.save("output_plot.xlsx");
```

{{< app/cells/assistant language="java" >}}