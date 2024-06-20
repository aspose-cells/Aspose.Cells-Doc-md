---
title: Implementieren Sie Cell.FormulaLocal ähnlich wie Excel VBA Range.FormulaLocal
type: docs
weight: 20
url: /de/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **Mögliche Verwendungsszenarien**
Microsoft Excel-Formeln können in verschiedenen Sprach- oder Regionslokalen unterschiedliche Namen haben. Zum Beispiel wird die *SUM*-Funktion im *Deutschen* als *SUMME* bezeichnet. Aspose.Cells kann nicht mit Funktionen arbeiten, die keine englischen Namen haben. In *Microsoft Excel VBA* gibt es die Eigenschaft *Range.FormulaLocal*, die den Namen der Funktion je nach Sprache oder Region zurückgibt. Aspose.Cells bietet auch die [Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal)-Eigenschaft für diesen Zweck. Allerdings funktioniert diese Eigenschaft nur, wenn Sie die Methode [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)) implementieren. 
## **Implementieren Sie Cell.FormulaLocal ähnlich wie Excel VBA Range.FormulaLocal**
Der folgende Beispielcode erläutert, wie die Methode [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)) implementiert wird. Die Methode gibt den lokalen Namen der Standardfunktion zurück. Wenn der Standardfunktionsname *SUM* ist, gibt sie *UserFormulaLocal_SUM* zurück. Sie können den Code nach Ihren Bedürfnissen ändern und die korrekten lokalen Funktionsnamen zurückgeben, z.B. *SUM* ist *SUMME* auf Deutsch und *TEXT* ist *ТЕКСТ* auf Russisch. Bitte beachten Sie auch die Konsolenausgabe des untenstehenden Beispielcodes als Referenz.
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **Konsolenausgabe**
{{< highlight java >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
