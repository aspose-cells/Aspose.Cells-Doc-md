---
title: ピボットテーブルでページフィールドのレイアウトを変更する
linktitle: ピボットテーブルでページフィールドのレイアウトを変更する
description: Aspose.Cells for C++ を使用して、ピボットテーブルのページフィールド領域のレイアウトを制御する方法を学びます。また、ピボットテーブル上部のページフィールドについて、表示順序、折り返し数、およびフィールド順序を設定する方法を説明します。
keywords: Aspose.Cells, C++ ライブラリ, スプレッドシート, ピボットテーブル, ページフィールド, ページフィールドの順序, ページフィールドの折り返し数, ページフィールドの移動
type: docs
weight: 191
url: /ja/cpp/change-page-field-layout/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
本記事は、**ピボットテーブルにページフィールドを追加する**の続きです。ページフィールド領域（ピボットテーブル上部に配置されるフィルターコントロールの帯）のレイアウトを制御する方法を説明します。具体的には、表示順序、折り返し数、およびフィールドの並べ替えを示します。
{{% /alert %}}

## **はじめに**
Microsoft Excel のピボットテーブルには、表の行・列・データ部分の上部に配置される専用の**ページフィールド領域**があります。この領域は、各ページフィールドに対応するドロップダウン型フィルターコントロールの帯として表示され、年や地域などの条件に応じてピボットテーブルのデータを絞り込むために、利用者がクリックする部分です。Aspose.Cells for C++ はこの領域を `PivotTable.PageFields` コレクションとしてモデル化し、帯のレイアウトを制御する 3 つのプロパティを公開します。
- `PivotTable.PageFieldOrder`（`Aspose.Cells.PrintOrderType` の値）は、追加されるページフィールドを既存のフィールドの*横*または*下*に配置するかどうかを決定します。
- `PivotTable.PageFieldWrapCount` は、折り返すまでの 1 行または 1 列に配置するページフィールド数を設定します。
- `PivotTable.PageFields.Move(currIndex, destIndex)` は、順序モードを変更せずにページフィールドを並べ替えます。
本チュートリアルでは、同じデータセットに対してこれら 3 つの操作をそれぞれ示す 3 つのコード例を紹介し、結果のレイアウトを並べて比較できるようにします。

## **ソースデータ**
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
すべてのコード例では、8 行すべてが同一の順序で入力されるため、シナリオ間でソースデータが変化することはありません。変更されるのはページフィールドのレイアウトプロパティだけです。

## **例 1: Over Then Down**
最初のシナリオでは、2 つのページフィールド（`Year`、`Region`）が、ピボットテーブルの上部に**1 行で横並び**になるように構成します。`Fruit` を行軸に割り当て、`Year` を先に、`Region` を次にページ軸に配置します（`AddFieldToArea` 呼び出しの順序によって初期インデックスが決まります）。さらに、`Amount`（`Sum`）をデータフィールドとして追加し、`PageFieldOrder` に `PrintOrderType.OverThenDown` を設定して `PageFieldWrapCount = 2` とします。`OverThenDown` と折り返し数 2 を使用すると、2 つのページフィールドがピボットテーブルの上部の 1 行に横並びで配置されます。そのため、帯は 2 つのページフィールドを収める 1 行として表示されます。

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    std::string dataDir = "output";
    if (!std::filesystem::exists(dataDir)) {
        std::filesystem::create_directories(dataDir);
    }
    Workbook workbook;
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet pivotDataSheet = worksheets.Add(u"PivotData");
    Cells pivotDataCells = pivotDataSheet.GetCells();
    // ヘッダー（0行目）
    pivotDataCells.Get(0, 0).PutValue(u"Fruit");
    pivotDataCells.Get(0, 1).PutValue(u"Year");
    pivotDataCells.Get(0, 2).PutValue(u"Region");
    pivotDataCells.Get(0, 3).PutValue(u"Amount");
    // 1行目: りんご、2022、北、150
    pivotDataCells.Get(1, 0).PutValue(u"Apple");
    pivotDataCells.Get(1, 1).PutValue(2022);
    pivotDataCells.Get(1, 2).PutValue(u"North");
    pivotDataCells.Get(1, 3).PutValue(150);
    // 2行目: りんご、2023、北、180
    pivotDataCells.Get(2, 0).PutValue(u"Apple");
    pivotDataCells.Get(2, 1).PutValue(2023);
    pivotDataCells.Get(2, 2).PutValue(u"North");
    pivotDataCells.Get(2, 3).PutValue(180);
    // 3行目: バナナ、2022、南、120
    pivotDataCells.Get(3, 0).PutValue(u"Banana");
    pivotDataCells.Get(3, 1).PutValue(2022);
    pivotDataCells.Get(3, 2).PutValue(u"South");
    pivotDataCells.Get(3, 3).PutValue(120);
    // 4行目: バナナ、2023、南、140
    pivotDataCells.Get(4, 0).PutValue(u"Banana");
    pivotDataCells.Get(4, 1).PutValue(2023);
    pivotDataCells.Get(4, 2).PutValue(u"South");
    pivotDataCells.Get(4, 3).PutValue(140);
    // 5行目: さくらんぼ、2022、東、200
    pivotDataCells.Get(5, 0).PutValue(u"Cherry");
    pivotDataCells.Get(5, 1).PutValue(2022);
    pivotDataCells.Get(5, 2).PutValue(u"East");
    pivotDataCells.Get(5, 3).PutValue(200);
    // 6行目: さくらんぼ、2023、東、220
    pivotDataCells.Get(6, 0).PutValue(u"Cherry");
    pivotDataCells.Get(6, 1).PutValue(2023);
    pivotDataCells.Get(6, 2).PutValue(u"East");
    pivotDataCells.Get(6, 3).PutValue(220);
    // 7行目: ぶどう、2022、西、90
    pivotDataCells.Get(7, 0).PutValue(u"Grape");
    pivotDataCells.Get(7, 1).PutValue(2022);
    pivotDataCells.Get(7, 2).PutValue(u"West");
    pivotDataCells.Get(7, 3).PutValue(90);
    // 8行目: ぶどう、2023、西、110
    pivotDataCells.Get(8, 0).PutValue(u"Grape");
    pivotDataCells.Get(8, 1).PutValue(2023);
    pivotDataCells.Get(8, 2).PutValue(u"West");
    pivotDataCells.Get(8, 3).PutValue(110);
    // PivotTableReportシートを追加
    Worksheet pivotTableSheet = worksheets.Add(u"PivotTableReport");
    PivotTableCollection pivotTables = pivotTableSheet.GetPivotTables();
    // PivotData!A1:D9をデータ元としてPivotTableReportのA1に配置するピボットテーブルを作成
    PivotTable pivotTable = pivotTables.Add(u"PivotData!A1:D9", 0, 0);
    // フィールドを追加
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);   // フルーツ
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);  // 年
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);  // 地域
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);  // 金額
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);
    // ページフィールド領域のレイアウトを構成：ページフィールドを横に配置し、2個ごとに改行
    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);
    // 更新して計算
    pivotTable.CalculateData();
    // 保存
    std::string filePath = dataDir + "/pageFieldLayout_overThenDown.xlsx";
    workbook.Save(U16String(filePath.c_str()));
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **例 2: Down Then Over**
この例では、例 1 と同様に、`Fruit` を行軸に、`Year` と `Region` をページ軸に（`Year` を先に）、`Amount`（`Sum`）をデータフィールドに配置します。次に、`PageFieldOrder` に `PrintOrderType.DownThenOver` を設定し、`PageFieldWrapCount` を 2 に設定します。`DownThenOver` と折り返し数 2 を使用すると、2 つのページフィールドは `Year` が上、`Region` がその直下に配置され、縦に 2 つ並びます。これにより、ピボットテーブルの上部に 1 列の帯が形成されます。したがって、帯は例 1 とは異なり、1 列幅で 2 行を占めます。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet pivotData = workbook.GetWorksheets().Get(0);
    pivotData.SetName(u"PivotData");
    Worksheet pivotReport = workbook.GetWorksheets().Add(u"PivotTableReport");
    const char* headers[] = { "Fruit", "Year", "Region", "Amount" };
    for (int c = 0; c < 4; c++)
    {
        pivotData.GetCells().Get(0, c).PutValue(U16String(headers[c]));
    }
    struct DataRow {
        U16String fruit;
        int year;
        U16String region;
        int amount;
    };
    DataRow data[] = {
        {U16String("Apple"),  2022, U16String("North"), 150},
        {U16String("Apple"),  2023, U16String("North"), 180},
        {U16String("Banana"), 2022, U16String("South"), 120},
        {U16String("Banana"), 2023, U16String("South"), 140},
        {U16String("Cherry"), 2022, U16String("East"),  200},
        {U16String("Cherry"), 2023, U16String("East"),  220},
        {U16String("Grape"),  2022, U16String("West"),  90},
        {U16String("Grape"),  2023, U16String("West"),  110}
    };
    for (int r = 0; r < 8; r++)
    {
        pivotData.GetCells().Get(r + 1, 0).PutValue(data[r].fruit);
        pivotData.GetCells().Get(r + 1, 1).PutValue(data[r].year);
        pivotData.GetCells().Get(r + 1, 2).PutValue(data[r].region);
        pivotData.GetCells().Get(r + 1, 3).PutValue(data[r].amount);
    }
    PivotTable pivotTable = pivotReport.GetPivotTables().Add(u"PivotData!A1:D9", 0, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);
    pivotTable.SetPageFieldOrder(PrintOrderType::DownThenOver);
    pivotTable.SetPageFieldWrapCount(2);
    pivotTable.CalculateData();
    workbook.Save(u"pageFieldLayout_downThenOver.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **例 3: ページフィールドの移動**
3 番目のシナリオでは、このデータセットとフィールド割り当てを維持し、標準的なレイアウト（`OverThenDown`、折り返し数 `2`）を設定してから、`PageFields.Move` 操作を示します。`Move(0, 1)` を呼び出すと、インデックス 0 にあるページフィールド（`Year`）が位置 1 に移動し、位置 1 にあったページフィールド（`Region`）が位置 0 に移ります。この呼び出し後、`Region` が最初のページフィールドになり、`Year` が 2 番目になります。折り返し設定と順序モードは変更されないため、帯は引き続き横並びで表示されます。変更されるのは、2 つのドロップダウンフィルターコントロールの順序だけです。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet dataSheet = wb.GetWorksheets().Get(0);
    dataSheet.SetName(u"PivotData");
    Cells dataCells = dataSheet.GetCells();
    dataCells.Get(u"A1").PutValue(u"Fruit");
    dataCells.Get(u"B1").PutValue(u"Year");
    dataCells.Get(u"C1").PutValue(u"Region");
    dataCells.Get(u"D1").PutValue(u"Amount");
    dataCells.Get(u"A2").PutValue(u"Apple");
    dataCells.Get(u"B2").PutValue(2022);
    dataCells.Get(u"C2").PutValue(u"North");
    dataCells.Get(u"D2").PutValue(150);
    dataCells.Get(u"A3").PutValue(u"Apple");
    dataCells.Get(u"B3").PutValue(2023);
    dataCells.Get(u"C3").PutValue(u"North");
    dataCells.Get(u"D3").PutValue(180);
    dataCells.Get(u"A4").PutValue(u"Banana");
    dataCells.Get(u"B4").PutValue(2022);
    dataCells.Get(u"C4").PutValue(u"South");
    dataCells.Get(u"D4").PutValue(120);
    dataCells.Get(u"A5").PutValue(u"Banana");
    dataCells.Get(u"B5").PutValue(2023);
    dataCells.Get(u"C5").PutValue(u"South");
    dataCells.Get(u"D5").PutValue(140);
    dataCells.Get(u"A6").PutValue(u"Cherry");
    dataCells.Get(u"B6").PutValue(2022);
    dataCells.Get(u"C6").PutValue(u"East");
    dataCells.Get(u"D6").PutValue(200);
    dataCells.Get(u"A7").PutValue(u"Cherry");
    dataCells.Get(u"B7").PutValue(2023);
    dataCells.Get(u"C7").PutValue(u"East");
    dataCells.Get(u"D7").PutValue(220);
    dataCells.Get(u"A8").PutValue(u"Grape");
    dataCells.Get(u"B8").PutValue(2022);
    dataCells.Get(u"C8").PutValue(u"West");
    dataCells.Get(u"D8").PutValue(90);
    dataCells.Get(u"A9").PutValue(u"Grape");
    dataCells.Get(u"B9").PutValue(2023);
    dataCells.Get(u"C9").PutValue(u"West");
    dataCells.Get(u"D9").PutValue(110);
    Worksheet pivotSheet = wb.GetWorksheets().Add(u"PivotTableReport");
    PivotTable pivotTable = pivotSheet.GetPivotTables().Add(u"PivotData!A1:D9", 2, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);
    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);
    pivotTable.GetPageFields().Move(0, 1);
    pivotTable.CalculateData();
    wb.Save(u"pageFieldLayout_move.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **関連記事**
- [ピボットテーブルにページフィールドを追加する](/cells/ja/cpp/add-page-field-in-pivot-table/) — ページフィールドをピボットテーブルに追加する方法を説明します。
- [ピボットテーブルの行フィールドと列フィールド](/cells/ja/cpp/row-and-column-fields/) — フィールドを行軸と列軸に割り当てる方法を説明し、本記事でのページ軸に関する操作を補完します。
- [ピボットテーブルの値フィールドを管理](/cells/ja/cpp/manage-value-fields/) — この記事で使用する `Sum` 集計を含め、データ（値）領域を設定する方法を説明します。
- [ピボットテーブルの更新](/cells/ja/cpp/refresh-pivot-table/) — ページフィールドを並べ替えた後に必要となる `RefreshData` と `CalculateData` について説明します。
- [ピボットテーブルにスタイルを適用](/cells/ja/cpp/apply-style-to-pivot-table/) — ページフィールドの帯を配置した後、表示されたピボットテーブルに書式設定を適用する方法を説明します。

{{< app/cells/assistant language="cpp" >}}