---
title: ピボットテーブルの挿入
linktitle: ピボットテーブルの挿入
description: Excel スプレッドシートファイルのピボットテーブルを Aspose.Cells for Node.js via Java を使用して作成し、書式を設定します。
keywords: ピボットテーブルの作成, ピボットテーブルの挿入, ピボットテーブルの書式設定, Aspose.Cells for Node.js via Java.
type: docs
weight: 160
url: /ja/nodejs-java/create-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **ピボットテーブルとは**
ピボットテーブルは、対話式の集計レポートです。行ごとに記録された大量の生データを、数式を 1 つも使わずにコンパクトなマトリックスに要約します。どの列を行ラベルとし、どの列を列ラベルとし、どの列を値として集計するかを決定すると、ピボットテーブルがグループ化と計算を実行します。
- **要約** — 長い数式の連鎖を使う代わりに、製品別、地域別、四半期別の売上合計を表示します。
- **比較** — 行にカテゴリ、列に期間を配置すると、フラットな一覧がクロスレポートに変わり、傾向を一目で把握できます。
- **ドリルダウン** — 任意の集計値をダブルクリックすると、その背後にあるソース行を確認できます。
- **更新** — ソースデータが変更された場合も、1 回の更新でレポート全体を再計算できます。
一般的なユースケースとしては、販売ダッシュボード、経費の内訳、在庫分析があります。これらはいずれも、「これらの数値はカテゴリと時間軸でどのように細分化されるか」という形式の質問に応える用途です。Aspose.Cells for Node.js via Java は同じピボットテーブルをプログラムで構築するため、アプリケーションが生成するワークブックには、生データだけでなく、すぐに使用できるレポートを含めることができます。

### **ピボットテーブルのオブジェクトモデル**
Aspose.Cells は、ピボットテーブルの作成と操作に使用される一連のクラスを提供します。構成要素は次のとおりです。
- `PivotField` は、`PivotTable` 内のフィールドを表します。
- `PivotFieldCollection` は、`PivotTable` 内のすべての `PivotField` オブジェクトのコレクションを表します。
- `PivotTable` は、ワークシート上のピボットテーブルを表します。
- `PivotTableCollection` は、ワークシート上のすべての `PivotTable` オブジェクトのコレクションを表します。

### **Aspose.Cells を使用してシンプルなピボットテーブルを作成**
ピボットテーブルの作成は次の手順で行います。ソースデータをワークシートのセルに書き込み、宛先の位置にピボットテーブルを追加し、行領域、列領域、およびデータ領域にピボットフィールドを配置します。
1. セルの `putValue` メソッドを使用して、ワークシートにデータを追加します。このデータはピボットテーブルのデータソースとして使用されます。
2. `PivotTables` コレクションの `add` メソッドを呼び出して、ワークシートにピボットテーブルを追加します：`add(sourceData, row, column)`。`sourceData` はソース範囲（例: `"A1:C8"`）です。`row` と `column` は、配置先セル（ピボットテーブルの左上隅のセル）の 0 始点座標です（E3 セルは、行 2、列 4 を意味します）。このメソッドは、新しい `PivotTable` オブジェクトを直接返します。
3. `PivotTable` オブジェクトの `addFieldToArea` メソッドでピボットフィールドを配置します。指定したフィールド名を、行領域（`PivotFieldType.ROW`）、列領域（`PivotFieldType.COLUMN`）、またはデータ領域（`PivotFieldType.DATA`）のいずれかに配置します。
4. ワークブックを保存します。ピボットテーブルが保存済みのファイルに書き込まれます。
サンプルコードを実行すると、ワークシートにピボットテーブルが追加されます。

```javascript
const AsposeCells = require("aspose.cells");

// 新しいワークブックを作成し、最初のワークシートを取得します
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// ソースデータ（スポーツと四半期ごとの売上）を書き込みます
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

// A1:C8 をソースとして、宛先セル E3 にピボットテーブルを追加します
let pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// ピボットフィールドを割り当てます：Sport を行、Quarter を列、Sales をデータ領域に設定します
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Quarter");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");

// ワークブックを保存します
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
セル範囲をデータソースとして割り当てる場合、範囲は左上端から右下端への順で指定する必要があります。たとえば、`"A1:C3"` は有効ですが、`"C3:A1"` は無効です。
{{% /alert %}}

## 関連記事
- [Aspose.Cells for Node.js via Java を使用してピボットテーブルにフィルターフールドを追加](/cells/ja/nodejs-java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Node.js via Java を使用してピボットテーブルにスタイルを適用](/cells/ja/nodejs-java/apply-style-to-pivot-table/)
- [ピボットテーブルのページフィールドレイアウトを変更](/cells/ja/nodejs-java/change-page-field-layout/)
- [ラベルまたは値によるピボットテーブルのフィルタリング](/cells/ja/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Aspose.Cells for Node.js via Java を使用してピボットテーブルの値フィールドを管理](/cells/ja/nodejs-java/manage-value-fields/)

{{< app/cells/assistant language="nodejs-java" >}}