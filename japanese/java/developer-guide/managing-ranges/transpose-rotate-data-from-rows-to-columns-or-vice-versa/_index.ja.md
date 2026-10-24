---
title: 範囲の転置
linktitle: 範囲の転置
description: Aspose.Cells for Java を使用して、Excel ファイル内のデータを行から列へ、またはその逆方向へ転置（回転）する方法を、3 つの異なるアプローチで説明します。
keywords: Aspose.Cells, Java ライブラリ, スプレッドシート, 範囲の転置, データの回転, TRANSPOSE 関数, 動的配列数式, 配列数式, Excel TRANSPOSE, 行から列
type: docs
weight: 80
url: /ja/java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Java は、行を列に、列を行に変換するtranspose（回転）機能を 3 つの異なる方法でサポートします。最初のアプローチではインプレースで動作する `Range.transpose()` メソッドを使用し、すべての Excel バージョンで動作します。2 番目のアプローチでは `Cell.setDynamicArrayFormula()` を使用して、Excel 365 または Excel 2021 で自動的にスピルする最新の動的配列数式 `=TRANSPOSE(...)` を書き込みます。3 番目のアプローチでは `Cell.setArrayFormula()` を使用して、Excel の旧バージョンと互換性のあるクラシックな Ctrl+Shift+Enter (CSE) 配列数式を書き込みます。この.neo에서는、各アプローチについて手順と完全なコード例を説明します。
{{% /alert %}}

## **はじめに**
範囲を転置するとは、行であったものが列になり、列であったものが行になるようにデータを回転することを意味し、事実上、主対角線に関してデータを反転することです。Microsoft Excel では、ワークシート関数 `TRANSPOSE` がこの操作を実行します。この機能に関する説明は、[https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) に記載されています。このtransposeはプログラムによってセル範囲に適用でき、多くのビジネスやレポート作成のAbbreviationsでqz有用です。
- 通常は四半期を横方向、地域を縦方向に配置する四半期別・年次の売上レポートを、その逆に配置する場合に使用できます。
- ダッシュボードやグラフで軸の方向を入れ替え、時系列データを横方向ではなく縦方向に並べる場合に使用できます。
- 外部システムからインポートしたデータを、後続の分析やレポートテンプレートが期待するレイアウトに合わせて整形する場合に使用できます。
以下の例を具体的に示すため、すべての例では小さな地域別・四半期別売上テーブルを使用します。サンプルワークブックでは、この表は範囲 **A1:D5** に配置され、左上隅の **A1** は空欄、**B1:D1** には地域ヘッダー、**A2:A5** には四半期ヘッダーが入力されています。
| 地域              | ヨーロッパ | アジア    | 北米        |
|------------------|-----------|-----------|-------------|
| 第1四半期         | 21704714  | 8774099   | 12094215    |
| 第2四半期         | 17987034  | 12214447  | 10873099    |
| 第3四半期         | 19485029  | 14356879  | 15689543    |
| 第4四半期         | 22567894  | 15763492  | 17456723    |
次に、Aspose.Cells for Java を使用してこのデータを転置する 3 つの異なる方法を説明します。それぞれの方法は、異なる Excel バージョンおよびユースケースに適しています。

## **アプローチ 1 — 範囲をインプレースで転置する (Range.transpose)**
`TRANSPOSE` ワークシート関数を使用せずにデータを転置する場合は、このアプローチを使用してください。この方法は **Excel のすべてのバージョン** で動作し、動的配列に依存しないため、バージョン間の互換性を確保できる最も安全な選択肢です。最終的な転置結果のみが必要で、ワークブックに元の `TRANSPOSE` 数式を保持する必要がない場合に最適です。

### **使用する API**
`Range.transpose()` は `com.aspose.cells.Range` クラスのインスタンスメソッドです。このメソッドは、行と列を交換することで範囲をその場で転置します。元に行であったものは列になり、元々列であったものは行になります。数式を書き込むことなく、範囲内のセルを直接変更します。

### **手順**
1. `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` を呼び出し、`LoadOptions` で `.xlsx` 形式を指定してソースワークブックを開きます。
2. `workbook.getWorksheets().get(0)` を使用して、ワークブックから最初のワークシートを取得します。
3. `worksheet.getCells()` を使用して、ワークシートのセルコレクションにアクセスします。
4. `cells.createRange("A1:D5")` を呼び出して、**A1:D5** をカバーするソース範囲を作成します。
5. `source.transpose()` を呼び出して、範囲をその場で転置し、行と列を交換します。
6. `workbook.save(outputFile)` を使用してワークブックを保存します。
転置後、初期位置にある範囲には転置されたデータが格納されます。最初の行は（空欄、**ヨーロッパ**、**アジア**、**北米**）となり、最初の列は（空欄、**第1四半期**、**第2四半期**、**第3四半期**、**第4四半期**）となります。元の売上データの各列が、転置後の範囲では行になります。

```java
import com.aspose.cells.*;
String srcFile = "source.xlsx";
String outputFile = "transposed.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
Range source = cells.createRange("A1:D5");
source.transpose();
workbook.save(outputFile);
```

## **アプローチ 2 — 動的配列数式で転置する (Excel 365 / 2021)**
`=TRANSPOSE(A1:D5)` 数式を出力ワークブックに有効な数式として保持し、ソースデータが変更された場合に結果が自動的に更新されるようにする場合は、このアプローチを使用してください。対象の Excel ファイルは、動的配列とスピル演算子がサポートされている **Excel 365 / Excel 2021 以降** で開かれることが前提です。

### **使用する API**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` は `com.aspose.cells.Cell` のメソッドで、セルの数式を **動的配列数式** として設定します。Excel は数式を一度評価し、結果を周囲のセルに自動的にスピルします。3 番目のパラメーターを `true` に設定すると、書き込み時にもAspose.Cells で結果の値が計算されます。

### **手順**
1. `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` を使用してソースワークブックを読み込みます。
2. 最初のワークシートを取得し、その `Cells` コレクションにアクセスします。
3. `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)` を呼び出して、ソース範囲のすぐ下にあるセル **A6** に動的配列数式を配置します。
4. `null` を渡すとデフォルトの `FormulaParseOptions` が使用されます。3 番目の引数 `true` は、数式を動的配列として扱い、スピルされる値がワークブックに書き込まれるように評価するよう Aspose.Cells に指示します。
5. `workbook.save(outputFile)` を使用してワークブックを保存します。
セル **A6** には数式 `=TRANSPOSE(A1:D5)` が格納され、Excel は結果を領域 **A6:D10** に自動的にスピルします。この領域は、転置されたデータと等しい 5 行 4 列のブロックです。

{{% alert color="primary" %}}
このアプローチは **Excel 365 / Excel 2021 以降でのみ** 動作します。Excel の旧バージョンでは、動的配列数式を正しくスピルできません。
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

## **アプローチ 3 — クラシック配列数式で転置する (CSE)**
`TRANSPOSE` 数式をワークブックに保持する必要がある一方、対象の Excel ファイルが動的配列のスピルをサポートしていない **Excel の旧バージョン (2021 より前、2019、2016、2013 など)** で開かれる可能性がある場合は、このアプローチを使用してください。クラシックな CSE (Ctrl+Shift+Enter) 配列数式は、すべての Excel バージョンで評価できる、互換性の高い代替手段です。

### **使用する API**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` は `com.aspose.cells.Cell` のメソッドで、**クラシックな配列 (CSE) 数式** をアンカーセルに割り当て、結果として得られる配列の次元を宣言します。Aspose.Cells は複数セルにまたがる配列数式マーカーを書き込むため、Excel は宣言された範囲を埋める単一の配列式として数式を評価します。

### **手順**
1. 前のアプローチで説明したように、ソースワークブックを読み込みます。
2. 最初のワークシートを取得し、その `Cells` コレクションにアクセスします。
3. `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)` を呼び出します。2 番目の引数 `4` は宛先配列の行数、3 番目の引数 `5` は列数です。
4. `workbook.save(outputFile)` を使用してワークブックを保存します。
セル **A6** は配列数式のアンカーであり、評価された配列は A6 から始まる 4 行 5 列の領域にまたがります。これは、A1:D5 のソース範囲を転置した次元と一致します。Excel は結果の範囲にわたって単一の配列数式マーカーを書き込むため、Excel の旧バージョンでも正しく評価されます。

{{% alert color="primary" %}}
CSE 配列数式は `TRANSPOSE` 式を評価するためのクラシックな Excel の方法であり、このアプローチは Excel のすべてのバージョンと互換性があります。
{{% /alert %}}

```java
import com.aspose.cells.*;
// xlsx LoadOptions を使用してソースワークブックを読み込む
String srcFile = "source.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
// 最初のワークシートとその Cells コレクションにアクセスする
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
// セル A6 に従来の CSE 配列数式を設定する
// 数式 =TRANSPOSE(A1:D5) は、5 行 x 4 列のソース範囲を
// 4 行 x 5 列の配列に回転させます。2 番目の引数 (4) は結果配列の行数
// 3 番目の引数 (5) は結果配列の列数です。
// Aspose.Cells は CSE 配列数式マーカーを書き込み、Excel がこれを
// 単一の複数セルにまたがる配列数式として評価するようにします。
// 動的配列の spilling をサポートしていない旧バージョンの Excel
// (2019、2016、2013 など) との互換性を保ちます。
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// 配列数式マーカーが永続化されるようにワークブックを保存する
workbook.save("output.xlsx");
```

## **比較 — 各アプローチの使い分け**
| アプローチ | API / メソッド | Excel のバージョン | 元の数式を保持しますか？ | 出力範囲 |
|-----------|----------------|--------------------|--------------------------|----------|
| アプローチ 1 — インプレース転置 | `Range.transpose()` | すべての Excel バージョン | いいえ（値のみ） | 初期位置を基準とした範囲、5×4 |
| アプローチ 2 — 動的配列数式 | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | はい（動的にスピル） | アンカーセルから動的にスピル |
| アプローチ 3 — クラシック配列数式 (CSE) | `Cell.setArrayFormula` | すべての Excel バージョン | はい（複数セル配列数式） | 明示的なサイズ、4×5 |
迅速なバージョン間変換が必要で、転置された値のみをファイルに書き込む場合は、**アプローチ 1** を使用してください。最新の Excel が使用され、ソースデータが変更された場合に数式が有効なまま更新されるようにする場合は、**アプローチ 2** を使用してください。動的配列をサポートしない旧リリースを含むすべての Excel バージョンとの互換性が必要で、数式を保持したい場合は、**アプローチ 3** を使用してください。

## **関連記事**
- [SmartMarker 単一セル配列レンダリング | Aspose.Cells for Java](/cells/ja/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [セルへの画像の挿入](/cells/ja/java/inserting-an-image-into-a-cell/)
- [Excel ファイルを複数のファイルに分割する](/cells/ja/java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="java" >}}