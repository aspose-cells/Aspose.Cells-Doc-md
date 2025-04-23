---
title: 数式の計算
description: この記事では、Aspose.Cellsライブラリを使用してMicrosoft Excelで数式を計算する方法について紹介します。既存のExcelファイルをロードするか、新しいExcelファイルを作成し、Aspose.Cellsで提供されるメソッドを使用して数式を計算して結果を取得することができます。最後に、変更したExcelファイルをディスクに保存します。
keywords: Aspose.Cells、Excel、数式、計算、数式の直接計算、数式の繰り返し計算。
type: docs
weight: 125
url: /ja/net/calculate-formulas/
---

## **数式の追加と結果の計算**

Aspose.Cellsには埋め込み数式計算エンジンがあります。デザイナーテンプレートからインポートされた数式を再計算するだけでなく、実行時に追加された数式の結果を計算することもサポートしています。

Aspose.Cellsは、Microsoft Excelの一部である多くの数式または関数をサポートしています（[計算エンジンがサポートする関数のリスト](/cells/ja/net/supported-formula-functions/)を参照）。これらの関数はAPIまたはデザイナースプレッドシートを介して使用できます。Aspose.Cellsは、数学、文字列、ブール値、日付/時刻、統計、データベース、検索、参照の広範なセットの数式をサポートしています。

[**Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)プロパティまたは[**SetFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2)メソッドの[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラスを使用して、セルに数式を追加します。数式を適用するときには常に等号（=）で始め、Microsoft Excelで数式を作成するときと同様に関数パラメータを区切るためにコンマ（,）を使用します。

数式の結果を計算するには、ユーザーはExcelファイルに埋め込まれたすべての数式を処理する[**CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)メソッドを呼び出すか、シートに埋め込まれたすべての数式を処理する[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)メソッドを呼び出すか、またはセルの数式を処理する[**CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula)メソッドを呼び出すかを選択できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

### **数式に関する重要な点**

{{% alert color="primary" %}}

[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)クラスの**Formula**プロパティと**SetFormula(...)**メソッドは、**Calculate**クラスのメソッドと異なる動作をします。**Formula**プロパティと**SetFormula(...)**メソッドは単にセルに数式を追加するだけであり、実行時に結果を計算しません。数式の結果を取得するには、**Calculate**メソッドを呼び出してください。

{{% /alert %}}

## **数式の直接計算**

Aspose.Cellsには、埋め込みファイルからインポートされた数式を計算するだけでなく、直接数式の結果を計算する機能があります。

時々、ワークシートに追加することなく、Microsoft Excelの数式に基づいてワークシート内にすでに存在するセルの値の結果を見つける必要があります。

Aspose.Cellsの数式計算エンジンAPIを使用して、ワークシートに追加せずにそのような数式の結果を[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)から[**calculate**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)まで計算できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

上記のコードは次の出力を生成します：
{{< highlight net >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **数式を繰り返し計算する方法**

ブック内に多くの数式があり、ユーザーがそれらを修正する部分がわずかで繰り返し計算する必要がある場合は、パフォーマンスのために数式計算チェーンを有効にすると役立ちます：[**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain)。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

### **重要なこと**

{{% alert color="primary" %}}

デフォルトでは、計算チェーンは無効になっています。チェーンを作成するには追加の時間が必要なため、数式を計算する最初の回（[**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)）は、チェーンを作成せずに数式を計算する場合と比較して、CPU処理時間とメモリをより多く消費する可能性があります。ユーザーが数式を繰り返し計算する必要がない場合は、デフォルトの動作（計算チェーンを作成せずに数式を直接計算する）がより良い方法となります。

{{% /alert %}}


## **高度なトピック**
- [Microsoft Excelフォーミュラ計算エンジンのAspose.Cells](/cells/ja/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cellsを使用してIFNA関数を計算する](/cells/ja/net/calculating-ifna-function-using-aspose-cells/)
- [データテーブルの配列式の計算](/cells/ja/net/calculation-of-array-formula-of-data-tables/)
- [Excel 2016のMINIFSおよびMAXIFS関数の計算](/cells/ja/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Cell.Calculateメソッドの計算時間を短縮する](/cells/ja/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [循環参照の検出](/cells/ja/net/detecting-circular-reference/)
- [ワークシートに書き込まずにカスタム機能を直接計算する](/cells/ja/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Aspose.Cellsのデフォルトの計算エンジンを拡張するためにカスタム計算エンジンを実装する](/cells/ja/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [ワークブックの数式計算を中断またはキャンセルする](/cells/ja/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [AbstarctCalculationEngineを使用して値の範囲を返す](/cells/ja/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [ICustomFunctionを使用して値の範囲を返す](/cells/ja/net/returning-a-range-of-values-using-icustomfunction/)
- [ブックの数式計算モードの設定](/cells/ja/net/setting-formula-calculation-mode-of-workbook/)
- [Aspose.CellsでのFormulaText関数の使用](/cells/ja/net/using-formulatext-function-in-aspose-cells/)
- [ICustomFunction機能の使用](/cells/ja/net/using-icustomfunction-feature/)
{{< app/cells/assistant language="csharp" >}}
