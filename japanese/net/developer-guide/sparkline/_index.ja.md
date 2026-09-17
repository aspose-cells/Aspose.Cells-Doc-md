---
title: Aspose.Cells for .NET でのスパークライン
linktitle: Aspose.Cells for .NET でのスパークライン
description: Aspose.Cells はスプレッドシートファイルを操作するための .NET ライブラリで、ワークシートセル内に配置されるミニチュアグラフであるスパークラインの作成をサポートしています。この記事では、Aspose.Cells ライブラリを使用して、ライン、列、勝敗のスパークラインを追加およびカスタマイズする方法について説明します。
keywords: Aspose.Cells, .NET ライブラリ, スプレッドシート, スパークライン, ラインスパークライン, 列スパークライン, 勝敗スパークライン, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ja/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ワークシートセル内にスパークラインを作成することをサポートします。スパークラインは 1 つのセル内に収まるミニチュアグラフであり、データ傾向を素早く視覚的に表現します。Aspose.Cells はライン、列、勝敗のスパークラインをサポートしており、それぞれを色、線の太さ、高値/安値ポイント、マーカーに関してカスタマイズできます。
{{% /alert %}}

## **Introduction**
スパークラインはセル内に収まる小さなグラフで、完全なグラフのスペースを占有せずにデータの行や列の隣に素早く傾向を表示したい場合に役立ちます。Excel は **ライン**、**列**、**勝敗** の 3 種類のスパークラインをサポートします。Aspose.Cells は `Aspose.Cells.Charts` 名前空間にある `SparklineGroup` および `SparklineGroupCollection` API を通じてこの機能を提供します。
Aspose.Cells では、追加するすべてのスパークラインが `worksheet.SparklineGroups.Add(...)` を通じて作成され、これは `SparklineGroup` オブジェクトを返します。その後、そのオブジェクトを使用してスパークラインの種類、データ範囲、配置先セル、および線の色、線の太さ、マーカー、高値/安値ポイントインジケーターなどの視覚的なプロパティを設定できます。
この記事では、Aspose.Cells がサポートする 3 種類のスパークライン、**ライン**、**列**、**勝敗** のそれぞれについて、その追加方法、色のカスタマイズ方法、結果として得られるワークブックの保存方法を説明します。

## **Line Sparklines**
ラインスパークラインは、系列のデータポイントを結ぶ連続的な線を描画するため、時間の経過に伴う傾向を示すのに最も自然な選択肢です。Aspose.Cells では、`SparklineType.Line` を `SparklineGroups.Add` メソッドに渡すことでラインスパークラインを作成します。
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. ソースデータの行 (たとえば 1 行目の A 列から E 列) に視覚化したい値を入力します。
3. スパークラインが描画される配置先セルを示す `CellArea` を作成します。
4. `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)` を呼び出します。3 番目の引数 `false` は、データ範囲が縦方向 (列) ではなく横方向 (行) であることを Aspose.Cells に伝えます。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズします。ラインスパークラインの場合、`group.Line.Color` を使用して線の色を設定し (`Aspose.Cells.Drawing` の `CellsColor` を必要とします)、線の太さを調整し、高値/安値ポイントマーカーを有効化できます。
6. ワークブックを保存します。
次の例は、ワークブックを作成し、セル A1 から E1 に値 5、-3、8、-2、6 を書き込み、セル F1 にそれらの値をトレースするラインスパークラインを追加します。また、線の色を赤にカスタマイズし、高値および安値のマーカーを有効化します。

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
            // ステップ1: Workbookを作成し、最初のワークシートを取得します
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            Cells cells = worksheet.Cells;
            // ステップ2: サンプル値5、-3、8、-2、6をセルA1:E1に書き込みます
            cells["A1"].PutValue(5);
            cells["B1"].PutValue(-3);
            cells["C1"].PutValue(8);
            cells["D1"].PutValue(-2);
            cells["E1"].PutValue(6);
            // ステップ3: 宛先セルF1を指すCellAreaを構築します
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // 列F（0から始まるインデックス）
            dest.EndColumn = 5;
            dest.StartRow = 0;      // 行1（0から始まるインデックス）
            dest.EndRow = 0;
            // ステップ4: A1:E1からF1に折れ線スパークラインを追加します
            // SparklineGroups.Addは新しく追加されたグループのインデックスを返します
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];
            // ステップ5: 赤いCellsColorを作成し、スパークラインの線の色に割り当てます
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;
            // ステップ6: 高点マーカーと低点マーカーを有効にします
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            // ステップ7: ワークブックを保存します
            workbook.Save("output_line.xlsx");
        }
    }
}
```

## **Column Sparklines**
列スパークラインは各データポイントを縦棒としてレンダリングします。そのため、大きさが意味を持つデータ、たとえば月次売上や個数などに適しています。Aspose.Cells では、`SparklineType.Column` を `SparklineGroups.Add` メソッドに渡すことで列スパークラインを作成します。
手順はラインスパークラインの例と同様です。
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
3. 配置先セルを示す `CellArea` を作成します。
4. `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)` を呼び出します。
5. 必要に応じて、結果として得られる `SparklineGroup` をカスタマイズします。たとえば、`group.Type` を設定して種類を確認したり、棒の色を調整したりできます。
6. ラインスパークラインの例を上書きしないように、ワークブックを別の出力ファイルに保存します。
次の例では、A1:E1 に値 5、-3、8、-2、6 を書き込み、F1 に列スパークラインをレンダリングします。負の値は下向きの棒として、正の値は上向きの棒として描画されるため、プラスとマイナスの寄与を一目で容易に確認できます。

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
            // ステップ 1: Workbook を作成し、最初のワークシートを取得します
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            // ステップ 2: A1:E1 にサンプル値書き込みます
            int[] values = { 5, -3, 8, -2, 6 };
            for (int i = 0; i < values.Length; i++)
            {
                worksheet.Cells[0, i].PutValue(values[i]);
            }
            // ステップ 3: F1 を指す CellArea を作成します (列インデックス 5、行インデックス 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;
            dest.EndColumn = 5;
            dest.StartRow = 0;
            dest.EndRow = 0;
            // ステップ 4: 目的セルに Column スパークラインを追加します
            int idx = worksheet.SparklineGroups.Add(
                SparklineType.Column, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[idx];
            // ステップ 5: group.Type を読み取ってスパークラインのタイプを確認します
            Console.WriteLine("Sparkline Type added: " + group.Type);
            // ステップ 6: ワークブックを保存します
            workbook.Save("output_column.xlsx");
            Console.WriteLine("Workbook saved as output_column.xlsx");
        }
    }
}
```

## **Win/Loss Sparklines**
勝敗スパークラインは、2 つの結果のみを表示するように設計された列スパークラインの特殊なバリエーションです。正の値は「上向き」の棒 (勝ち) として描画され、ゼロまたは負の値は「下向き」の棒 (負け) として描画されます。勝敗スパークラインは、勝ち負けの連続、合否結果、または経時的な二値の結果を可視化するためによく使用されます。
Aspose.Cells では、`SparklineType.Stacked` を `SparklineGroups.Add` メソッドに渡すことで勝敗スパークラインを作成します。(名前にかかわらず、`SparklineType.Stacked` は勝敗レンダリングを要求するために使用される列挙値です。)
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. ソース範囲を入力します。勝敗スパークラインはすべての値を勝ちまたは負けのいずれかとして扱うため、値の絶対値ではなく符号のみが重要です。正の値は上向きの棒に、非正の値は下向きの棒になります。
3. 配置先セルを示す `CellArea` を作成します。
4. `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)` を呼び出します。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズします。たとえば、勝ち棒と負け棒のアクセント色を設定します。
6. 3 つのすべての例がディスク上で共存できるように、ワークブックを別のファイル名で保存します。

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
            // ステップ 1: Workbook を作成し、最初のワークシートを取得します
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            worksheet.Name = "WinLoss";
            // ステップ 2: 1 行目にサンプル データを入力します: A1=5, B1=-3, C1=8, D1=-2, E1=6
            worksheet.Cells["A1"].PutValue(5);
            worksheet.Cells["B1"].PutValue(-3);
            worksheet.Cells["C1"].PutValue(8);
            worksheet.Cells["D1"].PutValue(-2);
            worksheet.Cells["E1"].PutValue(6);
            // ステップ 3: F1 (列 5、行 0) を指す CellArea を作成します
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // F
            dest.EndColumn = 5;
            dest.StartRow = 0;      // 行 1
            dest.EndRow = 0;
            // ステップ 4: Win/Loss スパークライン (SparklineType.Stacked) を追加します
            int groupIndex = worksheet.SparklineGroups.Add(
                SparklineType.Stacked,
                "A1:E1",
                false,
                dest);
            SparklineGroup group = worksheet.SparklineGroups[groupIndex];
            // ステップ 5: スパークライン グループをカスタマイズします
            // 高値ポイントと低値ポイントのマーカーを有効にします
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            group.ShowNegativePoints = true;
            // 高値ポイントの色を緑に設定します
            CellsColor highColor = workbook.CreateCellsColor();
            highColor.Color = System.Drawing.Color.Green;
            group.HighPointColor = highColor;
            // 低値ポイントの色を赤に設定します
            CellsColor lowColor = workbook.CreateCellsColor();
            lowColor.Color = System.Drawing.Color.Red;
            group.LowPointColor = lowColor;
            // 負のポイントの色をオレンジに設定します
            CellsColor negColor = workbook.CreateCellsColor();
            negColor.Color = System.Drawing.Color.Orange;
            group.NegativePointsColor = negColor;
            // 既定の系列の色 (正の棒に使用されます) を設定します
            CellsColor seriesColor = workbook.CreateCellsColor();
            seriesColor.Color = System.Drawing.Color.SteelBlue;
            group.SeriesColor = seriesColor;
            // ステップ 6: ワークブックを保存します
            workbook.Save("output_winloss.xlsx");
            Console.WriteLine("Workbook saved successfully: output_winloss.xlsx");
        }
    }
}
```

## **Combining All Three Sparkline Types**
次の統合例は、単一のワークブックを作成し、1 行目に値 5、-3、8、-2、6 を入力してから、セル F1、F2、F3 に 3 つのスパークライングループ (各種類 1 つずつ) を追加し、結果のファイルが 3 種類のスパークラインスタイルを一度に示すようにします。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
// ステップ1: ワークブックを作成し、最初のワークシートを取得する
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// ステップ2: 1行目(A1:E1)にサンプルデータを入力する
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
// CellsColorを介して折れ線スパークラインの色をカスタマイズする
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
// 縦棒スパークラインシリーズの色をカスタマイズする
CellsColor columnColor = workbook.CreateCellsColor();
columnColor.Color = System.Drawing.Color.Green;
columnGroup.SeriesColor = columnColor;
// ステップ5: F3にWin/Loss(積み上げ)スパークライングループを追加する
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.SparklineGroups[stackedIdx];
// Win/Lossスパークラインシリーズの色をカスタマイズする
CellsColor stackedColor = workbook.CreateCellsColor();
stackedColor.Color = System.Drawing.Color.DarkOrange;
stackedGroup.SeriesColor = stackedColor;
// ステップ6: ワークブックを保存する
workbook.Save("output_all.xlsx");
```

## **Customizing Sparkline Appearance**
`SparklineGroup` が作成されて `worksheet.SparklineGroups` に追加されたら、ワークブックを保存する前にその視覚的なプロパティのいくつかを読み取ったり変更したりできます。最も一般的にカスタマイズされるプロパティは次のとおりです。
- **`group.Type`** — `SparklineType` (Line、Column、または Stacked)。グループは追加されるときに設定されますが、読み戻して確認できます。
- **`group.Line.Color`** — 線の色で、`workbook.CreateCellsColor()` を介して作成された `CellsColor` として表現されます。これはラインスパークラインのストローク色に使用するプロパティです。
- **`group.Line.Weight`** — ポイント単位の線の太さ。値が大きいほど太い線が描画されます。
- **高値/安値ポイントマーカー** — 最高および最低のデータポイントに小さなマーカーをオンにするフラグで、極端な値を強調するのに役立ちます。
- **最初/最後/負のポイントマーカー** — 最初、最後、および負のデータポイントにマーカーを切り替えるフラグ。
色を変更するには、常に `CellsColor` インスタンスを作成し、関連するプロパティに割り当てます。`System.Drawing.Color` をスパークラインの色プロパティに直接割り当てないでください。それらは `Aspose.Cells.Drawing` の `CellsColor` 型を必要とします。`SparklineGroups.Add` メソッド自体は完全に型付けされた `SparklineGroup` オブジェクトを返すため、戻り値にプロパティ割り当てをチェーンしたり、ローカル変数に保存して保存前にカスタマイズしたりできます。

## Related Articles
- [Aspose.Cells for .NET でスパークラインを画像および HTML に変換する](/cells/ja/net/convert-sparkline-to-image-and-html/)
- [Aspose.Cells for .NET でピボットテーブルにページフィールドを追加する](/cells/ja/net/add-page-field-in-pivot-table/)
- [Aspose.Cells for .NET でピボットテーブルにスタイルを適用する](/cells/ja/net/apply-style-to-pivot-table/)
- [ピボットテーブルのページフィールドのレイアウトを変更する](/cells/ja/net/change-page-field-layout/)
- [Excel を OFD 形式に変換する](/cells/ja/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}