---
title: Aspose.Cells for Java のスパークライン
linktitle: Sparklines
description: Aspose.Cells はスプレッドシートファイルを操作するための Java ライブラリで、ワークシートセル内に配置されるミニチュアグラフであるスパークラインの作成をサポートしています。この記事では、Aspose.Cells ライブラリを使用して折れ線、列、勝敗のスパークラインを追加およびカスタマイズする方法を説明します。
keywords: Aspose.Cells, Java ライブラリ, スプレッドシート, スパークライン, 折れ線スパークライン, 列スパークライン, 勝敗スパークライン, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ja/java/creating-sparklines/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells はワークシートセル内にスパークラインを作成することをサポートしています。スパークラインは単一セル内に収まるミニチュアグラフで、データ傾向の迅速な視覚表現を提供します。Aspose.Cells は折れ線、列、勝敗のスパークラインをサポートしており、それぞれを色、線の太さ、高低点、マーカーに関してカスタマイズできます。

{{% /alert %}}

## **はじめに**

スパークラインはセル内に収まる小さなグラフで、完全なグラフのスペースを取らずに、行や列のデータの隣にすばやく傾向を表示したい場合に便利です。Excel は 3 種類のスパークラインをサポートしています：**折れ線**、**列**、**勝敗**。Aspose.Cells は、`Aspose.Cells.Charts` 名前空間にある `SparklineGroup` および `SparklineGroupCollection` API を通じてこの機能を提供します。

Aspose.Cells では、追加するすべてのスパークラインが `worksheet.getSparklineGroups().add(...)` を介して作成され、`SparklineGroup` オブジェクトが返されます。その後、そのオブジェクトを使用してスパークラインの種類、データ範囲、配置先セル、および線の色、線の太さ、マーカー、高低点インジケーターなどの視覚的なプロパティを設定できます。

{{% alert color="primary" %}}

単一の `SparklineGroup` には、同じスタイルを共有する 1 つ以上のスパークラインを含めることができます。`add` を呼び出してデータの行と単一の配置先セルを渡すと、そのセル内に 1 つのスパークラインが作成されます。配置先の範囲が 1 セルより広い場合、各配置先セルに個別のスパークラインが描画され、すべて同じスタイルとデータ範囲を使用します。

{{% /alert %}}

この記事を通じて、Aspose.Cells がサポートする 3 つのスパークラインの種類 — **折れ線**、**列**、**勝敗** — のそれぞれを順に見ていき、追加方法、色のカスタマイズ方法、結果として得られるワークブックの保存方法を説明します。

## **折れ線スパークライン**

折れ線スパークラインは、系列内のデータポイントを通る連続した線を描画するため、時間の経過に伴う傾向を示すのに最も自然な選択肢です。Aspose.Cells では、`add` メソッドに `SparklineType.LINE` を渡すことで折れ線スパークラインが作成されます。

ワークフローは他のスパークラインの種類と同じです：

1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. ソースデータの行（たとえば 1 行目、A 列から E 列）に視覚化する値を入力します。
3. スパークラインが描画される配置先セルを記述する `CellArea` を作成します。
4. `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)` を呼び出します。3 番目の引数 — `false` — は、データ範囲が垂直方向（列）ではなく水平方向（行）であることを Aspose.Cells に伝えます。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズします。折れ線スパークラインの場合、`group.getLine().setColor(...)`（これは `Aspose.Cells.Drawing` の `CellsColor` を必要とします）を使用して線の色を設定したり、線の太さを調整したり、高低点マーカーを切り替えたりできます。
6. ワークブックを保存します。

次の例では、ワークブックを作成し、セル A1 から E1 に値 5、-3、8、-2、6 を書き込み、これらの値をトレースする折れ線スパークラインをセル F1 に追加します。また、線の色を赤にカスタマイズし、高点と低点のマーカーを有効化します。

```java
public class CodeRunner {
    public static void main(String[] args) {
        try {
            // ステップ1: Workbookを作成し、最初のワークシートを取得する
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.getWorksheets().get(0);
            Cells cells = worksheet.getCells();

            // ステップ2: サンプル値 5、-3、8、-2、6 をセル A1:E1 に書き込む
            cells.get("A1").putValue(5);
            cells.get("B1").putValue(-3);
            cells.get("C1").putValue(8);
            cells.get("D1").putValue(-2);
            cells.get("E1").putValue(6);

            // ステップ3: 出力先セル F1 を指す CellArea を作成する
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // 列 F (0から始まるインデックス)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // 行 1 (0から始まるインデックス)
            dest.EndRow = 0;

            // ステップ4: A1:E1 から F1 に折れ線スパークラインを追加する
            // SparklineGroups.add は新しく追加されたグループのインデックスを返す
            int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
            SparklineGroup group = worksheet.getSparklineGroups().get(index);

            // ステップ5: 赤色の CellsColor を作成し、スパークラインの線の色に割り当てる
            CellsColor red = workbook.createCellsColor();
            red.setColor(com.aspose.cells.Color.getRed());
            group.setSeriesColor(red);

            // ステップ6: 高値マーカーと低値マーカーを有効にする
            group.setShowHighPoint(true);
            group.setShowLowPoint(true);

            // ステップ7: ワークブックを保存する
            workbook.save("output_line.xlsx");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

## **列スパークライン**

列スパークラインは、各データポイントを垂直バーとしてレンダリングします。これは、大きさが意味を持つデータ — たとえば、月次売上高やカウント — に適しています。Aspose.Cells では、`add` メソッドに `SparklineType.COLUMN` を渡すことで列スパークラインが作成されます。

手順は折れ線スパークラインの例と同じです：

1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. 同じソース範囲（A1:E1）に視覚化する値を入力します。
3. 配置先セルを記述する `CellArea` を作成します。
4. `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)` を呼び出します。
5. 必要に応じて、結果として得られる `SparklineGroup` をカスタマイズします — たとえば、`group.getType()` を設定して種類を確認したり、バーの色を調整したりします。
6. ワークブックを別の出力ファイルに保存して、折れ線スパークラインの例を上書きしないようにします。

以下の例では、5、-3、8、-2、6 の値を A1:E1 に書き込み、列スパークラインを F1 にレンダリングします。負の値は下向きのバーとして、正の値は上向きのバーとして描画されるため、一目で正と負の寄与を簡単に識別できます。

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// A1:E1にサンプル値を書き込む
int[] values = new int[] { 5, -3, 8, -2, 6 };
for (int i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// F1を指すCellAreaを構築する(列インデックス5、行インデックス0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// Columnスパークラインを宛先セルに追加する
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);

// group.Typeを読み取ってスパークラインの種類を確認する
System.out.println("Sparkline Type added: " + group.getType());

// ワークブックを保存する
workbook.save("output_column.xlsx");

System.out.println("Workbook saved as output_column.xlsx");
```

## **勝敗スパークライン**

勝敗スパークラインは、列スパークラインの特別なバリエーションで、2 つの結果のみを表示するように設計されています。正の値は「上」バー（勝ち）として描画され、ゼロまたは負の値は「下」バー（負け）として描画されます。勝敗スパークラインは、勝ちと負けのシーケンス、合否結果、または時間に伴う任意の二項結果を視覚化するためによく使用されます。

Aspose.Cells では、`add` メソッドに `SparklineType.STACKED` を渡すことで勝敗スパークラインが作成されます。（名前にもかかわらず、`SparklineType.STACKED` は勝敗レンダリングを要求するために使用される列挙値です。）

手順は他の 2 種類と同じです：

1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. ソース範囲に入力します。勝敗スパークラインではすべての値が勝ちまたは負けとして扱われるため、値の大きさは重要ではなく、符号のみが重要です。正の値は上バーになり、非正の値は下バーになります。
3. 配置先セルを記述する `CellArea` を作成します。
4. `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)` を呼び出します。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズします。たとえば、勝ちバーと負けバーのアクセント色を設定します。
6. ワークブックを別のファイル名で保存して、3 つのすべての例がディスク上に共存できるようにします。

以下の例では、前の 2 つのセクションと同じ入力データを使用しています。値 5、-3、8、-2、6 は勝ち、負け、勝ち、負け、勝ちとして解釈され、F1 に描画されるスパークラインはまさにそのパターンを反映しています。

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

// F1を指すCellAreaを構築（列5、行0）
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// Win/Lossスパークラインを追加（SparklineType.Stacked）
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);

// スパークライングループをカスタマイズ
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// 最高値の色を緑に設定
CellsColor highColor = workbook.createCellsColor();
highColor.setColor(Color.GREEN);
group.setHighPointColor(highColor);

// 最低値の色を赤に設定
CellsColor lowColor = workbook.createCellsColor();
lowColor.setColor(Color.RED);
group.setLowPointColor(lowColor);

// 負の値の色をオレンジに設定
CellsColor negColor = workbook.createCellsColor();
negColor.setColor(Color.ORANGE);
group.setNegativePointsColor(negColor);

// デフォルトの系列色を設定（正の値のバーに使用）
CellsColor seriesColor = workbook.createCellsColor();
seriesColor.setColor(new Color(70, 130, 180)); // SteelBlueの近似値
group.setSeriesColor(seriesColor);

// ワークブックを保存
workbook.save("output_winloss.xlsx");

System.out.println("Workbook saved successfully: output_winloss.xlsx");
```

## **3 つのスパークライン種類の組み合わせ**

前の 3 つの例はそれぞれ独自のワークブックを生成するため、出力ファイルを個別に簡単に確認できます。ただし、実際のシナリオでは、複数のデータ系列を並べて比較したいことがよくあります。これを行う最もクリーンな方法は、複数のスパークライン グループを同じワークシートに配置し、各グループが異なるスタイルをレンダリングすることです。

複数の `SparklineGroup` オブジェクトを同じ `SparklineGroupCollection` に追加でき、各グループは異なる配置先セルまたは異なる範囲を対象とすることができます。たとえば、1 行目の同じソースデータを読み取る折れ線スパークラインを F1 に、列スパークラインを F2 に、勝敗スパークラインを F3 に配置して、同じ数値の 3 つの異なる視覚的処理を閲覧者が見ることができるようにすることができます。

以下の組み合わせ例では、単一のワークブックを作成し、1 行目に値 5、-3、8、-2、6 を入力し、セル F1、F2、F3 に 3 つのスパークライン グループを追加します — 各種類の 1 つずつ — その結果、3 つのスパークライン スタイルすべてが同時に表示されるファイルになります。

```java
import com.aspose.cells.*;

// ステップ1：Workbookを作成し、最初のワークシートを取得する
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// ステップ2：行1（A1:E1）にサンプルデータを入力する
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// ステップ3：F1に折れ線スパークライングループを追加する
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5); // 修正：静的ファクトリメソッドを使用する
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// CellsColorを介して折れ線スパークラインの色をカスタマイズする
CellsColor lineColor = workbook.createCellsColor();
lineColor.setColor(com.aspose.cells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);

// ステップ4：F2に縦棒スパークライングループを追加する
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // 修正：静的ファクトリメソッドを使用する
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// 縦棒スパークラインシリーズの色をカスタマイズする
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);

// ステップ5：F3にWin/Loss（積み上げ）スパークライングループを追加する
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // 修正：静的ファクトリメソッドを使用する
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Win/Lossスパークラインシリーズの色をカスタマイズする
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);

// ステップ6：ワークブックを保存する
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

単一のワークシート内で複数のスパークライン グループを組み合わせる場合、各グループは独立しています。同じソース範囲を共有することも、異なるソース範囲を使用することもでき、個別にスタイル設定できます。これにより、既存のワークシート内に直接、セルの視覚化の小さな「ダッシュボード」を簡単に構築できます。

{{% /alert %}}

## **スパークラインの外観のカスタマイズ**

`SparklineGroup` が作成されて `worksheet.getSparklineGroups()` に追加された後、ワークブックを保存する前にその視覚的なプロパティのいくつかを読み取ったり変更したりできます。最も一般的にカスタマイズされるプロパティは次のとおりです：

- **`group.getType()`** — `SparklineType`（LINE、COLUMN、または STACKED）。これはグループの追加時に設定されますが、読み戻して確認することができます。
- **`group.getLine().setColor(...)`** — 線の色。`workbook.createCellsColor()` を介して作成された `CellsColor` として表現されます。これは折れ線スパークラインの線の色に使用するプロパティです。
- **`group.getLine().setWeight(...)`** — ポイント単位の線の太さ。値が大きいほど太い線が生成されます。
- **高点/低点マーカー** — 最高データポイントと最低データポイントに小さなマーカーをオンにするフラグで、極値を強調するのに役立ちます。
- **始点/終点/負のポイントマーカー** — 最初、最後、負のデータポイントにマーカーを切り替えるフラグ。

色を変更するには、常に `CellsColor` インスタンスを作成し、関連するプロパティに割り当てます。`java.awt.Color` をスパークラインの色プロパティに直接割り当てないでください — これらは `Aspose.Cells.Drawing` の `CellsColor` 型を必要とします。`add` メソッド自体は完全に型指定された `SparklineGroup` オブジェクトを返すため、戻り値のプロパティ割り当てをチェーンしたり、ローカル変数に格納して保存前にカスタマイズしたりできます。



{{< app/cells/assistant language="java" >}}