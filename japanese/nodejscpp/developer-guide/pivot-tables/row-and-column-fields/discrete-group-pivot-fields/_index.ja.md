---
title: ピボットフィールド項目の個別グループ化
linktitle: 個別グループ化
description: Aspose.Cells for Node.js via C++ で DiscreteGroupItem と PivotFieldGroupOptions.DiscreteGroupItems を使用して、フルーツや野菜などのカスタム名グループにピボットフィールド項目をグループ化する方法を学びます。
keywords: Aspose.Cells, ピボットテーブル, 個別グループ化, DiscreteGroupItem, PivotFieldGroupOptions, ピボット項目のグループ化, カスタムグループ, PivotField.Group, Node.js, Excel ピボットテーブル
type: docs
weight: 90
url: /ja/nodejs-cpp/discrete-group-pivot-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **利用シーン**
- 自動グループ化は、日付を月や四半期に、数値を範囲にまとめるなど、データ型ごとに項目を集めます。個別グループ化は、これとは逆に、特定の関連性のない項目をカスタム名グループにまとめます。たとえば、製品をフルーツと野菜に、店舗を地域に、アカウントをゾーンに分類します。Aspose.Cells for Node.js via C++ は、`DiscreteGroupItem` クラスと `PivotFieldGroupOptions.discreteGroupItems` プロパティを使用して個別グループ化を提供します。
- `DiscreteGroupItem` はグループ名とその項目の集合です。項目は名前で指定する方法（`new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" })`）またはソースデータ内のゼロベース位置で指定する方法（`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`）のいずれかで識別できます。両方の形式で同じ結果が得られます。
- 個別グループ化は、`pivotField.group(pivotFieldGroupOptions)` にオプションを渡すことで、ピボットテーブルの行領域または列領域にあるフィールドに適用されます。

## **項目名でピボットフィールド項目をグループ化**
以下の例は、販売リスト（商品、日付、金額）を作成し、`product` を行領域、`date` を列領域、`amount` をデータ領域に配置したピボットテーブルを生成し、項目名でカスタムグループ（フルーツ：grape、cherry、野菜：carrot、potato）を 2 つ定義します。結果は 2 レベルの行レイアウトとなり、外側がグループ名、内側が元の項目となって、カスタムグループごと・項目ごとの傾向が読み取れます。

```javascript
const AsposeCells = require("aspose.cells.node");
// Create a new workbook and get the first worksheet
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
// Populate data
cells.get(0, 0).setValue("product");
cells.get(1, 0).setValue("grape");
cells.get(2, 0).setValue("carrot");
cells.get(3, 0).setValue("potato");
cells.get(4, 0).setValue("cherry");
// Create a date style
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
// Add date header and values
cells.get(0, 1).setValue("date");
cells.get(1, 1).setValue(new Date(2021, 1, 5));   // February is month 1
cells.get(2, 1).setValue(new Date(2022, 2, 8));
cells.get(3, 1).setValue(new Date(2023, 3, 10));
cells.get(4, 1).setValue(new Date(2024, 4, 16));
// Apply date style to the date column
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
// Add amount header and values
cells.get(0, 2).setValue("amount");
cells.get(1, 2).setValue(50);
cells.get(2, 2).setValue(60);
cells.get(3, 2).setValue(70);
cells.get(4, 2).setValue(80);
// Add a pivot table at cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleMedium10);
// Group specific items into custom groups by item names
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems([fruit, vegetable]);
pivotTable.getRowFields().get(0).group(groupOptions);
// Calculate pivot data and save the workbook
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

`calculateData()` 後、ピボットテーブルの行領域にはフルーツ（grape 50、cherry 80）と野菜（carrot 60、potato 70）が表示され、合計は 260 です。列ラベルは 4 つの日付（2/5/2021、3/8/2022、4/10/2023、5/16/2024）を保持します。

## **項目インデックスでピボットフィールド項目をグループ化**
項目名が長い、またはローカライズされている場合は、`DiscreteGroupItem` の第 2 コンストラクタでインデックスで項目を指定します。インデックスはソースデータ内で項目が出現する順序のゼロベース位置であり、アルファベット順ではありません。上記サンプルデータでは、grape が 0、carrot が 1、potato が 2、cherry が 3 になるため、フルーツは `{ 0, 3 }`、野菜は `{ 1, 2 }` となります。結果は名前ベースの例と同一です。

```javascript
const AsposeCells = require("aspose.cells.node");
// Create workbook and get first worksheet
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
// Fill data
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
// Create a date style
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
// Date column header
cells.get(0, 1).putValue("date");
// Date values
cells.get(1, 1).putValue(new Date(2021, 1, 5));   // Feb 5, 2021
cells.get(2, 1).putValue(new Date(2022, 2, 8));   // Mar 8, 2022
cells.get(3, 1).putValue(new Date(2023, 3, 10));  // Apr 10, 2023
cells.get(4, 1).putValue(new Date(2024, 4, 16));  // May 16, 2024
// Apply date style to date cells
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
// Amount column header and values
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleMedium10);
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data)
const fruit = new AsposeCells.DiscreteGroupItem("fruit", [0, 3]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", [1, 2]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems([fruit, vegetable]);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
// Save the workbook
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **注意**

{{% alert color="primary" %}}
- カスタムグループに割り当てられなかった項目は失われません。元のフィールドと同じレベルに単一項目として残ります。上記の例では、フルーツグループだけを定義した場合、carrot と potato が行領域にスタンドアロンのエントリとしてフルーツグループの横に表示されます。
- `PivotFieldGroupOptions.newPivotField` プロパティは個別グループ化のレイアウトを制御します。デフォルトは true で、元のフィールドの横に新しい外側フィールドとしてグループ化されたフィールドを追加し、上記のような 2 レベルレイアウト（`rowFields` が 2 に増加）になります。false に設定すると元のフィールドを置き換え、行領域はグループ名のみの単一レベルとなり、フルーツは 130（50 + 80）、野菜は 130（60 + 70）と集計されます。
- `DiscreteGroupItem` の名前ベースとインデックスベースのコンストラクタは、同一の `PivotFieldGroupOptions.discreteGroupItems` 配列内で混在させることができます。
{{% /alert %}}

## **関連記事**
- [ピボットテーブルでピボットフィールドをグループ化](/cells/ja/nodejs-cpp/group-pivot-fields-in-the-pivot-table/)
- [ピボットテーブルに行フィールドと列フィールドを追加](/cells/ja/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [ラベルまたは値でピボットテーブルをフィルタリング](/cells/ja/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルにスタイルを適用](/cells/ja/nodejs-cpp/apply-style-to-pivot-table/)
- [ピボットテーブルをリフレッシュ](/cells/ja/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}