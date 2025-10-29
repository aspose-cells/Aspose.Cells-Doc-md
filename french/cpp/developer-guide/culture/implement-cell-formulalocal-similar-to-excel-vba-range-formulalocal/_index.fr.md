---
title: Implémenter Cell.FormulaLocal similaire à Excel VBA Range.FormulaLocal avec C++
linktitle: Implémenter Cell.FormulaLocal
type: docs
weight: 30
url: /fr/cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Apprenez comment implémenter Cell.FormulaLocal similaire à Excel VBA Range.FormulaLocal en utilisant Aspose.Cells avec C++.
---

## **Scénarios d'utilisation possibles**

Les formules Microsoft Excel peuvent avoir des noms différents dans différentes langues ou régions. Par exemple, la fonction **SUM** est appelée **SUMME** en allemand. Aspose.Cells ne peut pas fonctionner avec des noms de fonction non anglais. En VBA Excel, il existe la propriété **Range.FormulaLocal** qui renvoie le nom de la fonction selon sa langue ou sa région. Aspose.Cells fournit également la propriété [**Cell.FormulaLocal**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformulalocal/) à cette fin. Cependant, cette propriété ne fonctionnera que si vous implémentez [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/) méthode.

## **Implémenter Cell.FormulaLocal similaire à Excel VBA Range.FormulaLocal**

Le code d'exemple suivant explique comment implémenter la méthode [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/). La méthode renvoie le nom local de la fonction standard. Si le nom de la fonction standard est **SUM**, elle renvoie **UserFormulaLocal_SUM**. Vous pouvez modifier le code selon vos besoins et renvoyer les noms de fonction locaux corrects, par exemple **SUM** est **SUMME** en allemand et **TEXT** est **ТЕКСТ** en russe. Veuillez également consulter la sortie console du code d'exemple ci-dessous pour référence.

## **Code d'exemple**

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

## **Sortie console**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
