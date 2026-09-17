---
title: ピボットテーブルでページフィールドのレイアウトを変更する
linktitle: ピボットテーブルでページフィールドのレイアウトを変更する
description: Aspose.Cells for C++ を使用して、ピボットテーブル上部のページ フィールドの表示順序、折り返し数、フィールドの順序を設定する方法など、ページ フィールド領域のレイアウトを制御する方法を説明します。
keywords: Aspose.Cells, C++ library, spreadsheet, pivot table, page field, page field order, page field wrap count, move page field
type: docs
weight: 191
url: /ja/cpp/change-page-field-layout/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
この記事は、**ピボットテーブルにページフィールドを追加する**トピックの続きです。ピボットテーブル上部にあるフィルター コントロールの帯であるページ フィールド領域のレイアウトを、表示順序、折り返し数、フィールドの並べ替えを含めて制御する方法を説明します。
{{% /alert %}}

## **Introduction**
Microsoft Excel のピボットテーブルには、テーブルの行/列/データ本体の上にある専用の**ページフィールド領域**があります。この領域は、各ページ フィールドに対応するドロップダウン フィルター コントロールの帯として表示され、エンド ユーザーは年や地域などの条件でピボットをスライスするためにクリックする部分です。Aspose.Cells for C++ はこの領域を `PivotTable.PageFields` コレクションでモデル化し、帯の視覚的なレイアウトを制御する 3 つのプロパティを公開しています。
- `PivotTable.PageFieldOrder`（`Aspose.Cells.PrintOrderType` の値）は、追加のページ フィールドを既存のもの*横*に配置するか、*下*に配置するかを決定します。
- `PivotTable.PageFieldWrapCount` は、折り返しを行う前に 1 行または 1 列に配置するページ フィールドの数を設定します。
- `PivotTable.PageFields.Move(currIndex, destIndex)` は、順序モードを変更せずにページ フィールドの順序を変更します。
この記事では、各操作を共通データセットで実演する 3 つのコード例を取り上げるため、結果として得られるレイアウトを並べて比較できます。

## **Source Data**
| 果物 | 年 | 地域 | 金額 |
|---|---:|---|---:|
| リンゴ | 2022 | 北 | 150 |
| リンゴ | 2023 | 北 | 180 |
| バナナ | 2022 | 南 | 120 |
| バナナ | 2023 | 南 | 140 |
| チェリー | 2022 | 東 | 200 |
| チェリー | 2023 | 東 | 220 |
| ブドウ | 2022 | 西 | 90 |
| ブドウ | 2023 | 西 | 110 |
すべてのコード例には、同一の順序で 8 行のデータが入力されています。そのため、シナリオ間でソースデータが異なることはなく、異なるのはページフィールドのレイアウトプロパティだけです。

## **Example 1: Over Then Down**
最初のシナリオでは、2 つのページフィールド（`Year`、`Region`）がピボットテーブル上部に**1 行に横並び**で表示されるように設定します。`Fruit` を行軸に割り当て、ページ軸では `Year` を最初、`Region` を 2 番目に配置し（`AddFieldToArea` 呼び出しの順序が開始インデックスを決定します）、データフィールドとして `Amount`（`Sum`）を追加します。その後、`PageFieldOrder` を `PrintOrderType.OverThenDown` に設定し、`PageFieldWrapCount = 2` とします。`OverThenDown` と折り返し数 2 を組み合わせると、2 つのページフィールドがピボットテーブル上部の 1 行に横に並んで配置され、帯は 1 行を占め、幅は 2 フィールド分になります。

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
    // Headers (row 0)
    pivotDataCells.Get(0, 0).PutValue(u"Fruit");
    pivotDataCells.Get(0, 1).PutValue(u"Year");
    pivotDataCells.Get(0, 2).PutValue(u"Region");
    pivotDataCells.Get(0, 3).PutValue(u"Amount");
    // Row 1: Apple, 2022, North, 150
    pivotDataCells.Get(1, 0).PutValue(u"Apple");
    pivotDataCells.Get(1, 1).PutValue(2022);
    pivotDataCells.Get(1, 2).PutValue(u"North");
    pivotDataCells.Get(1, 3).PutValue(150);
    // Row 2: Apple, 2023, North, 180
    pivotDataCells.Get(2, 0).PutValue(u"Apple");
    pivotDataCells.Get(2, 1).PutValue(2023);
    pivotDataCells.Get(2, 2).PutValue(u"North");
    pivotDataCells.Get(2, 3).PutValue(180);
    // Row 3: Banana, 2022, South, 120
    pivotDataCells.Get(3, 0).PutValue(u"Banana");
    pivotDataCells.Get(3, 1).PutValue(2022);
    pivotDataCells.Get(3, 2).PutValue(u"South");
    pivotDataCells.Get(3, 3).PutValue(120);
    // Row 4: Banana, 2023, South, 140
    pivotDataCells.Get(4, 0).PutValue(u"Banana");
    pivotDataCells.Get(4, 1).PutValue(2023);
    pivotDataCells.Get(4, 2).PutValue(u"South");
    pivotDataCells.Get(4, 3).PutValue(140);
    // Row 5: Cherry, 2022, East, 200
    pivotDataCells.Get(5, 0).PutValue(u"Cherry");
    pivotDataCells.Get(5, 1).PutValue(2022);
    pivotDataCells.Get(5, 2).PutValue(u"East");
    pivotDataCells.Get(5, 3).PutValue(200);
    // Row 6: Cherry, 2023, East, 220
    pivotDataCells.Get(6, 0).PutValue(u"Cherry");
    pivotDataCells.Get(6, 1).PutValue(2023);
    pivotDataCells.Get(6, 2).PutValue(u"East");
    pivotDataCells.Get(6, 3).PutValue(220);
    // Row 7: Grape, 2022, West, 90
    pivotDataCells.Get(7, 0).PutValue(u"Grape");
    pivotDataCells.Get(7, 1).PutValue(2022);
    pivotDataCells.Get(7, 2).PutValue(u"West");
    pivotDataCells.Get(7, 3).PutValue(90);
    // Row 8: Grape, 2023, West, 110
    pivotDataCells.Get(8, 0).PutValue(u"Grape");
    pivotDataCells.Get(8, 1).PutValue(2023);
    pivotDataCells.Get(8, 2).PutValue(u"West");
    pivotDataCells.Get(8, 3).PutValue(110);
    // Add PivotTableReport sheet
    Worksheet pivotTableSheet = worksheets.Add(u"PivotTableReport");
    PivotTableCollection pivotTables = pivotTableSheet.GetPivotTables();
    // Create pivot table sourced from PivotData!A1:D9 placed at A1 on PivotTableReport
    int pivotIndex = pivotTables.Add(u"PivotData!A1:D9", u"A1", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(pivotIndex);
    // Add fields
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);   // Fruit
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);  // Year
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);  // Region
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);  // Amount
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);
    // Configure page field area layout: place page fields across first, wrap after every 2
    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);
    // Refresh and calculate
    pivotTable.CalculateData();
    // Save
    std::string filePath = dataDir + "/pageFieldLayout_overThenDown.xlsx";
    workbook.Save(U16String(filePath.c_str()));
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Example 2: Down Then Over**
この例では、例 1 とまったく同じように、`Fruit` を行軸に、`Year` と `Region` をページ軸に（`Year` を先頭に）、`Amount`（`Sum`）をデータフィールドとして配置します。その後、`PageFieldOrder` を `PrintOrderType.DownThenOver` に、`PageFieldWrapCount` を `2` に設定します。`DownThenOver` と折り返し数 2 を組み合わせると、2 つのページフィールドが縦に積まれ、`Year` が上、`Region` がそのすぐ下になり、ピボットテーブル上部に 1 列を形成します。したがって、帯は幅 1 の 2 行を占め、例 1 とは対照的です。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
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
    int idx = pivotReport.GetPivotTables().Add(u"PivotData!A1:D9", u"A1", u"PivotTable");
    PivotTable pivotTable = pivotReport.GetPivotTables().Get(idx);
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

## **Example 3: Move a Page Field**
3 番目のシナリオでは、このデータセットとフィールドの配置を維持し、中立的なレイアウト（折り返し数 `2` の `OverThenDown`）を設定してから、`PageFields.Move` 操作を実演します。`Move(0, 1)` 呼び出しは、インデックス 0 のページフィールド（`Year`）を位置 1 に移動し、元々位置 1 にあったページフィールド（`Region`）を位置 0 に移動します。この呼び出しの後、`Region` が最初のページフィールド、`Year` が 2 番目のページフィールドになります。折り返し数と順序モードは変わらないため、帯は依然として横に並んで表示され、2 つのドロップダウンの順序が入れ替わるだけです。

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
    int32_t pivotIndex = pivotSheet.GetPivotTables().Add(u"PivotData!A1:D9", u"A3", u"PivotTable");
    PivotTable pivotTable = pivotSheet.GetPivotTables().Get(pivotIndex);
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

## **Related Articles**
- [Add Page Field in Pivot Table](/cells/ja/cpp/add-page-field-in-pivot-table/) — ピボットテーブルにページ フィールドを追加する方法を紹介する親ページです。
- [Row and Column Fields in Pivot Table](/cells/ja/cpp/row-and-column-fields/) — フィールドを行軸と列軸に割り当てる方法を扱い、ここで示すページ軸の作業を補完します。
- [Manage Value Fields in Pivot Table](/cells/ja/cpp/manage-value-fields/) — データ（値）領域を設定する方法を説明し、この記事で使用する `Sum` 集計を含みます。
- [Refresh Pivot Table](/cells/ja/cpp/refresh-pivot-table/) — ページ フィールドの並べ替え後に必要となる `RefreshData` と `CalculateData` について説明します。
- [Apply Style to Pivot Table](/cells/ja/cpp/apply-style-to-pivot-table/) — ページ フィールドの帯を配置した後で、表示されたピボットテーブルの書式を設定する方法を示します。

{{< app/cells/assistant language="" >}}