---
title: Implementar Cell.FormulaLocal similar a Range.FormulaLocal de Excel VBA con C++
linktitle: Implementar Cell.FormulaLocal
type: docs
weight: 30
url: /es/cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Aprende cómo implementar Cell.FormulaLocal similar a Excel VBA Range.FormulaLocal usando Aspose.Cells con C++.
---

## **Escenarios de uso posibles**

Las fórmulas de Microsoft Excel pueden tener diferentes nombres en diferentes lugares o regiones o idiomas. Por ejemplo, la función **SUMA** se llama **SUMME** en alemán. Aspose.Cells no puede trabajar con nombres de función no-ingleses. En Microsoft Excel VBA, hay una propiedad **Range.FormulaLocal** que devuelve el nombre de la función según su idioma o región. Aspose.Cells también proporciona la propiedad [**Cell.FormulaLocal**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformulalocal/) para este propósito. Sin embargo, esta propiedad solo funcionará cuando implemente el método [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/).

## **Implementar Cell.FormulaLocal similar a Excel VBA Range.FormulaLocal**

El siguiente código de ejemplo explica cómo implementar el método [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/). El método devuelve el nombre local de la función estándar. Si el nombre de la función estándar es **SUM**, devuelve **UserFormulaLocal_SUM**. Puede cambiar el código según sus necesidades y devolver los nombres de función locales correctos, por ejemplo **SUMA** es **SUMME** en alemán y **TEXTO** es **ТЕКСТ** en ruso. Por favor, consulte también la salida de consola del código de ejemplo dado abajo para referencia.

## **Código de muestra**

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

## **Salida de la consola**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
