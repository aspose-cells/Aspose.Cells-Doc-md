---
title: Aspose.Cells for Java のスパークライン
linktitle: Aspose.Cells for Java のスパークライン
description: Aspose.Cells は、ワークシートセル内に配置するミニチュアチャートであるスパークラインの作成に対応した、スプレッドシートファイルを扱うための Java ライブラリです。本記事では、Aspose.Cells ライブラリを使用して、折れ線、縦棒、勝敗のスパークラインを追加しカスタマイズする方法を説明します。
keywords: Aspose.Cells, Java ライブラリ, スプレッドシート, スパークライン, 折れ線スパークライン, 縦棒スパークライン, 勝敗スパークライン, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ja/java/creating-sparklines/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells はワークシートセル内でのスパークライン作成をサポートしています。スパークラインは 1 つのセルに収まるミニチュアチャートであり、データ傾向を素早く視覚的に表現します。Aspose.Cells は折れ線、縦棒、勝敗のスパークラインをサポートしており、それぞれを色、線の太さ、高値/安値ポイント、マーカーなどに関してカスタマイズできます。

## **はじめに**
スパークラインはセル内に表示される小さなチャートで、完全なチャートほどのスペースを取らずに、行や列のデータの隣に簡単な傾向を示したい場合に役立ちます。Excel は **折れ線**、**縦棒**、**勝敗** という 3 種類のスパークラインをサポートしています。Aspose.Cells も `Aspose.Cells.Charts` 名前空間にある `SparklineGroup` および `SparklineGroupCollection` API によってこの機能を提供します。
Aspose.Cells では、追加するすべてのスパークラインが `worksheet.getSparklineGroups().add(...)` を通じて作成され、`SparklineGroup` オブジェクトが返されます。その後、そのオブジェクトを使用してスパークラインの種類、データ範囲、配置先セル、線の色や線の太さ、マーカー、高値/安値ポイントインジケーターなどの視覚的なプロパティを設定できます。
本記事では、Aspose.Cells でサポートされている 3 種類のスパークライン — **折れ線**、**縦棒**、**勝敗** — のそれぞれについて、追加方法、色のカスタマイズ方法、そして結果として得られるワークブックの保存方法を順に説明します。

## **折れ線スパークライン**
折れ線スパークラインは、系列のデータ点を結ぶ連続した線を引くものであり、時間の経過に伴う傾向を示すために最も自然な選択肢です。Aspose.Cells では、`add` メソッドに `SparklineType.LINE` を渡すことで折れ線スパークラインを作成します。
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. 視覚化したい値を用いて、ソースデータの行（例えば 1 行目の A 列から E 列）を埋めます。
3. スパークラインが描画される配置先セルを記述する `CellArea` を作成します。
4. `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)` を呼び出します。3 番目の引数である `false` は、データ範囲が縦方向（列）ではなく横方向（行）であることを Aspose.Cells に伝えます。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズします。折れ線スパークラインの場合、`group.getLine().setColor(...)`（`Aspose.Cells.Drawing` の `CellsColor` を引数に取ります）を使用して線の色を設定したり、線の太さを調整したり、高値/安値ポイントのマーカーを切り替えたりできます。
6. ワークブックを保存します。
次の例では、ワークブックを作成し、セル A1 から E1 に値 5、-3、8、-2、6 を書き込んで、それらの値をトレースする折れ線スパークラインをセル F1 に追加します。また、線の色を赤にカスタマイズし、高値および安値のポイントにマーカーを有効化しています。

```java
public class CodeRunner {
    public static void main(String[] args) {
        try {
            // ステップ1: Workbookを作成し、最初のワークシートを取得します
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.getWorksheets().get(0);
            Cells cells = worksheet.getCells();
            // ステップ2: セルA1:E1にサンプル値 5、-3、8、-2、6 を書き込みます
            cells.get("A1").putValue(5);
            cells.get("B1").putValue(-3);
            cells.get("C1").putValue(8);
            cells.get("D1").putValue(-2);
            cells.get("E1").putValue(6);
            // ステップ3: コピー先セルF1を指すCellAreaを構築します
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // 列F（0から始まるインデックス）
            dest.EndColumn = 5;
            dest.StartRow = 0;      // 行1（0から始まるインデックス）
            dest.EndRow = 0;
            // ステップ4: A1:E1からF1に折れ線スパークラインを追加します
            // SparklineGroups.addは新しく追加されたグループのインデックスを返します
            int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
            SparklineGroup group = worksheet.getSparklineGroups().get(index);
            // ステップ5: 赤色のCellsColorを作成し、スパークラインの線の色に割り当てます
            CellsColor red = workbook.createCellsColor();
            red.setColor(com.aspose.cells.Color.getRed());
            group.setSeriesColor(red);
            // ステップ6: 高値マーカーと低値マーカーを有効にします
            group.setShowHighPoint(true);
            group.setShowLowPoint(true);
            // ステップ7: ワークブックを保存します
            workbook.save("output_line.xlsx");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

## **縦棒スパークライン**
縦棒スパークラインは、各データ点を縦の棒として描画します。そのため、値の大きさが意味を持つデータ（たとえば月次の売上数値や件数）の表示に適しています。Aspose.Cells では、`add` メソッドに `SparklineType.COLUMN` を渡すことで縦棒スパークラインを作成します。
手順は折れ線スパークラインの例と同じです。
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
3. 配置先セルを記述する `CellArea` を作成します。
4. `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)` を呼び出します。
5. 必要に応じて、結果として得られた `SparklineGroup` をカスタマイズします。例えば、`group.getType()` を設定して種類を確認したり、棒の色を調整したりできます。
6. 折れ線スパークラインの例を上書きしないように、ワークブックを別の出力ファイルに保存します。
以下の例では、値 5、-3、8、-2、6 を A1:E1 に書き込み、F1 に縦棒スパークラインを描画します。負の値は下向きの棒として、正の値は上向きの棒として描かれるため、プラスとマイナスの寄与を一目で簡単に見分けられます。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// A1:E1にサンプル値を入力
int[] values = new int[] { 5, -3, 8, -2, 6 };
for (int i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// F1を指すCellAreaを構築（列インデックス5、行インデックス0）
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// 目的セルにColumnスパークラインを追加
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);
// group.Typeを読み取ってスパークラインのタイプを確認
System.out.println("Sparkline Type added: " + group.getType());
// ワークブックを保存
workbook.save("output_column.xlsx");
System.out.println("Workbook saved as output_column.xlsx");
```

## **勝敗スパークライン**
勝敗スパークラインは、2 つの結果だけを示すために設計された縦棒スパークラインの特別なバリエーションです。正の値は「上」向きの棒（勝ち）として、ゼロまたは負の値は「下」向きの棒（負け）として描画されます。勝敗スパークラインは、勝ち負けの連続、合格/不合格の結果、あるいは任意の二項結果の時系列を視覚化するためによく使用されます。
Aspose.Cells では、`add` メソッドに `SparklineType.STACKED` を渡すことで勝敗スパークラインを作成します（名称とは裏腹に、勝敗のレンダリングを要求するための列挙値は `SparklineType.STACKED` です）。
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. ソース範囲を埋めます。勝敗スパークラインはすべての値を勝ちまたは負けのどちらかとして扱うため、値の絶対値は重要ではなく、符号のみが重要です。正の値は上向きの棒になり、非正の値は下向きの棒になります。
3. 配置先セルを記述する `CellArea` を作成します。
4. `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)` を呼び出します。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズします。例えば、勝ちと負けの棒のアクセントカラーを設定します。
6. 3 つの例すべてをディスク上で共存させられるよう、ワークブックを別のファイル名で保存します。

```java
import com.aspose.cells.*;
import com.aspose.cells.charts.*;
import com.aspose.cells.drawing.*;
import java.awt.Color;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// サンプルデータを入力
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// F1（5列目、0行目）を指す CellArea を作成
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// Win/Loss スパークラインを追加（SparklineType.Stacked）
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);
// スパークライングループをカスタマイズ
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// 高値の色を緑に設定
CellsColor highColor = workbook.createCellsColor();
highColor.setColor(Color.GREEN);
group.setHighPointColor(highColor);
// 低値の色を赤に設定
CellsColor lowColor = workbook.createCellsColor();
lowColor.setColor(Color.RED);
group.setLowPointColor(lowColor);
// 負値の色をオレンジに設定
CellsColor negColor = workbook.createCellsColor();
negColor.setColor(Color.ORANGE);
group.setNegativePointsColor(negColor);
// デフォルトの系列色を設定（正の値に使用）
CellsColor seriesColor = workbook.createCellsColor();
seriesColor.setColor(new Color(70, 130, 180)); // スチールブルーの近似色
group.setSeriesColor(seriesColor);
// ワークブックを保存
workbook.save("output_winloss.xlsx");
System.out.println("Workbook saved successfully: output_winloss.xlsx");
```

## **3 種類のスパークラインをまとめて使用する**
次の総合的な例では、単一のワークブックを作成し、1 行目に値 5、-3、8、-2、6 を書き込み、続いてセル F1、F2、F3 に 3 つのスパークライングループ（それぞれ異なる種類）を追加します。これにより、生成されたファイルが 3 種類のスパークラインスタイルを一度に示すようになります。

```java
import com.aspose.cells.*;
// ステップ1: ワークブックを作成し、最初のワークシートを取得する
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// ステップ2: 1行目(A1:E1)にサンプルデータを入力する
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// ステップ3: F1に折れ線スパークライングループを追加する
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5); // 修正: 静的ファクトリメソッドを使用する
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// CellsColorを介して折れ線スパークラインの色をカスタマイズする
CellsColor lineColor = workbook.createCellsColor();
lineColor.setColor(com.aspose.cells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// ステップ4: F2に縦棒スパークライングループを追加する
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // 修正: 静的ファクトリメソッドを使用する
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// 縦棒スパークライン系列の色をカスタマイズする
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// ステップ5: F3にWin/Loss(積み上げ)スパークライングループを追加する
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // 修正: 静的ファクトリメソッドを使用する
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Win/Lossスパークライン系列の色をカスタマイズする
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// ステップ6: ワークブックを保存する
workbook.save("output_all.xlsx");
```

## **スパークラインの外観をカスタマイズする**
`SparklineGroup` が作成されて `worksheet.getSparklineGroups()` に追加された後は、ワークブックを保存する前にそのいくつかの視覚的なプロパティを読み取ったり変更したりできます。最も一般的にカスタマイズされるプロパティは以下のとおりです。
- **`group.getType()`** — `SparklineType`（LINE、COLUMN、または STACKED）。グループは追加時に設定されますが、読み戻して確認することができます。
- **`group.getLine().setColor(...)`** — 線の色。`workbook.createCellsColor()` を通じて作成された `CellsColor` として表現されます。これは折れ線スパークラインの線の色を設定するためのプロパティです。
- **`group.getLine().setWeight(...)`** — 線の太さ（ポイント単位）。値が大きいほど線が太くなります。
- **高値/安値ポイントのマーカー** — 最高および最低のデータ点に小さなマーカーを表示するフラグ。極端な値を強調するのに役立ちます。
- **最初/最後/負のポイントのマーカー** — 最初、最後、および負のデータ点にマーカーを表示するフラグ。
色を変更するには、必ず `CellsColor` インスタンスを作成して該当するプロパティに割り当ててください。スパークラインの色プロパティに `java.awt.Color` を直接代入しないでください。それらは `Aspose.Cells.Drawing` の `CellsColor` 型を期待します。`add` メソッド自体は完全な型付けされた `SparklineGroup` オブジェクトを返すため、戻り値に対してプロパティの代入をチェーンしたり、ローカル変数に保存して保存前にカスタマイズしたりできます。
{{% /alert %}}

{{< app/cells/assistant language="java" >}}