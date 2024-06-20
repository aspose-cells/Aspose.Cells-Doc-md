---
title: 数式の計算
type: docs
weight: 110
url: /ja/java/calculate-formulas/
---

## **数式の追加と結果の計算**

Aspose.Cellsには埋め込み数式計算エンジンがあります。デザイナーテンプレートからインポートされた数式を再計算するだけでなく、実行時に追加された数式の結果を計算することもサポートしています。

Aspose.Cellsは、Microsoft Excelの一部である多くの関数や式をサポートしています（[計算エンジンでサポートされている関数のリスト](/cells/ja/java/supported-formula-functions/)）。これらの関数はAPIまたはデザイナースプレッドシートを通じて使用できます。Aspose.Cellsは、数学、文字列、ブール、日付/時刻、統計、データベース、検索、参照関数などの大規模なセットの式をサポートしています。

[**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)プロパティまたは[**SetFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setFormula(java.lang.String,%20com.aspose.cells.FormulaParseOptions,%20java.lang.Object))メソッドの[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)クラスを使用して、セルに数式を追加します。数式を適用するときには常に等号（=）で始め、Microsoft Excelで数式を作成するときと同様に関数パラメータを区切るためにコンマ（,）を使用します。

数式の結果を計算するには、ユーザーはExcelファイルに埋め込まれたすべての数式を処理する[**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions))メソッドを呼び出すか、シートに埋め込まれたすべての数式を処理する[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)メソッドを呼び出すか、またはセルの数式を処理する[**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(com.aspose.cells.CalculationOptions,%20boolean))メソッドを呼び出すかを選択できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulas-CalculatingFormulas.java" >}}

### **重要なこと**

{{% alert color="primary" %}}

[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)クラスの**Formula**プロパティと**SetFormula(...)**メソッドは、**Calculate**クラスのメソッドと異なる動作をします。**Formula**プロパティと**SetFormula(...)**メソッドは単にセルに数式を追加するだけであり、実行時に結果を計算しません。数式の結果を取得するには、**Calculate**メソッドを呼び出してください。

{{% /alert %}}

## **数式の直接計算**

Aspose.Cellsには、埋め込みファイルからインポートされた数式を計算するだけでなく、直接数式の結果を計算する機能があります。

時々、ワークシートに追加することなく、Microsoft Excelの数式に基づいてワークシート内にすでに存在するセルの値の結果を見つける必要があります。

Aspose.Cellsの数式計算エンジンAPIを使用して、ワークシートに追加せずにそのような数式の結果を[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)から[**calculate**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(java.lang.String,%20com.aspose.cells.CalculationOptions))まで計算できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DirectCalculationFormula-DirectCalculationFormula.java" >}}

上記のコードは次の出力を生成します：
{{< highlight java >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **繰り返し数式を計算する**

ブック内に多くの数式があり、ユーザーがそれらを修正する部分がわずかで繰り返し計算する必要がある場合は、パフォーマンスのために数式計算チェーンを有効にすると役立ちます：[**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#EnableCalculationChain)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulasOnce-CalculatingFormulasOnce.java" >}}

### **重要なこと**

{{% alert color="primary" %}}

デフォルトでは、計算チェーンは無効になっています。チェーンを作成するには追加の時間が必要なため、数式を計算する最初の回（[**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions))）は、チェーンを作成せずに数式を計算する場合と比較して、CPU処理時間とメモリをより多く消費する可能性があります。ユーザーが数式を繰り返し計算する必要がない場合は、デフォルトの動作（計算チェーンを作成せずに数式を直接計算する）がより良い方法となります。

{{% /alert %}}

## **高度なトピック**
- [Microsoft Excelフォーミュラ計算エンジンのAspose.Cells](/cells/ja/java/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cellsの数式計算エンジン](/cells/ja/java/aspose-cells-formula-calculation-engine/)
- [Aspose.Cellsを使用してIFNA関数を計算する](/cells/ja/java/calculating-ifna-function-using-aspose-cells/)
- [データテーブルの配列式の計算](/cells/ja/java/calculation-of-array-formula-of-data-tables/)
- [Excel 2016のMINIFSおよびMAXIFS関数の計算](/cells/ja/java/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Cell.Calculateメソッドの計算時間を短縮する](/cells/ja/java/decrease-the-calculation-time-of-cell-calculate-method/)
- [循環参照の検出](/cells/ja/java/detecting-circular-reference/)
- [ワークシートに書き込まずにカスタム機能を直接計算する](/cells/ja/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Aspose.Cellsのデフォルトの計算エンジンを拡張するためにカスタム計算エンジンを実装する](/cells/ja/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [ワークブックの数式計算を中断またはキャンセルする](/cells/ja/java/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [AbstarctCalculationEngineを使用して値の範囲を返す](/cells/ja/java/returning-a-range-of-values-using-abstractcalculationengine/)
- [ICustomFunctionを使用して値の範囲を返す](/cells/ja/java/returning-a-range-of-values-using-icustomfunction/)
- [ICustomFunction機能の使用](/cells/ja/java/using-icustomfunction-feature/)
