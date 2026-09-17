---
title: 範囲の転置
linktitle: 範囲の転置
description: この記事では、Aspose.Cells for Java を使用して Excel ファイル内のデータを 3 つの異なる方法で転置または回転する方法について説明します。
keywords: Aspose.Cells, Java library, spreadsheet, transpose range, rotate data, transpose function, dynamic array formula, array formula, Excel TRANSPOSE, Rows to Columns
type: docs
weight: 80
url: /ja/java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Java は、行を列に、列を行に転置（回転）する操作を 3 つの異なる方法でサポートします。1 つ目の方法はインプレースの `Range.transpose()` メソッドを使用し、すべての Excel バージョンで動作します。2 つ目の方法は `Cell.setDynamicArrayFormula()` を使用して、Excel 365 または Excel 2021 で自動的にスピルされる最新の動的配列数式 `=TRANSPOSE(...)` を記述します。3 つ目の方法は `Cell.setArrayFormula()` を使用して、古い Excel バージョンと互換性のある従来の Ctrl+Shift+Enter (CSE) 配列数式を記述します。この記事では、各方法をステップバイステップの手順と完全なコード例で説明します。
{{% /alert %}}

## **Introduction**
範囲を転置するとは、主対角線を越えてデータを実質的に反転し、行であったものを列に、列であったものを行に回転することです。Microsoft Excel では、ワークシート関数 `TRANSPOSE` がこの操作を実行し、その概念上のリファレンスは [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) で公開されています。この概念はセルの範囲に対してプログラム的に適用でき、多くのビジネスやレポートのシナリオで役立ちます。
- 四半期または年次の売上レポートを再構成する。通常は四半期がページ横方向に、地域がページ下方向に並んでいるレイアウトをその逆方向に回転する場合、またはその逆の場合。
- ダッシュボードやグラフの軸方向を切り替え、時系列データがページ横方向ではなくページ下方向に流れるようにする。
- 外部システムからインポートしたデータを整形し、下流の分析やレポートテンプレートが期待するレイアウトに合わせる。
記事の残りの部分を具体的にするため、すべての例では次の小さな地域別・四半期別売上テーブルを使用します。サンプルワークブックでは、このテーブルは **A1:D5** の範囲を占め、左上隅の **A1** は空白、**B1:D1** には地域ヘッダー、**A2:A5** には四半期ヘッダーが配置されます。
| Region            | Europe    | Asia      | North America |
|-------------------|-----------|-----------|---------------|
| Qtr 1             | 21704714  | 8774099   | 12094215      |
| Qtr 2             | 17987034  | 12214447  | 10873099      |
| Qtr 3             | 19485029  | 14356879  | 15689543      |
| Qtr 4             | 22567894  | 15763492  | 17456723      |
続いて、Aspose.Cells for Java を使用してこのデータを転置する 3 つの方法を紹介します。各方法は Excel のバージョンや用途に応じて使い分けます。

## **Approach 1 — Transpose Range in Place (Range.transpose)**
`TRANSPOSE` ワークシート関数を使用せずにデータを転置したい場合は、この方法を使用してください。**すべての Excel バージョン** で動作し、動的配列に依存しないため、互換性の高い最も安全な選択肢です。最終的な転置結果のみが必要で、ワークブックに元の `TRANSPOSE` 数式を残しておく必要がない場合に最適です。

### **API used**
`Range.transpose()` は `com.aspose.cells.Range` クラスのインスタンスメソッドです。これを呼び出すと、範囲の行と列を入れ替えることで範囲をインプレースで反転し、行であったものが列に、列であったものが行になります。このメソッドは数式を書き込まずに、基になるセルを直接変更します。

### **Steps**
1. `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` を呼び出して、ソースワークブックを `.xlsx` 形式の `LoadOptions` で開きます。
2. `workbook.getWorksheets().get(0)` を使用して、ワークブックから最初のワークシートを取得します。
3. `worksheet.getCells()` を通じて、ワークシートのセルコレクションにアクセスします。
4. `cells.createRange("A1:D5")` を呼び出して、**A1:D5** をカバーするソース範囲を作成します。
5. `source.transpose()` を呼び出して範囲を行と列を入れ替えてインプレースで回転します。
6. `workbook.save(outputFile)` でワークブックを保存します。
転置後、最初のアンカー範囲には回転されたデータが保持されます。最初の行は (空白、**Europe**、**Asia**、**North America**) となり、最初の列は (空白、**Qtr 1**、**Qtr 2**、**Qtr 3**、**Qtr 4**) となります。元の各売上列が、転置後の範囲では行になります。

```java
import com.aspose.cells.*;
String srcFile = "source.xlsx";
String outputFile = "transposed.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
source.transpose();
workbook.save(outputFile);
```

## **Approach 2 — Transpose with a Dynamic Array Formula (Excel 365 / 2021)**
出力ワークブックで `=TRANSPOSE(A1:D5)` 数式をライブの数式として保持し、ソースデータが変更された場合に結果が自動的に更新されるようにしたい場合、そして対象の Excel ファイルが動的配列とスピル演算子をサポートする **Excel 365 / Excel 2021 以降** で開かれる場合は、この方法を使用してください。

### **API used**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` は `com.aspose.cells.Cell` のメソッドで、セルの数式を **動的配列数式** として設定します。Excel は数式を一度評価し、結果を周囲のセルに自動的にスピルします。3 番目のパラメータを `true` に設定すると、書き込み時に結果の値も計算するよう Aspose.Cells に指示します。

### **Steps**
1. `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` を使用して、ソースワークブックを読み込みます。
2. 最初のワークシートを取得し、その `Cells` コレクションにアクセスします。
3. `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)` を呼び出して、ソース範囲のすぐ下にあるセル **A6** に動的配列数式を配置します。
4. `null` 引数はデフォルトの `FormulaParseOptions` を渡し、3 番目の引数 `true` は Aspose.Cells に対して数式を動的配列として扱い、スピルされた値がワークブックに書き込まれるように評価するように指示します。
5. `workbook.save(outputFile)` でワークブックを保存します。
セル **A6** には数式 `=TRANSPOSE(A1:D5)` が保持され、Excel は結果を **A6:D10** の領域（転置されたデータと同じ 5 行 4 列のブロック）に自動的にスピルします。

{{% alert color="primary" %}}
この方法は **Excel 365 / 2021 以降でのみ** 動作します。古い Excel バージョンでは動的配列数式が正しくスピルされません。
{{% /alert %}}

```java
import com.aspose.cells.*;
String srcFile = "source.xlsx";
String outFile = "output_transpose_dynamic.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true);
workbook.save(outFile, SaveFormat.XLSX);
```

## **Approach 3 — Transpose with a Classic Array Formula (CSE)**
`TRANSPOSE` 数式をワークブックに保持したいが、対象の Excel ファイルが動的配列のスピルをサポートしていない **古い Excel バージョン（2021 より前、2019、2016、2013 など）** で開かれる可能性がある場合は、この方法を使用してください。従来の CSE（Ctrl+Shift+Enter）配列数式は、すべての Excel バージョンで評価可能なレガシー互換の代替手段です。

### **API used**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` は `com.aspose.cells.Cell` のメソッドで、**従来の配列（CSE）数式** をアンカーセルに割り当て、結果として得られる配列の次元を宣言します。Aspose.Cells は複数セルの配列数式マーカーを書き込むため、Excel は宣言された範囲を埋める単一の配列式として数式を評価します。

### **Steps**
1. 前の方法で説明したように、ソースワークブックを読み込みます。
2. 最初のワークシートを取得し、その `Cells` コレクションにアクセスします。
3. `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)` を呼び出します。2 番目の引数 `4` はコピー先の配列の行数で、3 番目の引数 `5` はコピー先の配列の列数です。
4. `workbook.save(outputFile)` でワークブックを保存します。
セル **A6** が配列数式のアンカーとなり、評価された配列は A6 から始まる 4 行 5 列にまたがり、ソース範囲 A1:D5 の転置された次元と一致します。Excel は結果の範囲全体に単一の配列数式マーカーを書き込むため、古い Excel バージョンでも正しく評価されます。

{{% alert color="primary" %}}
CSE 配列数式は、`TRANSPOSE` 式を評価するための従来の Excel の方法であり、この方法は Excel のすべてのバージョンで普遍的に互換性があります。
{{% /alert %}}

```java
import com.aspose.cells.*;
// Load the source workbook with xlsx LoadOptions
String srcFile = "source.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
// Access the first worksheet and its Cells collection
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
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
| 方法 | API / メソッド | Excel バージョン | 元の数式が保持されるか | 出力範囲 |
|----------|--------------|---------------|--------------------------|--------------|
| 方法 1 — インプレース転置 | `Range.transpose()` | すべての Excel バージョン | いいえ（値のみ） | 初期アンカー範囲、5×4 |
| 方法 2 — 動的配列数式 | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | はい（動的にスピル） | アンカーからスピル |
| 方法 3 — 従来の配列数式 (CSE) | `Cell.setArrayFormula` | すべての Excel バージョン | はい（複数セル配列数式） | 明示的なサイズ、4×5 |
迅速でバージョン横断的な変換が必要で、ファイルに転置された値のみを書き込む必要がある場合は、**方法 1** を使用してください。最新の Excel が確実に使用され、ソースが変更された場合に数式をライブで更新したい場合は、**方法 2** を使用してください。動的配列をサポートしない古いバージョンを含むすべての Excel バージョンで、数式を保持したまま最大限の互換性が必要な場合は、**方法 3** を使用してください。

## **Related Articles**
- [SmartMarker Single Cell Array Rendering | Aspose.Cells Java](/cells/ja/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Inserting an Image into a Cell](/cells/ja/java/inserting-an-image-into-a-cell/)
- [Splitting Excel Files into Multiple Files](/cells/ja/java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="java" >}}