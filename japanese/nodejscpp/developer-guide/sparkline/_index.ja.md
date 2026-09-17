---
title: Aspose.Cells for Node.js via C++ でのスパークライン
linktitle: Aspose.Cells for Node.js via C++ でのスパークライン
description: Aspose.Cells は、ワークシートセル内に配置されるミニグラフであるスパークラインの作成をサポートするスプレッドシート操作用の Node.js ライブラリです。この記事では、Aspose.Cells ライブラリを使用して、折れ線、縦棒、勝敗の各スパークラインを追加およびカスタマイズする方法を説明します。
keywords: Aspose.Cells, Node.js ライブラリ, スプレッドシート, スパークライン, 折れ線スパークライン, 縦棒スパークライン, 勝敗スパークライン, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ja/nodejs-cpp/creating-sparklines/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells はワークシートセル内にスパークラインを作成することをサポートします。スパークラインは 1 つのセル内に収まるミニグラフであり、データ傾向を素早く視覚的に表現します。Aspose.Cells は折れ線、縦棒、勝敗の各スパークラインをサポートしており、それぞれを色、線の太さ、高値/安値、マーカーに関してカスタマイズできます。

## **はじめに**
スパークラインはセル内に収まる小さなグラフで、行や列のデータの隣に完全なグラフほどのスペースを取らずに迅速な傾向を表示したい場合に便利です。Excel は **折れ線**、**縦棒**、**勝敗** の 3 種類のスパークラインをサポートします。Aspose.Cells は `Aspose.Cells.Charts` 名前空間にある `SparklineGroup` および `SparklineGroupCollection` API を介してこの機能を提供します。
Aspose.Cells では、追加するすべてのスパークラインが `worksheet.sparklineGroups.add(...)` を通じて作成され、`SparklineGroup` オブジェクトが返されます。そのオブジェクトを使用して、スパークラインの種類、データ範囲、出力先セル、および線の色、線の太さ、マーカー、高値/安値インジケーターなどの視覚プロパティを設定できます。
Aspose.Cells がサポートする 3 種類のスパークライン — **折れ線**、**縦棒**、**勝敗** — のそれぞれを順に追加し、色をカスタマイズし、結果として得られるワークブックを保存する方法を説明します。

## **折れ線スパークライン**
折れ線スパークラインは、系列のデータ点を結ぶ連続した線を描画し、時間の経過に伴う傾向を示すのに最も自然な選択肢です。Aspose.Cells では、`sparklineGroups.add` メソッドに `SparklineType.Line` を渡すことで折れ線スパークラインが作成されます。
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. 視覚化したい値（たとえば 1 行目の A 列から E 列）にデータ行を入力します。
3. スパークラインが描画される出力先セルを示す `CellArea` を構築します。
4. `worksheet.sparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)` を呼び出します。3 番目の引数 — `false` — は、データ範囲が縦（列）ではなく横（行）であることを Aspose.Cells に伝えます。
5. 必要に応じて返された `SparklineGroup` をカスタマイズします。折れ線スパークラインの場合は、`group.line.color`（`Aspose.Cells.Drawing` の `CellsColor` を必要とします）を使用して線の色を設定したり、線の太さを調整したり、高値/安値マーカーを切り替えたりできます。
6. ワークブックを保存します。
次の例は、ワークブックを作成し、セル A1 から E1 に値 5、-3、8、-2、6 を書き込み、それらの値をトレースする折れ線スパークラインをセル F1 に追加します。また、線の色を赤にカスタマイズし、高値および安値のマーカーを有効化します。

```javascript
const AsposeCells = require("aspose.cells");
// ステップ1: Workbookを作成し、最初のワークシートを取得する
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// ステップ2: サンプル値5、-3、8、-2、6をセルA1:E1に書き込む
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// ステップ3: 宛先セルF1を指すCellAreaを構築する
const dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // 列F（0から始まるインデックス）
dest.setEndColumn(5);
dest.setStartRow(0);      // 行1（0から始まるインデックス）
dest.setEndRow(0);
// ステップ4: A1:E1からF1にLineスパークラインを追加する
// SparklineGroups.Addは新しく追加されたグループのインデックスを返す
const index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
const group = worksheet.getSparklineGroups().get(index);
// ステップ5: 赤いCellsColorを作成し、スパークラインの線の色に割り当てる
const red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);
// ステップ6: 高点と低点のマーカーを有効にする
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// ステップ7: ワークブックを保存する
workbook.save("output_line.xlsx");
```

## **縦棒スパークライン**
縦棒スパークラインは各データ点を縦棒としてレンダリングします。そのため、月次売上やカウントなど、値の大きさが意味を持つデータに適しています。Aspose.Cells では、`sparklineGroups.add` メソッドに `SparklineType.Column` を渡すことで縦棒スパークラインが作成されます。
手順は折れ線スパークラインの例と同様です。
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
3. 出力先セルを示す `CellArea` を構築します。
4. `worksheet.sparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)` を呼び出します。
5. 必要に応じて結果の `SparklineGroup` をカスタマイズします — たとえば、`group.type` を設定して種類を確認したり、棒の色を調整したりします。
6. ワークブックを別の出力ファイルに保存し、折れ線スパークラインの例を上書きしないようにします。
以下の例では、値 5、-3、8、-2、6 を A1:E1 に書き込み、F1 に縦棒スパークラインを描画します。負の値は下向きの棒として、正の値は上向きの棒として描かれるため、寄与の正負を一目で簡単に見分けられます。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// ステップ 2: A1:E1 にサンプル値を書き込む
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// ステップ 3: F1 (列インデックス 5、行インデックス 0) を指す CellArea を作成する
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// ステップ 4: 目的セルに縦棒スパークラインを追加する
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);
// ステップ 5: group.Type を読み取ってスパークラインの種類を確認する
console.log("Sparkline Type added: " + group.getType());
// ステップ 6: ワークブックを保存する
workbook.save("output_column.xlsx");
console.log("Workbook saved as output_column.xlsx");
```

## **勝敗スパークライン**
勝敗スパークラインは、2 つの結果のみを表示するように設計された縦棒スパークラインの特殊なバリアントです。正の値は「上」バー（勝ち）として、ゼロまたは負の値は「下」バー（負け）として描画されます。勝敗スパークラインは、一連の勝ち負け、合否結果、または時間の経過に伴う任意の二項結果を視覚化するためによく使用されます。
Aspose.Cells では、`sparklineGroups.add` メソッドに `SparklineType.Stacked` を渡すことで勝敗スパークラインが作成されます。（名前とは裏腹に、`SparklineType.Stacked` は勝敗レンダリングを要求するために使用される列挙値です。）
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. ソース範囲を入力します。勝敗スパークラインではすべての値を勝ちまたは負けのいずれかとして扱うため、値の絶対値ではなく符号のみが重要になります。正の値は上バー、非正の値は下バーになります。
3. 出力先セルを示す `CellArea` を構築します。
4. `worksheet.sparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)` を呼び出します。
5. 必要に応じて返された `SparklineGroup` をカスタマイズします。たとえば、勝ちバーと負けバーのアクセント色を設定します。
6. ワークブックを別のファイル名で保存し、3 つの例すべてがディスク上に共存できるようにします。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// ステップ2: 1行目にサンプルデータを入力: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// ステップ3: F1を指すCellAreaを構築する(列5、行0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F
dest.setEndColumn(5);
dest.setStartRow(0);      // 1行目
dest.setEndRow(0);
// ステップ4: 勝ち/負けのスパークラインを追加(SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest);
let group = worksheet.getSparklineGroups().get(groupIndex);
// ステップ5: スパークライングループをカスタマイズ
// 高値マーカーと安値マーカーを有効化
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// 高値マーカーの色を緑に設定
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.Green);
group.setHighPointColor(highColor);
// 安値マーカーの色を赤に設定
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.Red);
group.setLowPointColor(lowColor);
// 負のポイントの色をオレンジに設定
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.Orange);
group.setNegativePointsColor(negColor);
// デフォルトの系列の色を設定(プラスのバーに使用)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.SteelBlue);
group.setSeriesColor(seriesColor);
// ステップ6: ワークブックを保存
workbook.save("output_winloss.xlsx");
console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **3 種類のスパークラインの組み合わせ**
以下の結合例は、単一のワークブックを作成し、1 行目に値 5、-3、8、-2、6 を入力し、セル F1、F2、F3 に 3 つのスパークライン グループ（各種類 1 つずつ）を追加します。結果として得られるファイルは 3 種類のスパークライン スタイルすべてを一度に示します。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// ステップ2: 1行目（A1:E1）にサンプルデータを入力する
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// ステップ3: F1に折れ線スパークライングループを追加する
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// CellsColorを使用して折れ線スパークラインの色をカスタマイズする
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.Blue);
lineGroup.setSeriesColor(lineColor);
// ステップ4: F2に縦棒スパークライングループを追加する
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// 縦棒スパークラインシリーズの色をカスタマイズする
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.Green);
columnGroup.setSeriesColor(columnColor);
// ステップ5: F3に勝敗（積み上げ）スパークライングループを追加する
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// 勝敗スパークラインシリーズの色をカスタマイズする
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.DarkOrange);
stackedGroup.setSeriesColor(stackedColor);
// ステップ6: ワークブックを保存する
workbook.save("output_all.xlsx");
```

## **スパークライン外観のカスタマイズ**
`SparklineGroup` が作成されて `worksheet.sparklineGroups` に追加された後、ワークブックを保存する前にいくつかの視覚プロパティを読み取ったり変更したりできます。最も一般的にカスタマイズされるプロパティは次のとおりです。
- **`group.type`** — `SparklineType`（Line、Column、または Stacked）。グループ追加時に設定されますが、読み戻して確認できます。
- **`group.line.color`** — 線の色。`workbook.createCellsColor()` で作成された `CellsColor` として表現されます。これは折れ線スパークラインの線の色に使用するプロパティです。
- **`group.line.weight`** — ポイント単位の線の太さ。値が大きいほど線が太くなります。
- **高値/安値マーカー** — 最高および最低データ点に小さなマーカーを表示するフラグ。極端な値を強調する場合に便利です。
- **最初/最後/負のデータ点マーカー** — 最初、最後、負のデータ点にマーカーを切り替えるフラグ。
色を変更するには、常に `CellsColor` インスタンスを作成し、該当するプロパティに割り当ててください。`System.Drawing.Color` を直接スパークラインの色プロパティに代入しないでください。それらは `Aspose.Cells.Drawing` の `CellsColor` 型を必要とします。`sparklineGroups.add` メソッド自体は完全に型付けされた `SparklineGroup` オブジェクトを返すため、戻り値にプロパティ割り当てを連鎖させることも、ローカル変数に保存して保存前にカスタマイズすることもできます。
{{% /alert %}}

{{< app/cells/assistant language="javascript" >}}