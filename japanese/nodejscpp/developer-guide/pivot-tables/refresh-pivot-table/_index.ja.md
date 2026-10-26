---
title: Aspose.Cells for Node.js via C++ でピボットテーブルと PivotCache を更新
linktitle: Aspose.Cells for Node.js via C++ でピボットテーブルと PivotCache を更新
description: v26.7 以降のピボット更新 API を使用して Aspose.Cells for Node.js via C++ でピボットテーブルを更新する方法を学びます。この記事では、refreshAll、refreshPivotTables、PivotCache.refresh、calculateData、getPivotTables を実践的なコード例とともに説明します。
keywords: Aspose.Cells, Node.js via C++, ピボットテーブル, 更新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ja/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ワークブック全体から単一のピボットテーブルまで、4 つの異なるスコープでピボットデータを再読み込みできる多層的な更新 API を提供します。**Aspose.Cells for Node.js via C++ v26.7** から、旧来のメソッド `PivotTable.RefreshData()` は非推奨とされ、この記事でお説明している、より効率的でキャッシュに対応した API に置き換える必要があります。
{{% /alert %}}

## Introduction
ピボットテーブルの更新が単一の操作にとどまることは、ほとんどありません。その裏側では、Aspose.Cells は元のソースデータとワークシートに表示されるレンダリング済みの値を結ぶ、多層的なデータチェーンを維持しています。このチェーンを理解することが、状況に適した更新 API を選択する鍵になります。
4 層のデータチェーンは次のとおりです。
1. **データソース** — 生の値が格納されている、元のワークシート範囲、データベースクエリ、または統合範囲です。
2. **PivotCache** — ソースデータのインメモリスナップショットです。各ピボットテーブルは `PivotCache` の上に構築され、すべてのデータはこの場所で収集および集計されます。
3. **PivotTable** — 行、列、値、およびフィルターを定義するフィールドのビューオブジェクトです。`PivotTable` はデータソースから直接読み取られるのではなく、`PivotCache` からのみ読み取ります。
4. **Cells** — `PivotTable` が計算値とスタイルをレンダリングする、ワークシートの `Cells` です。

{{% alert color="primary" %}}
`PivotCache.SourceType`（列挙型 `PivotTableSourceType`）は、キャッシュデータの取得元を示します。v26.7 の時点で、`PivotCache.refresh()` がサポートするのは **`Sheet`** と **`Consolidation`** のソースタイプ、つまりワークシート範囲に格納されているデータのみです。外部ソース（データベース、外部接続など）は、現時点ではキャッシュ API 経由で更新できません。
このチェーンにより、Aspose.Cells には 2 つの基本的な更新パスがあります。
- **`PivotTable.calculateData()`** — データソースへの往復通信なしに、キャッシュ済みのデータから 1 つの `PivotTable` の表示を再計算します。
この記事のすべてのシナリオではワークシートセルのソースデータを使用するため、ソースタイプは `Sheet` となり、更新操作は説明どおりに動作します。
{{% /alert %}}

## Quick Start
ワークブック内のすべてのピボットを更新するための最小限のコードだけが必要なら、1 回の呼び出しで十分です。

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

それ以外の詳細については、より範囲が狭い API を選ぶべき場合について説明します。

## Required Imports
この記事の JavaScript の例では、Aspose.Cells for Node.js via C++ モジュールが読み込まれ、ピボット型が `Aspose.Cells.Pivot` namespace に存在すると仮定しています。典型的なセットアップは次のとおりです。
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;`（または `AsposeCells.Pivot.PivotFieldType` 経由でアクセス）

## Refresh All Pivot Tables in the Workbook
ワークブック内のすべてのピボットキャッシュとすべてのピボットテーブルを最新のソースデータに合わせる必要がある場合、最も単純で包括的な API は `Workbook.refreshAll()` です。1 回の呼び出しでワークブック全体を処理し、各 `PivotCache` をそのソースから更新してから、依存するすべての `PivotTable` を再計算します。性能が問題にならない一般的な文書全体の更新では、この方法を推奨します。
次の例では、Fruit/Year/Amount のソース範囲を持つワークブックを作成し、1 つのピボットテーブルを生成して一部のソース値を変更してから、`refreshAll()` を 1 回呼び出してすべてを最新の状態に更新します。

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Write header row into cells A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
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
// Add a pivot table: source range "A1:C9", destination cell "E3"
let pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
// Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Modify several Amount values in the source data to simulate changes
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Refresh every pivot table / pivot cache in the workbook
workbook.refreshAll();
// Save the workbook
workbook.save("output.xlsx");
```

## Refresh All Pivot Tables on a Single Worksheet
他のワークシート上のピボットテーブルは更新対象ではないことが分かっている場合など、特定のワークシート上にあるピボットテーブルだけを更新する必要がある場合があります。この場合、Aspose.Cells は 1 つの `Worksheet` インスタンスに範囲が限定された `Worksheet.refreshPivotTables()` を提供します。

```javascript
const AsposeCells = require("aspose.cells.node");
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
let pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## Refresh a Single Pivot Table
単一のピボットテーブルを細かく制御したい場合は、キャッシュベースの API に 2 つの選択肢があります。どちらを選ぶかは、実際に変更されたものがピボットテーブルの基盤となるソースデータか、表示やレイアウトの設定だけかによって異なります。

### Source Data Changed — Use `PivotCache.refresh()`
基盤となるソースデータが変更された場合は、`pivotTable.PivotCache.refresh()` が適切なエントリーポイントです。この呼び出しはソースデータをキャッシュに再読み込みし、そのキャッシュに依存するすべての `PivotTable` を再計算します。

### Only View/Layout Changed — Use `calculateData()`
ソースデータが変更されておらず、ピボットテーブルの表示またはレイアウト設定だけが変更された場合（フィールドを別の領域に移動した場合や、開くときに更新する設定を切り替えた場合など）、データソースへの往復通信は必要ありません。キャッシュにはすでに正しいデータが格納されているため、再計算が必要なのはレンダリング済みの `PivotTable` だけです。この場合は、`pivotTable.calculateData()` が適切です。
次の例では、ピボットテーブルのソースデータ以外のプロパティを変更し、既存のキャッシュから `calculateData()` で再レンダリングします。

```javascript
const AsposeCells = require("aspose.cells.node");
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Write Fruit / Year / Amount header row
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Write 8 data rows (rows 2-9, fitting the source range A1:C9)
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
// Add a pivot table placed at destination cell E3, sourcing from A1:C9
var pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
// Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Modify a view/layout property — this is a presentation-only change,
// so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() re-renders THIS pivot table's display (data + style) from the
// data already held in the PivotCache. Because the source data did not change,
// no round-trip to the source is performed — only the cached values are recalculated
// into worksheet cells.
pivotTable.calculateData();
// Save the workbook to disk
workbook.save("output.xlsx");
```

1 つの共有キャッシュの上に構築されたピボットテーブルが多数含まれるワークブックもあります。一括更新の前にそれらを列挙する場合や、共有キャッシュの影響を診断する場合は、`PivotCache.getPivotTables()` を使用します。このメソッドは、指定したキャッシュに依存するすべての `PivotTable` のコレクションを返します。

## Migrating from the Obsolete `PivotTable.RefreshData()`
Aspose.Cells for Node.js via C++ v26.7 より前、ピボットテーブルを更新する標準的な方法は、各ピボットテーブルで `PivotTable.RefreshData()` を個別に呼び出すことでした。v26.7 では、このメソッドは**非推奨**とされ、上で説明したキャッシュ対応 API に置き換える必要があります。
実際のワークブックでは、テーブルごとの `RefreshData()` の使用が問題になる理由は 2 つあります。
- ソースが変更されていなくても、呼び出すたびにソースからデータを再取得します。
推奨される置き換え方法は次のとおりです。
次の例は、複数のピボットテーブルが 1 つのキャッシュを共有するワークブックにおける、新しい効率的方法を示しています。

## Which Refresh API Should I Use?
以下の表は、利用可能な更新 API と、それぞれの選択機会をまとめたものです。
| 目的 | 推奨 API | 備考 |
|------|-----------------|-------|
| ワークブック内のすべてを更新する | `Workbook.refreshAll()` | 1 回の呼び出しで、すべてのキャッシュとテーブルを網羅します。 |
| 単一のシート上にあるピボットテーブルだけを更新する | `Worksheet.refreshPivotTables()` | 1 つのワークシートに範囲が限定されます。 |
| 1 つのキャッシュのソースデータが変更された | `pivotTable.PivotCache.refresh()` | その共有キャッシュに依存するすべてのピボットテーブルを更新します。 |
| 表示やレイアウトの設定だけが変更された | `pivotTable.calculateData()` | 不要なソースへの往復通信を省略します。 |
| 共有キャッシュ上のすべてのピボットテーブルを一覧表示する | `pivotCache.getPivotTables()` | 一括更新の前に列挙する場合に使用します。 |
実際の使用では、非推奨のテーブルごとの `RefreshData()` よりも、キャッシュベースの API を優先してください。これらの API は共有キャッシュを考慮し、冗長なソース取得を避け、更新要件を満たす最小のスコープを選択できます。

## Common Pitfalls
- **保存前に更新することを忘れる。** ピボットテーブルは、データチェーンが更新されたときにのみ、レンダリング済みの値をワークシートに書き込みます。ソースセルを変更した場合は、`Workbook.save()` の前に `PivotCache.refresh()`（または `Workbook.refreshAll()`）を呼び出してください。そうでなければ、保存されるファイルには古い集計値が含まれます。
- **テーブルごとに非推奨の `RefreshData()` を呼び出す。** v26.7 では、`PivotTable.RefreshData()` は非推奨とされ、呼び出しごとにソースを再取得します。複数のピボットテーブルが 1 つのキャッシュを共有している場合、N 回の冗長なソース取得を行うことになります。`PivotCache.refresh()` を 1 回呼び出す方法に置き換え、その後、テーブルごとに `calculateData()` を呼び出します。
- **レイアウトのみが変更されたのに更新する。** ソースデータに手を触れずにピボットテーブルの表示（列の順序、`ConsolidationFunction` など）のみを変更した場合、`PivotCache.refresh()` は不要で低速です。既存のキャッシュから再レンダリングするには、`pivotTable.calculateData()` を呼び出してください。
- **`PivotCache.refresh()` では外部ソースがサポートされていない。** ピボットテーブルのソースが外部接続（データベース、OLAP キューブなど）に由来する場合、v26.7 では `PivotCache.refresh()` で更新できません。現在サポートされているソースタイプは `Sheet` と `Consolidation` のみです。外部ソースの場合は、ワークブックを開き直すか、ソースからキャッシュを再構築してください。

{{< app/cells/assistant language="nodejs-cpp" >}}