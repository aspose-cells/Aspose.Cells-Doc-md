---
title: 数式を計算する
description: この記事では、Aspose.Cells Excel で数式を計算するための Aspose.Cells ライブラリを使用する方法を紹介します。既存の Excel ファイルをロードするか、新しい Excel ファイルを作成することで、Aspose.Cells が提供するメソッドを使用して数式を計算し、結果を取得できます。最後に、変更した Excel ファイルをディスクに保存します。
keywords: Aspose.Cells, Excel, formulas, calculations, Direct Calculation of Formula, Calculate Formulas repeatedly, add formulas.
type: docs
weight: 125
url: /ja/net/calculate-formulas/
---
##  **数式の追加と結果の計算**

Aspose.Cells には数式計算エンジンが組み込まれています。デザイナー テンプレートからインポートされた数式を再計算できるだけでなく、実行時に追加された数式の結果の計算もサポートします。

 Aspose.Cells は、Microsoft Excel(読み取り) の一部である数式または関数のほとんどをサポートしています。[計算エンジンがサポートする関数のリスト](/cells/ja/net/supported-formula-functions/)）。これらの関数は、API またはデザイナー スプレッドシートを通じて使用できます。 Aspose.Cells は、数学、文字列、ブール値、日付/時刻、統計、データベース、ルックアップ、および参照の数式の膨大なセットをサポートしています。

使用[**式**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)財産または[**SetFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2)のメソッド[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)セルに数式を追加するクラス。数式を適用するときは、Microsoft Excel で数式を作成する場合と同様に、必ず文字列を等号 (=) で開始し、カンマ (,) を使用して関数パラメータを区切ります。

数式の結果を計算するには、ユーザーは[**計算式**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)の方法[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Excel ファイルに埋め込まれたすべての数式を処理するクラス。または、ユーザーは[**計算式**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula)の方法[**ワーシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)シートに埋め込まれたすべての数式を処理するクラス。または、ユーザーは、[**計算する**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/calculate)の方法[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)つの Cell の数式を処理するクラス:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

###  **数式について知っておくべき重要なこと**

{{% alert color="primary" %}}

の**式**財産と**SetFormula(...)**のメソッド[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラスの仕事は他のものとは異なります**計算する**のメソッド[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook), [**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)そして[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。の**式**財産と**SetFormula(...)**メソッドはセルに数式を追加するだけで、実行時に結果を計算しません。数式の結果を取得するには、電話してください。**計算する**メソッド。

{{% /alert %}}

##  **式の直接計算**

Aspose.Cells には数式計算エンジンが組み込まれています。デザイナー ファイルからインポートされた数式を計算するだけでなく、Aspose.Cells は数式の結果を直接計算することもできます。

場合によっては、数式の結果をワークシートに追加せずに直接計算する必要があることがあります。数式で使用されるセルの値はワークシート内にすでに存在しているため、ワークシートに数式を追加せずに、Microsoft Excel 数式に基づいてそれらの値の結果を検索するだけで済みます。

 Aspose.Cells' の数式計算エンジン API を次の目的で使用できます。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)に[**計算する**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)このような数式の結果をワークシートに追加せずに表示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

上記のコードは次の出力を生成します。
{{< highlight "net" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

##  **数式を繰り返し計算する方法**

ワークブックに多数の数式があり、ユーザーがその一部のみを変更して繰り返し計算する必要がある場合、数式計算チェーンを有効にするとパフォーマンスが向上する可能性があります。[**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

###  **知っておくべき重要なこと**

{{% alert color="primary" %}}

デフォルトでは、計算チェーンは無効になっています。チェーンの作成にも時間がかかるので、最初の計算式([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)) チェーンを使用しない計算式と比較すると、より多くの CPU 処理時間とメモリを消費する可能性があります。ユーザーが数式を繰り返し計算する必要がない場合は、デフォルトの動作 (計算チェーンを作成せずに数式を直接計算する) の方が良い方法です。

{{% /alert %}}


##  **アドバンストトピック**
- [Cells を Microsoft Excel 数式ウォッチ ウィンドウに追加](/cells/ja/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cellsを使用したIFNA関数の計算](/cells/ja/net/calculating-ifna-function-using-aspose-cells/)
- [データテーブルの配列式の計算](/cells/ja/net/calculation-of-array-formula-of-data-tables/)
- [Excel 2016 MINIFS および MAXIFS 関数の計算](/cells/ja/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Cellの計算時間を短縮します。計算メソッド](/cells/ja/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [循環参照の検出](/cells/ja/net/detecting-circular-reference/)
- [カスタム関数をワークシートに記述せずに直接計算](/cells/ja/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [カスタム計算エンジンを実装して、Aspose.Cells のデフォルト計算エンジンを拡張します。](/cells/ja/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [ワークブックの数式計算を中断またはキャンセルする](/cells/ja/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [AbstractCalculationEngine を使用して値の範囲を返す](/cells/ja/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [ICustomFunction を使用して値の範囲を返す](/cells/ja/net/returning-a-range-of-values-using-icustomfunction/)
- [ワークブックの数式計算モードの設定](/cells/ja/net/setting-formula-calculation-mode-of-workbook/)
- [Aspose.Cells での FormulaText 関数の使用](/cells/ja/net/using-formulatext-function-in-aspose-cells/)
- [ICustomFunction 機能の使用](/cells/ja/net/using-icustomfunction-feature/)
