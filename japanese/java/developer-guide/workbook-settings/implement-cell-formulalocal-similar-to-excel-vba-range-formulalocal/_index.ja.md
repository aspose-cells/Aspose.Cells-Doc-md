---
title: Excel VBAのRange.FormulaLocalに類似したCell.FormulaLocalの実装
type: docs
weight: 20
url: /ja/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **可能な使用シナリオ**
Microsoft Excelの数式は、異なるロケール、地域、または言語では異なる名前を持つ場合があります。たとえば、*SUM*関数は*German*では*SUMME*と呼ばれます。Aspose.Cellsは非英語の関数名では機能しません。*Microsoft Excel VBA*には*Range.FormulaLocal*プロパティがあり、その言語や地域に応じた関数名を返します。Aspose.Cellsもこの目的のために[Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal)プロパティを提供しています。ただし、このプロパティは[GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\))メソッドを実装するとのみ機能します。 
## **Excel VBAのRange.FormulaLocalと同様にCell.FormulaLocalを実装する**
次のサンプルコードでは、[GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\))メソッドの実装方法を説明しています。このメソッドは、標準関数のローカル名を返します。標準関数名が*SUM*であれば*UserFormulaLocal_SUM*を返します。コードを必要に応じて変更し、正しいローカル関数名を返します。たとえば、*SUM*は*German*で*SUMME*であり、*TEXT*は*Russian*で*ТЕКСТ*です。また、以下のサンプルコードのコンソール出力を参照してください。
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **コンソール出力**
{{< highlight java >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
