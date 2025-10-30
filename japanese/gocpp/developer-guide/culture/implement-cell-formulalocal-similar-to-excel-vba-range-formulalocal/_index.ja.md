---
title: Excel VBA Range.FormulaLocalと似たCell.FormulaLocalをC++経由のGolangで実装する
linktitle: Cell.FormulaLocalの実装
type: docs
weight: 30
url: /ja/go-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Aspose.Cellsを使用してC++経由のGolangでExcel VBA Range.FormulaLocalに似たCell.FormulaLocalを実装する方法を学ぶ。
---

## **可能な使用シナリオ**

Microsoft Excelの関数は、異なる地域や言語で異なるロケール名を持つ場合があります。例えば、**SUM**関数はドイツ語では**SUMME**と呼ばれます。Aspose.Cellsでは、非英語の関数名は使用できません。Microsoft Excel VBAには、関数の名前をその言語や地域に合わせて返す**Range.FormulaLocal**プロパティがあります。Aspose.Cellsもこの目的のために[**Cell.FormulaLocal**](https://reference.aspose.com/cells/go-cpp/cell/getformulalocal/)プロパティを提供しています。ただし、このプロパティは[**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/)メソッドを実装している場合にのみ機能します。

## **Excel VBAのRange.FormulaLocalと同様にCell.FormulaLocalを実装する**

以下のサンプルコードは、[**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/getlocalfunctionname/)メソッドの実装方法を説明しています。このメソッドは、標準関数のローカル名を返します。標準関数名が **SUM** の場合、**UserFormulaLocal_SUM** を返します。**SUM** はドイツ語では **SUMME** 、ロシア語では **ТЕКСТ** となります。必要に応じてコードを変更し、正しいローカル関数名を返してください。また、下記のサンプルコードのコンソール出力も参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementCellFormulalocalSimilarToExcelVbaRangeFormulalocal.go" >}}
## **コンソール出力**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
