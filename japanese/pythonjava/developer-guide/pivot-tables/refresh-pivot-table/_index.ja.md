---
title: Aspose.Cells for Python via Java でピボットテーブルとピボットキャッシュを更新する
linktitle: Aspose.Cells for Python via Java でピボットテーブルとピボットキャッシュを更新する
description: Aspose.Cells for Python via Java の v26.7+ ピボット更新 API を使用してピボットテーブルを更新する方法を説明します。本記事では RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData、GetPivotTables を実践的なコード例とともに解説します。
keywords: Aspose.Cells, Python via Java, ピボットテーブル, 更新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ja/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ワークブック全体から単一のピボットテーブルまで、4 つの異なるスコープでピボットデータを再読み込みできる階層型更新 API を提供します。**Aspose.Cells for Python via Java v26.7** 以降、旧来のメソッド `PivotTable.refreshData()` は非推奨となり、本記事で紹介するより効率的なキャッシュ対応 API に置き換える必要があります。
{{% /alert %}}

## はじめに
ピボットテーブルの更新は、単一の操作であることはほとんどありません。舞台裏では、Aspose.Cells は元のソースデータからワークシートに表示される値へと接続する階層的なデータチェーンを維持しています。このチェーンを理解することが、状況に応じて適切な更新 API を選択する鍵となります。
4 層のデータチェーンは以下のとおりです。
1. **データソース** — 生の値が格納されている、元のワークシート範囲、データベースクエリ、または統合範囲。
2. **PivotCache** — ソースデータのメモリ内スナップショット。すべてのピボットテーブルは `PivotCache` の上に構築され、すべてのデータの収集と集計はここで行われます。
3. **PivotTable** — 行、列、値、フィルタの各フィールドを定義するビューオブジェクト。`PivotTable` は `PivotCache` からの*み*データを読み取り、データソースから直接読み取ることはありません。
4. **Cells** — `PivotTable` が計算結果とスタイルを描画する先のワークシートの `Cells`。

{{% alert color="primary" %}}
`PivotCache.getSourceType()`(列挙型 `PivotTableSourceType`)は、キャッシュデータの取得元を示します。v26.7 時点で、`PivotCache.refresh()` がサポートするのは **`SHEET`** と **`CONSOLIDATION`** のソースタイプ、つまりワークシート範囲に存在するデータのみです。外部ソース(データベースや外部接続など)は、現時点ではキャッシュ API 経由では更新できません。
{{% /alert %}}

このチェーンのため、Aspose.Cells には 2 つの基本的な更新パスがあります。
- **`PivotTable.calculateData()`** — すでにキャッシュされたデータから 1 つの `PivotTable` の表示を再計算し、データソースへのラウンドトリップは行いません。
本記事のすべてのシナリオではワークシートセルをソースデータとして使用しているため、ソースタイプは `SHEET` となり、更新操作は前述のとおりに動作します。

## クイックスタート
ワークブック内のすべてのピボットを更新する最小限のコードが必要な場合は、1 つの呼び出しだけで十分です。

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
# データ行をセルA2:C9に書き込む（2020年と2021年にわたる8行の果物のデータ）
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
# ピボットフィールドを割り当て：Fruitを行、Yearを列、Amountをデータ
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
# ソースデータのいくつかのAmountの値を変更して変更をシミュレート
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)
# ワークブック内のすべてのピボットテーブル/ピボットキャッシュを更新
workbook.refreshAll()
# ワークブックを保存
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

本記事の以降のセクションでは、より限定的な API を選択すべきケースについて説明します。

## 必要なインポート
本記事のすべての Python サンプルは、ピボット型が `aspose.cells.pivot` 名前空間に存在するため、次のインポートに依存しています。
- `import jpype`
- `import aspose.cells as cells`
`jpype` モジュールは JVM をブートストラップするために使用され、`aspose.cells` は全体で使用される workbook/worksheet/cell/pivot 型を公開します。

## ワークブック内のすべてのピボットテーブルを更新する
ワークブック内のすべてのピボットキャッシュとすべてのピボットテーブルが最新のソースデータを反映するようにする必要がある場合、最もシンプルで包括的な API は `Workbook.refreshAll()` です。この 1 つの呼び出しでワークブック全体を走査し、各 `PivotCache` をソースから更新した後、依存するすべての `PivotTable` を再計算します。パフォーマンスを重視しない通常の全ドキュメント更新には、この方法が推奨されます。
次の例では、Fruit/Year/Amount のソース範囲を持つワークブックを構築し、1 つのピボットテーブルを作成し、一部のソース値を変更した後、`refreshAll()` を使用して 1 回の呼び出しですべてを最新の状態にします。

```python
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

## 単一ワークシート上のすべてのピボットテーブルを更新する
特定のワークシート上にあるピボットテーブルだけを更新したい場合があります。たとえば、他のワークシート上のピボットテーブルは無関係で変更すべきではないことが分かっている場合です。このような場合のために、Aspose.Cells は単一の `Worksheet` インスタンスを対象とする `Worksheet.refreshPivotTables()` を提供しています。

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
単一のピボットテーブルを細かく制御したい場合は、キャッシュベースの API に 2 つの選択肢があります。どちらを選ぶかは、実際に何が変わったか、つまり基になるソースデータなのか、ピボットテーブル自身のビュー/レイアウト設定のみなのかによって異なります。

### ソースデータが変更された場合 — `PivotCache.refresh()` を使用
基になるソースデータが変更された場合、正しいエントリポイントは `pivotTable.getPivotCache().refresh()` です。この呼び出しはソースデータをキャッシュに再読み込みし、そのキャッシュに依存するすべての `PivotTable` を再計算します。

### ビュー/レイアウトのみが変更された場合 — `calculateData()` を使用
ソースデータが変更されておらず、ピボットテーブルのビューまたはレイアウト設定のみが変更された場合(たとえば、フィールドが別のエリアに移動された場合や、ファイルを開く際に更新する設定が切り替えられた場合)、データソースへのラウンドトリップは必要ありません。キャッシュにはすでに正しいデータが保持されているため、再計算する必要があるのはレンダリングされた `PivotTable` のみです。このような場合、`pivotTable.calculateData()` が正しい選択です。
次の例では、ピボットテーブルのソース以外のプロパティを変更し、その後 `calculateData()` を呼び出して既存のキャッシュから再レンダリングします。

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
# 8 つのデータ行を書き込む（行 2-9、ソース範囲 A1:C9 に適合）
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
# フィールドを割り当てる：Fruit を行、Year を列、Amount をデータ
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
# 表示/レイアウトのプロパティを変更する — これは表示のみの変更であり、
# PivotCache.Refresh() を介してソースデータを再読み込みする必要はない。
pivotTable.setRefreshDataOnOpeningFile(False)
# CalculateData() は、PivotCache に保持されているデータから
# このピボットテーブルの表示（データ + スタイル）を再描画する。ソースデータが変更されていないため、
# ソースへのラウンドトリップは行われず、キャッシュされた値のみが
# ワークシートのセルに再計算される。
pivotTable.calculateData()
# ワークブックをディスクに保存する
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

ワークブックには、1 つの共有キャッシュの上に存在する多くのピボットテーブルが含まれていることがよくあります。これらを列挙する場合(たとえば、一括更新を実行する前や、共有キャッシュの影響を診断する場合)は、`PivotCache.getPivotTables()` を使用します。このメソッドは、指定されたキャッシュに依存するすべての `PivotTable` のコレクションを返します。

## 非推奨の `PivotTable.refreshData()` からの移行
Aspose.Cells for Python via Java v26.7 以前では、ピボットテーブルを更新する標準的な方法は、各ピボットテーブルに対して個別に `PivotTable.refreshData()` を呼び出すことでした。v26.7 以降、このメソッドは **非推奨** となり、上記で説明したキャッシュ対応 API に置き換える必要があります。
実際のワークブックでは、テーブルごとの `refreshData()` アプローチに問題がある理由は 2 つあります。
- ソースが変更されていない場合でも、呼び出すたびにソースからデータを再取得します。
推奨される代替方法は次のとおりです。
次の例では、単一キャッシュを共有する複数のピボットテーブルを持つワークブックに対する新しい効率的なパターンを示します。

## どの更新 API を使用すべきか?
次の表は、利用可能な更新 API とそれぞれの選択基準をまとめたものです。
| 目的 | 推奨 API | メモ |
|------|---------|------|
| ワークブック全体を更新 | `Workbook.refreshAll()` | 1 回の呼び出しで、すべてのキャッシュとテーブルをカバー。 |
| 単一ワークシート上のピボットテーブルのみを更新 | `Worksheet.refreshPivotTables()` | 1 つのワークシートに限定。 |
| 1 つのキャッシュのソースデータが変更された | `pivotTable.getPivotCache().refresh()` | 共有キャッシュ上のすべてのピボットテーブルを更新。 |
| ビュー/レイアウト設定のみが変更された | `pivotTable.calculateData()` | 不要なソースラウンドトリップを回避。 |
| 共有キャッシュ上のすべてのピボットテーブルを列挙 | `pivotCache.getPivotTables()` | 一括更新の前に列挙するために使用。 |
実際には、非推奨のテーブルごとの `refreshData()` よりもキャッシュベースの API を優先してください。これらは共有キャッシュを認識し、冗長なソース取得を回避し、更新要件を満たす最小のスコープを選択できるようにします。

## よくある落とし穴
- **保存前に更新を忘れる。** ピボットテーブルは、データチェーンが更新されたときにのみ、レンダリングされた値をワークシートに書き込みます。ソースセルを変更した場合は、`Workbook.save()` の前に `PivotCache.Refresh()`(または `Workbook.RefreshAll()`)を呼び出してください。さもないと、保存されたファイルには古い集計値が含まれたままになります。
- **テーブルごとに非推奨の `RefreshData()` を呼び出す。** v26.7 では、`PivotTable.RefreshData()` は非推奨であり、呼び出しごとにソースを再取得します。複数のピボットテーブルがキャッシュを共有している場合、N 回の冗長なソース取得が発生します。テーブルごとに 1 つの `PivotCache.Refresh()` の後に `CalculateData()` を呼び出す方法で置き換えてください。
- **レイアウトのみが変更された場合に更新する。** ソースデータに触れずにピボットテーブルのビュー(列順、`ConsolidationFunction` など)のみを変更した場合は、`PivotCache.Refresh()` は不要であり、処理も遅くなります。`pivotTable.CalculateData()` を呼び出して、既存のキャッシュから再レンダリングしてください。
- **外部ソースは `PivotCache.Refresh()` でサポートされない。** ピボットテーブルのソースが外部接続(データベース、OLAP キューブなど)からのものである場合、`PivotCache.Refresh()` では v26.7 で更新できません。現在サポートされているのは `Sheet` と `Consolidation` のソースタイプのみです。外部ソースの場合は、ワークブックを再度開くか、ソースからキャッシュを再構築してください。

{{< app/cells/assistant language="python" >}}