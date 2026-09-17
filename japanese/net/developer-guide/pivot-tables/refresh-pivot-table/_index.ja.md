---
title: Aspose.Cells for .NET でピボットテーブルとピボットキャッシュを更新する
linktitle: Aspose.Cells for .NET でピボットテーブルとピボットキャッシュを更新する
description: Aspose.Cells for .NET で v26.7+ のピボット更新 API を使用してピボットテーブルを更新する方法を学びます。この記事では RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData、GetPivotTables を実用的なコード例とともに解説します。
keywords: Aspose.Cells, .NET, ピボットテーブル, 更新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ja/net/refresh-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells はレイヤード更新 API を提供しており、ワークブック全体から単一のピボットテーブルまで、4 つの異なるスコープでピボットデータを再読み込みできます。**Aspose.Cells for .NET v26.7** 以降、レガシーメソッド `PivotTable.RefreshData()` は obsolete（廃止予定）としてマークされているため、この記事で説明するより効率的でキャッシュ対応の API に置き換える必要があります。
{{% /alert %}}

## はじめに
ピボットテーブルの更新は、単一の操作であることはまれです。背後では、Aspose.Cells は元のソースデータとワークシートに表示されるレンダリング済みの値を結ぶレイヤードデータチェーンを維持しています。このチェーンを理解することが、あらゆる状況で適切な更新 API を選択する鍵となります。
4 層データチェーンは以下のとおりです。
1. **データソース** — 生の値が存在する元のワークシート範囲、データベースクエリ、または統合範囲。
2. **PivotCache** — ソースデータのインメモリスナップショット。すべてのピボットテーブルは `PivotCache` の上に構築され、ここで全データが収集・集計されます。
3. **PivotTable** — 行、列、値、フィルターフィールドを定義するビューオブジェクト。`PivotTable` はデータソースから直接ではなく、`PivotCache` からのみデータを読み取ります。
4. **Cells** — `PivotTable` が計算された値と書式をレンダリングするワークシートの `Cells`。

{{% alert color="primary" %}}
`PivotCache.SourceType`（enum `PivotTableSourceType`）は、キャッシュデータの取得元を示します。v26.7 時点で、`PivotCache.Refresh()` は **`Sheet`** および **`Consolidation`** ソースタイプのみをサポートします。つまり、ワークシート範囲に存在するデータのみが対象です。外部ソース（データベース、外部接続など）は、キャッシュ API ではまだ更新できません。
{{% /alert %}}

このチェーンのため、Aspose.Cells には 2 つの基本的な更新パスがあります。
- **`PivotTable.CalculateData()`** — データソースへのラウンドトリップなしで、すでにキャッシュされたデータから 1 つの `PivotTable` の表示を再計算します。
この記事のすべてのシナリオではワークシートセルをソースデータとして使用しているため、ソースタイプは `Sheet` であり、更新操作は説明どおりに動作します。

## クイックスタート
ワークブック内のすべてのピボットを更新する最小限のコードだけが必要な場合は、1 回の呼び出しで十分です。

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

この記事の他のすべてのセクションでは、より狭いスコープの API を選択すべき場面について説明します。

## 必要な Using ディレクティブ
この記事のすべての C# の例は、ピボットタイプが `Aspose.Cells.Pivot` 名前空間に存在するため、次の 3 つの using ディレクティブから始まります。
- `using System;`
- `using Aspose.Cells;`
- `using Aspose.Cells.Pivot;`

## ワークブック内のすべてのピボットテーブルを更新する
ワークブック内のすべてのピボットキャッシュとすべてのピボットテーブルが最新のソースデータを反映するようにする必要がある場合、最もシンプルで包括的な API は `Workbook.RefreshAll()` です。1 回の呼び出しでワークブック全体を走査し、各 `PivotCache` をソースから更新し、次にそのキャッシュに依存するすべての `PivotTable` を再計算します。これは、パフォーマンスが重要でない一般的なフルドキュメント更新の推奨されるアプローチです。
次の例では、Fruit/Year/Amount のソース範囲を持つワークブックを作成し、1 つのピボットテーブルを作成して、いくつかのソース値を変更し、その後 `RefreshAll()` を使用してすべてを 1 回の呼び出しで最新状態にします。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// 新しいワークブックを作成する
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// セルA1:C1にヘッダー行を書き込む
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// セルA2:C9にデータ行を書き込む（2020年と2021年にわたる8行の果物データ）
worksheet.Cells["A2"].PutValue("grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(50);
worksheet.Cells["A3"].PutValue("blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(60);
worksheet.Cells["A4"].PutValue("kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(70);
worksheet.Cells["A5"].PutValue("cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(80);
worksheet.Cells["A6"].PutValue("grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(90);
worksheet.Cells["A7"].PutValue("blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(100);
worksheet.Cells["A8"].PutValue("kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(110);
worksheet.Cells["A9"].PutValue("cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(120);
// ピボットテーブルを追加する：ソース範囲「A1:C9」、配置先セル「E3」、名前「Pivot1」
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
// ピボットフィールドを割り当てる：Fruitを行、Yearを列、Amountをデータ
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// ソースデータの複数のAmount値を変更して変更をシミュレートする
worksheet.Cells["C2"].PutValue(55);
worksheet.Cells["C5"].PutValue(85);
worksheet.Cells["C9"].PutValue(125);
// ワークブック内のすべてのピボットテーブル/ピボットキャッシュを更新する
workbook.RefreshAll();
// ワークブックを保存する
workbook.Save("output.xlsx");
```

## 単一のワークシート上のすべてのピボットテーブルを更新する
特定のワークシート上にあるピボットテーブルだけを更新する必要がある場合もあります。たとえば、他のワークシート上のピボットテーブルは無関係であり、触れてはいけないことが分かっている場合です。このようなシナリオのために、Aspose.Cells は単一の `Worksheet` インスタンスにスコープされた `Worksheet.RefreshPivotTables()` を提供します。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
worksheet.Cells["A2"].PutValue("grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);
worksheet.Cells["A3"].PutValue("blueberry");
worksheet.Cells["B3"].PutValue(2021);
worksheet.Cells["C3"].PutValue(150);
worksheet.Cells["A4"].PutValue("kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(200);
worksheet.Cells["A5"].PutValue("cherry");
worksheet.Cells["B5"].PutValue(2021);
worksheet.Cells["C5"].PutValue(120);
worksheet.Cells["A6"].PutValue("grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(180);
worksheet.Cells["A7"].PutValue("blueberry");
worksheet.Cells["B7"].PutValue(2020);
worksheet.Cells["C7"].PutValue(130);
worksheet.Cells["A8"].PutValue("kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(220);
worksheet.Cells["A9"].PutValue("cherry");
worksheet.Cells["B9"].PutValue(2020);
worksheet.Cells["C9"].PutValue(140);
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
worksheet.Cells["C2"].PutValue(300);
worksheet.Cells["C5"].PutValue(250);
worksheet.Cells["C9"].PutValue(400);
worksheet.RefreshPivotTables();
workbook.Save("output.xlsx");
```

## 単一のピボットテーブルを更新する
単一のピボットテーブルを細かく制御したい場合、キャッシュベースの API には 2 つのオプションがあります。どちらを選択するかは、実際に何が変わったか、つまり基になるソースデータなのか、それともピボットテーブル自体のビュー/レイアウト設定だけなのかによって決まります。

### ソースデータが変更された場合 — `PivotCache.Refresh()` を使用する
基になるソースデータが変更された場合、正しいエントリポイントは `pivotTable.PivotCache.Refresh()` です。この呼び出しはソースデータをキャッシュに再読み込みし、そのキャッシュに依存するすべての `PivotTable` を再計算します。

### ビュー/レイアウトのみが変更された場合 — `CalculateData()` を使用する
ソースデータは変更されておらず、ピボットテーブルのビューやレイアウト設定のみが変更された場合（たとえば、フィールドが別のエリアに移動されたり、開くときに更新する設定が切り替えられたりした場合）、データソースへのラウンドトリップは必要ありません。キャッシュにはすでに正しいデータが保持されており、レンダリングされた `PivotTable` の再計算のみが必要です。この場合、`pivotTable.CalculateData()` が正しい選択です。
次の例では、ピボットテーブルのソース以外のプロパティを変更し、その後 `CalculateData()` を呼び出して既存のキャッシュから再レンダリングします。

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
// Fruit / Year / Amount のヘッダー行を書き込み
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// 8 行のデータ行を書き込み (行 2-9、ソース範囲 A1:C9 に合わせる)
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);
worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);
worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);
worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);
worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(150);
worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(250);
worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(350);
worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(450);
// "Pivot1" という名前のピボット テーブルを宛先セル E3 に追加し、A1:C9 をソースとする
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.PivotTables[pivotIndex];
// フィールドを割り当て: Fruit を行、Year を列、Amount をデータ
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// 表示/レイアウトのプロパティを変更 — これは表示のみの変更であり、
// PivotCache.Refresh() を介してソース データを再読み込みする必要はない
pivotTable.RefreshDataOnOpeningFile = false;
// CalculateData() は、PivotCache に既に保持されているデータから、
// このピボット テーブルの表示 (データ + スタイル) を再レンダリングする。ソース データが変更されていないため、
// ソースへのラウンドトリップは行われず、キャッシュされた値のみが再計算される
// ワークシートのセルに反映される
pivotTable.CalculateData();
// ワークブックをディスクに保存
workbook.Save("output.xlsx");
```

ワークブックには多くのピボットテーブルが含まれており、それらはすべて 1 つの共有キャッシュ上にあります。これらを列挙するには（たとえば、バッチ更新を実行する前、または共有キャッシュの影響を診断するために）、`PivotCache.GetPivotTables()` を使用します。このメソッドは、指定されたキャッシュに依存するすべての `PivotTable` のコレクションを返します。

## 廃止予定の `PivotTable.RefreshData()` からの移行
Aspose.Cells for .NET v26.7 より前では、ピボットテーブルを更新する標準的な方法は、各ピボットテーブルで個別に `PivotTable.RefreshData()` を呼び出すことでした。v26.7 以降、このメソッドは **obsolete（廃止予定）** としてマークされているため、上記で説明したキャッシュ対応の API に置き換える必要があります。
実世界のワークブックでは、テーブルごとの `RefreshData()` アプローチに問題がある理由が 2 つあります。
- ソースが変更されていない場合でも、呼び出すたびにソースからデータを再取得します。
推奨される置き換えは次のとおりです。
次の例は、単一のキャッシュを共有する複数のピボットテーブルを持つワークブックの新しい効率的なパターンを示しています。

## どの更新 API を使用すべきか
次の表は、利用可能な更新 API とそれぞれの選択すべき場面をまとめたものです。
| 目的 | 推奨 API | メモ |
|------|-----------------|-------|
| ワークブック内のすべてを更新する | `Workbook.RefreshAll()` | 1 回の呼び出しで、すべてのキャッシュとテーブルをカバーします。 |
| 単一シート上のピボットテーブルだけ更新する | `Worksheet.RefreshPivotTables()` | 1 つのワークシートにスコープされます。 |
| 1 つのキャッシュのソースデータが変更された | `pivotTable.PivotCache.Refresh()` | その共有キャッシュ上のすべてのピボットテーブルを更新します。 |
| ビュー/レイアウト設定のみが変更された | `pivotTable.CalculateData()` | 不要なソースへのラウンドトリップをスキップします。 |
| 共有キャッシュ上のすべてのピボットテーブルを列挙する | `pivotCache.GetPivotTables()` | 一括更新の前に列挙するために使用します。 |
実際には、廃止予定のテーブルごとの `RefreshData()` よりもキャッシュベースの API を優先してください。共有キャッシュを認識し、冗長なソース取得を回避し、更新要件を満たす最小限のスコープを選択できます。

## 一般的な落とし穴
- **保存前に更新し忘れる。** ピボットテーブルは、データチェーンが更新されたときにのみ、レンダリングされた値をワークシートに書き込みます。ソースセルを変更した場合は、`Workbook.Save()` の前に `PivotCache.Refresh()`（または `Workbook.RefreshAll()`）を呼び出してください。そうしないと、保存されたファイルには古い集計値が含まれてしまいます。
- **廃止予定の `RefreshData()` をテーブルごとに呼び出す。** v26.7 では、`PivotTable.RefreshData()` は obsolete としてマークされており、呼び出しごとにソースを再取得します。キャッシュを共有する複数のピボットテーブルがある場合、これは N 回の冗長なソース取得を意味します。単一の `PivotCache.Refresh()` を呼び出し、その後にテーブルごとに `CalculateData()` を呼び出すように置き換えてください。
- **レイアウトのみが変更された場合に更新する。** ソースデータを変更せずにピボットテーブルのビューのみ（列の順序、`ConsolidationFunction` など）を変更した場合、`PivotCache.Refresh()` は不要であり、遅くなります。`pivotTable.CalculateData()` を呼び出して、既存のキャッシュから再レンダリングしてください。
- **外部ソースは `PivotCache.Refresh()` でサポートされない。** ピボットテーブルのソースが外部接続（データベース、OLAP キューブなど）から取得される場合、v26.7 では `PivotCache.Refresh()` で更新できません。現在、`Sheet` および `Consolidation` ソースタイプのみがサポートされています。外部ソースの場合は、ワークブックを再度開くか、ソースからキャッシュを再構築してください。

{{< app/cells/assistant language="csharp" >}}