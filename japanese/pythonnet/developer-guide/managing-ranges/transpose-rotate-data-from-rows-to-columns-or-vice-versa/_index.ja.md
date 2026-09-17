---
title: 範囲の轉置
linktitle: 範囲の轉置
description: 本記事では、Aspose.Cells for Python via .NET を使用して、Excel ファイル内の行から列、または列から行へデータを転置（回転）する方法を 3 つの異なるアプローチで解説します。
keywords: Aspose.Cells for Python via .NET, スプレッドシート, 範囲の轉置, データ回転, TRANSPOSE 関数, 動的配列数式, 配列数式, Excel TRANSPOSE, 行から列
type: docs
weight: 80
url: /ja/python-net/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET は、行を列に、列を行に変換するデータ転置（回転）を 3 つの方法でサポートします。最初のアプローチはインプレースで実行する `range.transpose()` メソッドを使用し、すべての Excel バージョンで動作します。2 つ目は `cell.set_dynamic_array_formula()` を使用して、Excel 365 または Excel 2021 で自動的にスピルする最新の動的配列数式 `=TRANSPOSE(...)` を書き込みます。3 つ目のアプローチは `cell.set_array_formula()` を使用して、古い Excel バージョンと互換性のある従来の Ctrl+Shift+Enter (CSE) 配列数式を書き込みます。本記事では、各アプローチを段階的な手順と完全なコード例で解説します。
{{% /alert %}}

## **Introduction**
範囲を転置するとは、行であったものを列に、列であったものを行になるように回転し、事実上データを主対角線で反射させることを意味します。Microsoft Excel では、ワークシート関数 `TRANSPOSE` がこの操作を実行します。概念的なリファレンスは [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) に記載されています。この概念はセルの範囲に対してプログラムで適用でき、多くのビジネスやレポートのシナリオで役立ちます。
- 四半期が通常ページ横方向、地域がページ縦方向に並ぶ四半期または年次の売上レポートを再配置する（またはその逆）。
- ダッシュボードやグラフの軸方向を切り替え、時系列データをページ横方向ではなく縦方向に並ぶようにする。
- 外部システムからインポートしたデータを再整形し、下流の分析やレポートテンプレートが想定するレイアウトに合わせる。
以降の説明を具体化するため、すべての例では以下の小さな地域別・四半期別売上テーブルを使用します。サンプルワークブックでは、このテーブルは範囲 **A1:D5** を占め、左上隅の **A1** は空欄、**B1:D1** は地域ヘッダー、**A2:A5** は四半期ヘッダーとなっています。
| 地域         | ヨーロッパ | アジア    | 北米        |
|--------------|------------|-----------|-------------|
| 第1四半期    | 21704714   | 8774099   | 12094215    |
| 第2四半期    | 17987034   | 12214447  | 10873099    |
| 第3四半期    | 19485029   | 14356879  | 15689543    |
| 第4四半期    | 22567894   | 15763492  | 17456723    |
続いて本記事では、Aspose.Cells for Python via .NET を使用してこのデータを転置する 3 つの異なる方法を紹介します。それぞれ異なる Excel バージョンとユースケースに対応しています。

## **Approach 1 — Transpose Range in Place (range.transpose)**
`TRANSPOSE` ワークシート関数を使用せずにデータを転置したい場合は、このアプローチを使用してください。**すべてのバージョンの Excel** で動作し、動的配列に依存しないため、バージョンをまたいで最も互換性に優れた安全なオプションです。最終的な転置出力のみが必要で、ワークブックに元の `TRANSPOSE` 数式を保持しておく必要がない場合に最適です。

### **API used**
`range.transpose()` は `Aspose.Cells.Range` クラスのインスタンスメソッドです。これを呼び出すと、範囲の行と列が入れ替わり、その場で反転されます。つまり、行であったものが列になり、列であったものが行になります。このメソッドは数式を書き込まずに、底层のセルを直接変更します。

### **Steps**
1. `LoadOptions` を `.xlsx` 形式に設定し、`Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))` を呼び出してソースワークブックを開きます。
2. `workbook.worksheets[0]` を使用して、ワークブックから最初のワークシートを取得します。
3. `worksheet.cells` を通じてワークシートのセルコレクションにアクセスします。
4. `cells.create_range("A1:D5")` を呼び出して、**A1:D5** をカバーするソース範囲を作成します。
5. `source.transpose()` を呼び出して範囲をその場で回転し、行と列を入れ替えます。
6. `workbook.save(outputFile)` でワークブックを保存します。
転置後、初期アンカー範囲には反転されたデータが保持されます。最初の行は (空、**ヨーロッパ**、**アジア**、**北米**) となり、最初の列は (空、**第1四半期**、**第2四半期**、**第3四半期**、**第4四半期**) になります。元の売上の各列が、転置された範囲では行になります。

```python
import aspose.cells as ac
srcFile = "source.xlsx"
outputFile = "transposed.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.XLSX))
worksheet = workbook.worksheets[0]
cells = worksheet.cells
source = cells.create_range("A1:D5")
source.transpose()
workbook.save(outputFile)
```

## **Approach 2 — Transpose with a Dynamic Array Formula (Excel 365 / 2021)**
出力ワークブックに `=TRANSPOSE(A1:D5)` 数式をライブ数式として保持し、ソースデータが変更された場合に結果が自動的に更新されるようにしたい場合で、かつ対象の Excel ファイルが動的配列とスピル演算子がサポートされている **Excel 365 / Excel 2021 以降**で開かれる場合は、このアプローチを使用してください。

### **API used**
`cell.set_dynamic_array_formula(formula, options, calculate_value)` は `Aspose.Cells.Cell` のメソッドで、セルの数式を**動的配列数式**として設定します。Excel は数式を 1 回評価し、結果を周囲のセルに自動的にスピルします。3 番目のパラメータを `True` に設定すると、書き込み時に結果の値も計算するよう Aspose.Cells に指示します。

### **Steps**
1. `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))` を使用してソースワークブックを読み込みます。
2. 最初のワークシートを取得し、その `cells` コレクションにアクセスします。
3. ソース範囲の直下にあるセル **A6** に、`cells["A6"].set_dynamic_array_formula("=TRANSPOSE(A1:D5)", None, True)` を呼び出して動的配列数式を配置します。
4. `None` 引数はデフォルトの `FormulaParseOptions` を渡し、3 番目の引数 `True` は Aspose.Cells に対して、数式を動的配列として扱い、スピル値がワークブックに書き込まれるように評価するよう指示します。
5. `workbook.save(outputFile)` でワークブックを保存します。
セル **A6** には数式 `=TRANSPOSE(A1:D5)` が保持され、Excel は結果を自動的に領域 **A6:D10**（転置されたデータと等しい 5 行 × 4 列のブロック）にスピルします。

{{% alert color="primary" %}}
このアプローチは **Excel 365 / 2021 以降でのみ**動作します。古い Excel バージョンでは動的配列数式は正しくスピルされません。
{{% /alert %}}

```python
import aspose.cells as ac
srcFile = "source.xlsx"
outFile = "output_transpose_dynamic.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.Xlsx))
worksheet = workbook.worksheets[0]
cells = worksheet.cells
cells["A6"].set_dynamic_array_formula("=TRANSPOSE(A1:D5)", ac.FormulaParseOptions(), True)
workbook.save(outFile, ac.SaveFormat.Xlsx)
```

## **Approach 3 — Transpose with a Classic Array Formula (CSE)**
`TRANSPOSE` 数式をワークブックに保持したいが、対象の Excel ファイルが動的配列のスピルをサポートしていない**古い Excel バージョン（2021 より前、2019、2016、2013 など）**で開かれる可能性がある場合は、このアプローチを使用してください。従来の CSE (Ctrl+Shift+Enter) 配列数式は、すべての Excel バージョンで評価可能なレガシー互換の代替手段です。

### **API used**
`cell.set_array_formula(array_formula, n_rows, n_columns)` は `Aspose.Cells.Cell` のメソッドで、**従来の配列 (CSE) 数式**をアンカーセルに割り当て、結果配列の次元を宣言します。Aspose.Cells は複数セルの配列数式マーカーを書き込むため、Excel は宣言された範囲を埋める単一の配列式として数式を評価します。

### **Steps**
1. 前のアプローチで説明したようにソースワークブックを読み込みます。
2. 最初のワークシートを取得し、その `cells` コレクションにアクセスします。
3. `cells["A6"].set_array_formula("=TRANSPOSE(A1:D5)", 4, 5)` を呼び出します。2 番目の引数 `4` は出力先の配列の行数、3 番目の引数 `5` は列数です。
4. `workbook.save(outputFile)` でワークブックを保存します。
セル **A6** は配列数式のアンカーであり、評価された配列は A6 から始まる 4 行 × 5 列に及び、A1:D5 ソースの轉置された次元と一致します。Excel は結果の範囲に 1 つの配列数式マーカーを書き込むため、古い Excel バージョンでも正しく評価されます。

{{% alert color="primary" %}}
CSE 配列数式は `TRANSPOSE` 式を評価する従来の Excel の方法であり、このアプローチは Excel のすべてのバージョンで普遍的に互換性があります。
{{% /alert %}}

```python
import aspose.cells as ac
# Load the source workbook with xlsx LoadOptions
srcFile = "source.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.Xlsx))
# Access the first worksheet and its Cells collection
worksheet = workbook.worksheets[0]
cells = worksheet.cells
# Set the classic CSE array formula on cell A6.
# The formula =TRANSPOSE(A1:D5) rotates the 5-row x 4-column source range
# into a 4-row x 5-column array. The second argument (4) is the number of rows
# and the third argument (5) is the number of columns of the resulting array.
# Aspose.Cells writes the CSE array-formula marker so Excel evaluates it as
# a single multi-cell array formula, compatible with older Excel versions
# (2019, 2016, 2013, etc.) that do not support dynamic array spilling.
cells["A6"].set_array_formula("=TRANSPOSE(A1:D5)", 4, 5)
# Save the workbook so the array-formula marker is persisted
workbook.save("output.xlsx")
```

## **Comparison — When to Use Each Approach**
| アプローチ | API / メソッド | Excel バージョン | ソース数式を保持するか | 出力範囲 |
|-----------|----------------|------------------|------------------------|----------|
| アプローチ 1 — インプレース転置 | `range.transpose()` | すべての Excel バージョン | いいえ（値のみ） | 初期アンカー範囲、5×4 |
| アプローチ 2 — 動的配列数式 | `cell.set_dynamic_array_formula` | Excel 365 / 2021+ | はい（動的にスピル） | アンカーからスピル |
| アプローチ 3 — 従来の配列数式 (CSE) | `cell.set_array_formula` | すべての Excel バージョン | はい（複数セル配列数式） | 明示的なサイズ、4×5 |
迅速なバージョン横断の変換が必要で、ファイルに転置された値のみを書き込む必要がある場合は、**アプローチ 1** を使用してください。最新の Excel が保証されており、ソースが変更された場合に数式をライブで保ち更新したい場合は、**アプローチ 2** を使用してください。動的配列をサポートしない古いリリースを含むすべての Excel バージョンで、数式を保持したまま最も広い互換性が必要な場合は、**アプローチ 3** を使用してください。

## **Related Articles**
- [SmartMarker 単一セル配列レンダリング | Aspose.Cells for Python via .NET](/cells/ja/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [セルへの画像の挿入](/cells/ja/python-net/inserting-an-image-into-a-cell/)
- [Excel ファイルを複数ファイルに分割](/cells/ja/python-net/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="python-net" >}}