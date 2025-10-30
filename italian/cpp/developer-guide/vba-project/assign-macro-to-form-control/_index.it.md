---
title: Assegna Macro al Controllo Modulo con C++
linktitle: Assegna Macro a Controllo Modulo
type: docs
weight: 60
url: /it/cpp/assign-macro-to-form-control/
description: Impara come assegnare un Codice Macro a un Controllo Modulo come un Pulsante usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells ti consente di assegnare un codice Macro a un Controllo Modulo come un Pulsante. Si prega di utilizzare la proprietà [**Shape.GetMacroName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getmacroname/) per assegnare un nuovo codice Macro a un Controllo Modulo all'interno del workbook.

{{% /alert %}}

Il seguente esempio di codice crea un nuovo workbook, assegna un Codice Macro a un Pulsante di Modulo e salva l’output in formato XLSM. Una volta aperto il file XLSM in Microsoft Excel, vedrai il seguente codice macro.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Assegna Macro al Controllo Modulo in C++**

Qui c'è il codice di esempio per generare il file XLSM di output con il codice Macro.

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
{{< app/cells/assistant language="cpp" >}}
