---
title: Aspose.Cells for C++ におけるピボットテーブルの行フィールドと列フィールド
linktitle: 行フィールドと列フィールド
description: ピボットテーブルの行領域および列領域に基本フィールドを追加し、`PivotField.SetSubtotals` を使用してピボットフィールドの小計を制御する方法を学びます。
keywords: Aspose.Cells, C++, ピボットテーブル, 行フィールド, 列フィールド, PivotField, SetSubtotals, PivotFieldSubtotalType, 小計
type: docs
weight: 220
url: /ja/cpp/row-and-column-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

行フィールドと列フィールドはピボットテーブルの構成要素です。行領域に配置されたフィールドはピボットテーブルの左側に縦方向に、列領域に配置されたフィールドは上部に横方向にそれぞれ表示されます。この記事では、プログラムによってこれらの領域に基本フィールドを追加する方法、および `PivotField.SetSubtotals` メソッドを使用してフィールドグループ間に表示される小計を制御する方法を説明します。

## **行領域または列領域へのフィールドの追加**

`PivotTable.AddFieldToArea(PivotFieldType fieldType, intrusive_ptr<Aspose::Cells::Systems::String> fieldName)` メソッドは、ソースデータから基本フィールドを4つのピボット領域のいずれかに移動します。`fieldType` 引数は次の `PivotFieldType` 値のいずれかを受け付けます。

- `Row` — 左側に縦方向に配置されるフィールド
- `Column` — 上部に横方向に配置されるフィールド
- `Data` — 値が集計されるフィールド
- `Page` — レポートフィルターとして使用されるフィールド

フィールドを追加した後、`PivotTable.RowFields` プロパティおよび `PivotTable.ColumnFields` プロパティを介してそれらにアクセスできます。各プロパティは `PivotFieldCollection` を返します。`RowFields` のインデックス 0 のフィールドが最も外側の行フィールドであり、後続のインデックスはその内側にネストされたフィールドを表します。同じインデックス規約が `ColumnFields` にも適用されます。

フィールドのネスト順序は重要です。最初に行領域に `Category` を追加し、その後 `Item` を追加すると、外側のグループ化が `Category`、内側のグループ化が `Item` になるピボットが生成されます。順序を逆にした場合、階層も逆になります。

## **ピボットフィールドの小計**

`PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` メソッドは、ピボットフィールドに表示される小計行を制御します。各呼び出しは単一の小計タイプを独立に切り替えます。`shown = true` を渡すと小計が表示され、`shown = false` を渡すと非表示になります。各呼び出しは1つのタイプにのみ影響するため、異なる `subtotalType` 値で複数回メソッドを呼び出すことで、小計のカスタムサブセットを構築できます。

`PivotFieldSubtotalType` 列挙型は、利用可能な小計の種類を定義します。

- `Automatic` — Aspose.Cells がデフォルトの選択を行います (通常、数値フィールドには `Sum`)
- `None` — すべての小計行を抑制します
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
小計は、行領域 (または列領域) に2つ以上のピボットフィールドがある場合にのみ表示されます。単一のフィールドでは小計を計算する意味がないため、その場合 `SetSubtotals` 呼び出しは表示上の効果を持ちません。したがって、この記事では、すべての例で2つの行フィールド (`Category` が外側、`Item` が内側) を配置し、各 `Category` グループ間の小計境界が表示されるようにしています。
{{% /alert %}}

## **シナリオ 1 — 自動 (デフォルト) 小計**

`SetSubtotals` をまったく呼び出さない場合、Aspose.Cells は数値フィールドに `Automatic` 選択を適用します。次の例では、外側の `Category` 行フィールドで `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` を呼び出すことによって、この動作を明示的に確認します。

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    worksheet.GetCells().Get(0, 0).PutValue(u"Category");
    worksheet.GetCells().Get(0, 1).PutValue(u"Item");
    worksheet.GetCells().Get(0, 2).PutValue(u"Year");
    worksheet.GetCells().Get(0, 3).PutValue(u"Amount");

    worksheet.GetCells().Get(1, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(1, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(1, 2).PutValue(2020);
    worksheet.GetCells().Get(1, 3).PutValue(100);

    worksheet.GetCells().Get(2, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(2, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(2, 2).PutValue(2021);
    worksheet.GetCells().Get(2, 3).PutValue(150);

    worksheet.GetCells().Get(3, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(3, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(3, 2).PutValue(2020);
    worksheet.GetCells().Get(3, 3).PutValue(80);

    worksheet.GetCells().Get(4, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(4, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(4, 2).PutValue(2021);
    worksheet.GetCells().Get(4, 3).PutValue(90);

    worksheet.GetCells().Get(5, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(5, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(5, 2).PutValue(2020);
    worksheet.GetCells().Get(5, 3).PutValue(50);

    worksheet.GetCells().Get(6, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(6, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(6, 2).PutValue(2021);
    worksheet.GetCells().Get(6, 3).PutValue(60);

    worksheet.GetCells().Get(7, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(7, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(7, 2).PutValue(2020);
    worksheet.GetCells().Get(7, 3).PutValue(40);

    worksheet.GetCells().Get(8, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(8, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(8, 2).PutValue(2021);
    worksheet.GetCells().Get(8, 3).PutValue(45);

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Automatic, true);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"output_automatic.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **シナリオ 2 — すべての小計の抑制 (None)**

`SetSubtotals(PivotFieldSubtotalType.None, true)` を呼び出すと、ピボットからすべての小計行が削除され、フィールド行と最下部にある総計のみが残ります。これは、集計行なしの生のグループ化データが必要な場合に便利です。

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    sheet.SetName(u"Data");

    U16String headers[] = { u"Category", u"Item", u"Year", u"Amount" };
    for (int j = 0; j < 4; j++) {
        sheet.GetCells().Get(0, j).PutValue(headers[j]);
    }

    U16String categories[] = { u"Fruit", u"Fruit", u"Fruit", u"Fruit",
                               u"Vegetable", u"Vegetable", u"Vegetable", u"Vegetable" };
    U16String items[] = { u"Apple", u"Apple", u"Banana", u"Banana",
                          u"Carrot", u"Carrot", u"Daikon", u"Daikon" };
    int years[]   = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
    int amounts[] = {  100,  150,   80,   90,   50,   60,   40,   45 };

    for (int i = 0; i < 8; i++) {
        sheet.GetCells().Get(i + 1, 0).PutValue(categories[i]);
        sheet.GetCells().Get(i + 1, 1).PutValue(items[i]);
        sheet.GetCells().Get(i + 1, 2).PutValue(years[i]);
        sheet.GetCells().Get(i + 1, 3).PutValue(amounts[i]);
    }

    int pivotIndex = sheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = sheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::None, true);
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    wb.Save(u"output_none.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **シナリオ 3 — カスタム小計サブセット (Sum + Average)**

単一の小計タイプに限定されません。各 `SetSubtotals` 呼び出しは1つのタイプに対して独立して動作するため、メソッドを2回 (1回は `Sum`、もう1回は `Average`) 呼び出すことで、各 `Category` グループに対して2つの小計行のカスタムサブセットが生成されます。

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    worksheet.GetCells().Get(u"A1").PutValue(u"Category");
    worksheet.GetCells().Get(u"B1").PutValue(u"Item");
    worksheet.GetCells().Get(u"C1").PutValue(u"Year");
    worksheet.GetCells().Get(u"D1").PutValue(u"Amount");

    worksheet.GetCells().Get(1, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(1, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(1, 2).PutValue(2020);
    worksheet.GetCells().Get(1, 3).PutValue(100);

    worksheet.GetCells().Get(2, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(2, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(2, 2).PutValue(2021);
    worksheet.GetCells().Get(2, 3).PutValue(150);

    worksheet.GetCells().Get(3, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(3, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(3, 2).PutValue(2020);
    worksheet.GetCells().Get(3, 3).PutValue(80);

    worksheet.GetCells().Get(4, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(4, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(4, 2).PutValue(2021);
    worksheet.GetCells().Get(4, 3).PutValue(90);

    worksheet.GetCells().Get(5, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(5, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(5, 2).PutValue(2020);
    worksheet.GetCells().Get(5, 3).PutValue(50);

    worksheet.GetCells().Get(6, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(6, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(6, 2).PutValue(2021);
    worksheet.GetCells().Get(6, 3).PutValue(60);

    worksheet.GetCells().Get(7, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(7, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(7, 2).PutValue(2020);
    worksheet.GetCells().Get(7, 3).PutValue(40);

    worksheet.GetCells().Get(8, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(8, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(8, 2).PutValue(2021);
    worksheet.GetCells().Get(8, 3).PutValue(45);

    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Sum, true);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Average, true);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"output_custom.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **まとめ**

上記の3つのシナリオは、データセットとピボットテーブルの構造を共有しています。それらの唯一の違いは、外側の `Category` 行フィールドに適用される `SetSubtotals` 呼び出しです。2つのフィールドのルールを忘れないでください: 領域内の単一のフィールドには小計対象の間隔がないため、`SetSubtotals` を視覚的な効果を持たせたい場合は、行領域または列領域に常に少なくとも2つのフィールドを配置してください。

## **関連項目**

- [ピボットテーブル内のページフィールド](/cells/ja/cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for C++ におけるピボットテーブルの更新](/cells/ja/cpp/refresh-pivot-table/)
- [ピボットテーブルへのスタイルの適用](/cells/ja/cpp/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
