---
title: Implementera Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal
type: docs
weight: 20
url: /sv/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **Möjliga användningsscenario**
Microsoft Excel-formler kan ha olika namn i olika platser, regioner eller språk. Till exempel, *SUM* funktionen kallas *SUMME* på *Tyska*. Aspose.Cells kan inte arbeta med icke-Engelska funktionsnamn. I *Microsoft Excel VBA* finns *Range.FormulaLocal* egenskap som returnerar funktionsnamnets namn enligt språk eller region. Aspose.Cells tillhandahåller också [Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal) egenskap för detta ändamål. Men denna egenskap fungerar endast när du implementerar [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName-java.lang.String-) metod. 
## **Implementera Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal**
Följande exempel förklarar hur man implementerar [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName-java.lang.String-) metod. Metoden returnerar det lokala namnet för standardfunktionen. Om standardfunktionsnamnet är *SUM*, returnerar den *UserFormulaLocal_SUM*. Du kan ändra koden enligt dina behov och returnera de korrekta lokala funktionsnamnen, t.ex. *SUM* är *SUMME* på *Tyska* och *TEXT* är *ТЕКСТ* på *Ryska*. Se även utdata från exempel kod för referens.
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **Konsoloutput**
{{< highlight java >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
