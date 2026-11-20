---
title: ピボットフィールド項目の離散グループ化
linktitle: 離散グループ化
description: Aspose.Cells for C++ の DiscreteGroupItem と PivotFieldGroupOptions.DiscreteGroupItems を使用して、果物や野菜のような任意の名前を持つカスタムグループにピボットフィールド項目をグループ化する方法を学びます。
keywords: Aspose.Cells for C++, ピボットテーブル, 離散グループ化, DiscreteGroupItem, PivotFieldGroupOptions, ピボット項目のグループ化, カスタムグループ, PivotField.Group, C++, Excel ピボットテーブル
type: docs
weight: 90
url: /ja/cpp/discrete-group-pivot-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる使用シナリオ**
- 自動グループ化は、データの種類に基づいて項目をまとめます。日付を月や四半期にまとめ、数値を範囲にまとめます。離散グループ化はこれとは逆に、特定の互いに無関係な項目を任意の名前を持つカスタムグループにまとめる機能です。例えば、商品を果物と野菜に、店舗を地域に、勘定科目をゾーンにまとめる場合です。Aspose.Cells は `DiscreteGroupItem` クラスと `PivotFieldGroupOptions.DiscreteGroupItems` プロパティを通じて離散グループ化を提供します。
- `DiscreteGroupItem` は、グループ名と、そのグループに属する項目で構成されます。項目は 2 つの方法で識別できます。名前 (`DiscreteGroupItem("fruit", { "grape", "cherry" })`) で指定するか、ソースデータ内の 0 始まりの位置 (`DiscreteGroupItem("fruit", { 0, 3 })`) で指定するかです。どちらの形式でも同じ結果になります。
- 離散グループ化は、オプションを `PivotField.Group(PivotFieldGroupOptions)` に渡すことで、ピボットテーブルの行領域または列領域にあるフィールドに適用されます。

## **項目名によるピボットフィールド項目のグループ化**
以下の例では、小さな売上リスト（商品、日付、金額）を作成し、そのデータに基づいて、`product` を行領域、`date` を列領域、`amount` をデータ領域に配置したピボットテーブルを作成します。次に、項目名に基づいて、fruit（grape、cherry）と vegetable（carrot、potato）の 2 つのカスタムグループを定義します。結果として、2 階層の行レイアウトになります。外側のレベルにはグループ名、その下には元の項目がネストされるため、カスタムグループ単位でも項目単位でも傾向を読み取ることができます。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(0, 0).PutValue(u"product");
    cells.Get(1, 0).PutValue(u"grape");
    cells.Get(2, 0).PutValue(u"carrot");
    cells.Get(3, 0).PutValue(u"potato");
    cells.Get(4, 0).PutValue(u"cherry");
    Style dateStyle = wb.CreateStyle();
    dateStyle.SetCustom(u"m/d/yyyy");
    cells.Get(0, 1).PutValue(u"date");
    cells.Get(1, 1).PutValue(Date{2021, 2, 5, 0, 0, 0, 0});
    cells.Get(2, 1).PutValue(Date{2022, 3, 8, 0, 0, 0, 0});
    cells.Get(3, 1).PutValue(Date{2023, 4, 10, 0, 0, 0, 0});
    cells.Get(4, 1).PutValue(Date{2024, 5, 16, 0, 0, 0, 0});
    for (int r = 1; r <= 4; ++r) {
        cells.Get(r, 1).SetStyle(dateStyle);
    }
    cells.Get(0, 2).PutValue(u"amount");
    cells.Get(1, 2).PutValue(50);
    cells.Get(2, 2).PutValue(60);
    cells.Get(3, 2).PutValue(70);
    cells.Get(4, 2).PutValue(80);
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=Sheet1!A1:C5", 11, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"product"));
    pivotTable.AddFieldToArea(PivotFieldType::Column, U16String(u"date"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"amount"));
    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleMedium10);
    DiscreteGroupItem fruit(u"fruit", Vector<U16String>{u"grape", u"cherry"});
    DiscreteGroupItem vegetable(u"vegetable", Vector<U16String>{u"carrot", u"potato"});
    PivotFieldGroupOptions groupOptions;
    groupOptions.SetDiscreteGroupItems(Vector<DiscreteGroupItem>{fruit, vegetable});
    pivotTable.GetRowFields().Get(0).Group(groupOptions);
    pivotTable.CalculateData();
    wb.Save(u"outputDiscreteGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

`CalculateData()` の後、ピボットテーブルの行領域には、fruit (grape 50、cherry 80) と vegetable (carrot 60、potato 70) が表示され、grand total は 260 になります。また、列ラベルには 4 つの日付 (2/5/2021、3/8/2022、4/10/2023、5/16/2024) がそのまま保持されます。

## **項目インデックスによるピボットフィールド項目のグループ化**
項目名が長い、またはローカライズされている場合、`DiscreteGroupItem` の 2 番目のコンストラクターはインデックスで項目を識別します。インデックスは、ソースデータ内で項目が現れる順序に基づく 0 始まりの位置であり、アルファベット順ではありません。上記のサンプルデータでは、grape は項目 0、carrot は項目 1、potato は項目 2、cherry は項目 3 となるため、fruit は `{ 0, 3 }`、vegetable は `{ 1, 2 }` になります。結果は項目名による例と同じです。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(0, 0).PutValue(u"product");
    cells.Get(1, 0).PutValue(u"grape");
    cells.Get(2, 0).PutValue(u"carrot");
    cells.Get(3, 0).PutValue(u"potato");
    cells.Get(4, 0).PutValue(u"cherry");
    Style dateStyle = wb.CreateStyle();
    dateStyle.SetCustom(u"m/d/yyyy");
    cells.Get(0, 1).PutValue(u"date");
    Date firstDate{2021, 2, 5, 0, 0, 0, 0};
    Date secondDate{2022, 3, 8, 0, 0, 0, 0};
    Date thirdDate{2023, 4, 10, 0, 0, 0, 0};
    Date fourthDate{2024, 5, 16, 0, 0, 0, 0};
    cells.Get(1, 1).PutValue(firstDate);
    cells.Get(2, 1).PutValue(secondDate);
    cells.Get(3, 1).PutValue(thirdDate);
    cells.Get(4, 1).PutValue(fourthDate);
    for (int r = 1; r <= 4; ++r) {
        cells.Get(r, 1).SetStyle(dateStyle);
    }
    cells.Get(0, 2).PutValue(u"amount");
    cells.Get(1, 2).PutValue(50);
    cells.Get(2, 2).PutValue(60);
    cells.Get(3, 2).PutValue(70);
    cells.Get(4, 2).PutValue(80);
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=Sheet1!A1:C5", 11, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"product");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"date");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"amount");
    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleMedium10);
    DiscreteGroupItem fruit(u"fruit", Vector<int32_t>{0, 3});
    DiscreteGroupItem vegetable(u"vegetable", Vector<int32_t>{1, 2});
    PivotFieldGroupOptions groupOptions;
    groupOptions.SetDiscreteGroupItems(Vector<DiscreteGroupItem>{fruit, vegetable});
    pivotTable.GetRowFields().Get(0).Group(groupOptions);
    pivotTable.CalculateData();
    wb.Save(u"outputDiscreteGroupPivotFieldByIndex.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **注意**

{{% alert color="primary" %}}
- どのカスタムグループにも割り当てられていない項目は失われません。カスタムグループと同じレベルにピボットテーブル内に残り、それぞれが単独の項目エントリとして維持されます。上記の例では、fruit グループのみを定義すると、carrot と potato は行領域に fruit グループの隣に独立したエントリとして残ります。
- `PivotFieldGroupOptions.NewPivotField` プロパティは離散グループ化のレイアウトを制御します。デフォルト値は true です。グループ化したフィールドを元のフィールドに隣接する新しい外側フィールドとして追加することで、上記のような 2 階層のレイアウトになります (`RowFields` は 2 になります)。false に設定すると、元のフィールドが置き換えられます。行領域には、グループ名とその集計値のみを含む 1 階層が表示され、fruit は 130 (50 + 80)、vegetable は 130 (60 + 70) となります。
- `DiscreteGroupItem` の名前ベースとインデックスベースのコンストラクターは、同じ `DiscreteGroupItems` コレクション内で併用できます。
{{% /alert %}}

## **関連記事**
- [ピボットテーブル内でピボットフィールドをグループ化する](/cells/ja/cpp/group-pivot-fields-in-the-pivot-table/)
- [ピボットテーブルに行と列のフィールドを追加する](/cells/ja/cpp/pivot-table-add-row-and-column-fields/)
- [ラベルまたは値によるピボットテーブルのフィルタリング](/cells/ja/cpp/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルにスタイルを適用する](/cells/ja/cpp/apply-style-to-pivot-table/)
- [ピボットテーブルを更新する](/cells/ja/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}