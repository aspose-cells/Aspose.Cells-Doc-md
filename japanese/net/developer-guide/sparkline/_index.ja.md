---
title: Aspose.Cells for .NET のスパークライン
linktitle: Aspose.Cells for .NET のスパークライン
description: Aspose.Cells はワークシートのセル内に配置できるミニチャートであるスパークラインの作成をサポートする .NET ライブラリです。本記事では、Aspose.Cells ライブラリを使用してライン、カラム、勝敗スパークラインを追加およびカスタマイズする方法を説明します。
keywords: Aspose.Cells, .NET ライブラリ, スプレッドシート, スパークライン, ライン スパークライン, カラム スパークライン, 勝敗 スパークライン, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ja/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells はワークシートのセル内にスパークラインを作成することをサポートしています。スパークラインは単一セルに収まるミニチャートで、データのトレンドをすばやく視覚的に表現します。Aspose.Cells はライン、カラム、勝敗スパークラインをサポートしており、色、線の太さ、最高/最低ポイント、マーカーなどをカスタマイズできます。
{{% /alert %}}

## **導入**
スパークラインはセル内に表示できる小さなチャートで、行や列の横にデータの傾向を素早く示したいときに便利です。Excel では **ライン**、**カラム**、**勝敗** の 3 種類のスパークラインが使用可能です。Aspose.Cells は `Aspose.Cells.Charts` 名前空間の `SparklineGroup` と `SparklineGroupCollection` API を通じて同様の機能を提供します。  
Aspose.Cells では、追加する各スパークラインは `worksheet.SparklineGroups.Add(...)` によって作成され、戻り値として `SparklineGroup` オブジェクトが得られます。このオブジェクトを使用して、スパークラインの種類、データ範囲、配置先セル、線の色や太さ、マーカーや最高/最低ポイントの表示などの視覚プロパティを設定できます。  
本記事では、Aspose.Cells がサポートする **ライン**、**カラム**、**勝敗** の 3 種類のスパークラインについて、追加方法、色のカスタマイズ方法、そして最終的なワークブックの保存手順を順に解説します。

## **ライン スパークライン**
ライン スパークラインは系列内のデータポイントを連続した線で結び、時間経過による傾向を示すのに最適です。Aspose.Cells では、`SparklineType.Line` を `SparklineGroups.Add` メソッドに渡すことでライン スパークラインを作成します。
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。  
2. ソース データの行を入力します（例：1 行目の A 列から E 列へ）し、可視化したい値を設定します。  
3. スパークラインを描画する先のセルを示す `CellArea` を作成します。  
4. `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)` を呼び出します。3 番目の引数 `false` はデータ範囲が水平（行）であることを Aspose.Cells に示し、垂直（列）ではないことを指定します。  
5. 必要に応じて返された `SparklineGroup` をカスタマイズします。ライン スパークラインの場合、`group.Line.Color`（`Aspose.Cells.Drawing` の `CellsColor` が必要）で線の色を設定し、`group.Line.Weight` で線の太さを調整し、最高/最低ポイントのマーカーを有効化できます。  
6. ワークブックを保存します。
以下の例は、ワークブックを作成し、セル A1~E1 に 5, -3, 8, -2, 6 の値を書き込み、セル F1 にそれらの値を描画したライン スパークラインを追加します。また、線の色を赤に設定し、最高点と最低点のマーカーを有効にしています。

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
            // Step 1: Create a Workbook and get the first worksheet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            Cells cells = worksheet.Cells;
            // Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
            cells["A1"].PutValue(5);
            cells["B1"].PutValue(-3);
            cells["C1"].PutValue(8);
            cells["D1"].PutValue(-2);
            cells["E1"].PutValue(6);
            // Step 3: Build a CellArea pointing to destination cell F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // column F (0-indexed)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // row 1 (0-indexed)
            dest.EndRow = 0;
            // Step 4: Add a Line sparkline from A1:E1 into F1
            // SparklineGroups.Add returns the index of the newly added group
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];
            // Step 5: Create a red CellsColor and assign it to the sparkline line color
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;
            // Step 6: Enable high-point and low-point markers
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            // Step 7: Save the workbook
            workbook.Save("output_line.xlsx");
        }
    }
}
```

## **カラム スパークライン**
カラム スパークラインは各データポイントを縦棒で表示します。値の大小が重要なデータ（例：月次売上や件数など）に適しています。Aspose.Cells では、`SparklineType.Column` を `SparklineGroups.Add` メソッドに渡すことでカラム スパークラインを作成します。
手順はライン スパークラインの例と同様です。
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。  
2. ソース データの行を入力します（例：1 行目の A 列から E 列へ）し、可視化したい値を設定します。  
3. スパークラインを描画する先のセルを示す `CellArea` を作成します。  
4. `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)` を呼び出します。  
5. 必要に応じて生成された `SparklineGroup` をカスタマイズします。たとえば `group.Type` を確認したり、棒の色を変更したりできます。  
6. ライン スパークラインの例と上書きしないように、別ファイルとしてワークブックを保存します。
以下の例は、A1:E1 に 5, -3, 8, -2, 6 の値を書き込み、セル F1 にカラム スパークラインを描画します。負の値は下方向の棒、正の値は上方向の棒として表示され、正負の貢献度を一目で把握できます。

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
            // Step 1: Create a Workbook and get the first worksheet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            // Step 2: Write sample values into A1:E1
            int[] values = { 5, -3, 8, -2, 6 };
            for (int i = 0; i < values.Length; i++)
            {
                worksheet.Cells[0, i].PutValue(values[i]);
            }
            // Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;
            dest.EndColumn = 5;
            dest.StartRow = 0;
            dest.EndRow = 0;
            // Step 4: Add a Column sparkline to the destination cell
            int idx = worksheet.SparklineGroups.Add(
                SparklineType.Column, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[idx];
            // Step 5: Confirm the sparkline type by reading group.Type
            Console.WriteLine("Sparkline Type added: " + group.Type);
            // Step 6: Save the workbook
            workbook.Save("output_column.xlsx");
            Console.WriteLine("Workbook saved as output_column.xlsx");
        }
    }
}
```

## **勝敗 スパークライン**
勝敗 スパークラインはカラム スパークラインの特殊形で、2 つの結果のみを示します。正の値は「上向き」の棒（勝ち）として、0 または負の値は「下向き」の棒（負け）として描画されます。勝敗 スパークラインは、勝敗のシーケンスや合格/不合格結果、2 値データの時系列表示によく用いられます。
Aspose.Cells では、`SparklineType.Stacked` を `SparklineGroups.Add` メソッドに渡すことで勝敗 スパークラインを作成します。（名前は `Stacked` ですが、勝敗表示を要求する列挙値として使用されます。）
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。  
2. ソース範囲を入力します。勝敗 スパークラインは各値を勝ちまたは負けとして扱うため、数値の大きさは無視され、符号のみが重要です。正の値は上向き棒、非正（0 または負）の値は下向き棒になります。  
3. スパークラインを描画する先のセルを示す `CellArea` を作成します。  
4. `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)` を呼び出します。  
5. 必要に応じて返された `SparklineGroup` をカスタマイズします。たとえば、勝ち棒と負け棒のアクセントカラーを設定できます。  
6. 3 つの例が同時に存在できるよう、別ファイル名でワークブックを保存します。

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
            // Step 1: Create a Workbook and get the first worksheet
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            worksheet.Name = "WinLoss";
            // Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
            worksheet.Cells["A1"].PutValue(5);
            worksheet.Cells["B1"].PutValue(-3);
            worksheet.Cells["C1"].PutValue(8);
            worksheet.Cells["D1"].PutValue(-2);
            worksheet.Cells["E1"].PutValue(6);
            // Step 3: Build a CellArea pointing to F1 (column 5, row 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // F
            dest.EndColumn = 5;
            dest.StartRow = 0;      // row 1
            dest.EndRow = 0;
            // Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
            int groupIndex = worksheet.SparklineGroups.Add(
                SparklineType.Stacked,
                "A1:E1",
                false,
                dest);
            SparklineGroup group = worksheet.SparklineGroups[groupIndex];
            // Step 5: Customize the sparkline group
            // Enable high-point and low-point markers
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            group.ShowNegativePoints = true;
            // Set the high-point color to green
            CellsColor highColor = workbook.CreateCellsColor();
            highColor.Color = System.Drawing.Color.Green;
            group.HighPointColor = highColor;
            // Set the low-point color to red
            CellsColor lowColor = workbook.CreateCellsColor();
            lowColor.Color = System.Drawing.Color.Red;
            group.LowPointColor = lowColor;
            // Set the negative-point color to orange
            CellsColor negColor = workbook.CreateCellsColor();
            negColor.Color = System.Drawing.Color.Orange;
            group.NegativePointsColor = negColor;
            // Set the default series color (used for positive bars)
            CellsColor seriesColor = workbook.CreateCellsColor();
            seriesColor.Color = System.Drawing.Color.SteelBlue;
            group.SeriesColor = seriesColor;
            // Step 6: Save the workbook
            workbook.Save("output_winloss.xlsx");
            Console.WriteLine("Workbook saved successfully: output_winloss.xlsx");
        }
    }
}
```

## **3 つすべてのスパークライン タイプを組み合わせる**
以下の統合例は、単一のワークブックを作成し、1 行目に 5, -3, 8, -2, 6 の値を配置したうえで、セル F1、F2、F3 にそれぞれライン、カラム、勝敗のスパークライン グループを追加します。これにより、生成されたファイルで 3 種類すべてのスパークライン スタイルを同時に確認できます。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
// Step 1: Create a Workbook and get the first worksheet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Step 2: Populate sample data in row 1 (A1:E1)
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);
// Step 3: Add a Line sparkline group at F1
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.SparklineGroups[lineIdx];
// Customize the line sparkline color via CellsColor
CellsColor lineColor = workbook.CreateCellsColor();
lineColor.Color = System.Drawing.Color.Blue;
lineGroup.SeriesColor = lineColor;
// Step 4: Add a Column sparkline group at F2
CellArea columnArea = new CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.SparklineGroups[columnIdx];
// Customize the column sparkline series color
CellsColor columnColor = workbook.CreateCellsColor();
columnColor.Color = System.Drawing.Color.Green;
columnGroup.SeriesColor = columnColor;
// Step 5: Add a Win/Loss (Stacked) sparkline group at F3
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.SparklineGroups[stackedIdx];
// Customize the win/loss sparkline series color
CellsColor stackedColor = workbook.CreateCellsColor();
stackedColor.Color = System.Drawing.Color.DarkOrange;
stackedGroup.SeriesColor = stackedColor;
 // Step 6: Save the workbook
workbook.Save("output_all.xlsx");
```

## **スパークラインの外観をカスタマイズする**
`SparklineGroup` を作成し `worksheet.SparklineGroups` に追加した後、ワークブックを保存する前にいくつかの視覚プロパティを読み取り・変更できます。最も一般的にカスタマイズされるプロパティは以下の通りです。
- **`group.Type`** — `SparklineType`（Line、Column、Stacked）。追加時に設定されますが、確認のために取得可能です。  
- **`group.Line.Color`** — `Aspose.Cells.Drawing` の `CellsColor` で作成したオブジェクトを使用して設定する線の色。ライン スパークラインのストローク色に使用します。  
- **`group.Line.Weight`** — 線の太さ（ポイント単位）。数値が大きいほど太い線になります。  
- **最高/最低ポイント マーカー** — 最高点と最低点に小さなマーカーを表示するフラグ。極端な値を強調するのに便利です。  
- **先頭/末尾/負のポイント マーカー** — 先頭、末尾、および負のデータポイントにマーカーを付けるフラグ。
色を変更する場合は、必ず `CellsColor` インスタンスを作成し、該当プロパティに割り当ててください。`System.Drawing.Color` を直接代入してはいけません。`SparklineGroups.Add` メソッド自体が完全に型指定された `SparklineGroup` オブジェクトを返すため、返り値に対してプロパティ設定をチェーンしたり、ローカル変数に保持して保存前にカスタマイズしたりできます。

## 関連記事
- [Aspose.Cells for .NET でスパークラインを画像と HTML に変換する](/cells/ja/net/convert-sparkline-to-image-and-html/)
- [Aspose.Cells for .NET でピボットテーブルにフィルタ フィールドを追加する](/cells/ja/net/add-page-field-in-pivot-table/)
- [Aspose.Cells for .NET でピボットテーブルにスタイルを適用する](/cells/ja/net/apply-style-to-pivot-table/)
- [ピボットテーブルのページ フィールド レイアウトを変更する](/cells/ja/net/change-page-field-layout/)
- [Excel を OFD 形式に変換する](/cells/ja/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}