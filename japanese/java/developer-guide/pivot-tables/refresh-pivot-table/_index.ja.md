---
title: Aspose.Cells for Java でのピボットテーブルの更新
linktitle: Aspose.Cells for Java でのピボットテーブルの更新
description: Aspose.Cells for Java でのピボットテーブルの更新方法を v26.7+ のピボット更新 API を使って学習します。本記事では RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData、GetPivotTables を実用的なコード例とともに解説します。
keywords: Aspose.Cells, Java, ピボットテーブル, 更新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ja/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は、ワークブック全体から単一のピボットテーブルまで、4 つの異なるスコープでピボットデータを再ロードできる階層型の更新 API を提供します。**Aspose.Cells for Aspose.Cells for Java v26.7** 以降、従来のメソッド `PivotTable.refreshData()` は非推奨となり、本記事で説明するより効率的でキャッシュを認識する API に置き換える必要があります。

{{% /alert %}}

## はじめに

ピボットテーブルの更新は、単一の操作であることはほとんどありません。その裏側では、Aspose.Cells は元のソースデータからワークシートに表示されるレンダリング済みの値までを結ぶ、階層化されたデータチェーンを維持しています。このチェーンを理解することが、あらゆる状況に対して適切な更新 API を選択する鍵となります。

4 層のデータチェーンは次のとおりです。

1. **データソース** — 生の値が存在する元のワークシートの範囲、データベースクエリ、または統合範囲。
2. **PivotCache** — ソースデータのインメモリスナップショット。すべてのピボットテーブルは `PivotCache` の上に構築されます。すべてのデータはここで収集・集計されます。
3. **PivotTable** — 行、列、値、フィルタのフィールドを定義するビューオブジェクト。`PivotTable` はデータソースから直接ではなく、`PivotCache` からのみデータを読み取ります。
4. **Cells** — `PivotTable` が計算された値とスタイルを描画する先のワークシートの `Cells`。

特に重要な概念は **共有キャッシュ** です。ワークブック内の複数のピボットテーブルが同じソース範囲を参照している場合、それらは *1つの* `PivotCache` インスタンスを共有します。1 つの `PivotCache` は多くのピボットテーブルから参照でき、そのキャッシュを更新すると、依存するすべての `PivotTable` が一度に更新されます。

{{% alert color="primary" %}}

`PivotCache.getSourceType()`（列挙型 `PivotTableSourceType`）は、キャッシュデータの取得元を示します。v26.7 の時点で、`PivotCache.refresh()` は **`Sheet`** および **`Consolidation`** のソースタイプのみをサポートします。つまり、ワークシートの範囲に存在するデータのみです。外部ソース（データベース、外部接続など）は、キャッシュ API を通じてはまだ更新できません。

{{% /alert %}}

このチェーンのため、Aspose.Cells には 2 つの基本的な更新パスがあります。

- **`PivotCache.refresh()`** — ソースからキャッシュへ再ロードし、依存するすべての `PivotTable` を 1 回の操作で再計算します。
- **`PivotTable.calculateData()`** — すでにキャッシュされたデータから 1 つの `PivotTable` の表示を再計算します。データソースへのラウンドトリップはありません。

本記事のすべてのシナリオではワークシートセルをソースデータとして使用しているため、ソースタイプは `Sheet` であり、更新操作は説明どおりに動作します。

## 必要なインポート文

本記事のすべての Java の例は、ピボットタイプが `com.aspose.cells.pivot` パッケージに存在するため、以下のインポート文から始まります。

- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## ワークブック内のすべてのピボットテーブルを更新する

ワークブック内のすべてのピボットキャッシュとすべてのピボットテーブルが最新のソースデータを反映するようにする必要がある場合、最もシンプルで包括的な API は `Workbook.refreshAll()` です。1 回の呼び出しでワークブック全体を走査し、各 `PivotCache` をソースから更新し、依存するすべての `PivotTable` を再計算します。これは、パフォーマンスが気にならない一般的なドキュメント全体の更新に対して推奨されるアプローチです。

次の例では、Fruit/Year/Amount のソース範囲を持つワークブックを作成し、1 つのピボットテーブルを作成し、一部のソース値を変更し、その後 `refreshAll()` を使用してすべてを 1 回の呼び出しで最新状態にします。

```java
import com.aspose.cells.*;

// 新しいワークブックを作成
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// A1:C1 のセルにヘッダー行を書き込む
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// A2:C9 のセルにデータ行を書き込む（2020年と2021年にわたる8行の果物データ）
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

// ピボットテーブルを追加：ソース範囲 "A1:C9"、配置先セル "E3"、名前 "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// ピボットフィールドを割り当て：Fruit を行、Year を列、Amount をデータ
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// 変更をシミュレートするためにソースデータのいくつかの Amount 値を変更
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// ワークブック内のすべてのピボットテーブル/ピボットキャッシュを更新
workbook.refreshAll();

// ワークブックを保存
workbook.save("output.xlsx");
```

## 単一のワークシート上のすべてのピボットテーブルを更新する

ときには、特定の 1 つのワークシート上に存在するピボットテーブルだけを更新する必要がある場合があります。たとえば、他のワークシートのピボットテーブルは無関係であることがわかっており、触れたくない場合です。このケースのために、Aspose.Cells は `Worksheet.refreshPivotTables()` を提供しており、単一の `Worksheet` インスタンスを対象とします。

これは `Workbook.refreshAll()` よりも選択的です。対象のワークシート上のピボットテーブルだけが更新され、他のワークシート上のピボットテーブルはそのまま残されます。

次の例では、同じ Fruit/Year/Amount のソースデータを設定し、最初のワークシートにピボットテーブルを追加し、一部のソース値を変更した後、そのワークシート上のピボットテーブルだけを更新します。

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

## 単一のピボットテーブルを更新する

単一のピボットテーブルを細かく制御したい場合は、キャッシュベースの API が 2 つの選択肢を提供します。どちらを選択するかは、実際に何が変わったかによって異なります。基になるソースデータなのか、それともピボットテーブル自体のビュー/レイアウト設定のみなのかです。

### ソースデータが変更された場合 — `PivotCache.refresh()` を使用する

基になるソースデータが変更された場合、正しいエントリーポイントは `pivotTable.getPivotCache().refresh()` です。この呼び出しはソースデータをキャッシュに再読み込みし、そのキャッシュに依存するすべての `PivotTable` を再計算します。

{{% alert color="primary" %}}

ピボットテーブルは単一の `PivotCache` インスタンスを共有するため、`PivotCache.refresh()` を呼び出すと、参照した 1 つだけでなく、その同じキャッシュ上に構築された **すべての** ピボットテーブルが再計算されます。2 つのピボットテーブルが同じソース範囲を共有している場合、1 つのキャッシュを更新すると両方が更新されます。

{{% /alert %}}

次の例では、この共有キャッシュの動作を示すために、同じソース範囲上に 2 つのピボットテーブルを作成し、一部のソース値を変更し、その後 1 つのキャッシュ参照を通じて更新します。

```java
import com.aspose.cells.*;

// 新しいワークブックを作成し、最初のワークシートにアクセスする
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// ヘッダー行を書き込む: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 約9行のデータ行を書き込む（2020〜2021年のgrape / blueberry / kiwi / cherry）
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
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

// セルE3に配置する最初のピボットテーブル「Pivot1」を追加、ソース範囲はA1:C9
int pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// Pivot1のフィールドを割り当てる
pivotTable1.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable1.addFieldToArea(PivotFieldType.DATA, "Amount");

// 同じソース範囲A1:C9を使用して、E15に配置する2番目のピボットテーブル「Pivot2」を追加する
// ソース範囲が同一であるため、Pivot1とPivot2は単一のPivotCacheを共有する。
int pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Pivot2に同じフィールドを割り当てる
pivotTable2.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable2.addFieldToArea(PivotFieldType.DATA, "Amount");

// データ変更をシミュレートするため、ソースデータの複数のAmountセルの値を変更する
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// 共有されているPivotCacheを更新する。
// Pivot1とPivot2は同じPivotCacheを共有しているため、この単一の呼び出しで
// 更新されたソースから両方のピボットテーブル（データ + スタイル）を更新する。
pivotTable1.refreshData();

// ワークブックを保存する
workbook.save("output.xlsx");
```

### ビュー/レイアウトのみが変更された場合 — `calculateData()` を使用する

ソースデータが変更されておらず、ピボットテーブルのビューやレイアウト設定のみが変更された場合（たとえば、フィールドが別のエリアに移動された場合や、ファイルを開くときに更新する設定が切り替えられた場合など）、データソースへラウンドトリップする必要はありません。キャッシュにはすでに正しいデータが保持されており、レンダリングされた `PivotTable` のみが再計算を必要とします。この場合、`pivotTable.calculateData()` が正しい選択です。

これにより、不要なソースフェッチが回避され、多くのピボットテーブルが同じキャッシュを共有している場合に大幅に高速になります。

次の例では、ピボットテーブルのソース以外のプロパティを変更し、その後 `calculateData()` を呼び出して既存のキャッシュから再レンダリングします。

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Fruit / Year / Amount のヘッダー行を書き込み
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 8 つのデータ行を書き込み (2-9 行目、ソース範囲 A1:C9 に適合)
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

// "Pivot1" という名前のピボットテーブルを追加し、配置先はセル E3、ソースは A1:C9
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// フィールドを割り当て: Fruit を行、Year を列、Amount をデータへ
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// 表示/レイアウトプロパティを変更 -- これは表示のみの変更で、
// PivotCache.Refresh() を通じてソースデータを再読み込みする必要はない。
pivotTable.setRefreshDataOnOpeningFile(false);

// calculateData() は PivotCache に保持されているデータから、このピボットテーブルの表示 (データ + スタイル) を再レンダリングする。
// ソースデータは変更されていないため、ソースへのラウンドトリップは行われず -- キャッシュされた値のみが
// ワークシートセルに再計算される。
pivotTable.calculateData();

// ワークブックをディスクに保存
workbook.save("output.xlsx");
```

## 同じ PivotCache を共有するすべてのピボットテーブルを取得する

ワークブックには、1 つの共有キャッシュの上に存在する多くのピボットテーブルが含まれていることがよくあります。それらを列挙するには（たとえば、バッチ更新を実行する前や、共有キャッシュの影響を診断するために）、`PivotCache.getPivotTables()` を使用します。このメソッドは、指定されたキャッシュに依存するすべての `PivotTable` のコレクションを返します。

これは、2 つのピボットテーブルが実際に同じ `PivotCache` インスタンスを共有していることを確認する最も直接的な方法でもあります。キャッシュ参照を（`==` 演算子を使用して）比較するか、`getPivotTables()` が返したコレクションを反復処理してどのピボットテーブルが含まれているかを観察することができます。

次の例では、同じソース範囲上に 2 つのピボットテーブルを作成し、それらが同じキャッシュインスタンスを共有していることを確認し、その後、キャッシュのピボットテーブルを列挙します。

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Sheet1");

worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

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
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);

int pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.getPivotTables().get(pivot1Index);
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount");

int pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount");

boolean sameCache = pivotTable1.getPivotCache() == pivotTable2.getPivotCache();
System.out.println("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

PivotTable[] sharedPivotTables = pivotTable1.getPivotCache().getPivotTables();
System.out.println("Number of pivot tables sharing the cache: " + sharedPivotTables.length);

for (PivotTable pt : sharedPivotTables)
{
    System.out.println("Pivot table name: " + pt.getName());
}

workbook.save("output.xlsx");
```

## 非推奨の `PivotTable.refreshData()` からの移行

Aspose.Cells for Aspose.Cells for Java v26.7 より前では、ピボットテーブルを更新する標準的な方法は、各ピボットテーブルに対して個別に `PivotTable.refreshData()` を呼び出すことでした。v26.7 以降、このメソッドは **非推奨** とされ、上記で説明したキャッシュを認識する API に置き換える必要があります。

実際のワークブックでは、テーブルごとの `refreshData()` アプローチに問題がある理由は 2 つあります。

- ソースが変更されていない場合でも、呼び出すたびにソースからデータを再取得します。
- 各呼び出しは共有キャッシュ全体を更新します。多くのピボットテーブルが 1 つのキャッシュを共有している場合、ピボットテーブルごとに `refreshData()` を繰り返し呼び出すと、同じキャッシュが何度も再取得されることになり、非常に遅くなります。

推奨される代替手段は次のとおりです。

- **ワークブック内のすべてのピボットテーブルを更新する** → `workbook.refreshAll();` を使用する
- **一部のピボットテーブルを更新する** → 1 つのキャッシュに対して `pivotTable.getPivotCache().refresh();` を使用する。キャッシュは共有されているため、この 1 回の呼び出しでそのキャッシュ上に構築されたすべてのピボットテーブルが更新されます。すでに更新済みのキャッシュ上に存在する他のピボットテーブルは、安全にスキップできます。
- **ピボットビュー/レイアウトのみが変更された場合** → ソースへのラウンドトリップなしで既存のキャッシュから再レンダリングするために `pivotTable.calculateData();` を使用する。

次の例では、単一のキャッシュを共有する複数のピボットテーブルを持つワークブックに対する新しい効率的なパターンを示します。

```java
import com.aspose.cells.*;
import com.aspose.cells.pivot.*;

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);

// --- ソースデータの作成: Fruit / Year / Amount（ヘッダー + 9行）---
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000);
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500);
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500);
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000);
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800);
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200);
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700);

// --- 最初のピボットテーブル（Pivot1）を配置先セル E3 に追加 ---
int idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount");

// --- 同じソース範囲に2番目のピボットテーブル（Pivot2）を追加 ---
int idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount");

// --- ソースデータの複数の Amount 値を変更 ---
sheet.getCells().get("C2").putValue(5000);   // Grape  2020
sheet.getCells().get("C5").putValue(7500);   // Cherry 2020
sheet.getCells().get("C9").putValue(9500);   // Cherry 2021

// --- 新しい v26.7+ のパターン: キャッシュを1回更新し、必要に応じて再レンダリング ---
pivotTable1.getPivotCache().refresh();

// ソースに影響を与えずに2番目のピボットテーブルのビュー/レイアウトを再レンダリング
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## どの更新 API を使用すべきか？

次の表は、利用可能な更新 API とそれぞれをいつ選択すべきかをまとめたものです。

| 目的 | 推奨 API | メモ |
|------|-----------------|-------|
| ワークブック内のすべてを更新する | `Workbook.refreshAll()` | 1 回の呼び出しで、すべてのキャッシュとテーブルを対象とします。 |
| 単一シート上のピボットテーブルだけを更新する | `Worksheet.refreshPivotTables()` | 1 つのワークシートを対象とします。 |
| 1 つのキャッシュのソースデータが変更された | `pivotTable.getPivotCache().refresh()` | その共有キャッシュ上のすべてのピボットテーブルを更新します。 |
| ビュー/レイアウト設定のみが変更された | `pivotTable.calculateData()` | 不要なソースへのラウンドトリップをスキップします。 |
| 共有キャッシュ上のすべてのピボットテーブルを一覧表示する | `pivotCache.getPivotTables()` | 一括更新の前に列挙するために使用します。 |

実際には、非推奨のテーブルごとの `refreshData()` よりもキャッシュベースの API を優先してください。これらは共有キャッシュを認識しており、冗長なソースフェッチを回避し、更新要件を満たす最小のスコープを選択できるようにします。

## 関連記事

- [セルへの画像の挿入](/cells/ja/java/inserting-an-image-into-a-cell/)
- [DBF ファイルの読み取りと書き込み](/cells/ja/java/dbf/)
- [Excel ファイルの複数ファイルへの分割](/cells/ja/java/splitting-excel-files-into-multiple-files/)
- [Aspose.Cells for Aspose.Cells for Java でのスパークライン](/cells/ja/java/sparkline/)

{{< app/cells/assistant language="java" >}}