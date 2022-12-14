---
title: Implementera Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal
type: docs
weight: 30
url: /sv/net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---
## **Möjliga användningsscenarier**

 Microsoft Excel-formler kan ha olika namn i olika lokaler eller regioner eller språk. Till exempel,**BELOPP**funktionen kallas**SUMMA**på tyska. Aspose.Cells kan inte fungera med icke-engelska funktionsnamn. I Microsoft Excel VBA finns det**Range.FormulaLocal**egenskap som returnerar namnet på funktionen enligt dess språk eller region. Aspose.Cells tillhandahåller också[**Cell.FormulaLocal**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formulalocal)egendom för detta ändamål. Den här egenskapen kommer dock bara att fungera när du ska implementera[**GlobalizationSettings.GetLocalFunctionName(sträng standardnamn)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname)metod.

## **Implementera Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal**

 Följande exempelkod förklarar hur man implementerar[**GlobalizationSettings.GetLocalFunctionName(sträng standardnamn)**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getlocalfunctionname) metod. Metoden returnerar det lokala namnet på standardfunktionen. Om standardfunktionsnamnet är**BELOPP** , den återkommer**UserFormulaLocal_SUM** . Du kan ändra koden enligt dina behov och returnera de korrekta lokala funktionsnamnen, t.ex**BELOPP** är**SUMMA** på tyska och**TEXT** är**ТЕКСТ**på ryska. Se även konsolutgången för exempelkoden nedan för en referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal.cs" >}}

## **Konsolutgång**

{{< highlight "java" >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
