---
title: Transpose Range
linktitle: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for Node.js via C++ with three different approaches.
keywords: Aspose.Cells, Node.js via C++ ライブラリ, スプレッドシート, 範囲の転置, データの回転, TRANSPOSE 関数, 動的配列数式, 配列数式, Excel TRANSPOSE, 行から列へ
type: docs
weight: 80
url: /ja/nodejs-cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ は、行を列に、列を行に転置（回転）する操作を 3 つの方法でサポートしています。1 つ目の方法では、インプレースの `range.transpose()` メソッドを使用し、すべての Excel バージョンで動作します。2 つ目の方法では、`cell.setDynamicArrayFormula()` を使用してモダンな動的配列の `=TRANSPOSE(...)` 数式を書き、Excel 365 または Excel 2021 で自動的にスピルさせます。3 つ目の方法では、`cell.setArrayFormula()` を使用して従来の Ctrl+Shift+Enter（CSE）配列数式を書き、旧バージョンの Excel と互換性を持たせます。この記事では、各方法を段階的な手順と完全なコード例で解説します。
{{% /alert %}}

## **Introduction**
範囲を転置するとは、行であったものを列に、列であったものを行にして、主対角線を軸に反転させることです。Microsoft Excel では、ワークシート関数 `TRANSPOSE` がこの操作を実行し、概念的なリファレンスは [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) に記載されています。同じ考え方をセル範囲に対してプログラム的に適用することもでき、多くの業務やレポートのシナリオで役立ちます。
転置が役立つ一般的なシナリオには、以下のようなものがあります。
- 四半期ごとや年次の売上レポートなど、通常はページ上を四半期方向に進み、ページ下を地域方向に並ぶレイアウトを、反対の向きに再構成するケース。
- ダッシュボードやグラフの軸方向を切り替え、時系列データがページを横方向にではなく縦方向に流れるようにするケース。
- 外部システムからインポートしたデータを、下流の分析やレポートテンプレートが期待するレイアウトに合わせて再形成するケース。
以降の説明を具体的にするため、すべての例では次の地域別・四半期別の小さな売上表を使用します。サンプルワークブックでは、この表は **A1:D5** の範囲を占めており、左上隅の **A1** は空白、**B1:D1** が地域ヘッダー、**A2:A5** が四半期ヘッダーとなっています。
| Region            | Europe    | Asia      | North America |
|-------------------|-----------|-----------|---------------|
| Qtr 1             | 21704714  | 8774099   | 12094215      |
| Qtr 2             | 17987034  | 12214447  | 10873099      |
| Qtr 3             | 19485029  | 14356879  | 15689543      |
| Qtr 4             | 22567894  | 15763492  | 17456723      |
続いて、Aspose.Cells for Node.js via C++ を使用してこのデータを転置する 3 つの方法を紹介します。それぞれ異なる Excel のバージョンとユースケースに適しています。

## **Approach 1 — Transpose Range in Place (range.transpose)**
`TRANSPOSE` ワークシート関数を使用せずデータのみを転置したい場合は、この方法を使用します。**すべてのバージョンの Excel** で動作し、動的配列に依存しないため、互換性の面で最も安全な選択肢です。最終的な転置出力のみが必要で、出力ファイルに元の `TRANSPOSE` 数式を残しておく必要がない場合に最適です。

### **API used**
`range.transpose()` は `Aspose.Cells.Range` クラスのインスタンスメソッドです。このメソッドを呼び出すと、範囲の行と列を入れ替えることでその場で反転され、行であったものは列に、列であったものは行になります。このメソッドは数式を書き込まずに、基になるセルを直接変更します。

### **Steps**
1. `LoadOptions` を `.xlsx` 形式に設定してソースワークブックを `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` で開きます。
2. `workbook.getWorksheets().get(0)` を使用して、ワークブックから最初のワークシートを取得します。
3. `worksheet.getCells()` を通じて、ワークシートのセルコレクションにアクセスします。
4. `cells.createRange("A1:D5")` を呼び出して、**A1:D5** をカバーするソース範囲を作成します。
5. `source.transpose()` を呼び出して、範囲をその場で回転し、行と列を入れ替えます。
6. `workbook.save(outputFile)` でワークブックを保存します。
転置後、同じアンカー範囲に回転されたデータが保持されます。最初の行は（空白、**Europe**、**Asia**、**North America**）となり、最初の列は（空白、**Qtr 1**、**Qtr 2**、**Qtr 3**、**Qtr 4**）となります。元の売上データの各列が、転置後の範囲では行になります。

```javascript
var srcFile = "source.xlsx";
var outputFile = "transposed.xlsx";
var workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
var worksheet = workbook.getWorksheets().get(0);
var cells = worksheet.getCells();
var source = cells.createRange("A1:D5");
source.transpose();
workbook.save(outputFile);
```

## **Approach 2 — Transpose with a Dynamic Array Formula (Excel 365 / 2021)**
出力ワークブックに `=TRANSPOSE(A1:D5)` の数式をライブの数式として保持し、ソースデータが変更された場合に結果が自動的に更新されるようにしたい場合はこの方法を使用します。また、対象の Excel ファイルが、動的配列とスピル演算子がサポートされている **Excel 365 / Excel 2021 以降**で開かれる場合にも適しています。

### **API used**
`cell.setDynamicArrayFormula(string formula, FormulaParseOptions options, bool calculateValue)` は `Aspose.Cells.Cell` のメソッドで、セルの数式を **動的配列数式** として設定します。Excel は数式を一度評価し、結果を周囲のセルに自動的にスピルさせます。3 番目のパラメータを `true` に設定すると、書き込み時に Aspose.Cells が結果の値も計算します。

### **Steps**
1. `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` を使用してソースワークブックを読み込みます。
2. 最初のワークシートを取得し、その `Cells` コレクションにアクセスします。
3. ソース範囲のすぐ下にあるセル **A6** に、`cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)` を呼び出して動的配列数式を設定します。
4. `null` 引数はデフォルトの `FormulaParseOptions` を渡し、3 番目の引数 `true` は Aspose.Cells に対して数式を動的配列として扱い、スピルされた値がワークブックに書き込まれるように評価するように指示します。
5. `workbook.save(outputFile)` でワークブックを保存します。
セル **A6** には `=TRANSPOSE(A1:D5)` の数式が保持され、Excel は結果を **A6:D10** の領域（転置されたデータと等しい 5 行 4 列のブロック）に自動的にスピルします。

{{% alert color="primary" %}}
この方法は **Excel 365 / 2021 以降** でのみ動作します。古いバージョンの Excel では動的配列数式を正しくスピルできません。
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outFile = "output_transpose_dynamic.xlsx";
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
const workbook = new AsposeCells.Workbook(srcFile, opts);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new AsposeCells.FormulaParseOptions(), true);
workbook.save(outFile, AsposeCells.SaveFormat.Xlsx);
```

## **Approach 3 — Transpose with a Classic Array Formula (CSE)**
ワークブック内に `TRANSPOSE` 数式を保持したいものの、対象の Excel ファイルが **古いバージョンの Excel（2021 より前、2019、2016、2013 など）** で開かれる可能性がある場合はこの方法を使用します。従来の CSE（Ctrl+Shift+Enter）配列数式は、すべての Excel バージョンで評価可能なレガシー互換の代替手段です。

### **API used**
`cell.setArrayFormula(string arrayFormula, int nRows, int nColumns)` は `Aspose.Cells.Cell` のメソッドで、**従来の配列（CSE）数式** をアンカーセルに割り当て、結果として得られる配列のサイズを宣言します。Aspose.Cells は複数セル配列数式マーカーを書き込むため、Excel は宣言された範囲を埋める単一の配列式として数式を評価します。

### **Steps**
1. これまでの方法と同様に、ソースワークブックを読み込みます。
2. 最初のワークシートを取得し、その `Cells` コレクションにアクセスします。
3. `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)` を呼び出します。2 番目の引数 `4` は結果配列の行数、3 番目の引数 `5` は列数です。
4. `workbook.save(outputFile)` でワークブックを保存します。
セル **A6** が配列数式のアンカーとなり、評価された配列は A6 から始まる 4 行 5 列に展開され、これは A1:D5 のソースを転置した次元と一致します。Excel は結果の範囲にわたって単一の配列数式マーカーを書き込むため、古いバージョンの Excel でも正しく評価されます。

{{% alert color="primary" %}}
CSE 配列数式は `TRANSPOSE` 式を評価する従来の Excel の方法であり、この方法は Excel のすべてのバージョンで普遍的に互換性があります。
{{% /alert %}}

```javascript
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
| 方法 | API / メソッド | Excel のバージョン | ソース数式を保持するか | 出力範囲 |
|----------|--------------|---------------|--------------------------|--------------|
| 方法 1 — インプレースでの転置 | `range.transpose()` | すべての Excel バージョン | いいえ（値のみ） | 同じアンカー範囲、5×4 |
| 方法 2 — 動的配列数式 | `cell.setDynamicArrayFormula` | Excel 365 / 2021 以降 | はい（動的にスピル） | アンカーからスピル |
| 方法 3 — 従来の配列数式（CSE） | `cell.setArrayFormula` | すべての Excel バージョン | はい（複数セル配列数式） | 明示的なサイズ、4×5 |
迅速でバージョン互換性のある変換が必要で、転置された値のみをファイルに書き込む場合は **方法 1** を使用します。最新の Excel が確実であり、ソースが変更された場合に数式がライブで更新されるようにしたい場合は **方法 2** を使用します。動的配列をサポートしない古いリリースを含め、すべての Excel バージョンと互換性があり、かつ数式を保持したい場合は **方法 3** を使用します。

## **Related Articles**
- [SmartMarker 単一セル配列のレンダリング](/cells/ja/nodejs-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [セルへの画像の挿入](/cells/ja/nodejs-cpp/inserting-an-image-into-a-cell/)
- [Excel ファイルを複数ファイルに分割する](/cells/ja/nodejs-cpp/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="nodejs-cpp" >}}