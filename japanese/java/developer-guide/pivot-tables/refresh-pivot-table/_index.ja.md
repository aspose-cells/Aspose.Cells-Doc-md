---
title: Aspose.Cells for JavaでピボットテーブルとPivotCacheを更新
linktitle: Aspose.Cells for JavaでピボットテーブルとPivotCacheを更新
description: Aspose.Cells for Javaのv26.7以降のピボット更新APIを使用して、ピボットテーブルを更新する方法を学びます。この.brückでは、RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData、およびGetPivotTablesについて、実用的なコード例を説明します。
keywords: Aspose.Cells, Java, ピボットテーブル, 更新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ja/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cellsは、ワークブック全体から単一のピボットテーブルまで、4つの異なるスコープでピボットデータを再読み込みできる階層型の更新APIを提供します。**Aspose.Cells for Java v26.7**以降、従来のメソッド`PivotTable.refreshData()`は非推奨としてマークされており、この.extensionsで説明する、より効率的でキャッシュに対応するAPIに置き換える必要があります。
{{% /alert %}}

## Introduction
ピボットテーブルの更新が1つの操作だけで完結することはまれです。内部では、Aspose.Cellsは元のソースデータとワークシートに表示される値をつなぐ階層型のデータチェーンを管理しています。このチェーンを理解することが、さまざまな状況で適切な更新APIを選択するための鍵となります。
4層構造のデータチェーンは次のとおりです。
1. **データソース** — 元のワークシート範囲、データベースクエリ、または統合範囲であり、生の値が格納されているものです。
2. **PivotCache** — ソースデータのインメモリスナップショットです。すべてのピボットテーブルは`PivotCache`の上に構築され、データはここで収集されて集計されます。
3. **PivotTable** — 行、列、値、およびフィルター項目を定義するビューオブジェクトです。`PivotTable`が読み込むのは*`PivotCache`のみ*であり、データソースから直接読み込むことはありません。
4. **Cells** — `PivotTable`が計算済みの値とスタイルを描画するワークシートの`Cells`です。

{{% alert color="primary" %}}
`PivotCache.getSourceType()`（列挙型`PivotTableSourceType`）は、キャッシュデータの取得元を示します。v26.7現在、`PivotCache.refresh()`がサポートするソースタイプは**`Sheet`**と**`Consolidation`**のみです。つまり、ワークシート範囲に格納されているデータが対象です。外部ソース（データベース、外部接続など）は、キャッシュAPIではまだ更新できません。
このチェーンにより、Aspose.Cellsには2つの基本的な更新パスがあります。
- **`PivotTable.calculateData()`** — データソースへの往復処理なしで、キャッシュ済みデータから1つの`PivotTable`の表示を再計算します。
この記事のすべての例ではワークシートのセルをソースデータとして使用するため、ソースタイプは`Sheet`であり、更新操作は次のように動作します。
{{% /alert %}}

## Quick Start
ワークブック内のすべてのピボットテーブルを更新するために必要最小限のコードだけでよい場合は、1回の呼び出しで十分です。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

この記事の他のセクションでは、より対象を限定したAPIを選択すべき場合について説明します。

## Required Import Statements
ピボット関連の型は`com.aspose.cells.pivot`パッケージにあるため、この記事のJavaの例はすべて次のimportステートメントで始まります。
- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## Refresh All Pivot Tables in the Workbook
ワークブック内のすべてのPivotCacheとPivotTableが最新のソースデータを反映するようにする必要がある場合、最も包括的なAPIは`Workbook.refreshAll()`です。1回の呼び出しでワークブック全体を処理し、各`PivotCache`をソースから更新してから、それに依存するすべての`PivotTable`を再計算します。パフォーマンスをあまり気にしない場合の、一般的な文書全体の更新にはこの方法を推奨します。
次の例では、Fruit/Year/Amountのソース範囲を持つワークブックを作成し、1つのピボットテーブルを生成します。その後、一部のソース値を変更し、`refreshAll()`を1回呼び出すことで、すべてを最新の状態に更新します。

```java
import com.aspose.cells.*;
// Create a new workbook
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
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
// Add a pivot table: source range "A1:C9", destination cell "E3", name "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
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
他のワークシート上にあるピボットテーブルは関係がなく、変更してはいけないことが分かっている場合など、特定のワークシート上のピボットテーブルだけを更新する必要がある場合があります。この場合、Aspose.Cellsは`Worksheet.refreshPivotTables()`を提供しており、このメソッドは1つの`Worksheet`インスタンスに限定されます。

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

## Refresh a Single Pivot Table
単一のピボットテーブルを細かく制御したい場合、キャッシュベースのAPIには2つの選択肢があります。どちらを選ぶかは、実際に変更された内容、つまり基礎となるソースデータか、ピボットテーブル自体の表示/レイアウト設定かによって異なります。

### Source Data Changed — Use `PivotCache.refresh()`
基礎となるソースデータが変更された場合は、`pivotTable.getPivotCache().refresh()`が正しいエントリーポイントです。この呼び出しはソースデータをキャッシュに再読み込みし、そのキャッシュに依存するすべての`PivotTable`を再計算します。

### Only View/Layout Changed — Use `calculateData()`
ソースデータは*変更されていない*が、ピボットテーブルの表示またはレイアウト設定が変更されている場合（例：項目を別の領域に移動した場合、または開くときに更新する設定を切り替えた場合）、データソースへ往復する必要はありません。キャッシュにはすでに正しいデータが含まれているため、再計算が必要なのはレンダリングされた`PivotTable`だけです。この場合、`pivotTable.calculateData()`が正しい選択です。
次の例では、ピボットテーブルのソース以外のプロパティを変更し、既存のキャッシュから再レンダリングするために`calculateData()`を呼び出します。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
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
// Add a pivot table named "Pivot1" placed at destination cell E3, sourcing from A1:C9
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Modify a view/layout property -- this is a presentation-only change,
// so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() re-renders THIS pivot table's display (data + style) from the
// data already held in the PivotCache. Because the source data did not change,
// no round-trip to the source is performed -- only the cached values are recalculated
// into worksheet cells.
pivotTable.calculateData();
// Save the workbook to disk
workbook.save("output.xlsx");
```

1つの共有キャッシュの上に置かれた多数のピボットテーブルを含むワークブックも_argument:_.それらを列挙するには、たとえば一括更新の実行前や共有キャッシュの影響を診断するときに、`PivotCache.getPivotTables()`を使用します。このメソッドは、指定されたキャッシュに依存するすべての`PivotTable`のコレクションを返します。

## Migrating from the Obsolete `PivotTable.refreshData()`
Aspose.Cells for Java v26.7より前は、ピボットテーブルを更新する標準的な方法は、各ピボットテーブルで`PivotTable.refreshData()`を個別に呼び出すことでした。v26.7以降、このメソッドは**非推奨**とマークされ、上記で説明したキャッシュ対応APIに置き換える必要があります。
実際のワークブックで、テーブルごとの`refreshData()`アプローチが問題になる理由は次のとおりです。
- ソースが変更されていない場合でも、呼び出すたびにソースからデータを再取得します。
推奨される置き換え方法は次のとおりです。
次の例では、1つのキャッシュを共有する複数のピボットテーブルを持つワークブックの新しい効率的なパターンを示します。

## Which Refresh API Should I Use?
以下の表は、利用可能な更新APIと、それぞれの選択基準をまとめたものです。
| 目的 | 推奨API | 注記 |
|------|-----------------|-------|
| ワークブック内のすべてを更新する | `Workbook.refreshAll()` | 1回の呼び出しですべてのキャッシュとテーブルを処理します。 |
| 単一シート上のピボットテーブルのみを更新する | `Worksheet.refreshPivotTables()` | 1つのワークシートに限定されます。 |
| 1つのキャッシュのソースデータが変更された | `pivotTable.getPivotCache().refresh()` | その共有キャッシュ上のすべてのピボットテーブルを更新します。 |
| 表示またはレイアウトの設定だけが変更された | `pivotTable.calculateData()` | 不要なソースへの往復処理を省略します。 |
| 共有キャッシュ上のすべてのピボットテーブルを一覧表示する | `pivotCache.getPivotTables()` | 一括更新の前に列挙します。 |
実際の使用では、非推奨のテーブルごとの`refreshData()`より、キャッシュベースのAPIを優先してください。共有キャッシュを認識し、冗長なソース取得を避け、更新要件を満たす最小の範囲を選択できます。

## Common Pitfalls
- **保存前に更新するのを忘れる。** ピボットテーブルは、データチェーンが更新されたときにのみ、レンダリングされた値をワークシートに書き込みます。ソースセルを変更した場合は、`Workbook.save()`の前に`PivotCache.refresh()`（または`Workbook.refreshAll()`）を呼び出してください。そうしないと、保存されるファイルに古い集計値が含まれたままになります。
- **廃止予定の`refreshData()`をテーブルごとに呼び出す。** v26.7では、`PivotTable.refreshData()`は非推奨とマークされており、呼び出しごとにソースを再取得します。複数のピボットテーブルが1つのキャッシュを共有している場合、N回の冗長なソース取得になります。1回の`PivotCache.refresh()`と、各テーブルに対する`calculateData()`で置き換えてください。
- **レイアウトだけを変更したときに更新する。** ソースデータに触れることなくピボットテーブルの表示（列の順序、`ConsolidationFunction`など）のみ変更した場合、`PivotCache.refresh()`は不要であり、遅くなります。`pivotTable.calculateData()`を呼び出して、既存のキャッシュから再レンダリングしてください。
- **`PivotCache.refresh()`がサポートしない外部ソース。** ピボットテーブルのソースが外部接続（データベース、OLAPキューブなど）からの場合、v26.7では`PivotCache.refresh()`で更新できません。現在サポートされているのは`Sheet`と`Consolidation`のソースタイプのみです。外部ソースの場合は、ワークブックを開き直すか、ソースからキャッシュを再構築してください。

{{< app/cells/assistant language="java" >}}