---
title: Aspose.Cells for Python via .NET でのピボットテーブルの更新
linktitle: Aspose.Cells for Python via .NET でのピボットテーブルの更新
description: Aspose.Cells for Python via .NET で v26.7 以降のピボット更新 API を使用してピボットテーブルを更新する方法を学びます。この記事では RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData、GetPivotTables を実用的なコード例とともに解説します。
keywords: Aspose.Cells, Python via .NET, ピボットテーブル, 更新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ja/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ワークブック全体から単一のピボットテーブルまで、4 つの異なるスコープでピボットデータを再読み込みできる階層的な更新 API を提供します。**Aspose.Cells for Python via .NET v26.7** 以降、従来の `PivotTable.refresh_data()` メソッドは非推奨となり、この記事で説明するより効率的でキャッシュを認識する API に置き換える必要があります。
{{% /alert %}}
## はじめに
ピボットテーブルの更新は、単一の操作であることはほとんどありません。舞台裏では、Aspose.Cells は元のソースデータをワークシートに表示されるレンダリング済みの値に接続する階層的なデータチェーンを維持しています。このチェーンを理解することが、あらゆる状況で適切な更新 API を選択する鍵となります。
4 層のデータチェーンは次のとおりです。
1. **データソース** — 生データが格納されている元のワークシート範囲、データベースクエリ、または統合範囲。
2. **PivotCache** — ソースデータのメモリ内スナップショット。すべてのピボットテーブルは `PivotCache` の上に構築され、すべてのデータがここで収集・集計されます。
3. **PivotTable** — 行、列、値、フィルタのフィールドを定義するビューオブジェクト。`PivotTable` はデータソースから直接ではなく、`PivotCache` からのみデータを読み取ります。
4. **Cells** — `PivotTable` が計算済みの値とスタイルを描画する先のワークシートの `Cells`。
特に重要な概念は**共有キャッシュ**です。ワークブック内の複数のピボットテーブルが同じソース範囲を参照する場合、それらは*1 つの* `PivotCache` インスタンスを共有します。1 つの `PivotCache` を多くのピボットテーブルから参照でき、そのキャッシュを更新すると、依存するすべての `PivotTable` が一度に更新されます。
{{% alert color="primary" %}}
`PivotCache.source_type`（列挙型 `PivotTableSourceType`）は、キャッシュデータの取得元を示します。v26.7 時点で、`PivotCache.refresh()` は **`Sheet`** と **`Consolidation`** のソースタイプ、つまりワークシート範囲に存在するデータのみをサポートします。外部ソース（データベースや外部接続など）は、キャッシュ API 経由ではまだ更新できません。
{{% /alert %}}
このチェーンのため、Aspose.Cells には 2 つの基本的な更新パスがあります。
- **`PivotCache.refresh()`** — ソースからキャッシュへデータを再読み込みし、依存するすべての `PivotTable` を単一の操作で再計算します。
- **`PivotTable.calculate_data()`** — すでにキャッシュされているデータから 1 つの `PivotTable` の表示を再計算し、データソースへのラウンドトリップは行いません。
この記事のすべてのシナリオではワークシートセルをソースデータとして使用しているため、ソースタイプは `Sheet` であり、更新操作は前述どおりに動作します。
## 必要なインポート
この記事のすべての Python サンプルコードは、ピボット関連の型が `aspose.cells.pivot` 名前空間に存在するため、次の 3 つの import 文から始まります。
## ワークブック内のすべてのピボットテーブルを更新する
ワークブック内のすべてのピボットキャッシュとすべてのピボットテーブルが最新のソースデータを反映していることを確認する必要がある場合、最もシンプルで包括的な API は `Workbook.refresh_all()` です。1 回の呼び出しでワークブック全体を走査し、各 `PivotCache` をソースから更新し、次にそのキャッシュに依存するすべての `PivotTable` を再計算します。これは、パフォーマンスが懸念されない一般的な、ドキュメント全体の更新において推奨されるアプローチです。
次の例では、Fruit/Year/Amount のソース範囲を持つワークブックを作成し、1 つのピボットテーブルを作成し、一部のソース値を変更してから、`refresh_all()` を使用してすべてを 1 回の呼び出しで最新の状態にします。
```python
import aspose.cells as ac

# 新しいワークブックを作成
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# A1:C1 のセルにヘッダー行を書き込む
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# A2:C9 のセルにデータ行を書き込む（2020年と2021年にわたる8行のフルーツデータ）
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

# ピボットテーブルを追加：ソース範囲「A1:C9」、配置先セル「E3」、名前「Pivot1」
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# ピボットフィールドを割り当て：Fruit を行に、Year を列に、Amount をデータに
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# ソースデータの複数の Amount 値を変更して変更をシミュレート
worksheet.cells["C2"].put_value(55)
worksheet.cells["C5"].put_value(85)
worksheet.cells["C9"].put_value(125)

# ワークブック内のすべてのピボットテーブル / ピボットキャッシュを更新
workbook.refresh_all()

# ワークブックを保存
workbook.save("output.xlsx")
```
## 単一のワークシート上のすべてのピボットテーブルを更新する
特定の 1 つのワークシート上にあるピボットテーブルだけを更新する必要がある場合があります。たとえば、他のワークシート上にあるピボットテーブルは無関係であることがわかっており、触れたくない場合です。このような場合、Aspose.Cells は単一の `Worksheet` インスタンスを対象とする `Worksheet.refresh_pivot_tables()` を提供します。
これは `Workbook.refresh_all()` よりも選択的で、対象ワークシート上のピボットテーブルのみが更新され、他のワークシート上のピボットテーブルはそのまま残されます。
次の例では、同じ Fruit/Year/Amount のソースデータを設定し、最初のワークシートにピボットテーブルを追加し、一部のソース値を変更してから、そのワークシート上のピボットテーブルのみを更新します。
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
単一のピボットテーブルを細かく制御したい場合、キャッシュベースの API には 2 つの選択肢があります。どちらを選ぶかは、実際に何が変更されたか、つまり基礎となるソースデータなのか、それともピボットテーブル自体の表示やレイアウトの設定のみなのかによって決まります。
### ソースデータが変更された場合 — `PivotCache.refresh()` を使用する
基礎となるソースデータが変更された場合、正しいエントリポイントは `pivot_table.pivot_cache.refresh()` です。この呼び出しはソースデータをキャッシュに再読み込みし、そのキャッシュに依存するすべての `PivotTable` を再計算します。
{{% alert color="primary" %}}
ピボットテーブルは単一の `PivotCache` インスタンスを共有するため、`PivotCache.refresh()` を呼び出すと、そのキャッシュ上に構築された**すべての**ピボットテーブルが再計算されます（参照したピボットテーブルだけではありません）。2 つのピボットテーブルが同じソース範囲を共有している場合、1 つのキャッシュを更新すると両方が更新されます。
{{% /alert %}}
次の例では、同じソース範囲上に 2 つのピボットテーブルを作成し、この共有キャッシュの動作を示し、一部のソース値を変更してから、1 つのキャッシュ参照を通じて更新します。
```python
import aspose.cells as ac

# 新しいワークブックを作成し、最初のワークシートにアクセスします
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# ヘッダー行を書き込みます: Fruit / Year / Amount
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# 約9行のデータ行を書き込みます（2020-2021年にかけての grape / blueberry / kiwi / cherry）
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

# セルE3に固定された最初のピボットテーブル「Pivot1」を追加し、データ範囲はA1:C9
pivotIndex1 = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.pivot_tables[pivotIndex1]

# Pivot1にフィールドを割り当てます
pivotTable1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# 同じデータ範囲A1:C9を使用して、セルE15に固定された2番目のピボットテーブル「Pivot2」を追加します
# データ範囲が同一であるため、Pivot1とPivot2は単一のPivotCacheを共有します。
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

# 共有されているPivotCacheを更新します。
# Pivot1とPivot2は同じPivotCacheを共有しているため、この単一の呼び出しで
# 更新されたソースから両方のピボットテーブル（データ+スタイル）を更新します。
pivotTable1.pivot_cache.refresh()

# ワークブックを保存します
workbook.save("output.xlsx")
```
### 表示やレイアウトのみが変更された場合 — `calculate_data()` を使用する
ソースデータは変更されておらず、ピボットテーブルの表示やレイアウトの設定のみが変更された場合（たとえば、フィールドを別のエリアに移動した、または更新時にファイルを開く設定が切り替わったなど）、データソースにラウンドトリップする必要はありません。キャッシュには正しいデータがすでに保持されており、レンダリングされた `PivotTable` を再計算するだけで済みます。この場合、`pivot_table.calculate_data()` が正しい選択です。
これにより、不要なソース取得が回避され、多くのピボットテーブルが同じキャッシュを共有している場合に大幅に高速化されます。
次の例では、ピボットテーブルのソース以外のプロパティを変更し、その後 `calculate_data()` を呼び出して既存のキャッシュから再レンダリングします。
```python
import aspose.cells as ac
import aspose.cells.pivot as acp

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Fruit / Year / Amount のヘッダー行を書き込み
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# 8 行のデータ行を書き込み (2-9 行目、ソース範囲 A1:C9 に合わせる)
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

# 名前 "Pivot1" のピボットテーブルを追加し、出力先セル E3 に配置、ソースは A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# フィールドを割り当て: Fruit を行、Year を列、Amount をデータ
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")

# 表示/レイアウトのプロパティを変更 — これは表示のみの変更なので、
# PivotCache.Refresh() を使用してソースデータを再読み込みする必要はありません。
pivot_table.refresh_data_on_opening_file = False

# CalculateData() は、PivotCache に既に保持されているデータから、このピボットテーブルの
# 表示 (データ + スタイル) を再レンダリングします。ソースデータが変更されていないため、
# ソースへの往復処理は行われず、キャッシュされた値のみがワークシートのセルに再計算されます。
pivot_table.calculate_data()

# ワークブックをディスクに保存
workbook.save("output.xlsx")
```
## 同じ PivotCache を共有するすべてのピボットテーブルを取得する
ワークブックには、1 つの共有キャッシュ上に存在する多くのピボットテーブルが含まれていることがよくあります。これらを列挙するには（たとえば、一括更新を行う前や、共有キャッシュの影響を診断するために）、`PivotCache.get_pivot_tables()` を使用します。このメソッドは、指定されたキャッシュに依存するすべての `PivotTable` のコレクションを返します。
これは、2 つのピボットテーブルが実際に同じ `PivotCache` インスタンスを共有していることを確認する最も直接的な方法でもあります。キャッシュ参照を比較するか、`get_pivot_tables()` が返すコレクションを単純に反復処理し、どのピボットテーブルがそこに含まれているかを観察することができます。
次の例では、同じソース範囲上に 2 つのピボットテーブルを作成し、それらが同じキャッシュインスタンスを共有していることを確認し、キャッシュのピボットテーブルを列挙します。

## 非推奨の `PivotTable.refresh_data()` からの移行
Aspose.Cells for Python via .NET v26.7 より前では、ピボットテーブルを更新する標準的な方法は、各ピボットテーブルに対して個別に `PivotTable.refresh_data()` を呼び出すことでした。v26.7 以降、このメソッドは**非推奨**となり、上記で説明したキャッシュを認識する API に置き換える必要があります。
実際のワークブックでテーブルごとの `refresh_data()` アプローチに問題がある理由は 2 つあります。
- ソースが変更されていない場合でも、呼び出すたびにソースからデータを再取得します。
- 各呼び出しは共有キャッシュ全体を更新します。多くのピボットテーブルが 1 つのキャッシュを共有している場合、ピボットテーブルごとに `refresh_data()` を繰り返し呼び出すと、同じキャッシュが何度も再取得されることになり、非常に低速になります。
推奨される代替手段は次のとおりです。
- **ワークブック内のすべてのピボットテーブルを更新する** → `workbook.refresh_all();` を使用します。
- **一部だけを更新する** → 1 つのキャッシュに対して `pivot_table.pivot_cache.refresh();` を使用します。キャッシュは共有されているため、この 1 回の呼び出しで、そのキャッシュ上に構築されたすべてのピボットテーブルが更新されます。すでに更新済みのキャッシュ上に存在する他のピボットテーブルは、安全にスキップできます。
- **ピボットテーブルの表示やレイアウトのみが変更された** → ソースへのラウンドトリップなしで既存のキャッシュから再レンダリングするために `pivot_table.calculate_data();` を使用します。
次の例では、単一のキャッシュを共有する複数のピボットテーブルを持つワークブックの、新しい効率的なパターンを示します。
```python
import aspose.cells as ac

# 新しいワークブックを作成し、最初のワークシートにアクセスします
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# --- ソースデータの作成: Fruit / Year / Amount (ヘッダー + 9行) ---
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
# Pivot1とPivot2は1つの基礎となるPivotCacheを共有します。
# これはまさに、レガシーのテーブルごとのRefreshData()が
# 非効率になるシナリオです:1つのテーブルを更新すると、共有キャッシュ全体を
# 再フェッチするため、N個のテーブルを更新すると同じ高コストのフェッチをN回実行します。
idx2 = sheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = sheet.pivot_tables[idx2]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- ソースデータの複数のAmount値を変更 ---
sheet.cells["C2"].put_value(5000)   # Grape  2020
sheet.cells["C5"].put_value(7500)   # Cherry 2020
sheet.cells["C9"].put_value(9500)   # Cherry 2021

# --- 旧式パターン (26.7以前) — PivotTable.RefreshData() ---
# pivot_table1.refresh_data();  # ソースから再フェッチし、キャッシュ全体を更新
# pivot_table2.refresh_data();  # 再度再フェッチ — キャッシュは既に最新です!
# 各呼び出しで共有キャッシュが再構築されるため、N個のテーブル = N回の冗長なフェッチ。

# --- 新規v26.7+パターン: キャッシュを1回更新し、必要に応じて再レンダリング ---
# PivotCache.Refresh()を1回呼び出すと、変更された値が共有キャッシュに取り込まれ、
# それを参照するすべてのピボットテーブルの表示も再計算されます。
# Pivot1とPivot2は1つのPivotCacheを共有しているため、この単一の呼び出しで
# 両方のテーブルが更新されます — ソースへの2回目のラウンドトリップは不要です。
pivot_table1.pivot_cache.refresh()

# CalculateData()はピボットテーブルの表示(データ+スタイル)のみを再レンダリングします
# キャッシュに既にあるデータから — ソースには触れません。
# ここではPivot2に対してAPIを実証するためだけに呼び出します:キャッシュが
# 1回更新された後、依存するテーブルはソースに戻らずに再レンダリングできます。
# ピボットテーブルの表示/レイアウト設定のみが変更され、
# キャッシュが最新である場合に、CalculateData()を単独で使用します。
pivot_table2.calculate_data()

workbook.save("output.xlsx")
```
## どの更新 API を使用すべきか？
次の表は、利用可能な更新 API と、それぞれの選択時期をまとめたものです。
| 目的 | 推奨される API | メモ |
|------|-----------------|-------|
| ワークブック内のすべてを更新する | `Workbook.refresh_all()` | 1 回の呼び出しで、すべてのキャッシュとテーブルを対象とします。 |
| 単一シート上のピボットテーブルだけを更新する | `Worksheet.refresh_pivot_tables()` | 1 つのワークシートを対象とします。 |
| 1 つのキャッシュのソースデータが変更された | `pivot_table.pivot_cache.refresh()` | その共有キャッシュ上のすべてのピボットテーブルを更新します。 |
| 表示やレイアウトの設定のみが変更された | `pivot_table.calculate_data()` | 不要なソースへのラウンドトリップを回避します。 |
| 共有キャッシュ上のすべてのピボットテーブルを一覧表示する | `pivot_cache.get_pivot_tables()` | 一括更新の前に列挙するために使用します。 |
実際には、非推奨のテーブルごとの `refresh_data()` よりもキャッシュベースの API を優先してください。これらは共有キャッシュを認識し、冗長なソース取得を回避し、更新要件を満たす最小のスコープを選択できるようにします。

{{< app/cells/assistant language="python-net" >}}
