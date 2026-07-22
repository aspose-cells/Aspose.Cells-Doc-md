---
title: Aspose.Cells for Python via .NET のスパークライン
linktitle: スパークライン
description: Aspose.Cells は、ワークシートセル内に配置されるミニチュアグラフであるスパークラインの作成をサポートする、スプレッドシートファイルを扱うための Python ライブラリです。この記事では、Aspose.Cells ライブラリを使用して、折れ線、縦棒、勝敗のスパークラインを追加およびカスタマイズする方法について説明します。
keywords: Aspose.Cells, Python ライブラリ, スプレッドシート, スパークライン, 折れ線スパークライン, 縦棒スパークライン, 勝敗スパークライン, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ja/python-net/creating-sparklines/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells は、ワークシートセル内のスパークラインの作成をサポートしています。スパークラインは単一のセルに収まるミニチュアグラフであり、データトレンドを素早く視覚的に表現します。Aspose.Cells は折れ線、縦棒、勝敗のスパークラインをサポートしており、それぞれを色、線の太さ、高値/安値のポイント、マーカーに関してカスタマイズできます。

{{% /alert %}}

## **はじめに**

スパークラインはセル内の小さなグラフで、データの行や列の隣に完全なグラフのスペースを取らずに素早くトレンドを表示したい場合に便利です。Excel は **折れ線 (line)**、**縦棒 (column)**、**勝敗 (win/loss)** の 3 種類のスパークラインをサポートしています。Aspose.Cells は `aspose.cells.charts` 名前空間にある `SparklineGroup` および `SparklineGroupCollection` API を通じてこの機能を提供します。

Aspose.Cells では、追加するすべてのスパークラインは `worksheet.sparkline_groups.add(...)` を通じて作成され、`SparklineGroup` オブジェクトが返されます。そのオブジェクトを使用して、スパークラインの種類、データ範囲、配置先セル、および線の色、線の太さ、マーカー、高値/安値ポイントインジケーターなどの表示プロパティを設定できます。

{{% alert color="primary" %}}

単一の `SparklineGroup` には、同じスタイルを共有する 1 つ以上のスパークラインを含めることができます。`add` を呼び出してデータの行と単一の配置先セルを渡すと、そのセル内に 1 つのスパークラインが作成されます。配置先の範囲が 1 セルより広い場合、各配置先セルに個別のスパークラインが描画され、すべて同じスタイルとデータ範囲が使用されます。

{{% /alert %}}

この記事を通じて、Aspose.Cells がサポートする 3 種類のスパークライン — **折れ線 (Line)**、**縦棒 (Column)**、**勝敗 (Win/Loss)** — それぞれを順に見ていき、追加方法、色のカスタマイズ、結果として得られるワークブックの保存方法を説明します。

## **折れ線スパークライン**

折れ線スパークラインは、系列のデータポイントを結ぶ連続した線を描画するため、時間の経過に伴うトレンドを示すのに最も自然な選択肢です。Aspose.Cells では、`SparklineType.Line` を `sparkline_groups.add` メソッドに渡すことで折れ線スパークラインを作成します。

ワークフローは他のスパークライン種類と同じです:

1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. ソースデータの行 (たとえば 1 行目、A 列から E 列) に、視覚化したい値を書き込みます。
3. スパークラインが描画される配置先セルを記述する `CellArea` を構築します。
4. `worksheet.sparkline_groups.add(SparklineType.Line, "A1:E1", False, dest)` を呼び出します。3 番目の引数である `False` は、データ範囲が水平 (行) であり、垂直 (列) ではないことを Aspose.Cells に伝えます。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズします。折れ線スパークラインの場合、`group.line.color` (`aspose.cells.drawing` の `CellsColor` を必要とします) を使用して線の色を設定したり、線の太さを調整したり、高値/安値ポイントのマーカーを切り替えたりできます。
6. ワークブックを保存します。

次の例では、ワークブックを作成し、セル A1 から E1 に値 5、-3、8、-2、6 を書き込み、これらの値をトレースする折れ線スパークラインをセル F1 に追加します。また、線の色を赤にカスタマイズし、高値と安値のポイントのマーカーを有効化します。

```python
import aspose.cells as ac
import System.Drawing

# ステップ1: Workbookを作成し、最初のワークシートを取得する
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells

# ステップ2: サンプル値 5、-3、8、-2、6 をセル A1:E1 に書き込む
cells["A1"].put_value(5)
cells["B1"].put_value(-3)
cells["C1"].put_value(8)
cells["D1"].put_value(-2)
cells["E1"].put_value(6)

# ステップ3: 出力先のセル F1 を指す CellArea を作成する
dest = ac.CellArea()
dest.start_column = 5   # 列 F（0から始まるインデックス）
dest.end_column = 5
dest.start_row = 0      # 行 1（0から始まるインデックス）
dest.end_row = 0

# ステップ4: A1:E1 から F1 への折れ線スパークラインを追加する
# SparklineGroups.Add は新しく追加されたグループのインデックスを返す
index = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, dest)
group = worksheet.sparkline_groups[index]

# ステップ5: 赤色の CellsColor を作成し、スパークラインの線の色に割り当てる
red = workbook.create_cells_color()
red.color = System.Drawing.Color.Red
group.series_color = red

# ステップ6: 高値マーカーと安値マーカーを有効にする
group.show_high_point = True
group.show_low_point = True

# ステップ7: ワークブックを保存する
workbook.save("output_line.xlsx")
```

## **縦棒スパークライン**

縦棒スパークラインは、各データポイントを垂直バーとしてレンダリングします。これにより、値が重要な意味を持つデータ (たとえば、月次売上高や個数) によく適しています。Aspose.Cells では、`SparklineType.Column` を `sparkline_groups.add` メソッドに渡すことで縦棒スパークラインを作成します。

手順は折れ線スパークラインの例と同じです:

1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. 同じソース範囲 (A1:E1) に視覚化したい値を書き込みます。
3. 配置先セルを記述する `CellArea` を構築します。
4. `worksheet.sparkline_groups.add(SparklineType.Column, "A1:E1", False, dest)` を呼び出します。
5. 必要に応じて、結果として得られる `SparklineGroup` をカスタマイズします (たとえば、`group.type` を設定して種類を確認したり、バーの色を微調整したりします)。
6. ワークブックを別の出力ファイルに保存し、折れ線スパークラインの例を上書きしないようにします。

以下の例では、A1:E1 に値 5、-3、8、-2、6 を書き込み、F1 に縦棒スパークラインをレンダリングします。負の値は下向きのバーとして、正の値は上向きのバーとして描画されるため、正の寄与と負の寄与を一目で簡単に識別できます。

```python
import aspose.cells as ac

# ステップ1: ワークブックを作成し、最初のワークシートを取得する
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# ステップ2: サンプル値をA1:E1に書き込む
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.cells[0, i].put_value(values[i])

# ステップ3: F1を指すCellAreaを構築する (列インデックス5、行インデックス0)
dest = ac.CellArea()
dest.start_column = 5
dest.end_column = 5
dest.start_row = 0
dest.end_row = 0

# ステップ4: コピー先のセルにColumnスパークラインを追加する
idx = worksheet.sparkline_groups.add(
    ac.SparklineType.COLUMN, "A1:E1", False, dest)
group = worksheet.sparkline_groups[idx]

# ステップ5: group.Typeを読み取ってスパークラインのタイプを確認する
print("Sparkline Type added: " + str(group.type))

# ステップ6: ワークブックを保存する
workbook.save("output_column.xlsx")

print("Workbook saved as output_column.xlsx")
```

## **勝敗スパークライン**

勝敗スパークラインは、縦棒スパークラインの特殊な変種で、2 つの結果のみを表示するように設計されています: 正の値は「上」バー (勝ち) として描画され、ゼロまたは負の値は「下」バー (負け) として描画されます。勝敗スパークラインは、勝ち負けのシーケンス、合否結果、または時間にわたる任意の二項結果を視覚化するためによく使用されます。

Aspose.Cells では、`SparklineType.Stacked` を `sparkline_groups.add` メソッドに渡すことで勝敗スパークラインを作成します。(名前にもかかわらず、`SparklineType.Stacked` は勝敗レンダリングを要求するために使用される enum 値です。)

手順は他の 2 種類と同じです:

1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. ソース範囲にデータを書き込みます。勝敗スパークラインではすべての値を勝ちまたは負けのいずれかとして扱うため、値の大きさは関係なく、符号のみが関係します。正の値は上バーになり、非正の値は下バーになります。
3. 配置先セルを記述する `CellArea` を構築します。
4. `worksheet.sparkline_groups.add(SparklineType.Stacked, "A1:E1", False, dest)` を呼び出します。
5. 必要に応じて、返された `SparklineGroup` をカスタマイズします (たとえば、勝ちバーと負けバーのアクセント色を設定します)。
6. 3 つのすべての例がディスク上で共存できるように、ワークブックを別のファイル名で保存します。

以下の例では、前の 2 つのセクションと同じ入力データを使用しています。値 5、-3、8、-2、6 は勝ち、負け、勝ち、負け、勝ち として解釈され、F1 に描画されるスパークラインはそのパターンを正確に反映します。

```python
import aspose.cells as ac
import System.Drawing

# ステップ1: ワークブックを作成し、最初のワークシートを取得する
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "WinLoss"

# ステップ2: 1行目にサンプルデータを入力する: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# ステップ3: F1を指すCellAreaを構築する (列5、行0)
dest = ac.CellArea()
dest.start_column = 5   # F
dest.end_column = 5
dest.start_row = 0      # 行1
dest.end_row = 0

# ステップ4: Win/Lossスパークラインを追加する (SparklineType.Stacked)
group_index = worksheet.sparkline_groups.add(
    ac.SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.sparkline_groups[group_index]

# ステップ5: スパークライングループをカスタマイズする
# 高値マーカーと安値マーカーを有効にする
group.show_high_point = True
group.show_low_point = True
group.show_negative_points = True

# 高値の色を緑に設定する
high_color = workbook.create_cells_color()
high_color.color = System.Drawing.Color.Green
group.high_point_color = high_color

# 安値の色を赤に設定する
low_color = workbook.create_cells_color()
low_color.color = System.Drawing.Color.Red
group.low_point_color = low_color

# 負のポイントの色をオレンジに設定する
neg_color = workbook.create_cells_color()
neg_color.color = System.Drawing.Color.Orange
group.negative_points_color = neg_color

# デフォルトの系列色を設定する (正のバーに使用)
series_color = workbook.create_cells_color()
series_color.color = System.Drawing.Color.SteelBlue
group.series_color = series_color

# ステップ6: ワークブックを保存する
workbook.save("output_winloss.xlsx")

print("Workbook saved successfully: output_winloss.xlsx")
```

## **3 種類のスパークラインタイプの組み合わせ**

前述の 3 つの例はそれぞれ独自のワークブックを生成するため、出力ファイルを個別に簡単に確認できます。ただし、実際のシナリオでは、複数のデータ系列を並べて比較することがよくあります。これを行う最もクリーンな方法は、異なるスタイルをレンダリングする複数のスパークライングループを同じワークシートに配置することです。

複数の `SparklineGroup` オブジェクトを同じ `SparklineGroupCollection` に追加でき、各グループは異なる配置先セルまたは異なる範囲を対象とすることができます。たとえば、1 行目の同じソースデータを読み取る折れ線スパークラインを F1 に、縦棒スパークラインを F2 に、勝敗スパークラインを F3 に配置することで、同じ数値の 3 つの異なる視覚的処理を 読者が見ることができます。

以下の組み合わせ例では、単一のワークブックを作成し、1 行目に値 5、-3、8、-2、6 を書き込み、セル F1、F2、F3 に 3 つのスパークライングループ (各タイプ 1 つずつ) を追加して、結果として得られるファイルが 3 つのスパークラインスタイルすべてを一度に示します。

```python
import aspose.cells as ac
import System.Drawing

# ステップ 1: Workbook を作成し、最初のワークシートを取得します
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# ステップ 2: 1 行目 (A1:E1) にサンプル データを入力します
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# ステップ 3: F1 に折れ線スパークライン グループを追加します
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)
line_group = worksheet.sparkline_groups[line_idx]

# CellsColor を使用して折れ線スパークラインの色をカスタマイズします
line_color = workbook.create_cells_color()
line_color.color = System.Drawing.Color.Blue
line_group.series_color = line_color

# ステップ 4: F2 に縦棒スパークライン グループを追加します
column_area = ac.CellArea()
column_area.start_column = 5
column_area.end_column = 5
column_area.start_row = 1
column_area.end_row = 1
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)
column_group = worksheet.sparkline_groups[column_idx]

# 縦棒スパークライン シリーズの色をカスタマイズします
column_color = workbook.create_cells_color()
column_color.color = System.Drawing.Color.Green
column_group.series_color = column_color

# ステップ 5: F3 に Win/Loss (積み上げ) スパークライン グループを追加します
stacked_area = ac.CellArea()
stacked_area.start_column = 5
stacked_area.end_column = 5
stacked_area.start_row = 2
stacked_area.end_row = 2
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)
stacked_group = worksheet.sparkline_groups[stacked_idx]

# Win/Loss スパークライン シリーズの色をカスタマイズします
stacked_color = workbook.create_cells_color()
stacked_color.color = System.Drawing.Color.DarkOrange
stacked_group.series_color = stacked_color

# ステップ 6: ワークブックを保存します
workbook.save("output_all.xlsx")
```

{{% alert color="primary" %}}

単一のワークシートに複数のスパークライングループを組み合わせる場合、各グループは独立しています。同じソース範囲を共有することも、異なるソース範囲を使用することもでき、独立してスタイルを設定できます。これにより、既存のワークシート内に直接、セル内ビジュアリゼーションの小さな「ダッシュボード」を簡単に構築できます。

{{% /alert %}}

## **スパークラインの外観のカスタマイズ**

`SparklineGroup` が作成されて `worksheet.sparkline_groups` に追加された後、ワークブックを保存する前にその表示プロパティのいくつかを読み取ったり変更したりできます。最も一般的にカスタマイズされるプロパティは次のとおりです:

- **`group.type`** — `SparklineType` (Line、Column、または Stacked)。グループは追加されるときに設定されますが、読み戻して確認することができます。
- **`group.line.color`** — 線の色。`workbook.create_cells_color()` を通じて作成された `CellsColor` として表現されます。これは折れ線スパークラインのストローク色に使用するプロパティです。
- **`group.line.weight`** — ポイント単位の線の太さ。値が大きいほど線が太くなります。
- **高値/安値ポイントマーカー** — 最高および最低のデータポイントに小さなマーカーをオンにするフラグ。極値を強調するのに役立ちます。
- **最初/最後/負のポイントマーカー** — 最初、最後、および負のデータポイントのマーカーを切り替えるフラグ。

色を変更するには、常に `CellsColor` インスタンスを作成し、関連するプロパティに割り当ててください。スパークラインの色プロパティは `aspose.cells.drawing` の `CellsColor` 型を必要とします。生の色値を直接割り当てないでください。`sparkline_groups.add` メソッド自体は完全に型付けされた `SparklineGroup` オブジェクトを返すため、戻り値のプロパティ割り当てを連鎖させたり、ローカル変数に格納して保存前にカスタマイズしたりすることができます。

{{< app/cells/assistant language="python" >}}