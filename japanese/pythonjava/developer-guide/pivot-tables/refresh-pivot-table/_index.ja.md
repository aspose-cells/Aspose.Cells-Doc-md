---
title: Aspose.Cells for Python via Java でのピボットテーブルの更新
linktitle: Aspose.Cells for Python via Java でのピボットテーブルの更新
description: Aspose.Cells for Python via Java で v26.7+ のピボット更新 API を使用してピボットテーブルを更新する方法を学びます。この記事では、RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData、GetPivotTables を実際のコード例とともに説明します。
keywords: Aspose.Cells, Python via Java, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ja/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells はレイヤード更新 API を提供しており、ワークブック全体から単一のピボットテーブルまで、4 つの異なるスコープでピボットデータを再読み込みできます。**Aspose.Cells for Aspose.Cells for Python via Java v26.7** 以降、従来のメソッド `PivotTable.refreshData()` は廃止予定となり、この記事で説明するより効率的でキャッシュ対応の API に置き換える必要があります。

{{% /alert %}}

## はじめに

ピボットテーブルの更新は、単一の操作であることはほとんどありません。背後では、Aspose.Cells は元のソースデータとワークシートに表示されるレンダリングされた値を接続するレイヤードデータチェーンを維持しています。このチェーンを理解することが、あらゆる状況に適した更新 API を選択する鍵となります。

4 層データチェーンは以下のとおりです。

1. **データソース** — 生の値が存在する元のワークシート範囲、データベースクエリ、または統合範囲。
2. **PivotCache** — ソースデータのインメモリスナップショット。すべてのピボットテーブルは `PivotCache` の上に構築されます。ここですべてのデータが集約および集計されます。
3. **PivotTable** — 行、列、値、フィルタフィールドを定義するビューオブジェクト。`PivotTable` はデータソースから直接ではなく、`PivotCache` からのみ読み取ります。
4. **Cells** — `PivotTable` が計算された値と書式をレンダリングするワークシートの `Cells`。

特に重要な概念は **共有キャッシュ** です。ワークブック内の複数のピボットテーブルが同じソース範囲を参照している場合、それらは *1 つの* `PivotCache` インスタンスを共有します。1 つの `PivotCache` を複数のピボットテーブルから参照でき、そのキャッシュを更新すると、依存するすべての `PivotTable` が一度に更新されます。

{{% alert color="primary" %}}

`PivotCache.getSourceType()` (列挙型 `PivotTableSourceType`) は、キャッシュデータの取得元を示します。v26.7 の時点で、`PivotCache.refresh()` は **`SHEET`** および **`CONSOLIDATION`** ソースタイプ、つまりワークシート範囲にあるデータのみをサポートします。外部ソース (データベース、外部接続など) は、キャッシュ API からはまだ更新できません。

{{% /alert %}}

このチェーンのため、Aspose.Cells には 2 つの基本的な更新パスがあります。

- **`PivotCache.refresh()`** — 単一の操作でソース → キャッシュを再読み込みし、依存するすべての `PivotTable` を再計算します。
- **`PivotTable.calculateData()`** — すでにキャッシュされているデータから 1 つの `PivotTable` の表示を再計算します。データソースへのラウンドトリップはありません。

この記事のすべてのシナリオではワークシートセルソースデータを使用しているため、ソースタイプは `SHEET` であり、更新操作は説明したとおりに動作します。

## 必要なインポート

この記事のすべての Python の例は、ピボットタイプが `aspose.cells.pivot` 名前空間にあるため、以下のインポートに依存しています。

- `import jpype`
- `import aspose.cells as cells`

`jpype` モジュールは JVM をブートストラップするために使用され、`aspose.cells` は全体を通して使用されるワークブック/ワークシート/セル/ピボットのタイプを公開します。

## ワークブック内のすべてのピボットテーブルを更新する

ワークブック内のすべてのピボットキャッシュとすべてのピボットテーブルが最新のソースデータを反映するようにする必要がある場合、最もシンプルで包括的な API は `Workbook.refreshAll()` です。1 回の呼び出しでワークブック全体を走査し、各 `PivotCache` をソースから更新し、依存するすべての `PivotTable` を再計算します。これは、パフォーマンスが懸念されない一般的なドキュメント全体の更新に推奨されるアプローチです。

次の例では、Fruit/Year/Amount ソース範囲を持つワークブックを作成し、1 つのピボットテーブルを作成し、一部のソース値を変更し、`refreshAll()` を使用してすべてを 1 回の呼び出しで最新の状態にします。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# 新しいワークブックを作成
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# ヘッダー行をセルA1:C1に書き込む
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# データ行をセルA2:C9に書き込む（2020年と2021年にわたる8行のフルーツデータ）
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(50)

worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(60)

worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(70)

worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(80)

worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(90)

worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(100)

worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(110)

worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(120)

# ピボットテーブルを追加：ソース範囲 "A1:C9"、配置セル "E3"、名前 "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# ピボットフィールドを割り当て：Fruitを行、Yearを列、Amountをデータ
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# 変更をシミュレートするため、ソースデータの複数のAmount値を変更
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)

# ワークブック内のすべてのピボットテーブル/ピボットキャッシュを更新
workbook.refreshAll()

# ワークブックを保存
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## 単一のワークシート上のすべてのピボットテーブルを更新する

特定の 1 つのワークシート上にあるピボットテーブルのみを更新する必要がある場合があります。たとえば、他のワークシートのピボットテーブルは無関係であり、触れたくないことが分かっている場合です。この場合、Aspose.Cells は `Worksheet.refreshPivotTables()` を提供します。これは単一の `Worksheet` インスタンスにスコープされます。

これは `Workbook.refreshAll()` よりも選択的です。対象ワークシート上のピボットテーブルのみが更新され、他のワークシート上のピボットテーブルはそのまま残されます。

次の例では、同じ Fruit/Year/Amount ソースデータを入力し、最初のワークシートにピボットテーブルを追加し、一部のソース値を変更し、そのワークシート上のピボットテーブルのみを更新します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2021)
worksheet.getCells().get("C3").putValue(150)

worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)

worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2021)
worksheet.getCells().get("C5").putValue(120)

worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(180)

worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2020)
worksheet.getCells().get("C7").putValue(130)

worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(220)

worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2020)
worksheet.getCells().get("C9").putValue(140)

pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

worksheet.getCells().get("C2").putValue(300)
worksheet.getCells().get("C5").putValue(250)
worksheet.getCells().get("C9").putValue(400)

worksheet.refreshPivotTables()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## 単一のピボットテーブルを更新する

単一のピボットテーブルを細かく制御したい場合、キャッシュベースの API には 2 つのオプションがあります。どちらを選択するかは、実際に何が変わったか、つまり基になるソースデータか、ピボットテーブル自体のビュー/レイアウト設定かによって異なります。

### ソースデータが変更された — `PivotCache.refresh()` を使用する

基になるソースデータが変更された場合、正しいエントリポイントは `pivotTable.getPivotCache().refresh()` です。この呼び出しはソースデータをキャッシュに再読み込みし、そのキャッシュに依存するすべての `PivotTable` を再計算します。

{{% alert color="primary" %}}

ピボットテーブルは単一の `PivotCache` インスタンスを共有するため、`PivotCache.refresh()` を呼び出すと、参照している 1 つのテーブルだけでなく、その同じキャッシュ上に構築された **すべての** ピボットテーブルが再計算されます。2 つのピボットテーブルが同じソース範囲を共有している場合、1 つのキャッシュを更新すると両方が更新されます。

{{% /alert %}}

次の例では、この共有キャッシュ動作を示すために同じソース範囲に 2 つのピボットテーブルを作成し、一部のソース値を変更し、1 つのキャッシュ参照を通じて更新します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# 新しいワークブックを作成し、最初のワークシートにアクセスします
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# ヘッダー行を書き込みます: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# 約9行のデータ行を書き込みます (2020-2021にわたる grape / blueberry / kiwi / cherry)
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

# セル E3 にアンカーされた最初のピボットテーブル "Pivot1" を追加します。ソース範囲は A1:C9
pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivotIndex1)

# Pivot1 のフィールドを割り当てます
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# 同じソース範囲 A1:C9 を使用して、E15 にアンカーされた 2 番目のピボットテーブル "Pivot2" を追加します
# Pivot1 と Pivot2 はソース範囲が同じため、単一の PivotCache を共有します。
pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivotIndex2)

# Pivot2 に同じフィールドを割り当てます
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# ソースデータのいくつかの Amount セルの値を変更してデータ変更をシミュレートします
worksheet.getCells().get("C2").putValue(150)
worksheet.getCells().get("C4").putValue(350)
worksheet.getCells().get("C7").putValue(650)

# 共有 PivotCache を更新します。
# Pivot1 と Pivot2 は同じ PivotCache を共有しているため、この 1 回の呼び出しで
# 更新されたソースから両方のピボットテーブル (データ + スタイル) を更新します。
pivotTable1.getPivotCache().refresh()

# ワークブックを保存します
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### ビュー/レイアウトのみが変更された — `calculateData()` を使用する

ソースデータが変更されておらず、ピボットテーブルのビューまたはレイアウト設定のみが変更された場合 (たとえば、フィールドが別のエリアに移動された場合や、開くときに更新する設定が切り替えられた場合)、データソースへのラウンドトリップは必要ありません。キャッシュにはすでに正しいデータが保持されています。再計算する必要があるのはレンダリングされた `PivotTable` だけです。この場合、`pivotTable.calculateData()` が正しい選択です。

これにより、不要なソースフェッチが回避され、多くのピボットテーブルが同じキャッシュを共有している場合、著しく高速になります。

次の例では、ピボットテーブルのソース以外のプロパティを変更し、`calculateData()` を呼び出して既存のキャッシュから再レンダリングします。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Fruit / Year / Amount のヘッダー行を書き込む
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# 8行のデータ行を書き込む (2-9行、ソース範囲 A1:C9 に適合)
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(150)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(250)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(350)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(450)

# "Pivot1" という名前のピボットテーブルを追加し、配置先はセル E3、ソースは A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# フィールドを割り当て: Fruit を行へ、Year を列へ、Amount をデータへ
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# 表示/レイアウトプロパティの変更 — これは表示のみの変更であり、
# PivotCache.Refresh() を介してソースデータを再読み込みする必要はありません。
pivotTable.setRefreshDataOnOpeningFile(False)

# CalculateData() は、このピボットテーブルの表示 (データ + スタイル) を
# PivotCache に既にあるデータから再レンダリングします。ソースデータが変更されていないため、
# ソースへのラウンドトリップは行われず — キャッシュされた値のみが再計算され
# ワークシートのセルに反映されます。
pivotTable.calculateData()

# ワークブックをディスクに保存
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## 同じ PivotCache を共有するすべてのピボットテーブルを取得する

ワークブックには、多くの場合、すべて 1 つの共有キャッシュの上に存在する多くのピボットテーブルが含まれています。これらを列挙するには (たとえば、バッチ更新を実行する前や、共有キャッシュの影響を診断するために)、`PivotCache.getPivotTables()` を使用します。このメソッドは、指定されたキャッシュに依存するすべての `PivotTable` のコレクションを返します。

これは、2 つのピボットテーブルが実際に同じ `PivotCache` インスタンスを共有していることを確認する最も直接的な方法でもあります。キャッシュ参照を比較するか、`getPivotTables()` が返すコレクションを単純に反復処理し、どのピボットテーブルがそこに現れるかを観察できます。

次の例では、同じソース範囲に 2 つのピボットテーブルを作成し、同じキャッシュインスタンスを共有していることを確認してから、キャッシュのピボットテーブルを列挙します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotFieldType

# 移植されたコードはここ
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Sheet1")

worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(900)

pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivot1Index)
pivotTable1.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable1.addFieldToArea(PivotFieldType.DATA, "Amount")

pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivot2Index)
pivotTable2.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable2.addFieldToArea(PivotFieldType.DATA, "Amount")

sameCache = pivotTable1.getPivotCache() is pivotTable2.getPivotCache()
print("Pivot1 and Pivot2 share the same PivotCache: " + str(sameCache))

sharedPivotTables = pivotTable1.getPivotCache().getPivotTables()
print("Number of pivot tables sharing the cache: " + str(len(sharedPivotTables)))

for pt in sharedPivotTables:
    print("Pivot table name: " + pt.getName())

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## 廃止予定の `PivotTable.refreshData()` からの移行

Aspose.Cells for Aspose.Cells for Python via Java v26.7 より前では、ピボットテーブルを更新する標準的な方法は、各ピボットテーブルに対して個別に `PivotTable.refreshData()` を呼び出すことでした。v26.7 の時点で、そのメソッドは **廃止予定** とマークされており、上記のキャッシュ対応 API に置き換える必要があります。

実際のワークブックでは、テーブルごとの `refreshData()` アプローチに問題がある理由は 2 つあります。

- ソースが変更されていない場合でも、呼び出されるたびにソースからデータを再フェッチします。
- 各呼び出しは共有キャッシュ全体を更新します。多くのピボットテーブルが 1 つのキャッシュを共有している場合、ピボットテーブルごとに `refreshData()` を繰り返し呼び出すと、同じキャッシュが何度も再フェッチされ、非常に遅くなります。

推奨される代替手段は次のとおりです。

- **ワークブック内のすべてのピボットテーブルを更新する** → `workbook.refreshAll();` を使用する
- **一部のピボットテーブルを更新する** → 1 つのキャッシュに対して `pivotTable.getPivotCache().refresh();` を使用する。キャッシュは共有されているため、この 1 回の呼び出しでそのキャッシュの上に構築されたすべてのピボットテーブルが更新されます。すでに更新されたキャッシュ上に存在する他のピボットテーブルは、安全にスキップできます。
- **ピボットビュー/レイアウトのみが変更された** → ソースへのラウンドトリップなしで既存のキャッシュから再レンダリングするには、`pivotTable.calculateData();` を使用する。

次の例では、単一のキャッシュを共有する複数のピボットテーブルを持つワークブックの新しい効率的なパターンを示します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# 新しいワークブックを作成し、最初のワークシートにアクセスします
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# --- ソースデータの構築: 果物 / 年 / 金額 (ヘッダー + 9 行) ---
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000)
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000)
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500)
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500)
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000)
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800)
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200)
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700)

# --- 宛先セル E3 に最初のピボットテーブル (Pivot1) を追加 ---
idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = sheet.getPivotTables().get(idx1)
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# --- 同じソース範囲に 2 番目のピボットテーブル (Pivot2) を追加 ---
# Pivot1 と Pivot2 は 1 つの基礎となる PivotCache を共有します。
# これはまさに、レガシーのテーブルごとの RefreshData() のシナリオです
# アプローチが非効率になるシナリオ: 1 つのテーブルを更新すると、全体の再フェッチが発生します
# 共有キャッシュを更新するため、N 個のテーブルを更新すると、同じ高コストのフェッチを N 回実行します。
idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = sheet.getPivotTables().get(idx2)
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# --- ソースデータの複数の Amount 値を変更 ---
sheet.getCells().get("C2").putValue(5000)   # グレープ 2020
sheet.getCells().get("C5").putValue(7500)   # チェリー 2020
sheet.getCells().get("C9").putValue(9500)   # チェリー 2021

# --- 廃止されたパターン (26.7 以前) — PivotTable.RefreshData() ---
# pivotTable1.RefreshData();  // ソースから再フェッチし、キャッシュ全体を更新
# pivotTable2.RefreshData();  // 再フェッチ — キャッシュはすでに最新です!
# 各呼び出しは共有キャッシュを再構築するため、N テーブル = N 回の冗長なフェッチ。

# --- 新しい v26.7+ パターン: キャッシュを 1 回更新し、必要に応じて再レンダリング ---
# PivotCache.Refresh() を 1 回呼び出すと、変更された値が共有にプルされます
# キャッシュと、それを参照するすべてのピボットテーブルの表示を再計算します。
# Pivot1 と Pivot2 は 1 つの PivotCache を共有しているため、この 1 回の呼び出しで更新されます
# 両方のテーブル — ソースへの 2 回目のラウンドトリップは不要です。
pivotTable1.getPivotCache().refresh()

# CalculateData() はピボットテーブルの表示 (データ + スタイル) のみを再レンダリングします
# キャッシュにすでに保持されているデータから — ソースには触れません。
# ここでは API を実証するためだけに Pivot2 で呼び出します: キャッシュの後
# 1 回更新されると、依存するテーブルはすべて再レンダリングできます
# ソースに戻ることなく。 CalculateData() を単独で使用するのは、次の場合のみです
# ピボットテーブルの表示/レイアウト設定が変更され、キャッシュが最新である場合。
pivotTable2.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## どの更新 API を使用すべきか?

以下の表は、利用可能な更新 API とそれぞれを選択するタイミングをまとめたものです。

| 目標 | 推奨 API | メモ |
|------|-----------------|-------|
| ワークブック内のすべてを更新する | `Workbook.refreshAll()` | 1 回の呼び出しですべてのキャッシュとテーブルをカバーします。 |
| 単一シート上のピボットテーブルのみを更新する | `Worksheet.refreshPivotTables()` | 1 つのワークシートにスコープされます。 |
| 1 つのキャッシュのソースデータが変更された | `pivotTable.getPivotCache().refresh()` | その共有キャッシュ上のすべてのピボットテーブルを更新します。 |
| ビュー/レイアウト設定のみが変更された | `pivotTable.calculateData()` | 不要なソースラウンドトリップをスキップします。 |
| 共有キャッシュ上のすべてのピボットテーブルを一覧表示する | `pivotCache.getPivotTables()` | 一括更新の前に列挙するために使用します。 |

実際には、廃止予定のテーブルごとの `refreshData()` よりもキャッシュベースの API を優先してください。これらは共有キャッシュを認識し、不要なソースフェッチを回避し、更新要件を満たす最小スコープを選択できるようにします。

## 関連記事

- [セルへの画像の挿入](/cells/ja/python-java/inserting-an-image-into-a-cell/)
- [DBF ファイルの読み取りと書き込み](/cells/ja/python-java/dbf/)
- [Excel ファイルを複数のファイルに分割する](/cells/ja/python-java/splitting-excel-files-into-multiple-files/)
- [Aspose.Cells for Aspose.Cells for Python via Java のスパークライン](/cells/ja/python-java/sparkline/)

{{< app/cells/assistant language="python" >}}