---
title: Implementieren Sie Cell.FormulaLocal ähnlich wie Excel VBA Range.FormulaLocal
type: docs
weight: 20
url: /de/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---
## **Mögliche Nutzungsszenarien**
Microsoft Excel-Formeln können in verschiedenen Gebietsschemata, Regionen oder Sprachen unterschiedliche Namen haben. Zum Beispiel,*SUMME*Funktion aufgerufen wird*SUMME*in*Deutsch*Aspose.Cells funktioniert nicht mit nicht-englischen Funktionsnamen. In*Microsoft Excel-VBA*, Es gibt* *a*Range.FormulaLocal*-Eigenschaft, die den Namen der Funktion gemäß ihrer Sprache oder Region zurückgibt. Aspose.Cells bietet auch[Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal)Eigentum für diesen Zweck. Diese Eigenschaft funktioniert jedoch nur, wenn Sie implementieren[GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)) Methode.
## **Implementieren Sie Cell.FormulaLocal ähnlich wie Excel VBA Range.FormulaLocal**
Der folgende Beispielcode erläutert die Implementierung[GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)) Methode. Die Methode gibt den lokalen Namen der Standardfunktion zurück. Wenn der Standardfunktionsname lautet*SUMME*, es kehrt zurück*UserFormulaLocal_SUM*. Sie können den Code nach Ihren Bedürfnissen ändern und die richtigen lokalen Funktionsnamen zurückgeben, z*SUMME*ist*SUMME*in*Deutsch*und*TEXT*ist*ТЕКСТ*in*Russisch*. Siehe auch die Konsolenausgabe des unten angegebenen Beispielcodes als Referenz.
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **Konsolenausgabe**
{{< highlight "java" >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
