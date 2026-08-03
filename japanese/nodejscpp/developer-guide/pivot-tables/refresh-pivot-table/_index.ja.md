---
title: Aspose.Cells for Node.js via C++でピボットテーブルを更新する
linktitle: Aspose.Cells for Node.js via C++でピボットテーブルを更新する
description: Aspose.Cells for Node.js via C++のv26.7+ピボットリフレッシュAPIを使用してピボットテーブルを更新する方法を学びます。この記事では、RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData、GetPivotTablesを実用的なコード例とともに解説します。
keywords: Aspose.Cells, Node.js via C++, ピボットテーブル, 更新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ja/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cellsは、ワークブック全体から単一のピボットテーブルまで、4つの異なるスコープでピボットデータを再読み込みできる階層的なリフレッシュAPIを提供します。**Aspose.Cells for Node.js via C++ v26.7**以降、従来のメソッド`PivotTable.RefreshData()`は非推奨となり、本記事で紹介するより効率的でキャッシュ対応のAPIに置き換える必要があります。
{{% /alert %}}
## はじめに
ピボットテーブルの更新は、単一の操作であることはほとんどありません。背後では、Aspose.Cellsは元のソースデータからワークシートに表示されるレンダリング済み値までを結ぶ階層的なデータチェーンを維持しています。このチェーンを理解することが、あらゆる状況に適したリフレッシュAPIを選択する鍵となります。
4層のデータチェーンは以下のとおりです。
1. **データソース** — 生の値が格納されている元のワークシート範囲、データベースクエリ、または統合範囲。
2. **PivotCache** — ソースデータのインメモリスナップショット。すべてのピボットテーブルは`PivotCache`の上に構築され、ここですべてのデータが収集および集計されます。
3. **PivotTable** — 行、列、値、フィルタのフィールドを定義するビューオブジェクト。`PivotTable`はデータソースから直接読み取ることはなく、*常に*その`PivotCache`からのみ読み取ります。
4. **Cells** — `PivotTable`が計算された値とスタイルをレンダリングする先のワークシートの`Cells`。
特に重要な概念は**共有キャッシュ**です。ワークブック内の複数のピボットテーブルが同じソース範囲を参照している場合、それらは*1つ*の`PivotCache`インスタンスを共有します。1つの`PivotCache`を多くのピボットテーブルから参照でき、そのキャッシュを更新すると、依存しているすべての`PivotTable`が一度に更新されます。
{{% alert color="primary" %}}
`PivotCache.SourceType`（列挙型`PivotTableSourceType`）は、キャッシュデータの取得元を示します。v26.7時点で、`PivotCache.Refresh()`がサポートするのは**`Sheet`**と**`Consolidation`**のソースタイプのみです。つまり、ワークシート範囲に存在するデータのみが対象となります。外部ソース（データベースや外部接続など）は、キャッシュAPIを介してはまだ更新できません。
{{% /alert %}}
このチェーンのため、Aspose.Cellsには2つの基本的なリフレッシュパスがあります。
- **`PivotCache.Refresh()`** — ソースからキャッシュへの再読み込みと、それに依存するすべての`PivotTable`の再計算を単一の操作で行います。
- **`PivotTable.CalculateData()`** — すでにキャッシュされたデータから1つの`PivotTable`の表示を再計算し、データソースへのラウンドトリップは行いません。
本記事のすべてのシナリオではワークシートセルのソースデータを使用するため、ソースタイプは`Sheet`となり、リフレッシュ操作は前述のとおりに動作します。
## 必要なインポート
本記事のすべてのJavaScriptの例では、Aspose.Cells for Node.js via C++モジュールが読み込まれ、ピボットタイプが`Aspose.Cells.Pivot`名前空間に存在することを前提としています。一般的なセットアップは以下のとおりです。
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;`（または`AsposeCells.Pivot.PivotFieldType`経由でアクセス）
## ワークブック内のすべてのピボットテーブルを更新する
ワークブック内のすべてのピボットキャッシュとすべてのピボットテーブルが最新のソースデータを反映するようにする必要がある場合、最もシンプルで包括的なAPIは`Workbook.RefreshAll()`です。1回の呼び出しでワークブック全体を走査し、各`PivotCache`をソースからリフレッシュし、それに依存するすべての`PivotTable`を再計算します。パフォーマンスを気にせずに一般的なドキュメント全体の更新を行う場合は、この方法を推奨します。
次の例では、Fruit/Year/Amountのソース範囲を含むワークブックを作成し、1つのピボットテーブルを追加し、一部のソース値を変更してから、`RefreshAll()`を使用してすべてを単一の呼び出しで最新状態に更新します。
```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// セルA1:C1にヘッダー行を書き込みます
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// セルA2:C9にデータ行を書き込みます（2020年と2021年のフルーツデータ8行）
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

// ピボットフィールドを割り当て：Fruitを行、Yearを列、Amountをデータ
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 変更をシミュレートするためにソースデータのAmount値をいくつか変更
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// ワークブック内のすべてのピボットテーブル/ピボットキャッシュを更新
workbook.refreshAll();

// ワークブックを保存
workbook.save("output.xlsx");
```
## 単一のワークシート上のすべてのピボットテーブルを更新する
特定のワークシート上に存在するピボットテーブルのみを更新したい場合があります。例えば、他のワークシート上のピボットテーブルは無関係であり、影響を受けるべきではないことが分かっている場合などです。このケースのために、Aspose.Cellsは単一の`Worksheet`インスタンスを対象とした`Worksheet.RefreshPivotTables()`を提供しています。
これは`Workbook.RefreshAll()`よりも選択的です。対象のワークシート上にあるピボットテーブルのみが更新され、他のワークシート上にあるピボットテーブルはそのまま残されます。
次の例では、同じFruit/Year/Amountのソースデータを設定し、最初のワークシートにピボットテーブルを追加し、一部のソース値を変更してから、そのワークシート上にあるピボットテーブルのみを更新します。
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
単一のピボットテーブルをきめ細かく制御したい場合、キャッシュベースのAPIには2つの選択肢があります。これらの選択は、実際に何が変わったのか、つまり基になるソースデータなのか、それともピボットテーブル自体のビュー/レイアウト設定のみなのかによって決まります。
### ソースデータが変更された場合 — `PivotCache.Refresh()`を使用
基になるソースデータが変更された場合、正しいエントリポイントは`pivotTable.PivotCache.Refresh()`です。この呼び出しはソースデータをキャッシュに再読み込みし、そのキャッシュに依存するすべての`PivotTable`を再計算します。
{{% alert color="primary" %}}
ピボットテーブルは単一の`PivotCache`インスタンスを共有するため、`PivotCache.Refresh()`を呼び出すと、参照した1つのテーブルだけでなく、そのキャッシュ上に構築された**すべての**ピボットテーブルが再計算されます。2つのピボットテーブルが同じソース範囲を共有している場合、一方のキャッシュを更新すると両方が更新されます。
{{% /alert %}}
次の例では、この共有キャッシュの動作を示すために同じソース範囲上に2つのピボットテーブルを作成し、一部のソース値を変更してから、1つのキャッシュ参照を介して更新します。
```javascript
const AsposeCells = require("aspose.cells");

// 新しいワークブックを作成し、最初のワークシートにアクセスする
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// ヘッダー行を書き込む: 果物 / 年 / 数量
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 約9行のデータ行を書き込む (ぶどう / ブルーベリー / キウイ / さくらんぼ を 2020-2021 にわたって)
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

// セル E3 に配置する最初のリピボットテーブル「Pivot1」を追加する、ソース範囲は A1:C9
const pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// Pivot1 のフィールドを割り当てる
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 同じソース範囲 A1:C9 を使用して E15 に配置する 2 番目のピボットテーブル「Pivot2」を追加する
// Pivot1 と Pivot2 はソース範囲が同じであるため、1 つの PivotCache を共有する。
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Pivot2 に同じフィールドを割り当てる
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// データ変更をシミュレートするために、ソースデータの複数の Amount セルの値を変更する
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// 共有されている PivotCache を更新する。
// Pivot1 と Pivot2 は同じ PivotCache を共有しているため、この 1 回の呼び出しで
// 両方のピボットテーブル (データ + スタイル) が更新されたソースから更新される。
pivotTable1.getPivotCache().refresh();

// ワークブックを保存する
workbook.save("output.xlsx");
```
### ビュー/レイアウトのみが変更された場合 — `CalculateData()`を使用
ソースデータは変更されておらず、ピボットテーブルのビューやレイアウト設定のみが変更された場合（例えば、フィールドが別のエリアに移動された場合や、ファイルを開いたときに更新する設定が切り替えられた場合など）、データソースへのラウンドトリップは必要ありません。キャッシュにはすでに正しいデータが保持されており、レンダリングされた`PivotTable`のみを再計算する必要があります。この場合、`pivotTable.CalculateData()`が適切な選択です。
これにより不要なソースフェッチが回避され、多くのピボットテーブルが同じキャッシュを共有している場合に大幅に高速化されます。
次の例では、ピボットテーブルのソース以外のプロパティを変更し、既存のキャッシュから`CalculateData()`を呼び出して再レンダリングします。
```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Fruit / Year / Amount のヘッダー行を書き込む
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 8 つのデータ行を書き込む（2〜9 行目、ソース範囲 A1:C9 に収まる）
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

// セル E3 に配置し、A1:C9 をソースとする「Pivot1」という名前のピボットテーブルを追加する
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// フィールドを割り当てる：Fruit を行、Year を列、Amount をデータ
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");

// 表示／レイアウトのプロパティを変更する — これは表示のみの変更なので、
// PivotCache.Refresh() を介してソースデータを再読み込みする必要はない。
pivotTable.setRefreshDataOnOpeningFile(false);

// CalculateData() は、PivotCache に既に保持されているデータから、このピボットテーブルの表示
//（データとスタイル）を再レンダリングする。ソースデータは変更されていないため、
// ソースへのラウンドトリップは行われず、キャッシュされた値がワークシートのセルに
// 再計算されるだけである。
pivotTable.calculateData();

// ワークブックをディスクに保存する
workbook.save("output.xlsx");
```
## 同じPivotCacheを共有するすべてのピボットテーブルを取得する
ワークブックには、1つの共有キャッシュ上に構築された多くのピボットテーブルが含まれていることがよくあります。これらを列挙するには、例えば一括更新を実行する前や共有キャッシュの影響を診断するために、`PivotCache.GetPivotTables()`を使用します。このメソッドは、指定されたキャッシュに依存するすべての`PivotTable`のコレクションを返します。
これは2つのピボットテーブルが実際に同じ`PivotCache`インスタンスを共有していることを確認するための最も直接的な方法でもあります。キャッシュ参照を比較するか、`GetPivotTables()`が返すコレクションを反復処理してどのピボットテーブルが含まれているかを確認するだけです。
次の例では、同じソース範囲上に2つのピボットテーブルを作成し、それらが同じキャッシュインスタンスを共有していることを確認し、キャッシュのピボットテーブルを列挙します。

## 非推奨の`PivotTable.RefreshData()`からの移行
Aspose.Cells for Node.js via C++ v26.7より前では、ピボットテーブルを更新するための標準的な方法は、各ピボットテーブルに対して個別に`PivotTable.RefreshData()`を呼び出すことでした。v26.7時点で、このメソッドは**非推奨**となり、上記のキャッシュ対応APIに置き換える必要があります。
現実のワークブックでは、テーブルごとの`RefreshData()`のアプローチに問題がある理由が2つあります。
- ソースが変更されていない場合でも、呼び出すたびにソースからデータを再取得します。
- 呼び出しのたびに共有キャッシュ全体が更新されます。多くのピボットテーブルが1つのキャッシュを共有している場合、ピボットテーブルごとに`RefreshData()`を繰り返し呼び出すと、同じキャッシュが何度も再取得され、非常に低速になります。
推奨される代替方法は次のとおりです。
- **ワークブック内のすべてのピボットテーブルを更新する** → `workbook.refreshAll();`を使用
- **その一部を更新する** → 1つのキャッシュに対しては`pivotTable.PivotCache.Refresh();`を使用。キャッシュは共有されているため、この1回の呼び出しで、そのキャッシュ上に構築されたすべてのピボットテーブルが更新されます。すでに更新済みのキャッシュ上に存在する他のピボットテーブルは、安全にスキップできます。
- **ピボットビュー/レイアウトのみが変更された** → ソースへのラウンドトリップなしに既存のキャッシュから再レンダリングするために`pivotTable.CalculateData();`を使用。
次の例では、単一のキャッシュを共有する複数のピボットテーブルを持つワークブックに対する新しい効率的なパターンを示します。
```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- ソースデータを構築: Fruit / Year / Amount (ヘッダー + 9行) ---
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

// --- 2番目のピボットテーブル (Pivot2) を同じソース範囲に追加 ---
// Pivot1 と Pivot2 は 1 つの PivotCache を共有します。
// これはまさに、テーブルごとの従来の RefreshData() が
// 非効率になるシナリオです。1つのテーブルを更新すると共有キャッシュ全体を
// 再フェッチするため、N 個のテーブルを更新すると同じ高コストのフェッチを N 回実行します。
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- ソースデータの複数の Amount 値を変更 ---
sheet.getCells().get("C2").putValue(5000);   // Grape  2020
sheet.getCells().get("C5").putValue(7500);   // Cherry 2020
sheet.getCells().get("C9").putValue(9500);   // Cherry 2021

// --- 旧パターン (v26.7 以前) — PivotTable.RefreshData() ---
// pivotTable1.RefreshData();  // ソースから再フェッチし、キャッシュ全体を更新
// pivotTable2.RefreshData();  // 再び再フェッチ — キャッシュはすでに最新です!
// 各呼び出しで共有キャッシュが再構築されるため、N テーブル = N 回の冗長なフェッチになります。

// --- 新しい v26.7+ パターン: キャッシュを 1 回更新し、必要に応じて再レンダリング ---
// PivotCache.Refresh() を 1 回呼び出すと、変更された値が共有キャッシュに取り込まれ、
// それを参照するすべてのピボットテーブルの表示が再計算されます。
// Pivot1 と Pivot2 は 1 つの PivotCache を共有しているため、この 1 回の呼び出しで
// 両方のテーブルが更新されます — ソースへの 2 度目のラウンドトリップは不要です。
pivotTable1.getPivotCache().refresh();

// CalculateData() は、キャッシュ内のデータからピボットテーブルの表示 (データ + スタイル)
// のみを再レンダリングします — ソースには触れません。
// ここでは API を実演するために Pivot2 に対して呼び出します: キャッシュが
// 1 回更新された後は、ソースに戻ることなく依存するテーブルを再レンダリングできます。
// ピボットテーブルの表示/レイアウト設定のみが変更され、
// キャッシュが最新の場合は、CalculateData() を単独で使用してください。
pivotTable2.calculateData();

workbook.save("output.xlsx");
```
## どのリフレッシュAPIを使用すべきか
以下の表は、利用可能なリフレッシュAPIとそれぞれを選択するタイミングをまとめたものです。
| 目的 | 推奨API | 備考 |
|------|-----------------|-------|
| ワークブック内のすべてを更新する | `Workbook.RefreshAll()` | 1回の呼び出しで、すべてのキャッシュとテーブルをカバーします。 |
| 単一シート上にあるピボットテーブルのみを更新する | `Worksheet.RefreshPivotTables()` | 1つのワークシートを対象とします。 |
| 1つのキャッシュのソースデータが変更された | `pivotTable.PivotCache.Refresh()` | その共有キャッシュ上にあるすべてのピボットテーブルを更新します。 |
| ビュー/レイアウト設定のみが変更された | `pivotTable.CalculateData()` | 不要なソースへのラウンドトリップを回避します。 |
| 共有キャッシュ上にあるすべてのピボットテーブルを一覧表示する | `pivotCache.GetPivotTables()` | 一括更新の前に列挙するために使用します。 |
実際には、非推奨のテーブルごとの`RefreshData()`よりもキャッシュベースのAPIを優先してください。これらは共有キャッシュを認識しており、冗長なソースフェッチを回避し、更新要件を満たす最小限のスコープを選択できるようにします。

{{< app/cells/assistant language="nodejs-cpp" >}}
