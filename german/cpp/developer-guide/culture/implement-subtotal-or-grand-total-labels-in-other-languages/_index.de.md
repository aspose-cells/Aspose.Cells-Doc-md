---
title: Implementieren Sie Zwischen oder Gesamtsummen Labels in anderen Sprachen mit C++
linktitle: Implementieren Sie Subtotal oder Gesamtsummen Labels in anderen Sprachen
type: docs
weight: 50
url: /de/cpp/implement-subtotal-or-grand-total-labels-in-other-languages/
description: Erfahren Sie, wie Sie Subtotal und Gesamtsummenbeschriftungen in Nicht Englisch Sprachen mit Aspose.Cells for C++ implementieren.
---

## **Mögliche Verwendungsszenarien**

Manchmal möchten Sie Subtotal- und Gesamtsummenbeschriftungen in Nicht-Englisch-Sprachen wie Chinesisch, Japanisch, Arabisch, Hindi usw. anzeigen. Aspose.Cells ermöglicht dies mithilfe der [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) Klasse und der [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getglobalizationsettings/) Eigenschaft. Bitte lesen Sie diesen Artikel, um die Verwendung der [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) Klasse zu lernen:

- [Verwendung der GlobalizationSettings-Klasse für benutzerdefinierte Teilergebnisbeschriftungen und andere Beschriftungen des Kuchendiagramms](/cells/de/cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **Implementieren Sie Subtotal- oder Gesamtsummen-Labels in anderen Sprachen**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](5115151.xlsx) und implementiert Subtotal- und Gesamtsummen-Namen in der chinesischen Sprache. Bitte prüfen Sie die [Ausgabedatei Excel](5115152.xlsx), die von diesem Code generiert wurde, zu Ihrer Referenz. Zuerst erstellen wir eine Klasse von [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) und verwenden sie im Code.

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

Verwenden Sie nun die oben erstellte Klasse im Code wie folgt:

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
