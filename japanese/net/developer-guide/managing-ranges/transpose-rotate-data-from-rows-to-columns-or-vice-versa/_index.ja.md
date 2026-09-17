---
title: 範囲の転置
linktitle: 範囲の転置
description: 本記事では、Aspose.Cells for .NET を使用して Excel ファイル内のデータを行から列へ、または列から行へ転置（回転）する方法を、3 つの異なるアプローチで説明します。
keywords: Aspose.Cells, .NET ライブラリ, スプレッドシート, 範囲の転置, データの回転, TRANSPOSE 関数, 動的配列数式, 配列数式, Excel TRANSPOSE, 行から列
type: docs
weight: 80
url: /ja/net/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for .NET は、行を列に、列を行に変換するデータ転置（回転）を 3 つの方法でサポートします。1 つ目のアプローチはインプレースの `Range.Transpose()` メソッドを使用し、すべての Excel バージョンで動作します。2 つ目は `Cell.SetDynamicArrayFormula()` を使用して、Excel 365 または Excel 2021 で自動的にスピルするモダンな動的配列数式 `=TRANSPOSE(...)` を記述します。3 つ目のアプローチは `Cell.SetArrayFormula()` を使用して、古い Excel バージョンと互換性のある従来の Ctrl+Shift+Enter (CSE) 配列数式を記述します。本記事では、各アプローチを段階的な手順と完全なコード例で説明します。
{{% /alert %}}

## **はじめに**
範囲の転置とは、行であったものを列に、列であったものを行に、つまり主対角線を軸としてデータを反転させるように回転させることです。Microsoft Excel では、ワークシート関数 `TRANSPOSE` がこの操作を実行し、概念上のリファレンスは [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) に記載されています。この概念はセルの範囲に対してプログラム的に適用でき、多くのビジネスやレポートのシナリオで役立ちます。
- 通常はページ横方向に四半期が並び、ページ下方向に地域が並ぶレイアウト（またはその逆）の四半期ごとまたは年間の売上レポートを再構成する。
- ダッシュボードやグラフで時系列がページ横方向ではなくページ下方向に並ぶように、軸の向きを交換する。
- 外部システムからインポートしたデータを、下流の分析やレポートテンプレートで想定されるレイアウトに合わせて整形する。
本記事の以降の説明を具体化するため、すべての例では次の地域別・四半期別の売上テーブルを使用します。サンプルワークブックでは、このテーブルは範囲 **A1:D5** を占め、左上隅の **A1** は空欄、**B1:D1** は地域ヘッダー、**A2:A5** は四半期ヘッダーとなっています。
| 地域              | ヨーロッパ | アジア     | 北米         |
|-------------------|-----------|-----------|---------------|
| 第 1 四半期       | 21704714  | 8774099   | 12094215      |
| 第 2 四半期       | 17987034  | 12214447  | 10873099      |
| 第 3 四半期       | 19485029  | 14356879  | 15689543      |
| 第 4 四半期       | 22567894  | 15763492  | 17456723      |
本記事では、Aspose.Cells for .NET を使用してこのデータを転置する 3 つの異なる方法を紹介します。それぞれが異なる Excel バージョンとユースケースに適しています。

## **アプローチ 1 — 範囲をインプレースで転置する (Range.Transpose)**
`TRANSPOSE` ワークシート関数を使用せずにデータを転置したい場合は、このアプローチを使用してください。**すべての Excel バージョン**で動作し、動的配列に依存しないため、バージョンを横断して最も安全な互換性オプションです。最終的な転置出力のみが必要で、ワークブックに元の `TRANSPOSE` 数式を保持する必要がない場合に最適です。

### **使用される API**
`Range.Transpose()` は `Aspose.Cells.Range` クラスのインスタンスメソッドです。これを呼び出すと、行と列を交換して範囲をインプレースで反転させ、行であったものが列に、列であったものが行になります。このメソッドは数式を記述せずに基になるセルを直接変更します。

### **手順**
1. ソースワークブックを、`LoadOptions` を `.xlsx` 形式に設定して `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` を呼び出して開きます。
2. `workbook.Worksheets[0]` を使用して、ワークブックから最初のワークシートを取得します。
3. `worksheet.Cells` を通じて、ワークシートのセルコレクションにアクセスします。
4. `cells.CreateRange("A1:D5")` を呼び出して、**A1:D5** をカバーするソース範囲を作成します。
5. `source.Transpose()` を呼び出して、範囲をインプレースで回転させ、行と列を交換します。
6. `workbook.Save(outputFile)` でワークブックを保存します。
転置後、このアンカー範囲には回転後のデータが保持されます。最初の行は (空、**Europe**、**Asia**、**North America**) となり、最初の列は (空、**Qtr 1**、**Qtr 2**、**Qtr 3**、**Qtr 4**) となります。元の売上の各列が、転置された範囲では行になります。

```csharp
using System;
using System.IO;
using Aspose.Cells;
string srcFile = "source.xlsx";
string outputFile = "transposed.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
var source = cells.CreateRange("A1:D5");
source.Transpose();
workbook.Save(outputFile);
```

## **アプローチ 2 — 動的配列数式を使用した転置 (Excel 365 / 2021)**
出力ワークブックに `=TRANSPOSE(A1:D5)` 数式をライブ数式として保持し、ソースデータが変更された場合に結果が自動的に更新されるようにしたい場合は、ターゲット Excel ファイルが動的配列とスピル演算子がサポートされている **Excel 365 / Excel 2021 以降**で開かれる場合に、このアプローチを使用します。

### **使用される API**
`Cell.SetDynamicArrayFormula(string formula, FormulaParseOptions options, bool calculateValue)` は `Aspose.Cells.Cell` のメソッドで、セルの数式を **動的配列数式** として設定します。Excel は数式を一度評価し、結果を周囲のセルに自動的にスピルします。3 番目のパラメータを `true` に設定すると、書き込み時に結果の値も計算するように Aspose.Cells に指示します。

### **手順**
1. `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` を使用して、ソースワークブックを読み込みます。
2. 最初のワークシートを取得し、その `Cells` コレクションにアクセスします。
3. `cells["A6"].SetDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true)` を呼び出して、ソース範囲のすぐ下にあるセル **A6** に動的配列数式を配置します。
4. `new FormulaParseOptions()` 引数はデフォルトの `FormulaParseOptions` 設定を使用し、3 番目の引数 `true` は Aspose.Cells に対して、数式を動的配列として扱い、スピルされた値を計算してワークブックに書き込むよう指示します。
5. `workbook.Save(outputFile)` でワークブックを保存します。
セル **A6** には数式 `=TRANSPOSE(A1:D5)` が保持され、Excel は結果を自動的に領域 **A6:E9**（転置されたデータと等しい 4 行 5 列のブロック）にスピルします。

{{% alert color="primary" %}}
このアプローチは **Excel 365 / 2021 以降でのみ**動作します。古い Excel バージョンでは動的配列数式が正しくスピルされません。
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
string srcFile = "source.xlsx";
string outFile = "output_transpose_dynamic.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
cells["A6"].SetDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true);
workbook.Save(outFile, SaveFormat.Xlsx);
```

## **アプローチ 3 — 従来の配列数式（CSE）を使用した転置**
ワークブックに `TRANSPOSE` 数式を保持したいが、ターゲット Excel ファイルが動的配列のスピルがサポートされていない **古い Excel バージョン (2021 年以前、2019、2016、2013 など)** で開かれる可能性がある場合は、このアプローチを使用します。従来の CSE (Ctrl+Shift+Enter) 配列数式は、すべての Excel バージョンで評価可能なレガシー互換の代替手段です。

### **使用される API**
`Cell.SetArrayFormula(string arrayFormula, int nRows, int nColumns)` は `Aspose.Cells.Cell` のメソッドで、**従来の配列 (CSE) 数式** をアンカーセルに割り当て、結果として得られる配列のサイズを宣言します。Aspose.Cells は複数セル配列数式マーカーを書き込むため、Excel は宣言された範囲を埋める単一の配列式として数式を評価します。

### **手順**
1. 前述のアプローチと同様に、ソースワークブックを読み込みます。
2. 最初のワークシートを取得し、その `Cells` コレクションにアクセスします。
3. `cells["A6"].SetArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)` を呼び出します。2 番目の引数 `4` は宛先配列の行数、3 番目の引数 `5` は列数です。
4. `workbook.Save(outputFile)` でワークブックを保存します。
セル **A6** は配列数式のアンカーであり、評価された配列は A6 から始まる 4 行 5 列にまたがり、A1:D5 ソースの転置後のサイズと一致します。Excel は結果の範囲にわたって単一の配列数式マーカーを書き込むため、古い Excel バージョンでも正しく評価されます。

{{% alert color="primary" %}}
CSE 配列数式は `TRANSPOSE` 式を評価するための従来の Excel の方法であり、このアプローチはすべての Excel バージョンで普遍的に互換性があります。
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
// xlsx LoadOptions を使用してソース ワークブックを読み込む
string srcFile = "source.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
// 最初のワークシートとその Cells コレクションにアクセスする
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
// セル A6 にクラシック CSE 配列数式を設定する。
// 数式 =TRANSPOSE(A1:D5) は、5 行 x 4 列のソース範囲を回転します
// 4 行 x 5 列の配列に変換します。2 番目の引数 (4) は行数
// 3 番目の引数 (5) は結果として得られる配列の列数です。
// Aspose.Cells は CSE 配列数式マーカーを書き込むため、Excel はそれを
// 単一の複数セル配列数式として評価し、古い Excel バージョンと互換性があります
// (2019、2016、2013 など)、動的配列のスピルをサポートしないバージョン。
cells["A6"].SetArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// 配列数式マーカーが保持されるようにワークブックを保存する
workbook.Save("output.xlsx");
```

## **比較 — それぞれのアプローチをいつ使用するか**
| アプローチ | API / メソッド | Excel バージョン | ソース数式の保持 | 出力範囲 |
|----------|--------------|---------------|--------------------------|--------------|
| アプローチ 1 — インプレース転置 | `Range.Transpose()` | すべての Excel バージョン | いいえ（値のみ） | 初期アンカー範囲、5×4 |
| アプローチ 2 — 動的配列数式 | `Cell.SetDynamicArrayFormula` | Excel 365 / 2021+ | はい（動的にスピル） | アンカーからスピル |
| アプローチ 3 — 従来の配列数式（CSE） | `Cell.SetArrayFormula` | すべての Excel バージョン | はい（複数セル配列数式） | 明示的なサイズ、4×5 |
迅速なバージョンを横断した変換が必要で、転置された値のみをファイルに書き込む場合は、**アプローチ 1** を使用してください。最新の Excel が保証されており、ソースが変更された場合に数式をライブ状態に保ち、更新したい場合は、**アプローチ 2** を使用してください。動的配列をサポートしない古いリリースを含むすべての Excel バージョンで、保持された数式による最も幅広い互換性が必要な場合は、**アプローチ 3** を使用してください。

{{< app/cells/assistant language="csharp" >}}