---
title: Makro einer Formularsteuerung mit C++ zuweisen
linktitle: Weisen Sie einem Formularsteuerelement einen Makrocode zu.
type: docs
weight: 60
url: /de/cpp/assign-macro-to-form-control/
description: Erfahren Sie, wie Sie einen Makro Code einer Formularsteuerung wie einer Schaltfläche mit Aspose.Cells for C++ zuweisen.
---

{{% alert color="primary" %}}

Mit Aspose.Cells können Sie einem Formularsteuerelement wie einer Schaltfläche einen Makrocode zuweisen. Verwenden Sie die Eigenschaft [**Shape.GetMacroName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getmacroname/), um einem Formularsteuerelement in der Arbeitsmappe einen neuen Makrocode zuzuweisen.

{{% /alert %}}

Der folgende Beispielcode erstellt eine neue Arbeitsmappe, weist einer Formularschaltfläche einen Makro-Code zu und speichert die Ausgabe im XLSM-Format. Sobald Sie die ausgegebene XLSM-Datei in Microsoft Excel öffnen, sehen Sie den folgenden Makro-Code.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Makro zu Formularsteuerung in C++ zuweisen**

Hier ist der Beispielcode zum Generieren der Ausgabedatei XLSM mit Makrocode.

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
