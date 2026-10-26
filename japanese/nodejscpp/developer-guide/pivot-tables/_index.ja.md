---
title: ピボットテーブルの挿入
linktitle: ピボットテーブルの挿入
description: Aspose.Cells for Node.js via C++ を使用して、ピボットテーブルを作成し、書式を設定します。
keywords: ピボットテーブルの作成, ピボットテーブルの挿入, ピボットテーブルの書式設定.
type: docs
weight: 160
url: /ja/nodejs-cpp/create-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **ピボットテーブルとは？**
ピボットテーブルは、インタラクティブなサマリーレポートです。行ごとに並ぶ大量な生データを、数式を一切使わずにコンパクトなマトリックスへまとめられます。どの列を行ラベル、列ラベル、または集計値として使用するかを自由に選択でき、グループ化と集計はピボットテーブルが行います。
- **集計** — 長い数式チェーンを使用せず、製品別、地域別、四半期別に売上合計を集計できます。
- **比較** — 行にカテゴリを、列に期間を配置すると、平坦なリストをクロスレポートに変換でき、傾向を一目で確認できます。
- **詳細表示** — 任意の集計値をダブルクリックすると、その背後にある元の行を確認できます。
- **更新** — 元データが変更された場合も、更新を一度行うだけでレポート全体を再計算できます。
典型的な用途として、売上ダッシュボード、経費の内訳、在庫分析などが挙げられます。「これらの数値をカテゴリや期間ごとにどう内訳として示するか」という種類の質問に、コンパクトなピボットテーブルが適しています。Aspose.Cells for Node.js via C++ を使用すると、同じピボットテーブルをプログラムで作成できます。そのため、アプリケーションが生成するワークブックには、生データだけでなくすぐに使えるレポートを含めることができます。

### **ピボットテーブルのオブジェクトモデル**
Aspose.Cells for Node.js via C++ には、ピボットテーブルの作成と制御に特化した一連のクラスが提供されます。これらのクラスは、ピボットテーブルの構成要素である [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) オブジェクトの作成と設定に使用されます。オブジェクトは次のとおりです。
- [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) は、[**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) 内のフィールドを表します。
- [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection) は、[**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) 内にあるすべての [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) オブジェクトのコレクションを表します。
- [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) は、ワークシート上のピボットテーブルを表します。
- [**PivotTableCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) は、ワークシート上にあるすべての [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) オブジェクトのコレクションを表します。

### **Aspose.Cells を使用してシンプルなピボットテーブルを作成**
ピボットテーブルの作成は次の手順で行います。ワークシートのセルにソースデータを書き込み、宛先位置にピボットテーブルを追加して、ピボットフィールドを行、列、データ領域に配置します。
1. [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) オブジェクトの [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) メソッドを使用して、ワークシートのセルにデータを追加します。このデータはピボットテーブルのデータソースとして使用されます。
2. [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) コレクションの [**add**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#add-string-string-string-) メソッドを呼び出して、ワークシートにピボットテーブルを追加します。メソッドの形式は `add(sourceData, row, column)` です。`sourceData` はソース範囲（例: "A1:C8"）です。`row` と `column` は、ピボットテーブルの左上角となる宛先セルの 0 始まりの座標です（セル E3 の場合、`row` は 2、`column` は 4 を表します）。このメソッドは、新しい [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) オブジェクトを直接返します。
3. [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) オブジェクトの `addFieldToArea` メソッドでピボットフィールドを配置します。フィールド名を指定すると、行領域 (`PivotFieldType.Row`)、列領域 (`PivotFieldType.Column`)、またはデータ領域 (`PivotFieldType.Data`) に配置できます。
4. ワークブックを保存します。ピボットテーブルは保存されたファイルに書き込まれます。
例コードを実行すると、ワークシートにピボットテーブルが追加されます。

```javascript
const AsposeCells = require("aspose.cells.node");

// 新しいワークブックを作成し、最初のワークシートを取得する
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// ソースデータ（スポーツと四半期ごとの売上）を書き込む
sheet.getCells().get("A1").putValue("Sport");
sheet.getCells().get("B1").putValue("Quarter");
sheet.getCells().get("C1").putValue("Sales");
sheet.getCells().get("A2").putValue("Golf");
sheet.getCells().get("B2").putValue("Qtr3");
sheet.getCells().get("C2").putValue(1500);
sheet.getCells().get("A3").putValue("Golf");
sheet.getCells().get("B3").putValue("Qtr4");
sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Tennis");
sheet.getCells().get("B4").putValue("Qtr3");
sheet.getCells().get("C4").putValue(600);
sheet.getCells().get("A5").putValue("Tennis");
sheet.getCells().get("B5").putValue("Qtr4");
sheet.getCells().get("C5").putValue(1500);
sheet.getCells().get("A6").putValue("Tennis");
sheet.getCells().get("B6").putValue("Qtr3");
sheet.getCells().get("C6").putValue(4070);
sheet.getCells().get("A7").putValue("Tennis");
sheet.getCells().get("B7").putValue("Qtr4");
sheet.getCells().get("C7").putValue(5000);
sheet.getCells().get("A8").putValue("Golf");
sheet.getCells().get("B8").putValue("Qtr3");
sheet.getCells().get("C8").putValue(6430);

// A1:C8 をソースとして、宛先セル E3 にピボットテーブルを追加する
let pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// ピボットフィールドを割り当てる：Sport を行、Quarter を列、Sales をデータ領域に配置
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Quarter");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");

// ワークブックを保存する
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
セル範囲をデータソースとして割り当てる場合、範囲は左上端から右下端に向かって指定する必要があります。たとえば、"A1:C3" は有効ですが、"C3:A1" は無効です。
{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}