---
title: Aspose.Cells for Python via .NET のスパークライン
linktitle: Aspose.Cells for Python via .NET のスパークライン
description: Aspose.Cells は、スプレッドシートファイルを扱うための Python ライブラリで、ワークシートセル内に配置されるミニチュアグラフであるスパークラインの作成をサポートしています。本記事では、Aspose.Cells ライブラリを使用して、折れ線、縦棒、勝敗のスパークラインを追加およびカスタマイズする方法を説明します。
keywords: Aspose.Cells, Python ライブラリ, スプレッドシート, スパークライン, 折れ線スパークライン, 縦棒スパークライン, 勝敗スパークライン, SparklineGroup, SparklineType
type: docs
weight: 195
url: /ja/python-net/creating-sparklines/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ワークシートセル内のスパークライン作成をサポートしています。スパークラインは単一セルに収まるミニチュアグラフであり、データ傾向を素早く視覚的に表現します。Aspose.Cells は折れ線、縦棒、勝敗のスパークラインをサポートしており、それぞれ色、線の太さ、高値/安値のポイント、マーカーについてカスタマイズできます。

## **はじめに**
スパークラインはセル内に収まる小さなグラフで、データの行や列の隣に完全なグラフのスペースを取らずに素早く傾向を表示したい場合に便利です。Excel は **折れ線**、**縦棒**、**勝敗** の 3 種類のスパークラインをサポートしています。Aspose.Cells も、`aspose.cells.charts` 名前空間にある `SparklineGroup` および `SparklineGroupCollection` API を通じてこの機能を提供します。
Aspose.Cells では、追加するすべてのスパークラインが `worksheet.sparkline_groups.add(...)` を通じて作成され、`SparklineGroup` オブジェクトが返されます。そのオブジェクトを使用して、スパークラインの種類、データ範囲、配置先セル、および線の色、線の太さ、マーカー、高値/安値のインジケーターなどの視覚的プロパティを設定できます。
本記事では、Aspose.Cells でサポートされている 3 種類のスパークライン (**折れ線**、**縦棒**、**勝敗**) それぞれを順に解説し、追加方法、色のカスタマイズ方法、結果として得られるワークブックの保存方法を紹介します。

## **折れ線スパークライン**
折れ線スパークラインは、系列のデータポイントを結ぶ連続した線を描画するため、時系列の傾向を示すのに最も自然な選択肢です。Aspose.Cells では、`sparkline_groups.add` メソッドに `SparklineType.Line` を渡すことで折れ線スパークラインを作成します。
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. 視覚化したい値を含むソースデータの行 (たとえば 1 行目の A 列から E 列) を入力します。
3. スパークラインが描画される配置先セルを記述する `CellArea` を作成します。
4. `worksheet.sparkline_groups.add(SparklineType.Line, "A1:E1", False, dest)` を呼び出します。3 番目の引数 `False` は、データ範囲が横方向 (行) であり、縦方向 (列) ではないことを Aspose.Cells に伝えます。
5. 必要に応じて返された `SparklineGroup` をカスタマイズします。折れ線スパークラインの場合は、`group.line.color` を使用して線の色を設定し (`aspose.cells.drawing` の `CellsColor` を指定します)、線の太さを調整し、高値/安値のポイントマーカーを切り替えることができます。
6. ワークブックを保存します。
次の例では、ワークブックを作成し、セル A1 から E1 に値 5、-3、8、-2、6 を書き込み、これらの値をトレースする折れ線スパークラインをセル F1 に追加します。また、線の色を赤にカスタマイズし、高値と安値のポイントに対するマーカーを有効化します。

```python
import aspose.cells as ac
import System.Drawing
# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "WinLoss"
# Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)
# Step 3: Build a CellArea pointing to F1 (column 5, row 0)
dest = ac.CellArea()
dest.start_column = 5   # F
dest.end_column = 5
dest.start_row = 0      # row 1
dest.end_row = 0
# Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
group_index = worksheet.sparkline_groups.add(
    ac.SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.sparkline_groups[group_index]
# Step 5: Customize the sparkline group
# Enable high-point and low-point markers
group.show_high_point = True
group.show_low_point = True
group.show_negative_points = True
# Set the high-point color to green
high_color = workbook.create_cells_color()
high_color.color = System.Drawing.Color.Green
group.high_point_color = high_color
# Set the low-point color to red
low_color = workbook.create_cells_color()
low_color.color = System.Drawing.Color.Red
group.low_point_color = low_color
# Set the negative-point color to orange
neg_color = workbook.create_cells_color()
neg_color.color = System.Drawing.Color.Orange
group.negative_points_color = neg_color
# Set the default series color (used for positive bars)
series_color = workbook.create_cells_color()
series_color.color = System.Drawing.Color.SteelBlue
group.series_color = series_color
# Step 6: Save the workbook
workbook.save("output_winloss.xlsx")
print("Workbook saved successfully: output_winloss.xlsx")
```

## **縦棒スパークライン**
縦棒スパークラインは、各データポイントを縦棒としてレンダリングします。このため、大きさが意味を持つデータ (たとえば月次の売上高やカウント) に適しています。Aspose.Cells では、`sparkline_groups.add` メソッドに `SparklineType.Column` を渡すことで縦棒スパークラインを作成します。
手順は折れ線スパークラインの例と同様です。
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. スパークラインが描画される配置先セルを記述する `CellArea` を作成します。
3. `worksheet.sparkline_groups.add(SparklineType.Column, "A1:E1", False, dest)` を呼び出します。
4. 必要に応じて結果として得られる `SparklineGroup` をカスタマイズします。たとえば、`group.type` を設定して種類を確認したり、棒の色を調整したりします。
5. ワークブックを別の出力ファイルに保存し、折れ線スパークラインの例を上書きしないようにします。
次の例では、A1:E1 に値 5、-3、8、-2、6 を書き込み、F1 に縦棒スパークラインをレンダリングします。負の値は下向きの棒として、正の値は上向きの棒として描画されるため、正と負の寄与を一目で簡単に識別できます。

```python
import aspose.cells as ac
# ステップ1：Workbookを作成し、最初のワークシートを取得する
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# ステップ2：A1:E1にサンプル値を書き込む
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.cells[0, i].put_value(values[i])
# ステップ3：F1（列インデックス5、行インデックス0）を指すCellAreaを構築する
dest = ac.CellArea()
dest.start_column = 5
dest.end_column = 5
dest.start_row = 0
dest.end_row = 0
# ステップ4：目的のセルに縦棒スパークラインを追加する
idx = worksheet.sparkline_groups.add(
    ac.SparklineType.COLUMN, "A1:E1", False, dest)
group = worksheet.sparkline_groups[idx]
# ステップ5：group.Typeを読み取ってスパークラインの種類を確認する
print("Sparkline Type added: " + str(group.type))
# ステップ6：ワークブックを保存する
workbook.save("output_column.xlsx")
print("Workbook saved as output_column.xlsx")
```

## **勝敗スパークライン**
勝敗スパークラインは、縦棒スパークラインの特殊なバリエーションで、2 つの結果のみを表示するように設計されています。正の値は「上」バー (勝ち) として描画され、ゼロまたは負の値は「下」バー (負け) として描画されます。勝敗スパークラインは、一連の勝ち負け、合否結果、または時系列での任意の二項結果の視覚化によく使用されます。
Aspose.Cells では、`sparkline_groups.add` メソッドに `SparklineType.Stacked` を渡すことで勝敗スパークラインを作成します。(名前とは異なりますが、`SparklineType.Stacked` は勝敗レンダリングを要求するために使用される列挙値です。)
1. 新しい `Workbook` を作成し、最初のワークシートにアクセスします。
2. ソース範囲を入力します。勝敗スパークラインでは、すべての値が勝ちまたは負けとして扱われるため、値の大きさは重要ではなく、符号のみが重要です。正の値は上バーになり、非正の値は下バーになります。
3. 配置先セルを記述する `CellArea` を作成します。
4. `worksheet.sparkline_groups.add(SparklineType.Stacked, "A1:E1", False, dest)` を呼び出します。
5. 必要に応じて返された `SparklineGroup` をカスタマイズします。たとえば、勝ちバーと負けバーのアクセントカラーを設定します。
6. 3 つの例すべてがディスク上に共存できるように、ワークブックを別のファイル名で保存します。

```python
import aspose.cells as ac
import System.Drawing
# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells
# Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells["A1"].put_value(5)
cells["B1"].put_value(-3)
cells["C1"].put_value(8)
cells["D1"].put_value(-2)
cells["E1"].put_value(6)
# Step 3: Build a CellArea pointing to destination cell F1
dest = ac.CellArea()
dest.start_column = 5   # column F (0-indexed)
dest.end_column = 5
dest.start_row = 0      # row 1 (0-indexed)
dest.end_row = 0
# Step 4: Add a Line sparkline from A1:E1 into F1
# SparklineGroups.Add returns the index of the newly added group
index = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, dest)
group = worksheet.sparkline_groups[index]
# Step 5: Create a red CellsColor and assign it to the sparkline line color
red = workbook.create_cells_color()
red.color = System.Drawing.Color.Red
group.series_color = red
# Step 6: Enable high-point and low-point markers
group.show_high_point = True
group.show_low_point = True
# Step 7: Save the workbook
workbook.save("output_line.xlsx")
```

## **3 種類のスパークラインの組み合わせ**
次の統合例では、単一のワークブックを作成し、1 行目に値 5、-3、8、-2、6 を入力してから、セル F1、F2、F3 に 3 つのスパークライン グループ (各種類 1 つずつ) を追加し、結果のファイルで 3 種類のスパークライン スタイルすべてを一度に示します。

```python
import aspose.cells as ac
import System.Drawing
# ステップ 1: Workbook を作成し、最初のワークシートを取得します
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# ステップ 2: 行 1 (A1:E1) にサンプルデータを入力します
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
# ステップ 5: F3 に Win/Loss（積み上げ）スパークライン グループを追加します
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

## **スパークラインの外観のカスタマイズ**
`SparklineGroup` が作成され `worksheet.sparkline_groups` に追加されたら、ワークブックを保存する前にその視覚的プロパティのいくつかを読み取ったり変更したりできます。最も一般的にカスタマイズされるプロパティは次のとおりです。
- **`group.type`** — `SparklineType` (Line、Column、または Stacked)。グループ追加時に設定されますが、読み戻して確認できます。
- **`group.line.color`** — 線の色。`workbook.create_cells_color()` で作成された `CellsColor` として表されます。折れ線スパークラインの線の色を設定するために使用するプロパティです。
- **`group.line.weight`** — ポイント単位での線の太さ。値が大きいほど太い線になります。
- **高値/安値のポイントマーカー** — 最高および最低のデータポイントに小さなマーカー表示をオンにするフラグ。極端な値を強調するのに役立ちます。
- **最初/最後/負のポイントマーカー** — 最初、最後、負のデータポイントに対するマーカーを切り替えるフラグ。
色を変更するには、常に `CellsColor` インスタンスを作成し、関連するプロパティに割り当ててください。スパークラインの色プロパティは `aspose.cells.drawing` の `CellsColor` 型を期待しており、生のカラー値を直接割り当てください。`sparkline_groups.add` メソッド自体は完全に型付けされた `SparklineGroup` オブジェクトを返すため、戻り値のプロパティを連鎖して割り当てることも、ローカル変数に格納して保存前にカスタマイズすることもできます。
{{% /alert %}}

{{< app/cells/assistant language="python" >}}