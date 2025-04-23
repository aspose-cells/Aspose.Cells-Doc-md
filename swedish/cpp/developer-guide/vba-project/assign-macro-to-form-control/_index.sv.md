---
title: Tilldela makro till formulärkontroll med C++
linktitle: Tilldela Makro till Formulärkontroll
type: docs
weight: 60
url: /sv/cpp/assign-macro-to-form-control/
description: Lär dig hur man tilldelar en makkod till en formulärkontroll som en knapp med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells låter dig tilldela ett makro kod till en formulärkontroll som en knapp. Använd [**Shape.GetMacroName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getmacroname/) -egenskapen för att tilldela en ny makro kod till en formulärkontroll i arbetsboken.

{{% /alert %}}

Följande kodexempel skapar en ny arbetsbok, tilldelar ett makrokod till en formulärknapp och sparar resultatet i XLSM-format. När du öppnar XLSM-filen i Microsoft Excel, kommer du att se följande makrokod.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Tilldela makro till formulärkontroll i C++**

Här är ett exempel på kod för att generera utdata-XLSM-fil med makro kod.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Vba;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    int moduleIdx = workbook.GetVbaProject().GetModules().Add(sheet);
    VbaModule module = workbook.GetVbaProject().GetModules().Get(moduleIdx);
    module.SetCodes(
        u"Sub ShowMessage()\r\n"
        u"    MsgBox \"Welcome to Aspose!\"\r\n"
        u"End Sub"
    );

    Button button = sheet.GetShapes().AddButton(2, 0, 2, 0, 28, 80);
    button.SetPlacement(PlacementType::FreeFloating);
    button.GetFont().SetName(u"Tahoma");
    button.GetFont().SetIsBold(true);
    button.GetFont().SetColor(Color::Blue());
    button.SetText(u"Aspose");

    button.SetMacroName(sheet.GetName() + u".ShowMessage");

    U16String outputPath = outDir + u"Output.out.xlsm";
    workbook.Save(outputPath);

    std::cout << "VBA button added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
