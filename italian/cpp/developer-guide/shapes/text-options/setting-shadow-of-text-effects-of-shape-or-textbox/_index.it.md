---
title: Impostare l’ombra degli effetti di testo di forma o casella di testo con C++
linktitle: Impostare l’ombra degli effetti di testo
type: docs
weight: 250
url: /it/cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: Impara come impostare l’ombra degli effetti di testo per forme o caselle di testo usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Puoi impostare l’**Ombra** degli **Effetti di testo** di qualsiasi forma o casella di testo. Usa la proprietà [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/). Essa rappresenta la configurazione del testo della forma e restituisce oggetti [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/). Dopo averla accessata, imposta l’**Ombra** tramite la proprietà [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/). Questa proprietà è di tipo [**PresetShadowType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/presetshadowtype/) e può avere diversi valori. Alcuni di questi sono:

- DiagonaleOffsetInferioreDestra
- OffsetInferiore
- DiagonaleOffsetSuperioreDestra
- SinistraInterno
- CentroInterno
- DiagonaleSuperioreSinistraProspettiva
- DiagonaleInferioreDestraProspettiva

{{% /alert %}}

Il seguente frammento di codice dimostra l'uso della proprietà [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/) per impostare l'ombra sugli effetti di testo di Forma o Casella di Testo.

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
