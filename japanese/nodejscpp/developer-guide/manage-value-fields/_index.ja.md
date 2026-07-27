---
title: Aspose.Cells for Node.js via C++ の値フィールド
linktitle: Aspose.Cells for Node.js via C++ の値フィールド
description: Aspose.Cells for Node.js via C++ で、ピボットテーブルのデータ領域に基本フィールドを追加する方法、PivotField.Function で集計関数を変更する方法、値フィールドを行または列軸にプロットする方法を学びます。
keywords: Aspose.Cells, Node.js, C++, ピボットテーブル, 値フィールド, PivotField, PivotField.Function, データフィールド, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ja/nodejs-cpp/manage-value-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
値フィールドはすべてのピボットテーブルの中心であり、ソースデータを集計する数値フィールドです。Aspose.Cells for Node.js via C++ では、ピボットテーブルのデータ領域に `PivotTable.addFieldToArea` を通じて基本フィールドを追加することでデータを配置し、その領域に配置された各フィールドは独自の集計関数を持つことができます。2つ以上のデータフィールドが存在する場合、Aspose.Cells は `PivotTable.ValuesField` という特別な集計フィールドを公開しており、これを行または列軸に基本フィールドとしてプロットすることで、レイアウトにおける値フィールドの表示方法を細かく制御できます。
## データ領域へのフィールドの追加
データ（値）領域に基本フィールドを追加することは、ピボットテーブルがソースデータを集計する方法を形作る最初のステップです。Aspose.Cells は `PivotTable.addFieldToArea(PivotFieldType, string)` を提供しており、これは定数 `PivotFieldType.Data` とソース列名を受け取るオーバーロードです。データ領域にフィールドが追加されると、API はそれを `PivotTable.DataFields` コレクションを通じてフィールドが追加された順序で公開します。デフォルトでは、数値のソース列は `ConsolidationFunction.Sum` で集計され、非数値の列は `Count` がデフォルトになります。
## 集計関数の変更
データ領域に配置された各フィールドは内部的に `PivotField` インスタンスとしてラップされ、その `Function` プロパティは `ConsolidationFunction` 列挙体の値を返します。同じ `Function` セッターを使用すると、`Sum`、`Count`、`Average`、`Max`、`Min`、`Product`、`StdDev`、`StdDevp`、`Var`、`Varp` などの利用可能な集計関数に切り替えることができます。
{{% alert color="primary" %}}
`Function` を変更しても集計にのみ影響し、ソース列は変更されません。
{{% /alert %}}
したがって、1つのデータフィールドを `Sum` のままにして、同じソース列を対象とするが `Count` または `Average` を使用する2つ目のデータフィールドを、1つのピボット内で追加することができます。
## 行または列軸への値フィールドのプロット
ピボットテーブルに2つ以上のデータフィールドが含まれている場合、Aspose.Cells は `PivotTable.ValuesField` という追加の仮想フィールドを公開します。この仮想フィールドは、データ領域に存在するすべてのデータフィールドの集計を表します。これを基本ピボットフィールドとして行領域または列領域にドラッグすることができ、複数のメジャーを並べてレイアウトする場合に便利です。
{{% alert color="primary" %}}
値フィールドが存在しないか1つしかない場合、`PivotTable.ValuesField` は機能しません。
{{% /alert %}}
以下のシナリオでは、同じピボット構造に対して上記で説明した各機能を実証する3つのエンドツーエンドの例を順を追って説明します。
## シナリオ1 — 基本フィールドを値領域にドラッグする
このシナリオでは、既存のピボットテーブルのデータ領域に1つの基本フィールド（`Amount`）を配置する方法を示します。共有のピボット構造では、`Category` と `Item` を行軸に、`Year` を列軸に配置します。操作後、`Amount` はデータ領域に表示され、デフォルトで `Amount` の `Sum` として計算されます。
```javascript
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// A1:D1 のヘッダー
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// A2:D9 のデータ行（j で分岐するネストされたループを使用）
for (let i = 1; i <= 8; i++) {
  for (let j = 0; j < 4; j++) {
    switch (j) {
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

// F3 に PivotTable1 という名前のピボットテーブルを追加
let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// ピボットレイアウト：Category と Item を行、Year を列、Amount をデータフィールド
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

pivotTable.refreshData();
pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```
## シナリオ2 — 集計関数の変更
このシナリオはシナリオ1と同じピボット構造から始まり、データ領域に `Amount` フィールドを2回追加します。両方のデータフィールドは同じソース列を参照しますが、2番目のフィールドは `PivotField.Function` セッターを使用して上書きされ、デフォルトの `Sum` ではなく `Count` になります。
```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

for (let i = 1; i <= 8; i++)
{
    for (let j = 0; j <= 3; j++)
    {
        if (j == 0)
        {
            worksheet.getCells().get(i, j).putValue(i <= 5 ? "Fruit" : "Vegetable");
        }
        else if (j == 1)
        {
            let items = ["Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon"];
            worksheet.getCells().get(i, j).putValue(items[i - 1]);
        }
        else if (j == 2)
        {
            let years = [2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021];
            worksheet.getCells().get(i, j).putValue(years[i - 1]);
        }
        else
        {
            let amounts = [100, 150, 80, 90, 50, 60, 40, 45];
            worksheet.getCells().get(i, j).putValue(amounts[i - 1]);
        }
    }
}

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let countField = pivotTable.getDataFields().get(1);
countField.setFunction(AsposeCells.ConsolidationFunction.Count);

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_function.xlsx");
```
## シナリオ3 — 行または列軸への値フィールドのプロット
2つのデータフィールドが配置されていると、`PivotTable.ValuesField` が利用可能になります。このシナリオでは、その集計仮想フィールドを列領域にドラッグし、データ領域の各メジャーが `Year` の隣に独自の列ブロックとして表示されるようにします。
これら3つのシナリオを合わせると、デフォルトの `Sum` を持つ単一のデータフィールドから、仮想 `ValuesField` が行または列軸のレイアウトを制御する複数メジャーのピボットまで、Aspose.Cells for Node.js via C++ における値フィールド操作のあらゆる側面を網羅しています。
## 関連記事
- [Aspose.Cells for Node.js via C++ のピボットテーブル行と列フィールド](/cells/ja/nodejs-cpp/row-and-column-fields/)
- [ピボットテーブルのページフィールド](/cells/ja/nodejs-cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for Node.js via C++ でピボットテーブルを更新する](/cells/ja/nodejs-cpp/refresh-pivot-table/)
- [ピボットテーブルへのスタイルの適用](/cells/ja/nodejs-cpp/apply-style-to-pivot-table/)
{{< app/cells/assistant language="javascript" >}}