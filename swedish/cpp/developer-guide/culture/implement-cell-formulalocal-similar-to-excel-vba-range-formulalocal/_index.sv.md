---
title: Implementera Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal med C++
linktitle: Implementera Cell.FormulaLocal
type: docs
weight: 30
url: /sv/cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Lär dig hur du implementerar Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal med Aspose.Cells och C++.
---

## **Möjliga användningsscenario**

Microsoft Excel-formler kan ha olika namn på olika platser eller språk. Till exempel kallas **SUM**-funktionen för **SUMME** på tyska. Aspose.Cells kan inte användas med icke-engelska funktionsnamn. I Microsoft Excel VBA finns det egenskapen **Range.FormulaLocal** som returnerar namnet på funktionen enligt dess språk eller plats. Aspose.Cells tillhandahåller också [**Cell.FormulaLocal**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformulalocal/) egenskap för detta ändamål. Denna egenskap fungerar dock endast när du implementerar [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/) metoden.

## **Implementera Cell.FormulaLocal liknande Excel VBA Range.FormulaLocal**

Följande exempelkod förklarar hur du implementerar [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/) metoden. Metoden returnerar det lokala namnet på den standardfunktionen. Om den standardfunktionen heter **SUM**, returnerar den **UserFormulaLocal_SUM**. Du kan ändra koden enligt dina behov och returnera de korrekta lokala funktionsnamnen t.ex. är **SUM** **SUMME** på tyska och **TEXT** **ТЕКСТ** på ryska. Se även utdata för exemplkoden nedan som referens.

## **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

// Implement GlobalizationSettings class
class GS : public GlobalizationSettings
{
public:
    virtual U16String GetLocalFunctionName(const U16String& standardName) override
    {
        // Change the SUM function name as per your needs.
        if (standardName == u"SUM")
        {
            return u"UserFormulaLocal_SUM";
        }

        // Change the AVERAGE function name as per your needs.
        if (standardName == u"AVERAGE")
        {
            return u"UserFormulaLocal_AVERAGE";
        }

        return u"";
    }
};

void Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal()
{
    // Create workbook
    Workbook wb;

    // Assign GlobalizationSettings implementation class
    wb.GetSettings().SetGlobalizationSettings(new GS());

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access some cell
    Cell cell = ws.GetCells().Get(u"C4");

    // Assign SUM formula and print its FormulaLocal
    cell.SetFormula(u"SUM(A1:A2)");
    std::cout << "Formula Local: " << cell.GetFormulaLocal().ToUtf8() << std::endl;

    // Assign AVERAGE formula and print its FormulaLocal
    cell.SetFormula(u"=AVERAGE(B1:B2, B5)");
    std::cout << "Formula Local: " << cell.GetFormulaLocal().ToUtf8() << std::endl;
}

int main()
{
    Aspose::Cells::Startup();
    Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsoloutput**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
