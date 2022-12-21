---
title: 数式を計算する
type: docs
weight: 125
url: /ja/net/calculate-formulas/
---
## **式の追加と結果の計算**

Aspose.Cells には数式計算エンジンが組み込まれています。デザイナー テンプレートからインポートされた数式を再計算できるだけでなく、実行時に追加された数式の結果を計算することもサポートします。

 Aspose.Cells は、Microsoft Excel (Read[計算エンジンがサポートする関数のリスト](/cells/ja/net/supported-formula-functions/)）。これらの機能は、API またはデザイナー スプレッドシートを介して使用できます。 Aspose.Cells は、数学、文字列、ブール、日付/時刻、統計、データベース、ルックアップ、および参照式の膨大なセットをサポートしています。

使用[**方式**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)プロパティまたは[**式の設定(...)**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2)のメソッド[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)セルに数式を追加するクラス。数式を適用するときは、Microsoft Excel で数式を作成するときと同じように、文字列を常に等号 (=) で開始し、カンマ (,) を使用して関数パラメーターを区切ります。

式の結果を計算するには、ユーザーは[**計算式**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)の方法[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Excel ファイルに埋め込まれたすべての数式を処理するクラス。または、ユーザーは[**計算式**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula)の方法[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)シートに埋め込まれたすべての数式を処理するクラス。または、ユーザーは[**計算する**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/calculate)の方法[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)つの Cell の数式を処理するクラス:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

### **知っておくべき重要事項**

{{% alert color="primary" %}}

の**方式**プロパティと**式の設定(...)**のメソッド[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラスは、**計算する**のメソッド[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook), [**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)と[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラス。の**方式**プロパティと**式の設定(...)**メソッドは数式をセルに追加するだけで、実行時に結果を計算しません。数式の結果を取得するには、 を呼び出してください。**計算する**メソッド。

{{% /alert %}}

## **数式の直接計算**

Aspose.Cells には数式計算エンジンが組み込まれています。 Aspose.Cells は、デザイナー ファイルからインポートされた数式を計算するだけでなく、数式の結果を直接計算できます。

数式の結果をワークシートに追加せずに直接計算する必要がある場合があります。数式で使用されているセルの値は既にワークシートに存在しており、ワークシートに数式を追加せずに、Microsoft Excel 数式に基づいてこれらの値の結果を見つけるだけで済みます。

 Aspose.Cells の数式計算エンジン API を使用できます。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)に[**計算する**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)ワークシートに追加せずに、そのような数式の結果:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

上記のコードは、次の出力を生成します。
{{< highlight "net" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **数式を繰り返し計算する**

ワークブックに多くの数式があり、ユーザーが数式のごく一部のみを変更して繰り返し計算する必要がある場合、数式計算チェーンを有効にするとパフォーマンスが向上する場合があります。[**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

### **知っておくべき重要事項**

{{% alert color="primary" %}}

デフォルトでは、計算チェーンは無効になっています。チェーンの作成にも余分な時間がかかるため、最初の数式の計算([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)) チェーンなしの計算式と比較すると、より多くの CPU 処理時間とメモリを消費する可能性があります。ユーザーが数式を繰り返し計算する必要がない場合は、既定の動作 (計算チェーンを作成せずに数式を直接計算する) を使用することをお勧めします。

{{% /alert %}}


## **先行トピック**
- [Cells を Microsoft に追加 Excel 数式ウォッチ ウィンドウ](/cells/ja/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cells を使用した IFNA 関数の計算](/cells/ja/net/calculating-ifna-function-using-aspose-cells/)
- [データテーブルの配列式の計算](/cells/ja/net/calculation-of-array-formula-of-data-tables/)
- [Excel 2016 MINIFS および MAXIFS 関数の計算](/cells/ja/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Cell.Calculateメソッドの計算時間を短縮](/cells/ja/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [循環参照の検出](/cells/ja/net/detecting-circular-reference/)
- [カスタム関数をワークシートに書かずに直接計算](/cells/ja/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [カスタム計算エンジンを実装して、Aspose.Cells のデフォルト計算エンジンを拡張します](/cells/ja/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [ワークブックの数式計算を中断またはキャンセルする](/cells/ja/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [AbstractCalculationEngine を使用して値の範囲を返す](/cells/ja/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [ICustomFunction を使用して値の範囲を返す](/cells/ja/net/returning-a-range-of-values-using-icustomfunction/)
- [ワークブックの数式計算モードの設定](/cells/ja/net/setting-formula-calculation-mode-of-workbook/)
- [Aspose.Cells で FormulaText 関数を使用する](/cells/ja/net/using-formulatext-function-in-aspose-cells/)
- [ICustomFunction 機能の使用](/cells/ja/net/using-icustomfunction-feature/)
