---
title: Aspose.Cells for C++ でのスパークライン
linktitle: Aspose.Cells for C++ でのスパークライン
description: Aspose.Cells はスプレッドシートファイルを扱うための C++ ライブラリで、ワークシートセル内に配置されるミニチュアグラフであるスパークラインの作成をサポートします。この記事では、Aspose.Cells ライブラリを使用して、折れ線、縦棒、勝敗スパークラインを追加およびカスタマイズする方法について説明します。
keywords: Aspose.Cells, C++ ライブラリ, スプレッドシート, スパークライン, 折れ線スパークライン, 縦棒スパークライン, 勝敗スパークライン, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ja/cpp/creating-sparklines/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ワークシートセル内にスパークラインを作成することをサポートします。スパークラインは単一のセルに収まるミニチュアグラフであり、データ傾向の迅速な視覚的表現を提供します。Aspose.Cells は折れ線、縦棒、勝敗スパークラインをサポートし、それぞれを色、線の太さ、高値/安値ポイント、マーカーに関してカスタマイズできます。

## **はじめに**
スパークラインはセル内の小さなグラフであり、完全なグラフのスペースを取らずに行または列のデータの隣に迅速な傾向を表示したい場合に役立ちます。Excel は **折れ線**、**縦棒**、**勝敗** の 3 種類のスパークラインをサポートします。Aspose.Cells は `Aspose.Cells.Charts` 名前空間にある `SparklineGroup` および `SparklineGroupCollection` API を通じてこの機能を再現しています。
Aspose.Cells では、追加するすべてのスパークラインが `worksheet.SparklineGroups.Add(...)` を通じて作成され、これは `SparklineGroup` オブジェクトを返します。そのオブジェクトを使用して、スパークラインのタイプ、データ範囲、配置先セル、および線の色、線の太さ、マーカー、高値/安値ポイントインジケーターなどの視覚的プロパティを設定できます。
本記事では、Aspose.Cells がサポートする 3 つのスパークラインタイプである **折れ線**、**縦棒**、**勝敗** のそれぞれについて、その追加方法、色のカスタマイズ方法、結果として得られるワークブックの保存方法を説明します。

## **折れ線スパークライン**
折れ線スパークラインは、データ系列内のデータ点を通る連続した線を描画し、時間の経過に伴う傾向を示すための最も自然な選択肢です。Aspose.Cells では、`SparklineGroups.Add` メソッドに `SparklineType.Line` を渡すことで折れ線スパークラインが作成されます。
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. 視覚化したい値を含むソースデータの行 (たとえば 1 行目、A 列から E 列) を入力します。
3. スパークラインが描画される配置先セルを記述する `CellArea` を構築します。
4. `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)` を呼び出します。3 番目の引数である `false` は、データ範囲が水平 (行) であり垂直 (列) ではないことを Aspose.Cells に伝えます。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズします。折れ線スパークラインの場合、`group.Line.Color` を使用して線の色を設定し (`Aspose.Cells.Drawing` の `CellsColor` を期待します)、線の太さを調整し、高値/安値ポイントのマーカーを切り替えることができます。
6. ワークブックを保存します。
次の例は、ワークブックを作成し、セル A1 から E1 に値 5、-3、8、-2、6 を書き込み、それらの値をトレースする折れ線スパークラインをセル F1 に追加します。また、線の色を赤にカスタマイズし、高値および安値のポイントのマーカーを有効にします。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // ステップ 1: Workbookを作成し、最初のワークシートを取得する
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // ステップ 2: セル A1:E1 にサンプル値 5, -3, 8, -2, 6 を書き込む
    cells.Get(u"A1").PutValue(5);
    cells.Get(u"B1").PutValue(-3);
    cells.Get(u"C1").PutValue(8);
    cells.Get(u"D1").PutValue(-2);
    cells.Get(u"E1").PutValue(6);
    // ステップ 3: 配置先のセル F1 を指す CellArea を作成する
    CellArea dest;
    dest.StartColumn = 5;   // 列 F (0から始まるインデックス)
    dest.EndColumn = 5;
    dest.StartRow = 0;      // 行 1 (0から始まるインデックス)
    dest.EndRow = 0;
    // ステップ 4: A1:E1 から F1 への折れ線スパークラインを追加する
    int index = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(index);
    // ステップ 5: 赤い CellsColor を作成し、スパークラインの色として設定する
    CellsColor red = workbook.CreateCellsColor();
    red.SetColor(Color::Red());
    group.SetSeriesColor(red);
    // ステップ 6: 高値マーカーと安値マーカーを有効化する
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    // ステップ 7: ワークブックを保存する
    workbook.Save(u"output_line.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **縦棒スパークライン**
縦棒スパークラインは、各データ点を縦棒としてレンダリングします。これにより、大きさが意味を持つデータ (たとえば、月次売上や個数) に適しています。Aspose.Cells では、`SparklineGroups.Add` メソッドに `SparklineType.Column` を渡すことで縦棒スパークラインを作成します。
手順は折れ線スパークラインの例と同様です:
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
3. ソース範囲に値を入力します。
4. 配置先セルを記述する `CellArea` を構築します。
5. `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)` を呼び出します。
6. 必要に応じて、結果として得られる `SparklineGroup` をカスタマイズします。たとえば、`group.Type` を設定してタイプを確認したり、棒の色を調整したりします。
7. 折れ線スパークラインの例を上書きしないよう、ワークブックを別の出力ファイルに保存します。
次の例は、A1:E1 に値 5、-3、8、-2、6 を書き込み、F1 に縦棒スパークラインをレンダリングします。負の値は下向きの棒として、正の値は上向きの棒として描画されるため、正と負の寄与を一目で簡単に識別できます。

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // ステップ 1: Workbook を作成し、最初のワークシートを取得する
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    // ステップ 2: A1:E1 にサンプルの値を入力する
    int values[5] = { 5, -3, 8, -2, 6 };
    Cells cells = worksheet.GetCells();
    for (int i = 0; i < 5; i++) {
        cells.Get(0, i).PutValue(values[i]);
    }
    // ステップ 3: F1 を指す CellArea を作成する (列インデックス 5、行インデックス 0)
    CellArea dest;
    dest.StartColumn = 5;
    dest.EndColumn = 5;
    dest.StartRow = 0;
    dest.EndRow = 0;
    // ステップ 4: 出力先セルに Column スパークラインを追加する
    int idx = worksheet.GetSparklineGroups().Add(
        SparklineType::Column, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(idx);
    // ステップ 5: group.Type を読み取ってスパークラインの種類を確認する
    std::cout << "Sparkline Type added: " << static_cast<int>(group.GetType()) << std::endl;
    // ステップ 6: ワークブックを保存する
    wb.Save(u"output_column.xlsx");
    std::cout << "Workbook saved as output_column.xlsx" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **勝敗スパークライン**
勝敗スパークラインは、2 つの結果のみを表示するように設計された縦棒スパークラインの特殊なバリエーションです。正の値は「上向き」の棒 (勝) として描画され、ゼロまたは負の値は「下向き」の棒 (敗) として描画されます。勝敗スパークラインは、一連の勝敗、合否結果、または経時的なバイナリ結果を視覚化するために一般的に使用されます。
Aspose.Cells では、`SparklineGroups.Add` メソッドに `SparklineType.Stacked` を渡すことで勝敗スパークラインが作成されます。(名前にもかかわらず、`SparklineType.Stacked` は勝敗レンダリングを要求するために使用される列挙値です。)
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. ソース範囲を入力します。勝敗スパークラインではすべての値が「勝ち」または「負け」として扱われるため、値の大きさは重要ではなく、符号のみが重要です。正の値は上向きの棒になり、非正の値は下向きの棒になります。
3. 配置先セルを記述する `CellArea` を構築します。
4. `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)` を呼び出します。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズします。たとえば、勝ちと負けの棒のアクセントカラーを設定します。
6. 3 つの例すべてがディスク上で共存できるように、ワークブックを別のファイル名で保存します。

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // ステップ 1: Workbook を作成し、最初のワークシートを取得する
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"WinLoss");
    // ステップ 2: 1 行目にサンプルデータを入力する: A1=5, B1=-3, C1=8, D1=-2, E1=6
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);
    // ステップ 3: F1 (列 5、行 0) を指す CellArea を作成する
    CellArea dest;
    dest.StartColumn = 5;   // F
    dest.EndColumn = 5;
    dest.StartRow = 0;      // 行 1
    dest.EndRow = 0;
    // ステップ 4: Win/Loss スパークライン (SparklineType.Stacked) を追加する
    int groupIndex = worksheet.GetSparklineGroups().Add(
        SparklineType::Stacked,
        u"A1:E1",
        false,
        dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(groupIndex);
    // ステップ 5: スパークライン グループをカスタマイズする
    // 最高点マーカーと最低点マーカーを有効にする
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.SetShowNegativePoints(true);
    // 最高点の色を緑に設定する
    CellsColor highColor = workbook.CreateCellsColor();
    highColor.SetColor(Color::Green());
    group.SetHighPointColor(highColor);
    // 最低点の色を赤に設定する
    CellsColor lowColor = workbook.CreateCellsColor();
    lowColor.SetColor(Color::Red());
    group.SetLowPointColor(lowColor);
    // 負の値の色をオレンジに設定する
    CellsColor negColor = workbook.CreateCellsColor();
    negColor.SetColor(Color::Orange());
    group.SetNegativePointsColor(negColor);
    // デフォルトの系列色（正の値のバーに使用）を設定する
    CellsColor seriesColor = workbook.CreateCellsColor();
    seriesColor.SetColor(Color::SteelBlue());
    group.SetSeriesColor(seriesColor);
    // ステップ 6: ワークブックを保存する
    workbook.Save(u"output_winloss.xlsx");
    std::cout << "Workbook saved successfully: output_winloss.xlsx" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **3 つのスパークラインタイプの組み合わせ**
次の組み合わせ例は、単一のワークブックを作成し、1 行目に値 5、-3、8、-2、6 を入力し、セル F1、F2、F3 に 3 つのスパークライングループ (各タイプの 1 つずつ) を追加し、結果として得られるファイルが 3 つのスパークラインスタイルすべてを一度に示すようにします。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // ステップ1: ワークブックを作成し、最初のワークシートを取得します
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // ステップ2: 1行目 (A1:E1) にサンプルデータを入力します
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);
    // ステップ3: F1に折れ線スパークライングループを追加します
    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, lineArea);
    SparklineGroup lineGroup = worksheet.GetSparklineGroups().Get(lineIdx);
    // CellsColor を使用して折れ線スパークラインの色をカスタマイズします
    CellsColor lineColor = workbook.CreateCellsColor();
    lineColor.SetColor(Color::Blue());
    lineGroup.SetSeriesColor(lineColor);
    // ステップ4: F2に縦棒スパークライングループを追加します
    CellArea columnArea;
    columnArea.StartColumn = 5;
    columnArea.EndColumn = 5;
    columnArea.StartRow = 1;
    columnArea.EndRow = 1;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, u"A1:E1", false, columnArea);
    SparklineGroup columnGroup = worksheet.GetSparklineGroups().Get(columnIdx);
    // 縦棒スパークラインのシリーズ色をカスタマイズします
    CellsColor columnColor = workbook.CreateCellsColor();
    columnColor.SetColor(Color::Green());
    columnGroup.SetSeriesColor(columnColor);
    // ステップ5: F3に勝敗(積み上げ)スパークライングループを追加します
    CellArea stackedArea;
    stackedArea.StartColumn = 5;
    stackedArea.EndColumn = 5;
    stackedArea.StartRow = 2;
    stackedArea.EndRow = 2;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, u"A1:E1", false, stackedArea);
    SparklineGroup stackedGroup = worksheet.GetSparklineGroups().Get(stackedIdx);
    // 勝敗スパークラインのシリーズ色をカスタマイズします
    CellsColor stackedColor = workbook.CreateCellsColor();
    stackedColor.SetColor(Color::FromArgb(0xFF8C00));
    stackedGroup.SetSeriesColor(stackedColor);
    // ステップ6: ワークブックを保存します
    workbook.Save(u"output_all.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **スパークライン外観のカスタマイズ**
`SparklineGroup` が作成されて `worksheet.SparklineGroups` に追加されたら、ワークブックを保存する前にその視覚的プロパティのいくつかを読み取ったり変更したりできます。最も一般的にカスタマイズされるプロパティは次のとおりです:
- **`group.Type`** — `SparklineType` (Line、Column、または Stacked)。これはグループが追加されるときに設定されますが、読み戻して確認することができます。
- **`group.Line.Color`** — 線の色で、`workbook.CreateCellsColor()` を介して作成された `CellsColor` として表現されます。これは、折れ線スパークラインの線の色に使用するプロパティです。
- **`group.Line.Weight`** — ポイント単位の線の太さ。値が大きいほど線が太くなります。
- **高値/安値ポイントマーカー** — 最高および最低のデータ点に小さなマーカーをオンにするフラグで、極端な値を強調するのに役立ちます。
- **最初/最後/負のポイントマーカー** — 最初、最後、負のデータ点にマーカーを切り替えるフラグです。
色を変更するには、常に `CellsColor` インスタンスを作成し、関連するプロパティに割り当てます。生のカラー値をスパークラインの色プロパティに直接割り当てないでください。これらは `Aspose.Cells.Drawing` の `CellsColor` 型を期待します。`SparklineGroups.Add` メソッド自体は完全に型付けされた `SparklineGroup` オブジェクトを返すため、戻り値のプロパティ割り当てを連鎖させたり、ローカル変数に格納して保存前にカスタマイズしたりすることができます。
{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}