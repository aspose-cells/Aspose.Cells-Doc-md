---
title: Aspose.Cells for Node.js via C++ の Aspose.Cells におけるスパークライン
linktitle: スパークライン
description: Aspose.Cells は、スプレッドシート ファイルを扱うための Node.js ライブラリであり、ワークシート セル内に配置されるミニチュア グラフであるスパークラインの作成をサポートしています。この記事では、Aspose.Cells ライブラリを使用して折れ線、縦棒、勝敗の各スパークラインを追加およびカスタマイズする方法について説明します。
keywords: Aspose.Cells, Node.js ライブラリ, スプレッドシート, スパークライン, 折れ線スパークライン, 縦棒スパークライン, 勝敗スパークライン, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ja/nodejs-cpp/creating-sparklines/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は、ワークシート セル内にスパークラインを作成することをサポートしています。スパークラインとは、単一セル内に収まるミニチュア グラフであり、データ傾向を素早く視覚的に表現するものです。Aspose.Cells は折れ線、縦棒、勝敗のスパークラインをサポートしており、それぞれを色、線の太さ、高値/安値ポイント、マーカーに関してカスタマイズできます。

{{% /alert %}}

## **はじめに**

スパークラインはセル内に表示される小さなグラフであり、完全なグラフのスペースを取らずに、行や列のデータの隣にすばやく傾向を表示したい場合に便利です。Excel は **折れ線**、**縦棒**、**勝敗** の 3 種類のスパークラインをサポートしています。Aspose.Cells は `Aspose.Cells.Charts` 名前空間にある `SparklineGroup` および `SparklineGroupCollection` API を介してこの機能を提供します。

Aspose.Cells では、追加するすべてのスパークラインが `worksheet.sparklineGroups.add(...)` によって作成され、`SparklineGroup` オブジェクトが返されます。その後、そのオブジェクトを使用してスパークラインのタイプ、データ範囲、配置先セル、および線の色、線の太さ、マーカー、高値/安値インジケーターなどの視覚的なプロパティを設定できます。

{{% alert color="primary" %}}

単一の `SparklineGroup` には、同じスタイルを共有する 1 つ以上のスパークラインを含めることができます。`add` を呼び出してデータの行と単一の配置先セルを渡すと、そのセル内に 1 つのスパークラインが作成されます。配置先の範囲が 1 セルより広い場合は、それぞれの配置先セルに個別のスパークラインが描画され、すべて同じスタイルとデータ範囲を使用します。

{{% /alert %}}

この記事を通じて、Aspose.Cells がサポートする **折れ線**、**縦棒**、**勝敗** という 3 つのスパークライン タイプそれぞれについて、その追加方法、色のカスタマイズ、結果として得られるワークブックの保存方法を説明します。

## **折れ線スパークライン**

折れ線スパークラインは、系列内のデータ ポイントを結ぶ連続した線を描画するため、時系列の傾向を示すのに最も自然な選択肢です。Aspose.Cells では、`SparklineType.Line` を `sparklineGroups.add` メソッドに渡すことで折れ線スパークラインを作成します。

ワークフローは他のスパークライン タイプと同じです。

1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. 視覚化したい値を入力データの 1 行 (たとえば 1 行目の A 列から E 列) に設定します。
3. スパークラインが描画される配置先セルを記述する `CellArea` を作成します。
4. `worksheet.sparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)` を呼び出します。3 番目の引数である `false` は、データ範囲が縦 (列) ではなく横 (行) であることを Aspose.Cells に伝えます。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズします。折れ線スパークラインの場合、`group.line.color` (`Aspose.Cells.Drawing` の `CellsColor` を必要とします) を使用して線の色を設定したり、線の太さを調整したり、高値/安値ポイント マーカーを切り替えたりできます。
6. ワークブックを保存します。

次の例では、ワークブックを作成し、セル A1 から E1 に値 5、-3、8、-2、6 を書き込んで、これらの値をトレースする折れ線スパークラインをセル F1 に追加します。また、線の色を赤にカスタマイズし、高値および安値のポイント マーカーを有効化しています。

```javascript
const AsposeCells = require("aspose.cells");

// ステップ 1: Workbookを作成し、最初のワークシートを取得する
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

// ステップ 2: セル A1:E1 にサンプルの値 5, -3, 8, -2, 6 を書き込む
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);

// ステップ 3: 出力先セル F1 を指す CellArea を作成する
const dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // 列 F（0から始まるインデックス）
dest.setEndColumn(5);
dest.setStartRow(0);      // 行 1（0から始まるインデックス）
dest.setEndRow(0);

// ステップ 4: A1:E1 から F1 へライン スパークラインを追加する
// SparklineGroups.Add は追加されたグループのインデックスを返す
const index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
const group = worksheet.getSparklineGroups().get(index);

// ステップ 5: 赤色の CellsColor を作成し、スパークラインの線の色に割り当てる
const red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);

// ステップ 6: 高値マーカーと安値マーカーを有効にする
group.setShowHighPoint(true);
group.setShowLowPoint(true);

// ステップ 7: ワークブックを保存する
workbook.save("output_line.xlsx");
```

## **縦棒スパークライン**

縦棒スパークラインは、各データ ポイントを縦棒としてレンダリングします。これにより、月の売上数値やカウントなど、値の大きさが意味を持つデータに適しています。Aspose.Cells では、`SparklineType.Column` を `sparklineGroups.add` メソッドに渡すことで縦棒スパークラインを作成します。

手順は折れ線スパークラインの例と同様です。

1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. 同じソース範囲 (A1:E1) に視覚化したい値を設定します。
3. 配置先セルを記述する `CellArea` を作成します。
4. `worksheet.sparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)` を呼び出します。
5. 必要に応じて、結果として得られる `SparklineGroup` をカスタマイズします。たとえば、`group.type` を設定してタイプを確認したり、棒の色を調整したりします。
6. 折れ線スパークラインの例を上書きしないように、ワークブックを別の出力ファイルに保存します。

以下の例では、A1:E1 に値 5、-3、8、-2、6 を書き込み、F1 に縦棒スパークラインをレンダリングします。負の値は下向きの棒として、正の値は上向きの棒として描画されるため、プラスとマイナスの寄与を一目で簡単に見分けることができます。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// ステップ2: A1:E1にサンプル値を書き込む
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// ステップ3: F1を指すCellAreaを構築する（列インデックス5、行インデックス0）
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// ステップ4: 宛先セルに縦棒スパークラインを追加する
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);

// ステップ5: group.Typeを読み取ってスパークラインの種類を確認する
console.log("Sparkline Type added: " + group.getType());

// ステップ6: ワークブックを保存する
workbook.save("output_column.xlsx");

console.log("Workbook saved as output_column.xlsx");
```

## **勝敗スパークライン**

勝敗スパークラインは、縦棒スパークラインの特殊なバリエーションであり、2 つの結果のみを表示するように設計されています。正の値は「上向き」の棒 (勝ち) として描画され、ゼロまたは負の値は「下向き」の棒 (負け) として描画されます。勝敗スパークラインは、一連の勝敗、合否結果、あるいは時系列での 2 値の結果を視覚化するためによく使用されます。

Aspose.Cells では、`SparklineType.Stacked` を `sparklineGroups.add` メソッドに渡すことで勝敗スパークラインを作成します。(名前にもかかわらず、`SparklineType.Stacked` は勝敗レンダリングを要求するために使用される列挙値です。)

手順は他の 2 つのタイプと同じです。

1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. ソース範囲に値を設定します。勝敗スパークラインではすべての値が「勝ち」または「負け」のいずれかとして扱われるため、値そのものの大きさは重要ではなく、符号のみが重要です。正の値は上向きの棒になり、非正の値は下向きの棒になります。
3. 配置先セルを記述する `CellArea` を作成します。
4. `worksheet.sparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)` を呼び出します。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズします。たとえば、勝ち棒および負け棒のアクセント色を設定します。
6. 3 つの例すべてがディスク上に共存できるよう、ワークブックを別のファイル名で保存します。

以下の例では、前の 2 つのセクションと同じ入力データを使用しています。値 5、-3、8、-2、6 はそれぞれ勝ち、負け、勝ち、負け、勝ちとして解釈され、F1 に描画されるスパークラインはそのパターンを正確に反映します。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");

// Step 2: 1行目にサンプルデータを入力: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Step 3: F1を指すCellAreaを構築 (列5, 行0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F
dest.setEndColumn(5);
dest.setStartRow(0);      // 行1
dest.setEndRow(0);

// Step 4: Win/Lossスパークラインを追加 (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest);
let group = worksheet.getSparklineGroups().get(groupIndex);

// Step 5: スパークライングループをカスタマイズ
// 高値マーカーと安値マーカーを有効化
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// 高値の色を緑に設定
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.Green);
group.setHighPointColor(highColor);

// 安値の色を赤に設定
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.Red);
group.setLowPointColor(lowColor);

// 負の値の色をオレンジに設定
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.Orange);
group.setNegativePointsColor(negColor);

// デフォルトの系列色を設定 (正の値に使用)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.SteelBlue);
group.setSeriesColor(seriesColor);

// Step 6: ワークブックを保存
workbook.save("output_winloss.xlsx");

console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **3 つのスパークライン タイプの組み合わせ**

これまでの 3 つの例はそれぞれ独自のワークブックを生成するため、出力ファイルを個別に簡単に確認できます。しかし実際のシナリオでは、複数のデータ系列を並べて比較したい場合がよくあります。これを実現するための最もクリーンな方法は、複数のスパークライン グループを同じワークシートに配置し、それぞれのグループが異なるスタイルでレンダリングされるようにすることです。

複数の `SparklineGroup` オブジェクトを同じ `SparklineGroupCollection` に追加することができ、各グループは異なる配置先セルまたは異なる範囲をターゲットにできます。たとえば、F1 に折れ線スパークライン、F2 に縦棒スパークライン、F3 に勝敗スパークラインを配置し、すべて 1 行目の同じソース データから読み取るようにすれば、閲覧者は同じ数値に対する 3 つの異なる視覚的表現を確認できます。

以下の組み合わせ例では、単一のワークブックを作成し、1 行目に値 5、-3、8、-2、6 を設定し、F1、F2、F3 のセルに 3 つのスパークライン グループ (各タイプ 1 つずつ) を追加して、結果として得られるファイルが 3 つのスパークライン スタイルすべてを一度に示すようにしています。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// ステップ2: 1行目 (A1:E1) にサンプルデータを入力
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// ステップ3: F1に折れ線スパークライングループを追加
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// CellsColorを使用して折れ線スパークラインの色をカスタマイズ
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.Blue);
lineGroup.setSeriesColor(lineColor);

// ステップ4: F2に縦棒スパークライングループを追加
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// 縦棒スパークラインシリーズの色をカスタマイズ
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.Green);
columnGroup.setSeriesColor(columnColor);

// ステップ5: F3にWin/Loss (積み上げ) スパークライングループを追加
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Win/Lossスパークラインシリーズの色をカスタマイズ
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.DarkOrange);
stackedGroup.setSeriesColor(stackedColor);

// ステップ6: ワークブックを保存
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

1 つのワークシート内に複数のスパークライン グループを組み合わせる場合、各グループは独立しています。同じソース範囲を共有することも、異なるソース範囲を使用することもでき、個別にスタイルを設定できます。これにより、既存のワークシート内に小さな「ダッシュボード」形式のセル内ビジュアライゼーションを簡単に構築できます。

{{% /alert %}}

## **スパークラインの外観のカスタマイズ**

`SparklineGroup` が作成されて `worksheet.sparklineGroups` に追加されたら、ワークブックを保存する前にその視覚的なプロパティのいくつかを読み取ったり変更したりできます。最も一般的にカスタマイズされるプロパティは次のとおりです。

- **`group.type`** — `SparklineType` (Line、Column、または Stacked)。グループは追加時に設定されますが、読み戻して確認することができます。
- **`group.line.color`** — `workbook.createCellsColor()` を介して作成された `CellsColor` として表される線の色。これは折れ線スパークラインの線の色を設定するためのプロパティです。
- **`group.line.weight`** — ポイント単位の線の太さ。値を大きくすると線が太くなります。
- **高値/安値ポイント マーカー** — 最高および最低データ ポイントに小さなマーカーを表示するフラグで、極値を強調するのに役立ちます。
- **最初/最後/負のポイント マーカー** — 最初、最後、および負のデータ ポイントにマーカーを切り替えるフラグ。

色を変更するには、常に `CellsColor` インスタンスを作成し、関連するプロパティに割り当ててください。`System.Drawing.Color` をスパークラインの色プロパティに直接割り当てないでください。これらのプロパティは `Aspose.Cells.Drawing` の `CellsColor` 型を必要とします。`sparklineGroups.add` メソッド自体は完全に型付けされた `SparklineGroup` オブジェクトを返すため、戻り値に対してプロパティの割り当てをチェーンしたり、ローカル変数に保存して保存前にカスタマイズしたりすることができます。

{{< app/cells/assistant language="javascript" >}}