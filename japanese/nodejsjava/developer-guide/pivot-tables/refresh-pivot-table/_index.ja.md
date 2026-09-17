---
title: Aspose.Cells for Node.js via Java でピボットテーブルとピボットキャッシュを更新する
linktitle: Aspose.Cells for Node.js via Java でピボットテーブルとピボットキャッシュを更新する
description: v26.7+ の pivot-refresh API を使用して Aspose.Cells for Node.js via Java でピボットテーブルを更新する方法を学びます。この記事では RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData、GetPivotTables を実用的なコード例とともに解説します。
keywords: Aspose.Cells, Node.js, Java, ピボットテーブル, 更新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ja/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ワークブック全体から単一のピボットテーブルまで、4 つの異なるスコープでピボットデータを再ロードできる階層化された更新 API を提供します。**Aspose.Cells for Node.js via Java v26.7** 以降、従来の `PivotTable.RefreshData()` メソッドは非推奨となり、この記事で説明するより効率的でキャッシュ対応の API に置き換える必要があります。
{{% /alert %}}

## はじめに
ピボットテーブルの更新は、単一の操作であることはほとんどありません。内部的には、Aspose.Cells は元のソースデータとワークシートに表示されるレンダリング値を接続する階層化されたデータチェーンを維持しています。このチェーンを理解することが、あらゆる状況において適切な更新 API を選択する鍵となります。
4 層データチェーンは次のとおりです:
1. **Data Source** — 生データが格納されている元のワークシート範囲、データベースクエリ、または統合範囲。
2. **PivotCache** — ソースデータのメモリ内スナップショット。すべてのピボットテーブルは `PivotCache` の上に構築され、ここですべてのデータが収集および集計されます。
3. **PivotTable** — 行、列、値、フィルタの各フィールドを定義するビューオブジェクト。`PivotTable` はデータソースから直接ではなく、`PivotCache` からのみデータを読み取ります。
4. **Cells** — `PivotTable` が計算値と書式をレンダリングする先のワークシートの `Cells`。

{{% alert color="primary" %}}
`PivotCache.SourceType` (列挙型 `PivotTableSourceType`) は、キャッシュデータの取得元を示します。v26.7 の時点で、`PivotCache.Refresh()` は **`Sheet`** と **`Consolidation`** のソースタイプのみをサポートしています。つまり、ワークシート範囲に存在するデータのみです。外部ソース (データベース、外部接続など) は、現時点ではキャッシュ API を通じて更新できません。
{{% /alert %}}

このチェーンのため、Aspose.Cells には 2 つの基本的な更新パスがあります:
- **`PivotTable.CalculateData()`** — 既にキャッシュされたデータから 1 つの `PivotTable` の表示を再計算します。データソースへのラウンドトリップはありません。
この記事のすべてのシナリオではワークシートセルのソースデータを使用しているため、ソースタイプは `Sheet` であり、更新操作は説明どおりに動作します。

## クイックスタート
ワークブック内のすべてのピボットを更新する最小限のコードだけが必要な場合は、1 回の呼び出しで十分です:

```javascript
const aspose = require('aspose.cells');
const workbook = new aspose.cells.Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

この記事の残りの部分では、代わりにいつより狭い API を選択すべきかについて説明します。

## 必要なインポート
- `const aspose = require('aspose.cells');`
- 特定のインポートの場合: `const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`

## ワークブック内のすべてのピボットテーブルを更新する
ワークブック内のすべてのピボットキャッシュとすべてのピボットテーブルが最新のソースデータを反映するようにする必要がある場合、最もシンプルで包括的な API は `Workbook.RefreshAll()` です。1 回の呼び出しでワークブック全体を走査し、各 `PivotCache` をそのソースから更新し、それに依存するすべての `PivotTable` を再計算します。これは、パフォーマンスが問題にならない一般的なフルドキュメントの更新に推奨されるアプローチです。
次の例では、Fruit/Year/Amount ソース範囲を持つワークブックを作成し、1 つのピボットテーブルを作成してソース値の一部を変更し、その後 `RefreshAll()` を使用してすべてを 1 回の呼び出しで最新の状態に更新します。

```javascript
const AsposeCells = require("aspose.cells");
// 新しいワークブックを作成
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
// セルA1:C1にヘッダー行を書き込み
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// セルA2:C9にデータ行を書き込み（2020年と2021年にわたる8行の果物のデータ）
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
// ピボットテーブルを追加：ソース範囲"A1:C9"、配置先のセル"E3"、名前"Pivot1"
const pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);
// ピボットフィールドを割り当て：Fruitを行、Yearを列、Amountをデータに
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// 変更をシミュレートするため、ソースデータのいくつかのAmount値を変更
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// ワークブック内のすべてのピボットテーブル/ピボットキャッシュを更新
workbook.refreshAll();
// ワークブックを保存
workbook.save("output.xlsx");
```

## 単一のワークシート上のすべてのピボットテーブルを更新する
ときには、特定のワークシートに存在するピボットテーブルのみを更新する必要がある場合があります。たとえば、他のワークシートのピボットテーブルが関連していないことがわかっていて、触れてはならない場合です。このケースのために、Aspose.Cells は単一の `Worksheet` インスタンスを対象とする `Worksheet.RefreshPivotTables()` を提供します。

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
単一のピボットテーブルに対してきめ細かい制御を行いたい場合、キャッシュベースの API は 2 つのオプションを提供します。どちらを選択するかは、実際に何が変更されたかによって異なります。基になるソースデータか、ピボットテーブル自体のビュー/レイアウト設定のみかです。

### ソースデータが変更された場合 — `PivotCache.Refresh()` を使用
基になるソースデータが変更された場合、正しいエントリポイントは `pivotTable.PivotCache.Refresh()` です。この呼び出しはソースデータをキャッシュに再読み込みし、そのキャッシュに依存するすべての `PivotTable` を再計算します。

### ビュー/レイアウトのみが変更された場合 — `CalculateData()` を使用
ソースデータが変更されておらず、ピボットテーブルのビューまたはレイアウト設定のみが変更された場合 (たとえば、フィールドが別のエリアに移動された場合や、開く時に更新する設定が切り替えられた場合)、データソースへのラウンドトリップは不要です。キャッシュにはすでに正しいデータが保持されており、レンダリングされた `PivotTable` の再計算のみが必要です。この場合、`pivotTable.CalculateData()` が正しい選択です。
次の例では、ピボットテーブルのソース以外のプロパティを変更し、その後 `CalculateData()` を呼び出して既存のキャッシュから再レンダリングします。

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// フルーツ / 年 / 数量の見出し行を書き込む
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// 8行のデータ行を書き込む（2〜9行目、ソース範囲A1:C9に合わせる）
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
// 名前が "Pivot1" のピボットテーブルを追加し、配置先セルE3、ソース範囲をA1:C9とする
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);
// フィールドを割り当てる：Fruitを行、Yearを列、Amountをデータへ
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// 表示/レイアウトプロパティを変更する — これは表示のみの変更であるため、
// PivotCache.Refresh() を通じてソースデータを再読み込みする必要はない。
pivotTable.setRefreshDataOnOpeningFile(false);
// CalculateData() はこのピボットテーブルの表示（データ＋スタイル）を
// PivotCache にすでに保持されているデータから再レンダリングする。ソースデータは変更されていないため、
// ソースへのラウンドトリップは行われず、キャッシュされた値のみがワークシートセルに再計算される。
pivotTable.calculateData();
// ワークブックをディスクに保存する
workbook.save("output.xlsx");
```

ワークブックには、多くの場合、1 つの共有キャッシュの上に存在する多くのピボットテーブルが含まれています。これらを列挙するには (たとえば、一括更新を実行する前や、共有キャッシュの影響を診断するため)、`PivotCache.GetPivotTables()` を使用します。このメソッドは、指定されたキャッシュに依存するすべての `PivotTable` のコレクションを返します。

## 非推奨の `PivotTable.RefreshData()` からの移行
Aspose.Cells for Node.js via Java v26.7 より前では、ピボットテーブルを更新する標準的な方法は、各ピボットテーブルに対して個別に `PivotTable.RefreshData()` を呼び出すことでした。v26.7 以降、そのメソッドは**非推奨**となり、上記のキャッシュ対応 API に置き換える必要があります。
実際のワークブックでは、テーブルごとの `RefreshData()` アプローチに問題がある理由は 2 つあります:
- ソースが変更されていない場合でも、呼び出すたびにソースからデータを再取得します。
推奨される代替手段は次のとおりです:
次の例では、単一のキャッシュを共有する複数のピボットテーブルを持つワークブックの新しい効率的なパターンを示します。

## どの更新 API を使用すべきか?
次の表は、利用可能な更新 API とそれぞれをいつ選択すべきかをまとめたものです。
| 目的 | 推奨 API | メモ |
|------|-----------------|-------|
| ワークブック内のすべてを更新する | `Workbook.RefreshAll()` | 1 回の呼び出しで、すべてのキャッシュとテーブルをカバーします。 |
| 単一シートのピボットテーブルのみを更新する | `Worksheet.RefreshPivotTables()` | 単一のワークシートを対象とします。 |
| 1 つのキャッシュのソースデータが変更された | `pivotTable.PivotCache.Refresh()` | 共有キャッシュ上のすべてのピボットテーブルを更新します。 |
| ビュー/レイアウト設定のみが変更された | `pivotTable.CalculateData()` | 不要なソースへのラウンドトリップをスキップします。 |
| 共有キャッシュ上のすべてのピボットテーブルをリスト表示する | `pivotCache.GetPivotTables()` | 一括更新の前に列挙するために使用します。 |
実際には、非推奨のテーブルごとの `RefreshData()` よりも、キャッシュベースの API を優先してください。これらは共有キャッシュを認識し、冗長なソースフェッチを回避し、更新要件を満たす最小のスコープを選択できるようにします。

## よくある落とし穴
- **保存前に更新することを忘れる。** ピボットテーブルは、データチェーンが更新された場合にのみ、レンダリングされた値をワークシートに書き込みます。ソースセルを変更した場合は、`Workbook.save()` の前に `PivotCache.Refresh()` (または `Workbook.RefreshAll()`) を呼び出してください。そうしないと、保存されたファイルには古い集計値が含まれます。
- **テーブルごとに非推奨の `RefreshData()` を呼び出す。** v26.7 では、`PivotTable.RefreshData()` は非推奨となっており、呼び出しごとにソースを再取得します。複数のピボットテーブルがキャッシュを共有している場合、これは N 回の冗長なソースフェッチを意味します。単一の `PivotCache.Refresh()` を呼び出し、続けてテーブルごとに `CalculateData()` を呼び出すように置き換えてください。
- **レイアウトのみが変更された場合に更新する。** ソースデータに触れずにピボットテーブルのビューのみ (列順、`ConsolidationFunction` など) を変更した場合、`PivotCache.Refresh()` は不要で低速です。`pivotTable.CalculateData()` を呼び出して、既存のキャッシュから再レンダリングしてください。
- **`PivotCache.Refresh()` では外部ソースがサポートされない。** ピボットテーブルのソースが外部接続 (データベース、OLAP キューブなど) からのものである場合、`PivotCache.Refresh()` は v26.7 ではそれを更新できません。現在、`Sheet` と `Consolidation` のソースタイプのみをサポートしています。外部ソースの場合は、ワークブックを再オープンするか、ソースからキャッシュを再構築してください。

{{< app/cells/assistant language="nodejs-java" >}}