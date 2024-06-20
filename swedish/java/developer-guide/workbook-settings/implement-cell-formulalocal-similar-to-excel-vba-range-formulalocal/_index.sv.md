---
title: Implementera Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal
type: docs
weight: 20
url: /sv/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **Möjliga användningsscenario**
Microsoft Excel-formler kan ha olika namn i olika platser eller språk. Till exempel kallas funktionen *SUM* för *SUMME* på tyska. Aspose.Cells kan inte hantera icke-engelska funktionsnamn. I *Microsoft Excel VBA* finns det en *Range.FormulaLocal* egenskap som returnerar namnet på funktionen enligt dess språk eller plats. Aspose.Cells tillhandahåller också egenskapen [Cell.FormulaLocal](https://reference.aspose.com/cells/java/com.aspose.cells/cell#FormulaLocal) för detta ändamål. Dock fungerar denna egenskap bara om du implementerar [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName(java.lang.String)) metod. 
## **Implementera Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal**
Följande exempelkod förklarar hur man implementerar [GlobalizationSettings.getLocalFunctionName(String standardName)](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getLocalFunctionName(java.lang.String)) metod. Metoden returnerar det lokala namnet på den standardiserade funktionen. Om det standardiserade funktionsnamnet är *SUM* returnerar den *UserFormulaLocal_SUM*. Du kan ändra koden efter dina behov och returnera de korrekta lokala funktionsnamnen, t.ex. *SUM* är *SUMME* på tyska och *TEXT* är *ТЕКСТ* på ryska. Se även konsoloutputen från exemplet nedan för referens.
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.java" >}}
## **Konsoloutput**
{{< highlight java >}}

 Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
