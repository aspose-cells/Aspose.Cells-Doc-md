---
title: Excel VBA Range.FormulaLocal と同様の Cell.FormulaLocal を実装します。
type: docs
weight: 30
url: /ja/net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---
## **考えられる使用シナリオ**

 Microsoft Excel の数式は、ロケール、地域、言語によって名前が異なる場合があります。例えば、**和**関数が呼び出されます**SUMME**ドイツ語で。 Aspose.Cells は、英語以外の関数名では機能しません。 Microsoft Excel VBA には、**Range.FormulaLocal**言語または地域ごとに関数の名前を返すプロパティ。 Aspose.Cellsも提供しています[**Cell.FormulaLocal**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formulalocal)この目的のためのプロパティ。ただし、このプロパティは、実装する場合にのみ機能します[**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname)方法。

## **Excel VBA Range.FormulaLocal と同様の Cell.FormulaLocal を実装します。**

次のサンプル コードでは、実装方法について説明します。[**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname)方法。このメソッドは、標準関数のローカル名を返します。標準関数名が**和**、それを返します**UserFormulaLocal_SUM**.必要に応じてコードを変更し、正しいローカル関数名を返すことができます。**和**は**SUMME**ドイツ語で**文章**は**ТЕКСТ**ロシア語で。以下のサンプル コードのコンソール出力も参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.cs" >}}

## **コンソール出力**

{{< highlight "java" >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
