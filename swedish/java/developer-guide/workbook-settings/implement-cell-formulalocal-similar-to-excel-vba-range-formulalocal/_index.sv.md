---
title: Implementera Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal
type: docs
weight: 20
url: /sv/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---
## **Möjliga användningsscenarier**
Microsoft Excel-formler kan ha olika namn i olika lokaler eller regioner eller språk. Till exempel,*BELOPP*funktionen kallas*SUMMA*i*tysk*. Aspose.Cells kan inte fungera med icke-engelska funktionsnamn. I*Microsoft Excel VBA*, det finns* *a*Range.FormulaLocal*egenskap som returnerar namnet på funktionen enligt dess språk eller region. Aspose.Cells tillhandahåller också[Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal)egendom för detta ändamål. Den här egenskapen kommer dock bara att fungera när du ska implementera[GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)) metod.
## **Implementera Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal**
Följande exempelkod förklarar hur man implementerar[GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName\(java.lang.String\)) metod. Metoden returnerar det lokala namnet på standardfunktionen. Om standardfunktionsnamnet är*BELOPP*, den återkommer*UserFormulaLocal_SUM*. Du kan ändra koden enligt dina behov och returnera de korrekta lokala funktionsnamnen, t.ex*BELOPP*är*SUMMA*i*tysk*och*TEXT*är*ТЕКСТ*i*ryska*. Se även konsolutgången för exempelkoden nedan för en referens.
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **Konsolutgång**
{{< highlight "java" >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
