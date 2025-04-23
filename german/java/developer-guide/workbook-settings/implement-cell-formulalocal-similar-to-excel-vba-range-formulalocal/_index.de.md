---
title: Implementieren Sie Cell.FormulaLocal ähnlich wie Excel VBA Range.FormulaLocal
type: docs
weight: 20
url: /de/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **Mögliche Verwendungsszenarien**
Microsoft Excel-Formeln können in verschiedenen Regionen, Ländern oder Sprachen unterschiedliche Namen haben. Zum Beispiel wird die Funktion *SUM* in *German* *SUMME* genannt. Aspose.Cells kann mit nicht-englischen Funktionsnamen nicht arbeiten. In *Microsoft Excel VBA* gibt es die Eigenschaft *Range.FormulaLocal*, die den Namen der Funktion entsprechend ihrer Sprache oder Region zurückgibt. Aspose.Cells bietet auch die Eigenschaft [Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal) für diesen Zweck. Diese Eigenschaft funktioniert jedoch nur, wenn Sie [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName-java.lang.String-) implementieren. 
## **Implementieren Sie Cell.FormulaLocal ähnlich wie Excel VBA Range.FormulaLocal**
Das folgende Beispiel zeigt, wie die Methode [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName-java.lang.String-) implementiert wird. Die Methode gibt den lokalen Namen der Standardfunktion zurück. Wenn der Standardfunktionsname *SUM* ist, gibt sie *UserFormulaLocal_SUM* zurück. Sie können den Code nach Ihren Bedürfnissen anpassen und die richtigen lokalen Funktionsnamen zurückgeben, z.B. *SUM* ist in *German* *SUMME* und *TEXT* ist in *Russisch* *ТЕКСТ*. Siehe auch die Konsolenausgabe des Beispielcodes unten als Referenz.
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **Konsolenausgabe**
{{< highlight java >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
