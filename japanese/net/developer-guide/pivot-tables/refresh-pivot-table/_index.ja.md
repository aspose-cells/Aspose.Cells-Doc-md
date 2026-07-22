---
title: Aspose.Cells for .NET でのピボットテーブルの更新
linktitle: ピボットテーブルの更新
description: Aspose.Cells for .NET で v26.7+ のピボット更新 API を使用してピボットテーブルを更新する方法を学びます。本記事では RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData、GetPivotTables を実用的なコード例とともに解説します。
keywords: Aspose.Cells, .NET, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ja/net/refresh-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は、ワークブック全体から単一のピボットテーブルまで、4 つの異なるスコープでピボットデータを再読み込みできる階層的な更新 API を提供します。**Aspose.Cells for .NET v26.7** 以降、従来のメソッド `PivotTable.RefreshData()` は obsolete（廃止予定）となり、本記事で説明するより効率的でキャッシュ対応の API に置き換える必要があります。

{{% /alert %}}

## 概要

ピボットテーブルの更新は、単一の操作であることは稀です。内部的には、Aspose.Cells は元のソースデータとワークシートに表示されるレンダリング済みの値を結ぶ階層的なデータチェーンを維持しています。このチェーンを理解することが、あらゆる状況において適切な更新 API を選択する鍵となります。

4 層のデータチェーンは次のとおりです。

1. **データソース** — 元のワークシート範囲、データベースクエリ、または統合範囲。生データがここに存在します。
2. **PivotCache** — ソースデータのインメモリスナップショットです。すべてのピボットテーブルは `PivotCache` の上に構築され、すべてのデータはこの場所で収集・集計されます。
3. **PivotTable** — 行、列、値、フィルタフィールドを定義するビューオブジェクトです。`PivotTable` はデータソースから直接ではなく、`PivotCache` からのみ読み取ります。
4. **Cells** — `PivotTable` が計算済みの値やスタイルを描画する先のワークシートの `Cells`。

特に重要な概念は **共有キャッシュ** です。ワークブック内の複数のピボットテーブルが同じソース範囲を参照している場合、それらは *1 つの* `PivotCache` インスタンスを共有します。1 つの `PivotCache` は多くのピボットテーブルから参照でき、そのキャッシュを更新すると、依存するすべての `PivotTable` が一度に更新されます。

{{% alert color="primary" %}}

`PivotCache.SourceType`（列挙型 `PivotTableSourceType`）は、キャッシュデータの取得元を示します。v26.7 時点で、`PivotCache.Refresh()` は **`Sheet`** および **`Consolidation`** のソースタイプ、つまりワークシート範囲に存在するデータのみをサポートしています。外部ソース（データベース、外部接続など）は、まだキャッシュ API 経由では更新できません。

{{% /alert %}}

このチェーンのため、Aspose.Cells には 2 つの基本的な更新パスがあります。

- **`PivotCache.Refresh()`** — ソースからキャッシュへデータを再読み込みし、依存するすべての `PivotTable` を 1 回の操作で再計算します。
- **`PivotTable.CalculateData()`** — 既にキャッシュされたデータから、1 つの `PivotTable` の表示を再計算します。データソースへのラウンドトリップは行いません。

本記事のすべてのシナリオではワークシートセルのソースデータを使用しているため、ソースタイプは `Sheet` であり、更新操作は説明したとおりに動作します。

## 必要な Using ディレクティブ

本記事のすべての C# コード例は、ピボットタイプが `Aspose.Cells.Pivot` 名前空間に存在するため、以下の 3 つの using ディレクティブから始まります。

- `using System;`
- `using Aspose.Cells;`
- `using Aspose.Cells.Pivot;`

## ワークブック内のすべてのピボットテーブルを更新する

ワークブック内のすべてのピボットキャッシュとすべてのピボットテーブルが最新のソースデータを反映するようにする必要がある場合、最もシンプルで包括的な API は `Workbook.RefreshAll()` です。1 回の呼び出しでワークブック全体を走査し、各 `PivotCache` をソースから更新し、その後、依存するすべての `PivotTable` を再計算します。これは、パフォーマンスが問題にならない一般的なドキュメント全体の更新に対して推奨されるアプローチです。

次の例では、Fruit/Year/Amount のソース範囲を持つワークブックを作成し、1 つのピボットテーブルを作成し、一部のソース値を変更してから、`RefreshAll()` を使用してすべてを 1 回の呼び出しで最新の状態にしています。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// 新しいワークブックを作成
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// A1:C1のセルにヘッダー行を書き込み
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// A2:C9のセルにデータ行を書き込み（2020年と2021年にわたる8行のフルーツデータ）
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

// ピボットテーブルを追加：ソース範囲「A1:C9」、配置先セル「E3」、名前「Pivot1」
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// ピボットフィールドを割り当て：FruitをRows、YearをColumns、AmountをDataに
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// ソースデータの複数のAmount値を変更して変更をシミュレート
worksheet.Cells["C2"].PutValue(55);
worksheet.Cells["C5"].PutValue(85);
worksheet.Cells["C9"].PutValue(125);

// ワークブック内のすべてのピボットテーブル/ピボットキャッシュを更新
workbook.RefreshAll();

// ワークブックを保存
workbook.Save("output.xlsx");
```

## 単一のワークシート上のすべてのピボットテーブルを更新する

特定のワークシート上にあるピボットテーブルだけを更新する必要がある場合があります。たとえば、他のワークシート上のピボットテーブルは無関係であり、触らないことがわかっている場合などです。このケースのために、Aspose.Cells は `Worksheet.RefreshPivotTables()` を提供しており、単一の `Worksheet` インスタンスにスコープされます。

これは `Workbook.RefreshAll()` よりも選択的です。対象となるワークシート上のピボットテーブルのみが更新され、他のワークシート上のピボットテーブルはそのまま残ります。

次の例では、同じ Fruit/Year/Amount のソースデータを入力し、最初のワークシートにピボットテーブルを追加し、一部のソース値を変更してから、そのワークシート上のピボットテーブルのみを更新しています。

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

単一のピボットテーブルを細かく制御したい場合、キャッシュベースの API には 2 つのオプションがあります。どちらを選択するかは、実際に変更された内容、つまり基になるソースデータなのか、それともピボットテーブル自体の表示/レイアウト設定のみなのかによって異なります。

### ソースデータが変更された場合 — `PivotCache.Refresh()` を使用する

基になるソースデータが変更された場合、正しいエントリポイントは `pivotTable.PivotCache.Refresh()` です。この呼び出しはソースデータをキャッシュに再読み込みし、そのキャッシュに依存するすべての `PivotTable` を再計算します。

{{% alert color="primary" %}}

ピボットテーブルは単一の `PivotCache` インスタンスを共有するため、`PivotCache.Refresh()` を呼び出すと、参照している 1 つだけでなく、**同じ** キャッシュ上に構築された **すべての** ピボットテーブルが再計算されます。2 つのピボットテーブルが同じソース範囲を共有している場合、1 つのキャッシュを更新すると両方が更新されます。

{{% /alert %}}

次の例では、同じソース範囲上に 2 つのピボットテーブルを作成し、この共有キャッシュの動作をデモンストレーションし、一部のソース値を変更してから、1 つのキャッシュ参照を介して更新しています。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// 新しいワークブックを作成し、最初のワークシートにアクセスします
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// ヘッダー行を書き込みます: Fruit / Year / Amount
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// 約9行のデータ行を書き込みます(2020〜2021年にわたる grape / blueberry / kiwi / cherry)
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
worksheet.Cells["C6"].PutValue(500);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);

// セルE3に配置される最初のピボットテーブル「Pivot1」を追加します。ソース範囲はA1:C9です
int pivotIndex1 = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.PivotTables[pivotIndex1];

// Pivot1にフィールドを割り当てます
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

// 同じソース範囲A1:C9を使用して、E15に配置される2番目のピボットテーブル「Pivot2」を追加します
// ソース範囲が同一であるため、Pivot1とPivot2は単一のPivotCacheを共有します。
int pivotIndex2 = worksheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.PivotTables[pivotIndex2];

// Pivot2にも同じフィールドを割り当てます
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

// データ変更をシミュレートするために、ソースデータの複数のAmountセルの値を変更します
worksheet.Cells["C2"].PutValue(150);
worksheet.Cells["C4"].PutValue(350);
worksheet.Cells["C7"].PutValue(650);

// 共有されているPivotCacheを更新します。
// Pivot1とPivot2は同じPivotCacheを共有しているため、この1回の呼び出しで
// 更新されたソースから両方のピボットテーブル(データ+スタイル)を更新します。
pivotTable1.PivotCache.Refresh();

// ワークブックを保存します
workbook.Save("output.xlsx");
```

### 表示/レイアウトのみが変更された場合 — `CalculateData()` を使用する

ソースデータは変更されておらず、ピボットテーブルの表示やレイアウト設定のみが変更された場合（たとえば、フィールドが別のエリアに移動された、またはファイルを開くときに更新する設定が切り替えられたなど）、データソースへラウンドトリップする必要はありません。キャッシュにはすでに正しいデータが保持されており、レンダリングされた `PivotTable` の再計算のみが必要です。この場合、`pivotTable.CalculateData()` が正しい選択です。

これにより、不要なソースフェッチを回避でき、多くのピボットテーブルが同じキャッシュを共有している場合は大幅に高速になります。

次の例では、ピボットテーブルのソース以外のプロパティを変更し、その後 `CalculateData()` を呼び出して既存のキャッシュから再レンダリングしています。

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];

// Fruit / Year / Amount のヘッダー行を書き込み
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// 8 つのデータ行を書き込み (2-9 行目、ソース範囲 A1:C9 に適合)
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

// "Pivot1" という名前のピボットテーブルを追加。配置先セル E3、ソース範囲 A1:C9
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.PivotTables[pivotIndex];

// フィールドを割り当て: Fruit を行、Year を列、Amount をデータ
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// 表示/レイアウトプロパティの変更 - これは表示のみの変更です。
// したがって PivotCache.Refresh() を通じてソースデータを再読み込みする必要はありません。
pivotTable.RefreshDataOnOpeningFile = false;

// CalculateData() は、PivotCache に保持されているデータから
// このピボットテーブルの表示 (データ + スタイル) を再レンダリングします。
// ソースデータが変更されていないため、ソースへのラウンドトリップは実行されません -
// キャッシュされた値のみが再計算され、ワークシートのセルに反映されます。
pivotTable.CalculateData();

// ワークブックをディスクに保存
workbook.Save("output.xlsx");
```

## 同じ PivotCache を共有するすべてのピボットテーブルを取得する

ワークブックには、1 つの共有キャッシュの上にすべて存在する多くのピボットテーブルが含まれていることがよくあります。これらを列挙するには（たとえば、一括更新を実行する前や、共有キャッシュの影響を診断するために）、`PivotCache.GetPivotTables()` を使用します。このメソッドは、指定されたキャッシュに依存するすべての `PivotTable` のコレクションを返します。

これは、2 つのピボットテーブルが実際に同じ `PivotCache` インスタンスを共有していることを確認する最も直接的な方法でもあります。キャッシュ参照を比較したり、`GetPivotTables()` が返したコレクションを反復処理してどのピボットテーブルが含まれているかを観察したりできます。

次の例では、同じソース範囲上に 2 つのピボットテーブルを作成し、それらが同じキャッシュインスタンスを共有していることを確認してから、キャッシュのピボットテーブルを列挙しています。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Sheet1";

worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

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
worksheet.Cells["C6"].PutValue(500);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(900);

int pivot1Index = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.PivotTables[pivot1Index];
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

int pivot2Index = worksheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.PivotTables[pivot2Index];
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

bool sameCache = object.ReferenceEquals(pivotTable1.PivotCache, pivotTable2.PivotCache);
Console.WriteLine("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

PivotTable[] sharedPivotTables = pivotTable1.PivotCache.GetPivotTables();
Console.WriteLine("Number of pivot tables sharing the cache: " + sharedPivotTables.Length);

foreach (PivotTable pt in sharedPivotTables)
{
    Console.WriteLine("Pivot table name: " + pt.Name);
}

workbook.Save("output.xlsx");
```

## 廃止予定の `PivotTable.RefreshData()` からの移行

Aspose.Cells for .NET v26.7 より前では、ピボットテーブルを更新する標準的な方法は、各ピボットテーブルに対して個別に `PivotTable.RefreshData()` を呼び出すことでした。v26.7 以降、このメソッドは **obsolete**（廃止予定）としてマークされており、上記で説明したキャッシュ対応の API に置き換える必要があります。

実際のワークブックでは、テーブルごとの `RefreshData()` アプローチに問題がある理由は 2 つあります。

- ソースが変更されていない場合でも、呼び出すたびにソースからデータを再取得します。
- 呼び出しごとに共有キャッシュ全体が更新されます。多くのピボットテーブルが 1 つのキャッシュを共有している場合、ピボットテーブルごとに `RefreshData()` を繰り返し呼び出すと、同じキャッシュが何度も再取得されることになり、非常に遅くなります。

推奨される置き換えは次のとおりです。

- **ワークブック内のすべてのピボットテーブルを更新する** → `workbook.RefreshAll();` を使用します。
- **一部のピボットテーブルを更新する** → 1 つのキャッシュに対して `pivotTable.PivotCache.Refresh();` を使用します。キャッシュは共有されているため、この 1 回の呼び出しでそのキャッシュ上に構築されたすべてのピボットテーブルが更新されます。既に更新されたキャッシュ上に存在する他のピボットテーブルは、安全にスキップできます。
- **ピボットビュー/レイアウトのみが変更された場合** → ソースへのラウンドトリップなしに既存のキャッシュから再レンダリングするために `pivotTable.CalculateData();` を使用します。

次の例では、単一のキャッシュを共有する複数のピボットテーブルを持つワークブックの新しい効率的なパターンを示しています。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// 新しいワークブックを作成し、最初のワークシートにアクセスします
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// --- ソースデータを構築: 果物 / 年 / 金額 (ヘッダー + 9行) ---
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");

sheet.Cells["A2"].PutValue("Grape");      sheet.Cells["B2"].PutValue(2020); sheet.Cells["C2"].PutValue(1000);
sheet.Cells["A3"].PutValue("Blueberry");  sheet.Cells["B3"].PutValue(2020); sheet.Cells["C3"].PutValue(2000);
sheet.Cells["A4"].PutValue("Kiwi");       sheet.Cells["B4"].PutValue(2020); sheet.Cells["C4"].PutValue(1500);
sheet.Cells["A5"].PutValue("Cherry");     sheet.Cells["B5"].PutValue(2020); sheet.Cells["C5"].PutValue(2500);
sheet.Cells["A6"].PutValue("Grape");      sheet.Cells["B6"].PutValue(2021); sheet.Cells["C6"].PutValue(3000);
sheet.Cells["A7"].PutValue("Blueberry");  sheet.Cells["B7"].PutValue(2021); sheet.Cells["C7"].PutValue(1800);
sheet.Cells["A8"].PutValue("Kiwi");       sheet.Cells["B8"].PutValue(2021); sheet.Cells["C8"].PutValue(2200);
sheet.Cells["A9"].PutValue("Cherry");     sheet.Cells["B9"].PutValue(2021); sheet.Cells["C9"].PutValue(2700);

// --- 最初のピボットテーブル (Pivot1) を宛先セル E3 に追加 ---
int idx1 = sheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = sheet.PivotTables[idx1];
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

// --- 同じソース範囲に2番目のピボットテーブル (Pivot2) を追加 ---
// Pivot1 と Pivot2 は両方とも1つの基礎となる PivotCache を共有します。
// これはまさに、従来のテーブルごとの RefreshData()
// アプローチが非効率になるシナリオです: 1つのテーブルをリフレッシュすると、
// 共有キャッシュ全体を再取得するため、N個のテーブルをリフレッシュすると
// 同じ高コストの取得がN回行われます。
int idx2 = sheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = sheet.PivotTables[idx2];
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

// --- ソースデータの複数の金額値を変更 ---
sheet.Cells["C2"].PutValue(5000);   // グレープ 2020
sheet.Cells["C5"].PutValue(7500);   // チェリー 2020
sheet.Cells["C9"].PutValue(9500);   // チェリー 2021

// --- 廃止されたパターン (26.7以前) — PivotTable.RefreshData() ---
// pivotTable1.RefreshData();  // ソースから再取得し、キャッシュ全体をリフレッシュ
// pivotTable2.RefreshData();  // 再度再取得 — キャッシュはすでに最新です!
// 各呼び出しで共有キャッシュが再構築されるため、N個のテーブル = N個の冗長な取得。

// --- 新しい v26.7+ パターン: キャッシュを1回リフレッシュし、必要に応じて再レンダリング ---
// PivotCache.Refresh() を1回呼び出すと、変更された値が共有キャッシュに取り込まれ、
// それを参照するすべてのピボットテーブルの表示が再計算されます。
// Pivot1 と Pivot2 は1つの PivotCache を共有しているため、この単一の呼び出しで
// 両方のテーブルが更新されます — 2回目のソースへのラウンドトリップは不要です。
pivotTable1.PivotCache.Refresh();

// CalculateData() はピボットテーブルの表示(データ + スタイル)のみを
// すでにキャッシュに保持されているデータから再レンダリングします — ソースには触れません。
// ここでは API のデモのみを目的として Pivot2 に対して呼び出します: キャッシュが
// 一度リフレッシュされた後は、依存するテーブルはソースに戻ることなく再レンダリングできます。
// ピボットテーブルの表示/レイアウト設定のみが変更され、キャッシュが最新である場合は、
// CalculateData() を単独で使用してください。
pivotTable2.CalculateData();

workbook.Save("output.xlsx");
```

## どの更新 API を使用すべきか？

次の表は、利用可能な更新 API と、それぞれをいつ選択すべきかをまとめたものです。

| 目的 | 推奨される API | メモ |
|------|-----------------|-------|
| ワークブック内のすべてを更新する | `Workbook.RefreshAll()` | 1 回の呼び出しで、すべてのキャッシュとテーブルをカバーします。 |
| 単一シート上のピボットテーブルだけを更新する | `Worksheet.RefreshPivotTables()` | 1 つのワークシートにスコープされます。 |
| 1 つのキャッシュのソースデータが変更された | `pivotTable.PivotCache.Refresh()` | その共有キャッシュ上のすべてのピボットテーブルを更新します。 |
| 表示/レイアウト設定のみが変更された | `pivotTable.CalculateData()` | 不要なソースへのラウンドトリップをスキップします。 |
| 共有キャッシュ上のすべてのピボットテーブルを一覧表示する | `pivotCache.GetPivotTables()` | 一括更新の前に列挙するために使用します。 |

実際には、廃止予定のテーブルごとの `RefreshData()` よりも、キャッシュベースの API を優先してください。これらは共有キャッシュを認識し、冗長なソースフェッチを回避し、更新要件を満たす最小限のスコープを選択できるようにします。

## 関連記事

- [セルに画像を挿入する](/cells/ja/net/inserting-an-image-into-a-cell/)
- [DBF ファイルの読み取りと書き込み](/cells/ja/net/dbf/)
- [Excel ファイルを複数のファイルに分割する](/cells/ja/net/splitting-excel-files-into-multiple-files/)
- [Aspose.Cells for .NET のスパークライン](/cells/ja/net/sparkline/)

{{< app/cells/assistant language="csharp" >}}