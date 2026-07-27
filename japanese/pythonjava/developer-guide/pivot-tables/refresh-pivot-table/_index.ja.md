---
title: Aspose.Cells for Python via Java でのピボットテーブルの更新
linktitle: Aspose.Cells for Python via Java でのピボットテーブルの更新
description: Aspose.Cells for Python via Java で v26.7+ のピボット更新 API を使用してピボットテーブルを更新する方法を学びます。本記事では RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData、GetPivotTables を実践的なコード例とともに解説します。
keywords: Aspose.Cells, Python via Java, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ja/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ワークブック全体から単一のピボットテーブルまで、4 つの異なるスコープでピボットデータを再読み込みできる階層的な更新 API を提供します。**Aspose.Cells for Python via Java v26.7** 以降、旧メソッド `PivotTable.refreshData()` は非推奨となり、本記事で紹介するより効率的でキャッシュを認識する API に置き換える必要があります。
{{% /alert %}}
## はじめに
ピボットテーブルの更新は、単一の操作であることはほとんどありません。Aspose.Cells は舞台裏で、元のソースデータとワークシートに表示されるレンダリングされた値を結ぶ階層的なデータチェーンを維持しています。このチェーンを理解することが、あらゆる状況に適した更新 API を選択する鍵となります。
4 層のデータチェーンは次のとおりです。
1. **データソース** — 生の値が格納されている元のワークシート範囲、データベースクエリ、または統合範囲。
2. **PivotCache** — ソースデータのメモリ内スナップショット。すべてのピボットテーブルは `PivotCache` の上に構築されます。ここで、すべてのデータが収集および集計されます。
3. **PivotTable** — 行、列、値、フィルタの各フィールドを定義するビューオブジェクト。`PivotTable` はデータソースから直接ではなく、`PivotCache` からのみデータを読み取ります。
4. **Cells** — `PivotTable` が計算結果とスタイルを描画するワークシートの `Cells`。
特に重要な概念は **共有キャッシュ** です。ワークブック内の複数のピボットテーブルが同じソース範囲を参照している場合、それらは *1 つの* `PivotCache` インスタンスを共有します。1 つの `PivotCache` は多くのピボットテーブルから参照でき、そのキャッシュを更新すると、依存するすべての `PivotTable` が一度に更新されます。
{{% alert color="primary" %}}
`PivotCache.getSourceType()` (列挙型 `PivotTableSourceType`) は、キャッシュデータの取得元を示します。v26.7 以降、`PivotCache.refresh()` は **`SHEET`** および **`CONSOLIDATION`** のソースタイプのみをサポートします。つまり、ワークシート範囲にあるデータのみです。外部ソース (データベース、外部接続など) は、キャッシュ API を通じてはまだ更新できません。
{{% /alert %}}
このチェーンにより、Aspose.Cells には 2 つの基本的な更新パスがあります。
- **`PivotCache.refresh()`** — ソースからキャッシュへデータを再読み込みし、すべての依存する `PivotTable` を単一の操作で再計算します。
- **`PivotTable.calculateData()`** — すでにキャッシュされているデータから、1 つの `PivotTable` の表示を再計算します。データソースへのラウンドトリップはありません。
本記事のすべてのシナリオではワークシートセルのソースデータを使用しているため、ソースタイプは `SHEET` であり、更新操作は記載どおりに動作します。
## 必要なインポート
本記事のすべての Python の例では、ピボット型が `aspose.cells.pivot` 名前空間に存在するため、次のインポートを使用します。
`jpype` モジュールは JVM のブートストラップに使用され、`aspose.cells` は本記事全体で使用されるワークブック/ワークシート/セル/ピボットの型を公開します。
## ワークブック内のすべてのピボットテーブルを更新する
ワークブック内のすべてのピボットキャッシュとすべてのピボットテーブルが最新のソースデータを反映していることを確認する必要がある場合、最もシンプルで包括的な API は `Workbook.refreshAll()` です。1 回の呼び出しでワークブック全体を走査し、各 `PivotCache` をソースから更新し、その後、依存するすべての `PivotTable` を再計算します。これは、パフォーマンスが気にならない一般的な全ドキュメント更新に推奨されるアプローチです。
次の例では、Fruit/Year/Amount のソース範囲を持つワークブックを作成し、1 つのピボットテーブルを作成し、ソース値の一部を変更し、`refreshAll()` を使用してすべてを 1 回の呼び出しで最新の状態にします。
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# 新しいワークブックを作成
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# セルA1:C1に見出し行を書き込む
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# セルA2:C9にデータ行を書き込む（2020年と2021年のフルーツデータ8行）
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

# ピボットテーブルを追加：ソース範囲「A1:C9」、配置先セル「E3」、名前「Pivot1」
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# ピボットフィールドを割り当て：Fruitは行、Yearは列、Amountはデータ
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# ソースデータのAmount値をいくつか変更して変更をシミュレート
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
特定のワークシート上にあるピボットテーブルのみを更新する必要がある場合があります。例えば、他のワークシート上のピボットテーブルは無関係であることがわかっており、触れたくない場合です。この場合のために、Aspose.Cells は単一の `Worksheet` インスタンスにスコープされた `Worksheet.refreshPivotTables()` を提供します。
これは `Workbook.refreshAll()` よりも選択的です。対象のワークシート上のピボットテーブルのみが更新され、他のワークシート上のピボットテーブルはそのまま残されます。
次の例では、同じ Fruit/Year/Amount のソースデータを設定し、最初のワークシートにピボットテーブルを追加し、ソース値の一部を変更し、そのワークシート上のピボットテーブルのみを更新します。
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
単一のピボットテーブルをきめ細かく制御したい場合、キャッシュベースの API には 2 つのオプションがあります。どちらを選択するかは、実際に変更された内容、つまり基になるソースデータか、ピボットテーブル自体のビュー/レイアウト設定のみかによって異なります。
### ソースデータが変更された場合 — `PivotCache.refresh()` を使用する
基になるソースデータが変更された場合、正しいエントリポイントは `pivotTable.getPivotCache().refresh()` です。この呼び出しはソースデータをキャッシュに再読み込みし、そのキャッシュに依存するすべての `PivotTable` を再計算します。
{{% alert color="primary" %}}
ピボットテーブルは単一の `PivotCache` インスタンスを共有するため、`PivotCache.refresh()` を呼び出すと、参照した 1 つだけでなく、**同じキャッシュ上に構築されたすべての** ピボットテーブルが再計算されます。2 つのピボットテーブルが同じソース範囲を共有している場合、1 つのキャッシュを更新すると両方が更新されます。
{{% /alert %}}
次の例では、この共有キャッシュの動作を示すために、同じソース範囲上に 2 つのピボットテーブルを作成し、ソース値の一部を変更し、1 つのキャッシュ参照を通じて更新します。
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

# 約9行のデータ行を書き込みます（2020〜2021年における grape / blueberry / kiwi / cherry）
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

# セルE3にアンカーされ、ソース範囲A1:C9を持つ最初のピボットテーブル"Pivot1"を追加します
pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivotIndex1)

# Pivot1のフィールドを割り当てます
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# 同じソース範囲A1:C9を使用して、セルE15にアンカーされた2番目のピボットテーブル"Pivot2"を追加します
# Pivot1とPivot2はソース範囲が同一であるため、単一のPivotCacheを共有します。
pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivotIndex2)

# Pivot2に同じフィールドを割り当てます
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# データ変更をシミュレートするために、ソースデータの複数のAmountセルの値を変更します
worksheet.getCells().get("C2").putValue(150)
worksheet.getCells().get("C4").putValue(350)
worksheet.getCells().get("C7").putValue(650)

# 共有されているPivotCacheを更新します。
# Pivot1とPivot2は同じPivotCacheを共有しているため、この単一の呼び出しで
# 更新されたソースから両方のピボットテーブル（データ + スタイル）を更新します。
pivotTable1.getPivotCache().refresh()

# ワークブックを保存します
workbook.save("output.xlsx")

jpype.shutdownJVM()
```
### ビュー/レイアウトのみが変更された場合 — `calculateData()` を使用する
ソースデータは変更されておらず、ピボットテーブルのビューまたはレイアウト設定のみが変更された場合 (たとえば、フィールドが別のエリアに移動された、またはファイルを開くときに更新する設定が切り替えられた場合)、データソースへのラウンドトリップは必要ありません。キャッシュにはすでに正しいデータが保持されています。レンダリングされた `PivotTable` の再計算のみが必要です。この場合、`pivotTable.calculateData()` が正しい選択です。
これにより、不要なソースフェッチが回避され、多くのピボットテーブルが同じキャッシュを共有している場合に大幅に高速化されます。
次の例では、ピボットテーブルのソース以外のプロパティを変更し、`calculateData()` を呼び出して既存のキャッシュから再レンダリングします。
```python
posecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Fruit / Year / Amount のヘッダー行を書き込み
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# 8 つのデータ行を書き込み (2-9 行目、ソース範囲 A1:C9 に収まる)
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

# "Pivot1" という名前のピボットテーブルを、配置先セル E3 に、A1:C9 をソースとして追加
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# フィールドを割り当て: Fruit を行、Year を列、Amount をデータ
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# 表示/レイアウトのプロパティを変更 — これは表示のみの変更です、
# したがって、PivotCache.Refresh() を通してソースデータを再読み込みする必要はありません。
pivotTable.setRefreshDataOnOpeningFile(False)

# CalculateData() は、このピボットテーブルの表示 (データ + スタイル) を、
# PivotCache に既に保持されているデータから再レンダリングします。ソースデータが変更されていないため、
# ソースへのラウンドトリップは実行されません — キャッシュされた値のみが再計算されます
# ワークシートのセルに展開されます。
pivotTable.calculateData()

# ワークブックをディスクに保存
workbook.save("output.xlsx")

jpype.shutdownJVM()
```
## 同じ PivotCache を共有するすべてのピボットテーブルを取得する
ワークブックには、1 つの共有キャッシュ上に存在する多くのピボットテーブルが含まれていることがよくあります。これらを列挙するには (たとえば、バッチ更新を実行する前や、共有キャッシュの影響を診断するために)、`PivotCache.getPivotTables()` を使用します。このメソッドは、指定されたキャッシュに依存するすべての `PivotTable` のコレクションを返します。
これは、2 つのピボットテーブルが実際に同じ `PivotCache` インスタンスを共有していることを確認する最も直接的な方法でもあります。キャッシュ参照を比較したり、`getPivotTables()` によって返されたコレクションを反復処理し、どのピボットテーブルがそれに含まれるかを観察したりすることができます。
次の例では、同じソース範囲上に 2 つのピボットテーブルを作成し、それらが同じキャッシュインスタンスを共有していることを確認し、キャッシュのピボットテーブルを列挙します。

## 非推奨の `PivotTable.refreshData()` からの移行
Aspose.Cells for Python via Java v26.7 より前は、ピボットテーブルを更新する標準的な方法は、各ピボットテーブルに対して個別に `PivotTable.refreshData()` を呼び出すことでした。v26.7 以降、そのメソッドは **非推奨** としてマークされており、上記のキャッシュを認識する API に置き換える必要があります。
実際のワークブックでテーブルごとの `refreshData()` アプローチに問題がある理由は 2 つあります。
- ソースが変更されていない場合でも、呼び出されるたびにソースからデータを再フェッチします。
- 各呼び出しは共有キャッシュ全体を更新します。多くのピボットテーブルが 1 つのキャッシュを共有している場合、ピボットテーブルごとに `refreshData()` を繰り返し呼び出すと、同じキャッシュが何度も再フェッチされることになり、非常に低速になります。
推奨される代替手段は次のとおりです。
- **ワークブック内のすべてのピボットテーブルを更新する** → `workbook.refreshAll();` を使用します。
- **一部のピボットテーブルを更新する** → 1 つのキャッシュに対して `pivotTable.getPivotCache().refresh();` を使用します。キャッシュは共有されているため、この 1 回の呼び出しで、そのキャッシュ上に構築されたすべてのピボットテーブルが更新されます。すでに更新されたキャッシュ上に存在する他のピボットテーブルは、安全にスキップできます。
- **ピボットビュー/レイアウトのみが変更された** → ソースへのラウンドトリップなしで既存のキャッシュから再レンダリングするには `pivotTable.calculateData();` を使用します。
次の例では、単一のキャッシュを共有する複数のピボットテーブルを持つワークブックの新しい効率的なパターンを示します。

## どの更新 API を使用すべきか?
次の表は、利用可能な更新 API と、それぞれをいつ選択すべきかをまとめたものです。
| 目標 | 推奨される API | 備考 |
|------|-----------------|-------|
| ワークブック内のすべてを更新する | `Workbook.refreshAll()` | 1 回の呼び出しですべてのキャッシュとテーブルをカバーします。 |
| 単一シート上のピボットテーブルのみを更新する | `Worksheet.refreshPivotTables()` | 1 つのワークシートにスコープされます。 |
| 1 つのキャッシュのソースデータが変更された | `pivotTable.getPivotCache().refresh()` | その共有キャッシュ上のすべてのピボットテーブルを更新します。 |
| ビュー/レイアウト設定のみが変更された | `pivotTable.calculateData()` | 不要なソースへのラウンドトリップをスキップします。 |
| 共有キャッシュ上のすべてのピボットテーブルを一覧表示する | `pivotCache.getPivotTables()` | 一括更新の前に列挙するために使用します。 |
実際には、非推奨のテーブルごとの `refreshData()` よりもキャッシュベースの API を優先してください。これらは共有キャッシュを認識し、冗長なソースフェッチを回避し、更新要件を満たす最小のスコープを選択できるようにします。{{< app/cells/assistant language="python" >}}
