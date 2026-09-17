---
title: 範囲の転置
linktitle: 範囲の転置
description: Aspose.Cells for Python via Java を使用して、Excel ファイル内のデータを行から列へ、または列から行へ転置（回転）する方法を 3 つの異なるアプローチで説明します。
keywords: Aspose.Cells, Python via Java ライブラリ, スプレッドシート, 範囲の転置, データ回転, TRANSPOSE 関数, 動的配列数式, 配列数式, Excel TRANSPOSE, 行から列
type: docs
weight: 80
url: /ja/python-java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Python via Java は、行を列に、列を行に転置（回転）する操作を 3 つの異なる方法でサポートしています。最初のアプローチはインプレースの `Range.transpose()` メソッドを使用し、すべての Excel バージョンで動作します。2 つ目は `Cell.setDynamicArrayFormula()` を使用して、Excel 365 または Excel 2021 で自動的にスピルする最新の動的配列 `=TRANSPOSE(...)` 数式を書き込みます。3 つ目のアプローチは `Cell.setArrayFormula()` を使用して、旧バージョンの Excel と互換性のある従来の Ctrl+Shift+Enter (CSE) 配列数式を書き込みます。この記事では、各アプローチをステップバイステップの手順と完全なコード例で説明します。
{{% /alert %}}

## **Introduction**
範囲の転置とは、行であったものを列に、列であったものを行にするように回転することを意味し、実質的にはデータを主対角線を軸に反転させます。Microsoft Excel では、ワークシート関数 `TRANSPOSE` がこの操作を実行し、概念的なリファレンスは [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) に記載されています。この概念はセル範囲に対してプログラム的に適用でき、多くのビジネスやレポートのシナリオで役立ちます。
- 四半期が通常ページを横方向に進み、地域がページを縦方向に進む、四半期別または年次の売上レポートの向きを変更する（またはその逆）。
- ダッシュボードやグラフで軸の向きを切り替え、時系列が横方向ではなく縦方向に並ぶようにする。
- 外部システムからインポートしたデータを再形成し、下流の分析やレポートテンプレートが想定するレイアウトに一致させる。
記事の残りの部分を具体的にするために、すべての例では以下の地域別・四半期別の売上表を使用します。サンプルワークブックでは、この表は範囲 **A1:D5** を占めており、**A1** は左上隅として空白、**B1:D1** は地域ヘッダー、**A2:A5** は四半期ヘッダーとなっています。
| 地域              | Europe    | Asia      | North America |
|-------------------|-----------|-----------|---------------|
| Qtr 1             | 21704714  | 8774099   | 12094215      |
| Qtr 2             | 17987034  | 12214447  | 10873099      |
| Qtr 3             | 19485029  | 14356879  | 15689543      |
| Qtr 4             | 22567894  | 15763492  | 17456723      |
続いて、Aspose.Cells for Python via Java を使用してこのデータを転置する 3 つの異なる方法を紹介します。それぞれが異なる Excel バージョンとユースケースに適しています。

## **Approach 1 — Transpose Range in Place (Range.transpose)**
`TRANSPOSE` ワークシート関数を使用せずにデータを転置したい場合は、このアプローチを使用してください。これは**すべての Excel バージョン**で動作し、動的配列に依存しないため、最も安全なクロスバージョン互換オプションです。最終的な転置された出力のみが必要で、ワークブックに元の `TRANSPOSE` 数式を保持する必要がない場合に最適です。

### **API used**
`Range.transpose()` は `com.aspose.cells.Range` クラスのインスタンスメソッドです。これを呼び出すと、行と列を交換して範囲をインプレースで反転させ、行であったものが列になり、列であったものが行になります。このメソッドは数式を書き込まずに、基になるセルを直接変更します。

### **Steps**
1. `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))` を呼び出して、`LoadOptions` を `.xlsx` 形式に設定したソースワークブックを開きます。
2. `workbook.getWorksheets().get(0)` を使用して、ワークブックから最初のワークシートを取得します。
3. `worksheet.getCells()` を通じてワークシートのセルコレクションにアクセスします。
4. `cells.createRange("A1:D5")` を呼び出して、**A1:D5** をカバーするソース範囲を作成します。
5. `source.transpose()` を呼び出して、範囲をインプレースで回転させ、行と列を交換します。
6. `workbook.save(outputFile)` でワークブックを保存します。
転置後、初期アンカー範囲には回転されたデータが保持されます。最初の行は (空、**Europe**、**Asia**、**North America**) となり、最初の列は (空、**Qtr 1**、**Qtr 2**、**Qtr 3**、**Qtr 4**) となります。元の各売上列が転置された範囲で行になります。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, LoadOptions, LoadFormat
srcFile = "source.xlsx"
outputFile = "transposed.xlsx"
loadOptions = LoadOptions(LoadFormat.Xlsx)
workbook = Workbook(srcFile, loadOptions)
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
source = cells.createRange("A1:D5")
source.transpose()
workbook.save(outputFile)
jpype.shutdownJVM()
```

## **Approach 2 — Transpose with a Dynamic Array Formula (Excel 365 / 2021)**
出力ワークブックで `=TRANSPOSE(A1:D5)` 数式をライブの数式として保持し、ソースデータが変更された場合に結果が自動的に更新されるようにしたい場合、また対象の Excel ファイルが動的配列とスピル演算子がサポートされている **Excel 365 / Excel 2021 以降**で開かれる場合は、このアプローチを使用してください。

### **API used**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` は `com.aspose.cells.Cell` のメソッドで、セルの数式を**動的配列数式**として設定します。Excel は数式を一度評価し、結果を周囲のセルに自動的にスピルします。3 番目のパラメータを `True` に設定すると、書き込み時に結果の値も計算するように Aspose.Cells に指示します。

### **Steps**
1. `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))` を使用してソースワークブックを読み込みます。
2. 最初のワークシートを取得し、その `Cells` コレクションにアクセスします。
3. `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", None, True)` を呼び出して、ソース範囲のすぐ下にあるセル **A6** に動的配列数式を配置します。
4. `None` 引数はデフォルトの `FormulaParseOptions` を渡し、3 番目の引数 `True` は Aspose.Cells に対して、数式を動的配列として扱い、スピルされた値がワークブックに書き込まれるように評価するよう指示します。
5. `workbook.save(outputFile)` でワークブックを保存します。
セル **A6** には数式 `=TRANSPOSE(A1:D5)` が保持され、Excel は結果を領域 **A6:D10**（転置されたデータと等しい 5 行 × 4 列のブロック）に自動的にスピルします。

{{% alert color="primary" %}}
このアプローチは **Excel 365 / 2021 以降でのみ**動作します。古い Excel バージョンでは動的配列数式が正しくスピルされません。
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, LoadOptions, LoadFormat, FormulaParseOptions, SaveFormat
# ported code here
srcFile = "source.xlsx"
outFile = "output_transpose_dynamic.xlsx"
workbook = Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", FormulaParseOptions(), True)
workbook.save(outFile, SaveFormat.Xlsx)
jpype.shutdownJVM()
```

## **Approach 3 — Transpose with a Classic Array Formula (CSE)**
ワークブックに `TRANSPOSE` 数式を保持したいが、対象の Excel ファイルが動的配列のスピルがサポートされていない**古い Excel バージョン（2021 より前、2019、2016、2013 など）**で開かれる可能性がある場合は、このアプローチを使用してください。従来の CSE (Ctrl+Shift+Enter) 配列数式は、すべての Excel バージョンが評価できるレガシー互換の代替手段です。

### **API used**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` は `com.aspose.cells.Cell` のメソッドで、アンカーセルに**従来の配列 (CSE) 数式**を割り当て、結果として得られる配列の次元を宣言します。Aspose.Cells は複数セルの配列数式マーカーを書き込むため、Excel は宣言された範囲を埋める単一の配列式として数式を評価します。

### **Steps**
1. 前のアプローチで説明したようにソースワークブックを読み込みます。
2. 最初のワークシートを取得し、その `Cells` コレクションにアクセスします。
3. `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)` を呼び出します。2 番目の引数 `4` は宛先配列の行数、3 番目の引数 `5` は列数です。
4. `workbook.save(outputFile)` でワークブックを保存します。
セル **A6** は配列数式のアンカーであり、評価された配列は A6 から始まる 4 行 × 5 列に及び、A1:D5 ソースの転置された次元と一致します。Excel は結果の範囲全体に単一の配列数式マーカーを書き込むため、古い Excel バージョンでも正しく評価されます。

{{% alert color="primary" %}}
CSE 配列数式は `TRANSPOSE` 式を評価する従来の Excel の方法であり、このアプローチは Excel の全バージョンで普遍的に互換性があります。
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, LoadOptions, LoadFormat, Worksheet, Cells
# Load the source workbook with xlsx LoadOptions
srcFile = "source.xlsx"
workbook = Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))
# Access the first worksheet and its Cells collection
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
# Set the classic CSE array formula on cell A6.
# The formula =TRANSPOSE(A1:D5) rotates the 5-row x 4-column source range
# into a 4-row x 5-column array. The second argument (4) is the number of rows
# and the third argument (5) is the number of columns of the resulting array.
# Aspose.Cells writes the CSE array-formula marker so Excel evaluates it as
# a single multi-cell array formula, compatible with older Excel versions
# (2019, 2016, 2013, etc.) that do not support dynamic array spilling.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)
# Save the workbook so the array-formula marker is persisted
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Comparison — When to Use Each Approach**
| アプローチ | API / メソッド | Excel バージョン | ソース数式の保持 | 出力範囲 |
|----------|--------------|---------------|--------------------------|--------------|
| アプローチ 1 — インプレース転置 | `Range.transpose()` | すべての Excel バージョン | いいえ（値のみ） | 初期アンカー範囲、5×4 |
| アプローチ 2 — 動的配列数式 | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | はい（動的にスピル） | アンカーからスピル |
| アプローチ 3 — 従来の配列数式 (CSE) | `Cell.setArrayFormula` | すべての Excel バージョン | はい（複数セル配列数式） | 明示的なサイズ、4×5 |
迅速でクロスバージョン互換の変換が必要で、転置された値をファイルに書き込むだけでよい場合は、**アプローチ 1** を使用してください。最新の Excel が保証されており、ソースが変更された場合に数式をライブで更新したい場合は、**アプローチ 2** を使用してください。動的配列をサポートしない古いバージョンを含むすべての Excel バージョンで、保持された数式との最大限の互換性が必要な場合は、**アプローチ 3** を使用してください。

## **Related Articles**
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for Python via Java](/cells/ja/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [セルへの画像の挿入](/cells/ja/python-java/inserting-an-image-into-a-cell/)
- [Excel ファイルを複数のファイルに分割する](/cells/ja/python-java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="python" >}}