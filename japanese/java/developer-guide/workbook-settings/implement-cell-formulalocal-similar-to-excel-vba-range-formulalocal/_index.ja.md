---
title: Excel VBAのRange.FormulaLocalに類似したCell.FormulaLocalの実装
type: docs
weight: 20
url: /ja/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **可能な使用シナリオ**
Microsoft Excelの数式は、ロケールや地域、言語によって異なる名前を持つ場合があります。例として、*SUM* 関数はドイツ語では *SUMME* と呼ばれます。Aspose.Cellsは非英語の関数名には対応していません。*Microsoft Excel VBA*には *Range.FormulaLocal* プロパティがあり、その言語や地域に応じた関数名を返します。Aspose.Cellsもこれに対応しており、[Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal) プロパティを提供しています。ただし、このプロパティは [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName-java.lang.String-) メソッドを実装したときだけ機能します。 
## **Excel VBAのRange.FormulaLocalと同様にCell.FormulaLocalを実装する**
以下のサンプルコードは、[GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName-java.lang.String-) メソッドの実装方法を説明しています。このメソッドは、標準関数のローカル名を返します。標準関数名が *SUM* の場合、*UserFormulaLocal_SUM* を返します。必要に応じてコードを変更し、正しいローカル関数名を返してください。例として、*SUM* はドイツ語で *SUMME*、*TEXT* はロシア語で *ТЕКСТ* です。下記のサンプルコードのコンソール出力も参考にしてください。
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **コンソール出力**
{{< highlight java >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
