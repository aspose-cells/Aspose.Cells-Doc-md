---
title: Aspose.Cells for C++ でのピボットテーブルとピボットキャッシュの更新
linktitle: Aspose.Cells for C++ でのピボットテーブルとピボットキャッシュの更新
description: Aspose.Cells for C++ の v26.7+ ピボット更新 API を使用してピボットテーブルを更新する方法を学習します。この記事では、RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData、GetPivotTables を実際のコード例とともに解説します。
keywords: Aspose.Cells, C++, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ja/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ワークブック全体から単一のピボットテーブルまで、4つの異なるスコープでピボットデータを再読み込みできる階層型更新 API を提供します。**Aspose.Cells for C++ v26.7** 以降、従来のメソッド `PivotTable.RefreshData()` は非推奨となり、この記事で説明するより効率的なキャッシュ対応 API に置き換える必要があります。
{{% /alert %}}

## 概要
ピボットテーブルの更新は、単一の操作であることはほとんどありません。内部では、Aspose.Cells は元のソースデータからワークシートに表示されるレンダリング値までを接続する階層型データチェーンを維持しています。このチェーンを理解することが、あらゆる状況に適した更新 API を選択する鍵となります。
4層データチェーンは次のとおりです:
1. **データソース** — 生の値が存在する元のワークシート範囲、データベースクエリ、または統合範囲。
2. **PivotCache** — ソースデータのメモリ内スナップショット。すべてのピボットテーブルは `PivotCache` の上に構築されます。ここで、すべてのデータが収集および集計されます。
3. **PivotTable** — 行、列、値、フィルタのフィールドを定義するビューオブジェクト。`PivotTable` は自身の `PivotCache` からのみデータを読み取り、データソースから直接読み取ることはありません。
4. **Cells** — `PivotTable` が計算された値とスタイルをレンダリングする先の、ワークシートの `Cells`。

{{% alert color="primary" %}}
`PivotCache.SourceType`(列挙型 `PivotTableSourceType`)は、キャッシュデータの取得元を示します。v26.7 現在、`PivotCache.Refresh()` は **`Sheet`** および **`Consolidation`** のソースタイプのみをサポートしています。つまり、ワークシート範囲に存在するデータのみが対象です。外部ソース(データベース、外部接続など)は、キャッシュ API ではまだ更新できません。
{{% /alert %}}

このチェーンのため、Aspose.Cells には 2つの基本的な更新パスがあります:
- **`PivotTable.CalculateData()`** — すでにキャッシュされたデータから 1つの `PivotTable` の表示を再計算し、データソースへのラウンドトリップは行いません。
この記事のすべてのシナリオではワークシートセルをソースデータとして使用しているため、ソースタイプは `Sheet` であり、更新操作は前述のとおりに動作します。

## クイックスタート
ワークブック内のすべてのピボットを更新する最小限のコードが必要な場合は、1回の呼び出しで十分です:

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));
    cells.Get(u"A2").PutValue(U16String("grape"));
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(50);
    cells.Get(u"A3").PutValue(U16String("blueberry"));
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(60);
    cells.Get(u"A4").PutValue(U16String("kiwi"));
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(70);
    cells.Get(u"A5").PutValue(U16String("cherry"));
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(80);
    cells.Get(u"A6").PutValue(U16String("grape"));
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(90);
    cells.Get(u"A7").PutValue(U16String("blueberry"));
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(100);
    cells.Get(u"A8").PutValue(U16String("kiwi"));
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(110);
    cells.Get(u"A9").PutValue(U16String("cherry"));
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(120);
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    cells.Get(u"C2").PutValue(55);
    cells.Get(u"C5").PutValue(85);
    cells.Get(u"C9").PutValue(125);
    pivotTable.CalculateData();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

この記事の以降の部分では、より限定的な API を選択すべき場面について説明します。

## 必要なインクルードディレクティブ
この記事のすべての C++ のサンプルコードは、ピボット型が `Aspose::Cells::Pivot` 名前空間に存在するため、次のヘッダーインクルードと名前空間ディレクティブから始まります:
- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`

## ワークブック内のすべてのピボットテーブルを更新
ワークブック内のすべてのピボットキャッシュとすべてのピボットテーブルが最新のソースデータを反映するようにする必要がある場合、最もシンプルで包括的な API は `Workbook.RefreshAll()` です。1回の呼び出しでワークブック全体を走査し、各 `PivotCache` をソースから更新し、それに依存するすべての `PivotTable` を再計算します。これは、パフォーマンスが問題にならない一般的なドキュメント全体の更新に対して推奨されるアプローチです。
次の例では、Fruit/Year/Amount のソース範囲を持つワークブックを作成し、1つのピボットテーブルを作成して一部のソース値を変更し、`RefreshAll()` を使用してすべてを 1回の呼び出しで最新の状態に更新します。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");
    worksheet.GetCells().Get(u"A2").PutValue(u"grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(u"blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2021);
    worksheet.GetCells().Get(u"C3").PutValue(150);
    worksheet.GetCells().Get(u"A4").PutValue(u"kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(200);
    worksheet.GetCells().Get(u"A5").PutValue(u"cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2021);
    worksheet.GetCells().Get(u"C5").PutValue(120);
    worksheet.GetCells().Get(u"A6").PutValue(u"grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(180);
    worksheet.GetCells().Get(u"A7").PutValue(u"blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2020);
    worksheet.GetCells().Get(u"C7").PutValue(130);
    worksheet.GetCells().Get(u"A8").PutValue(u"kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(220);
    worksheet.GetCells().Get(u"A9").PutValue(u"cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2020);
    worksheet.GetCells().Get(u"C9").PutValue(140);
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    worksheet.GetCells().Get(u"C2").PutValue(300);
    worksheet.GetCells().Get(u"C5").PutValue(250);
    worksheet.GetCells().Get(u"C9").PutValue(400);
    worksheet.RefreshPivotTables();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## 単一のワークシート上のすべてのピボットテーブルを更新
特定のワークシート上にあるピボットテーブルのみを更新する必要がある場合があります。例えば、他のワークシート上のピボットテーブルが関連していないことがわかっており、触れたくない場合です。このような場合、Aspose.Cells は `Worksheet.RefreshPivotTables()` を提供しており、単一の `Worksheet` インスタンスを対象とします。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Fruit / Year / Amount のヘッダー行を書き込む
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");
    // 8 件のデータ行を書き込む (2～9 行目、元データ範囲 A1:C9 に収まる)
    worksheet.GetCells().Get(u"A2").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2020);
    worksheet.GetCells().Get(u"C3").PutValue(200);
    worksheet.GetCells().Get(u"A4").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(300);
    worksheet.GetCells().Get(u"A5").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2020);
    worksheet.GetCells().Get(u"C5").PutValue(400);
    worksheet.GetCells().Get(u"A6").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(150);
    worksheet.GetCells().Get(u"A7").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2021);
    worksheet.GetCells().Get(u"C7").PutValue(250);
    worksheet.GetCells().Get(u"A8").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(350);
    worksheet.GetCells().Get(u"A9").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2021);
    worksheet.GetCells().Get(u"C9").PutValue(450);
    // 配置先セル E3 に「Pivot1」という名前のピボットテーブルを追加し、データソースを A1:C9 とする
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    // フィールドを割り当てる: 行に Fruit、列に Year、データに Amount
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // 表示/レイアウトのプロパティを変更する — これは表示のみの変更なので、
    // PivotCache.Refresh() を介してソースデータを再読み込みする必要はない
    pivotTable.SetRefreshDataOnOpeningFile(false);
    // CalculateData() は、保持されているデータを基に、このピボットテーブルの表示
    // (データとスタイル) を再描画する。ソースデータが変更されていないため、
    // ソースへのラウンドトリップは行われず、キャッシュされた値のみが
    // ワークシートのセルに再計算される
    pivotTable.CalculateData();
    // ワークブックをディスクに保存する
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## 単一のピボットテーブルを更新
単一のピボットテーブルに対してきめ細かい制御が必要な場合、キャッシュベースの API には 2つのオプションがあります。どちらを選択するかは、実際に何が変更されたかによって異なります。基になるソースデータが変更されたのか、それともピボットテーブル自体のビュー/レイアウト設定のみが変更されたのかです。

### ソースデータが変更された場合 — `PivotCache.Refresh()` を使用
基になるソースデータが変更された場合、正しいエントリポイントは `pivotTable.GetPivotCache().Refresh()` です。この呼び出しはソースデータをキャッシュに再読み込みし、そのキャッシュに依存するすべての `PivotTable` を再計算します。

### ビュー/レイアウトのみが変更された場合 — `CalculateData()` を使用
ソースデータは変更されておらず、ピボットテーブルのビューまたはレイアウト設定のみが変更されている場合(例えば、フィールドが別のエリアに移動されたり、開くときに更新する設定が切り替えられたりした場合)、データソースへのラウンドトリップは必要ありません。キャッシュにはすでに正しいデータが保持されています。再計算する必要があるのは、レンダリングされた `PivotTable` のみです。この場合、`pivotTable.CalculateData()` が適切な選択です。
次の例では、ピボットテーブルのソース以外のプロパティを変更し、その後 `CalculateData()` を呼び出して既存のキャッシュから再レンダリングします。
ワークブックには、多くの場合、1つの共有キャッシュ上に存在する多くのピボットテーブルが含まれています。これらを列挙するには、例えばバッチ更新を実行する前や、共有キャッシュの影響を診断する場合、`PivotCache.GetPivotTables()` を使用します。このメソッドは、指定されたキャッシュに依存するすべての `PivotTable` のコレクションを返します。

## 非推奨の `PivotTable.RefreshData()` からの移行
Aspose.Cells for C++ v26.7 より前では、ピボットテーブルを更新する標準的な方法は、各ピボットテーブルに対して個別に `PivotTable.RefreshData()` を呼び出すことでした。v26.7 以降、このメソッドは **非推奨** とされ、上記のキャッシュ対応 API に置き換える必要があります。
実際のワークブックでは、テーブルごとの `RefreshData()` アプローチに問題がある理由は 2つあります:
- ソースが変更されていない場合でも、呼び出されるたびにソースからデータを再取得します。
推奨される代替手段は次のとおりです:
次の例では、単一のキャッシュを共有する複数のピボットテーブルを持つワークブックに対する新しい効率的なパターンを示します。

## どの更新 API を使用すべきか
次の表は、利用可能な更新 API とそれぞれを選択するタイミングをまとめたものです。
| 目標 | 推奨 API | メモ |
|------|-----------------|-------|
| ワークブック内のすべてを更新 | `Workbook.RefreshAll()` | 1回の呼び出しで、すべてのキャッシュとテーブルをカバー。 |
| 単一シート上のピボットテーブルのみを更新 | `Worksheet.RefreshPivotTables()` | 1つのワークシートを対象。 |
| 1つのキャッシュのソースデータが変更された | `pivotTable.GetPivotCache().Refresh()` | 共有キャッシュ上のすべてのピボットテーブルを更新。 |
| ビュー/レイアウト設定のみが変更された | `pivotTable.CalculateData()` | 不要なソースへのラウンドトリップをスキップ。 |
| 共有キャッシュ上のすべてのピボットテーブルを一覧表示 | `pivotCache.GetPivotTables()` | 一括更新の前に列挙するために使用。 |
実際には、非推奨のテーブルごとの `RefreshData()` よりも、キャッシュベースの API を優先してください。これらは共有キャッシュを認識し、不要なソース取得を避け、更新要件を満たす最小のスコープを選択できるようにします。

## 一般的な落とし穴
- **保存前に更新するのを忘れる。** ピボットテーブルは、データチェーンが更新されたときにのみ、レンダリングされた値をワークシートに書き込みます。ソースセルを変更した場合は、`Workbook.Save()` の前に `PivotCache.Refresh()`(または `Workbook.RefreshAll()`)を呼び出さないと、保存されたファイルには古い集計値が残ったままになります。
- **テーブルごとに非推奨の `RefreshData()` を呼び出す。** v26.7 では、`PivotTable.RefreshData()` は非推奨とされており、呼び出しごとにソースを再取得します。複数のピボットテーブルがキャッシュを共有している場合、N 回の冗長なソース取得が発生します。1回の `PivotCache.Refresh()` と、その後のテーブルごとの `CalculateData()` に置き換えてください。
- **レイアウトのみが変更された場合に更新する。** ソースデータを変更せずにピボットテーブルのビュー(列順、`ConsolidationFunction` など)のみを変更した場合、`PivotCache.Refresh()` は不要であり、処理が遅くなります。`pivotTable.CalculateData()` を呼び出して、既存のキャッシュから再レンダリングしてください。
- **外部ソースは `PivotCache.Refresh()` でサポートされていない。** ピボットテーブルのソースが外部接続(データベース、OLAP キューブなど)からのものである場合、v26.7 では `PivotCache.Refresh()` では更新できません。現在のところ、`Sheet` と `Consolidation` のソースタイプのみをサポートしています。外部ソースの場合は、ワークブックを再度開くか、ソースからキャッシュを再構築してください。

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    sheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    sheet.GetCells().Get(u"B1").PutValue(u"Year");
    sheet.GetCells().Get(u"C1").PutValue(u"Amount");
    sheet.GetCells().Get(u"A2").PutValue(u"Grape");      sheet.GetCells().Get(u"B2").PutValue(2020); sheet.GetCells().Get(u"C2").PutValue(1000);
    sheet.GetCells().Get(u"A3").PutValue(u"Blueberry");  sheet.GetCells().Get(u"B3").PutValue(2020); sheet.GetCells().Get(u"C3").PutValue(2000);
    sheet.GetCells().Get(u"A4").PutValue(u"Kiwi");       sheet.GetCells().Get(u"B4").PutValue(2020); sheet.GetCells().Get(u"C4").PutValue(1500);
    sheet.GetCells().Get(u"A5").PutValue(u"Cherry");     sheet.GetCells().Get(u"B5").PutValue(2020); sheet.GetCells().Get(u"C5").PutValue(2500);
    sheet.GetCells().Get(u"A6").PutValue(u"Grape");      sheet.GetCells().Get(u"B6").PutValue(2021); sheet.GetCells().Get(u"C6").PutValue(3000);
    sheet.GetCells().Get(u"A7").PutValue(u"Blueberry");  sheet.GetCells().Get(u"B7").PutValue(2021); sheet.GetCells().Get(u"C7").PutValue(1800);
    sheet.GetCells().Get(u"A8").PutValue(u"Kiwi");       sheet.GetCells().Get(u"B8").PutValue(2021); sheet.GetCells().Get(u"C8").PutValue(2200);
    sheet.GetCells().Get(u"A9").PutValue(u"Cherry");     sheet.GetCells().Get(u"B9").PutValue(2021); sheet.GetCells().Get(u"C9").PutValue(2700);
    int idx1 = sheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = sheet.GetPivotTables().Get(idx1);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");
    int idx2 = sheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = sheet.GetPivotTables().Get(idx2);
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");
    sheet.GetCells().Get(u"C2").PutValue(5000);
    sheet.GetCells().Get(u"C5").PutValue(7500);
    sheet.GetCells().Get(u"C9").PutValue(9500);
    pivotTable2.CalculateData();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{< app/cells/assistant language="cpp" >}}