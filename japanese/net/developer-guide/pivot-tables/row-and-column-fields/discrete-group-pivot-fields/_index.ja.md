---
title: ピボットフィールド項目の個別グループ化
linktitle: 個別グループ化
description: `DiscreteGroupItem` と `PivotFieldGroupOptions.DiscreteGroupItems` を使用して、果物や野菜などの名前付きのカスタムグループにピボットフィールド項目をグループ化する方法を Aspose.Cells for .NET で学習します。
keywords: Aspose.Cells, ピボットテーブル, 個別グループ化, DiscreteGroupItem, PivotFieldGroupOptions, ピボット項目のグループ化, カスタムグループ, PivotField.Group, C#, Excel ピボットテーブル
type: docs
weight: 90
url: /ja/net/discrete-group-pivot-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる使用例**
- 自動グループ化では、データ型に基づいて項目を分類します。たとえば、日付を月や四半期単位にまとめたり、数値を範囲に分けたりします。個別グループ化はこれとは逆に、特定の項目（互いに無関係な項目）を名前付きのカスタムグループにまとめます。たとえば、商品を果物と野菜に分類したり、店舗を地域別に分類したり、アカウントをゾーン別に分類したりします。Aspose.Cells は `DiscreteGroupItem` クラスと `PivotFieldGroupOptions.DiscreteGroupItems` プロパティを使用して個別グループ化を提供します。
- `DiscreteGroupItem` は、グループ名と、そのグループに属する項目から構成されます。項目は、名前（`new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" })`）またはソースデータ内の 0 始まりの位置（`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`）の 2 つの方法で識別できます。どちらの形式でも同じ結果になります。
- オプションを `PivotField.Group(PivotFieldGroupOptions)` に渡すことで、ピボットテーブルの行領域または列領域にあるフィールドに個別グループ化を適用できます。

## **項目名に基づいてピボットフィールド項目をグループ化する**
次の例では、小さな売上データ（商品、日付、金額）を作成し、`product` を行領域、`date` を列領域、`amount` をデータ領域に配置してピボットテーブルを作成します。その後、項目名に基づいて 2 つのカスタムグループ、すなわち果物（ぶどう、さくらんぼ）と野菜（にんじん、じゃがいも）を定義します。結果には、グループ名が外側のレベルに表示され、元の項目がその下にネストされた 2 階層の行レイアウトが作成されるため、カスタムグループ別および項目別に傾向を確認できます。

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

`CalculateData()` の後、ピボットテーブルの行領域には、果物（ぶどう 50、さくらんぼ 80）と野菜（にんじん 60、じゃがいも 70）が表示され、総計は 260 となります。列ラベルには、4 つの日付（2/5/2021、3/8/2022、4/10/2023、5/16/2024）がそのまま保持されます。

## **項目インデックスに基づいてピボットフィールド項目をグループ化する**
項目名が長い、またはローカライズされている場合は、`DiscreteGroupItem` の 2 番目のコンストラクターでは、インデックスを使って項目を識別します。インデックスは、項目がソースデータに現れる順序での 0 始まりの位置であり、アルファベット順ではありません。上記のサンプルデータでは、ぶどうが項目 0、にんじんが項目 1、じゃがいもが項目 2、さくらんぼが項目 3 となるため、果物は `{ 0, 3 }`、野菜は `{ 1, 2 }` です。結果は項目名に基づく例と同じです。

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

## **注記**

{{% alert color="primary" %}}
- カスタムグループに割り当てられていない項目も失われません。これらの項目はピボットテーブル内に残され、カスタムグループと同じレベルに、各項目が単独のエントリとして表示されます。上記の例では、果物グループだけを定義すると、にんじんとじゃがいもは行領域に残り、果物グループの隣に単独のエントリとして表示されます。
- `PivotFieldGroupOptions.NewPivotField` プロパティは、個別グループ化のレイアウトを制御します。デフォルト値は `true` で、元のフィールドの横にグループ化されたフィールドを新しい外側フィールドとして追加するため、上記の 2 階層レイアウトが作成されます（`RowFields` は 2 に増加します）。`false` に設定すると、代わりに元のフィールドが置き換えられます。この場合、行領域には、集計値を持つグループ名だけを含む 1 階層が表示され、果物は 130（50 + 80）、野菜は 130（60 + 70）となります。
- `DiscreteGroupItem` の名前に基づくコンストラクターとインデックスに基づくコンストラクターは、同じ `DiscreteGroupItems` 配列内で組み合わせることができます。
{{% /alert %}}

## **関連記事**
- [ピボットテーブル内でピボットフィールドをグループ化する](/cells/ja/net/group-pivot-fields-in-the-pivot-table/)
- [ピボットテーブルに行と列のフィールドを追加する](/cells/ja/net/pivot-table-add-row-and-column-fields/)
- [ラベルまたは値によるピボットテーブルのフィルター処理](/cells/ja/net/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルにスタイルを適用する](/cells/ja/net/apply-style-to-pivot-table/)
- [ピボットテーブルを更新する](/cells/ja/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}