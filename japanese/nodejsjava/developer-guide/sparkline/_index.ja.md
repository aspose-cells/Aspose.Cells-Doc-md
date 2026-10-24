---
title: Sparklines in Aspose.Cells for Node.js via Java
linktitle: Sparklines
description: Aspose.Cells is a Node.js via Java library for working with spreadsheet files that supports creating sparklines — miniature charts placed inside worksheet cells. This article explains how to add and customize line, column, and win/loss sparklines using the Aspose.Cells library.
keywords: Aspose.Cells, Node.js via Java ライブラリ, スプレッドシート, スパークライン, ラインスパークライン, 列スパークライン, 勝敗スパークライン, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ja/nodejs-java/creating-sparklines/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells はワークシートのセル内にスパークラインの作成をサポートしています。スパークラインは単一のセル内に収まるミニチャートであり、データ傾向を素早く視覚的に表現します。Aspose.Cells はライン、列、勝敗のスパークラインをサポートしており、それぞれを色、線の太さ、高値/低値のポイント、マーカーについてカスタマイズできます。
{{% /alert %}}

## **Introduction**
スパークラインはセル内に表示される小さなチャートであり、フルチャート分のスペースを取らずにデータの行や列の隣に素早く傾向を表示したい場合に便利です。Excel は 3 種類のスパークラインをサポートしています。**ライン**、**列**、および**勝敗**です。Aspose.Cells は `com.aspose.cells.Charts` 名前空間にある `SparklineGroup` および `SparklineGroupCollection` API を通じてこの機能を実現しています。
Aspose.Cells では、追加するすべてのスパークラインが `worksheet.SparklineGroups.add(...)` を通じて作成され、`SparklineGroup` オブジェクトを返します。その後、そのオブジェクトを使用してスパークラインタイプ、データ範囲、配置先セル、および線の色、線の太さ、マーカー、高値/低値インジケーターなどの視覚的なプロパティを設定できます。
本記事は、Aspose.Cells がサポートする 3 種類のスパークラインタイプ—**ライン**、**列**、**勝敗**—のそれぞれについて、スパークラインの追加方法、色のカスタマイズ方法、および結果として生成されるブックの保存方法を説明します。

## **Line Sparklines**
ラインスパークラインは、系列内のデータポイントを通る連続した線を描くため、時系列の傾向を示すのに最も自然な選択肢です。Aspose.Cells では、`SparklineGroups.add` メソッドに `SparklineType.Line` を渡してラインスパークラインを作成します。
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. 可視化したい値 (例: 1 行目の A 列から E 列) で 1 行のソースデータを入力します。
3. スパークラインを描画する宛先セルを説明する `CellArea` を作成します。
4. `worksheet.SparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)` を呼び出します。3 番目の引数 `false` は、データ範囲が垂直方向 (列) ではなく水平方向 (行) であることを Aspose.Cells に通知します。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズできます。ラインスパークラインでは、`group.Line.Color` (`com.aspose.cells.Drawing` の `CellsColor` が必要) を使って線の色を設定し、線の太さを調整したり、高値/低値のマーカーを切り替えたりできます。
6. ブックを保存します。
次の例では、ブックを作成し、値 5、-3、8、-2、6 を A1 ～ E1 のセルに書き込み、それらの値を追跡するラインスパークラインを F1 セルに追加します。また、線の色を赤にカスタマイズし、高値と低値のマーカーを有効にします。

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();
// Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// Step 3: Build a CellArea pointing to destination cell F1
let dest = new AsposeCells.CellArea();
dest.StartColumn = 5;   // column F (0-indexed)
dest.EndColumn = 5;
dest.StartRow = 0;      // row 1 (0-indexed)
dest.EndRow = 0;
// Step 4: Add a Line sparkline from A1:E1 into F1
// SparklineGroups.Add returns the index of the newly added group
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.LINE, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(index);
// Step 5: Create a red CellsColor and assign it to the sparkline line color
let red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);
// Step 6: Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// Step 7: Save the workbook
workbook.save("output_line.xlsx");
```

## **Column Sparklines**
列スパークラインは、各データポイントを垂直の棒として描画します。これは、月次の売上数値や個数など、値の大きさが意味を持つデータに適しています。Aspose.Cells では、`SparklineGroups.add` メソッドに `SparklineType.Column` を渡して列スパークラインを作成します。
手順はラインスパークラインの例と同じです。
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
3. 宛先セルを説明する `CellArea` を作成します。
4. `worksheet.SparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)` を呼び出します。
5. 必要に応じて、生成された `SparklineGroup` をカスタマイズできます。たとえば、`group.Type` を設定してタイプを確認したり、棒の色を調整したりできます。
6. ラインスパークラインの例を上書きしないよう、別の出力ファイルにブックを保存します。
以下の例では、値 5、-3、8、-2、6 を A1:E1 に書き込み、F1 に列スパークラインを描画します。負の値は下向きの棒、正の値は上向きの棒として描画されるため、正の値と負の値の寄与を一目で確認できます。

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Step 2: Write sample values into A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
let dest = new AsposeCells.CellArea();
dest.StartColumn = 5;
dest.EndColumn = 5;
dest.StartRow = 0;
dest.EndRow = 0;
// Step 4: Add a Column sparkline to the destination cell
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.COLUMN, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);
// Step 5: Confirm the sparkline type by reading group.Type
console.log("Sparkline Type added: " + group.getType());
// Step 6: Save the workbook
workbook.save("output_column.xlsx");
console.log("Workbook saved as output_column.xlsx");
```

## **Win/Loss Sparklines**
勝敗スパークラインは、2 つの結果のみを表示するように設計された列スパークラインの特殊なバリアントです。正の値は「上」の棒 (勝ち)、ゼロまたは負の値は「下」の棒 (負け) として描画されます。勝敗スパークラインは通常、勝ちと負けの系列、合格/不合格の結果、または時間の経過に伴う任意の二値結果を視覚化するために使用されます。
Aspose.Cells では、`SparklineGroups.add` メソッドに `SparklineType.Stacked` を渡して勝敗スパークラインを作成します (名前が `Stacked` ではありますが、これは勝敗レンダリングを要求するために使用される列挙値です)。
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. ソース範囲を入力します。勝敗スパークラインはすべての値を勝ちまたは負けとして扱うため、値の大きさは重要ではなく、符号だけが重要です。正の値は上向きの棒に、0 以下の値は下向きの棒になります。
3. 宛先セルを説明する `CellArea` を作成します。
4. `worksheet.SparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)` を呼び出します。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズできます。たとえば、勝ちと負けの棒にアクセントカラーを設定できます。
6. 3 つすべての例をディスク上で共存できるように、異なるファイル名でブックを保存します。

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Step 3: Build a CellArea pointing to F1 (column 5, row 0)
let dest = new AsposeCells.CellArea();
dest.StartColumn = 5;   // F
dest.EndColumn = 5;
dest.StartRow = 0;      // row 1
dest.EndRow = 0;
// Step 4: Add a Win/Loss sparkline (SparklineType.STACKED)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.STACKED,
    "A1:E1",
    false,
    dest
);
let group = worksheet.getSparklineGroups().get(groupIndex);
// Step 5: Customize the sparkline group
// Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Set the high-point color to green
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.getGreen());
group.setHighPointColor(highColor);
// Set the low-point color to red
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.getRed());
group.setLowPointColor(lowColor);
// Set the negative-point color to orange
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.getOrange());
group.setNegativePointsColor(negColor);
// Set the default series color (used for positive bars)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.getSteelBlue());
group.setSeriesColor(seriesColor);
// Step 6: Save the workbook
workbook.save("output_winloss.xlsx");
console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **Combining All Three Sparkline Types**
以下の組み合わせ例では、単一のブックを作成し、1 行目に値 5、-3、8、-2、6 を入力し、F1、F2、F3 のセルに 3 つのスパークライングループ (各タイプ 1 つ) を追加します。そのため、生成されたファイルでは 3 種類のスパークラインスタイルを一度に確認できます。

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Step 2: Populate sample data in row 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Step 3: Add a Line sparkline group at F1
let lineArea = new AsposeCells.CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.LINE, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Customize the line sparkline color via CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// Step 4: Add a Column sparkline group at F2
let columnArea = new AsposeCells.CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.COLUMN, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Customize the column sparkline series color
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// Step 5: Add a Win/Loss (Stacked) sparkline group at F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.STACKED, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Customize the win/loss sparkline series color
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// Step 6: Save the workbook
workbook.save("output_all.xlsx");
```

## **Customizing Sparkline Appearance**
`SparklineGroup` を作成して `worksheet.SparklineGroups` に追加した後、ブックを保存する前に、その一部の視覚的プロパティを読み取ったり変更したりできます。最もよくカスタマイズされるプロパティは次のとおりです。
- **`group.Type`** — `SparklineType` (Line、Column、または Stacked)。これはグループを追加するときに設定されますが、後から読み取って確認できます。
- **`group.Line.Color`** — `workbook.createCellsColor()` で作成された `CellsColor` として表される線の色です。ラインスパークラインのストローク色に使用するプロパティです。
- **`group.Line.Weight`** — ポイント単位の線の太さ。値が大きいほど線が太くなります。
- **高値/低値のマーカー** — 最高値と最低値のデータポイントに小さなマーカーを表示するフラグです。極端な値を強調するのに役立ちます。
- **最初/最後/負のポイントのマーカー** — 最初、最後、および負のデータポイントのマーカーを切り替えるフラグです。
色を変更する場合は、常に `CellsColor` インスタンスを作成し、該当するプロパティに割り当てます。スパークラインの色プロパティに `java.awt.Color` を直接割り当てないでください。これらのプロパティは `com.aspose.cells.Drawing` の `CellsColor` 型を要求します。`SparklineGroups.add` メソッド自体が完全に型指定された `SparklineGroup` オブジェクトを返すため、戻り値に対してプロパティの割り当てをチェーンしたり、ローカル変数に保存したりして、保存前にカスタマイズできます。

{{< app/cells/assistant language="nodejs-java" >}}