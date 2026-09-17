---
title: Aspose.Cells for Node.js via C++ でピボットテーブルとピボットキャッシュを更新する
linktitle: Aspose.Cells for Node.js via C++ でピボットテーブルとピボットキャッシュを更新する
description: Aspose.Cells for Node.js via C++ の v26.7+ ピボット更新 API を使用してピボットテーブルを更新する方法を学びます。本記事では、RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData、GetPivotTables を実践的なコード例と共に解説します。
keywords: Aspose.Cells, Node.js via C++, ピボットテーブル, 更新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ja/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ワークブック全体から単一のピボットテーブルまで、4 つの異なるスコープでピボットデータを再読み込みできる、階層化された更新 API を提供します。**Aspose.Cells for Node.js via C++ v26.7** 以降、従来のメソッド `PivotTable.RefreshData()` は非推奨となり、本記事で紹介するより効率的なキャッシュ対応 API に置き換える必要があります。
{{% /alert %}}

## はじめに
ピボットテーブルの更新は、単一の操作であることはほとんどありません。Aspose.Cells は内部で、元のソースデータからワークシートに表示されるレンダリング済みの値までをつなぐ、階層化されたデータチェーンを保持しています。このチェーンを理解することが、あらゆる状況に応じて適切な更新 API を選択する鍵となります。
4 層のデータチェーンは次のとおりです。
1. **データソース** — 生の値が格納されている元のワークシート範囲、データベースクエリ、または統合範囲。
2. **PivotCache** — ソースデータのメモリ内スナップショット。すべてのピボットテーブルは `PivotCache` の上に構築されます。すべてのデータが集約・集計されるのはここです。
3. **PivotTable** — 行、列、値、フィルタの各フィールドを定義するビューオブジェクト。`PivotTable` は自身の `PivotCache` からのみデータを読み取り、データソースから直接読み取ることはありません。
4. **Cells** — `PivotTable` が計算済みの値とスタイルを描画する先のワークシートの `Cells`。

{{% alert color="primary" %}}
`PivotCache.SourceType`（列挙型 `PivotTableSourceType`）は、キャッシュデータの取得元を示します。v26.7 時点では、`PivotCache.Refresh()` は **`Sheet`** および **`Consolidation`** のソースタイプ、つまりワークシート範囲に存在するデータのみをサポートします。外部ソース（データベース、外部接続など）は、まだキャッシュ API では更新できません。
{{% /alert %}}

このチェーンのため、Aspose.Cells には 2 つの基本的な更新パスがあります。
- **`PivotTable.CalculateData()`** — すでにキャッシュされたデータから単一の `PivotTable` の表示を再計算します。データソースへのラウンドトリップは発生しません。
本記事のすべてのシナリオではワークシートのセルをソースデータとして使用しているため、ソースタイプは `Sheet` となり、更新操作は説明どおりに動作します。

## クイックスタート
ワークブック内のすべてのピボットを更新できるだけ短いコードが必要な場合は、1 回の呼び出しで十分です。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// セルA1:C1にヘッダー行を書き込む
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// セルA2:C9にデータ行を書き込む（2020年と2021年にわたる8行の果物のデータ）
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
// ピボットテーブルを追加：ソース範囲「A1:C9」、配置先セル「E3」、名前「Pivot1」
let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
// ピボットフィールドを割り当て：Fruitを行、Yearを列、Amountをデータ
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// 変更をシミュレートするためにソースデータの複数のAmount値を変更
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// ワークブック内のすべてのピボットテーブル/ピボットキャッシュを更新
workbook.refreshAll();
// ワークブックを保存
workbook.save("output.xlsx");
```

本記事の以降の内容では、代わりにいつより限定的な API を選択すべきかについて説明します。

## 必要なインポート
本記事のすべての JavaScript の例では、Aspose.Cells for Node.js via C++ モジュールが読み込まれ、ピボット関連の型が `Aspose.Cells.Pivot` 名前空間に存在することを前提としています。一般的なセットアップは次のとおりです。
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;`（または `AsposeCells.Pivot.PivotFieldType` 経由でアクセス）

## ワークブック内のすべてのピボットテーブルを更新する
ワークブック内のすべてのピボットキャッシュとすべてのピボットテーブルが最新のソースデータを反映していることを確認する必要がある場合、最もシンプルで包括的な API は `Workbook.RefreshAll()` です。1 回の呼び出しでワークブック全体を走査し、各 `PivotCache` をソースから更新し、それに依存するすべての `PivotTable` を再計算します。パフォーマンスを懸念しない、一般的なドキュメント全体の更新には、このアプローチを推奨します。
次の例では、果物/年度/金額のソース範囲を含むワークブックを作成し、1 つのピボットテーブルを作成して一部のソース値を変更した後、`RefreshAll()` を使用して 1 回の呼び出しで全体を最新の状態にします。

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

## 単一のワークシート上のすべてのピボットテーブルを更新する
特定のワークシート上にあるピボットテーブルのみを更新する必要がある場合があります。たとえば、他のワークシート上にあるピボットテーブルは無関係であり、影響を受けるべきではないことがわかっている場合などです。このような場合のために、Aspose.Cells では単一の `Worksheet` インスタンスを対象とする `Worksheet.RefreshPivotTables()` を提供しています。

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Fruit / Year / Amount のヘッダー行を書き込みます
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// 8 行のデータ行（2〜9 行目）を書き込みます（ソース範囲 A1:C9 に収まります）
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
// 「Pivot1」という名前のピボットテーブルを配置先セル E3 に追加し、ソースは A1:C9 とします
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);
// フィールドを割り当てます：Fruit を行、Year を列、Amount をデータ
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, "Amount");
// 表示／レイアウトのプロパティを変更します — これは表示のみの変更なので、
// PivotCache.Refresh() を介してソースデータを再読み込みする必要はありません。
pivotTable.setRefreshDataOnOpeningFile(false);
// CalculateData() は、PivotCache に保持されているデータから、このピボットテーブルの表示（データ＋スタイル）を再描画します。
// ソースデータは変更されていないため、ソースへのラウンドトリップは行われず、キャッシュされた値のみがワークシートのセルに再計算されます。
pivotTable.calculateData();
// ワークブックをディスクに保存します
workbook.save("output.xlsx");
```

## 単一のピボットテーブルを更新する
単一のピボットテーブルを細かく制御したい場合、キャッシュベースの API には 2 つの選択肢があります。どちらを選ぶかは、実際に何が変わったか、つまり基になるソースデータなのか、それともピボットテーブル自身のビュー/レイアウト設定のみなのかによって決まります。

### ソースデータが変更された場合 — `PivotCache.Refresh()` を使用する
基になるソースデータが変更された場合、正しいエントリポイントは `pivotTable.PivotCache.Refresh()` です。この呼び出しはソースデータをキャッシュに再取り込みし、そのキャッシュに依存するすべての `PivotTable` を再計算します。

### ビュー/レイアウトのみが変更された場合 — `CalculateData()` を使用する
ソースデータは変更されておらず、ピボットテーブルのビューまたはレイアウト設定のみが変更された場合（たとえば、フィールドが別のエリアに移動されたり、開くときに更新する設定が切り替えられたりした場合）、データソースへのラウンドトリップは必要ありません。キャッシュにはすでに正しいデータが保持されており、再計算する必要があるのはレンダリング済みの `PivotTable` のみです。このような場合は、`pivotTable.CalculateData()` が正しい選択です。
次の例では、ピボットテーブルのソース以外のプロパティを変更し、その後 `CalculateData()` を呼び出して既存のキャッシュから再レンダリングします。
ワークブックには、単一の共有キャッシュの上に存在する多くのピボットテーブルが含まれていることがよくあります。これらを列挙するには（たとえば、バッチ更新を実行する前や、共有キャッシュの影響を診断するために）、`PivotCache.GetPivotTables()` を使用します。このメソッドは、指定されたキャッシュに依存するすべての `PivotTable` のコレクションを返します。

## 非推奨の `PivotTable.RefreshData()` からの移行
Aspose.Cells for Node.js via C++ v26.7 より前では、ピボットテーブルを更新する標準的な方法は、各ピボットテーブルに対して個別に `PivotTable.RefreshData()` を呼び出すことでした。v26.7 時点では、この方法は**非推奨**となり、上記のキャッシュ対応 API に置き換える必要があります。
実際のワークブックでは、テーブル単位の `RefreshData()` アプローチに問題がある理由は 2 つあります。
- ソースが変更されていない場合でも、呼び出されるたびにソースからデータを再取得します。
推奨される代替方法は次のとおりです。
次の例では、単一のキャッシュを共有する複数のピボットテーブルを含むワークブックに対する新しい効率的なパターンを示します。

## どの更新 API を使用すべきか？
次の表は、利用可能な更新 API とそれぞれをいつ選択すべきかをまとめたものです。
| 目的 | 推奨 API | メモ |
|------|-----------------|-------|
| ワークブックのすべてを更新する | `Workbook.RefreshAll()` | 1 回の呼び出しですべてのキャッシュとテーブルをカバー。 |
| 単一シート上のピボットテーブルのみを更新する | `Worksheet.RefreshPivotTables()` | 単一のワークシートを対象とします。 |
| 単一キャッシュのソースデータが変更された | `pivotTable.PivotCache.Refresh()` | 共有キャッシュ上のすべてのピボットテーブルを更新します。 |
| ビュー/レイアウト設定のみが変更された | `pivotTable.CalculateData()` | 不要なソースへのラウンドトリップをスキップします。 |
| 共有キャッシュ上のすべてのピボットテーブルを一覧表示する | `pivotCache.GetPivotTables()` | 一括更新の前に列挙するために使用。 |
実際には、非推奨のテーブル単位の `RefreshData()` よりもキャッシュベースの API を優先してください。共有キャッシュを認識し、冗長なソース取得を回避し、更新要件を満たす最小限のスコープを選択できます。

## よくある落とし穴
- **保存前に更新するのを忘れる。** ピボットテーブルは、データチェーンが更新されたときにのみ、レンダリング済みの値をワークシートに書き込みます。ソースのセルを変更した場合は、`Workbook.save()` の前に `PivotCache.Refresh()`（または `Workbook.RefreshAll()`）を呼び出してください。さもないと、保存されたファイルには古い集計値が残ったままになります。
- **テーブルごとに非推奨の `RefreshData()` を呼び出す。** v26.7 では、`PivotTable.RefreshData()` は非推奨となり、呼び出しごとにソースを再取得します。単一のキャッシュを共有する複数のピボットテーブルがある場合、これは N 回の冗長なソース取得を意味します。`PivotCache.Refresh()` を 1 回呼び出し、その後テーブルごとに `CalculateData()` を呼び出すように置き換えてください。
- **レイアウトのみが変更された場合に更新する。** ソースデータを変更せずにピボットテーブルのビュー（列の順序、`ConsolidationFunction` など）のみを変更した場合、`PivotCache.Refresh()` は不要で、処理が遅くなります。`pivotTable.CalculateData()` を呼び出して、既存のキャッシュから再レンダリングしてください。
- **`PivotCache.Refresh()` でサポートされない外部ソース。** ピボットテーブルのソースが外部接続（データベース、OLAP キューブなど）からのものである場合、v26.7 では `PivotCache.Refresh()` でそれを更新できません。現時点では `Sheet` と `Consolidation` のソースタイプのみをサポートしています。外部ソースの場合は、ワークブックを再度開くか、ソースからキャッシュを再構築してください。

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}