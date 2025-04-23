---
title: Configuración de sombra de efectos de texto de forma o cuadro de texto con C++
linktitle: Configuración de sombra de efectos de texto
type: docs
weight: 250
url: /es/cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: Aprenda cómo configurar la sombra de efectos de texto para formas o cuadros de texto usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Puede configurar la **Sombra** de los **Efectos de texto** de cualquier forma o cuadro de texto. Por favor, utilice la propiedad [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/). Esta presenta la configuración del texto de la forma y devuelve objetos [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/). Después de acceder a ella, configure la **Sombra** a través de la propiedad [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/). Esta propiedad es del tipo [**PresetShadowType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/presetshadowtype/) y tiene varios valores. Algunos de estos son:

- Diagonal inferior derecha
- Inferior
- Diagonal superior derecha
- Interior izquierdo
- Centro interior
PerspectiveDiagonalUpperLeft
PerspectiveDiagonalLowerRight

{{% /alert %}}

El siguiente fragmento de código demuestra el uso de la propiedad [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/) para establecer la sombra de efectos de texto de Forma o Cuadro de texto.

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
