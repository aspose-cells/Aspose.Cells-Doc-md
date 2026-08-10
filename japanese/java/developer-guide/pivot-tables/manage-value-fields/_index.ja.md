---
title: Aspose.Cells for Java の値フィールド
linktitle: Aspose.Cells for Java の値フィールド
description: ピボットテーブルのデータ領域にベースフィールドを追加し、PivotField.Function で集計関数を変更し、Row または Column 軸に値フィールドをプロットする方法を Aspose.Cells for Java で学びます。
keywords: Aspose.Cells, Java, ピボットテーブル, 値フィールド, PivotField, PivotField.Function, データフィールド, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ja/java/manage-value-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## データ領域へのフィールドの追加
データ(値)領域にベースフィールドを追加することは、ピボットテーブルがソースデータを集計する方法を形作る最初のステップです。Aspose.Cells は `PivotTable.addFieldToArea(PivotFieldType, String)` を提供しており、定数 `PivotFieldType.DATA` とソース列名を受け取るオーバーロードを使用できます。フィールドがデータ領域に追加されると、API はそれを `PivotTable.getDataFields()` コレクションを通じて、フィールドが追加された順に公開します。デフォルトでは、数値ソース列は `ConsolidationFunction.SUM` で集計され、非数値列のデフォルトは `COUNT` となります。

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// A1:D1のヘッダー
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// jで分岐するネストされたループを使用したA2:D9のデータ行
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

// F3に「PivotTable1」という名前のピボットテーブルを追加
int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// ピボットレイアウト：行にCategoryとItem、列にYear、データフィールドにAmount
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## 集計関数の変更
データ領域に配置された各フィールドは内部的に `PivotField` インスタンスとしてラップされ、その `getFunction()` プロパティは `ConsolidationFunction` 列挙型の値を返します。同じ `setFunction(...)` セッターを使用すると、`SUM`、`COUNT`、`AVERAGE`、`MAX`、`MIN`、`PRODUCT`、`STD_DEV`、`STD_DEVP`、`VAR`、`VARP` などの利用可能な集計関数を切り替えることができます。
{{% alert color="primary" %}}
`Function` の変更は集計にのみ影響し、ソース列は変更されません。
{{% /alert %}}
そのため、1 つのデータフィールドを `SUM` のままにして、同じソース列を対象とするが `COUNT` または `AVERAGE` を使用する 2 番目のデータフィールドを追加することも、すべて単一のピボット内で行うことができます。

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

## 値フィールドの Row または Column 軸へのプロット
ピボットテーブルに 2 つ以上のデータフィールドが含まれる場合、Aspose.Cells は `PivotTable.getValuesField()` という追加の仮想フィールドを公開します。この仮想フィールドは、データ領域に存在するすべてのデータフィールドの集計を表します。これをベースピボットフィールドとして Row または Column 領域にドラッグすることができ、複数のメジャーを並べてレイアウトする場合に便利です。
{{% alert color="primary" %}}
値フィールドが存在しないか 1 つしかない場合、`PivotTable.getValuesField()` は機能しません。
{{% /alert %}}
以下のシナリオでは、上記で説明した各機能を同じピボット構造に対して実証する 3 つのエンドツーエンドの例を紹介します。

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