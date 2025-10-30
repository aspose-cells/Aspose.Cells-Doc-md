---
title: Schatten der Texteffekte von Form oder Textbox mit C++ einstellen
linktitle: Schatten der Texteffekte einstellen
type: docs
weight: 250
url: /de/cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: Lernen Sie, wie man den Schatten der Texteffekte für Formen oder Textboxen mit Aspose.Cells for C++ einstellt.
---

{{% alert color="primary" %}}

Sie können den **Schatten** der **Texts-Effekte** jeder Form oder Textbox einstellen. Bitte verwenden Sie die [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/)-Eigenschaft. Diese stellt die Einstellung des Textes der Form dar und gibt [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/)-Objekte zurück. Nachdem Sie darauf zugegriffen haben, stellen Sie bitte den **Schatten** über die [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/)-Eigenschaft ein. Diese Eigenschaft ist vom Typ [**PresetShadowType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/presetshadowtype/) und hat mehrere Werte, darunter:

- OffsetDiagonal-unten-rechts
- OffsetBottom
- OffsetDiagonal-oben-rechts
- Innen-links
- Innen-mitte
- PerspektiveDiagonalObenLinks
- PerspektiveDiagonalUntenRechts

{{% /alert %}}

Das folgende Codesnippet zeigt die Verwendung der [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/)-Eigenschaft zum Festlegen des Schattens der Texteffekte von Shape oder TextBox.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add text box with these dimensions
    TextBox tb = ws.GetShapes().AddTextBox(2, 0, 2, 0, 100, 400);

    // Set the text of the textbox
    tb.SetText(u"This text has the following settings.\n\nText Effects > Shadow > Offset Bottom");

    // Set all the text runs shadow to preset offset bottom
    for (int i = 0; i < tb.GetTextBody().GetCount(); i++)
    {
        tb.GetTextBody().Get(i).GetTextOptions().GetShadow().SetPresetType(PresetShadowType::OffsetBottom);
    }

    // Set the font color and size of the textbox
    tb.GetFont().SetColor(Color::Red());
    tb.GetFont().SetSize(16);

    // Save the output file
    wb.Save(outDir + u"outputSettingTextEffectsShadowOfShapeOrTextbox.xlsx", SaveFormat::Xlsx);

    std::cout << "Text effects shadow of shape or textbox set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
