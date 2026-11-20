---
title: ピボットフィールド項目の個別グループ化
linktitle: 個別グループ化
description: Aspose.Cells for Java の DiscreteGroupItem と PivotFieldGroupOptions.DiscreteGroupItems を使用して、果物や野菜などのカスタムグループにピボットフィールド項目をグループ化する方法について説明します。
keywords: Aspose.Cells for Java, ピボットテーブル, 個別グループ化, DiscreteGroupItem, PivotFieldGroupOptions, ピボット項目のグループ化, カスタムグループ, PivotField.group, Java, Excel ピボットテーブル
type: docs
weight: 90
url: /ja/java/discrete-group-pivot-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる利用シナリオ**
- 自動グループ化では、データ型に基づいて項目をまとめます。たとえば、日付を月や四半期単位にまとめ、数値を範囲別にまとめます。これに対して、個別グループ化では、互いに無関係な特定の項目を、名前を設定したカスタムグループにまとめます。たとえば、商品を果物や野菜別、店舗を地域別、勘定科目をゾーン別にまとめます。`DiscreteGroupItem` クラスと `PivotFieldGroupOptions.getDiscreteGroupItems()` プロパティにより、Aspose.Cells は個別グループ化機能を提供します。
- `DiscreteGroupItem` は、グループ名と、そのグループに属する項目で構成されます。項目は、名前（`new DiscreteGroupItem("fruit", new String[] { "grape", "cherry" })`）またはソースデータ内の 0 始まりの位置（`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`）という 2 つの方法で識別できます。いずれの形式でも同じ結果になります。
- 個別グループ化は、`PivotField.group(PivotFieldGroupOptions)` にオプションを渡すことで、ピボットテーブルの行領域または列領域にあるフィールドに適用されます。

## **項目名に基づいてピボットフィールド項目をグループ化する**
次の例では、小さな売上リスト（商品、日付、金額）を作成し、そのデータから `product` を行領域、`date` を列領域、`amount` をデータ領域に配置したピボットテーブルを生成します。次に、項目名に基づいて、果物（グレープ、チェリー）と野菜（キャロット、ポテト）の 2 つのカスタムグループを定義します。結果には 2 レベルの行レイアウトが表示され、外側のレベルにグループ名、その下に元の項目がネストされます。これにより、カスタムグループ単位および項目単位で傾向を確認できます。

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

`calculateData()` の後、ピボットテーブルの行領域には、果物（グレープ 50、チェリー 80）と野菜（キャロット 60、ポテト 70）が表示され、総合計は 260 になります。列ラベルには、4 つの日付（2/5/2021、3/8/2022、4/10/2023、5/16/2024）が表示されます。

## **項目インデックスに基づいてピボットフィールド項目をグループ化する**
項目名が長い場合やローカライズされている場合、`DiscreteGroupItem` の 2 番目のコンストラクターでは項目をインデックスで識別します。インデックスは、項目がソースデータに現れる順序における 0 始まりの位置であり、アルファベット順ではありません。サンプルデータでは、グレープが項目 0、キャロットが項目 1、ポテトが項目 2、チェリーが項目 3 となるため、果物グループは `{ 0, 3 }`、野菜グループは `{ 1, 2 }` になります。結果は、項目名に基づいてグループ化した例と同じです。

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
- どのカスタムグループにも割り当てられていない項目が失われることはありません。これらの項目は、ピボットテーブル内でカスタムグループと同じレベルに配置され、それぞれ単独の項目エントリとして表示されます。上記の例では、果物グループのみを定義すると、キャロットとポテトは行領域に残り、果物グループの隣に単独のエントリとして表示されます。
- `PivotFieldGroupOptions.getNewPivotField()` プロパティは、個別グループ化のレイアウトを制御します。デフォルト値は `true` です。この場合、元のフィールドの隣にグループ化されたフィールドを新しい外側フィールドとして追加し、上記の 2 レベルのレイアウトを作成します（`getRowFields()` の要素数は 2 に増えます）。`setNewPivotField(false)` を使用すると、代わりに元のフィールドが置き換えられます。この場合、行領域には、グループ名とその集計値のみを含む 1 レベルが表示され、果物 130（50 + 80）、野菜 130（60 + 70）となります。
- `DiscreteGroupItem` の名前ベースとインデックスベースのコンストラクターは、同じ `getDiscreteGroupItems()` 配列内で併用できます。
{{% /alert %}}

## **関連記事**
- [ピボットテーブル内でピボットフィールドをグループ化する](/cells/ja/java/group-pivot-fields-in-the-pivot-table/)
- [ピボットテーブルに行フィールドと列フィールドを追加する](/cells/ja/java/pivot-table-add-row-and-column-fields/)
- [ラベルまたは値に基づいてピボットテーブルをフィルタリングする](/cells/ja/java/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルにスタイルを適用する](/cells/ja/java/apply-style-to-pivot-table/)
- [ピボットテーブルを更新する](/cells/ja/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}