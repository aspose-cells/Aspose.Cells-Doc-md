---
title: ImplementeraSubtotal eller Grand Total märken på andra språk med C++
linktitle: Implementera subtotal eller totalmärken på andra språk
type: docs
weight: 50
url: /sv/cpp/implement-subtotal-or-grand-total-labels-in-other-languages/
description: Lär dig hur du implementerar subtotal och totaletiketter på andra språk som kinesiska, japanska, arabiska, hindi etc. med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Ibland vill du visa subtotal- och totaletiketter på andra språk än engelska, som kinesiska, japanska, arabiska, hindi osv. Aspose.Cells tillåter detta med hjälp av [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) klassen och [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getglobalizationsettings/) egenskapen. Se denna artikel om hur du använder [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) klassen:

- [Användning av klassen GlobalizationSettings för anpassade subtotalmärken och andra märken för cirkeldiagram](/cells/sv/cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **Implementera subtotal eller totalmärken på andra språk**

Följande exempel laddar en [exempel Excel-fil](5115151.xlsx) och implementerar subtotal- och totalnamn på kinesiska. Kontrollera den [utdata Excel-fil](5115152.xlsx) som genereras av denna kod för referens. Först skapar vi en klass av [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) och använder den sedan i vår kod.

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

Använd nu den ovan skapade klassen i koden på följande sätt:

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
