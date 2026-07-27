---
title: Aspose.Cells for Java でのピボットテーブルの更新
linktitle: Aspose.Cells for Java でのピボットテーブルの更新
description: v26.7+ のピボット更新 API を使用して Aspose.Cells for Java でピボットテーブルを更新する方法を学びます。この記事では、RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData、GetPivotTables について実際のコード例とともに解説します。
keywords: Aspose.Cells, Java, ピボットテーブル, 更新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ja/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ワークブック全体から単一のピボットテーブルまで、4 つの異なるスコープでピボットデータを再読み込みできる階層的な更新 API を提供します。**Aspose.Cells for Java v26.7** 以降、旧来のメソッド `PivotTable.refreshData()` は非推奨となり、この記事で説明されているより効率的でキャッシュ対応の API に置き換える必要があります。
{{% /alert %}}
## はじめに
ピボットテーブルの更新は、単一の操作であることはほとんどありません。舞台裏では、Aspose.Cells は元のソースデータからワークシートに表示されるレンダリングされた値までを接続する階層的なデータチェーンを維持しています。このチェーンを理解することが、あらゆる状況に対して適切な更新 API を選択する鍵となります。
4 層のデータチェーンは次のとおりです。
1. **データソース** — 生の値が格納されている元のワークシート範囲、データベースクエリ、または統合範囲。
2. **PivotCache** — ソースデータのインメモリスナップショット。すべてのピボットテーブルは `PivotCache` の上に構築されます。すべてのデータが集約されるのはこの場所です。
3. **PivotTable** — 行、列、値、フィルタのフィールドを定義するビューオブジェクト。`PivotTable` はデータソースから直接ではなく、`PivotCache` からのみ読み取ります。
4. **Cells** — `PivotTable` が計算された値とスタイルを描画する先のワークシート `Cells`。
特に重要な概念は **共有キャッシュ** です。ワークブック内の複数のピボットテーブルが同じソース範囲を参照する場合、それらは *1 つの* `PivotCache` インスタンスを共有します。1 つの `PivotCache` は多くのピボットテーブルから参照でき、そのキャッシュを更新すると、依存しているすべての `PivotTable` が一度に更新されます。
{{% alert color="primary" %}}
`PivotCache.getSourceType()` (列挙型 `PivotTableSourceType`) は、キャッシュデータの取得元を示します。v26.7 以降、`PivotCache.refresh()` は **`Sheet`** および **`Consolidation`** のソースタイプ、つまりワークシート範囲に存在するデータのみをサポートします。外部ソース（データベースや外部接続など）は、キャッシュ API を通じてはまだ更新できません。
{{% /alert %}}
このチェーンのため、Aspose.Cells には 2 つの基本的な更新パスがあります。
- **`PivotCache.refresh()`** — ソース → キャッシュを再読み込みし、依存しているすべての `PivotTable` を単一の操作で再計算します。
- **`PivotTable.calculateData()`** — すでにキャッシュされているデータから、1 つの `PivotTable` の表示を再計算します。データソースへのラウンドトリップは行いません。
この記事のすべてのシナリオではワークシートセルをソースデータとして使用しているため、ソースタイプは `Sheet` であり、更新操作は説明どおりに動作します。
## 必要な import 文
この記事のすべての Java サンプルは、ピボットタイプが `com.aspose.cells.pivot` パッケージに含まれているため、次の import 文から始まります。
## ワークブック内のすべてのピボットテーブルを更新する
ワークブック内のすべてのピボットキャッシュとすべてのピボットテーブルが最新のソースデータを反映するようにする必要がある場合、最もシンプルで包括的な API は `Workbook.refreshAll()` です。1 回の呼び出しでワークブック全体を走査し、各 `PivotCache` をソースから更新し、依存しているすべての `PivotTable` を再計算します。これは、パフォーマンスが重要でない一般的なドキュメント全体の更新に対して推奨されるアプローチです。
次の例では、Fruit/Year/Amount のソース範囲を含むワークブックを作成し、1 つのピボットテーブルを作成し、ソース値の一部を変更してから、`refreshAll()` を使用してすべてを 1 回の呼び出しで最新にします。
```java
import com.aspose.cells.*;

// 新しいワークブックを作成
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// セルA1:C1にヘッダー行を書き込み
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// セルA2:C9にデータ行を書き込み（2020年と2021年にわたる8行の果物データ）
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

// ピボットテーブルを追加：ソース範囲"A1:C9"、配置先セル"E3"、名前"Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// ピボットフィールドを割り当て：Fruitを行、Yearを列、Amountをデータに
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// 変更をシミュレートするため、ソースデータの複数のAmount値を変更
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// ワークブック内のすべてのピボットテーブル/ピボットキャッシュを更新
workbook.refreshAll();

// ワークブックを保存
workbook.save("output.xlsx");
```
## 単一のワークシート上のすべてのピボットテーブルを更新する
特定のワークシート上にあるピボットテーブルのみを更新する必要がある場合があります。たとえば、他のワークシート上にあるピボットテーブルは無関係で、触るべきではないことが分かっている場合などです。このケースのために、Aspose.Cells は単一の `Worksheet` インスタンスを対象とする `Worksheet.refreshPivotTables()` を提供します。
これは `Workbook.refreshAll()` よりも選択的です。対象ワークシート上にあるピボットテーブルのみが更新され、他のワークシート上にあるピボットテーブルはそのまま残されます。
次の例では、同じ Fruit/Year/Amount のソースデータを入力し、最初のワークシートにピボットテーブルを追加し、ソース値の一部を変更してから、そのワークシート上のピボットテーブルのみを更新します。
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
単一のピボットテーブルに対してきめ細かい制御を行いたい場合、キャッシュベースの API には 2 つのオプションがあります。どちらを選択するかは、実際に何が変わったか、つまり基になるソースデータなのか、それともピボットテーブル自体のビュー/レイアウト設定のみなのかによって異なります。
### ソースデータが変更された場合 — `PivotCache.refresh()` を使用する
基になるソースデータが変更された場合、正しいエントリポイントは `pivotTable.getPivotCache().refresh()` です。この呼び出しはソースデータをキャッシュに再読み込みし、そのキャッシュに依存しているすべての `PivotTable` を再計算します。
{{% alert color="primary" %}}
ピボットテーブルは単一の `PivotCache` インスタンスを共有するため、`PivotCache.refresh()` を呼び出すと、参照している 1 つのピボットテーブルだけでなく、**すべて**のピボットテーブルが再計算されます。2 つのピボットテーブルが同じソース範囲を共有している場合、一方のキャッシュを更新すると両方が更新されます。
{{% /alert %}}
次の例では、同じソース範囲上に 2 つのピボットテーブルを作成し、この共有キャッシュの動作を示し、ソース値の一部を変更してから、1 つのキャッシュ参照を通じて更新します。
```java
import com.aspose.cells.*;

// 新しいワークブックを作成し、最初のワークシートにアクセスする
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// ヘッダー行を書き込む: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 約9行のデータ行を書き込む（2020年〜2021年にわたる grape / blueberry / kiwi / cherry）
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

// 最初のピボットテーブル「Pivot1」をセルE3に配置し、ソース範囲をA1:C9として追加する
int pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// Pivot1のフィールドを割り当てる
pivotTable1.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable1.addFieldToArea(PivotFieldType.DATA, "Amount");

// 同じソース範囲A1:C9を使用して、E15に2つ目のピボットテーブル「Pivot2」を追加する
// ソース範囲が同一であるため、Pivot1とPivot2は単一のPivotCacheを共有する。
int pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// Pivot2にも同じフィールドを割り当てる
pivotTable2.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable2.addFieldToArea(PivotFieldType.DATA, "Amount");

// データ変更をシミュレートするため、ソースデータのAmountセルの値をいくつか変更する
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// 共有されているPivotCacheを更新する。
// Pivot1とPivot2は同じPivotCacheを共有しているため、この1回の呼び出しで
// 両方のピボットテーブル（データとスタイル）を更新されたソースから更新する。
pivotTable1.refreshData();

// ワークブックを保存する
workbook.save("output.xlsx");
```
### ビュー/レイアウトのみが変更された場合 — `calculateData()` を使用する
ソースデータは変更されておらず、ピボットテーブルのビューやレイアウト設定のみが変更された場合（たとえば、フィールドが別のエリアに移動された場合や、開くときに更新する設定が切り替えられた場合など）、データソースへのラウンドトリップは必要ありません。キャッシュにはすでに正しいデータが保持されています。更新する必要があるのはレンダリングされた `PivotTable` だけです。この場合、`pivotTable.calculateData()` が正しい選択です。
これにより不要なソースフェッチが回避され、多くのピボットテーブルが同じキャッシュを共有している場合は大幅に高速化されます。
次の例では、ピボットテーブルのソース以外のプロパティを変更し、`calculateData()` を呼び出して既存のキャッシュから再レンダリングします。
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

// "Pivot1" という名前のピボットテーブルを、配置先セル E3 に追加し、ソースは A1:C9
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// フィールドを割り当て: Fruit を行、Year を列、Amount をデータ
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// 表示/レイアウトプロパティの変更 -- 表示のみの変更であるため、
// PivotCache.Refresh() を通じてソースデータを再読み取りする必要はない。
pivotTable.setRefreshDataOnOpeningFile(false);

// calculateData() は、このピボットテーブルの表示 (データ + スタイル) を
// PivotCache に既に保持されているデータから再レンダリングする。ソースデータが変更されていないため、
// ソースへのラウンドトリップは行われない -- キャッシュされた値のみが再計算され
// ワークシートのセルに反映される。
pivotTable.calculateData();

// ワークブックをディスクに保存
workbook.save("output.xlsx");
```
## 同じ PivotCache を共有するすべてのピボットテーブルを取得する
ワークブックには、1 つの共有キャッシュの上にすべてが乗っている多くのピボットテーブルが含まれていることがよくあります。それらを列挙するには（たとえば、一括更新を実行する前や、共有キャッシュの影響を診断するために）、`PivotCache.getPivotTables()` を使用します。このメソッドは、指定されたキャッシュに依存するすべての `PivotTable` のコレクションを返します。
これは、2 つのピボットテーブルが実際に同じ `PivotCache` インスタンスを共有していることを確認する最も直接的な方法でもあります。キャッシュ参照を `==` 演算子を使用して比較するか、`getPivotTables()` によって返されたコレクションを反復処理し、どのピボットテーブルがそれに含まれているかを観察することで確認できます。
次の例では、同じソース範囲上に 2 つのピボットテーブルを作成し、それらが同じキャッシュインスタンスを共有していることを確認してから、キャッシュのピボットテーブルを列挙します。

## 非推奨の `PivotTable.refreshData()` からの移行
Aspose.Cells for Java v26.7 より前は、ピボットテーブルを更新する標準的な方法は、各ピボットテーブルに対して個別に `PivotTable.refreshData()` を呼び出すことでした。v26.7 以降、このメソッドは **非推奨** となり、上記のキャッシュ対応 API に置き換える必要があります。
実際のワークブックでは、テーブルごとの `refreshData()` アプローチに問題がある理由が 2 つあります。
- ソースが変更されていない場合でも、呼び出すたびにソースからデータを再フェッチします。
- 各呼び出しは共有キャッシュ全体を更新します。多くのピボットテーブルが 1 つのキャッシュを共有している場合、ピボットテーブルごとに `refreshData()` を繰り返し呼び出すと、同じキャッシュが何度も再フェッチされるため、非常に遅くなります。
推奨される代替手段は次のとおりです。
- **ワークブック内のすべてのピボットテーブルを更新する** → `workbook.refreshAll();` を使用します。
- **その一部を更新する** → 1 つのキャッシュに対して `pivotTable.getPivotCache().refresh();` を使用します。キャッシュは共有されているため、この 1 回の呼び出しで、そのキャッシュの上に構築されているすべてのピボットテーブルが更新されます。すでに更新済みのキャッシュ上にある他のピボットテーブルは、安全にスキップできます。
- **ピボットビュー/レイアウトのみが変更された** → ソースへのラウンドトリップなしで既存のキャッシュから再レンダリングするには、`pivotTable.calculateData();` を使用します。
次の例では、単一のキャッシュを共有する複数のピボットテーブルを含むワークブックの新しい効率的なパターンを示します。
```java
import com.aspose.cells.*;
import com.aspose.cells.pivot.*;

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);

// --- ソースデータの作成：果物 / 年 / 金額（ヘッダー＋9行） ---
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

// --- 最初のピボットテーブル（Pivot1）をセルE3に追加 ---
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

// --- ソースデータの金額値をいくつか変更 ---
sheet.getCells().get("C2").putValue(5000);   // ブドウ 2020
sheet.getCells().get("C5").putValue(7500);   // さくらんぼ 2020
sheet.getCells().get("C9").putValue(9500);   // さくらんぼ 2021

// --- 新規v26.7+パターン：キャッシュを一度だけリフレッシュし、必要に応じて再レンダリング ---
pivotTable1.getPivotCache().refresh();

// ソースに影響を与えずに2番目のピボットテーブルのビュー/レイアウトを再レンダリング
pivotTable2.calculateData();

workbook.save("output.xlsx");
```
## どの更新 API を使用すべきか?
次の表は、利用可能な更新 API と、それぞれをいつ選択すべきかをまとめたものです。
| 目的 | 推奨 API | メモ |
|------|-----------------|-------|
| ワークブック内のすべてを更新する | `Workbook.refreshAll()` | 1 回の呼び出しで、すべてのキャッシュとテーブルを対象とします。 |
| 単一シート上のピボットテーブルのみを更新する | `Worksheet.refreshPivotTables()` | 1 つのワークシートを対象とします。 |
| 1 つのキャッシュのソースデータが変更された | `pivotTable.getPivotCache().refresh()` | その共有キャッシュ上のすべてのピボットテーブルを更新します。 |
| ビュー/レイアウト設定のみが変更された | `pivotTable.calculateData()` | 不要なソースへのラウンドトリップをスキップします。 |
| 共有キャッシュ上のすべてのピボットテーブルを一覧表示する | `pivotCache.getPivotTables()` | 一括更新の前に列挙するために使用します。 |
実際には、非推奨のテーブルごとの `refreshData()` よりもキャッシュベースの API を優先してください。これらは共有キャッシュを認識し、不要なソースフェッチを回避し、更新要件を満たす最小のスコープを選択できるようにします。

{{< app/cells/assistant language="java" >}}
