---
title: 数式を計算する方法
type: docs
weight: 30
url: /ja/cpp/ways-to-calculate-formulas/
---
## **序章**
Aspose.Cells には数式計算エンジンが組み込まれています。デザイナー テンプレートからインポートされた数式を再計算できるだけでなく、実行時に追加された数式の結果の計算もサポートします。
## **式の追加と結果の計算**
Aspose.Cells は、Microsoft Excel の一部である数式または関数のほとんどをサポートしています。 API またはデザイナー スプレッドシートを使用して使用できます。 Aspose.Cells は、数学、文字列、ブール、日付/時刻、統計、検索、および参照式の膨大なセットをサポートしています。

セルに数式を追加するには、Cell.Formula メソッドを使用します。数式をセルに適用するときは、Microsoft Excel で数式を作成するときと同じように、文字列を常に等号 (=) で始めます。関数のパラメーターを区切るには、コンマ (,) を使用します。

数式の結果を計算するには、Excel ファイルに埋め込まれたすべての数式を処理する Workbook.CalculateFormula() メソッドを呼び出します。数式を追加してその結果を計算する次のサンプル コードを参照してください。を確認してください[出力エクセルファイル](38109185.xlsx)このコードで生成されます。

**サンプルコード**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-AddingFormulasAndCalculatingResults.cpp" >}}
## **数式の直接計算**
数式の結果をワークシートに追加せずに直接計算する必要がある場合があります。数式で使用されているセルの値は既にワークシートに存在しており、ワークシートに数式を追加せずに、Microsoft Excel 数式に基づいてこれらの値の結果を見つけるだけで済みます。

Worksheet.CalculateFormula(String formula) メソッドを使用して、ワークシートに追加せずにそのような数式の結果を計算できます。

以下のコードは、次の出力を生成します。

{{< highlight "java" >}}

 Value of A1: 20

Value of A2: 30

Result of Sum(A1:A2): 50

{{< /highlight >}}

**サンプルコード**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-DirectCalculationOfFormula.cpp" >}}
## **数式を一度だけ計算する**
ブック テンプレート内の数式の値を計算するために Workbook.CalculateFormula() が呼び出されると、Aspose.Cells によって計算チェーンが作成されます。数式が 2 回目または 3 回目に計算されるときのパフォーマンスが向上します。

ただし、テンプレートに多数の式が含まれている場合、最初に式が計算されるときに、多くの CPU 処理時間とメモリが消費される可能性があります。

Aspose.Cells を使用すると、数式を 1 回だけ計算する場合に役立つ計算チェーンの作成をオフにすることができます。

 Workbook.GetISettings().SetCreateCalcChain() を false パラメータで呼び出してください。を使用できます。[提供されたエクセルファイル](38109186.xlsx)このコードをテストします。

**サンプルコード**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-CalculatingFormulasOnceOnly.cpp" >}}
