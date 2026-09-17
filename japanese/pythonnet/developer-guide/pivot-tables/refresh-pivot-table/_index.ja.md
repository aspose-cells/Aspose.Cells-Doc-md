---
title: Aspose.Cells for Python via .NET でピボットテーブルとピボットキャッシュを更新する
linktitle: Aspose.Cells for Python via .NET でピボットテーブルとピボットキャッシュを更新する
description: v26.7+ のピボット更新 API を使用して Aspose.Cells for Python via .NET でピボットテーブルを更新する方法を学びます。この記事では RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData、GetPivotTables を実用的なコード例とともに解説します。
keywords: Aspose.Cells, Python via .NET, ピボットテーブル, 更新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ja/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ワークブック全体から単一のピボットテーブルまで、4 つの異なるスコープでピボットデータを再読み込みできる階層型の更新 API を提供します。**Aspose.Cells for Python via .NET v26.7** 以降、従来のメソッド `PivotTable.refresh_data()` は廃止予定となり、この記事で説明するより効率的でキャッシュ対応の API に置き換える必要があります。
{{% /alert %}}

## はじめに
ピボットテーブルの更新は、単一の操作であることはほとんどありません。舞台裏では、Aspose.Cells は元のソースデータからワークシートに表示されるレンダリング値までを接続する階層化されたデータチェーンを維持しています。このチェーンを理解することが、あらゆる状況で適切な更新 API を選択する鍵となります。
4 層のデータチェーンは以下のとおりです。
1. **データソース** — 元のワークシート範囲、データベースクエリ、または統合範囲。生データがここに存在します。
2. **PivotCache** — ソースデータのインメモリスナップショット。すべてのピボットテーブルは `PivotCache` の上に構築されます。すべてのデータはこの場所で収集・集計されます。
3. **PivotTable** — 行、列、値、フィルタのフィールドを定義するビューオブジェクト。`PivotTable` はデータソースから直接ではなく、`PivotCache` からのみ読み取ります。
4. **セル** — `PivotTable` が計算結果とスタイルを描画するワークシートの `Cells` です。

{{% alert color="primary" %}}
`PivotCache.source_type`（列挙型 `PivotTableSourceType`）は、キャッシュデータの取得元を示します。v26.7 時点で、`PivotCache.refresh()` がサポートするのは **`Sheet`** と **`Consolidation`** のソースタイプのみです。つまり、ワークシート範囲にあるデータのみです。外部ソース（データベース、外部接続など）は、キャッシュ API を通じてはまだ更新できません。
{{% /alert %}}

このチェーンのため、Aspose.Cells には 2 つの基本的な更新パスがあります。
- **`PivotTable.calculate_data()`** — すでにキャッシュされたデータから 1 つの `PivotTable` の表示を再計算し、データソースへのラウンドトリップは行いません。
この記事のすべてのシナリオではワークシートセルをソースデータとして使用しているため、ソースタイプは `Sheet` であり、更新操作は説明したとおりに動作します。

## クイックスタート
ワークブック内のすべてのピボットを更新する最短のコードだけが必要な場合は、1 回の呼び出しで十分です。

```python
import aspose.cells as ac
# 新しいワークブックを作成
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# セルA1:C1にヘッダー行を書き込む
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
# セルA2:C9にデータ行を書き込む（2020年と2021年にわたる8行の果物データ）
worksheet.cells["A2"].put_value("grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(50)
worksheet.cells["A3"].put_value("blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(60)
worksheet.cells["A4"].put_value("kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(70)
worksheet.cells["A5"].put_value("cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(80)
worksheet.cells["A6"].put_value("grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(90)
worksheet.cells["A7"].put_value("blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(100)
worksheet.cells["A8"].put_value("kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(110)
worksheet.cells["A9"].put_value("cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(120)
# ピボットテーブルを追加: ソース範囲 "A1:C9"、配置先セル "E3"、名前 "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# ピボットフィールドを割り当て: 行にFruit、列にYear、データにAmount
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
# ソースデータのAmount値をいくつか変更して変更をシミュレート
worksheet.cells["C2"].put_value(55)
worksheet.cells["C5"].put_value(85)
worksheet.cells["C9"].put_value(125)
# ワークブック内のすべてのピボットテーブル / ピボットキャッシュを更新
workbook.refresh_all()
# ワークブックを保存
workbook.save("output.xlsx")
```

この記事の以降のセクションでは、より限定的な API をいつ選択すべきかを説明します。

## 必要なインポート
この記事のすべての Python サンプルは、ピボットタイプが `aspose.cells.pivot` 名前空間に存在するため、次の 3 つのインポート文から始まります。
- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## ワークブック内のすべてのピボットテーブルを更新する
ワークブック内のすべてのピボットキャッシュとすべてのピボットテーブルが最新のソースデータを反映するようにする必要がある場合、最もシンプルで包括的な API は `Workbook.refresh_all()` です。1 回の呼び出しでワークブック全体を走査し、各 `PivotCache` をソースから更新してから、それに依存するすべての `PivotTable` を再計算します。パフォーマンスが気にならない一般的なフルドキュメント更新には、このアプローチを推奨します。
次の例では、Fruit/Year/Amount のソース範囲を持つワークブックを作成し、1 つのピボットテーブルを作成して一部のソース値を変更し、`refresh_all()` を使用して 1 回の呼び出しですべてを最新の状態にします。

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
worksheet.cells["A2"].put_value("grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)
worksheet.cells["A3"].put_value("blueberry")
worksheet.cells["B3"].put_value(2021)
worksheet.cells["C3"].put_value(150)
worksheet.cells["A4"].put_value("kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(200)
worksheet.cells["A5"].put_value("cherry")
worksheet.cells["B5"].put_value(2021)
worksheet.cells["C5"].put_value(120)
worksheet.cells["A6"].put_value("grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(180)
worksheet.cells["A7"].put_value("blueberry")
worksheet.cells["B7"].put_value(2020)
worksheet.cells["C7"].put_value(130)
worksheet.cells["A8"].put_value("kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(220)
worksheet.cells["A9"].put_value("cherry")
worksheet.cells["B9"].put_value(2020)
worksheet.cells["C9"].put_value(140)
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
worksheet.cells["C2"].put_value(300)
worksheet.cells["C5"].put_value(250)
worksheet.cells["C9"].put_value(400)
worksheet.refresh_pivot_tables()
workbook.save("output.xlsx")
```

## 単一のワークシート上のすべてのピボットテーブルを更新する
特定のワークシート上にあるピボットテーブルだけを更新する必要がある場合があります。たとえば、他のワークシート上のピボットテーブルは無関係であることがわかっていて、触れたくない場合です。このような場合、Aspose.Cells は `Worksheet.refresh_pivot_tables()` を提供しており、これは単一の `Worksheet` インスタンスにスコープされます。

```python
import aspose.cells as ac
import aspose.cells.pivot as acp
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Fruit / Year / Amount のヘッダー行を書き込む
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
# 8 つのデータ行（2～9 行目、ソース範囲 A1:C9 に収まる）を書き込む
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)
worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)
worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)
worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)
worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(150)
worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(250)
worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(350)
worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(450)
# 「Pivot1」という名前のピボットテーブルを追加し、配置先はセル E3、ソースは A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# フィールドを割り当てる：Fruit を行、Year を列、Amount をデータへ
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")
# 表示/レイアウトプロパティを変更する — これは表示のみの変更であり、
# PivotCache.Refresh() を通じてソースデータを再読み込みする必要はない。
pivot_table.refresh_data_on_opening_file = False
# CalculateData() は、PivotCache に保持されている
# データから、このピボットテーブルの表示（データ + スタイル）を再レンダリングする。
# ソースデータが変更されていないため、ソースへのラウンドトリップは行われず、
# キャッシュされた値のみがワークシートセルに再計算される。
pivot_table.calculate_data()
# ワークブックをディスクに保存する
workbook.save("output.xlsx")
```

## 単一のピボットテーブルを更新する
単一のピボットテーブルに対してきめ細かい制御が必要な場合、キャッシュベース API には 2 つのオプションがあります。どちらを選択するかは、実際に変更された内容、つまり基になるソースデータなのか、ピボットテーブル自体のビュー/レイアウト設定のみなのかによって異なります。

### ソースデータが変更された場合 — `PivotCache.refresh()` を使用
基になるソースデータが変更された場合の正しいエントリポイントは `pivot_table.pivot_cache.refresh()` です。この呼び出しはソースデータをキャッシュに再読み込みし、そのキャッシュに依存するすべての `PivotTable` を再計算します。

### ビュー/レイアウトのみが変更された場合 — `calculate_data()` を使用
ソースデータは変更されておらず、ピボットテーブルのビューまたはレイアウト設定のみが変更された場合（たとえば、フィールドが別のエリアに移動された場合や、開くときに更新する設定が切り替えられた場合）、データソースへのラウンドトリップは必要ありません。キャッシュにはすでに正しいデータが保持されており、レンダリングされた `PivotTable` の再計算のみが必要です。この場合、`pivot_table.calculate_data()` が適切な選択です。
次の例では、ピボットテーブルのソース以外のプロパティを変更し、`calculate_data()` を呼び出して既存のキャッシュから再レンダリングします。
ワークブックには、多くの場合、1 つの共有キャッシュ上に存在する多数のピボットテーブルが含まれています。これらを列挙する場合（たとえば、バッチ更新を実行する前や、共有キャッシュの影響を診断するため）には、`PivotCache.get_pivot_tables()` を使用します。このメソッドは、指定されたキャッシュに依存するすべての `PivotTable` のコレクションを返します。

## 廃止予定の `PivotTable.refresh_data()` からの移行
Aspose.Cells for Python via .NET v26.7 より前は、ピボットテーブルを更新する標準的な方法は、各ピボットテーブルに対して個別に `PivotTable.refresh_data()` を呼び出すことでした。v26.7 以降、このメソッドは **廃止予定** とマークされており、上記で説明したキャッシュ対応の API に置き換える必要があります。
実世界のワークブックでは、テーブルごとの `refresh_data()` アプローチに問題がある理由が 2 つあります。
- ソースが変更されていない場合でも、呼び出されるたびにソースからデータを再取得します。
推奨される置き換えは次のとおりです。
次の例では、単一のキャッシュを共有する複数のピボットテーブルを含むワークブックの、新しい効率的なパターンを示します。

## どの更新 API を使用すべきか
次の表は、利用可能な更新 API とそれぞれをいつ選択すべきかをまとめたものです。
| 目標 | 推奨 API | メモ |
|------|-----------------|-------|
| ワークブック内のすべてを更新する | `Workbook.refresh_all()` | 1 回の呼び出しで、すべてのキャッシュとテーブルをカバーします。 |
| 単一シート上のピボットテーブルだけを更新する | `Worksheet.refresh_pivot_tables()` | 1 つのワークシートにスコープされます。 |
| 1 つのキャッシュのソースデータが変更された | `pivot_table.pivot_cache.refresh()` | 共有キャッシュ上のすべてのピボットテーブルを更新します。 |
| ビュー/レイアウト設定のみが変更された | `pivot_table.calculate_data()` | 不要なソースへのラウンドトリップを回避します。 |
| 共有キャッシュ上のすべてのピボットテーブルを一覧表示する | `pivot_cache.get_pivot_tables()` | 一括更新の前に列挙するために使用します。 |
実際には、廃止予定のテーブルごとの `refresh_data()` よりもキャッシュベースの API を優先してください。これらは共有キャッシュを認識し、不要なソースフェッチを回避し、更新要件を満たす最小限のスコープを選択できるようにします。

## よくある落とし穴
- **保存前に更新するのを忘れる。** ピボットテーブルは、データチェーンが更新されたときにのみ、レンダリングされた値をワークシートに書き込みます。ソースセルを変更した場合は、`Workbook.save()` の前に `PivotCache.Refresh()`（または `Workbook.RefreshAll()`）を呼び出してください。そうしないと、保存されたファイルには古い集計値がそのまま含まれます。
- **廃止予定の `RefreshData()` をテーブルごとに呼び出す。** v26.7 では、`PivotTable.RefreshData()` は廃止予定とマークされており、呼び出しごとにソースを再取得します。キャッシュを共有する複数のピボットテーブルがある場合、これは N 回の冗長なソースフェッチを意味します。テーブルごとに `CalculateData()` を続けた 1 回の `PivotCache.Refresh()` に置き換えてください。
- **レイアウトのみが変更されたときに更新する。** ソースデータに触れずにピボットテーブルのビュー（列順、`ConsolidationFunction` など）のみを変更した場合、`PivotCache.Refresh()` は不要で低速です。`pivotTable.CalculateData()` を呼び出して、既存のキャッシュから再レンダリングしてください。
- **`PivotCache.Refresh()` で外部ソースがサポートされない。** ピボットテーブルのソースが外部接続（データベース、OLAP キューブなど）からのものである場合、v26.7 では `PivotCache.Refresh()` で更新できません。現在、`Sheet` と `Consolidation` のソースタイプのみをサポートしています。外部ソースの場合は、ワークブックを再度開くか、ソースからキャッシュを再構築してください。

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="python-net" >}}