---
title: Aspose.Cells for C++ でのスパークライン
linktitle: スパークライン
description: Aspose.Cells はスプレッドシートファイルを扱うための C++ ライブラリで、ワークシートのセル内に配置するミニチュアグラフであるスパークラインの作成をサポートしています。この記事では、Aspose.Cells ライブラリを使用して、折れ線、縦棒、勝敗の各スパークラインを追加およびカスタマイズする方法を説明します。
keywords: Aspose.Cells, C++ ライブラリ, スプレッドシート, スパークライン, 折れ線スパークライン, 縦棒スパークライン, 勝敗スパークライン, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ja/cpp/creating-sparklines/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells はワークシートのセル内にスパークラインを作成することをサポートしています。スパークラインとは、単一セル内に収まるミニチュアグラフであり、データ傾向を素早く視覚的に表現するためのものです。Aspose.Cells は折れ線、縦棒、勝敗のスパークラインをサポートしており、それぞれを色、線の太さ、高値/安値ポイント、マーカーに関してカスタマイズできます。

{{% /alert %}}

## **はじめに**

スパークラインはセル内に収まる小さなグラフで、行や列のデータの隣に完全なグラフのスペースを取らずに迅速な傾向を表示したい場合に便利です。Excel は **折れ線**、**縦棒**、**勝敗** の 3 種類のスパークラインをサポートしています。Aspose.Cells は、`Aspose.Cells.Charts` 名前空間にある `SparklineGroup` および `SparklineGroupCollection` API を通じてこの機能を提供します。

Aspose.Cells では、追加するすべてのスパークラインは `worksheet.SparklineGroups.Add(...)` を通じて作成され、`SparklineGroup` オブジェクトを返します。その後、そのオブジェクトを使用してスパークラインの種類、データ範囲、出力先セル、線の色、線の太さ、マーカー、高値/安値ポイントインジケーターなどの視覚的プロパティを設定できます。

{{% alert color="primary" %}}

単一の `SparklineGroup` には、同じスタイルを共有する 1 つ以上のスパークラインを含めることができます。`Add` を呼び出して 1 行のデータと 1 つの出力先セルを渡すと、そのセル内に 1 つのスパークラインが作成されます。出力先範囲が 1 セルより広い場合、各出力先セルに個別のスパークラインが描画され、すべて同じスタイルとデータ範囲が使用されます。

{{% /alert %}}

この記事を通じて、Aspose.Cells がサポートする 3 種類のスパークライン — **折れ線**、**縦棒**、**勝敗** — のそれぞれを順に説明し、追加方法、色のカスタマイズ方法、結果として得られるワークブックの保存方法を紹介します。

## **折れ線スパークライン**

折れ線スパークラインは、系列内のデータポイントを通る連続した線を描画するため、時間の経過に伴う傾向を示すための最も自然な選択肢です。Aspose.Cells では、`SparklineType.Line` を `SparklineGroups.Add` メソッドに渡すことで折れ線スパークラインを作成します。

ワークフローは他のスパークライン種類と同じです:

1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. ソースデータの 1 行 (たとえば、1 行目の A 列から E 列) を可視化したい値で埋めます。
3. スパークラインが描画される出力先セルを記述する `CellArea` を作成します。
4. `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)` を呼び出します。3 番目の引数 `false` は、データ範囲が横方向 (行) であり、縦方向 (列) ではないことを Aspose.Cells に伝えます。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズします。折れ線スパークラインの場合、`group.Line.Color` (これは `Aspose.Cells.Drawing` の `CellsColor` を必要とします) を使用して線の色を設定したり、線の太さを調整したり、高値/安値ポイントマーカーを切り替えたりできます。
6. ワークブックを保存します。

次の例では、ワークブックを作成し、セル A1 から E1 に値 5、-3、8、-2、6 を書き込み、それらの値をトレースする折れ線スパークラインをセル F1 に追加します。また、線の色を赤にカスタマイズし、高値および安値のマーカーを有効化します。

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // ステップ1: Workbookを作成し、最初のワークシートを取得する
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // ステップ2: サンプル値 5、-3、8、-2、6 をセル A1:E1 に書き込む
    cells.Get(u"A1").PutValue(5);
    cells.Get(u"B1").PutValue(-3);
    cells.Get(u"C1").PutValue(8);
    cells.Get(u"D1").PutValue(-2);
    cells.Get(u"E1").PutValue(6);

    // ステップ3: 出力先のセル F1 を指す CellArea を作成する
    CellArea dest;
    dest.StartColumn = 5;   // 列 F（0から始まるインデックス）
    dest.EndColumn = 5;
    dest.StartRow = 0;      // 行 1（0から始まるインデックス）
    dest.EndRow = 0;

    // ステップ4: A1:E1 から F1 への折れ線スパークラインを追加する
    int index = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(index);

    // ステップ5: 赤い CellsColor を作成し、スパークラインの色として設定する
    CellsColor red = workbook.CreateCellsColor();
    red.SetColor(Color::Red());
    group.SetSeriesColor(red);

    // ステップ6: 高値と安値のマーカーを有効にする
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);

    // ステップ7: ワークブックを保存する
    workbook.Save(u"output_line.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **縦棒スパークライン**

縦棒スパークラインは各データポイントを縦棒としてレンダリングします。そのため、大きさ (マグニチュード) が意味を持つデータ、たとえば月次売上数値やカウントなどに適しています。Aspose.Cells では、`SparklineType.Column` を `SparklineGroups.Add` メソッドに渡すことで縦棒スパークラインを作成します。

手順は折れ線スパークラインの例と同じです:

1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. 同じソース範囲 (A1:E1) を可視化したい値で埋めます。
3. 出力先セルを記述する `CellArea` を作成します。
4. `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)` を呼び出します。
5. 必要に応じて、結果として得られた `SparklineGroup` をカスタマイズします。たとえば、`group.Type` を設定して種類を確認したり、棒の色を調整したりします。
6. ワークブックを別の出力ファイルに保存し、折れ線スパークラインの例を上書きしないようにします。

次の例では、A1:E1 に値 5、-3、8、-2、6 を書き込み、F1 に縦棒スパークラインをレンダリングします。負の値は下向きの棒として描画され、正の値は上向きの棒として描画されるため、プラスとマイナスの寄与を一目で簡単に識別できます。

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // ステップ1: Workbookを作成し、最初のワークシートを取得する
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // ステップ2: サンプル値をA1:E1に書き込む
    int values[5] = { 5, -3, 8, -2, 6 };
    Cells cells = worksheet.GetCells();
    for (int i = 0; i < 5; i++) {
        cells.Get(0, i).PutValue(values[i]);
    }

    // ステップ3: F1を指すCellAreaを構築する (列インデックス5、行インデックス0)
    CellArea dest;
    dest.StartColumn = 5;
    dest.EndColumn = 5;
    dest.StartRow = 0;
    dest.EndRow = 0;

    // ステップ4: 宛先セルにColumnスパークラインを追加する
    int idx = worksheet.GetSparklineGroups().Add(
        SparklineType::Column, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(idx);

    // ステップ5: group.Typeを読み取ってスパークラインの種類を確認する
    std::cout << "Sparkline Type added: " << static_cast<int>(group.GetType()) << std::endl;

    // ステップ6: ワークブックを保存する
    wb.Save(u"output_column.xlsx");

    std::cout << "Workbook saved as output_column.xlsx" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **勝敗スパークライン**

勝敗スパークラインは、2 つの結果のみを示すように設計された縦棒スパークラインの特別なバリエーションです。正の値は「上」棒 (勝ち) として描画され、ゼロまたは負の値は「下」棒 (負け) として描画されます。勝敗スパークラインは、勝ち負けのシーケンス、合格/不合格の結果、または時間に伴う任意の二項結果の可視化によく使用されます。

Aspose.Cells では、`SparklineType.Stacked` を `SparklineGroups.Add` メソッドに渡すことで勝敗スパークラインを作成します。(名前にもかかわらず、`SparklineType.Stacked` は勝敗レンダリングを要求するために使用される列挙値です。)

手順は他の 2 種類と同じです:

1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. ソース範囲を埋めます。勝敗スパークラインはすべての値を勝ちまたは負けのいずれかとして扱うため、値そのものの大きさは重要ではなく、符号のみが重要です。正の値は上棒になり、非正の値は下棒になります。
3. 出力先セルを記述する `CellArea` を作成します。
4. `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)` を呼び出します。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズします。たとえば、勝ち棒と負け棒のアクセントカラーを設定します。
6. ワークブックを別のファイル名で保存し、3 つのすべての例がディスク上に共存できるようにします。

次の例では、前の 2 つのセクションと同じ入力データを使用します。値 5、-3、8、-2、6 は勝ち、負け、勝ち、負け、勝ちとして解釈され、F1 に描画されるスパークラインはそのパターンを正確に反映します。

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // ステップ1: ワークブックを作成し、最初のワークシートを取得する
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"WinLoss");

    // ステップ2: 1行目にサンプルデータを入力する: A1=5, B1=-3, C1=8, D1=-2, E1=6
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    // ステップ3: F1を指すCellAreaを構築する（列5、行0）
    CellArea dest;
    dest.StartColumn = 5;   // F
    dest.EndColumn = 5;
    dest.StartRow = 0;      // 1行目
    dest.EndRow = 0;

    // ステップ4: Win/Lossスパークラインを追加する（SparklineType.Stacked）
    int groupIndex = worksheet.GetSparklineGroups().Add(
        SparklineType::Stacked,
        u"A1:E1",
        false,
        dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(groupIndex);

    // ステップ5: スパークライングループをカスタマイズする
    // 高値マーカーと安値マーカーを有効にする
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.SetShowNegativePoints(true);

    // 高値の色を緑に設定する
    CellsColor highColor = workbook.CreateCellsColor();
    highColor.SetColor(Color::Green());
    group.SetHighPointColor(highColor);

    // 安値の色を赤に設定する
    CellsColor lowColor = workbook.CreateCellsColor();
    lowColor.SetColor(Color::Red());
    group.SetLowPointColor(lowColor);

    // 負値の色をオレンジに設定する
    CellsColor negColor = workbook.CreateCellsColor();
    negColor.SetColor(Color::Orange());
    group.SetNegativePointsColor(negColor);

    // デフォルトの系列色を設定する（陽性バーに使用される）
    CellsColor seriesColor = workbook.CreateCellsColor();
    seriesColor.SetColor(Color::SteelBlue());
    group.SetSeriesColor(seriesColor);

    // ステップ6: ワークブックを保存する
    workbook.Save(u"output_winloss.xlsx");

    std::cout << "Workbook saved successfully: output_winloss.xlsx" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **3 種類のスパークラインの組み合わせ**

前の 3 つの例ではそれぞれ独自のワークブックを生成するため、出力ファイルを個別に簡単に確認できます。ただし実際のシナリオでは、複数のデータ系列を並べて比較したい場合が多くあります。これを行う最もクリーンな方法は、複数のスパークライングループを同じワークシート内に配置し、各グループが異なるスタイルをレンダリングすることです。

同じ `SparklineGroupCollection` に複数の `SparklineGroup` オブジェクトを追加でき、各グループは異なる出力先セルまたは異なる範囲を対象とすることができます。たとえば、F1 に折れ線スパークライン、F2 に縦棒スパークライン、F3 に勝敗スパークラインを配置し、すべて 1 行目の同じソースデータを読み取るようにすると、閲覧者は同じ数値の 3 つの異なる視覚的表現を見ることができます。

次の組み合わせ例では、単一のワークブックを作成し、1 行目に値 5、-3、8、-2、6 を入力し、セル F1、F2、F3 に 3 つのスパークライングループ (各種類 1 つずつ) を追加します。これにより、結果として得られるファイルが 3 つのスパークラインスタイルすべてを一度に示します。

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // ステップ1: ワークブックを作成し、最初のワークシートを取得する
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // ステップ2: 1行目(A1:E1)にサンプルデータを入力する
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    // ステップ3: F1にラインヒストグラムグループを追加する
    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, lineArea);
    SparklineGroup lineGroup = worksheet.GetSparklineGroups().Get(lineIdx);

    // CellsColorを介してラインヒストグラムの色をカスタマイズする
    CellsColor lineColor = workbook.CreateCellsColor();
    lineColor.SetColor(Color::Blue());
    lineGroup.SetSeriesColor(lineColor);

    // ステップ4: F2にカラムヒストグラムグループを追加する
    CellArea columnArea;
    columnArea.StartColumn = 5;
    columnArea.EndColumn = 5;
    columnArea.StartRow = 1;
    columnArea.EndRow = 1;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, u"A1:E1", false, columnArea);
    SparklineGroup columnGroup = worksheet.GetSparklineGroups().Get(columnIdx);

    // カラムヒストグラムの系列色をカスタマイズする
    CellsColor columnColor = workbook.CreateCellsColor();
    columnColor.SetColor(Color::Green());
    columnGroup.SetSeriesColor(columnColor);

    // ステップ5: F3にWin/Loss(積み上げ)ヒストグラムグループを追加する
    CellArea stackedArea;
    stackedArea.StartColumn = 5;
    stackedArea.EndColumn = 5;
    stackedArea.StartRow = 2;
    stackedArea.EndRow = 2;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, u"A1:E1", false, stackedArea);
    SparklineGroup stackedGroup = worksheet.GetSparklineGroups().Get(stackedIdx);

    // Win/Lossヒストグラムの系列色をカスタマイズする
    CellsColor stackedColor = workbook.CreateCellsColor();
    stackedColor.SetColor(Color::FromArgb(0xFF8C00));
    stackedGroup.SetSeriesColor(stackedColor);

    // ステップ6: ワークブックを保存する
    workbook.Save(u"output_all.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

単一のワークシートに複数のスパークライングループを組み合わせる場合、各グループは独立しています。同じソース範囲を共有することも、異なるソース範囲を使用することもでき、個別にスタイルを設定できます。これにより、既存のワークシート内に直接、セルの可視化の小さな「ダッシュボード」を簡単に構築できます。

{{% /alert %}}

## **スパークラインの外観のカスタマイズ**

`SparklineGroup` が作成されて `worksheet.SparklineGroups` に追加された後、ワークブックを保存する前に、いくつかの視覚的プロパティを読み取ったり変更したりできます。最も一般的にカスタマイズされるプロパティは次のとおりです:

- **`group.Type`** — `SparklineType` (折れ線、縦棒、または Stacked)。グループは追加時に設定されますが、読み戻して確認することができます。
- **`group.Line.Color`** — 線の色で、`workbook.CreateCellsColor()` を通じて作成される `CellsColor` として表現されます。これは、折れ線スパークラインの線の色を設定するために使用するプロパティです。
- **`group.Line.Weight`** — ポイント単位の線の太さ。値が大きいほど、太い線になります。
- **高値/安値ポイントマーカー** — 最高および最低データポイントに小さなマーカーをオンにするフラグで、極端な値を強調するのに役立ちます。
- **最初/最後/負のポイントマーカー** — 最初、最後、および負のデータポイントにマーカーを切り替えるフラグ。

色を変更するには、常に `CellsColor` インスタンスを作成し、関連するプロパティに割り当ててください。生のカラー値を直接スパークラインの色プロパティに代入しないでください。これらは `Aspose.Cells.Drawing` の `CellsColor` 型を必要とします。`SparklineGroups.Add` メソッド自体は完全に型指定された `SparklineGroup` オブジェクトを返すため、戻り値にプロパティ代入をチェーンしたり、ローカル変数に保存して保存前にカスタマイズしたりできます。



{{< app/cells/assistant language="cpp" >}}