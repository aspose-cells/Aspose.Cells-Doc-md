---
title: ピボットテーブルのページフィールド
linktitle: ピボットテーブルのページフィールド
description: Aspose.Cells for C++ を使用して、ピボットテーブル内のページフィールドの追加と設定（ページフィールドの追加、単一選択フィルタリング、複数選択フィルタリングを含む）について学びます。
keywords: Aspose.Cells, C++, ピボットテーブル, ページフィールド, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, フィルター
type: docs
weight: 250
url: /ja/cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ピボットテーブル内のページフィールドの全ライフサイクルをサポートします。ハイレベルの便利な API または低レベルの `PageFields` コレクションを介してページフィールドを追加でき、単一選択モードでページフィルターを駆動したり、すべてのページ項目を表示するためにクリアしたり、フィールドを複数選択に切り替えて Excel のチェックボックス UI を通じて複数のページ項目を一度に選択できるようにしたりできます。
{{% /alert %}}

## **はじめに**

ページフィールドは、ピボット本体が表示するソースデータの *どのサブセット* を制御するピボットフィールドです。エンドユーザーは Excel でレンダリングされたピボットの上部にドロップダウンとしてそれを目にし、利用可能なページ項目のいずれかを選択すると、そのページ項目に属するレコードのみが集約されるようにピボット本体が再構築されます。ピボットフィールドは、`PivotFieldType.Row`、`PivotFieldType.Column`、または `PivotFieldType.Data` ではなく `PivotFieldType.Page` として登録された場合にページフィールドになります。

ページフィールドは 2 つの動作で動作できます。デフォルトの **単一選択** 動作では、一度に 1 つのページ項目のみが表示されるため、ピボット本体は正確に 1 つのサブセットを集約します。**複数選択** 動作では、フィールドはチェックボックスリストを公開し、ピボット本体はチェックされたすべてのページ項目の和集合を集約します。同じソースフィールドは、単一のプロパティを切り替えることによって、これらの動作間で行き来できます。

Aspose.Cells for C++ は、ページフィールドを登録する 2 つの同等の方法を公開しています。ハイレベル API は `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` で、ソース列名を引数として受け取り、単一の呼び出しでフィールドを追加します。低レベル API は `PivotTable.PageFields.Add(PivotField)` で、すでに `PivotField` 参照を保持しており、同じフィールドインスタンスをページ領域に追加したい場合に使用されます。両方の API は最終的に同じ `PageFields` コレクションを生成し、この記事の残りの部分では、それらの選択方法と各フィルタリングモードの駆動方法について説明します。

## **ページフィールドの追加**

ページ領域にピボットフィールドを登録するには 2 つの方法があります。ハイレベル呼び出しは、ソース列名を文字列として受け取り、最も一般的なパスです。低レベル呼び出しは既存の `PivotField` インスタンスを受け取り、同じフィールドオブジェクトを複数のピボット領域で再利用する必要がある場合に便利です。どちらの呼び出しもフィールドを `PivotTable.PageFields` に配置し、その後、レンダリングされたピボットの上部にページドロップダウンとして表示されます。

### AddFieldToArea を使用したページフィールドの追加

次の例は、小さな Fruit / Year / Amount データセットを作成し、`Fruit` を行領域、`Amount` をデータ領域、`Year` をページ領域としてセル E3 にピボットテーブルを配置し、ピボットを更新して、ワークブックを保存します。

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    // 新しいワークブックを作成
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    Cells cells = worksheet.GetCells();

    // ヘッダー行を設定
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // フルーツ、年度、数量の9行のサンプルデータを入力
    const char* fruits[] = { "apple", "banana", "apple", "grape", "orange", "banana", "grape", "apple", "orange" };
    int years[]   = { 2020, 2021, 2021, 2020, 2022, 2020, 2021, 2022, 2021 };
    int amounts[] = { 100, 200, 150, 120, 180, 90, 130, 170, 110 };

    for (int i = 0; i < 9; ++i)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }

    // セルE3にアンカーされたピボットテーブルを追加
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"PivotTable1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // フィールドをそれぞれのエリアに追加：フルーツを行、データをデータ、年度をページフィールド
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");

    // ピボットテーブルのデータを更新して計算
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // ワークブックを保存
    workbook.Save(u"pageFieldSample.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### PageFields.Add を使用したページフィールドの追加

すでに `PivotField` インスタンスを操作している場合は、それを `PivotTable.PageFields.Add` に直接渡すことができます。ピボットテーブルとページフィールドは前のシナリオとまったく同じ方法で構築されます。最終的なページ領域の登録のみが低レベル API 呼び出しに置き換えられます。

```cpp
#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // ヘッダー
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // サンプルデータ（9行）
    cells.Get(u"A2").PutValue(u"apple");     cells.Get(u"B2").PutValue(u"2020"); cells.Get(u"C2").PutValue(100);
    cells.Get(u"A3").PutValue(u"apple");     cells.Get(u"B3").PutValue(u"2021"); cells.Get(u"C3").PutValue(150);
    cells.Get(u"A4").PutValue(u"apple");     cells.Get(u"B4").PutValue(u"2022"); cells.Get(u"C4").PutValue(200);
    cells.Get(u"A5").PutValue(u"grape");     cells.Get(u"B5").PutValue(u"2020"); cells.Get(u"C5").PutValue(300);
    cells.Get(u"A6").PutValue(u"grape");     cells.Get(u"B6").PutValue(u"2021"); cells.Get(u"C6").PutValue(400);
    cells.Get(u"A7").PutValue(u"grape");     cells.Get(u"B7").PutValue(u"2022"); cells.Get(u"C7").PutValue(500);
    cells.Get(u"A8").PutValue(u"blueberry"); cells.Get(u"B8").PutValue(u"2020"); cells.Get(u"C8").PutValue(250);
    cells.Get(u"A9").PutValue(u"blueberry"); cells.Get(u"B9").PutValue(u"2021"); cells.Get(u"C9").PutValue(350);
    cells.Get(u"A10").PutValue(u"blueberry");cells.Get(u"B10").PutValue(u"2022");cells.Get(u"C10").PutValue(450);

    // E3にA1:C10をカバーするピボットテーブルを追加
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(U16String(u"E3"), U16String(u"A1:C10"), U16String(u"PivotTable1"));
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    // フルーツ -> 行、金額 -> データ
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"Amount"));

    // 低レベルアプローチ：BaseFieldsから既存のYear PivotFieldを検索し、
    // PageFields.Add(PivotField)経由でページ領域に登録する。
    PivotFieldCollection baseFields = pivotTable.GetBaseFields();
    int baseFieldCount = baseFields.GetCount();
    for (int i = 0; i < baseFieldCount; ++i) {
        PivotField f = baseFields.Get(i);
        if (f.GetName().ToUtf8() == "Year") {
            pivotTable.GetPageFields().Add(f);
            break;
        }
    }

    // 新しいページフィールドが保存されたワークブックに反映されるように更新
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **単一選択フィルタリング (1 つのページ項目の表示)**

デフォルトの単一選択動作では、ページフィールドは単一のドロップダウンとしてレンダリングされ、`PivotField.CurrentPageItem` 整数がピボット本体を駆動するページ項目を選択します。特定のインデックスを割り当てるとその項目が選択されます。特別なセンチネル `0x7FFD` (10 進数 32765) を割り当てるとフィルターがクリアされ、すべてのページ項目が一度に集約されます。単一選択がデフォルトです。明示的に有効にする必要はありません。

### すべての項目の表示

`CurrentPageItem` をマジック値 `0x7FFD` に設定することは、ページフィルターをクリアすることと同じです。フィルターが適用されていないかのように、ピボット本体はすべてのページ項目を集約します。

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    U16String fruits[6] = {u"Apple", u"Apple", u"Banana", u"Banana", u"Cherry", u"Cherry"};
    int years[6] = {2022, 2023, 2022, 2023, 2022, 2023};
    int amounts[6] = {100, 150, 80, 120, 200, 250};

    for (int r = 0; r < 6; r++) {
        cells.Get(r + 1, 0).PutValue(fruits[r]);
        cells.Get(r + 1, 1).PutValue(years[r]);
        cells.Get(r + 1, 2).PutValue(amounts[r]);
    }

    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int index = pivotTables.Add(u"=A1:C7", u"E3", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(index);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    pivotTable.GetPageFields().Get(0).SetCurrentPageItem(0x7FFD);

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### 特定の 1 つの項目の表示

`CurrentPageItem` を実際のインデックスに設定すると、その 1 つのページ項目のみが選択されます。インデックスはページフィールドのソートされた項目リスト内の項目の位置であるため、たとえば `1` はソート後に 2 番目の項目を選択します。

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));

    cells.Get(u"A2").PutValue(U16String("Apple"));
    cells.Get(u"B2").PutValue(U16String("2020"));
    cells.Get(u"C2").PutValue(U16String("100"));

    cells.Get(u"A3").PutValue(U16String("Apple"));
    cells.Get(u"B3").PutValue(U16String("2021"));
    cells.Get(u"C3").PutValue(U16String("150"));

    cells.Get(u"A4").PutValue(U16String("Banana"));
    cells.Get(u"B4").PutValue(U16String("2020"));
    cells.Get(u"C4").PutValue(U16String("200"));

    cells.Get(u"A5").PutValue(U16String("Banana"));
    cells.Get(u"B5").PutValue(U16String("2021"));
    cells.Get(u"C5").PutValue(U16String("250"));

    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(U16String("A1:C5"), U16String("E3"), U16String("PivotTable1"));
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String("Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String("Amount"));
    pivotTable.AddFieldToArea(PivotFieldType::Page, U16String("Year"));

    pivotTable.GetPageFields().Get(0).SetCurrentPageItem(1);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **複数選択フィルタリング**

複数選択フィルタリングは、ページドロップダウンをチェックボックスリストに変え、エンドユーザーが複数のページ項目を同時に選択できるようにします。Aspose.Cells は連携して動作する 2 つのプロパティを公開しています。複数選択 UI がまったく有効になる前に、`PivotField.IsMultipleItemSelectionAllowed` を `true` に設定する必要があります。有効にされた後、`PivotItem.IsHidden` はチェックボックスリストに表示される項目を制御するため、すべての項目を表示するか、特定の項目のみをホワイトリストに登録するかを選択できます。

次のコードは、シナリオ 1a で構築された同じ Year ページフィールドで複数選択を有効にし、2 つのパターンを示しています。パート A では、すべてのエントリの `IsHidden` を `false` のままにしてすべてのページ項目を公開し、パート B では、`switch (pivotItems[i].GetStringValue())` ブロックを介して、選択したソース値のみをホワイトリストに登録し、その他すべてを非表示にします。

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <vector>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // サンプルデータ: 果物 | 年 | 数量
    cells.Get(0, 0).PutValue(u"Fruit");
    cells.Get(0, 1).PutValue(u"Year");
    cells.Get(0, 2).PutValue(u"Amount");

    std::vector<std::vector<std::string>> data = {
        {"apple",  "2019", "100"},
        {"apple",  "2020", "150"},
        {"apple",  "2021", "200"},
        {"banana", "2019", "110"},
        {"banana", "2020", "160"},
        {"banana", "2021", "210"},
        {"grape",  "2019", "120"},
        {"grape",  "2020", "170"},
        {"grape",  "2021", "220"}
    };

    for (int i = 0; i < (int)data.size(); i++) {
        cells.Get(i + 1, 0).PutValue(U16String(data[i][0].c_str()));
        cells.Get(i + 1, 1).PutValue(std::stoi(data[i][1]));
        cells.Get(i + 1, 2).PutValue(std::stoi(data[i][2]));
    }

    Worksheet pivotSheet = workbook.GetWorksheets().Add(u"Pivot");
    PivotTableCollection pivots = pivotSheet.GetPivotTables();
    int pivotIndex = pivots.Add(u"E3", u"A1:C10", u"PivotTable1");
    PivotTable pivotTable = pivots.Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");

    // — ページフィールドで複数選択を有効にする
    pivotTable.GetPageFields().Get(0).SetIsMultipleItemSelectionAllowed(true);

    // パート A — すべての項目を選択 (すべての項目を表示する)
    PivotItemCollection pivotItems = pivotTable.GetPageFields().Get(0).GetPivotItems();
    int itemCount = pivotItems.GetCount();
    for (int i = 0; i < itemCount; i++) {
        pivotItems.Get(i).SetIsHidden(false);
    }

    // パート B — ソース値で特定の項目のみを選択
    for (int i = 0; i < itemCount; i++) {
        U16String val = pivotItems.Get(i).GetStringValue();
        std::string s = val.ToUtf8();
        if (s == "2020" || s == "grape" || s == "blueberry") {
            pivotItems.Get(i).SetIsHidden(false);
        } else {
            pivotItems.Get(i).SetIsHidden(true);
        }
    }

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

> **注意:** `PivotItem.IsHidden` を通じて複数選択フィルタリングを使用する場合、**少なくとも 1 つの `PivotItem` は表示されたままにする必要があります** (`IsHidden == false`)。すべての項目が非表示になっている場合、Excel はファイルを開くときにクラッシュするか、空のピボットをレンダリングします。複数選択のホワイトリストにソースデータから少なくとも 1 つの項目が含まれていることを常に確認してください。

## **どの API とどのモードを使用すべきか?**

次の表は、各 API とモードをいつ使用するかをまとめたもので、すべてのシナリオを詳細に読まなくても適切な組み合わせを選択できます。

| シナリオ / ユースケース | 推奨 API | 使用されるプロパティ | メモ |
|---|---|---|---|
| ソース列名でページフィールドを追加する (最も一般的) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | ハイレベル、ワンライナー。`PivotField` 参照が必要ない限り、これを使用してください。 |
| すでに `PivotField` オブジェクトがある場合にページフィールドを追加する | `PivotTable.PageFields.Add(PivotField)` | n/a | フィールドオブジェクトが他の場所で取得されたか、再利用が必要な場合に使用します。 |
| 単一のページ項目にフィルターする (デフォルトモード) | `PivotField.CurrentPageItem` | 特定のインデックスに設定 | たとえば、`1` はソートされたリストの 2 番目の項目を表示します。 |
| すべての項目を表示する / ページフィルターをクリアする | `PivotField.CurrentPageItem` | `0x7FFD` に設定 | マジック値 `0x7FFD` (10 進数 32765) は「すべての項目」のセンチネルです。 |
| Excel で複数選択 UI を有効にする | `PivotField.IsMultipleItemSelectionAllowed` | `true` に設定 | `IsHidden` 呼び出しが有効になる前に必要です。 |
| 複数選択リスト内の個別項目を非表示 / 表示する | `PivotItem.IsHidden` | 項目ごとに設定 | 少なくとも 1 つの項目が表示されたままである必要があります (`IsHidden == false`)。 |

{{% alert color="primary" %}}
複数選択フィルタリングを設定するときは、表示制約を常に覚えておいてください。複数選択ページフィールドのすべての `PivotItem` が非表示になっている場合、Excel は開くときにクラッシュするか、空のピボットをレンダリングします。少なくとも 1 つの項目が表示されたままになるようにソースデータに対してホワイトリストを構築すると、保存されたワークブックはすべてのマシンで確実に開きます。
{{% /alert %}}



{{< app/cells/assistant language="cpp" >}}