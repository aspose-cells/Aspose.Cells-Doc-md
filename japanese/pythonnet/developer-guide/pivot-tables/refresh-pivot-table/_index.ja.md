---
title: Aspose.Cells for Python via .NET でピボットテーブルを更新する
linktitle: Aspose.Cells for Python via .NET でピボットテーブルを更新する
description: Aspose.Cells for Python via .NET の v26.7+ ピボット更新 API を使用してピボットテーブルを更新する方法を学びます。この記事では RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData、GetPivotTables について実用的なコード例とともに説明します。
keywords: Aspose.Cells, Python via .NET, ピボットテーブル, 更新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ja/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は、ワークブック全体から単一のピボットテーブルまで、4つの異なるスコープでピボットデータを再読み込みできる階層型更新 API を提供します。**Aspose.Cells for Python via .NET v26.7** 以降、従来のメソッド `PivotTable.refresh_data()` は非推奨となり、この記事で説明するより効率的なキャッシュ対応 API に置き換える必要があります。

{{% /alert %}}

## はじめに

ピボットテーブルの更新は、単一の操作であることはほとんどありません。舞台裏では、Aspose.Cells は元のソースデータとワークシートに表示されるレンダリングされた値を結ぶ階層的なデータチェーンを維持しています。このチェーンを理解することが、あらゆる状況に対して適切な更新 API を選択する鍵となります。

四層データチェーンは以下の通りです：

1. **データソース** — 生の値が格納されている元のワークシート範囲、データベースクエリ、または統合範囲。
2. **PivotCache** — ソースデータのインメモリスナップショット。すべてのピボットテーブルは `PivotCache` の上に構築されます。すべてのデータが集約されるのはここです。
3. **PivotTable** — 行、列、値、フィルタフィールドを定義するビューオブジェクト。`PivotTable` はデータソースから直接ではなく、`PivotCache` からのみ読み取ります。
4. **Cells** — `PivotTable` が計算された値とスタイルをレンダリングする先のワークシートの `Cells`。

特に重要な概念は **共有キャッシュ** です。ワークブック内の複数のピボットテーブルが同じソース範囲を参照する場合、*1つの* `PivotCache` インスタンスを共有します。1つの `PivotCache` は多くのピボットテーブルから参照でき、そのキャッシュを更新すると、依存するすべての `PivotTable` が一度に更新されます。

{{% alert color="primary" %}}

`PivotCache.source_type`（列挙型 `PivotTableSourceType`）は、キャッシュデータの出所を示します。v26.7 時点で、`PivotCache.refresh()` は **`Sheet`** と **`Consolidation`** のソースタイプのみをサポートします。つまり、ワークシート範囲にあるデータのみです。外部ソース（データベース、外部接続など）は、キャッシュ API 経由ではまだ更新できません。

{{% /alert %}}

このチェーンのため、Aspose.Cells には2つの基本的な更新パスがあります：

- **`PivotCache.refresh()`** — 1回の操作でソース→キャッシュを再読み込みし、依存するすべての `PivotTable` を再計算します。
- **`PivotTable.calculate_data()`** — データソースへのラウンドトリップなしで、既にキャッシュされたデータから1つの `PivotTable` の表示を再計算します。

この記事のすべてのシナリオはワークシートセルのソースデータを使用するため、ソースタイプは `Sheet` であり、更新操作は記載通りに動作します。

## 必要なインポート

この記事のすべての Python の例は、ピボットタイプが `aspose.cells.pivot` 名前空間に存在するため、以下の3つのインポート文から始まります：

- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## ワークブック内のすべてのピボットテーブルを更新する

ワークブック内のすべてのピボットキャッシュとすべてのピボットテーブルが最新のソースデータを反映するようにする必要がある場合、最もシンプルで包括的な API は `Workbook.refresh_all()` です。1回の呼び出しでワークブック全体を走査し、各 `PivotCache` をソースから更新し、依存するすべての `PivotTable` を再計算します。これは、パフォーマンスが懸念されない一般的なドキュメント全体の更新に推奨されるアプローチです。

次の例では、Fruit/Year/Amount ソース範囲を含むワークブックを作成し、1つのピボットテーブルを作成し、一部のソース値を変更してから、`refresh_all()` を使用してすべてを1回の呼び出しで最新の状態にします。

```python
import aspose.cells as ac

# 新しいワークブックを作成
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# A1:C1 のセルにヘッダー行を書き込み
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# A2:C9 のセルにデータ行を書き込み（2020年と2021年にまたがる8行の果物データ）
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

# ピボットテーブルを追加：ソース範囲 "A1:C9"、配置先セル "E3"、名前 "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# ピボットフィールドを割り当て：Fruit を行、Year を列、Amount をデータ
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# 変更をシミュレートするために、ソースデータのいくつかの Amount 値を変更
worksheet.cells["C2"].put_value(55)
worksheet.cells["C5"].put_value(85)
worksheet.cells["C9"].put_value(125)

# ワークブック内のすべてのピボットテーブル/ピボットキャッシュを更新
workbook.refresh_all()

# ワークブックを保存
workbook.save("output.xlsx")
```

## 単一ワークシート上のすべてのピボットテーブルを更新する

時には、特定の1つのワークシート上にあるピボットテーブルのみを更新する必要がある場合があります。たとえば、他のワークシート上のピボットテーブルが関連していないことがわかっていて、触れずに残しておきたい場合です。この場合のために、Aspose.Cells は単一の `Worksheet` インスタンスを対象とする `Worksheet.refresh_pivot_tables()` を提供します。

これは `Workbook.refresh_all()` よりも選択的です。対象ワークシート上のピボットテーブルのみが更新され、他のワークシート上のピボットテーブルはそのまま残されます。

次の例では、同じ Fruit/Year/Amount ソースデータを設定し、最初のワークシートにピボットテーブルを追加し、一部のソース値を変更してから、そのワークシートのピボットテーブルのみを更新します。

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

## 単一のピボットテーブルを更新する

単一のピボットテーブルを細かく制御したい場合、キャッシュベースの API には2つのオプションがあります。どちらを選択するかは、実際に何が変わったかによって異なります。基になるソースデータか、ピボットテーブル自体のビュー/レイアウト設定のみかです。

### ソースデータが変更された場合 — `PivotCache.refresh()` を使用

基になるソースデータが変更された場合、正しいエントリーポイントは `pivot_table.pivot_cache.refresh()` です。この呼び出しはソースデータをキャッシュに再読み込みし、そのキャッシュに依存するすべての `PivotTable` を再計算します。

{{% alert color="primary" %}}

ピボットテーブルは1つの `PivotCache` インスタンスを共有するため、`PivotCache.refresh()` を呼び出すと、参照したテーブルだけでなく、同じキャッシュ上に構築された **すべての** ピボットテーブルが再計算されます。2つのピボットテーブルが同じソース範囲を共有している場合、1つのキャッシュを更新すると両方が更新されます。

{{% /alert %}}

次の例では、同じソース範囲上に2つのピボットテーブルを作成し、この共有キャッシュの動作を示し、一部のソース値を変更してから、1つのキャッシュ参照を介して更新します。

```python
import aspose.cells as ac

# 新しいワークブックを作成し、最初のワークシートにアクセスします
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# ヘッダー行を書き込みます: Fruit / Year / Amount
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# 約9行のデータ行を書き込みます (2020-2021にわたるgrape / blueberry / kiwi / cherry)
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
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

# セルE3に固定された最初のピボットテーブル "Pivot1" を追加し、ソース範囲はA1:C9
pivotIndex1 = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.pivot_tables[pivotIndex1]

# Pivot1のフィールドを割り当てます
pivotTable1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# 同じソース範囲A1:C9を使用して、セルE15に固定された2番目のピボットテーブル "Pivot2" を追加します
# ソース範囲が同一であるため、Pivot1とPivot2は単一のPivotCacheを共有します。
pivotIndex2 = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.pivot_tables[pivotIndex2]

# Pivot2に同じフィールドを割り当てます
pivotTable2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# データ変更をシミュレートするために、ソースデータのいくつかのAmountセルの値を変更します
worksheet.cells["C2"].put_value(150)
worksheet.cells["C4"].put_value(350)
worksheet.cells["C7"].put_value(650)

# 共有PivotCacheを更新します。
# Pivot1とPivot2は同じPivotCacheを共有しているため、この単一の呼び出しで
# 更新されたソースから両方のピボットテーブル (データ + スタイル) を更新します。
pivotTable1.pivot_cache.refresh()

# ワークブックを保存します
workbook.save("output.xlsx")
```

### ビュー/レイアウトのみが変更された場合 — `calculate_data()` を使用

ソースデータが変更されておらず、ピボットテーブルのビューまたはレイアウト設定のみが変更された場合（たとえば、フィールドが別のエリアに移動された、またはファイルを開くときに更新する設定が切り替えられたなど）、データソースへのラウンドトリップは必要ありません。キャッシュには正しいデータがすでに保持されており、レンダリングされた `PivotTable` を再計算するだけで済みます。この場合、`pivot_table.calculate_data()` が正しい選択です。

これにより、不要なソースフェッチが回避され、多くのピボットテーブルが同じキャッシュを共有している場合に大幅に高速化されます。

次の例では、ピボットテーブルのソース以外のプロパティを変更してから、`calculate_data()` を呼び出して既存のキャッシュから再レンダリングします。

```python
import aspose.cells as ac
import aspose.cells.pivot as acp

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Fruit / Year / Amount のヘッダー行を書き込み
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# 8 行のデータ行を書き込み (2-9 行目、ソース範囲 A1:C9 に適合)
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

# 目的セル E3 に配置される "Pivot1" という名前のピボットテーブルを追加し、A1:C9 をソースとする
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# フィールドを割り当て: Fruit を行、Year を列、Amount をデータ
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")

# 表示/レイアウトのプロパティを変更 — これは表示のみの変更であるため、
# PivotCache.Refresh() を通じてソースデータを再読み込みする必要はありません。
pivot_table.refresh_data_on_opening_file = False

# CalculateData() は PivotCache に既に保持されているデータから、このピボットテーブルの表示
# (データとスタイル) を再レンダリングします。ソースデータが変更されていないため、
# ソースへのラウンドトリップは実行されず、キャッシュされた値がワークシートのセルに
# 再計算されるだけです。
pivot_table.calculate_data()

# ワークブックをディスクに保存
workbook.save("output.xlsx")
```

## 同じ PivotCache を共有するすべてのピボットテーブルを取得する

ワークブックには、1つの共有キャッシュの上にすべてが乗っている多くのピボットテーブルが含まれていることがよくあります。これらを列挙するには（たとえば、一括更新を実行する前や、共有キャッシュの影響を診断するために）、`PivotCache.get_pivot_tables()` を使用します。このメソッドは、指定されたキャッシュに依存するすべての `PivotTable` のコレクションを返します。

これはまた、2つのピボットテーブルが実際に同じ `PivotCache` インスタンスを共有していることを確認する最も直接的な方法でもあります。キャッシュ参照を比較したり、`get_pivot_tables()` が返すコレクションを反復処理して、どのピボットテーブルが含まれているかを確認したりできます。

次の例では、同じソース範囲上に2つのピボットテーブルを作成し、それらが同じキャッシュインスタンスを共有していることを確認してから、キャッシュのピボットテーブルを列挙します。

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Sheet1"

worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

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
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(900)

pivot1_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = worksheet.pivot_tables[pivot1_index]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

pivot2_index = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = worksheet.pivot_tables[pivot2_index]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

same_cache = pivot_table1.pivot_cache is pivot_table2.pivot_cache
print("Pivot1 and Pivot2 share the same PivotCache: " + str(same_cache))

shared_pivot_tables = pivot_table1.pivot_cache.get_pivot_tables()
print("Number of pivot tables sharing the cache: " + str(len(shared_pivot_tables)))

for pt in shared_pivot_tables:
    print("Pivot table name: " + pt.name)

workbook.save("output.xlsx")
```

## 廃止された `PivotTable.refresh_data()` からの移行

Aspose.Cells for Python via .NET v26.7 より前では、ピボットテーブルを更新する標準的な方法は、各ピボットテーブルに対して個別に `PivotTable.refresh_data()` を呼び出すことでした。v26.7 では、このメソッドは **廃止** とマークされており、上記のキャッシュ対応 API に置き換える必要があります。

実世界のワークブックでは、テーブルごとの `refresh_data()` アプローチに問題がある理由は2つあります：

- ソースが変更されていない場合でも、呼び出されるたびにソースからデータを再取得します。
- 各呼び出しは共有キャッシュ全体を更新します。多くのピボットテーブルが1つのキャッシュを共有している場合、ピボットテーブルごとに `refresh_data()` を繰り返し呼び出すと、同じキャッシュが何度も再フェッチされるため、非常に遅くなります。

推奨される置き換えは次のとおりです：

- **ワークブック内のすべてのピボットテーブルを更新する** → `workbook.refresh_all();` を使用
- **一部のみを更新する** → 1つのキャッシュに対して `pivot_table.pivot_cache.refresh();` を使用します。キャッシュは共有されるため、この1回の呼び出しで、そのキャッシュ上に構築されたすべてのピボットテーブルが更新されます。すでに更新されたキャッシュ上に存在する他のピボットテーブルは、安全にスキップできます。
- **ピボットビュー/レイアウトのみが変更された場合** → ソースへのラウンドトリップなしで既存のキャッシュから再レンダリングするには、`pivot_table.calculate_data();` を使用します。

次の例では、単一のキャッシュを共有する複数のピボットテーブルを持つワークブックに対する新しい効率的なパターンを示します。

```python
import aspose.cells as ac

# 新しいワークブックを作成し、最初のワークシートにアクセスします
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# --- ソースデータを構築: 果物 / 年 / 金額 (ヘッダー + 9行) ---
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

sheet.cells["A2"].put_value("Grape")      ; sheet.cells["B2"].put_value(2020); sheet.cells["C2"].put_value(1000)
sheet.cells["A3"].put_value("Blueberry")  ; sheet.cells["B3"].put_value(2020); sheet.cells["C3"].put_value(2000)
sheet.cells["A4"].put_value("Kiwi")       ; sheet.cells["B4"].put_value(2020); sheet.cells["C4"].put_value(1500)
sheet.cells["A5"].put_value("Cherry")     ; sheet.cells["B5"].put_value(2020); sheet.cells["C5"].put_value(2500)
sheet.cells["A6"].put_value("Grape")      ; sheet.cells["B6"].put_value(2021); sheet.cells["C6"].put_value(3000)
sheet.cells["A7"].put_value("Blueberry")  ; sheet.cells["B7"].put_value(2021); sheet.cells["C7"].put_value(1800)
sheet.cells["A8"].put_value("Kiwi")       ; sheet.cells["B8"].put_value(2021); sheet.cells["C8"].put_value(2200)
sheet.cells["A9"].put_value("Cherry")     ; sheet.cells["B9"].put_value(2021); sheet.cells["C9"].put_value(2700)

# --- 宛先セルE3に最初のピボットテーブル(Pivot1)を追加 ---
idx1 = sheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = sheet.pivot_tables[idx1]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- 同じソース範囲に2番目のピボットテーブル(Pivot2)を追加 ---
# Pivot1とPivot2は両方とも1つの基礎となるPivotCacheを共有します。
# これはまさに、レガシーのテーブルごとのRefreshData()が
# 非効率になるシナリオです: 1つのテーブルを更新すると、共有キャッシュ全体を再取得し、
# したがって、N個のテーブルを更新すると、同じ高コストの取得をN回実行します。
idx2 = sheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = sheet.pivot_tables[idx2]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- ソースデータの複数の金額値を変更 ---
sheet.cells["C2"].put_value(5000)   # グレープ 2020
sheet.cells["C5"].put_value(7500)   # チェリー 2020
sheet.cells["C9"].put_value(9500)   # チェリー 2021

# --- 廃止されたパターン (v26.7以前) — PivotTable.RefreshData() ---
# pivot_table1.refresh_data();  # ソースから再取得し、キャッシュ全体を更新します
# pivot_table2.refresh_data();  # 再度再取得 — キャッシュはすでに最新です!
# 各呼び出しで共有キャッシュが再構築されるため、N個のテーブル = N回の冗長な取得が行われます。

# --- 新しいv26.7+パターン: キャッシュを1回更新し、必要に応じて再レンダリング ---
# PivotCache.Refresh()の1回の呼び出しで、変更された値が共有キャッシュに取り込まれ、
# それを参照するすべてのピボットテーブルの表示も再計算されます。
# Pivot1とPivot2は1つのPivotCacheを共有しているため、この1回の呼び出しで
# 両方のテーブルが更新されます — ソースへの2回目のラウンドトリップは不要です。
pivot_table1.pivot_cache.refresh()

# CalculateData()はピボットテーブルの表示(データ + スタイル)のみを再レンダリングします
# キャッシュに既にあるデータから — ソースには触れません。
# Pivot2でこれを呼び出すのは、APIを実演するためだけです: キャッシュが更新された後、
# 依存するテーブルはすべて、ソースに戻らずに再レンダリングできます。
# ピボットテーブルの表示/レイアウト設定のみが変更され、
# キャッシュが最新の場合は、CalculateData()を単独で使用してください。
pivot_table2.calculate_data()

workbook.save("output.xlsx")
```

## どの更新 API を使用すべきか?

以下の表は、利用可能な更新 API とそれぞれを選択するタイミングをまとめたものです。

| 目的 | 推奨 API | メモ |
|------|-----------------|-------|
| ワークブック内のすべてを更新する | `Workbook.refresh_all()` | 1回の呼び出しで、すべてのキャッシュとテーブルをカバーします。 |
| 単一ワークシート上のピボットテーブルのみを更新する | `Worksheet.refresh_pivot_tables()` | 1つのワークシートを対象とします。 |
| 1つのキャッシュのソースデータが変更された | `pivot_table.pivot_cache.refresh()` | その共有キャッシュ上のすべてのピボットテーブルを更新します。 |
| ビュー/レイアウト設定のみが変更された | `pivot_table.calculate_data()` | 不要なソースへのラウンドトリップをスキップします。 |
| 共有キャッシュ上のすべてのピボットテーブルを一覧表示する | `pivot_cache.get_pivot_tables()` | 一括更新の前に列挙するために使用します。 |

実際には、廃止されたテーブルごとの `refresh_data()` よりもキャッシュベースの API を優先してください。これらは共有キャッシュを認識し、不要なソースフェッチを回避し、更新要件を満たす最小スコープを選択できるようにします。

## 関連記事

- [Aspose.Cells for Python via .NET のスパークライン](/cells/ja/python-net/sparkline/)

{{< app/cells/assistant language="python" >}}