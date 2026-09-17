---
title: 範囲の転置
linktitle: 範囲の転置
description: Aspose.Cells for C++ を使用して Excel ファイル内のデータを行から列へ、または列から行へ転置（回転）する方法を、3 つの異なるアプローチで説明します。
keywords: Aspose.Cells, C++ ライブラリ, スプレッドシート, 範囲の転置, データ回転, TRANSPOSE 関数, 動的配列数式, 配列数式, Excel TRANSPOSE, 行から列へ
type: docs
weight: 80
url: /ja/cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for C++ は、行を列に、列を行に変換することでデータ転置（回転）を 3 つの方法でサポートします。1 つ目のアプローチはインプレースの `Range.Transpose()` メソッドを使用し、すべての Excel バージョンで動作します。2 つ目は `Cell.SetDynamicArrayFormula()` を使用して、Excel 365 または Excel 2021 で自動的にスピルする最新の動的配列数式 `=TRANSPOSE(...)` を書き込みます。3 つ目のアプローチは `Cell.SetArrayFormula()` を使用して、古い Excel バージョンと互換性のある従来の Ctrl+Shift+Enter（CSE）配列数式を書き込みます。本記事では、各アプローチをステップバイステップの説明と完全なコード例で解説します。
{{% /alert %}}

## **Introduction**
範囲を転置するとは、行であったものを列に、列であったものを行に回転させる、つまり主対角線を軸にデータを反映することを意味します。Microsoft Excel では、ワークシート関数 `TRANSPOSE` がこの操作を実行し、その概念リファレンスは [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) で公開されています。この概念はセル範囲に対してプログラム的に適用でき、多くのビジネスやレポートのシナリオで役立ちます。
- 四半期ごとまたは年間の売上レポートで、通常は四半期がページ全体に、地域がページ下に並ぶ構成を、その逆に再構成する。
- ダッシュボードやグラフで軸の向きを反転させ、時系列データをページ横方向ではなく縦方向に並べる。
- 外部システムからインポートしたデータを、下流の分析やレポートテンプレートで想定されるレイアウトに合わせて再整形する。
記事の以降の説明を具体化するため、すべての例では次の地域別・四半期別の売上表を使用します。サンプルワークブックでは、この表は範囲 **A1:D5** を占め、**A1** は左上隅として空白、**B1:D1** に地域ヘッダー、**A2:A5** に四半期ヘッダーが配置されます。
| Region            | Europe    | Asia      | North America |
|-------------------|-----------|-----------|---------------|
| Qtr 1             | 21704714  | 8774099   | 12094215      |
| Qtr 2             | 17987034  | 12214447  | 10873099      |
| Qtr 3             | 19485029  | 14356879  | 15689543      |
| Qtr 4             | 22567894  | 15763492  | 17456723      |
次に、Aspose.Cells for C++ を使用してこのデータを変換する 3 つの方法を紹介します。それぞれ異なる Excel バージョンとユースケースに適しています。

## **Approach 1 — Transpose Range in Place (Range.Transpose)**
`TRANSPOSE` ワークシート関数を使用せずにデータ転置を行いたい場合は、このアプローチを使用します。**すべての Excel バージョン** で動作し、動的配列に依存しないため、最も安全なバージョン互換オプションです。最終的な転置出力のみが必要で、ワークブックに元の `TRANSPOSE` 数式を残しておく必要がない場合に最適です。

### **API used**
`Range.Transpose()` は `Aspose.Cells.Range` クラスのインスタンスメソッドです。これを呼び出すと、範囲の行と列を入れ替えてインプレースで回転させ、行であったものが列に、列であったものが行になります。このメソッドは数式を書き込まずに直接セルを変更します。

### **Steps**
1. `.xlsx` 形式に設定された `LoadOptions` でソースワークブックを開きます。`Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))` を作成します。
2. `workbook.GetWorksheets().Get(0)` を使用して、ワークブックから最初のワークシートを取得します。
3. `worksheet.GetCells()` を通じて、ワークシートのセルコレクションにアクセスします。
4. `cells.CreateRange(u"A1:D5")` を呼び出して、**A1:D5** をカバーするソース範囲を作成します。
5. `source.Transpose()` を呼び出して、範囲の行と列を入れ替え、インプレースで回転させます。
6. `workbook.Save(outputFile)` でワークブックを保存します。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    U16String srcFile(u"source.xlsx");
    U16String outputFile(u"transposed.xlsx");
    LoadOptions loadOptions(LoadFormat::Xlsx);
    Workbook workbook(srcFile, loadOptions);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    Range source = cells.CreateRange(u"A1:D5");
    source.Transpose();
    workbook.Save(outputFile);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Approach 2 — Transpose with a Dynamic Array Formula (Excel 365 / 2021)**
ソースデータが変更された場合に結果が自動的に更新されるように、ライブの数式として出力ワークブックに `=TRANSPOSE(A1:D5)` 数式を保持したい場合、および対象の Excel ファイルが動的配列とスピル演算子がサポートされている **Excel 365 / Excel 2021 以降** で開かれる場合は、このアプローチを使用します。

### **API used**
`Cell.SetDynamicArrayFormula(const char* formula, FormulaParseOptions options, bool calculateValue)` は `Aspose.Cells.Cell` のメソッドで、セルの数式を **動的配列数式** として設定します。Excel は数式を 1 回評価し、結果を周囲のセルに自動的にスピルします。3 番目のパラメータを `true` に設定すると、Aspose.Cells に書き込み時にも結果の値を計算するように指示します。

### **Steps**
1. `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))` を構築してソースワークブックを読み込みます。
2. `workbook.GetWorksheets().Get(0)` 経由で最初のワークシートを取得し、`worksheet.GetCells()` を通じてその `Cells` コレクションにアクセスします。
3. `cells.Get(u"A6").SetDynamicArrayFormula(u"=TRANSPOSE(A1:D5)", nullptr, true)` を呼び出して、ソース範囲の直下にあるセル **A6** に動的配列数式を配置します。
4. `nullptr` 引数はデフォルトの `FormulaParseOptions` を渡し、3 番目の引数 `true` は Aspose.Cells に対して、数式を動的配列として扱い、スピルした値がワークブックに書き込まれるように評価するように指示します。
5. `workbook.Save(outputFile)` でワークブックを保存します。
セル **A6** は数式 `=TRANSPOSE(A1:D5)` を保持し、Excel は結果を領域 **A6:D10** に自動的にスピルします。これは転置されたデータと等しい 5 行 × 4 列のブロックです。

{{% alert color="primary" %}}
このアプローチは **Excel 365 / 2021 以降でのみ** 機能します。古い Excel バージョンでは動的配列数式を正しくスピルできません。
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    std::string srcFile = "source.xlsx";
    std::string outFile = "output_transpose_dynamic.xlsx";
    LoadOptions loadOptions(LoadFormat::Xlsx);
    Workbook workbook(U16String(srcFile.c_str()), loadOptions);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    Cell cell = cells.Get(u"A6");
    FormulaParseOptions options;
    cell.SetDynamicArrayFormula(U16String("=TRANSPOSE(A1:D5)"), options, true);
    workbook.Save(U16String(outFile.c_str()), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Approach 3 — Transpose with a Classic Array Formula (CSE)**
ワークブックに `TRANSPOSE` 数式を保持したいが、対象の Excel ファイルが動的配列のスピルがサポートされていない **古い Excel バージョン（2021 以前、2019、2016、2013 など）** で開かれる可能性がある場合は、このアプローチを使用します。従来の CSE（Ctrl+Shift+Enter）配列数式は、すべての Excel バージョンが評価できるレガシー互換の代替手段です。

### **API used**
`Cell.SetArrayFormula(const char* arrayFormula, int nRows, int nColumns)` は `Aspose.Cells.Cell` のメソッドで、**従来の配列（CSE）数式** をアンカーセルに割り当て、結果として得られる配列の次元を宣言します。Aspose.Cells は複数セルの配列数式マーカーを書き込むため、Excel は宣言された範囲を埋める単一の配列式として数式を評価します。

### **Steps**
2. `workbook.GetWorksheets().Get(0)` 経由で最初のワークシートを取得し、`worksheet.GetCells()` を通じてその `Cells` コレクションにアクセスします。
3. `cells.Get(u"A6").SetArrayFormula(u"=TRANSPOSE(A1:D5)", 4, 5)` を呼び出します。2 番目の引数 `4` は宛先配列の行数、3 番目の引数 `5` は列数です。
4. `workbook.Save(outputFile)` でワークブックを保存します。
セル **A6** は配列数式のアンカーであり、評価された配列は A6 から始まる 4 行 × 5 列に及び、ソース A1:D5 の転置次元と一致します。Excel は結果の範囲にわたって単一の配列数式マーカーを書き込むため、古い Excel バージョンでも正しく評価されます。

{{% alert color="primary" %}}
CSE 配列数式は `TRANSPOSE` 式を評価するための従来の Excel の方法であり、このアプローチは Excel のすべてのバージョンで普遍的に互換性があります。
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // xlsx の LoadOptions を使用してソースワークブックを読み込む
    std::string srcFile = "source.xlsx";
    Workbook workbook(U16String(srcFile.c_str()), LoadOptions(LoadFormat::Xlsx));
    // 最初のワークシートとその Cells コレクションにアクセスする
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // セル A6 に従来の CSE 配列数式を設定する。
    // 数式 =TRANSPOSE(A1:D5) は 5 行 x 4 列のソース範囲を回転させ、
    // 4 行 x 5 列の配列に変換する。2 番目の引数 (4) は行数、
    // 3 番目の引数 (5) は結果として得られる配列の列数である。
    // Aspose.Cells は CSE 配列数式マーカーを書き込むので、Excel はこれを
    // 単一の複数セル配列数式として評価し、古いバージョンの Excel
    // (2019、2016、2013 など)、動的配列のスピリングをサポートしない環境と互換性がある。
    cells.Get(u"A6").SetArrayFormula(u"=TRANSPOSE(A1:D5)", 4, 5);
    // 配列数式マーカーが保持されるようにワークブックを保存する
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Comparison — When to Use Each Approach**
| アプローチ | API / メソッド | Excel バージョン | 元の数式の保持 | 出力範囲 |
|----------|--------------|---------------|--------------------------|--------------|
| アプローチ 1 — インプレース転置 | `Range.Transpose()` | すべての Excel バージョン | いいえ（値のみ） | 初期アンカー範囲、5×4 |
| アプローチ 2 — 動的配列数式 | `Cell.SetDynamicArrayFormula` | Excel 365 / 2021+ | はい（動的にスピル） | アンカーからスピル |
| アプローチ 3 — 従来の配列数式（CSE） | `Cell.SetArrayFormula` | すべての Excel バージョン | はい（複数セル配列数式） | 明示的なサイズ、4×5 |
迅速でバージョン互換性のある変換が必要で、転置された値のみをファイルに書き込む必要がある場合は、**アプローチ 1** を使用します。最新の Excel が保証されており、ソースが変更された場合に数式がライブのまま更新されるようにしたい場合は、**アプローチ 2** を使用します。動的配列をサポートしない古いリリースを含むすべての Excel バージョンで、数式を保持したまま最大限の互換性が必要な場合は、**アプローチ 3** を使用します。

## **Related Articles**
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for C++](/cells/ja/cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [セルへの画像の挿入](/cells/ja/cpp/inserting-an-image-into-a-cell/)
- [Excel ファイルの複数ファイルへの分割](/cells/ja/cpp/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="" >}}