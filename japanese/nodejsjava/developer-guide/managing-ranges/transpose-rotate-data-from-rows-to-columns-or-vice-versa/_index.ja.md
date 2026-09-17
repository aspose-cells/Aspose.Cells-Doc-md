---
title: 範囲の転置
linktitle: 範囲の転置
description: Aspose.Cells for Node.js via Java を使用して、Excel ファイル内の行と列のデータ (またはその逆) を転置 (回転) する方法を 3 つの異なるアプローチで説明します。
keywords: Aspose.Cells, Node.js via Java ライブラリ, スプレッドシート, 範囲の転置, データの回転, TRANSPOSE 関数, 動的配列数式, 配列数式, Excel TRANSPOSE, 行から列へ
type: docs
weight: 80
url: /ja/nodejs-java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Node.js via Java は、行を列に、列を行に変換する転置 (回転) を 3 つの異なる方法でサポートします。最初の方法では、インプレースの `Range.transpose()` メソッドを使用し、すべての Excel バージョンで動作します。2 番目の方法では、`Cell.setDynamicArrayFormula()` を使用して、Excel 365 または Excel 2021 で自動的にスピルする最新の動的配列 `=TRANSPOSE(...)` 数式を書き込みます。3 番目の方法では、`Cell.setArrayFormula()` を使用して、旧バージョンの Excel と互換性のあるクラシック型の Ctrl+Shift+Enter (CSE) 配列数式を書き込みます。この記事では、各アプローチを段階的な手順と完全なコード例で説明します。
{{% /alert %}}

## **Introduction**
範囲を転置するとは、行であったものを列に、列であったものを行になるように回転することを意味し、事実上、データを主対角線上で反射させます。Microsoft Excel では、ワークシート関数 `TRANSPOSE` がこの操作を実行し、概念的なリファレンスは [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) に記載されています。この概念はセルの範囲にプログラム的に適用することができ、多くのビジネスやレポートのシナリオで役立ちます。
- 四半期がページを横方向に、地域がページを縦方向に並ぶ、四半期別または年次の売上レポートの向きを変更する (またはその逆)。
- ダッシュボードやグラフで時系列がページを横方向にではなく縦方向に並ぶように、軸の向きを入れ替える。
- 外部システムからインポートしたデータを、下流の分析やレポートテンプレートで想定されるレイアウトに合わせて再構成する。
この記事の以降の説明を具体的にするため、すべての例では次の小さな「地域別・四半期別売上」テーブルを使用します。サンプルワークブックでは、このテーブルは範囲 **A1:D5** を占めており、**A1** は左上隅として空欄のまま、**B1:D1** には地域ヘッダー、**A2:A5** には四半期ヘッダーが入っています。
| 地域               | ヨーロッパ | アジア    | 北米         |
|--------------------|-----------|-----------|--------------|
| 第1四半期          | 21704714  | 8774099   | 12094215     |
| 第2四半期          | 17987034  | 12214447  | 10873099     |
| 第3四半期          | 19485029  | 14356879  | 15689543     |
| 第4四半期          | 22567894  | 15763492  | 17456723     |
続いて、この記事では Aspose.Cells for Node.js via Java を使用してこのデータを転置する 3 つの異なる方法を紹介します。それぞれが異なる Excel バージョンとユースケースに適しています。

## **Approach 1 — Transpose Range in Place (Range.transpose)**
`TRANSPOSE` ワークシート関数を使用せずにデータを転置したい場合は、この方法を使用してください。これは**すべての Excel バージョン**で動作し、動的配列に依存しないため、バージョン間で最も安全な互換性のあるオプションです。最終的な転置結果のみが必要で、ワークブックに元の `TRANSPOSE` 数式を保持する必要がない場合に最適です。

### **API used**
`Range.transpose()` は `com.aspose.cells.Range` クラスのインスタンスメソッドです。これを呼び出すと、範囲の行と列を入れ替えることで範囲がインプレースで反転し、行であったものは列になり、列であったものは行になります。このメソッドは、数式を記述せずに基になるセルを直接変更します。

### **Steps**
1. `LoadOptions` を `.xlsx` 形式に設定して、ソースワークブックを `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` で開きます。
2. ワークブックから最初のワークシートを `workbook.getWorksheets().get(0)` を使用して取得します。
3. `worksheet.getCells()` を通じてワークシートのセルコレクションにアクセスします。
4. `cells.createRange("A1:D5")` を呼び出して、**A1:D5** をカバーするソース範囲を作成します。
5. `source.transpose()` を呼び出して、行と列を入れ替えながら範囲をインプレースで回転します。
6. `workbook.save(outputFile)` でワークブックを保存します。
転置後、最初のアンカー範囲には回転後のデータが保持されます。最初の行は (空、**ヨーロッパ**、**アジア**、**北米**) となり、最初の列は (空、**第1四半期**、**第2四半期**、**第3四半期**、**第4四半期**) となります。元の売上列の各データが、転置後の範囲では行になります。

```python
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outputFile = "transposed.xlsx";
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
const workbook = new AsposeCells.Workbook(srcFile, loadOptions);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
const source = cells.createRange("A1:D5");
source.transpose();
workbook.save(outputFile);
```

## **Approach 2 — Transpose with a Dynamic Array Formula (Excel 365 / 2021)**
出力ワークブックにライブの数式として `=TRANSPOSE(A1:D5)` を保持し、ソースデータが変更された場合に結果が自動的に更新されるようにしたい場合、また対象の Excel ファイルが動的配列とスピル演算子がサポートされている **Excel 365 / Excel 2021 以降**で開かれる場合は、この方法を使用してください。

### **API used**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` は `com.aspose.cells.Cell` のメソッドで、セルの数式を**動的配列数式**として設定します。Excel は数式を 1 回評価し、結果を自動的に周囲のセルにスピルします。3 番目のパラメータを `true` に設定すると、書き込み時に結果の値も計算するように Aspose.Cells に指示します。

### **Steps**
1. ソースワークブックを `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` を使用して読み込みます。
2. 最初のワークシートを取得し、その `Cells` コレクションにアクセスします。
3. ソース範囲のすぐ下にあるセル **A6** に、`cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)` を呼び出して動的配列数式を配置します。
4. `null` 引数はデフォルトの `FormulaParseOptions` を渡し、3 番目の引数 `true` は Aspose.Cells に対して数式を動的配列として扱い、スピルされた値がワークブックに書き込まれるように評価するように指示します。
5. `workbook.save(outputFile)` でワークブックを保存します。
セル **A6** には数式 `=TRANSPOSE(A1:D5)` が保持され、Excel は結果を領域 **A6:D10** (転置されたデータと等しい 5 行 × 4 列のブロック) に自動的にスピルします。

{{% alert color="primary" %}}
この方法は **Excel 365 / 2021 以降でのみ**機能します。古い Excel バージョンでは動的配列数式が正しくスピルされません。
{{% /alert %}}

```python
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outFile = "output_transpose_dynamic.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new AsposeCells.FormulaParseOptions(), true);
workbook.save(outFile, AsposeCells.SaveFormat.Xlsx);
```

## **Approach 3 — Transpose with a Classic Array Formula (CSE)**
ワークブックに `TRANSPOSE` 数式を保持したいが、対象の Excel ファイルが動的配列のスピルがサポートされていない**古い Excel バージョン (2021 より前、2019、2016、2013 など)** で開かれる可能性がある場合は、この方法を使用してください。クラシックな CSE (Ctrl+Shift+Enter) 配列数式は、すべての Excel バージョンが評価できるレガシー互換の代替手段です。

### **API used**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` は `com.aspose.cells.Cell` のメソッドで、**クラシックな配列 (CSE) 数式**をアンカーセルに割り当て、結果として得られる配列の次元を宣言します。Aspose.Cells は複数セルの配列数式マーカーを書き込むため、Excel は宣言された範囲を埋める単一の配列式として数式を評価します。

### **Steps**
1. 前の方法と同様にソースワークブックを読み込みます。
2. 最初のワークシートを取得し、その `Cells` コレクションにアクセスします。
3. `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)` を呼び出します。2 番目の引数 `4` は宛先配列の行数、3 番目の引数 `5` は列数です。
4. `workbook.save(outputFile)` でワークブックを保存します。
セル **A6** は配列数式のアンカーであり、評価された配列は A6 から始まる 4 行 × 5 列にまたがり、ソース範囲 A1:D5 の転置次元と一致します。Excel は結果の範囲全体に単一の配列数式マーカーを書き込むため、古い Excel バージョンでも正しく評価されます。

{{% alert color="primary" %}}
CSE 配列数式は `TRANSPOSE` 式を評価するためのクラシックな Excel の方法であり、この方法は Excel のすべてのバージョンで普遍的に互換性があります。
{{% /alert %}}

```python
const AsposeCells = require("aspose.cells");
// Load the source workbook with xlsx LoadOptions
const srcFile = "source.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
// Access the first worksheet and its Cells collection
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// Set the classic CSE array formula on cell A6.
// The formula =TRANSPOSE(A1:D5) rotates the 5-row x 4-column source range
// into a 4-row x 5-column array. The second argument (4) is the number of rows
// and the third argument (5) is the number of columns of the resulting array.
// Aspose.Cells writes the CSE array-formula marker so Excel evaluates it as
// a single multi-cell array formula, compatible with older Excel versions
// (2019, 2016, 2013, etc.) that do not support dynamic array spilling.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Save the workbook so the array-formula marker is persisted
workbook.save("output.xlsx");
```

## **Comparison — When to Use Each Approach**
| 方法 | API / メソッド | Excel バージョン | ソース数式を保持するか | 出力範囲 |
|------|----------------|------------------|------------------------|----------|
| 方法 1 — インプレース転置 | `Range.transpose()` | すべての Excel バージョン | いいえ (値のみ) | 初期アンカー範囲、5×4 |
| 方法 2 — 動的配列数式 | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | はい (動的にスピル) | アンカーからスピル |
| 方法 3 — クラシック配列数式 (CSE) | `Cell.setArrayFormula` | すべての Excel バージョン | はい (複数セル配列数式) | 明示的なサイズ、4×5 |
迅速なバージョン横断的な変換が必要で、ファイルに転置された値のみを書き込む必要がある場合は、**方法 1** を使用してください。モダンの Excel が保証されており、ソースが変更された場合に数式をライブで更新したい場合は、**方法 2** を使用してください。動的配列をサポートしない古いリリースを含むすべての Excel バージョンで、保持された数式との幅広い互換性が必要な場合は、**方法 3** を使用してください。

## **Related Articles**
- [SmartMarker 単一セル配列レンダリング | Aspose.Cells for Node.js via Java](/cells/ja/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [セルへの画像の挿入](/cells/ja/nodejs-java/inserting-an-image-into-a-cell/)
- [Excel ファイルを複数のファイルに分割](/cells/ja/nodejs-java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="nodejs-java" >}}