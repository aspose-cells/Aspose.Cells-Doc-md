---
title: Aspose.Cells for C++でピボットテーブルを更新する
linktitle: Aspose.Cells for C++でピボットテーブルを更新する
description: Aspose.Cells for C++でv26.7以上のピボット更新APIを使用してピボットテーブルを更新する方法を学びます。この記事ではRefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData、GetPivotTablesを実用的なコード例とともに解説します。
keywords: Aspose.Cells, C++, ピボットテーブル, 更新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ja/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cellsは、ワークブック全体から単一のピボットテーブルまで、4つの異なるスコープでピボットデータを再読み込みできる階層化された更新APIを提供します。**Aspose.Cells for C++ v26.7**以降、レガシーメソッドの`PivotTable.RefreshData()`は廃止予定（非推奨）となり、この記事で説明するより効率的でキャッシュ対応のAPIに置き換える必要があります。
{{% /alert %}}
## はじめに
ピボットテーブルの更新は、単一の操作であることはほとんどありません。舞台裏では、Aspose.Cellsは元のソースデータをワークシートに表示されるレンダリング値に接続する階層化されたデータチェーンを維持しています。このチェーンを理解することが、あらゆる状況で適切な更新APIを選択する鍵となります。
四層データチェーンは次のとおりです：
1. **データソース（Data Source）** — 元のワークシート範囲、データベースクエリ、または生の値が存在する統合範囲。
2. **PivotCache** — ソースデータのインメモリスナップショット。すべてのピボットテーブルは`PivotCache`の上に構築されます。ここですべてのデータが集約・集計されます。
3. **PivotTable** — 行、列、値、フィルタフィールドを定義するビューオブジェクト。`PivotTable`はその`PivotCache`からの*み*読み取り、データソースから直接読み取ることは決してありません。
4. **Cells** — `PivotTable`が計算された値とスタイルを描画するワークシートの`Cells`。
特に重要な概念は**共有キャッシュ**です。ワークブック内の複数のピボットテーブルが同じソース範囲を参照している場合、それらは*1つの*`PivotCache`インスタンスを共有します。1つの`PivotCache`を多くのピボットテーブルから参照でき、そのキャッシュを更新すると、依存するすべての`PivotTable`が一度に更新されます。
{{% alert color="primary" %}}
`PivotCache.SourceType`（列挙型`PivotTableSourceType`）はキャッシュデータの取得元を示します。v26.7時点で、`PivotCache.Refresh()`は**`Sheet`**および**`Consolidation`**ソースタイプ、つまりワークシート範囲に存在するデータのみをサポートします。外部ソース（データベースや外部接続など）は、まだキャッシュAPI経由で更新できません。
{{% /alert %}}
このチェーンのため、Aspose.Cellsには2つの基本的な更新パスがあります：
- **`PivotCache.Refresh()`** — ソースからキャッシュへの再読み込み、およびそれに依存するすべての`PivotTable`の再計算を1回の操作で行います。
- **`PivotTable.CalculateData()`** — すでにキャッシュされているデータから、1つの`PivotTable`の表示を再計算します。データソースへのラウンドトリップはありません。
この記事のすべてのシナリオではワークシートセルソースデータを使用しているため、ソースタイプは`Sheet`であり、更新操作は記載どおりに動作します。
## 必要なインクルードディレクティブ
この記事のすべてのC++の例は、ピボットタイプが`Aspose::Cells::Pivot`名前空間に存在するため、以下のヘッダーインクルードと名前空間ディレクティブから始まります：
## ワークブック内のすべてのピボットテーブルを更新する
ワークブック内のすべてのピボットキャッシュとすべてのピボットテーブルが最新のソースデータを反映していることを確認する必要がある場合、最もシンプルで包括的なAPIは`Workbook.RefreshAll()`です。1回の呼び出しでワークブック全体を横断し、各`PivotCache`をソースから更新し、依存するすべての`PivotTable`を再計算します。これは、パフォーマンスが気にならない一般的な、ドキュメント全体の更新に対して推奨されるアプローチです。
次の例では、Fruit/Year/Amountソース範囲を持つワークブックを作成し、1つのピボットテーブルを作成し、いくつかのソース値を変更し、`RefreshAll()`を使用して単一の呼び出しですべてを最新の状態にします。
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
## 単一ワークシート上のすべてのピボットテーブルを更新する
時には、特定の1つのワークシート上にあるピボットテーブルだけを更新する必要がある場合があります（例えば、他のワークシート上のピボットテーブルは無関係で、触るべきではないと分かっている場合）。この場合、Aspose.Cellsは単一の`Worksheet`インスタンスにスコープされた`Worksheet.RefreshPivotTables()`を提供します。
これは`Workbook.RefreshAll()`よりも選択的です。対象ワークシート上のピボットテーブルのみが更新され、他のワークシート上のピボットテーブルはそのまま残ります。
次の例では、同じFruit/Year/Amountソースデータを格納し、最初のワークシートにピボットテーブルを追加し、いくつかのソース値を変更した後、そのワークシート上のピボットテーブルだけを更新します。
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
単一のピボットテーブルに対して細かい制御を行いたい場合、キャッシュベースのAPIは2つのオプションを提供します。どちらを選択するかは、実際に何が変わったかによって異なります：基礎となるソースデータか、ピボットテーブル自体の表示/レイアウト設定かだけです。
### ソースデータが変更された — `PivotCache.Refresh()`を使用
基礎となるソースデータが変更された場合、正しいエントリポイントは`pivotTable.GetPivotCache().Refresh()`です。この呼び出しはソースデータをキャッシュに再読み込みし、そのキャッシュに依存するすべての`PivotTable`を再計算します。
{{% alert color="primary" %}}
ピボットテーブルは単一の`PivotCache`インスタンスを共有するため、`PivotCache.Refresh()`を呼び出すと、参照しているピボットテーブルだけでなく、その同じキャッシュ上に構築された**すべての**ピボットテーブルが再計算されます。2つのピボットテーブルが同じソース範囲を共有している場合、1つのキャッシュを更新すると両方が更新されます。
{{% /alert %}}
次の例では、同じソース範囲上に2つのピボットテーブルを作成し、この共有キャッシュの動作を実証し、いくつかのソース値を変更した後、1つのキャッシュ参照を通して更新します。
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // ヘッダー行: 果物 / 年 / 金額
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

    // セルE3に固定された最初のピボットテーブル "Pivot1" を追加、ソース範囲は A1:C9
    int pivotIndex1 = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = worksheet.GetPivotTables().Get(pivotIndex1);

    // Pivot1 にフィールドを割り当てる
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // 同じソース範囲 A1:C9 を使用して、セルE15に固定された2番目のピボットテーブル "Pivot2" を追加
    int pivotIndex2 = worksheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = worksheet.GetPivotTables().Get(pivotIndex2);

    // Pivot2 に同じフィールドを割り当てる
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // データ変更をシミュレートするために、ソースデータのいくつかの Amount セルの値を変更する
    cells.Get(u"C2").PutValue(150);
    cells.Get(u"C4").PutValue(350);
    cells.Get(u"C7").PutValue(650);

    // ピボットテーブルのデータを更新して共有 PivotCache を更新する
    pivotTable1.RefreshData();

    // ブックを保存する
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
### 表示/レイアウトのみが変更された — `CalculateData()`を使用
ソースデータが変更されておらず、ピボットテーブルの表示やレイアウト設定のみが変更された場合（例えば、フィールドが別のエリアに移動された、またはファイルを開くときに更新する設定が切り替えられたなど）、データソースへのラウンドトリップは必要ありません。キャッシュにはすでに正しいデータが保持されており、レンダリングされた`PivotTable`を再計算するだけで済みます。この場合、`pivotTable.CalculateData()`が正しい選択です。
これにより、不要なソースフェッチが回避され、多くのピボットテーブルが同じキャッシュを共有している場合に大幅な高速化が実現します。
次の例では、ピボットテーブルのソース以外のプロパティを変更し、`CalculateData()`を呼び出して既存のキャッシュから再レンダリングします。
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

    // 8 行のデータ行を書き込む(2 ～ 9 行目、ソース範囲 A1:C9 に適合)
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

    // "Pivot1" という名前のピボットテーブルを追加し、配置先はセル E3、ソースは A1:C9
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // フィールドを割り当てる: Fruit を Row、Year を Column、Amount を Data に
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // 表示 / レイアウトプロパティを変更する — これは表示のみの変更であり、
    // PivotCache.Refresh() でソースデータを再読み込みする必要はない。
    pivotTable.SetRefreshDataOnOpeningFile(false);

    // CalculateData() は、PivotCache に保持されているデータから
    // このピボットテーブルの表示(データとスタイル)を再レンダリングする。
    // ソースデータが変更されていないため、ソースへのラウンドトリップは行われず、
    // キャッシュされた値がワークシートのセルに再計算されるだけである。
    pivotTable.CalculateData();

    // ワークブックをディスクに保存する
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## 同じPivotCacheを共有するすべてのピボットテーブルを取得する
ワークブックには、多くの場合、1つの共有キャッシュの上に存在する多数のピボットテーブルが含まれています。これらを列挙するには（例えば、一括更新を実行する前や、共有キャッシュの影響を診断する場合など）、`PivotCache.GetPivotTables()`を使用します。このメソッドは、指定されたキャッシュに依存するすべての`PivotTable`のコレクションを返します。
これは、2つのピボットテーブルが実際に同じ`PivotCache`インスタンスを共有していることを確認する最も直接的な方法でもあります。キャッシュ参照を比較するか、あるいは単に`GetPivotTables()`によって返されるコレクションを反復処理して、どのピボットテーブルがそこに出現するかを観察することができます。
次の例では、同じソース範囲上に2つのピボットテーブルを作成し、それらが同じキャッシュインスタンスを共有していることを確認し、キャッシュのピボットテーブルを列挙します。

## 廃止予定の`PivotTable.RefreshData()`からの移行
Aspose.Cells for C++ v26.7より前は、ピボットテーブルを更新する標準的な方法は、各ピボットテーブルに対して個別に`PivotTable.RefreshData()`を呼び出すことでした。v26.7時点で、そのメソッドは**廃止予定（非推奨）**となり、上記のキャッシュ対応APIに置き換える必要があります。
実世界のワークブックでテーブルごとの`RefreshData()`アプローチに問題がある理由は2つあります：
- ソースが変更されていない場合でも、呼び出されるたびにソースからデータを再取得します。
- 各呼び出しは共有キャッシュ全体を更新します。多くのピボットテーブルが1つのキャッシュを共有している場合、ピボットテーブルごとに`RefreshData()`を繰り返し呼び出すと、同じキャッシュが何度も再取得されることになり、非常に低速になります。
推奨される置き換えは次のとおりです：
- **ワークブック内のすべてのピボットテーブルを更新する** → `workbook.RefreshAll();`を使用します。
- **その一部を更新する** → 1つのキャッシュに対して`pivotTable.GetPivotCache().Refresh();`を使用します。キャッシュは共有されているため、この1回の呼び出しでそのキャッシュ上に構築されたすべてのピボットテーブルが更新されます。すでに更新されたキャッシュ上に存在する他のピボットテーブルは、安全にスキップできます。
- **ピボットビュー/レイアウトのみが変更された** → ソースへのラウンドトリップなしで既存のキャッシュから再レンダリングするには、`pivotTable.CalculateData();`を使用します。
次の例では、単一のキャッシュを共有する複数のピボットテーブルを持つワークブックの新しい効率的なパターンを示します。
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
## どの更新APIを使用すべきか？
以下の表は、利用可能な更新APIとそれぞれを選択するタイミングをまとめたものです。
| 目的 | 推奨API | メモ |
|------|-----------------|-------|
| ワークブック内のすべてを更新する | `Workbook.RefreshAll()` | 1回の呼び出しで、すべてのキャッシュとテーブルを対象とします。 |
| 単一シート上のピボットテーブルのみを更新する | `Worksheet.RefreshPivotTables()` | 1つのワークシートにスコープされます。 |
| 1つのキャッシュのソースデータが変更された | `pivotTable.GetPivotCache().Refresh()` | その共有キャッシュ上のすべてのピボットテーブルを更新します。 |
| 表示/レイアウト設定のみが変更された | `pivotTable.CalculateData()` | 不要なソースラウンドトリップをスキップします。 |
| 共有キャッシュ上のすべてのピボットテーブルを一覧表示する | `pivotCache.GetPivotTables()` | 一括更新の前に列挙するために使用します。 |
実際には、廃止予定のテーブルごとの`RefreshData()`よりもキャッシュベースのAPIを優先してください。これらは共有キャッシュを認識し、冗長なソースフェッチを回避し、更新要件を満たす最小のスコープを選択できるようにします。

{{< app/cells/assistant language="cpp" >}}
