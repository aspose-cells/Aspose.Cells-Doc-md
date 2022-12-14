---
title: Implementieren Sie Cell.FormulaLocal ähnlich wie Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /de/net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---
## **Mögliche Nutzungsszenarien**

 Microsoft Excel-Formeln können in verschiedenen Gebietsschemata, Regionen oder Sprachen unterschiedliche Namen haben. Zum Beispiel,**SUMME**Funktion aufgerufen wird**SUMME** auf Deutsch. Aspose.Cells funktioniert nicht mit nicht-englischen Funktionsnamen. In Microsoft Excel VBA gibt es**Range.FormulaLocal**-Eigenschaft, die den Namen der Funktion gemäß ihrer Sprache oder Region zurückgibt. Aspose.Cells bietet auch[**Cell.FormulaLocal**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formulalocal)Eigentum für diesen Zweck. Diese Eigenschaft funktioniert jedoch nur, wenn Sie implementieren[**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname)Methode.

## **Implementieren Sie Cell.FormulaLocal ähnlich wie Excel VBA Range.FormulaLocal**

 Der folgende Beispielcode erläutert die Implementierung[**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname) Methode. Die Methode gibt den lokalen Namen der Standardfunktion zurück. Wenn der Standardfunktionsname lautet**SUMME** , es kehrt zurück**UserFormulaLocal_SUM** Sie können den Code nach Ihren Bedürfnissen ändern und die richtigen lokalen Funktionsnamen zurückgeben, z**SUMME** ist**SUMME** auf Deutsch u**TEXT** ist**ТЕКСТ**auf Russisch. Siehe auch die Konsolenausgabe des unten angegebenen Beispielcodes als Referenz.

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.cs" >}}

## **Konsolenausgabe**

{{< highlight "java" >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
