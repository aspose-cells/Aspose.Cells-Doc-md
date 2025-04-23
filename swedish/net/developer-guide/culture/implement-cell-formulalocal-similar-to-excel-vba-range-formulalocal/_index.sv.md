---
title: Implementera Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /sv/net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **Möjliga användningsscenario**

Microsoft Excel-formler kan ha olika namn på olika platser eller språk. Till exempel kallas **SUM**-funktionen för **SUMME** på tyska. Aspose.Cells kan inte användas med icke-engelska funktionsnamn. I Microsoft Excel VBA finns det egenskapen **Range.FormulaLocal** som returnerar namnet på funktionen enligt dess språk eller plats. Aspose.Cells tillhandahåller också [**Cell.FormulaLocal**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formulalocal) egenskap för detta ändamål. Denna egenskap fungerar dock endast när du implementerar [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname) metoden.

## **Implementera Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal**

Följande exempelkod förklarar hur du implementerar [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname) metoden. Metoden returnerar det lokala namnet på den standardfunktionen. Om den standardfunktionen heter **SUM**, returnerar den **UserFormulaLocal_SUM**. Du kan ändra koden enligt dina behov och returnera de korrekta lokala funktionsnamnen t.ex. är **SUM** **SUMME** på tyska och **TEXT** **ТЕКСТ** på ryska. Se även utdata för exemplkoden nedan som referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.cs" >}}

## **Konsoloutput**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
