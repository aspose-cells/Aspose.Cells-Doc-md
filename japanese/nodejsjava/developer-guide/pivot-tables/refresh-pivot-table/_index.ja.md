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
Aspose.Cells は、ワークブック全体から単一のピボットテーブルに至るまで、4 つの異なるスコープでピボットデータを再読み込みできる階層的な更新 API を提供します。**Aspose.Cells for Node.js via Java v26.7** 以降、レガシーメソッドである `PivotTable.RefreshData()` は非推奨となり、本記事で説明するより効率的でキャッシュ対応の API に置き換える必要があります。
{{% /alert %}}
## はじめに
ピボットテーブルの更新は、単一の操作であることはほとんどありません。Aspose.Cells はバックグラウンドで、元のソースデータとワークシートに表示されるレンダリング済みの値を結ぶ階層的なデータチェーンを管理しています。このチェーンを理解することが、あらゆる状況に対して適切な更新 API を選択する鍵となります。
4 層のデータチェーンは次のとおりです。
1. **データソース** — 元のワークシート範囲、データベースクエリ、または統合範囲。生データが格納されている場所です。
2. **PivotCache** — ソースデータのインメモリスナップショットです。すべてのピボットテーブルは `PivotCache` の上に構築されます。すべてのデータはこの層で収集および集計されます。
3. **PivotTable** — 行、列、値、フィルタの各フィールドを定義するビューオブジェクトです。`PivotTable` はデータソースから直接ではなく、所属する `PivotCache` からのみデータを読み取ります。
4. **Cells** — `PivotTable` が計算結果とスタイルを描画する先のワークシートの `Cells` です。
特に重要な概念は **共有キャッシュ** です。ワークブック内の複数のピボットテーブルが同じソース範囲を参照している場合、それらは *1 つの* `PivotCache` インスタンスを共有します。1 つの `PivotCache` は多くのピボットテーブルから参照でき、そのキャッシュを更新すると、それに依存するすべての `PivotTable` が一度に更新されます。
{{% alert color="primary" %}}
`PivotCache.SourceType`（列挙型 `PivotTableSourceType`）は、キャッシュデータの取得元を示します。v26.7 時点で、`PivotCache.Refresh()` は **`Sheet`** および **`Consolidation`** のソース種別のみをサポートします。つまり、ワークシート範囲に存在するデータのみが対象です。外部ソース（データベースや外部接続など）は、キャッシュ API 経由ではまだ更新できません。
{{% /alert %}}
このチェーンのため、Aspose.Cells には 2 つの基本的な更新パスがあります。
- **`PivotCache.Refresh()`** — ソースからキャッシュへの再読み込みと、それに依存するすべての `PivotTable` の再計算を単一の操作で行います。
- **`PivotTable.CalculateData()`** — すでにキャッシュされたデータから、1 つの `PivotTable` の表示を再計算します。データソースへのラウンドトリップは発生しません。
本記事のすべてのシナリオではワークシートセルのソースデータを使用しているため、ソース種別は `Sheet` となり、更新操作は説明したとおりに動作します。
## 必要なインポート
本記事のすべての JavaScript の例では、Aspose.Cells for Node.js via Java モジュールが必要です。ピボット系の型は `Aspose.Cells.Pivot` 名前空間にあり、同じモジュールの一部です。
- `const aspose = require('aspose.cells');`
- または個別にインポートする場合: `const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`
## ワークブック内のすべてのピボットテーブルを更新する
ワークブック内のすべてのピボットキャッシュとすべてのピボットテーブルが最新のソースデータを反映するようにする必要がある場合、最もシンプルで包括的な API は `Workbook.RefreshAll()` です。1 回の呼び出しでワークブック全体を走査し、各 `PivotCache` をソースから更新し、それに依存するすべての `PivotTable` を再計算します。これは、パフォーマンスを気にせずにドキュメント全体を一括更新したい場合の推奨されるアプローチです。
次の例では、Fruit/Year/Amount のソース範囲を含むワークブックを作成し、1 つのピボットテーブルを追加し、一部のソース値を変更してから、`RefreshAll()` を使用してすべてを 1 回の呼び出しで最新の状態にします。
```javascript
const AsposeCells = require("aspose.cells");

// 新しいワークブックを作成
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// ヘッダー行をセル A1:C1 に書き込む
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// データ行をセル A2:C9 に書き込む (2020年と2021年にわたる8行の果物データ)
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

// ピボットテーブルを追加: ソース範囲 "A1:C9"、配置先セル "E3"、名前 "Pivot1"
const pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

// ピボットフィールドを割り当て: Fruit を行、Year を列、Amount をデータに
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// ソースデータのいくつかの Amount 値を変更して変更をシミュレート
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// ワークブック内のすべてのピボットテーブル / ピボットキャッシュを更新
workbook.refreshAll();

// ワークブックを保存
workbook.save("output.xlsx");
```
## 単一のワークシート上のすべてのピボットテーブルを更新する
特定の 1 つのワークシート上にあるピボットテーブルだけを更新したい場合もあります。たとえば、他のワークシート上にあるピボットテーブルは関係がなく、触るべきではないと分かっているような場合です。このケースのために、Aspose.Cells は単一の `Worksheet` インスタンスにスコープされる `Worksheet.RefreshPivotTables()` を提供します。
これは `Workbook.RefreshAll()` よりも選択的で、対象ワークシート上のピボットテーブルのみが更新され、他のワークシート上のピボットテーブルはそのまま残されます。
次の例では、同じ Fruit/Year/Amount のソースデータを投入し、最初のワークシートにピボットテーブルを追加し、一部のソース値を変更した後、そのワークシート上のピボットテーブルのみを更新します。
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
単一のピボットテーブルを細かく制御したい場合は、キャッシュベースの API に 2 つの選択肢があります。どちらを選ぶかは、実際に変更された内容、つまり基になるソースデータなのか、ピボットテーブル自体の表示やレイアウト設定だけなのかによって異なります。
### ソースデータが変更された場合 — `PivotCache.Refresh()` を使用
基になるソースデータが変更された場合の正しいエントリーポイントは `pivotTable.PivotCache.Refresh()` です。この呼び出しはソースデータをキャッシュに再読み込みし、そのキャッシュに依存するすべての `PivotTable` を再計算します。
{{% alert color="primary" %}}
ピボットテーブルは単一の `PivotCache` インスタンスを共有するため、`PivotCache.Refresh()` を呼び出すと、参照した 1 つのピボットテーブルだけでなく、**同じキャッシュ上に構築されたすべての**ピボットテーブルが再計算されます。2 つのピボットテーブルが同じソース範囲を共有している場合、片方を更新すると両方とも更新されます。
{{% /alert %}}
次の例では、同じソース範囲上に 2 つのピボットテーブルを作成してこの共有キャッシュの動作を示し、一部のソース値を変更した後、1 つのキャッシュ参照を通して更新を行います。
```javascript
const AsposeCells = require("aspose.cells");

// 新しいワークブックを作成し、最初のワークシートにアクセスする
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// ヘッダー行を書き込む: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 約9行のデータ行を書き込む (2020〜2021における grape / blueberry / kiwi / cherry)
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

// セル E3 に配置された最初のピボットテーブル "Pivot1" を追加し、ソース範囲は A1:C9
const pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// Pivot1 のフィールドを割り当てる
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 2番目のピボットテーブル "Pivot2" を E15 に追加し、同じソース範囲 A1:C9 を使用する
// ソース範囲が同一であるため、Pivot1 と Pivot2 は単一の PivotCache を共有する。
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Pivot2 に同じフィールドを割り当てる
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// データ変更をシミュレートするため、ソースデータの複数の Amount セルの値を変更する
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// 共有されている PivotCache を更新する。
// Pivot1 と Pivot2 は同じ PivotCache を共有しているため、この 1 回の呼び出しで
// 更新されたソースから両方のピボットテーブル (データ + スタイル) を更新する。
pivotTable1.getPivotCache().refresh();

// ワークブックを保存する
workbook.save("output.xlsx");
```
### 表示やレイアウトのみが変更された場合 — `CalculateData()` を使用
ソースデータは変更されておらず、ピボットテーブルの表示やレイアウト設定のみが変更された（たとえば、フィールドを別のエリアに移動した、あるいはファイルを開いたときに更新する設定を切り替えた）場合は、データソースへラウンドトリップする必要はありません。キャッシュにはすでに正しいデータが格納されており、再計算する必要があるのはレンダリング済みの `PivotTable` だけです。この場合、`pivotTable.CalculateData()` が適切な選択です。
これにより不要なソースフェッチが回避され、多くのピボットテーブルが同じキャッシュを共有している場合には大幅に高速化されます。
次の例では、ピボットテーブルのソース以外のプロパティを変更した後、`CalculateData()` を呼び出して既存のキャッシュから再レンダリングします。
```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Fruit / Year / Amount のヘッダー行を書き込む
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 8 行のデータ行を書き込む（2 行目〜9 行目、元データの範囲 A1:C9 に合わせる）
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

// 出力先セル E3 に配置する "Pivot1" という名前のピボットテーブルを追加し、A1:C9 をデータソースとする
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// フィールドを割り当てる：Fruit を行、Year を列、Amount をデータ
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 表示／レイアウトのプロパティを変更する — これは表示のみの変更なので、
// PivotCache.Refresh() を使ってソースデータを再読み込みする必要はない。
pivotTable.setRefreshDataOnOpeningFile(false);

// CalculateData() は PivotCache に保持されているデータから、このピボットテーブルの表示（データとスタイル）を再描画する。
// ソースデータは変更されていないため、ソースへのラウンドトリップは行われず、キャッシュされた値がワークシートのセルに再計算されるだけである。
pivotTable.calculateData();

// ワークブックをディスクに保存する
workbook.save("output.xlsx");
```
## 同じ PivotCache を共有するすべてのピボットテーブルを取得する
ワークブックには、1 つの共有キャッシュ上に構築された多くのピボットテーブルが含まれることがよくあります。それらを列挙する必要がある場合（たとえば一括更新を行う前や、共有キャッシュの影響を診断するために）、`PivotCache.GetPivotTables()` を使用します。このメソッドは、指定したキャッシュに依存するすべての `PivotTable` のコレクションを返します。
これは、2 つのピボットテーブルが実際に同じ `PivotCache` インスタンスを共有していることを確認する最も直接的な方法でもあります。キャッシュ参照を比較するか、`GetPivotTables()` が返すコレクションを反復処理し、どのピボットテーブルが含まれるかを観察するだけで確認できます。
次の例では、同じソース範囲上に 2 つのピボットテーブルを作成し、それらが同じキャッシュインスタンスを共有していることを確認し、キャッシュのピボットテーブルを列挙します。

## 非推奨となった `PivotTable.RefreshData()` からの移行
Aspose.Cells for Node.js via Java v26.7 より前は、ピボットテーブルを更新する標準的な方法は、各ピボットテーブルに対して個別に `PivotTable.RefreshData()` を呼び出すことでした。v26.7 以降、このメソッドは **非推奨** とされ、上記のキャッシュ対応 API に置き換える必要があります。
テーブルごとの `RefreshData()` アプローチが実際のワークブックで問題になる理由は 2 つあります。
- ソースが変更されていなくても、呼び出すたびにソースからデータを再フェッチします。
- 呼び出しごとに共有キャッシュ全体が更新されます。多くのピボットテーブルが 1 つのキャッシュを共有している場合、ピボットテーブルごとに `RefreshData()` を繰り返し呼び出すと、同じキャッシュが何度も再フェッチされ、非常に低速になります。
推奨される代替手段は次のとおりです。
- **ワークブック内のすべてのピボットテーブルを更新する** → `workbook.refreshAll();` を使用します。
- **一部のみを更新する** → 1 つのキャッシュに対して `pivotTable.getPivotCache().refresh();` を使用します。キャッシュは共有されているため、この 1 回の呼び出しで、そのキャッシュ上に構築されたすべてのピボットテーブルが更新されます。すでに更新済みのキャッシュ上にある他のピボットテーブルは、安全にスキップできます。
- **ピボットテーブルの表示やレイアウトのみが変更された場合** → ソースへのラウンドトリップなしで既存のキャッシュから再レンダリングするには `pivotTable.calculateData();` を使用します。
次の例では、単一のキャッシュを共有する複数のピボットテーブルを含むワークブックに対する、新しい効率的なパターンを示します。
```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- ソースデータを構築する: 果物 / 年 / 金額 (ヘッダー + 9行) ---
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

// --- 最初のピボットテーブル (Pivot1) を配置先セル E3 に追加 ---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- 2つ目のピボットテーブル (Pivot2) を同じソース範囲に追加 ---
// Pivot1 と Pivot2 は両方とも1つの PivotCache を共有する。
// これはまさに、レガシーなテーブルごとの RefreshData() が非効率になるシナリオだ。
// 1つのテーブルを更新すると共有キャッシュ全体を再取得するため、
// N個のテーブルを更新すると、同じ高コストな取得がN回行われる。
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- ソースデータのいくつかの Amount 値を変更する ---
sheet.getCells().get("C2").putValue(5000);   // グレープ 2020
sheet.getCells().get("C5").putValue(7500);   // チェリー 2020
sheet.getCells().get("C9").putValue(9500);   // チェリー 2021

// --- 旧式パターン (v26.7 以前) — PivotTable.RefreshData() ---
// pivotTable1.refreshData();  // ソースから再取得し、キャッシュ全体を更新
// pivotTable2.refreshData();  // 再度再取得 — キャッシュはすでに最新!
// 各呼び出しが共有キャッシュを再構築するため、N個のテーブル = N回の冗長な取得。

// --- 新 v26.7+ パターン: キャッシュを一度だけ更新し、必要に応じて再描画する ---
// PivotCache.Refresh() を一度呼び出すと、変更された値が共有キャッシュに取り込まれ、
// それを参照するすべてのピボットテーブルの表示も再計算される。
// Pivot1 と Pivot2 は1つの PivotCache を共有しているため、この1回の呼び出しで
// 両方のテーブルが更新される — ソースへの2回目のラウンドトリップは不要。
pivotTable1.getPivotCache().refresh();

// CalculateData() はピボットテーブルの表示 (データ + スタイル) のみを再描画する。
// キャッシュに既にあるデータから行うため、ソースには触れない。
// ここでは API のデモとして Pivot2 で呼び出している: キャッシュが一度更新された後は、
// 依存するテーブルはソースに戻らずに再描画できる。
// ピボットテーブルの表示/レイアウト設定のみが変更され、
// キャッシュが最新である場合は、CalculateData() を単独で使用する。
pivotTable2.calculateData();

workbook.save("output.xlsx");
```
## どの更新 API を使用すべきか
次の表は、利用可能な更新 API とそれぞれの選択場面をまとめたものです。
| 目的 | 推奨 API | メモ |
|------|-----------------|-------|
| ワークブック内のすべてを更新する | `Workbook.RefreshAll()` | 1 回の呼び出しで、すべてのキャッシュとテーブルを対象にします。 |
| 単一シート上のピボットテーブルのみを更新する | `Worksheet.RefreshPivotTables()` | 1 つのワークシートにスコープされます。 |
| 1 つのキャッシュのソースデータが変更された | `pivotTable.PivotCache.Refresh()` | 共有キャッシュ上のすべてのピボットテーブルを更新します。 |
| 表示やレイアウトの設定のみが変更された | `pivotTable.CalculateData()` | 不要なソースへのラウンドトリップを回避します。 |
| 共有キャッシュ上のすべてのピボットテーブルを一覧表示する | `pivotCache.GetPivotTables()` | 一括更新の前に列挙するために使用します。 |
実際には、非推奨のテーブル単位の `RefreshData()` よりも、キャッシュベースの API を優先してください。これらは共有キャッシュを認識し、不要なソースフェッチを避け、更新要件を満たす最小のスコープを選択できるようにしてくれます。

{{< app/cells/assistant language="nodejs-java" >}}
