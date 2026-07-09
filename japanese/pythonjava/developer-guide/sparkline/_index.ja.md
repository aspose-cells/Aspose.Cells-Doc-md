---
title: Aspose.Cells for Python via Java におけるスパークライン
linktitle: Sparklines
description: Aspose.Cells はスプレッドシートファイルを扱うための Python via Java ライブラリであり、ワークシートセル内に配置されるミニチュアチャートであるスパークラインの作成をサポートします。この記事では、Aspose.Cells ライブラリを使用して、折れ線、縦棒、勝敗のスパークラインを追加およびカスタマイズする方法について説明します。
keywords: Aspose.Cells, Python via Java ライブラリ, スプレッドシート, スパークライン, 折れ線スパークライン, 縦棒スパークライン, 勝敗スパークライン, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ja/python-java/creating-sparklines/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は、ワークシートセル内のスパークライン作成をサポートしています。スパークラインは単一セルに収まるミニチュアチャートであり、データ傾向を素早く視覚的に表現します。Aspose.Cells は折れ線、縦棒、勝敗のスパークラインをサポートしており、それぞれを色、線の太さ、高値/安値、マーカーに関してカスタマイズできます。

{{% /alert %}}

## **はじめに**

スパークラインはセル内に収まる小さなチャートであり、完全なチャートほどのスペースを取らずにデータの行や列の隣にすばやく傾向を表示したい場合に便利です。Excel は **折れ線**、**縦棒**、**勝敗** の 3 種類のスパークラインをサポートしています。Aspose.Cells は、`Aspose.Cells.Charts` 名前空間にある `SparklineGroup` および `SparklineGroupCollection` API を介してこの機能を提供します。

Aspose.Cells では、追加するすべてのスパークラインが `worksheet.getSparklineGroups().add(...)` を通じて作成され、`SparklineGroup` オブジェクトが返されます。その後、そのオブジェクトを使用して、スパークラインの種類、データ範囲、配置先セル、線の色、線の太さ、マーカー、高値/安値インジケーターなどの視覚的なプロパティを設定できます。

{{% alert color="primary" %}}

単一の `SparklineGroup` は、同じスタイルを共有する 1 つ以上のスパークラインを含めることができます。`add` を呼び出してデータの行と単一の配置先セルを渡すと、そのセル内に 1 つのスパークラインが作成されます。配置先範囲が 1 セルより広い場合は、各配置先セルに個別のスパークラインが描画され、すべて同じスタイルとデータ範囲が使用されます。

{{% /alert %}}

この記事では、Aspose.Cells がサポートする 3 種類のスパークライン — **折れ線**、**縦棒**、**勝敗** — のそれぞれについて、追加方法、色のカスタマイズ方法、結果として得られるワークブックの保存方法を説明します。

## **折れ線スパークライン**

折れ線スパークラインは、データ系列のデータ点を通る連続した線を描画するため、時間の経過に伴う傾向を示すための最も自然な選択肢です。Aspose.Cells では、`add` メソッドに `SparklineType.LINE` を渡すことで折れ線スパークラインが作成されます。

ワークフローは他のスパークライン種別と同じです:

1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. (たとえば 1 行目の A 列から E 列に) 視覚化したい値を持つソースデータの行を入力します。
3. スパークラインが描画される配置先セルを記述する `CellArea` を構築します。
4. `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)` を呼び出します。3 番目の引数である `false` は、データ範囲が水平方向 (行) であり、垂直方向 (列) ではないことを Aspose.Cells に伝えます。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズします。折れ線スパークラインの場合は、`group.getLine().getColor()` (`Aspose.Cells.Drawing` の `CellsColor` を必要とします) を使用して線の色を設定し、線の太さを調整し、高値/安値マーカーを切り替えることができます。
6. ワークブックを保存します。

次の例では、ワークブックを作成し、セル A1 から E1 に値 5、-3、8、-2、6 を書き込み、それらの値をトレースする折れ線スパークラインをセル F1 に追加します。また、線の色を赤にカスタマイズし、高値と安値のマーカーを有効化します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, SparklineType
from java.awt import Color

# ステップ1: Workbookを作成し、最初のワークシートを取得する
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()

# ステップ2: サンプル値 5, -3, 8, -2, 6 をセル A1:E1 に書き込む
cells.get("A1").putValue(5)
cells.get("B1").putValue(-3)
cells.get("C1").putValue(8)
cells.get("D1").putValue(-2)
cells.get("E1").putValue(6)

# ステップ3: 宛先セル F1 を指す CellArea を作成する
dest = CellArea()
dest.setStartColumn(5)  # 列 F (0から始まるインデックス)
dest.setEndColumn(5)
dest.setStartRow(0)     # 行 1 (0から始まるインデックス)
dest.setEndRow(0)

# ステップ4: A1:E1 から F1 に折れ線スパークラインを追加する
# SparklineGroups.add は新しく追加されたグループのインデックスを返します
index = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(index)

# ステップ5: 赤色の CellsColor を作成し、スパークラインの線の色に割り当てる
red = workbook.createCellsColor()
red.setColor(Color.RED)
group.setSeriesColor(red)

# ステップ6: 高値マーカーと低値マーカーを有効にする
group.setShowHighPoint(True)
group.setShowLowPoint(True)

# ステップ7: ワークブックを保存する
workbook.save("output_line.xlsx")

jpype.shutdownJVM()
```

## **縦棒スパークライン**

縦棒スパークラインは、各データ点を垂直な棒としてレンダリングします。そのため、大きさが意味を持つデータ (たとえば月次売上高や個数) に適しています。Aspose.Cells では、`add` メソッドに `SparklineType.COLUMN` を渡すことで縦棒スパークラインを作成します。

手順は折れ線スパークラインの例と同様です:

1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. 視覚化する値で同じソース範囲 (A1:E1) を入力します。
3. 配置先セルを記述する `CellArea` を構築します。
4. `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)` を呼び出します。
5. 必要に応じて、結果として得られる `SparklineGroup` をカスタマイズします (たとえば、`group.getType()` を設定して種類を確認したり、棒の色を調整したりします)。
6. 折れ線スパークラインの例を上書きしないように、ワークブックを別の出力ファイルに保存します。

次の例では、5、-3、8、-2、6 を A1:E1 に書き込み、F1 に縦棒スパークラインをレンダリングします。負の値は下向きの棒として、正の値は上向きの棒として描画されるため、プラスとマイナスの寄与を一目で簡単に識別できます。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType

# Step 1: Workbookを作成し、最初のワークシートを取得する
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Step 2: A1:E1にサンプル値を書き込む
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.getCells().get(0, i).putValue(values[i])

# Step 3: F1を指すCellAreaを構築する（列インデックス5、行インデックス0）
dest = CellArea()
dest.setStartColumn(5)
dest.setEndColumn(5)
dest.setStartRow(0)
dest.setEndRow(0)

# Step 4: 目的セルにColumnスパークラインを追加する
idx = worksheet.getSparklineGroups().add(
    SparklineType.Column, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(idx)

# Step 5: group.Typeを読み取ってスパークラインの種類を確認する
print("Sparkline Type added: " + str(group.getType()))

# Step 6: ワークブックを保存する
workbook.save("output_column.xlsx")

print("Workbook saved as output_column.xlsx")

jpype.shutdownJVM()
```

## **勝敗スパークライン**

勝敗スパークラインは、2 つの結果のみを表示するように設計された縦棒スパークラインの特殊なバリエーションです。正の値は「上」バー (勝ち) として描画され、ゼロまたは負の値は「下」バー (負け) として描画されます。勝敗スパークラインは、一連の勝ち負け、合否結果、または時系列の二値結果を視覚化するためによく使用されます。

Aspose.Cells では、`add` メソッドに `SparklineType.STACKED` を渡すことで勝敗スパークラインが作成されます。(名前にもかかわらず、`SparklineType.STACKED` は勝敗レンダリングを要求するために使用される enum 値です。)

手順は他の 2 つの種類と同じです:

1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. ソース範囲を入力します。勝敗スパークラインはすべての値を勝ちまたは負けとして扱うため、値そのものの大きさは重要ではなく、符号のみが重要です。正の値は上バーになり、非正の値は下バーになります。
3. 配置先セルを記述する `CellArea` を構築します。
4. `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)` を呼び出します。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズします (たとえば、勝ちバーと負けバーのアクセントカラーを設定します)。
6. 3 つの例すべてがディスク上に共存できるよう、ワークブックを別のファイル名で保存します。

次の例では、前の 2 つのセクションと同じ入力データを使用します。値 5、-3、8、-2、6 は勝ち、負け、勝ち、負け、勝ち として解釈され、F1 に描画されるスパークラインはそのパターンを正確に反映します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, CellsColor, Color

# ステップ1: Workbookを作成し、最初のワークシートを取得する
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("WinLoss")

# ステップ2: 1行目にサンプルデータを入力する: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# ステップ3: F1を指すCellAreaを構築する（列5、行0）
dest = CellArea()
dest.setStartColumn(5)   # F列
dest.setEndColumn(5)
dest.setStartRow(0)      # 1行目
dest.setEndRow(0)

# ステップ4: Win/Lossスパークラインを追加する（SparklineType.Stacked）
groupIndex = worksheet.getSparklineGroups().add(
    SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.getSparklineGroups().get(groupIndex)

# ステップ5: スパークライングループをカスタマイズする
# 高値マーカーと安値マーカーを有効にする
group.setShowHighPoint(True)
group.setShowLowPoint(True)
group.setShowNegativePoints(True)

# 高値の色を緑に設定する
highColor = workbook.createCellsColor()
highColor.setColor(Color.GREEN)
group.setHighPointColor(highColor)

# 安値の色を赤に設定する
lowColor = workbook.createCellsColor()
lowColor.setColor(Color.RED)
group.setLowPointColor(lowColor)

# 負のポイントの色をオレンジに設定する
negColor = workbook.createCellsColor()
negColor.setColor(Color.ORANGE)
group.setNegativePointsColor(negColor)

# デフォルトの系列色を設定する（ポジティブなバーに使用）
seriesColor = workbook.createCellsColor()
seriesColor.setColor(Color.STEELBLUE)
group.setSeriesColor(seriesColor)

# ステップ6: ワークブックを保存する
workbook.save("output_winloss.xlsx")

print("Workbook saved successfully: output_winloss.xlsx")

jpype.shutdownJVM()
```

## **3 種類のスパークラインをすべて組み合わせる**

前の 3 つの例はそれぞれ独自のワークブックを生成するため、出力ファイルを個別に確認できます。ただし実際のシナリオでは、複数のデータ系列を並べて比較したい場合がよくあります。これを行う最もクリーンな方法は、複数のスパークライン グループを同じワークシートに配置し、各グループが異なるスタイルをレンダリングするようにすることです。

複数の `SparklineGroup` オブジェクトを同じ `SparklineGroupCollection` に追加でき、各グループは異なる配置先セルまたは異なる範囲を対象とすることができます。たとえば、F1 に折れ線スパークライン、F2 に縦棒スパークライン、F3 に勝敗スパークラインを配置し、すべて 1 行目の同じソースデータを読み取るようにして、3 つの異なる視覚的表現を同じ数値で見ることができます。

次の複合例では、単一のワークブックを作成し、1 行目に値 5、-3、8、-2、6 を入力してから、F1、F2、F3 のセルに 3 つのスパークライン グループ (各種類 1 つずつ) を追加し、結果として得られるファイルが 3 つのスパークライン スタイルすべてを一度に示すようにします。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, CellsColor, SparklineType
from java.awt import Color

# ステップ1: Workbookを作成し、最初のワークシートを取得します
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# ステップ2: 1行目 (A1:E1) にサンプルデータを入力します
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# ステップ3: F1に折れ線スパークライングループを追加します
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", False, lineArea)
lineGroup = worksheet.getSparklineGroups().get(lineIdx)

# CellsColorを使用して折れ線スパークラインの色をカスタマイズします
lineColor = workbook.createCellsColor()
lineColor.setColor(Color.BLUE)
lineGroup.setSeriesColor(lineColor)

# ステップ4: F2に縦棒スパークライングループを追加します
columnArea = CellArea()
columnArea.setStartColumn(5)
columnArea.setEndColumn(5)
columnArea.setStartRow(1)
columnArea.setEndRow(1)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", False, columnArea)
columnGroup = worksheet.getSparklineGroups().get(columnIdx)

# 縦棒スパークラインのシリーズ色をカスタマイズします
columnColor = workbook.createCellsColor()
columnColor.setColor(Color.GREEN)
columnGroup.setSeriesColor(columnColor)

# ステップ5: F3にWin/Loss（積み上げ）スパークライングループを追加します
stackedArea = CellArea()
stackedArea.setStartColumn(5)
stackedArea.setEndColumn(5)
stackedArea.setStartRow(2)
stackedArea.setEndRow(2)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", False, stackedArea)
stackedGroup = worksheet.getSparklineGroups().get(stackedIdx)

# Win/Lossスパークラインのシリーズ色をカスタマイズします
stackedColor = workbook.createCellsColor()
stackedColor.setColor(Color(255, 140, 0))  # ダークオレンジ
stackedGroup.setSeriesColor(stackedColor)

# ステップ6: ワークブックを保存します
workbook.save("output_all.xlsx")

jpype.shutdownJVM()
```

{{% alert color="primary" %}}

単一のワークシート内で複数のスパークライン グループを組み合わせる場合、各グループは独立しています。同じソース範囲を共有することも、異なるソース範囲を使用することもでき、個別にスタイルを設定できます。これにより、既存のワークシート内に直接、セルの視覚化の小さな「ダッシュボード」を簡単に構築できます。

{{% /alert %}}

## **スパークラインの外観のカスタマイズ**

`SparklineGroup` が作成されて `worksheet.getSparklineGroups()` に追加された後、ワークブックを保存する前にその視覚的プロパティのいくつかを読み取ったり変更したりできます。最も一般的にカスタマイズされるプロパティは次のとおりです:

- **`group.getType()`** — `SparklineType` (LINE、COLUMN、または STACKED)。これはグループが追加されるときに設定されますが、読み戻して確認できます。
- **`group.getLine().getColor()`** — 線の色で、`workbook.createCellsColor()` を通じて作成された `CellsColor` として表されます。これは折れ線スパークラインの線の色に使用するプロパティです。
- **`group.getLine().getWeight()`** — ポイント単位の線の太さ。値が大きいほど、太い線が生成されます。
- **高値/安値マーカー** — 最高および最低データ点に小さなマーカーをオンにするフラグで、極端な値を強調するのに役立ちます。
- **最初/最後/負のポイントマーカー** — 最初、最後、および負のデータ点にマーカーを切り替えるフラグ。

色を変更するには、常に `CellsColor` インスタンスを作成し、関連プロパティに割り当ててください。`java.awt.Color` をスパークラインの色プロパティに直接割り当てないでください。それらは `Aspose.Cells.Drawing` の `CellsColor` 型を必要とします。`add` メソッド自体は完全に型付けされた `SparklineGroup` オブジェクトを返すため、戻り値のプロパティ代入を連鎖させることも、ローカル変数に格納して保存前にカスタマイズすることもできます。

{{< app/cells/assistant language="python" >}}