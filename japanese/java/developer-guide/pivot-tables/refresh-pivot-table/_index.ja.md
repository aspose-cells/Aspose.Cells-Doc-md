---
title: Aspose.Cells for Java でピボットテーブルとピボットキャッシュを更新する
linktitle: Aspose.Cells for Java でピボットテーブルとピボットキャッシュを更新する
description: v26.7+ のピボット更新 API を使用して Aspose.Cells for Java でピボットテーブルを更新する方法を学びます。本記事では RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData、GetPivotTables を実用的なコード例とともに解説します。
keywords: Aspose.Cells, Java, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ja/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ワークブック全体から単一のピボットテーブルまで、4 つの異なるスコープでピボットデータを再読み込みできる階層的な更新 API を提供します。**Aspose.Cells for Java v26.7** 以降、従来のメソッド `PivotTable.refreshData()` は非推奨となり、本記事で紹介するより効率的でキャッシュを認識する API に置き換える必要があります。
{{% /alert %}}

## はじめに
ピボットテーブルの更新は、単一の操作であることはほとんどありません。Aspose.Cells は内部で、元のソースデータとワークシートに表示されるレンダリング値を結ぶ階層的なデータチェーンを維持しています。このチェーンを理解することが、あらゆる状況で適切な更新 API を選択する鍵となります。
4 層のデータチェーンは次のとおりです。
1. **データソース** — 生の値が格納されている元のワークシート範囲、データベースクエリ、または統合範囲。
2. **PivotCache** — ソースデータのインメモリスナップショット。すべてのピボットテーブルは `PivotCache` の上に構築され、ここにすべてのデータが収集・集計されます。
3. **PivotTable** — 行、列、値、フィルタの各フィールドを定義するビューオブジェクト。`PivotTable` はデータソースから直接読み取ることはなく、*常に* `PivotCache` からのみ読み取ります。
4. **Cells** — `PivotTable` が計算結果とスタイルをレンダリングする先の、ワークシートの `Cells`。

{{% alert color="primary" %}}
`PivotCache.getSourceType()`（列挙型 `PivotTableSourceType`）は、キャッシュデータの取得元を示します。v26.7 時点で、`PivotCache.refresh()` は **`Sheet`** および **`Consolidation`** のソースタイプ、つまりワークシート範囲に存在するデータのみをサポートしています。外部ソース（データベース、外部接続など）は、まだキャッシュ API 経由では更新できません。
{{% /alert %}}

このチェーンのため、Aspose.Cells には次の 2 つの基本的な更新パスがあります。
- **`PivotTable.calculateData()`** — すでにキャッシュされたデータから、1 つの `PivotTable` の表示を再計算します。データソースへのラウンドトリップはありません。
本記事のすべてのシナリオではワークシートセルをソースデータとして使用しているため、ソースタイプは `Sheet` となり、更新操作は記載どおりに動作します。

## クイックスタート
ワークブック内のすべてのピボットを更新する最小限のコードが必要な場合は、次の 1 回の呼び出しだけで十分です。

```java
import com.aspose.cells.*;
// 新しいワークブックを作成
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// セル A1:C1 にヘッダー行を書き込む
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// セル A2:C9 にデータ行を書き込む（2020年と2021年にわたる8行の果物のデータ）
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
// ピボットテーブルを追加：ソース範囲 "A1:C9"、配置先のセル "E3"、名前 "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// ピボットフィールドを割り当て：Fruit を行に、Year を列に、Amount をデータに
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// 変更をシミュレートするためにソースデータのいくつかの Amount 値を変更
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// ワークブック内のすべてのピボットテーブル / ピボットキャッシュを更新
workbook.refreshAll();
// ワークブックを保存
workbook.save("output.xlsx");
```

本記事の以降のセクションでは、より狭いスコープの API を選ぶべき場面について説明します。

## 必要なインポート文
本記事のすべての Java サンプルは、ピボット型が `com.aspose.cells.pivot` パッケージに存在するため、次のインポート文から始まります。
- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## ワークブック内のすべてのピボットテーブルを更新する
ワークブック内のすべてのピボットキャッシュとすべてのピボットテーブルが最新のソースデータを反映するようにする必要がある場合、最もシンプルで包括的な API は `Workbook.refreshAll()` です。この呼び出し 1 回でワークブック全体を走査し、各 `PivotCache` をソースから更新し、それに依存するすべての `PivotTable` を再計算します。パフォーマンスを懸念しない一般的なフルドキュメントの更新には、この方法が推奨されます。
次の例では、Fruit/Year/Amount のソース範囲を持つワークブックを作成し、1 つのピボットテーブルを作成し、一部のソース値を変更し、`refreshAll()` を使用してすべてを 1 回の呼び出しで最新の状態にします。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
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
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## 単一のワークシート上のすべてのピボットテーブルを更新する
特定の 1 つのワークシート上にあるピボットテーブルだけを更新する必要がある場合があります（たとえば、他のワークシート上のピボットテーブルは無関係であり、触れないようにしたい場合など）。このようなケースのために、Aspose.Cells は単一の `Worksheet` インスタンスにスコープされた `Worksheet.refreshPivotTables()` を提供します。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Fruit / Year / Amount のヘッダー行を書き込みます
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// 8 行のデータ行を書き込みます (行 2-9、ソース範囲 A1:C9 に適合)
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
// "Pivot1" という名前のピボット テーブルを、配置先セル E3 に追加し、ソース範囲は A1:C9 です
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// フィールドを割り当てます: Fruit を行、Year を列、Amount をデータに
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// 表示/レイアウト プロパティを変更します -- これは表示のみの変更であり、
// したがって、PivotCache.Refresh() を通じてソース データを再読み込みする必要はありません。
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() は、PivotCache に保持されているデータから、このピボット テーブルの表示 (データ + スタイル) を再レンダリングします。
// ソース データが変更されていないため、ソースへのラウンド トリップは実行されません -- キャッシュされた値のみが再計算され、
// ワークシートのセルへ反映されます。
pivotTable.calculateData();
// ワークブックをディスクに保存します
workbook.save("output.xlsx");
```

## 単一のピボットテーブルを更新する
単一のピボットテーブルを細かく制御したい場合は、キャッシュベースの API で 2 つのオプションがあります。どちらを選ぶかは、実際に変更されたのが基になるソースデータなのか、それともピボットテーブル自身の表示/レイアウト設定のみなのかによって決まります。

### ソースデータが変更された場合 — `PivotCache.refresh()` を使用
基になるソースデータが変更された場合の正しいエントリポイントは、`pivotTable.getPivotCache().refresh()` です。この呼び出しはソースデータをキャッシュに再読み込みし、そのキャッシュに依存するすべての `PivotTable` を再計算します。

### 表示/レイアウトのみが変更された場合 — `calculateData()` を使用
ソースデータが変更されておらず、ピボットテーブルの表示やレイアウト設定のみが変更された場合（たとえば、フィールドを別のエリアに移動したり、開くたびに更新する設定を切り替えたりした場合）、データソースへのラウンドトリップは必要ありません。キャッシュにはすでに正しいデータが保持されており、再計算する必要があるのはレンダリング済みの `PivotTable` のみです。この場合、`pivotTable.calculateData()` が正しい選択です。
次の例では、ピボットテーブルのソース以外のプロパティを変更し、既存のキャッシュから再レンダリングするために `calculateData()` を呼び出します。
ワークブックには多くのピボットテーブルが含まれ、それらがすべて 1 つの共有キャッシュ上に存在することがよくあります。それらを列挙するには（たとえば、一括更新を行う前や、共有キャッシュの影響を診断するために）、`PivotCache.getPivotTables()` を使用します。このメソッドは、指定されたキャッシュに依存するすべての `PivotTable` のコレクションを返します。

## 非推奨の `PivotTable.refreshData()` からの移行
Aspose.Cells for Java v26.7 より前は、ピボットテーブルを更新する標準的な方法は、各ピボットテーブルに対して個別に `PivotTable.refreshData()` を呼び出すことでした。v26.7 時点で、このメソッドは **非推奨** とマークされており、上記のキャッシュ対応 API に置き換える必要があります。
実運用上のワークブックでテーブルごとの `refreshData()` アプローチに問題がある理由は 2 つあります。
- ソースが変更されていない場合でも、呼び出すたびにソースからデータを再取得します。
推奨される置き換えは次のとおりです。
次の例では、単一のキャッシュを共有する複数のピボットテーブルを持つワークブックに対する、新しい効率的なパターンを示します。

## どの更新 API を使用すべきか
次の表は、利用可能な更新 API とそれぞれを選択するタイミングをまとめたものです。
| 目的 | 推奨 API | 備考 |
|------|-----------------|-------|
| ワークブック内のすべてを更新する | `Workbook.refreshAll()` | 1 回の呼び出しで、すべてのキャッシュとテーブルを対象とします。 |
| 単一シート上のピボットテーブルだけを更新する | `Worksheet.refreshPivotTables()` | 1 つのワークシートにスコープされます。 |
| 1 つのキャッシュのソースデータが変更された | `pivotTable.getPivotCache().refresh()` | その共有キャッシュ上のすべてのピボットテーブルを更新します。 |
| 表示/レイアウト設定のみが変更された | `pivotTable.calculateData()` | 不要なソースへのラウンドトリップを回避します。 |
| 共有キャッシュ上のすべてのピボットテーブルを列挙する | `pivotCache.getPivotTables()` | 一括更新の前に列挙するために使用します。 |
実際のところ、非推奨のテーブルごとの `refreshData()` よりもキャッシュベースの API を優先してください。これらは共有キャッシュを認識しており、冗長なソース取得を回避し、更新要件を満たす最小のスコープを選択できるようにします。

## よくある落とし穴
- **保存前に更新し忘れる。** ピボットテーブルは、データチェーンが更新された場合にのみ、レンダリングされた値をワークシートに書き込みます。ソースセルを変更した場合は、`Workbook.save()` の前に `PivotCache.Refresh()`（または `Workbook.RefreshAll()`）を呼び出してください。さもないと、保存されたファイルには古い集計値がそのまま含まれます。
- **テーブルごとに非推奨の `RefreshData()` を呼び出す。** v26.7 では、`PivotTable.RefreshData()` は非推奨とマークされており、呼び出すたびにソースを再取得します。キャッシュを共有する複数のピボットテーブルがある場合、N 回の冗長なソース取得を意味します。テーブルごとに 1 回の `CalculateData()` の後に続く、単一の `PivotCache.Refresh()` に置き換えてください。
- **レイアウトのみが変更された場合に更新する。** ソースデータを変更せずにピボットテーブルの表示（列順、`ConsolidationFunction` など）のみを変更した場合、`PivotCache.Refresh()` は不要であり、遅くなります。既存のキャッシュから再レンダリングするには `pivotTable.CalculateData()` を呼び出してください。
- **`PivotCache.Refresh()` でサポートされない外部ソース。** ピボットテーブルのソースが外部接続（データベース、OLAP キューブなど）に由来する場合、v26.7 では `PivotCache.Refresh()` では更新できません。現在、`Sheet` および `Consolidation` のソースタイプのみをサポートしています。外部ソースの場合は、ワークブックを開き直すか、ソースからキャッシュを再構築してください。

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="java" >}}