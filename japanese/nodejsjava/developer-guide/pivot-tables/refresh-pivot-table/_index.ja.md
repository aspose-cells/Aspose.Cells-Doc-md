---
title: Refreshing Pivot Tables in Aspose.Cells for Node.js via Java
linktitle: Refreshing Pivot Tables
description: Learn how to refresh pivot tables in Aspose.Cells for Node.js via Java using the v26.7+ pivot-refresh API. This article covers RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData, and GetPivotTables with practical code examples.
keywords: Aspose.Cells, Node.js, Java, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ja/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は、ワークブック全体から単一のピボットテーブルまで、4 つの異なるスコープでピボットデータを再読み込みできる階層化された更新 API を提供します。**Aspose.Cells for Node.js via Java v26.7** 以降、従来の `PivotTable.RefreshData()` メソッドは非推奨となり、この記事で説明するより効率的なキャッシュ対応 API に置き換える必要があります。

{{% /alert %}}

## はじめに

ピボットテーブルの更新は、単一の操作であることはまれです。Aspose.Cells は内部で、元のソースデータからワークシートに表示されるレンダリング済みの値までを結ぶ階層化されたデータチェーンを管理しています。このチェーンを理解することが、あらゆる状況に適した更新 API を選択する鍵となります。

4 層のデータチェーンは以下のとおりです。

1. **データソース** — 元のワークシート範囲、データベースクエリ、または生の値が格納されている統合範囲。
2. **PivotCache** — ソースデータのインメモリスナップショット。すべてのピボットテーブルは `PivotCache` の上に構築され、すべてのデータの収集と集計はここで行われます。
3. **PivotTable** — 行、列、値、フィルタのフィールドを定義するビューオブジェクト。`PivotTable` はデータソースからではなく、`PivotCache` からのみデータを読み取ります。
4. **セル** — `PivotTable` が計算済みの値と書式をレンダリングする先のワークシートの `Cells`。

特に重要な概念は **共有キャッシュ** です。ワークブック内の複数のピボットテーブルが同じソース範囲を参照している場合、それらは *1つの* `PivotCache` インスタンスを共有します。1 つの `PivotCache` は多くのピボットテーブルから参照されることがあり、そのキャッシュを更新すると、依存するすべての `PivotTable` が一度に更新されます。

{{% alert color="primary" %}}

`PivotCache.SourceType`（列挙型 `PivotTableSourceType`）は、キャッシュデータの取得元を示します。v26.7 時点で、`PivotCache.Refresh()` は **`Sheet`** と **`Consolidation`** のソースタイプ、つまりワークシート範囲に存在するデータのみをサポートしています。外部ソース（データベースや外部接続など）は、まだキャッシュ API からは更新できません。

{{% /alert %}}

このチェーンにより、Aspose.Cells には 2 つの基本的な更新パスがあります。

- **`PivotCache.Refresh()`** — ソースからキャッシュへの再読み込みと、それに依存するすべての `PivotTable` の再計算を単一の操作で実行します。
- **`PivotTable.CalculateData()`** — 既にキャッシュされているデータから、1 つの `PivotTable` の表示を再計算します。データソースへのラウンドトリップはありません。

この記事のすべてのシナリオではワークシートセルのソースデータを使用しているため、ソースタイプは `Sheet` となり、更新操作は説明どおりに動作します。

## 必要なインポート

この記事のすべての JavaScript の例では、Aspose.Cells for Node.js via Java モジュールが必要です。ピボット関連の型は `Aspose.Cells.Pivot` 名前空間にあり、同じモジュールの一部です。

- `const aspose = require('aspose.cells');`
- または特定のインポートの場合：`const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`

## ワークブック内のすべてのピボットテーブルを更新する

ワークブック内のすべてのピボットキャッシュとすべてのピボットテーブルが最新のソースデータを反映するようにする必要がある場合、最もシンプルで包括的な API は `Workbook.RefreshAll()` です。1 回の呼び出しでワークブック全体を走査し、各 `PivotCache` をソースから更新し、続いて依存するすべての `PivotTable` を再計算します。これは、パフォーマンスが懸念されない一般的なドキュメント全体の更新に推奨されるアプローチです。

次の例では、Fruit/Year/Amount のソース範囲を含むワークブックを作成し、1 つのピボットテーブルを追加し、一部のソース値を変更した後、`RefreshAll()` を使用してすべてを 1 回の呼び出しで最新の状態にします。

```javascript
const AsposeCells = require("aspose.cells");

// 新しいワークブックを作成
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// A1:C1のセルにヘッダー行を書き込み
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// A2:C9のセルにデータ行を書き込み（2020年と2021年にわたる8行の果物データ）
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(50);

worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(60);

worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(70);

worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(80);

worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(90);

worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(100);

worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(110);

worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(120);

// ピボットテーブルを追加：ソース範囲 "A1:C9"、配置先セル "E3"、名前 "Pivot1"
const pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

// ピボットフィールドを割り当て：Fruitを行、Yearを列、Amountをデータ
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// ソースデータのAmount値をいくつか変更して更新をシミュレート
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// ワークブック内のすべてのピボットテーブル / ピボットキャッシュを更新
workbook.refreshAll();

// ワークブックを保存
workbook.save("output.xlsx");
```

## 単一のワークシート上のすべてのピボットテーブルを更新する

場合によっては、特定の 1 つのワークシートに存在するピボットテーブルのみを更新する必要があります。たとえば、他のワークシート上のピボットテーブルは無関係であり、触れたくないことが分かっている場合です。このような場合のために、Aspose.Cells は単一の `Worksheet` インスタンスを対象とした `Worksheet.RefreshPivotTables()` を提供しています。

これは `Workbook.RefreshAll()` よりも選択的であり、対象のワークシート上のピボットテーブルのみが更新され、他のワークシート上のピボットテーブルには影響しません。

次の例では、同じ Fruit/Year/Amount のソースデータを設定し、最初のワークシートにピボットテーブルを追加し、一部のソース値を変更した後、そのワークシート上のピボットテーブルのみを更新します。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2021);
worksheet.getCells().get("C3").putValue(150);

worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);

worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2021);
worksheet.getCells().get("C5").putValue(120);

worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(180);

worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2020);
worksheet.getCells().get("C7").putValue(130);

worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(220);

worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2020);
worksheet.getCells().get("C9").putValue(140);

let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);

worksheet.refreshPivotTables();

workbook.save("output.xlsx");
```

## 単一のピボットテーブルを更新する

単一のピボットテーブルを細かく制御したい場合、キャッシュベースの API は 2 つの選択肢を提供します。どちらを選ぶかは、実際に何が変わったか（基になるソースデータなのか、それともピボットテーブル自体のビュー/レイアウト設定のみなのか）によって異なります。

### ソースデータが変更された場合 — `PivotCache.Refresh()` を使用する

基になるソースデータが変更された場合、正しいエントリポイントは `pivotTable.PivotCache.Refresh()` です。この呼び出しは、ソースデータをキャッシュに再読み込みし、そのキャッシュに依存するすべての `PivotTable` を再計算します。

{{% alert color="primary" %}}

ピボットテーブルは単一の `PivotCache` インスタンスを共有するため、`PivotCache.Refresh()` を呼び出すと、参照したピボットテーブルだけでなく、その同じキャッシュ上に構築された **すべての** ピボットテーブルが再計算されます。2 つのピボットテーブルが同じソース範囲を共有している場合、1 つのキャッシュを更新すると両方が更新されます。

{{% /alert %}}

次の例では、同じソース範囲上に 2 つのピボットテーブルを作成し、この共有キャッシュの動作を実証し、一部のソース値を変更した後、1 つのキャッシュ参照を通じて更新します。

```javascript
const AsposeCells = require("aspose.cells");

// 新しいワークブックを作成し、最初のワークシートにアクセスする
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// ヘッダー行を書き込む: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 約9行のデータ行を書き込む（2020～2021年の grape / blueberry / kiwi / cherry）
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

// セル E3 に配置される最初のピボットテーブル "Pivot1" を追加する。ソース範囲は A1:C9
const pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// Pivot1 のフィールドを割り当てる
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 同じソース範囲 A1:C9 を使用して、E15 に配置される2番目のピボットテーブル "Pivot2" を追加する
// ソース範囲が同一であるため、Pivot1 と Pivot2 は単一の PivotCache を共有する。
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Pivot2 に同じフィールドを割り当てる
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// ソースデータの複数の Amount セルの値を変更してデータの変更をシミュレートする
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// 共有 PivotCache を更新する。
// Pivot1 と Pivot2 は同じ PivotCache を共有しているため、この1回の呼び出しで
// 両方のピボットテーブル（データとスタイル）を更新されたソースから更新する。
pivotTable1.getPivotCache().refresh();

// ワークブックを保存する
workbook.save("output.xlsx");
```

### ビュー/レイアウトのみが変更された場合 — `CalculateData()` を使用する

ソースデータは変更されておらず、ピボットテーブルのビューまたはレイアウト設定のみが変更された場合（たとえば、フィールドが別のエリアに移動された、またはファイルを開いたときに更新する設定が切り替えられた場合）、データソースへのラウンドトリップは必要ありません。キャッシュにはすでに正しいデータが保持されており、レンダリング済みの `PivotTable` を再計算するだけで済みます。この場合、`pivotTable.CalculateData()` が正しい選択です。

これにより、不要なソースフェッチが回避され、多くのピボットテーブルが同じキャッシュを共有している場合に大幅に高速化されます。

次の例では、ピボットテーブルのソース以外のプロパティを変更し、その後 `CalculateData()` を呼び出して既存のキャッシュから再レンダリングします。

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// フルーツ / 年 / 金額のヘッダー行を書き込む
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 8行のデータ(2〜9行目、ソース範囲A1:C9に収まる)を書き込む
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(150);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(250);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(350);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(450);

// 出力先セルE3に配置される「Pivot1」という名前のピボットテーブルを追加し、A1:C9をソースとする
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// フィールドを割り当てる:Fruitは行、Yearは列、Amountはデータ
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 表示/レイアウトのプロパティを変更する — これは表示のみの変更であるため、
// PivotCache.Refresh() を介してソースデータを再読み込みする必要はない
pivotTable.setRefreshDataOnOpeningFile(false);

// calculateData() は、PivotCache に保持されているデータからこのピボットテーブルの表示
// (データ + スタイル)を再レンダリングする。ソースデータは変更されていないため、
// ソースへのラウンドトリップは行われず、キャッシュされた値がワークシートセルに
// 再計算されるだけである
pivotTable.calculateData();

// ワークブックをディスクに保存する
workbook.save("output.xlsx");
```

## 同じ PivotCache を共有するすべてのピボットテーブルを取得する

ワークブックには、1 つの共有キャッシュの上に存在する多数のピボットテーブルが含まれていることがよくあります。これらを列挙する場合（たとえば、一括更新を実行する前や、共有キャッシュの影響を診断するため）には、`PivotCache.GetPivotTables()` を使用します。このメソッドは、指定されたキャッシュに依存するすべての `PivotTable` のコレクションを返します。

これは、2 つのピボットテーブルが実際に同じ `PivotCache` インスタンスを共有していることを確認するための最も直接的な方法でもあります。キャッシュ参照を比較するか、`GetPivotTables()` が返したコレクションを単純に反復処理して、どのピボットテーブルが含まれているかを確認できます。

次の例では、同じソース範囲上に 2 つのピボットテーブルを作成し、それらが同じキャッシュインスタンスを共有していることを確認し、キャッシュのピボットテーブルを列挙します。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Sheet1");

worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);

let pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = worksheet.getPivotTables().get(pivot1Index);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let sameCache = pivotTable1.getPivotCache() === pivotTable2.getPivotCache();
console.log("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

let sharedPivotTables = pivotTable1.getPivotCache().getPivotTables();
console.log("Number of pivot tables sharing the cache: " + sharedPivotTables.length);

for (let pt of sharedPivotTables) {
    console.log("Pivot table name: " + pt.getName());
}

workbook.save("output.xlsx");
```

## 非推奨の `PivotTable.RefreshData()` からの移行

Aspose.Cells for Node.js via Java v26.7 より前では、ピボットテーブルを更新する標準的な方法は、各ピボットテーブルに対して個別に `PivotTable.RefreshData()` を呼び出すことでした。v26.7 以降、このメソッドは **非推奨** とマークされ、上記のキャッシュ対応 API に置き換える必要があります。

実際のワークブックでは、テーブルごとの `RefreshData()` アプローチに問題がある理由は 2 つあります。

- ソースが変更されていない場合でも、呼び出すたびにソースからデータを再取得します。
- 各呼び出しは共有キャッシュ全体を更新します。多くのピボットテーブルが 1 つのキャッシュを共有している場合、ピボットテーブルごとに `RefreshData()` を繰り返し呼び出すと、同じキャッシュが何度も再取得され、非常に低速になります。

推奨される代替手段は次のとおりです。

- **ワークブック内のすべてのピボットテーブルを更新する** → `workbook.refreshAll();` を使用する
- **一部のみを更新する** → 1 つのキャッシュに対して `pivotTable.getPivotCache().refresh();` を使用する。キャッシュは共有されているため、この 1 回の呼び出しでそのキャッシュ上に構築されたすべてのピボットテーブルが更新されます。すでに更新済みのキャッシュ上に存在する他のピボットテーブルは、安全にスキップできます。
- **ピボットビュー/レイアウトのみが変更された場合** → ソースへのラウンドトリップなしで既存のキャッシュから再レンダリングするために `pivotTable.calculateData();` を使用する

次の例では、単一のキャッシュを共有する複数のピボットテーブルを持つワークブックの新しい効率的なパターンを示します。

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- ソースデータの作成: 果物 / 年 / 金額 (ヘッダー + 9 行) ---
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000);
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500);
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500);
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000);
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800);
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200);
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700);

// --- 出力先セル E3 に最初のピボットテーブル (Pivot1) を追加 ---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- 同じソース範囲に 2 つ目のピボットテーブル (Pivot2) を追加 ---
// Pivot1 と Pivot2 は両方とも 1 つの基礎となる PivotCache を共有します。
// これは、レガシーのテーブルごとの RefreshData() 方式が非効率になるまさにそのシナリオです
// 1 つのテーブルを更新すると共有キャッシュ全体を再度取得するため、
// N 個のテーブルを更新すると、その高コストな取得を N 回繰り返すことになります。
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- ソースデータの複数の Amount 値を変更 ---
sheet.getCells().get("C2").putValue(5000);   // グレープ 2020
sheet.getCells().get("C5").putValue(7500);   // チェリー 2020
sheet.getCells().get("C9").putValue(9500);   // チェリー 2021

// --- 廃止予定のパターン (26.7 以前) — PivotTable.RefreshData() ---
// pivotTable1.refreshData();  // ソースから再取得し、キャッシュ全体を更新
// pivotTable2.refreshData();  // 再度取得 — キャッシュはすでに最新です！
// 各呼び出しが共有キャッシュを再構築するため、N テーブル = N 回の冗長な取得となります。

// --- 新しい v26.7+ パターン: キャッシュを 1 回更新し、必要に応じて再レンダリング ---
// PivotCache.Refresh() を 1 回呼び出すと、変更された値が共有キャッシュに取り込まれ、
// それを参照するすべてのピボットテーブルの表示が再計算されます。
// Pivot1 と Pivot2 は 1 つの PivotCache を共有しているため、この 1 回の呼び出しで
// 両方のテーブルが更新されます — ソースへの 2 度目のラウンドトリップは不要です。
pivotTable1.getPivotCache().refresh();

// CalculateData() はピボットテーブルの表示 (データ + スタイル) のみを再レンダリングします
// キャッシュに保持されているデータから実行されるため、ソースには触れません。
// ここでは Pivot2 に対して API のデモンストレーションとして呼び出しています: キャッシュが
// 1 回更新された後は、ソースに戻ることなく依存する任意のテーブルを再レンダリングできます。
// ピボットテーブルの表示/レイアウト設定のみが変更され、キャッシュが最新である場合には
// 単独で CalculateData() を使用してください。
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## どの更新 API を使用すべきか

以下の表は、利用可能な更新 API とそれぞれを選択するタイミングをまとめたものです。

| 目的 | 推奨 API | メモ |
|------|-----------------|-------|
| ワークブック内のすべてを更新する | `Workbook.RefreshAll()` | 1 回の呼び出しですべてのキャッシュとテーブルをカバーします。 |
| 単一シートのピボットテーブルのみを更新する | `Worksheet.RefreshPivotTables()` | 1 つのワークシートを対象とします。 |
| 1 つのキャッシュのソースデータが変更された | `pivotTable.PivotCache.Refresh()` | その共有キャッシュ上のすべてのピボットテーブルを更新します。 |
| ビュー/レイアウト設定のみが変更された | `pivotTable.CalculateData()` | 不要なソースラウンドトリップをスキップします。 |
| 共有キャッシュ上のすべてのピボットテーブルを一覧表示する | `pivotCache.GetPivotTables()` | 一括更新の前に列挙するために使用します。 |

実際には、非推奨のテーブルごとの `RefreshData()` よりもキャッシュベースの API を優先してください。これらは共有キャッシュを認識し、不要なソースフェッチを回避し、更新要件を満たす最小のスコープを選択できるようにします。

## 関連記事

- [Inserting an Image into a Cell](/cells/ja/nodejs-java/inserting-an-image-into-a-cell/)
- [Reading and Writing DBF Files](/cells/ja/nodejs-java/dbf/)
- [Splitting Excel Files into Multiple Files](/cells/ja/nodejs-java/splitting-excel-files-into-multiple-files/)
- [Sparklines in Aspose.Cells for Node.js via Java](/cells/ja/nodejs-java/sparkline/)

{{< app/cells/assistant language="javascript" >}}