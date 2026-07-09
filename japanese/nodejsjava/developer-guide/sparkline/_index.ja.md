---
title: Aspose.Cells for Node.js via Java での Aspose.Cells におけるスパークライン
linktitle: Sparklines
description: Aspose.Cells は、ワークシートセル内に配置されるミニチュアチャートであるスパークラインの作成をサポートする、スプレッドシートファイルを扱うための Node.js via Java ライブラリです。この記事では、Aspose.Cells ライブラリを使用して、ライン、列、勝敗の各スパークラインを追加およびカスタマイズする方法について説明します。
keywords: Aspose.Cells, Node.js via Java ライブラリ, スプレッドシート, スパークライン, ラインスパークライン, 列スパークライン, 勝敗スパークライン, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ja/nodejs-java/creating-sparklines/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は、ワークシートセル内でのスパークラインの作成をサポートしています。スパークラインは単一セルに収まるミニチュアチャートであり、データ傾向を素早く視覚的に表現します。Aspose.Cells はライン、列、勝敗の各スパークラインをサポートしており、それぞれを色、線の太さ、高値/安値、マーカーに関してカスタマイズできます。

{{% /alert %}}

## **はじめに**

スパークラインはセル内に収まる小さなチャートであり、完全なチャート分のスペースを取らずに行や列のデータの隣に素早く傾向を表示したい場合に便利です。Excel は **ライン**、**列**、**勝敗** の 3 種類のスパークラインをサポートしています。Aspose.Cells は `com.aspose.cells.Charts` 名前空間にある `SparklineGroup` および `SparklineGroupCollection` API を通じてこの機能を提供します。

Aspose.Cells では、追加するすべてのスパークラインが `worksheet.SparklineGroups.add(...)` を通じて作成され、これにより `SparklineGroup` オブジェクトが返されます。そのオブジェクトを使用して、スパークラインのタイプ、データ範囲、配置先セル、および線の色、線の太さ、マーカー、高値/安値インジケーターなどの視覚的なプロパティを設定できます。

{{% alert color="primary" %}}

1 つの `SparklineGroup` には、同じスタイルを共有する 1 つ以上のスパークラインを含めることができます。`add` を呼び出してデータの行と 1 つの配置先セルを渡すと、そのセル内に 1 つのスパークラインが作成されます。配置先の範囲が 1 セルより広い場合は、各配置先セルに別々のスパークラインが描画され、すべて同じスタイルとデータ範囲を使用します。

{{% /alert %}}

この記事を通じて、Aspose.Cells でサポートされている 3 種類のスパークラインタイプ (**ライン**、**列**、**勝敗**) それぞれについて、追加方法、色のカスタマイズ方法、結果のワークブックの保存方法を説明します。

## **ラインスパークライン**

ラインスパークラインは、系列のデータポイントを通る連続した線を描画するため、経時的な傾向を示すのに最も自然な選択肢です。Aspose.Cells では、`SparklineType.Line` を `SparklineGroups.add` メソッドに渡すことでラインスパークラインが作成されます。

ワークフローは他のスパークラインタイプと同じです。

1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. 視覚化したい値を使用して、ソースデータの行 (たとえば、1 行目の A 列から E 列) に値を設定します。
3. スパークラインが描画される配置先セルを表す `CellArea` を作成します。
4. `worksheet.SparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)` を呼び出します。3 番目の引数 `false` は、データ範囲が水平 (行) であり、垂直 (列) ではないことを Aspose.Cells に伝えます。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズします。ラインスパークラインの場合、`group.Line.Color` (`com.aspose.cells.Drawing` の `CellsColor` を必要とします) を使用して線の色を設定したり、線の太さを調整したり、高値/安値マーカーを切り替えたりできます。
6. ワークブックを保存します。

次の例では、ワークブックを作成し、セル A1 から E1 に値 5、-3、8、-2、6 を書き込み、これらの値をトレースするラインスパークラインをセル F1 に追加します。また、線の色を赤にカスタマイズし、高値および安値のマーカーを有効にします。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();

// ステップ 2: サンプル値 5、-3、8、-2、6 をセル A1:E1 に書き込みます
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);

// ステップ 3: 宛先セル F1 を指す CellArea を作成します
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // 列 F (0 から始まるインデックス)
dest.setEndColumn(5);
dest.setStartRow(0);      // 行 1 (0 から始まるインデックス)
dest.setEndRow(0);

// ステップ 4: A1:E1 から F1 に折れ線スパークラインを追加します
// SparklineGroups.Add は新しく追加されたグループのインデックスを返します
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(index);

// ステップ 5: 赤色の CellsColor を作成し、スパークラインの線の色に割り当てます
let red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);

// ステップ 6: 高値マーカーと安値マーカーを有効にします
group.setShowHighPoint(true);
group.setShowLowPoint(true);

// ステップ 7: ワークブックを保存します
workbook.save("output_line.xlsx");
```

## **列スパークライン**

列スパークラインは、各データポイントを垂直バーとしてレンダリングします。そのため、データの大きさが意味を持つ場合 (たとえば、月次売上やカウントなど) に適しています。Aspose.Cells では、`SparklineType.Column` を `SparklineGroups.add` メソッドに渡すことで列スパークラインが作成されます。

手順はラインスパークラインの例と同様です。

1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. 同じソース範囲 (A1:E1) に視覚化したい値を設定します。
3. 配置先セルを表す `CellArea` を作成します。
4. `worksheet.SparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)` を呼び出します。
5. 必要に応じて、結果の `SparklineGroup` をカスタマイズします (たとえば、`group.Type` を設定してタイプを確認したり、棒の色を調整したりします)。
6. ラインスパークラインの例を上書きしないように、ワークブックを別の出力ファイルに保存します。

次の例では、A1:E1 に値 5、-3、8、-2、6 を書き込み、F1 に列スパークラインを描画します。負の値は下向きの棒として、正の値は上向きの棒として描画されるため、プラスとマイナスの寄与を一目で簡単に識別できます。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// ステップ2: A1:E1にサンプル値を入力
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// ステップ3: F1（列インデックス5、行インデックス0）を指すCellAreaを構築
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// ステップ4: 宛先セルに縦棒スパークラインを追加
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);

// ステップ5: group.Typeを読み取ってスパークラインの種類を確認
console.log("Sparkline Type added: " + group.getType());

// ステップ6: ワークブックを保存
workbook.save("output_column.xlsx");

console.log("Workbook saved as output_column.xlsx");
```

## **勝敗スパークライン**

勝敗スパークラインは、列スパークラインの特殊なバリアントであり、2 つの結果のみを表示するように設計されています。正の値は「上向き」バー (勝ち) として描画され、ゼロまたは負の値は「下向き」バー (負け) として描画されます。勝敗スパークラインは、一連の勝敗、合否結果、または経時的なバイナリ結果を視覚化するためによく使用されます。

Aspose.Cells では、`SparklineType.Stacked` を `SparklineGroups.add` メソッドに渡すことで勝敗スパークラインが作成されます。(名前にもかかわらず、`SparklineType.Stacked` は勝敗レンダリングを要求するために使用される列挙値です。)

手順は他の 2 種類と同じです。

1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. ソース範囲に値を設定します。勝敗スパークラインはすべての値を勝ちまたは負けとして扱うため、値の絶対値は重要ではなく、符号のみが重要です。正の値は上向きバーになり、非正の値は下向きバーになります。
3. 配置先セルを表す `CellArea` を作成します。
4. `worksheet.SparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)` を呼び出します。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズします (たとえば、勝ちバーと負けバーのアクセント色を設定します)。
6. 3 つの例すべてがディスク上に共存できるように、ワークブックを異なるファイル名で保存します。

次の例では、前の 2 つのセクションと同じ入力データを使用します。値 5、-3、8、-2、6 は勝ち、負け、勝ち、負け、勝ちとして解釈され、F1 に描画されるスパークラインはそのパターンを正確に反映します。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");

// ステップ2: 行1にサンプルデータを入力: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// ステップ3: F1を指すCellAreaを構築 (列5, 行0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F
dest.setEndColumn(5);
dest.setStartRow(0);      // 行1
dest.setEndRow(0);

// ステップ4: Win/Lossスパークラインを追加 (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest
);
let group = worksheet.getSparklineGroups().get(groupIndex);

// ステップ5: スパークライングループをカスタマイズ
// 高値と低値のマーカーを有効化
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// 高値の色を緑に設定
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.getGreen());
group.setHighPointColor(highColor);

// 低値の色を赤に設定
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.getRed());
group.setLowPointColor(lowColor);

// 負の値の色をオレンジに設定
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.getOrange());
group.setNegativePointsColor(negColor);

// デフォルトの系列色を設定 (正のバーに使用)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.getSteelBlue());
group.setSeriesColor(seriesColor);

// ステップ6: ワークブックを保存
workbook.save("output_winloss.xlsx");

console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **3 種類のスパークラインタイプの組み合わせ**

前の 3 つの例はそれぞれ独自のワークブックを生成するため、出力ファイルを個別に簡単に確認できます。ただし、実際のシナリオでは、複数のデータ系列を並べて比較したい場合がよくあります。これを行う最もクリーンな方法は、複数のスパークライングループを同じワークシートに配置し、各グループが異なるスタイルをレンダリングすることです。

複数の `SparklineGroup` オブジェクトを同じ `SparklineGroupCollection` に追加でき、各グループは異なる配置先セルまたは異なる範囲を対象とすることができます。たとえば、F1 にラインスパークライン、F2 に列スパークライン、F3 に勝敗スパークラインを配置し、すべて 1 行目の同じソースデータを読み取るようにすれば、読者に対して同じ数値の 3 つの異なる視覚的表現を示すことができます。

次の組み合わせ例では、単一のワークブックを作成し、1 行目に値 5、-3、8、-2、6 を設定してから、F1、F2、F3 のセルに 3 つのスパークライングループ (各タイプ 1 つずつ) を追加し、結果のファイルが 3 つのスパークラインスタイルを一度に示します。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// ステップ2: 1行目(A1:E1)にサンプルデータを入力する
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
lineColor.setColor(AsposeCells.Color.getBlue());
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
columnColor.setColor(AsposeCells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);

// ステップ5: F3に勝敗(積み上げ)スパークライングループを追加する
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// 勝敗スパークラインシリーズの色をカスタマイズする
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);

// ステップ6: ワークブックを保存する
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

1 つのワークシートで複数のスパークライングループを組み合わせる場合、各グループは独立しています。同じソース範囲を共有することも、異なるソース範囲を使用することもでき、独立してスタイルを設定できます。これにより、既存のワークシート内に直接、セルの視覚化の小さな「ダッシュボード」を簡単に構築できます。

{{% /alert %}}

## **スパークラインの外観のカスタマイズ**

`SparklineGroup` が作成されて `worksheet.SparklineGroups` に追加された後、ワークブックを保存する前にその視覚的なプロパティのいくつかを読み取ったり変更したりできます。一般的にカスタマイズされるプロパティは次のとおりです。

- **`group.Type`** — `SparklineType` (Line、Column、または Stacked)。これはグループの追加時に設定されますが、読み取って確認することができます。
- **`group.Line.Color`** — 線の色で、`workbook.createCellsColor()` を通じて作成された `CellsColor` として表現されます。これはラインスパークラインの線の色に使用するプロパティです。
- **`group.Line.Weight`** — ポイント単位の線の太さ。値が大きいほど線が太くなります。
- **高値/安値マーカー** — 最高データポイントと最低データポイントに小さなマーカーをオンにするフラグで、極値を強調するのに役立ちます。
- **始点/終点/負のポイントマーカー** — 始点、終点、負のデータポイントにマーカーを切り替えるフラグ。

色を変更するには、常に `CellsColor` インスタンスを作成し、関連するプロパティに割り当ててください。`java.awt.Color` をスパークラインの色プロパティに直接割り当てないでください。これらは `com.aspose.cells.Drawing` の `CellsColor` 型を必要とします。`SparklineGroups.add` メソッド自体は完全に型付けされた `SparklineGroup` オブジェクトを返すため、戻り値にプロパティ割り当てをチェーンしたり、ローカル変数に保存して保存前にカスタマイズしたりできます。



{{< app/cells/assistant language="javascript" >}}javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();

// ステップ 2: サンプル値 5、-3、8、-2、6 をセル A1:E1 に書き込みます
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);

// ステップ 3: 宛先セル F1 を指す CellArea を作成します
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // 列 F (0 から始まるインデックス)
dest.setEndColumn(5);
dest.setStartRow(0);      // 行 1 (0 から始まるインデックス)
dest.setEndRow(0);

// ステップ 4: A1:E1 から F1 に折れ線スパークラインを追加します
// SparklineGroups.Add は新しく追加されたグループのインデックスを返します
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(index);

// ステップ 5: 赤色の CellsColor を作成し、スパークラインの線の色に割り当てます
let red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);

// ステップ 6: 高値マーカーと安値マーカーを有効にします
group.setShowHighPoint(true);
group.setShowLowPoint(true);

// ステップ 7: ワークブックを保存します
workbook.save("output_line.xlsx");javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// ステップ2: A1:E1にサンプル値を入力
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// ステップ3: F1（列インデックス5、行インデックス0）を指すCellAreaを構築
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// ステップ4: 宛先セルに縦棒スパークラインを追加
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);

// ステップ5: group.Typeを読み取ってスパークラインの種類を確認
console.log("Sparkline Type added: " + group.getType());

// ステップ6: ワークブックを保存
workbook.save("output_column.xlsx");

console.log("Workbook saved as output_column.xlsx");javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");

// ステップ2: 行1にサンプルデータを入力: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// ステップ3: F1を指すCellAreaを構築 (列5, 行0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F
dest.setEndColumn(5);
dest.setStartRow(0);      // 行1
dest.setEndRow(0);

// ステップ4: Win/Lossスパークラインを追加 (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest
);
let group = worksheet.getSparklineGroups().get(groupIndex);

// ステップ5: スパークライングループをカスタマイズ
// 高値と低値のマーカーを有効化
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// 高値の色を緑に設定
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.getGreen());
group.setHighPointColor(highColor);

// 低値の色を赤に設定
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.getRed());
group.setLowPointColor(lowColor);

// 負の値の色をオレンジに設定
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.getOrange());
group.setNegativePointsColor(negColor);

// デフォルトの系列色を設定 (正のバーに使用)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.getSteelBlue());
group.setSeriesColor(seriesColor);

// ステップ6: ワークブックを保存
workbook.save("output_winloss.xlsx");

console.log("Workbook saved successfully: output_winloss.xlsx");javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// ステップ2: 1行目(A1:E1)にサンプルデータを入力する
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
lineColor.setColor(AsposeCells.Color.getBlue());
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
columnColor.setColor(AsposeCells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);

// ステップ5: F3に勝敗(積み上げ)スパークライングループを追加する
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// 勝敗スパークラインシリーズの色をカスタマイズする
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);

// ステップ6: ワークブックを保存する
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

1 つのワークシートで複数のスパークライングループを組み合わせる場合、各グループは独立しています。同じソース範囲を共有することも、異なるソース範囲を使用することもでき、独立してスタイルを設定できます。これにより、既存のワークシート内に直接、セルの視覚化の小さな「ダッシュボード」を簡単に構築できます。

{{% /alert %}}

## **スパークラインの外観のカスタマイズ**

`SparklineGroup` が作成されて `worksheet.SparklineGroups` に追加された後、ワークブックを保存する前にその視覚的なプロパティのいくつかを読み取ったり変更したりできます。一般的にカスタマイズされるプロパティは次のとおりです。

- **`group.Type`** — `SparklineType` (Line、Column、または Stacked)。これはグループの追加時に設定されますが、読み取って確認することができます。
- **`group.Line.Color`** — 線の色で、`workbook.createCellsColor()` を通じて作成された `CellsColor` として表現されます。これはラインスパークラインの線の色に使用するプロパティです。
- **`group.Line.Weight`** — ポイント単位の線の太さ。値が大きいほど線が太くなります。
- **高値/安値マーカー** — 最高データポイントと最低データポイントに小さなマーカーをオンにするフラグで、極値を強調するのに役立ちます。
- **始点/終点/負のポイントマーカー** — 始点、終点、負のデータポイントにマーカーを切り替えるフラグ。

色を変更するには、常に `CellsColor` インスタンスを作成し、関連するプロパティに割り当ててください。`java.awt.Color` をスパークラインの色プロパティに直接割り当てないでください。これらは `com.aspose.cells.Drawing` の `CellsColor` 型を必要とします。`SparklineGroups.add` メソッド自体は完全に型付けされた `SparklineGroup` オブジェクトを返すため、戻り値にプロパティ割り当てをチェーンしたり、ローカル変数に保存して保存前にカスタマイズしたりできます。



{{< app/cells/assistant language="javascript" >}}