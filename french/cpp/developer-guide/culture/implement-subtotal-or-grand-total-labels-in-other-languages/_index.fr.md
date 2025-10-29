---
title: Implémenter les étiquettes de sous total ou de total général dans d autres langues avec C++
linktitle: Implémentez les étiquettes de sous totaux ou de totaux généraux dans d autres langues
type: docs
weight: 50
url: /fr/cpp/implement-subtotal-or-grand-total-labels-in-other-languages/
description: Apprenez comment implémenter des étiquettes de sous total et de total général dans des langues autres que l anglais en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Parfois, vous souhaitez afficher des étiquettes de sous-total et de total général dans des langues autres que l'anglais, comme le chinois, le japonais, l'arabe, l'hindi, etc. Aspose.Cells vous permet de le faire en utilisant la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) et la propriété [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getglobalizationsettings/). Veuillez consulter cet article pour savoir comment utiliser la classe [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) :

- [Utilisation de la classe GlobalizationSettings pour des étiquettes de sous-total personnalisées et d'autres étiquettes du graphique circulaire](/cells/fr/cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **Implémentez les étiquettes de sous-totaux ou de totaux généraux dans d'autres langues**

Le code d'exemple suivant charge le [fichier Excel d'exemple](5115151.xlsx) et implémente des noms de sous-total et de total général en chinois. Veuillez vérifier le [fichier Excel de sortie](5115152.xlsx) généré par ce code pour référence. Nous créons d'abord une classe [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) puis l'utilisons dans notre code.

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

Utilisez la classe créée ci-dessus dans le code comme suit :

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
