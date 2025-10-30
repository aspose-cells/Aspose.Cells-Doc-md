---
title: Implementera Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal med Golang via C++
linktitle: Implementera Cell.FormulaLocal
type: docs
weight: 30
url: /sv/go-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Lär dig hur du implementerar Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal med Aspose.Cells med Golang via C++.
---

## **Möjliga användningsscenario**

Microsoft Excel-formler kan ha olika namn på olika platser eller språk. Till exempel kallas **SUM**-funktionen för **SUMME** på tyska. Aspose.Cells kan inte användas med icke-engelska funktionsnamn. I Microsoft Excel VBA finns det egenskapen **Range.FormulaLocal** som returnerar namnet på funktionen enligt dess språk eller plats. Aspose.Cells tillhandahåller också [**Cell.FormulaLocal**](https://reference.aspose.com/cells/go-cpp/cell/getformulalocal/) egenskap för detta ändamål. Denna egenskap fungerar dock endast när du implementerar [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/) metoden.

## **Implementera Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal**

Följande exempelkod förklarar hur du implementerar [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/getlocalfunctionname/) metoden. Metoden returnerar det lokala namnet på den standardfunktionen. Om den standardfunktionen heter **SUM**, returnerar den **UserFormulaLocal_SUM**. Du kan ändra koden enligt dina behov och returnera de korrekta lokala funktionsnamnen t.ex. är **SUM** **SUMME** på tyska och **TEXT** **ТЕКСТ** på ryska. Se även utdata för exemplkoden nedan som referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementCellFormulalocalSimilarToExcelVbaRangeFormulalocal.go" >}}
## **Konsoloutput**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
