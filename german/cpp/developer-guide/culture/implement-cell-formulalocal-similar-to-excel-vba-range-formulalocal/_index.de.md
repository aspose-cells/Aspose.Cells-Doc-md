---
title: Implementieren Sie Cell.FormulaLocal ähnlich wie Excel VBA Range.FormulaLocal mit C++
linktitle: Implementieren Sie Cell.FormulaLocal
type: docs
weight: 30
url: /de/cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Lernen Sie, wie Sie Cell.FormulaLocal ähnlich wie Excel VBA Range.FormulaLocal mit Aspose.Cells und C++ implementieren.
---

## **Mögliche Verwendungsszenarien**

Microsoft Excel-Formeln können in verschiedenen Regionen oder Sprachen unterschiedliche Namen haben. Zum Beispiel wird die **SUM**-Funktion auf Deutsch als **SUMME** bezeichnet. Aspose.Cells kann nicht mit Funktionen, die nicht in englischer Sprache angegeben sind, arbeiten. In Microsoft Excel VBA gibt es die **Range.FormulaLocal**-Eigenschaft, die den Namen der Funktion je nach Sprache oder Region zurückgibt. Aspose.Cells bietet auch die Eigenschaft [**Cell.FormulaLocal**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformulalocal/) für diesen Zweck. Diese Eigenschaft funktioniert jedoch nur, wenn Sie die [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/)-Methode implementiert haben.

## **Implementieren Sie Cell.FormulaLocal ähnlich wie Excel VBA Range.FormulaLocal**

Der folgende Beispielcode erläutert die Implementierung der Methode [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/). Die Methode gibt den lokalen Namen der Standardfunktion zurück. Wenn der Standardfunktionsname **SUM** ist, wird **UserFormulaLocal_SUM** zurückgegeben. Sie können den Code entsprechend Ihren Bedürfnissen ändern und die korrekten lokalen Funktionsnamen zurückgeben, z.B. ist **SUM** auf Deutsch **SUMME** und **TEXT** im Russischen **ТЕКСТ**. Bitte beachten Sie auch die Konsolenausgabe des untenstehenden Beispielcodes zur Referenz.

## **Beispielcode**

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

## **Konsolenausgabe**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
