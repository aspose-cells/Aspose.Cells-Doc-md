---
title: 数式を計算する方法
type: docs
weight: 30
url: /ja/go-cpp/ways-to-calculate-formulas/
---

## **紹介**

Aspose.Cellsには埋め込み式計算エンジンがあります。デザイナーテンプレートからインポートされた数式を再計算するだけでなく、実行時に追加された数式の結果を計算することもできます。

## **数式の追加と結果の計算**

Aspose.Cellsは、Microsoft Excelの一部であるほとんどの数式または関数をサポートしています。これらはAPIまたはデザイナースプレッドシートを通じて使用できます。Aspose.Cellsは、数学、文字列、ブール値、日付/時刻、統計、検索、参照の大規模な数式セットをサポートしています。

Cell.SetFormulaメソッドを使用して、セルに数式を追加します。セルに数式を適用する場合は、常にMicrosoft Excelで数式を作成するときと同様に、等号（=）で文字列を始めます。関数のパラメータを区切るには、コンマ（,）を使用します。

数式の結果を計算するには、Workbook.CalculateFormula()メソッドを呼び出します。このメソッドはExcelファイルに埋め込まれたすべての数式を処理します。このコードで追加された数式とその結果を計算した[出力Excelファイル](38109185.xlsx)を参照してください。

**サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingFormulasAndCalculatingResults.go" >}}

## **一度だけ数式を計算する**

Workbook.CalculateFormula()がワークブックテンプレート内の数式の値を計算すると、Aspose.Cellsは計算チェーンを作成します。数式を2回目や3回目に計算する際にパフォーマンスが向上します。

ただし、テンプレートに多数の数式が含まれている場合、最初に数式を計算するとCPU処理時間とメモリを多く消費する可能性があります。

Aspose.Cellsでは、一度だけ数式を計算したいときに便利な計算チェーンの作成をオフにすることができます。

Workbook.GetISettings().SetCreateCalcChain()メソッドをfalseパラメータとともに呼び出してください。このコードをテストするためには、提供されたExcelファイル(38109186.xlsx)を使用できます。

**サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculatingFormulasOnceOnly.go" >}}
