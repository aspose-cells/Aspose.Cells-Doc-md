---
title: ピボットテーブルで上位 10 件を表示またはフィルター
linktitle: ピボットテーブルで上位 10 件を表示またはフィルター
description: Aspose.Cells for C++ を使用して、ピボットフィールドの項目のうち、上位または下位にランク付けされた項目のみを表示する方法を学びます。この tensionesでは、Excel 97-2003 の Top10AutoShow メソッド、GetTop10AutoShowSettings によるオプションの読み取り、および FilterTop10 による Excel 2007-365 の上位 10 件フィルターについて説明します。
keywords: Aspose.Cells, C++, ピボットテーブル, 上位 10 件, 自動表示, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, GetTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField
type: docs
weight: 20
url: /ja/cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる利用シナリオ**
行フィールドのすべての項目を一覧表示するピボットテーブルは、そのフィールドに数十の項目がある場合、読み取りにくくなります。上位 10 件のレポートは、上位または下位の項目だけを残します。これは、「収益による上位 5 製品」や「販売数による下位 3 地域」のようなランキングレポートにまさに適合します。Aspose.Cells はこの機能として 2 つのメカニズムをサポートしており、それぞれ Microsoft Excel の 2 つの世代に対応しています。
- **Excel 97-2003 の自動表示** — `PivotField.Top10AutoShow()` メソッドです。これは、ピボットフィールドに直接保存される従来の「上位/下位 N 項目を表示」設定です。元のピボットテーブル形式の一部であるため、新旧すべての Excel バージョンで機能します。
- **Excel 2007-365 の上位 10 件フィルター** — `PivotField.FilterTop10()` メソッドです。これは、フィールドメニューの「値フィルター」にある新しい上位 10 件の値フィルターです。フィールドに関連付けられた `PivotFilter` オブジェクトとして保存され、項目数とパーセントに基づくランキングに対応しています。

## **Excel 97-2003 での上位 10 件の表示 (Top10AutoShow)**
従来の自動表示は、`PivotField.Top10AutoShow(bool isAutoShow, bool isTop, int32_t count, int32_t rankBy)` を一度呼び出すことで設定されます。
- `isAutoShow` — フィールドの自動表示設定を有効または無効にします。
- `isTop` — `true` の場合は最高順位の項目（上位）を保持し、`false` の場合は最低順位の項目（下位）を保持します。
- `count` — 保持する項目数です。例として、従来の上位 10 件レポートでは 10 を指定します。
- `rankBy` — **データフィールド**の 0 開始のインデックスです。このデータフィールドの値に基づいて項目をランク付けします。項目をフィールド自体でランク付けする場合は -1 を渡します。
ランキングの基準には値フィールドまたはフィールド自体を使用できます。以下に、2 つの代表的なバリエーションを示します。

### **値フィールドによるランク付け**
行フィールドの項目を、`Sum of Sales` のような通常の値フィールドでランク付けします。次の例では、行フィールド (`Sport`) とデータフィールド (`Sales`) を 1 つずつ持つピボットテーブルを作成し、販売数の上位 2 件のスポーツカテゴリを表示します。`Sum of Sales` はインデックス 0 のデータフィールドであるため、`rankBy` は 0 です。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // 「Sales の合計」で上位2項目を表示する（データフィールドのインデックスは0）
    sportField.Top10AutoShow(true, true, 2, 0);
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-by-value-field.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### **フィールド自体によるランク付け**
フィールド自体に基づいてフィールドをランク付けすることもできます。この場合、`rankBy` として -1 を渡します。このバリエーションでは追加のデータフィールドは不要で、フィールドを行（または列）領域に配置するだけです。次の例では、フィールド自体でランク付けした下位 3 件のスポーツカテゴリを示します。この設定を保存すると、-1 がピボットテーブル形式の既定値であるため、ピボットテーブル XML から `rankBy` 属性が省略されます。また、`GetTop10AutoShowSettings().GetRankBy()` は -1 を返します。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // フィールド自体でランク付けされた下位3項目を表示（rankBy = -1）
    sportField.Top10AutoShow(true, false, 3, -1);
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-by-field-itself.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **現在のオプションの読み取り (GetTop10AutoShowSettings)**
`PivotField.GetTop10AutoShowSettings()` メソッドは、フィールドに現在保存されている自動表示オプションを提供する `PivotFieldTop10AutoShowSettings` オブジェクトを返します。これを使用すると、既存のワークブックや、設定したばかりのピボットテーブルで項目がどのように表示されるかを確認できます。ファイルから読み込んだワークブックも対象です。

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"output-top10-by-value-field.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(0).GetPivotTables().Get(0);
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    PivotFieldTop10AutoShowSettings settings = sportField.GetTop10AutoShowSettings();
    std::cout << "AutoShow enabled: " << settings.IsAutoShow() << std::endl;
    std::cout << "Direction: " << (settings.IsTop() ? "Top" : "Bottom") << std::endl;
    std::cout << "Item count: " << settings.GetAutoShowCount() << std::endl;
    std::cout << "Ranking data field index: " << settings.GetRankBy() << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

4 つのメンバーは、ピボットテーブル XML に書き込まれる従来の自動表示属性 (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`) と対応しています。読み戻した値は、どの Excel バージョンでも有効となります。

## **注記**

{{% alert color="primary" %}}
- `PivotField` の直接のプロパティである `IsAutoShow`、`IsAscendShow`、`GetAutoShowCount` および `GetAutoShowField` は非推奨です。代わりに `PivotFieldTop10AutoShowSettings` オブジェクトを使用してください。`IsAutoShow` は `GetTop10AutoShowSettings().IsAutoShow()` に、`IsAscendShow` は `GetTop10AutoShowSettings().IsTop()` に、`GetAutoShowCount` は `GetTop10AutoShowSettings().GetAutoShowCount()` に、`GetAutoShowField` は `GetTop10AutoShowSettings().GetRankBy()` に相当します。設定を変更するには、サポートされている `Top10AutoShow()` メソッドを使用してください。
- `Top10AutoShow` は行フィールドと列フィールドで機能します。項目がピボットテーブルの本体領域に配置されていないため、ページ（フィルター）領域にのみ置かれたフィールドは、この方法ではランク付けできません。
{{% /alert %}}

## **Excel 2007-365: 上位 10 件フィルター (FilterTop10)**
新しいバージョンの Excel では、フィールドメニューの「値フィルター」→「上位 10 件...」で上位 10 件の値フィルターを利用できます。Aspose.Cells では、この機能に対応する `PivotField.FilterTop10(int32_t valueFieldIndex, PivotFilterType type, bool isTop, int32_t itemCount)` メソッドが、作成された `PivotFilter` を返します。
- `valueFieldIndex` — 集計値に基づいて項目をランク付けするデータフィールドの 0 開始のインデックス。
- `type` — `itemCount` の意味を定義します。`PivotFilterType::Count` は固定された項目数を保持します（ダイアログの「項目」オプション）。`PivotFilterType::Percent` は項目の一定パーセントを保持します。そのため、`itemCount` はパーセント値そのものになり、30 を指定すると上位 30 パーセントの項目を保持します。`PivotFilterType::Sum` は累積値によるカバレッジに基づいて項目をランク付けします。
- `isTop` — `true` の場合は上位、`false` の場合は下位です。
- `itemCount` — 上位 N 件における N を表します。単位は `type` によって異なります。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // 上位10件のフィルター — 「Sales の合計」（データフィールドインデックス 0）に基づいて上位2項目を維持します
    PivotFilter filter = sportField.FilterTop10(0, PivotFilterType::Count, true, 2);
    // パーセントベースのフィルターを使用する場合は、項目の上位30%を維持します:
    // sportField.FilterTop10(0, PivotFilterType::Percent, true, 30);
    pivotTable.GetPivotCache().Refresh();
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-filter.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}
`Top10AutoShow` と `FilterTop10` は 2 つの独立した機能です。`Top10AutoShow` はピボットフィールドに設定された従来の `autoShow` 属性を書き込み、Excel 97 以降のすべての Excel バージョンで有効になります。`FilterTop10` は新しい `PivotFilter` エントリを書き込むため、Excel 2007 以降が必要です。古い Excel バージョンでワークブックを開くと、この新しいフィルターを使用するピボットテーブルは、すべての項目を表示します。レガシーツールとの往復処理が必要なドキュメントでは `Top10AutoShow` を優先してください。また、新しい Excel のワークブックでは、`FilterTop10` は他の値フィルターと併用できるため、優先してください。
{{% /alert %}}

## **関連記事**
- [ラベルまたは値によるピボットテーブルのフィルター](/cells/ja/cpp/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルに行フィールドと列フィールドを追加](/cells/ja/cpp/pivot-table-add-row-and-column-fields/)
- [ピボットテーブルでピボットフィールドをグループ化](/cells/ja/cpp/group-pivot-fields-in-the-pivot-table/)
- [ピボットテーブルの更新](/cells/ja/cpp/refresh-pivot-table/)
- [ピボットテーブルにページフィールドを追加](/cells/ja/cpp/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="cpp" >}}