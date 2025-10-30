---
title: Golangを使用したC++経由での数式計算
linktitle: 数式の計算
description: この記事では、Golangを使用してC++経由でMicrosoft Excelの数式を計算するためにAspose.Cellsライブラリを使用する方法を紹介します。既存のExcelファイルを読み込むか、新しいExcelファイルを作成し、Aspose.Cellsの提供するメソッドを使って数式を計算し、その結果を取得します。最後に、修正したExcelファイルをディスクに保存します。
keywords: Aspose.Cells、Excel、数式、計算、数式の直接計算、数式の繰り返し計算。
type: docs
weight: 125
url: /ja/go-cpp/calculate-formulas/
---

## **数式の追加と結果の計算**

Aspose.Cellsには組み込みの式計算エンジンがあります。これにより、デザイナーテンプレートからインポートした式の再計算だけでなく、ランタイムで追加された式の結果の計算もサポートしています。

Aspose.CellsはMicrosoft Excelのほとんどの数式や関数をサポートしています（サポートされている関数のリストは [こちら](/cells/ja/cpp/supported-formula-functions/) を参照）。これらの関数はAPIやデザイナースプレッドシートを通じて使用できます。Aspose.Cellsは膨大な数学、文字列、ブール値、日付/時間、統計、データベース、ルックアップ、参照の数式セットをサポートしています。

セルに式を追加するには、[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラスの[**GetFormula**](https://reference.aspose.com/cells/go-cpp/cell/getformula/)プロパティまたは[**SetFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setformula/)メソッドを使用します。式を適用する際は、Microsoft Excelでの作成と同じく文字列の先頭に等号（=）を付け、関数パラメータをカンマ（,）で区切ります。

数式の結果を計算するには、ユーザーは[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスの[**CalculateFormula**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/)メソッドを呼び出すことができ、これによりExcelファイル内のすべての数式が処理されます。または、[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスの[**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/)メソッドを呼び出してシート内のすべての数式を処理するか、あるいは[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)クラスの[**Calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/calculate/)メソッドを呼び出して1つのセルの数式を処理することも可能です。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas.go" >}}
### **数式に関する重要な点**

{{% alert color="primary" %}}

[**Cell**](https://reference.aspose.com/cells/go-cpp/cell/)クラスの**GetFormula**プロパティと**SetFormula(...)**メソッドは、[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)、[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)、[**Cell**](https://reference.aspose.com/cells/go-cpp/cell/)クラスの**Calculate**メソッドとは異なります。**GetFormula**プロパティと**SetFormula(...)**メソッドは単にセルに数式を追加するだけであり、実行時に結果を計算しません。数式の結果を得るには、**Calculate**メソッドを呼び出してください。

{{% /alert %}}

## **数式の直接計算**

Aspose.Cellsには、埋め込みファイルからインポートされた数式を計算するだけでなく、直接数式の結果を計算する機能があります。

ときには、シートに追加せずに式の結果を直接計算する必要があります。式に使用されるセルの値はすでにシートに存在し、それらの値の結果をMicrosoft Excelの式に基づいて見つけたい場合です。

Aspose.Cellsの式計算エンジンAPIを使用して、[**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/)から[**calculate**](https://reference.aspose.com/cells/go-cpp/worksheet/calculateformula/)までの式の結果をシートに追加せずに計算できます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas-1.go" >}}
上記のコードは次の出力を生成します：
{{< highlight cpp >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **繰り返し式の計算方法**

ブック内に多くの式があり、ユーザーが一部分だけを修正して繰り返し計算する必要がある場合、パフォーマンス向上のために式の計算チェーンを有効にすることが役立つかもしれません：[**FormulaSettings.GetEnableCalculationChain()**](https://reference.aspose.com/cells/go-cpp/formulasettings/getenablecalculationchain/)。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculateFormulas-2.go" >}}
### **重要なこと**

{{% alert color="primary" %}}

デフォルトでは、計算チェーンは無効になっています。チェーンの作成には追加の時間が必要なため、最初の計算 ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/)) は、計算チェーンを作成しない場合と比較してCPU処理時間やメモリを多く消費することがあります。ユーザーが繰り返し式を計算する必要がない場合は、デフォルトの動作（直接式を計算し、計算チェーンを作成しない）を選択した方が良いでしょう。

{{% /alert %}}

## ** 高度なトピック**
- [Microsoft Excelフォーミュラ計算エンジンのAspose.Cells](/cells/ja/cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cellsを使用してIFNA関数を計算する](/cells/ja/cpp/calculating-ifna-function-using-aspose-cells/)
- [データテーブルの配列式の計算](/cells/ja/cpp/calculation-of-array-formula-of-data-tables/)
- [Excel 2016のMINIFSおよびMAXIFS関数の計算](/cells/ja/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Cell.Calculateメソッドの計算時間を短縮する](/cells/ja/cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [ワークシートに書き込まずにカスタム機能を直接計算する](/cells/ja/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Aspose.Cellsのデフォルトの計算エンジンを拡張するためにカスタム計算エンジンを実装する](/cells/ja/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [AbstarctCalculationEngineを使用して値の範囲を返す](/cells/ja/cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [ブックの数式計算モードの設定](/cells/ja/cpp/setting-formula-calculation-mode-of-workbook/)
- [Aspose.CellsでのFormulaText関数の使用](/cells/ja/cpp/using-formulatext-function-in-aspose-cells/)
