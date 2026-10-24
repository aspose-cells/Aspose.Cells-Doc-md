---
title: Aspose.Cells for C++ でピボットテーブルとピボットキャッシュを更新
linktitle: Aspose.Cells for C++ でピボットテーブルとピボットキャッシュを更新
description: Aspose.Cells for C++ の v26.7 以降のピボット更新 API を使用して、ピボットテーブルを更新する方法を学びます。この文書では、RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData、および GetPivotTables について、具体的なコード例を示しながら説明します。
keywords: Aspose.Cells, C++, ピボットテーブル, 更新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ja/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ワークブック全体から単一のピボットテーブルまで、4 つの異なるスコープでピボットデータを再読み込みできる階層的な更新 API を提供します。**Aspose.Cells for C++ v26.7** から、旧来のメソッド `PivotTable.RefreshData()` は非推奨として指定され、この文書で説明する、より効率的でキャッシュを考慮した API に置き換える必要があります。
{{% /alert %}}

## Introduction
ピボットテーブルの更新が、単一の操作になることはほとんどありません。内部では、Aspose.Cells は、元のソースデータとワークシート上に表示されるレンダリング済みの値をつなぐ、階層的なデータチェーンを維持しています。このチェーンを理解することが、状況に応じて適切な更新 API を選択するための鍵になります。
4 層のデータチェーンは次のとおりです。
1. **データソース** — 生データが格納されている元のワークシート範囲、データベースクエリ、または統合範囲です。
2. **`PivotCache`** — ソースデータのメモリ内スナップショットです。すべてのピボットテーブルは `PivotCache` の上に構築され、すべてのデータの収集と集計はこのレベルで行われます。
3. **`PivotTable`** — 行、列、値、およびフィルター項目を定義する表示オブジェクトです。`PivotTable` はデータソースから直接読み込むことはなく、所属する `PivotCache` からのみ読み込みます。
4. **`Cells`** — `PivotTable` が計算された値と書式をレンダリングする先のワークシート `Cells` コレクションです。

{{% alert color="primary" %}}
`PivotCache.SourceType`（列挙型 `PivotTableSourceType`）は、キャッシュデータの取得元を示します。v26.7 の時点では、`PivotCache.Refresh()` がサポートしているのは **`Sheet`** と **`Consolidation`** のソースタイプ、つまりワークシート範囲にあるデータのみです。外部ソース（データベース、外部接続など）は、キャッシュ API を介してはまだ更新できません。
このチェーンにより、Aspose.Cells には 2 つの基本的な更新経路があります。
- **`PivotTable.CalculateData()`** — データソースへの往復処理なしに、キャッシュ済みのデータから 1 つの `PivotTable` の表示を再計算します。
本項のすべてのシナリオではワークシートのセルをソースデータとして使用するため、ソースタイプは `Sheet` であり、更新操作は上記のとおりに動作します。
{{% /alert %}}

## Quick Start
ワークブック内のすべてのピボットテーブルを更新するための最小限のコードだけが必要な場合は、1 回の呼び出しで十分です。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();
    Workbook workbook(u"input.xlsx");
    workbook.RefreshAll();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

以下では、より対象範囲を限定した API を選択する必要がある場面を説明します。

## Required Include Directives
本項のすべての C++ の例は、ピボット関連の型が `Aspose::Cells::Pivot` namespace にあるため、次のヘッダー include および namespace ディレクティブで始まります。
- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`

## Refresh All Pivot Tables in the Workbook
ワークブック内のすべてのピボットキャッシュとピボットテーブルが最新のソースデータを反映するようにする必要がある場合、最もシンプルで包括的な API は `Workbook.RefreshAll()` です。1 回の呼び出しでワークブック全体を処理し、各 `PivotCache` をソースから更新してから、依存するすべての `PivotTable` を再計算します。パフォーマンスを懸念しない場合の、一般的なワークブック全体の更新に推奨されるアプローチです。
次の例では、Fruit/Year/Amount をソース範囲としてワークブックを作成し、1 つのピボットテーブルを作成します。一部のソース値を変更した後、`RefreshAll()` を 1 回呼び出すことで、すべてを最新の状態に更新します。

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

## Refresh All Pivot Tables on a Single Worksheet
特定のワークシート上にあるピボットテーブルのみを更新する必要がある場合があります。たとえば、他のワークシート上のピボットテーブルは関連しておらず、更新してはいけないと分かっている場合です。この場合、Aspose.Cells は 1 つの `Worksheet` インスタンスに限定される `Worksheet.RefreshPivotTables()` を提供します。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
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

## Refresh a Single Pivot Table
単一のピボットテーブルをきめ細かに制御する場合、キャッシュベースの API には 2 つの選択肢があります。どちらを選ぶかは、基礎となるソースデータが変更されたのか、それともピボットテーブル自体の表示やレイアウトの設定だけが変更されたのかによって異なります。

### Source Data Changed — Use `PivotCache.Refresh()`
基礎となるソースデータが変更された場合、適切なエントリーポイントは `pivotTable.GetPivotCache().Refresh()` です。この呼び出しは、ソースデータをキャッシュに再読み込みし、そのキャッシュに依存するすべての `PivotTable` を再計算します。

### Only View/Layout Changed — Use `CalculateData()`
ソースデータは変更されておらず、ピボットテーブルの表示またはレイアウトの設定だけが変更されている場合（フィールドを別の領域に移動した場合や、開いたときに更新する設定を切り替えた場合など）、データソースへの往復処理は必要ありません。キャッシュには既に正しいデータが格納されているため、レンダリングされた `PivotTable` を再計算するだけで十分です。この場合、`pivotTable.CalculateData()` が適切です。
次の例では、ピボットテーブルのソースではないプロパティを変更した後、`CalculateData()` を呼び出して、既存のキャッシュから再レンダリングします。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Write Fruit / Year / Amount header row
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");
    // Write 8 data rows (rows 2-9, fitting the source range A1:C9)
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
    // Add a pivot table named "Pivot1" placed at destination cell E3, sourcing from A1:C9
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    // Assign fields: Fruit to Row, Year to Column, Amount to Data
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // Modify a view/layout property — this is a presentation-only change,
    // so it does NOT require re-reading the source data through PivotCache.Refresh().
    pivotTable.SetRefreshDataOnOpeningFile(false);
    // CalculateData() re-renders THIS pivot table's display (data + style) from the
    // data already held in the PivotCache. Because the source data did not change,
    // no round-trip to the source is performed — only the cached values are recalculated
    // into worksheet cells.
    pivotTable.CalculateData();
    // Save the workbook to disk
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

1 つの共有キャッシュに基づいて構築されたピボットテーブルが、1 つのワークブックに多く含まれていることがよくあります。一括更新の前に列挙する場合や、共有キャッシュの影響を診断する場合にこれらのテーブルを列挙するには、`PivotCache.GetPivotTables()` を使用します。このメソッドは、指定されたキャッシュに依存するすべての `PivotTable` のコレクションを返します。

## Migrating from the Obsolete `PivotTable.RefreshData()`
Aspose.Cells for C++ v26.7 より前は、ピボットテーブルを更新する標準的な方法は、各ピボットテーブルで `PivotTable.RefreshData()` を呼び出すことでした。v26.7 では、このメソッドは**非推奨**として指定され、上記のキャッシュを考慮した API に置き換える必要があります。
実際のワークブックで、テーブルごとの `RefreshData()` の使用が問題となる理由が 2 つあります。
- ソースが変更されていない場合でも、呼び出す*たびに*ソースからデータを再取得します。
推奨される置き換え方法は次のとおりです。
次の例では、1 つのキャッシュを共有する複数のピボットテーブルを含むワークブックで、新しい効率的なパターンを示します。

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

## Which Refresh API Should I Use?
以下の表に、利用可能な更新 API と、それぞれの選択基準をまとめます。
| 目的 | 推奨 API | 注記 |
|------|-----------------|-------|
| ワークブック内のすべてを更新する | `Workbook.RefreshAll()` | 1 回の呼び出しで、すべてのキャッシュとテーブルを処理します。 |
| 1 つのシート上にあるピボットテーブルのみを更新する | `Worksheet.RefreshPivotTables()` | 1 つのワークシートに限定されます。 |
| 1 つのキャッシュのソースデータが変更された | `pivotTable.GetPivotCache().Refresh()` | その共有キャッシュ上のすべてのピボットテーブルを更新します。 |
| 表示またはレイアウトの設定だけが変更された | `pivotTable.CalculateData()` | 不要なソースへの往復処理を省略します。 |
| 共有キャッシュ上のすべてのピボットテーブルを一覧表示する | `pivotCache.GetPivotTables()` | 一括更新の前に列挙するために使用します。 |
実際の運用では、非推奨のテーブルごとの `RefreshData()` よりも、キャッシュベースの API を使用してください。これらの API は共有キャッシュを認識し、冗長なソース取得を回避し、更新要件を満たす最小のスコープを選択できます。

## Common Pitfalls
- **保存前に更新することを忘れる。** ピボットテーブルは、データチェーンが更新された場合にのみ、レンダリング済みの値をワークシートに書き込みます。ソースセルを変更した場合は、`Workbook.Save()` の前に `PivotCache.Refresh()`（または `Workbook.RefreshAll()`）を呼び出してください。そうでない場合、保存されたファイルには古い集計値が残ります。
- **非推奨の `RefreshData()` をテーブルごとに呼び出す。** v26.7 では、`PivotTable.RefreshData()` は非推奨であり、呼び出しごとにソースを取得し直します。複数のピボットテーブルが 1 つのキャッシュを共有している場合、これでは N 回の冗長なソース取得が発生します。1 回の `PivotCache.Refresh()` に置き換え、テーブルごとに `CalculateData()` を呼び出してください。
- **レイアウトだけを変更した仍然是更新してしまう。** ソースデータに触れずにピボットテーブルの表示（列の順序、`ConsolidationFunction` など）だけを変更した場合、`PivotCache.Refresh()` は不要で低速です。`pivotTable.CalculateData()` を呼び出して、既存のキャッシュから再レンダリングしてください。
- **外部ソースは `PivotCache.Refresh()` でサポートされていない。** ピボットテーブルのソースが外部接続（データベース、OLAPキューブなど）からの場合、v26.7 では `PivotCache.Refresh()` で更新できません。現在サポートされているのは `Sheet` と `Consolidation` のソースタイプのみです。外部ソースの場合は、ワークブックを開き直すか、ソースからキャッシュを再構築してください。

{{< app/cells/assistant language="cpp" >}}