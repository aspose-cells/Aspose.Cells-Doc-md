---
title: 数式の計算方法
type: docs
weight: 30
url: /ja/cpp/ways-to-calculate-formulas/
---
##  **導入**
Aspose.Cells には数式計算エンジンが組み込まれています。デザイナー テンプレートからインポートされた数式を再計算できるだけでなく、実行時に追加された数式の結果の計算もサポートします。
##  **数式の追加と結果の計算**
Aspose.Cells は、Microsoft Excel の一部であるほとんどの数式または関数をサポートしています。 API を通じて、またはデザイナー スプレッドシートを使用して使用できます。 Aspose.Cells は、数学、文字列、ブール値、日付/時刻、統計、検索および参照の数式の膨大なセットをサポートしています。

セルに数式を追加するには、Cell.SetFormula メソッドを使用します。セルに数式を適用するときは、Microsoft Excel で数式を作成する場合と同様に、必ず文字列を等号 (=) で始めてください。カンマ (,) を使用して関数パラメータを区切ります。

数式の結果を計算するには、Excel ファイルに埋め込まれているすべての数式を処理する Workbook.CalculateFormula() メソッドを呼び出します。数式を追加して結果を計算する次のサンプル コードを参照してください。をご確認ください。[Excelファイルを出力する](38109185.xlsx)このコードで生成されました。

**サンプルコード**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-AddingFormulasAndCalculatingResults-new.cpp" >}}
<!---## **Direct Calculation of Formula**
Sometimes, you need to calculate formula results directly without adding them into a worksheet. The values of the cells used in the formula already exist in a worksheet and all you need is to find the result of those values based on some Microsoft Excel formula without adding the formula in a worksheet.

You can use Worksheet.CalculateFormula(String formula) method to calculate the results of such formulas without adding them to worksheet.

The code below produces the following output.

{{< highlight java >}}

 Value of A1: 20

Value of A2: 30

Result of Sum(A1:A2): 50

{{< /highlight >}}

**Sample Code**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-DirectCalculationOfFormula.cpp" >}}   --->
##  **数式を一度だけ計算する**
Workbook.CalculateFormula() を呼び出してワークブック テンプレート内の数式の値を計算すると、Aspose.Cells によって計算チェーンが作成されます。数式が 2 回目または 3 回目に計算されるときのパフォーマンスが向上します。

ただし、テンプレートに多数の数式が含まれている場合、数式の初回計算時に大量の CPU 処理時間とメモリが消費される可能性があります。

Aspose.Cells を使用すると、計算チェーンの作成をオフにできます。これは、数式を 1 回だけ計算したい場合に便利です。

 false パラメータを指定して Workbook.GetISettings().SetCreateCalcChain() を呼び出してください。使用できます[提供されたエクセルファイル](38109186.xlsx)このコードをテストします。

**サンプルコード**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-CalculatingFormulasOnceOnly-new.cpp" >}}
