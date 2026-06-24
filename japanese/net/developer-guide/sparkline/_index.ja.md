---
title: Aspose.Cells for .NET でのスパークライン
linktitle: Sparklines
description: Aspose.Cells はスプレッドシートファイルを扱うための .NET ライブラリであり、ワークシートセル内に配置するミニチュアチャートであるスパークラインの作成をサポートしています。この記事では、Aspose.Cells ライブラリを使用して、折れ線、列、勝敗の各スパークラインを追加しカスタマイズする方法について説明します。
keywords: Aspose.Cells, .NET library, spreadsheet, sparklines, line sparkline, column sparkline, win/loss sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ja/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は、ワークシートセル内のスパークライン作成をサポートしています。スパークラインとは 1 つのセル内に収まるミニチュアチャートであり、データ傾向を素早く視覚的に表現します。Aspose.Cells は折れ線、列、勝敗のスパークラインをサポートしており、それぞれを色、線の太さ、高値/安値ポイント、マーカーなどについてカスタマイズできます。

{{% /alert %}}

## **はじめに**

スパークラインとはセル内に収まる小さなチャートであり、データ行や列の隣に完全なチャートほどのスペースを取らずに素早く傾向を表示したい場合に便利です。Excel は **折れ線**、**列**、**勝敗** の 3 種類のスパークラインをサポートしています。Aspose.Cells は `Aspose.Cells.Charts` 名前空間にある `SparklineGroup` および `SparklineGroupCollection` API を通じてこの機能を提供します。

Aspose.Cells では、追加するすべてのスパークラインが `worksheet.SparklineGroups.Add(...)` を通じて作成され、これは `SparklineGroup` オブジェクトを返します。そのオブジェクトを使用して、スパークラインの種類、データ範囲、出力先セル、線の色、線の太さ、マーカー、高値/安値ポイント表示などの視覚的なプロパティを設定できます。

{{% alert color="primary" %}}

1 つの `SparklineGroup` は、同じスタイルを共有する 1 つ以上のスパークラインを含むことができます。`Add` を呼び出して 1 行のデータと 1 つの出力先セルを渡すと、そのセル内に 1 つのスパークラインが作成されます。出力先範囲が 1 セルより広い場合、各出力先セルに個別のスパークラインが描画され、すべて同じスタイルとデータ範囲を使用します。

{{% /alert %}}

この記事を通じて、Aspose.Cells でサポートされている 3 種類のスパークライン — **折れ線**、**列**、**勝敗** — それぞれについて、追加方法、色のカスタマイズ、結果として得られるワークブックの保存方法を説明します。

## **折れ線スパークライン**

折れ線スパークラインは、系列内のデータポイントを結ぶ連続した線を描画するため、時系列での傾向を示すのに最も自然な選択肢です。Aspose.Cells では、`SparklineType.Line` を `SparklineGroups.Add` メソッドに渡すことで折れ線スパークラインが作成されます。

ワークフローは他のスパークライン種類と同じです。

1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. 視覚化したい値をソースデータの 1 行 (たとえば 1 行目、A 列から E 列) に入力します。
3. スパークラインが描画される出力先セルを表す `CellArea` を構築します。
4. `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)` を呼び出します。3 番目の引数である `false` は、データ範囲が縦 (列) ではなく横 (行) であることを Aspose.Cells に伝えます。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズします。折れ線スパークラインでは、`group.Line.Color` (これは `Aspose.Cells.Drawing` の `CellsColor` を必要とします) を使用して線の色を設定したり、線の太さを調整したり、高値/安値ポイントマーカーを切り替えたりできます。
6. ワークブックを保存します。

次の例では、ワークブックを作成し、セル A1 から E1 に値 5、-3、8、-2、6 を書き込み、セル F1 にこれらの値をトレースする折れ線スパークラインを追加します。また、線の色を赤にカスタマイズし、高値および安値ポイントのマーカーを有効化します。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;

namespace SparklineDemo
{
    public class Program
    {
        public static void Main()
        {
            // ステップ 1: Workbook を作成し、最初のワークシートを取得します
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            Cells cells = worksheet.Cells;

            // ステップ 2: サンプル値 5、-3、8、-2、6 をセル A1:E1 に書き込みます
            cells["A1"].PutValue(5);
            cells["B1"].PutValue(-3);
            cells["C1"].PutValue(8);
            cells["D1"].PutValue(-2);
            cells["E1"].PutValue(6);

            // ステップ 3: コピー先セル F1 を指す CellArea を作成します
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // 列 F (0 インデックス)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // 行 1 (0 インデックス)
            dest.EndRow = 0;

            // ステップ 4: A1:E1 から F1 に折れ線スパークラインを追加します
            // SparklineGroups.Add は新しく追加されたグループのインデックスを返します
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];

            // ステップ 5: 赤色の CellsColor を作成し、スパークラインの線の色に割り当てます
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;

            // ステップ 6: 高値マーカーと低値マーカーを有効にします
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;

            // ステップ 7: ワークブックを保存します
            workbook.Save("output_line.xlsx");
        }
    }
}
```

## **列スパークライン**

列スパークラインは、各データポイントを縦棒としてレンダリングします。これは、データの大きさが意味を持つ場合、たとえば月次の売上高や件数などによく適しています。Aspose.Cells では、`SparklineType.Column` を `SparklineGroups.Add` メソッドに渡すことで列スパークラインを作成します。

手順は折れ線スパークラインの例と同じです。

1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. 視覚化したい値を同じソース範囲 (A1:E1) に入力します。
3. 出力先セルを表す `CellArea` を構築します。
4. `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)` を呼び出します。
5. 必要に応じて、結果として得られた `SparklineGroup` をカスタマイズします (たとえば、`group.Type` を設定して種類を確認したり、棒の色を調整したりします)。
6. 列スパークラインの例を上書きしないように、ワークブックを別の出力ファイルに保存します。

次の例では、A1:E1 に値 5、-3、8、-2、6 を書き込み、F1 に列スパークラインを描画します。負の値は下向きの棒として、正の値は上向きの棒として描画されるため、プラスとマイナスの寄与を一目で簡単に識別できます。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;

namespace SparklineDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // ステップ1: Workbookを作成し、最初のワークシートを取得する
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];

            // ステップ2: A1:E1にサンプル値を書き込む
            int[] values = { 5, -3, 8, -2, 6 };
            for (int i = 0; i < values.Length; i++)
            {
                worksheet.Cells[0, i].PutValue(values[i]);
            }

            // ステップ3: F1を指すCellAreaを構築する (列インデックス5、行インデックス0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;
            dest.EndColumn = 5;
            dest.StartRow = 0;
            dest.EndRow = 0;

            // ステップ4: 目的のセルにColumnスパークラインを追加する
            int idx = worksheet.SparklineGroups.Add(
                SparklineType.Column, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[idx];

            // ステップ5: group.Typeを読み取ってスパークラインの種類を確認する
            Console.WriteLine("Sparkline Type added: " + group.Type);

            // ステップ6: ワークブックを保存する
            workbook.Save("output_column.xlsx");

            Console.WriteLine("Workbook saved as output_column.xlsx");
        }
    }
}
```

## **勝敗スパークライン**

勝敗スパークラインは、2 つの結果のみを示すように設計された列スパークラインの特殊なバリアントです。正の値は「上」バー (勝ち) として描画され、ゼロまたは負の値は「下」バー (負け) として描画されます。勝敗スパークラインは、一連の勝ち負け、合否結果、または時系列でのあらゆる二項結果を視覚化するためによく使用されます。

Aspose.Cells では、`SparklineType.Stacked` を `SparklineGroups.Add` メソッドに渡すことで勝敗スパークラインが作成されます。(名前にもかかわらず、`SparklineType.Stacked` は勝敗レンダリングを要求するために使用される列挙値です。)

手順は他の 2 種類と同じです。

1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. ソース範囲を入力します。勝敗スパークラインではすべての値を勝ちまたは負けのいずれかとして扱うため、値そのものの大きさは重要ではなく、符号のみが重要です。正の値は上バーになり、非正の値は下バーになります。
3. 出力先セルを表す `CellArea` を構築します。
4. `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)` を呼び出します。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズします (たとえば、勝ちバーと負けバーのアクセントカラーを設定します)。
6. 3 つの例すべてをディスク上で共存させられるよう、ワークブックを別のファイル名で保存します。

次の例では、前の 2 つのセクションと同じ入力データを使用します。値 5、-3、8、-2、6 は、勝ち、負け、勝ち、負け、勝ち として解釈され、F1 に描画されるスパークラインはそのパターンを正確に反映します。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;

namespace SparklineDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // ステップ1: ワークブックを作成し、最初のワークシートを取得する
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            worksheet.Name = "WinLoss";

            // ステップ2: 1行目にサンプルデータを入力する: A1=5, B1=-3, C1=8, D1=-2, E1=6
            worksheet.Cells["A1"].PutValue(5);
            worksheet.Cells["B1"].PutValue(-3);
            worksheet.Cells["C1"].PutValue(8);
            worksheet.Cells["D1"].PutValue(-2);
            worksheet.Cells["E1"].PutValue(6);

            // ステップ3: F1を指すCellAreaを構築する(列5、行0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // F
            dest.EndColumn = 5;
            dest.StartRow = 0;      // 1行目
            dest.EndRow = 0;

            // ステップ4: Win/Lossスパークラインを追加する(SparklineType.Stacked)
            int groupIndex = worksheet.SparklineGroups.Add(
                SparklineType.Stacked,
                "A1:E1",
                false,
                dest);
            SparklineGroup group = worksheet.SparklineGroups[groupIndex];

            // ステップ5: スパークライングループをカスタマイズする
            // 高値マーカーと低値マーカーを有効にする
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            group.ShowNegativePoints = true;

            // 高値の色を緑に設定する
            CellsColor highColor = workbook.CreateCellsColor();
            highColor.Color = System.Drawing.Color.Green;
            group.HighPointColor = highColor;

            // 低値の色を赤に設定する
            CellsColor lowColor = workbook.CreateCellsColor();
            lowColor.Color = System.Drawing.Color.Red;
            group.LowPointColor = lowColor;

            // 負値の色をオレンジに設定する
            CellsColor negColor = workbook.CreateCellsColor();
            negColor.Color = System.Drawing.Color.Orange;
            group.NegativePointsColor = negColor;

            // デフォルトの系列の色を設定する(正の値のバーに使用)
            CellsColor seriesColor = workbook.CreateCellsColor();
            seriesColor.Color = System.Drawing.Color.SteelBlue;
            group.SeriesColor = seriesColor;

            // ステップ6: ワークブックを保存する
            workbook.Save("output_winloss.xlsx");

            Console.WriteLine("Workbook saved successfully: output_winloss.xlsx");
        }
    }
}
```

## **3 種類のスパークラインの組み合わせ**

前述の 3 つの例はそれぞれ独自のワークブックを生成するため、出力ファイルを個別に簡単に確認できます。ただし実際のシナリオでは、複数のデータ系列を並べて比較したい場合がよくあります。これを行う最もクリーンな方法は、複数のスパークライン グループを同じワークシート内に配置し、各グループが異なるスタイルをレンダリングするようにすることです。

同じ `SparklineGroupCollection` に複数の `SparklineGroup` オブジェクトを追加でき、各グループは異なる出力先セルまたは異なる範囲を対象とすることができます。たとえば、1 行目の同じソースデータから読み取り、F1 に折れ線スパークライン、F2 に列スパークライン、F3 に勝敗スパークラインを配置することで、閲覧者は同じ数値に対する 3 つの異なる視覚的表現を確認できます。

次の組み合わせ例では、単一のワークブックを作成し、1 行目に値 5、-3、8、-2、6 を入力し、セル F1、F2、F3 に 3 つのスパークライン グループ (各種類 1 つずつ) を追加して、結果のファイルに 3 つのスパークライン スタイルすべてを一度に示します。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;

// ステップ1: ワークブックを作成し、最初のワークシートを取得する
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// ステップ2: 1行目 (A1:E1) にサンプルデータを入力する
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);

// ステップ3: F1に折れ線スパークライングループを追加する
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.SparklineGroups[lineIdx];

// CellsColorを使用して折れ線スパークラインの色をカスタマイズする
CellsColor lineColor = workbook.CreateCellsColor();
lineColor.Color = System.Drawing.Color.Blue;
lineGroup.SeriesColor = lineColor;

// ステップ4: F2に縦棒スパークライングループを追加する
CellArea columnArea = new CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.SparklineGroups[columnIdx];

// 縦棒スパークラインの系列色をカスタマイズする
CellsColor columnColor = workbook.CreateCellsColor();
columnColor.Color = System.Drawing.Color.Green;
columnGroup.SeriesColor = columnColor;

// ステップ5: F3にWin/Loss (積み上げ) スパークライングループを追加する
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.SparklineGroups[stackedIdx];

// Win/Lossスパークラインの系列色をカスタマイズする
CellsColor stackedColor = workbook.CreateCellsColor();
stackedColor.Color = System.Drawing.Color.DarkOrange;
stackedGroup.SeriesColor = stackedColor;

// ステップ6: ワークブックを保存する
workbook.Save("output_all.xlsx");
```

{{% alert color="primary" %}}

単一のワークシートに複数のスパークライン グループを組み合わせる場合、各グループは独立しています。同じソース範囲を共有することも、異なるソース範囲を使用することもでき、それぞれ独立してスタイルを設定できます。これにより、既存のワークシート内にセル内ビジュアライゼーションの小さな「ダッシュボード」を簡単に構築できます。

{{% /alert %}}

## **スパークラインの外観のカスタマイズ**

`SparklineGroup` が作成されて `worksheet.SparklineGroups` に追加された後、ワークブックを保存する前にその視覚的なプロパティのいくつかを読み取ったり変更したりできます。最も一般的にカスタマイズされるプロパティは次のとおりです。

- **`group.Type`** — `SparklineType` (Line、Column、または Stacked)。グループは追加されるときに設定されますが、読み戻して確認することができます。
- **`group.Line.Color`** — 線の色。`workbook.CreateCellsColor()` 経由で作成された `CellsColor` として表現されます。これは折れ線スパークラインの線の色を設定するために使用するプロパティです。
- **`group.Line.Weight`** — ポイント単位の線の太さ。値を大きくすると線が太くなります。
- **高値/安値ポイント マーカー** — 最高および最低のデータポイントに小さなマーカー表示をオンにするフラグ。極端な値を強調するのに役立ちます。
- **最初/最後/負のポイント マーカー** — 最初、最後、および負のデータポイントにマーカー表示を切り替えるフラグ。

色を変更するには、常に `CellsColor` インスタンスを作成し、関連するプロパティに割り当ててください。`System.Drawing.Color` をスパークラインの色プロパティに直接割り当てないでください。それらは `Aspose.Cells.Drawing` の `CellsColor` 型を必要とします。`SparklineGroups.Add` メソッド自体は完全に型付けされた `SparklineGroup` オブジェクトを返すため、戻り値に対してプロパティの割り当てを連鎖させることも、ローカル変数に保存して保存前にカスタマイズすることもできます。

## **関連記事**

- [ワークシートのセルへのアクセス](/cells/ja/net/accessing-cells-of-a-worksheet/)
- [ワークブック内のワークシートセルの書式設定](/cells/ja/net/format-worksheet-cells-in-a-workbook/)
- [グラフのカスタマイズ](/cells/ja/net/customizing-charts/)
- [動的グラフの作成](/cells/ja/net/create-dynamic-charts/)
- [Excel ファイルのデータを管理](/cells/ja/net/cells-data/)

{{< app/cells/assistant language="csharp" >}}