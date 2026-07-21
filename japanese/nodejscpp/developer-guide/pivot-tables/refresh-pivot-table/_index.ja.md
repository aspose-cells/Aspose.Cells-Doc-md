---
title: Aspose.Cells for Node.js via C++ でのピボットテーブルの更新
linktitle: Aspose.Cells for Node.js via C++ でのピボットテーブルの更新
description: Aspose.Cells for Node.js via C++ の v26.7+ ピボット更新 API を使用してピボットテーブルを更新する方法を学びます。この記事では RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData、GetPivotTables を実用的なコード例とともに解説します。
keywords: Aspose.Cells, Node.js via C++, ピボットテーブル, 更新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ja/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は、ワークブック全体から単一のピボットテーブルまで、4つの異なるスコープでピボットデータを再読み込みできる階層型リフレッシュ API を提供します。**Aspose.Cells for Node.js via C++ v26.7** 以降、従来のメソッド `PivotTable.RefreshData()` は廃止予定とされており、この記事で説明するより効率的なキャッシュ対応 API に置き換える必要があります。

{{% /alert %}}

## はじめに

ピボットテーブルの更新は、単一の操作であることはほとんどありません。舞台裏では、Aspose.Cells は元のソースデータとワークシートに表示されるレンダリング値を接続する階層型データチェーンを維持しています。このチェーンを理解することが、あらゆる状況で適切な更新 API を選択する鍵となります。

4層データチェーンは次のとおりです。

1. **データソース** — 元のワークシート範囲、データベースクエリ、または生データが含まれる統合範囲。
2. **PivotCache** — ソースデータのインメモリスナップショット。すべてのピボットテーブルは `PivotCache` の上に構築されます。ここでデータが収集および集計されます。
3. **PivotTable** — 行、列、値、フィルターフィールドを定義するビューオブジェクト。`PivotTable` はデータソースから直接ではなく、その `PivotCache` からのみ読み取ります。
4. **Cells** — `PivotTable` が計算値とスタイルをレンダリングするワークシートの `Cells`。

特に重要な概念は**共有キャッシュ**です。ワークブック内の複数のピボットテーブルが同じソース範囲を参照している場合、それらは*1つ*の `PivotCache` インスタンスを共有します。単一の `PivotCache` を多くのピボットテーブルが参照でき、そのキャッシュを更新すると、依存するすべての `PivotTable` が一度に更新されます。

{{% alert color="primary" %}}

`PivotCache.SourceType`(列挙型 `PivotTableSourceType`)は、キャッシュデータの取得元を示します。v26.7 の時点で、`PivotCache.Refresh()` は **`Sheet`** および **`Consolidation`** ソースタイプのみをサポートしています。つまり、ワークシート範囲に存在するデータです。外部ソース(データベース、外部接続など)は、キャッシュ API 経由ではまだ更新できません。

{{% /alert %}}

このチェーンのため、Aspose.Cells には2つの基本的な更新パスがあります。

- **`PivotCache.Refresh()`** — ソースからキャッシュを再読み込みし、すべての依存する `PivotTable` を単一の操作で再計算します。
- **`PivotTable.CalculateData()`** — すでにキャッシュされたデータから1つの `PivotTable` の表示を再計算し、データソースへのラウンドトリップは行いません。

この記事のすべてのシナリオではワークシートセルソースデータを使用しているため、ソースタイプは `Sheet` であり、更新操作は説明どおりに動作します。

## 必要なインポート

この記事のすべての JavaScript の例では、Aspose.Cells for Node.js via C++ モジュールがロードされており、ピボットタイプが `Aspose.Cells.Pivot` 名前空間に存在することを前提としています。典型的なセットアップは次のとおりです。

- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;`(または `AsposeCells.Pivot.PivotFieldType` 経由でアクセス)

## ワークブック内のすべてのピボットテーブルを更新する

ワークブック内のすべてのピボットキャッシュとすべてのピボットテーブルが最新のソースデータを反映するようにする必要がある場合、最もシンプルで包括的な API は `Workbook.RefreshAll()` です。単一の呼び出しでワークブック全体をトラバースし、各 `PivotCache` をソースから更新してから、すべての依存する `PivotTable` を再計算します。これは、パフォーマンスが問題にならない一般的なフルドキュメントの更新に推奨されるアプローチです。

次の例では、Fruit/Year/Amount ソース範囲を持つワークブックを作成し、1つのピボットテーブルを作成し、一部のソース値を変更してから、`RefreshAll()` を使用してすべてを1回の呼び出しで最新の状態に更新します。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// セルA1:C1にヘッダー行を書き込み
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// セルA2:C9にデータ行を書き込み（2020年と2021年の果物のデータ8行）
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
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// ピボットフィールドを割り当て：Fruitを行に、Yearを列に、Amountをデータに
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// ソースデータの複数のAmount値を変更して変更をシミュレート
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// ワークブック内のすべてのピボットテーブル/ピボットキャッシュを更新
workbook.refreshAll();

// ワークブックを保存
workbook.save("output.xlsx");
```

## 単一のワークシート上のすべてのピボットテーブルを更新する

特定のワークシート上にあるピボットテーブルのみを更新する必要がある場合があります。たとえば、他のワークシート上のピボットテーブルが関係ないとわかっていて、触れたくない場合です。この場合のために、Aspose.Cells は単一の `Worksheet` インスタンスにスコープされた `Worksheet.RefreshPivotTables()` を提供します。

これは `Workbook.RefreshAll()` よりも選択的です。対象のワークシート上のピボットテーブルのみが更新され、他のワークシート上のピボットテーブルはそのまま残されます。

次の例では、同じ Fruit/Year/Amount ソースデータを入力し、最初のワークシートにピボットテーブルを追加し、一部のソース値を変更してから、そのワークシート上のピボットテーブルのみを更新します。

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

単一のピボットテーブルを細かく制御したい場合、キャッシュベースの API は2つのオプションを提供します。それらの選択は、実際に何が変わったかによって異なります。基になるソースデータか、ピボットテーブル自体のビュー/レイアウト設定のみか。

### ソースデータが変更された — `PivotCache.Refresh()` を使用する

基になるソースデータが変更された場合、正しいエントリポイントは `pivotTable.PivotCache.Refresh()` です。この呼び出しはソースデータをキャッシュに再読み込みし、そのキャッシュに依存するすべての `PivotTable` を再計算します。

{{% alert color="primary" %}}

ピボットテーブルは単一の `PivotCache` インスタンスを共有するため、`PivotCache.Refresh()` を呼び出すと、参照しているピボットテーブルだけでなく、同じキャッシュ上に構築された**すべての**ピボットテーブルが再計算されます。2つのピボットテーブルが同じソース範囲を共有している場合、一方のキャッシュを更新すると両方が更新されます。

{{% /alert %}}

次の例では、同じソース範囲に2つのピボットテーブルを作成してこの共有キャッシュ動作を示し、一部のソース値を変更してから、1つのキャッシュ参照を介して更新します。

```javascript
const AsposeCells = require("aspose.cells");

// 新しいワークブックを作成し、最初のワークシートにアクセスする
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// ヘッダー行を書き込む: 果物 / 年 / 数量
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 約9行のデータ行を書き込む（2020〜2021年にわたるぶどう / ブルーベリー / キウイ / さくらんぼ）
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

// セルE3に配置する最初 pivot table "Pivot1" を追加する。ソース範囲は A1:C9
const pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// Pivot1 のフィールドを割り当てる
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 同じソース範囲 A1:C9 を使用して、E15に配置する2番目のピボットテーブル "Pivot2" を追加する
// ソース範囲が同一であるため、Pivot1 と Pivot2 は単一の PivotCache を共有する。
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Pivot2 にも同じフィールドを割り当てる
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// ソースデータの数量セルの値をいくつか変更して、データ変更をシミュレートする
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// 共有されている PivotCache を更新する。
// Pivot1 と Pivot2 は同じ PivotCache を共有しているため、この呼び出し一つで
// 更新されたソースから両方のピボットテーブル（データとスタイル）を更新する。
pivotTable1.getPivotCache().refresh();

// ワークブックを保存する
workbook.save("output.xlsx");
```

### ビュー/レイアウトのみが変更された — `CalculateData()` を使用する

ソースデータが変更*されていない*が、ピボットテーブルのビューまたはレイアウト設定のみが変更された場合(たとえば、フィールドが異なるエリアに移動された場合や、ファイルを開いたときに更新する設定が切り替えられた場合)、データソースへのラウンドトリップは必要ありません。キャッシュにはすでに正しいデータが保持されています。レンダリングされた `PivotTable` の再計算のみが必要です。この場合、`pivotTable.CalculateData()` が正しい選択です。

これにより、不要なソースフェッチが回避され、多くのピボットテーブルが同じキャッシュを共有している場合に大幅に高速になります。

次の例では、ピボットテーブルのソース以外のプロパティを変更し、`CalculateData()` を呼び出して既存のキャッシュから再レンダリングします。

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Fruit / Year / Amount ヘッダー行を書き込む
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 8つのデータ行を書き込む（2～9行目、ソース範囲 A1:C9 に適合）
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

// 目的地セル E3 に配置され、A1:C9 をソースとする「Pivot1」という名前のピボットテーブルを追加する
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// フィールドを割り当てる：Fruit を行、Year を列、Amount をデータに
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

// 表示/レイアウトプロパティを変更する — これは表示のみの変更であるため、
// PivotCache.Refresh() を通じてソースデータを再読み取りする必要はありません。
pivotTable.setRefreshDataOnOpeningFile(false);

// CalculateData() は、このピボットテーブルの表示（データ + スタイル）を
// PivotCache に既に保持されているデータから再レンダリングします。
// ソースデータは変更されていないため、ソースへのラウンドトリップは実行されず、
// キャッシュされた値のみがワークシートのセルに再計算されます。
pivotTable.calculateData();

// ワークブックをディスクに保存する
workbook.save("output.xlsx");
```

## 同じ PivotCache を共有するすべてのピボットテーブルを取得する

ワークブックには、多くの場合、1つの共有キャッシュの上に構築された多くのピボットテーブルが含まれています。それらを列挙するには(たとえば、バッチ更新を実行する前や、共有キャッシュの影響を診断するために)、`PivotCache.GetPivotTables()` を使用します。このメソッドは、指定されたキャッシュに依存するすべての `PivotTable` のコレクションを返します。

これは、2つのピボットテーブルが実際に同じ `PivotCache` インスタンスを共有していることを確認する最も直接的な方法でもあります。キャッシュ参照を比較するか、`GetPivotTables()` によって返されたコレクションを単に反復処理し、どのピボットテーブルが含まれているかを観察できます。

次の例では、同じソース範囲に2つのピボットテーブルを作成し、それらが同じキャッシュインスタンスを共有していることを確認してから、キャッシュのピボットテーブルを列挙します。

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
pivotTable1.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

let pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

let sameCache = pivotTable1.getPivotCache() === pivotTable2.getPivotCache();
console.log("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

let sharedPivotTables = pivotTable1.getPivotCache().getPivotTables();
console.log("Number of pivot tables sharing the cache: " + sharedPivotTables.length);

for (let pt of sharedPivotTables) {
    console.log("Pivot table name: " + pt.getName());
}

workbook.save("output.xlsx");
```

## 廃止予定の `PivotTable.RefreshData()` からの移行

Aspose.Cells for Node.js via C++ v26.7 より前では、ピボットテーブルを更新する標準的な方法は、各ピボットテーブルで個別に `PivotTable.RefreshData()` を呼び出すことでした。v26.7 の時点で、このメソッドは**廃止予定**とマークされており、上記のキャッシュ対応 API に置き換える必要があります。

テーブルごとの `RefreshData()` アプローチが実際のワークブックで問題になる理由は2つあります。

- ソースが変更されていない場合でも、呼び出されるたびにソースからデータを再取得します。
- 各呼び出しは共有キャッシュ全体を更新します。多くのピボットテーブルが1つのキャッシュを共有している場合、ピボットテーブルごとに `RefreshData()` を繰り返し呼び出すと、同じキャッシュが何度も再フェッチされるため、非常に遅くなります。

推奨される代替手段は次のとおりです。

- **ワークブック内のすべてのピボットテーブルを更新する** → `workbook.refreshAll();` を使用します
- **一部のみを更新する** → 1つのキャッシュに対して `pivotTable.PivotCache.Refresh();` を使用します。キャッシュは共有されているため、この1回の呼び出しでそのキャッシュの上に構築されたすべてのピボットテーブルが更新されます。すでに更新されたキャッシュ上にある他のピボットテーブルは安全にスキップできます。
- **ピボットビュー/レイアウトのみが変更された** → ソースへのラウンドトリップなしで既存のキャッシュから再レンダリングするには、`pivotTable.CalculateData();` を使用します。

次の例では、単一のキャッシュを共有する複数のピボットテーブルを持つワークブックの新しい効率的なパターンを示します。

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- ソースデータの作成: 果物 / 年 / 金額（ヘッダー + 9行） ---
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

// --- 最初のピボットテーブル（Pivot1）を宛先セル E3 に追加 ---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- 2番目のピボットテーブル（Pivot2）を同じソース範囲に追加 ---
// Pivot1 と Pivot2 は 1 つの基礎となる PivotCache を共有しています。
// これはまさに、レガシーのテーブルごとの RefreshData() が
// 非効率になるシナリオです。1 つのテーブルを更新すると、共有キャッシュ全体を
// 再取得するため、N 個のテーブルを更新すると、同じ高コストな取得が N 回行われます。
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- ソースデータの複数の金額値を変更 ---
sheet.getCells().get("C2").putValue(5000);   // グレープ 2020
sheet.getCells().get("C5").putValue(7500);   // チェリー 2020
sheet.getCells().get("C9").putValue(9500);   // チェリー 2021

// --- 旧パターン（v26.7 以前）— PivotTable.RefreshData() ---
// pivotTable1.RefreshData();  // ソースから再取得し、キャッシュ全体を更新
// pivotTable2.RefreshData();  // 再び再取得 — キャッシュはすでに最新です！
// 各呼び出しで共有キャッシュが再構築されるため、N テーブル = N 回の冗長な取得となります。

// --- 新パターン（v26.7 以降）: キャッシュを 1 回更新し、必要に応じて再描画 ---
// PivotCache.Refresh() を 1 回呼び出すと、変更された値が共有キャッシュに
// 取り込まれ、それを参照するすべてのピボットテーブルの表示が再計算されます。
// Pivot1 と Pivot2 は 1 つの PivotCache を共有しているため、この 1 回の呼び出しで
// 両方のテーブルが更新されます。ソースへの 2 回目のラウンドトリップは不要です。
pivotTable1.getPivotCache().refresh();

// CalculateData() はピボットテーブルの表示（データ + スタイル）のみを再描画します
// （キャッシュに保持されているデータから）。ソースにはアクセスしません。
// ここでは API のデモとして Pivot2 で呼び出しています。キャッシュが
// 一度更新された後は、依存するテーブルをソースに戻らずに
// 再描画できます。ピボットテーブルの表示/レイアウト設定のみが
// 変更され、キャッシュが最新である場合は、CalculateData() を単独で使用してください。
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## どの更新 API を使用すべきか?

以下の表は、利用可能な更新 API とそれぞれをいつ選択すべきかをまとめたものです。

| 目標 | 推奨 API | メモ |
|------|-----------------|-------|
| ワークブック内のすべてを更新する | `Workbook.RefreshAll()` | 1回の呼び出しで、すべてのキャッシュとテーブルをカバーします。 |
| 単一シート上のピボットテーブルのみを更新する | `Worksheet.RefreshPivotTables()` | 1つのワークシートにスコープされます。 |
| 1つのキャッシュのソースデータが変更された | `pivotTable.PivotCache.Refresh()` | 共有キャッシュ上のすべてのピボットテーブルを更新します。 |
| ビュー/レイアウト設定のみが変更された | `pivotTable.CalculateData()` | 不要なソースラウンドトリップをスキップします。 |
| 共有キャッシュ上のすべてのピボットテーブルを一覧表示する | `pivotCache.GetPivotTables()` | 一括更新の前に列挙するために使用します。 |

実際には、廃止予定のテーブルごとの `RefreshData()` よりもキャッシュベースの API を優先してください。これらは共有キャッシュを認識し、冗長なソースフェッチを回避し、更新要件を満たす最小のスコープを選択できるようにします。

## 関連記事

- [セルへの画像の挿入](/cells/ja/nodejs-cpp/inserting-an-image-into-a-cell/)
- [DBF ファイルの読み取りと書き込み](/cells/ja/nodejs-cpp/dbf/)
- [Excel ファイルを複数のファイルに分割する](/cells/ja/nodejs-cpp/splitting-excel-files-into-multiple-files/)
- [Aspose.Cells for Node.js via C++ のスパークライン](/cells/ja/nodejs-cpp/sparkline/)

{{< app/cells/assistant language="javascript" >}}