---
title: Implementa etichette di subtotale o totale generale in altre lingue con C++
linktitle: Implementa etichette Subtotal o Grand Total in altre lingue
type: docs
weight: 50
url: /it/cpp/implement-subtotal-or-grand-total-labels-in-other-languages/
description: Impara come implementare etichette di subtotale e totale generale in lingue non inglesi usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

A volte, vuoi mostrare etichette di subtotale e totale generale in lingue non inglesi come cinese, giapponese, arabo, hindi, ecc. Aspose.Cells ti permette di farlo usando la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) e la proprietà [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getglobalizationsettings/). Consulta questo articolo per sapere come utilizzare la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/).

- [Utilizzo della classe GlobalizationSettings per le etichette Subtotali personalizzate e altre etichette del grafico a torta](/cells/it/cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **Implementa etichette Subtotal o Grand Total in altre lingue**

Il codice di esempio seguente carica il file Excel [di esempio](5115151.xlsx) e implementa nomi di subtotale e totale generale in lingua cinese. Controlla il [file Excel di output](5115152.xlsx) generato da questo codice come riferimento. Prima creiamo una classe di [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) e poi la usiamo nel nostro codice.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class GlobalizationSettingsImp : public GlobalizationSettings
{
public:
    U16String GetTotalName(ConsolidationFunction functionType) override
    {
        return u"Chinese Total - \u53EF\u80FD\u7684\u7528\u6CD5";
    }

    U16String GetGrandTotalName(ConsolidationFunction functionType) override
    {
        return u"Chinese Grand Total - \u53EF\u80FD\u7684\u7528\u6CD5";
    }
};
```

Ora utilizza la classe creata sopra nel codice come segue:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

class GlobalizationSettingsImp : public GlobalizationSettings {
public:
    virtual U16String GetTotalName(ConsolidationFunction functionType) override {
        return u"Custom Total";
    }

    virtual U16String GetGrandTotalName(ConsolidationFunction functionType) override {
        return u"Custom Grand Total";
    }
};

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"sample.xlsx");

    GlobalizationSettingsImp gsi;
    wb.GetSettings().SetGlobalizationSettings(&gsi);

    Worksheet ws = wb.GetWorksheets().Get(0);

    CellArea ca = CellArea::CreateCellArea(u"A1", u"B10");
    ws.GetCells().Subtotal(ca, 0, ConsolidationFunction::Sum, {2, 3, 4});

    ws.GetCells().SetColumnWidth(0, 40);

    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Subtotal applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
