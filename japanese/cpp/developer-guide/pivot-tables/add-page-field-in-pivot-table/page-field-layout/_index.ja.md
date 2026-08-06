---
title: ピボットテーブルでページフィールドのレイアウトを変更する
linktitle: ピボットテーブルでページフィールドのレイアウトを変更する
description: Aspose.Cells for C++ を使用して、ピボットテーブルのページフィールド領域のレイアウト（表示順、ラップ数、ページフィールドの並び順）を制御する方法を学びます。
keywords: Aspose.Cells, C++ ライブラリ, スプレッドシート, ピボットテーブル, ページフィールド, ページフィールドの順序, ページフィールドのラップ数, ページフィールドの移動
type: docs
weight: 191
url: /ja/cpp/change-page-field-layout/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
この記事は「**ピボットテーブルにページフィールドを追加する**」トピックの続編です。ピボットテーブル上部にあるフィルタコントロールの帯であるページフィールド領域のレイアウト（表示順、ラップ数、フィールドの並び替え）を制御する方法を説明します。
{{% /alert %}}
## **はじめに**
Microsoft Excel のピボットテーブルには、テーブルの行／列／データの本体の上に位置する専用の**ページフィールド領域**があります。この領域は、ページフィールドごとに 1 つずつ配置されたドロップダウンフィルタコントロールの帯として表示され、エンドユーザーは年や地域などの条件によってピボットをスライスするためにクリックします。Aspose.Cells for C++ はこの領域を `PivotTable.PageFields` コレクションでモデル化し、この帯の視覚的なレイアウトを制御する 3 つのプロパティを公開しています。
- `PivotTable.PageFieldOrder`（`Aspose.Cells.PrintOrderType` 値）は、追加のページフィールドを既存のフィールドの*横*に配置するか、*下*に配置するかを決定します。
- `PivotTable.PageFieldWrapCount` は、ラップされる前に行または列ごとに配置されるページフィールドの数を設定します。
- `PivotTable.PageFields.Move(currIndex, destIndex)` は、順序モードを変更せずにページフィールドを並べ替えます。
この記事は、共有データセットに対してこれら 3 つの操作をそれぞれ示す 3 つのコード例を通して説明し、結果として得られるレイアウトを並べて比較できるようにします。
## **ソースデータ**
以下のすべての例では、これらの 8 行の売上データを `PivotData` という名前のワークシートに読み込みます。データには 2 つのページフィールド候補（`Year`、`Region`）、1 つの行フィールド候補（`Fruit`）、および 1 つのメジャー（`Amount`）が含まれており、ページフィールドの帯を調査する意味のあるものとなっています。
8 行すべてのデータが、すべてのコード例で同じ順序で設定されています。したがって、ソースデータはシナリオ間で変わることはありません。変わるのはページフィールドのレイアウトプロパティだけです。
## **例 1: Over Then Down**
最初のシナリオでは、2 つのページフィールド（`Year`、`Region`）をピボットテーブル上部の**1 行に横並びで**表示するように設定します。`Fruit` を行軸に割り当て、`Year` を最初に、`Region` を 2 番目にページ軸に配置し（`AddFieldToArea` 呼び出しの順序が開始インデックスを決定します）、`Amount`（Sum）をデータフィールドとして追加します。そして、`PageFieldOrder` を `PrintOrderType.OverThenDown` に、`PageFieldWrapCount` を `2` に設定します。`OverThenDown` でラップ数が 2 の場合、2 つのページフィールドはピボットテーブル上部の 1 つの行に水平方向に横並びで配置されるため、帯は幅 2 の 1 行を占めます。
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

    // 1行目：Apple, 2022, North, 150
    pivotDataCells.Get(1, 0).PutValue(u"Apple");
    pivotDataCells.Get(1, 1).PutValue(2022);
    pivotDataCells.Get(1, 2).PutValue(u"North");
    pivotDataCells.Get(1, 3).PutValue(150);

    // 2行目：Apple, 2023, North, 180
    pivotDataCells.Get(2, 0).PutValue(u"Apple");
    pivotDataCells.Get(2, 1).PutValue(2023);
    pivotDataCells.Get(2, 2).PutValue(u"North");
    pivotDataCells.Get(2, 3).PutValue(180);

    // 3行目：Banana, 2022, South, 120
    pivotDataCells.Get(3, 0).PutValue(u"Banana");
    pivotDataCells.Get(3, 1).PutValue(2022);
    pivotDataCells.Get(3, 2).PutValue(u"South");
    pivotDataCells.Get(3, 3).PutValue(120);

    // 4行目：Banana, 2023, South, 140
    pivotDataCells.Get(4, 0).PutValue(u"Banana");
    pivotDataCells.Get(4, 1).PutValue(2023);
    pivotDataCells.Get(4, 2).PutValue(u"South");
    pivotDataCells.Get(4, 3).PutValue(140);

    // 5行目：Cherry, 2022, East, 200
    pivotDataCells.Get(5, 0).PutValue(u"Cherry");
    pivotDataCells.Get(5, 1).PutValue(2022);
    pivotDataCells.Get(5, 2).PutValue(u"East");
    pivotDataCells.Get(5, 3).PutValue(200);

    // 6行目：Cherry, 2023, East, 220
    pivotDataCells.Get(6, 0).PutValue(u"Cherry");
    pivotDataCells.Get(6, 1).PutValue(2023);
    pivotDataCells.Get(6, 2).PutValue(u"East");
    pivotDataCells.Get(6, 3).PutValue(220);

    // 7行目：Grape, 2022, West, 90
    pivotDataCells.Get(7, 0).PutValue(u"Grape");
    pivotDataCells.Get(7, 1).PutValue(2022);
    pivotDataCells.Get(7, 2).PutValue(u"West");
    pivotDataCells.Get(7, 3).PutValue(90);

    // 8行目：Grape, 2023, West, 110
    pivotDataCells.Get(8, 0).PutValue(u"Grape");
    pivotDataCells.Get(8, 1).PutValue(2023);
    pivotDataCells.Get(8, 2).PutValue(u"West");
    pivotDataCells.Get(8, 3).PutValue(110);

    // PivotTableReportシートを追加
    Worksheet pivotTableSheet = worksheets.Add(u"PivotTableReport");
    PivotTableCollection pivotTables = pivotTableSheet.GetPivotTables();

    // PivotData!A1:D9をデータソースとし、PivotTableReportのA1に配置するピボットテーブルを作成
    int pivotIndex = pivotTables.Add(u"PivotData!A1:D9", u"A1", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    // フィールドを追加
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);   // Fruit
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);  // Year
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);  // Region
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);  // Amount
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    // ページフィールド領域のレイアウトを設定：ページフィールドを横方向に先に配置し、2つごとに改行する
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
この例では、例 1 とまったく同じように、`Fruit` を行軸に、`Year` と `Region` をページ軸に（`Year` を最初に）、`Amount`（Sum）をデータフィールドとして配置します。次に、`PageFieldOrder` を `PrintOrderType.DownThenOver` に、`PageFieldWrapCount` を `2` に設定します。`DownThenOver` でラップ数が 2 の場合、2 つのページフィールドは垂直方向に積み重ねられ、`Year` が上、`Region` がその直下に配置され、ピボットテーブル上部の 1 つの列を形成します。したがって、帯は例 1 とは対照的に、幅 1 の 2 行を占めます。
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
## **例 3: ページフィールドの移動**
3 番目のシナリオでは、このデータセットとフィールド割り当てを維持し、中立的なレイアウト（ラップ数 `2` の `OverThenDown`）を設定してから、`PageFields.Move` 操作を実演します。`Move(0, 1)` 呼び出しは、インデックス 0（`Year`）のページフィールドを位置 1 に移動し、位置 1（`Region`）にあったページフィールドは位置 0 にシフトします。この呼び出しの後、`Region` が最初のページフィールドになり、`Year` が 2 番目のページフィールドになります。ラップと順序モードは変更されていないため、帯はまだ水平方向に横並びでレンダリングされます。2 つのドロップダウンの順序のみが入れ替わっています。
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
## **関連記事**
- [ピボットテーブルにページフィールドを追加する](/cells/ja/cpp/add-page-field-in-pivot-table/) — ピボットテーブルにページフィールドを追加する方法を説明する親ページです。
- [ピボットテーブルの行フィールドと列フィールド](/cells/ja/cpp/row-and-column-fields/) — ここで示したページ軸の作業を補完する、行軸と列軸へのフィールドの割り当てについて説明します。
- [ピボットテーブルの値フィールドを管理する](/cells/ja/cpp/manage-value-fields/) — この記事で使用されている `Sum` 集計を含む、データ（値）領域の設定方法を説明します。
- [ピボットテーブルを更新する](/cells/ja/cpp/refresh-pivot-table/) — ページフィールドの並べ替え後に必要となる `RefreshData` と `CalculateData` について説明します。
- [ピボットテーブルにスタイルを適用する](/cells/ja/cpp/apply-style-to-pivot-table/) — ページフィールドの帯がレイアウトされた後、レンダリングされたピボットテーブルをフォーマットする方法を示します。
{{< app/cells/assistant language="" >}}