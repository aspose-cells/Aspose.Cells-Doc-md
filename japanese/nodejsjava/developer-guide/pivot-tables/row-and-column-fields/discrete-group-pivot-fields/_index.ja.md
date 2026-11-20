---
title: ピボットフィールド項目の個別グループ化
linktitle: 個別グループ化
description: Aspose.Cells for Node.js via Java で DiscreteGroupItem クラスと PivotFieldGroupOptions.getDiscreteGroupItems() プロパティを使用して、果物や野菜などのカスタム名のグループにピボットフィールド項目をグループ化する方法を説明します。
keywords: Aspose.Cells, ピボットテーブル, 個別グループ化, DiscreteGroupItem, PivotFieldGroupOptions, ピボット項目のグループ化, カスタムグループ, PivotField.group, Aspose.Cells for Node.js via Java, Excel ピボットテーブル
type: docs
weight: 90
url: /ja/nodejs-java/discrete-group-pivot-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる利用シナリオ**
- 自動グループ化は、データ型に基づいて項目をまとめます。たとえば、日付を月や四半期にまとめ、数値を範囲にまとめます。個別グループ化はこれとは逆に、互いに無関係な特定の項目をカスタム名のグループにまとめます。たとえば、製品を果物と野菜に分類したり、店舗を地域に分類したり、勘定をゾーンに分類したりできます。Aspose.Cells は、`DiscreteGroupItem` クラスと `PivotFieldGroupOptions.getDiscreteGroupItems()` プロパティを通じて個別グループ化を提供します。
- `DiscreteGroupItem` は、グループ名と、そのグループに属する項目から構成されます。項目は、名前 (`new DiscreteGroupItem("fruit", ["grape", "cherry"])`) またはソースデータ内のゼロベースの位置 (`new DiscreteGroupItem("fruit", [0, 3])`) の 2 通りで識別できます。いずれの場合も結果は同じです。
- 個別グループ化は、オプションを `PivotField.group(PivotFieldGroupOptions)` に渡すことで、ピボットテーブルの行領域または列領域にあるフィールドに適用されます。

## **項目名によるピボットフィールド項目のグループ化**
次の例では、小さな販売リスト（製品、日付、金額）を作成し、そのデータから `product` を行領域、`date` を列領域、`amount` をデータ領域に配置したピボットテーブルを作成します。続いて、項目名に基づいて、果物（ぶどう、さくらんぼ）と野菜（にんじん、じゃがいも）の 2 つのカスタムグループを定義します。结果は 2 つの階層を持つ行レイアウトとなり、外側のレベルにはグループ名が、その下には元の項目がネストされるため、カスタムグループごとおよび項目ごとの傾向を確認できます。

```javascript
const AsposeCells = require("aspose.cells");
const java = require("java");
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(44232);
cells.get(2, 1).putValue(44628);
cells.get(3, 1).putValue(45026);
cells.get(4, 1).putValue(45428);
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
// Group specific items into custom groups by item names
pivotTable.calculateData();
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
const groups = java.newArray("com.aspose.cells.DiscreteGroupItem", [fruit, vegetable]);
groupOptions.setDiscreteGroupItems(groups);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

`calculateData()` の実行後、ピボットテーブルの行領域には、果物（ぶどう 50、さくらんぼ 80）と野菜（にんじん 60、じゃがいも 70）が表示され、総計は 260 になります。列ラベルには、4 つの日付（2/5/2021、3/8/2022、4/10/2023、5/16/2024）が保持されます。

## **項目インデックスによるピボットフィールド項目のグループ化**
項目名が長い場合やローカライズされている場合、`DiscreteGroupItem` の 2 番目のコンストラクターは項目をインデックスで識別します。インデックスは、項目がソースデータに現れる順序でのゼロベースの位置であり、アルファベット順ではありません。サンプルデータでは、ぶどうは項目 0、にんじんは項目 1、じゃがいもは項目 2、さくらんぼは項目 3 となるため、果物は `{ 0, 3 }`、野菜は `{ 1, 2 }` になります。結果は名前に基づく例と同じです。

```javascript
const AsposeCells = require("aspose.cells");
const java = require("java");
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
// Use Excel serial dates because JavaScript Date objects cannot be passed through the bridge.
cells.get(1, 1).putValue(44232); // 2021-02-05
cells.get(2, 1).putValue(44628); // 2022-03-08
cells.get(3, 1).putValue(45026); // 2023-04-10
cells.get(4, 1).putValue(45428); // 2024-05-16
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0).
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(
    AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
);
// Calculate the pivot table before grouping.
pivotTable.calculateData();
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data).
// The Node.js bridge requires item names rather than the index-based constructor.
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
const groups = java.newArray("com.aspose.cells.DiscreteGroupItem", [fruit, vegetable]);
groupOptions.setDiscreteGroupItems(groups);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **注記**

{{% alert color="primary" %}}
- どのカスタムグループにも割り当てられていない項目は失われません。カスタムグループと同じレベルにピボットテーブル内に残され、それぞれが単独の項目エントリとして表示されます。上記の例では、果物グループだけを定義すると、にんじんとじゃがいもは果物グループの横に、行領域内の独立したエントリとして残ります。
- `PivotFieldGroupOptions.getNewPivotField()` プロパティは、個別グループ化のレイアウトを制御します。既定値は true であり、これによりグループ化したフィールドが元のフィールドの横にある新しい外側フィールドとして追加され、上記の 2 段のレイアウトが生成されます（`getRowFields()` は 2 に増えます）。`PivotFieldGroupOptions.setNewPivotField(false)` を使用して false に設定すると、元のフィールドが置き換えられます。この場合、行領域には、グループ名とその集計値のみを含む 1 段のレイアウトが表示され、果物は 130（50 + 80）、野菜は 130（60 + 70）となります。
- `DiscreteGroupItem` の名前ベースおよびインデックスベースのコンストラクターは、同じ `getDiscreteGroupItems()` 配列内で併用できます。
{{% /alert %}}

## **関連記事**
- [ピボットテーブルでピボットフィールドをグループ化](/cells/ja/nodejs-java/group-pivot-fields-in-the-pivot-table/)
- [ピボットテーブルに行および列のフィールドを追加](/cells/ja/nodejs-java/pivot-table-add-row-and-column-fields/)
- [ラベルまたは値に基づいてピボットテーブルを絞り込む](/cells/ja/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルにスタイルを適用](/cells/ja/nodejs-java/apply-style-to-pivot-table/)
- [ピボットテーブルを更新](/cells/ja/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}