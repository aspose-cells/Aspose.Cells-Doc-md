---
title: Aspose.Cells for Java でピボットテーブルに行フィールドと列フィールドを追加する
linktitle: Aspose.Cells for Java でピボットテーブルに行フィールドと列フィールドを追加する
description: Aspose.Cells for Java で PivotField.setSubtotals を使用して、ピボットテーブルの行領域と列領域に基本フィールドを追加し、ピボットフィールドの小計を制御する方法を学びます。
keywords: Aspose.Cells, Java, ピボットテーブル, 行フィールド, 列フィールド, PivotField, setSubtotals, PivotFieldSubtotalType, 小計
type: docs
weight: 220
url: /ja/java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **行または列領域にフィールドを追加する**
`PivotTable.addFieldToArea(int fieldType, String fieldName)` メソッドは、ソースデータから基本フィールドを 4 つのピボット領域のいずれか 1 つに移動します。`fieldType` 引数には、次の `PivotFieldType` 値のいずれかを指定できます。
- `ROW` — 左側に垂直に配置されるフィールド
- `COLUMN` — 上部に水平に配置されるフィールド
- `DATA` — 値が集計されるフィールド
- `PAGE` — レポートフィルターとして使用されるフィールド
フィールドの入れ子順序は重要です。最初に `Category` を行領域に追加し、その後 `Item` を追加すると、`Category` が外側のグループ、`Item` が内側のグループとなるピボットテーブルが作成されます。順序を逆にすると、階層も逆になります。

## **ピボットフィールドの小計**
`PivotField.setSubtotals(int subtotalType, boolean shown)` メソッドは、ピボットフィールドにどの小計行を表示するかを制御します。各呼び出しでは、1 つの小計タイプを独立して設定します。`shown = true` を渡すと小計が表示され、`shown = false` を渡すと非表示になります。各呼び出しが 1 つのタイプにのみ影響するため、異なる `subtotalType` 値でこのメソッドを複数回呼び出すと、任意の小計のサブセットを構成できます。
`PivotFieldSubtotalType` 列挙型は、使用できる小計の種類を定義します。
- `AUTOMATIC` — Aspose.Cells が既定の選択を行います（通常、数値フィールドでは `SUM`）
- `NONE` — すべての小計行を非表示にします
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
小計は、行領域（または列領域）に 2 つ以上のピボットフィールドがある場合にのみ表示されます。フィールドが 1 つだけでは、その間に小計を算出できる対象がないため、`setSubtotals` の呼び出しには表示上の効果がありません。そのため、本記事の各例では 2 つの行フィールド（外側が `Category`、内側が `Item`）を配置し、各 `Category` グループの小計の区切りを確認できるようにしています。
{{% /alert %}}

## **シナリオ 1 — 自動小計（デフォルト）**
`setSubtotals` を一度も呼び出さない場合、Aspose.Cells は数値フィールドに `AUTOMATIC` 選択を適用します。次の例では、外側の `Category` 行フィールドに対して `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` を呼び出すことで、この動作を明示的に確認します。

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

## **シナリオ 2 — すべての小計を非表示にする（`NONE`）**
`setSubtotals(PivotFieldSubtotalType.NONE, true)` を呼び出すと、ピボットテーブルからすべての小計行が削除され、フィールド行と下部の総計だけが残ります。サマリー行のない、元のグループ化データが必要な場合に便利です。

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

## **シナリオ 3 — カスタム小計のサブセット（`SUM` + `AVERAGE`）**
1 つの小計タイプに限定されません。各 `setSubtotals` の呼び出しは、1 つの小計タイプに対して独立して機能するため、このメソッドを 2 回（1 回目は `SUM`、2 回目は `AVERAGE`）呼び出すと、各 `Category` グループに対して 2 つの小計行からなるカスタムサブセットが作成されます。

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

## **まとめ**

3つのシナリオの違いは、`setSubtotals` メソッドの呼び出し方の1点のみです。その他の点 — データセット、フィールド、およびそれらが割り当てられるエリア — はすべて同一であり、これによりレイアウトを直接比較できるようになります。
- **フィールドの配置。** `PivotTable.addFieldToArea(PivotFieldType.ROW, fieldName)` は、ソース列を特定のエリアへ移動させます。同一エリア内では、メソッド呼び出しの順序が表示順序となります。したがって、最初の呼び出しが最も外側のグループになります。サブトータルを設定するには、同一エリア内に2つ以上のフィールドが必要です。1つのフィールドだけでは、グループ間にサブトータルを挿入する余地がありません。
- **シナリオ1 — 自動サブトータル。** `setSubtotals` を呼び出さない場合、Excelが独自のデフォルトサブトータルを数値フィールドに適用します。一方、`PivotFieldSubtotalType.AUTOMATIC` を指定して `setSubtotals` を呼び出すと、その選択が明示的にレコードされます。
- **シナリオ2 — サブトータルなし。** `PivotFieldSubtotalType.NONE` を指定して `setSubtotals` を呼び出すと、デフォルトのサブトータルが無効化され、ピボットテーブルはフィールド行と合計行を維持しますが、Excelが通常挿入する中間のサブトータル行は省略されます。
- **シナリオ3 — 選択したサブトータルのセット。** `setSubtotals` の各呼び出しは、1つのサブトータルタイプを切り替えます。複数回の呼び出しは累積的に機能し、相互に上書きしません。したがって、`PivotFieldSubtotalType.SUM` で1回呼び出し、`PivotFieldSubtotalType.AVERAGE` で1回呼び出すと、両方のサブトータルが有効となり、ピボットテーブルには「合計」サブトータル、「平均」サブトータル、および「合計」が表示されます。

{{% alert color="primary" %}}
サブトータルに関する設定は、行エリアに固有のものではありません。`PivotTable.ColumnFields` から取得したフィールドに対して同様の `setSubtotals` 呼び出しを行うと、列軸上でも同じ3つのレイアウトが得られます。これは、設定が軸ではなく、ピボットフィールド自体に属するためです。
{{% /alert %}}
## **関連記事**
- [ピボットテーブルのページフィールド](/cells/ja/java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Java でピボットテーブルを更新する](/cells/ja/java/refresh-pivot-table/)
- [ピボットテーブルにスタイルを適用する](/cells/ja/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}