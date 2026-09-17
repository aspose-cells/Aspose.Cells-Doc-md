---
title: Sparklines in Aspose.Cells for Node.js via Java
linktitle: Sparklines
description: Aspose.Cells is a Node.js via Java library for working with spreadsheet files that supports creating sparklines — miniature charts placed inside worksheet cells. This article explains how to add and customize line, column, and win/loss sparklines using the Aspose.Cells library.
keywords: Aspose.Cells, Node.js via Java library, spreadsheet, sparklines, line sparkline, column sparkline, win/loss sparkline, SparklineGroup, SparklineType
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
この記事では、Aspose.Cells がサポートする 3 種類のスパークラインタイプ (**ライン**、**列**、および**勝敗**) それぞれについて説明し、それらの追加方法、色のカスタマイズ方法、結果として得られるワークブックの保存方法を紹介します。

## **Line Sparklines**
ラインスパークラインは、系列内のデータポイントを結ぶ連続した線を描画するため、時間の経過に伴う傾向を表示するのに最も自然な選択肢です。Aspose.Cells では、`SparklineType.Line` を `SparklineGroups.add` メソッドに渡すことでラインスパークラインを作成します。
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. 可視化したい値を使用して、ソースデータの 1 行 (たとえば、行 1、A 列から E 列) を入力します。
3. スパークラインが描画される配置先セルを示す `CellArea` を作成します。
4. `worksheet.SparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)` を呼び出します。3 番目の引数 `false` は、データ範囲が垂直方向 (列) ではなく水平方向 (行) であることを Aspose.Cells に通知します。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズします。ラインスパークラインの場合、`group.Line.Color` を使用して線の色を設定し (`com.aspose.cells.Drawing` の `CellsColor` を必要とします)、線の太さを調整し、高値/低値ポイントマーカーを切り替えることができます。
6. ワークブックを保存します。
次の例では、ワークブックを作成し、セル A1 から E1 に値 5、-3、8、-2、6 を書き込み、セル F1 にこれらの値をトレースするラインスパークラインを追加します。また、線の色を赤にカスタマイズし、高値および低値のポイントのマーカーを有効にします。

```javascript
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
dest.setStartColumn(5);   // column F (0-indexed)
dest.setEndColumn(5);
dest.setStartRow(0);      // row 1 (0-indexed)
dest.setEndRow(0);
// Step 4: Add a Line sparkline from A1:E1 into F1
// SparklineGroups.Add returns the index of the newly added group
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
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
列スパークラインは、各データポイントを縦棒としてレンダリングします。そのため、大きさが意味を持つデータ (たとえば、月次売上や件数) に適しています。Aspose.Cells では、`SparklineType.Column` を `SparklineGroups.add` メソッドに渡すことで列スパークラインを作成します。
手順はラインスパークラインの例と同様です。
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. 配置先セルを示す `CellArea` を作成します。
3. `worksheet.SparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)` を呼び出します。
4. 必要に応じて、結果の `SparklineGroup` をカスタマイズします — たとえば、`group.Type` を設定してタイプを確認したり、棒の色調整したりします。
5. ラインスパークラインの例を上書きしないように、ワークブックを別の出力ファイルに保存します。
次の例では、値 5、-3、8、-2、6 を A1:E1 に書き込み、F1 に列スパークラインをレンダリングします。負の値は下向きの棒として、正の値は上向きの棒として描画されるため、プラスとマイナスの貢献を瞬時に識別できます。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Step 2: Write sample values into A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// Step 4: Add a Column sparkline to the destination cell
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);
// Step 5: Confirm the sparkline type by reading group.Type
console.log("Sparkline Type added: " + group.getType());
// Step 6: Save the workbook
workbook.save("output_column.xlsx");
console.log("Workbook saved as output_column.xlsx");
```

## **Win/Loss Sparklines**
勝敗スパークラインは、列スパークラインの特別なバリアントであり、2 つの結果のみを表示するように設計されています。正の値は「上」向きの棒 (勝ち) として描画され、ゼロまたは負の値は「下」向きの棒 (負け) として描画されます。勝敗スパークラインは、一連の勝敗、合否結果、または経時的な任意の二項結果の視覚化に一般的に使用されます。
Aspose.Cells では、`SparklineType.Stacked` を `SparklineGroups.add` メソッドに渡すことで勝敗スパークラインを作成します。(名前にかかわらず、`SparklineType.Stacked` は勝敗のレンダリングを要求するために使用される列挙値です。)
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. ソース範囲を入力します。勝敗スパークラインでは、すべての値を勝ちまたは負けのいずれかとして扱うため、値の大きさは重要ではなく、符号のみが重要です。正の値は上向きの棒になり、非正の値は下向きの棒になります。
3. 配置先セルを示す `CellArea` を作成します。
4. `worksheet.SparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)` を呼び出します。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズします (たとえば、勝ちと負けの棒のアクセントカラーを設定します)。
6. 3 つの例すべてがディスク上に共存できるように、ワークブックを別のファイル名で保存します。

```javascript
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
dest.setStartColumn(5);   // F
dest.setEndColumn(5);
dest.setStartRow(0);      // row 1
dest.setEndRow(0);
// Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
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
次の組み合わせ例では、単一のワークブックを作成し、行 1 に値 5、-3、8、-2、6 を入力し、セル F1、F2、F3 に 3 つのスパークライングループ (それぞれ異なるタイプ) を追加して、結果のファイルで 3 つのスパークラインスタイルを一度に示します。

```javascript
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
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Customize the line sparkline color via CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// Step 4: Add a Column sparkline group at F2
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Customize the column sparkline series color
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// Step 5: Add a Win/Loss (Stacked) sparkline group at F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Customize the win/loss sparkline series color
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// Step 6: Save the workbook
workbook.save("output_all.xlsx");
```

## **Customizing Sparkline Appearance**
`SparklineGroup` が作成されて `worksheet.SparklineGroups` に追加された後、ワークブックを保存する前に、その視覚的プロパティのいくつかを読み取ったり変更したりできます。最も一般的にカスタマイズされるプロパティは次のとおりです。
- **`group.Type`** — `SparklineType` (Line、Column、または Stacked)。グループは追加されるときに設定されますが、読み戻して確認することもできます。
- **`group.Line.Color`** — 線の色で、`workbook.createCellsColor()` で作成された `CellsColor` として表現されます。これはラインスパークラインの線の色に使用するプロパティです。
- **`group.Line.Weight`** — ポイント単位の線の太さ。値が大きいほど、太い線が描画されます。
- **High/Low ポイントマーカー** — 最高および最低のデータポイントに小さなマーカーを表示するフラグで、極値を強調するのに役立ちます。
- **First/Last/Negative ポイントマーカー** — 最初、最後、および負のデータポイントにマーカーを切り替えるフラグ。
色を変更するには、常に `CellsColor` インスタンスを作成し、関連するプロパティに割り当ててください。`java.awt.Color` をスパークラインの色プロパティに直接割り当てないでください — それらは `com.aspose.cells.Drawing` の `CellsColor` 型を必要とします。`SparklineGroups.add` メソッド自体が完全に型付けされた `SparklineGroup` オブジェクトを返すため、戻り値に対してプロパティ割り当てをチェーンしたり、ローカル変数に保存してカスタマイズしてから保存できます。

{{< app/cells/assistant language="javascript" >}}