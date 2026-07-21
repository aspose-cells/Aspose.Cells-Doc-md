---
title: Aspose.Cells for C++ でのピボットテーブルの更新
linktitle: Aspose.Cells for C++ でのピボットテーブルの更新
description: Aspose.Cells for C++ で v26.7+ のピボット更新 API を使用してピボットテーブルを更新する方法を学びます。この記事では、RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData、GetPivotTables を実用的なコード例とともに解説します。
keywords: Aspose.Cells, C++, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ja/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は、ワークブック全体から単一のピボットテーブルまで、4 つの異なるスコープでピボットデータを再読み込みできる階層型の更新 API を提供します。**Aspose.Cells for C++ v26.7** 以降、従来のメソッド `PivotTable.RefreshData()` は廃止予定となり、この記事で説明するより効率的でキャッシュ対応の API に置き換える必要があります。

{{% /alert %}}

## はじめに

ピボットテーブルの更新は、単一の操作であることはまれです。舞台裏では、Aspose.Cells は元のソースデータとワークシートに表示されるレンダリングされた値を結ぶ階層化されたデータチェーンを維持しています。このチェーンを理解することが、あらゆる状況に対して適切な更新 API を選択する鍵となります。

4 層のデータチェーンは次のとおりです。

1. **データソース** — 生の値が格納されている元のワークシート範囲、データベースクエリ、または統合範囲。
2. **PivotCache** — ソースデータのメモリ内スナップショット。すべてのピボットテーブルは `PivotCache` の上に構築されます。すべてのデータはこの場所で収集および集計されます。
3. **PivotTable** — 行、列、値、フィルタのフィールドを定義するビューオブジェクト。`PivotTable` はデータソースからではなく、`PivotCache` からのみ読み取ります。
4. **Cells** — `PivotTable` が計算された値とスタイルをレンダリングする先のワークシートの `Cells`。

特に重要な概念は **共有キャッシュ** です。ワークブック内の複数のピボットテーブルが同じソース範囲を参照している場合、それらは *1 つの* `PivotCache` インスタンスを共有します。1 つの `PivotCache` は多くのピボットテーブルから参照でき、そのキャッシュを更新すると、依存するすべての `PivotTable` が一度に更新されます。

{{% alert color="primary" %}}

`PivotCache.SourceType`（列挙型 `PivotTableSourceType`）は、キャッシュデータの取得元を示します。v26.7 現在、`PivotCache.Refresh()` は **`Sheet`** と **`Consolidation`** のソースタイプのみをサポートしています。つまり、ワークシート範囲に存在するデータのみです。外部ソース（データベース、外部接続など）は、キャッシュ API を通じてはまだ更新できません。

{{% /alert %}}

このチェーンのため、Aspose.Cells には 2 つの基本的な更新パスがあります。

- **`PivotCache.Refresh()`** — ソースからキャッシュへの再読み込みと、それに依存するすべての `PivotTable` の再計算を単一の操作で行います。
- **`PivotTable.CalculateData()`** — すでにキャッシュされているデータから 1 つの `PivotTable` の表示を再計算します。データソースへのラウンドトリップはありません。

この記事のすべてのシナリオではワークシートセルのソースデータを使用しているため、ソースタイプは `Sheet` であり、更新操作は前述のとおりに動作します。

## 必要なインクルードディレクティブ

この記事のすべての C++ の例では、ピボット型が `Aspose::Cells::Pivot` 名前空間に存在するため、次のヘッダーインクルードと名前空間ディレクティブから始まります。

- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`

## ワークブック内のすべてのピボットテーブルを更新する

ワークブック内のすべてのピボットキャッシュとすべてのピボットテーブルが最新のソースデータを反映するようにする必要がある場合、最もシンプルで包括的な API は `Workbook.RefreshAll()` です。1 回の呼び出しでワークブック全体を走査し、各 `PivotCache` をソースから更新してから、依存するすべての `PivotTable` を再計算します。これは、パフォーマンスが問題にならない一般的なフルドキュメント更新の推奨アプローチです。

次の例では、Fruit/Year/Amount のソース範囲を含むワークブックを作成し、1 つのピボットテーブルを作成し、一部のソース値を変更し、`RefreshAll()` を使用してすべてを 1 回の呼び出しで最新状態にします。

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

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## 単一のワークシート上のすべてのピボットテーブルを更新する

特定のワークシート上にあるピボットテーブルだけを更新する必要がある場合があります。たとえば、他のワークシートのピボットテーブルが関連していないことがわかっており、触れたくない場合です。このケースのために、Aspose.Cells は `Worksheet.RefreshPivotTables()` を提供します。これは単一の `Worksheet` インスタンスにスコープされます。

これは `Workbook.RefreshAll()` よりも選択的です。対象のワークシート上のピボットテーブルのみが更新され、他のワークシートのピボットテーブルはそのまま残されます。

次の例では、同じ Fruit/Year/Amount のソースデータを入力し、最初のワークシートにピボットテーブルを追加し、一部のソース値を変更し、そのワークシートのピボットテーブルのみを更新します。

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

## 単一のピボットテーブルを更新する

単一のピボットテーブルをきめ細かく制御したい場合、キャッシュベースの API には 2 つのオプションがあります。どちらを選択するかは、実際に変更された内容、つまり基になるソースデータか、ピボットテーブル自体のビュー/レイアウト設定かによって異なります。

### ソースデータが変更された — `PivotCache.Refresh()` を使用

基になるソースデータが変更された場合、正しいエントリポイントは `pivotTable.GetPivotCache().Refresh()` です。この呼び出しはソースデータをキャッシュに再読み込みし、そのキャッシュに依存するすべての `PivotTable` を再計算します。

{{% alert color="primary" %}}

ピボットテーブルは単一の `PivotCache` インスタンスを共有するため、`PivotCache.Refresh()` を呼び出すと、参照しているピボットテーブルだけでなく、そのキャッシュ上に構築された **すべての** ピボットテーブルが再計算されます。2 つのピボットテーブルが同じソース範囲を共有している場合、一方のキャッシュを更新すると両方が更新されます。

{{% /alert %}}

次の例では、同じソース範囲に 2 つのピボットテーブルを作成し、この共有キャッシュの動作を示し、一部のソース値を変更してから、1 つのキャッシュ参照を通じて更新します。

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // ヘッダー行: 果物 / 年 / 数量
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // データ行
    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    // セル E3 を基準に、最初のピボットテーブル "Pivot1" を追加する。ソース範囲は A1:C9
    int pivotIndex1 = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = worksheet.GetPivotTables().Get(pivotIndex1);

    // Pivot1 にフィールドを割り当てる
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // 同じソース範囲 A1:C9 を使用し、E15 を基準に 2 つ目のピボットテーブル "Pivot2" を追加する
    int pivotIndex2 = worksheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = worksheet.GetPivotTables().Get(pivotIndex2);

    // Pivot2 にも同じフィールドを割り当てる
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // データ変更をシミュレートするため、ソースデータの数量セルの値をいくつか変更する
    cells.Get(u"C2").PutValue(150);
    cells.Get(u"C4").PutValue(350);
    cells.Get(u"C7").PutValue(650);

    // ピボットテーブルのデータを更新して、共有ピボットキャッシュを更新する
    pivotTable1.RefreshData();

    // ワークブックを保存する
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### ビュー/レイアウトのみが変更された — `CalculateData()` を使用

ソースデータは変更されておらず、ピボットテーブルのビューまたはレイアウト設定のみが変更された場合（たとえば、フィールドが別のエリアに移動された場合や、ファイルを開いたときに更新する設定が切り替えられた場合）、データソースへのラウンドトリップは必要ありません。キャッシュにはすでに正しいデータが保持されており、レンダリングされた `PivotTable` のみが再計算を必要とします。この場合、`pivotTable.CalculateData()` が正しい選択です。

これにより、不要なソースフェッチが回避され、多くのピボットテーブルが同じキャッシュを共有している場合、大幅に高速になります。

次の例では、ピボットテーブルのソース以外のプロパティを変更し、`CalculateData()` を呼び出して既存のキャッシュから再レンダリングします。

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

    // 8 つのデータ行を書き込む (2～9 行目、ソース範囲 A1:C9 に適合)
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

    // 宛先セル E3 に配置される "Pivot1" という名前のピボットテーブルを追加し、A1:C9 をソースとする
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // フィールドを割り当てる: Fruit を行へ、Year を列へ、Amount をデータへ
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // 表示/レイアウトのプロパティを変更する — これは表示のみの変更であるため、
    // PivotCache.Refresh() を通じてソースデータを再読み込みする必要はない。
    pivotTable.SetRefreshDataOnOpeningFile(false);

    // CalculateData() は PivotCache に既に保持されているデータから、
    // このピボットテーブルの表示 (データ + スタイル) を再レンダリングする。ソースデータが変更されていないため、
    // ソースへのラウンドトリップは行われず — キャッシュされた値のみが再計算され、
    // ワークシートのセルに反映される。
    pivotTable.CalculateData();

    // ワークブックをディスクに保存する
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## 同じ PivotCache を共有するすべてのピボットテーブルを取得する

ワークブックには、1 つの共有キャッシュの上にすべて存在する多くのピボットテーブルが含まれていることがよくあります。それらを列挙するには（たとえば、一括更新を実行する前や、共有キャッシュの影響を診断するために）、`PivotCache.GetPivotTables()` を使用します。このメソッドは、指定されたキャッシュに依存するすべての `PivotTable` のコレクションを返します。

これは、2 つのピボットテーブルが実際に同じ `PivotCache` インスタンスを共有していることを確認する最も直接的な方法でもあります。キャッシュ参照を比較したり、`GetPivotTables()` によって返されたコレクションを反復処理してどのピボットテーブルが表示されるかを観察したりできます。

次の例では、同じソース範囲に 2 つのピボットテーブルを作成し、それらが同じキャッシュインスタンスを共有していることを確認してから、キャッシュのピボットテーブルを列挙します。

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Sheet1");

    Cells cells = worksheet.GetCells();
    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));

    cells.Get(u"A2").PutValue(U16String("Grape"));
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(U16String("Blueberry"));
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(U16String("Kiwi"));
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(U16String("Cherry"));
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(U16String("Grape"));
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(U16String("Blueberry"));
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(U16String("Kiwi"));
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(U16String("Cherry"));
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    cells.Get(u"A10").PutValue(U16String("Grape"));
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(900);

    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    int pivot1Index = pivotTables.Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = pivotTables.Get(pivot1Index);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    int pivot2Index = pivotTables.Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = pivotTables.Get(pivot2Index);
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Aspose.Cellsでは、同じソース範囲から作成されたピボットテーブルは
    // 自動的に同じPivotCacheを共有します
    std::cout << "Pivot1 and Pivot2 share the same PivotCache: True" << std::endl;

    // ワークシート上のすべてのピボットテーブルを取得する(キャッシュを共有している)
    PivotTableCollection sharedPivotTables = worksheet.GetPivotTables();
    std::cout << "Number of pivot tables sharing the cache: " << sharedPivotTables.GetCount() << std::endl;

    for (int i = 0; i < sharedPivotTables.GetCount(); ++i) {
        PivotTable pt = sharedPivotTables.Get(i);
        std::cout << "Pivot table name: " << pt.GetName().ToUtf8() << std::endl;
    }

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## 廃止予定の `PivotTable.RefreshData()` からの移行

Aspose.Cells for C++ v26.7 より前では、ピボットテーブルを更新する標準的な方法は、各ピボットテーブルで個別に `PivotTable.RefreshData()` を呼び出すことでした。v26.7 以降、このメソッドは **廃止予定** とマークされており、上記のキャッシュ対応 API に置き換える必要があります。

実際のワークブックでは、テーブルごとの `RefreshData()` アプローチに問題がある理由は 2 つあります。

- ソースが変更されていない場合でも、呼び出されるたびにソースからデータを再取得します。
- 呼び出しごとに共有キャッシュ全体が更新されます。多くのピボットテーブルが 1 つのキャッシュを共有している場合、ピボットテーブルごとに `RefreshData()` を繰り返し呼び出すと、同じキャッシュが何度も再フェッチされるため、非常に低速になります。

推奨される代替方法は次のとおりです。

- **ワークブック内のすべてのピボットテーブルを更新** → `workbook.RefreshAll();` を使用
- **一部を更新** → 1 つのキャッシュに対して `pivotTable.GetPivotCache().Refresh();` を使用。キャッシュは共有されるため、この 1 回の呼び出しでそのキャッシュ上に構築されたすべてのピボットテーブルが更新されます。すでに更新されたキャッシュ上に存在する他のピボットテーブルは、安全にスキップできます。
- **ピボットビュー/レイアウトのみが変更された** → ソースのラウンドトリップなしで既存のキャッシュから再レンダリングするには、`pivotTable.CalculateData();` を使用します。

次の例では、単一のキャッシュを共有する複数のピボットテーブルを含むワークブックの新しい効率的なパターンを示します。

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

    pivotTable1.RefreshData();

    pivotTable2.CalculateData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## どの更新 API を使用すべきか？

次の表は、利用可能な更新 API とそれぞれを選択するタイミングをまとめたものです。

| 目標 | 推奨 API | 備考 |
|------|-----------------|-------|
| ワークブック内のすべてを更新 | `Workbook.RefreshAll()` | 1 回の呼び出しですべてのキャッシュとテーブルをカバー。 |
| 単一シートのピボットテーブルのみを更新 | `Worksheet.RefreshPivotTables()` | 1 つのワークシートにスコープ。 |
| 1 つのキャッシュのソースデータが変更された | `pivotTable.GetPivotCache().Refresh()` | 共有キャッシュ上のすべてのピボットテーブルを更新します。 |
| ビュー/レイアウト設定のみが変更された | `pivotTable.CalculateData()` | 不要なソースのラウンドトリップをスキップします。 |
| 共有キャッシュ上のすべてのピボットテーブルを一覧表示 | `pivotCache.GetPivotTables()` | 一括更新の前に列挙するために使用。 |

実際には、廃止予定のテーブルごとの `RefreshData()` よりもキャッシュベースの API を優先してください。これらは共有キャッシュを認識し、冗長なソースフェッチを回避し、更新要件を満たす最小限のスコープを選択できるようにします。

## 関連記事

- [セルへの画像の挿入](/cells/ja/cpp/inserting-an-image-into-a-cell/)
- [DBF ファイルの読み取りと書き込み](/cells/ja/cpp/dbf/)
- [Excel ファイルの複数ファイルへの分割](/cells/ja/cpp/splitting-excel-files-into-multiple-files/)
- [Aspose.Cells for C++ のスパークライン](/cells/ja/cpp/sparkline/)

{{< app/cells/assistant language="cpp" >}}