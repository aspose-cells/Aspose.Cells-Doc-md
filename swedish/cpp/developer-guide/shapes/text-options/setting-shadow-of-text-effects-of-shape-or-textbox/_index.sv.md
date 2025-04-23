---
title: Ställ in skugga för textstilar på form eller textruta med C++
linktitle: Ställ in skugga för textstilar
type: docs
weight: 250
url: /sv/cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: Lär dig hur man ställer in skuggan för textstilar för former eller textrutor med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Du kan ställa in **Skugga** för **Textstilar** på vilken form eller textruta som helst. Använd [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/)-egenskapen. Den visar inställningen för formens text och returnerar [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/)-objekt. Efter att ha fått åtkomst till den, ställ sedan in **Skugga** via [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/)-egenskapen. Denna egenskap är av typen [**PresetShadowType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/presetshadowtype/) och har flera värden. Några av dessa är:

- OffsetDiagonalBottomRight
- OffsetBottom
- OffsetDiagonalTopRight
- InsideLeft
- InsideCenter
- PerspectiveDiagonalUpperLeft
- PerspectiveDiagonalLowerRight

{{% /alert %}}

Följande kodexempel demonstrerar användningen av [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/)-egenskapen för att ställa in skuggan för textstilar på form eller textruta.

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
