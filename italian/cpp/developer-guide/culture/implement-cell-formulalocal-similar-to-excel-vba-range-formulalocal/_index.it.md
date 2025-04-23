---
title: Implementa Cell.FormulaLocal simile a Range.FormulaLocal di Excel VBA con C++
linktitle: Implementa Cell.FormulaLocal
type: docs
weight: 30
url: /it/cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Impara come implementare Cell.FormulaLocal, simile a Excel VBA Range.FormulaLocal, usando Aspose.Cells con C++.
---

## **Possibili Scenari di Utilizzo**

Le formule di Microsoft Excel possono avere nomi diversi in diverse località, regioni o lingue. Ad esempio, la funzione **SUM** viene chiamata **SUMME** in tedesco. Aspose.Cells non può lavorare con nomi di funzioni non in inglese. In Microsoft Excel VBA, c'è la proprietà **Range.FormulaLocal** che restituisce il nome della funzione in base alla lingua o alla regione. Aspose.Cells fornisce anche la proprietà [**Cell.FormulaLocal**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformulalocal/) a questo scopo. Tuttavia, questa proprietà funzionerà solo quando implementerai il metodo [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/).

## **Implementa Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal**

Il seguente codice di esempio spiega come implementare il metodo [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/). Il metodo restituisce il nome locale della funzione standard. Se il nome della funzione standard è **SUM**, restituisce **UserFormulaLocal_SUM**. Puoi modificare il codice in base alle tue esigenze e restituire i nomi corretti delle funzioni locali come ad esempio **SUM** è **SUMME** in tedesco e **TEXT** è **ТЕКСТ** in russo. Consulta anche l'output della console del codice di esempio qui sotto a titolo di riferimento.

## **Codice di Esempio**

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

## **Output della console**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
