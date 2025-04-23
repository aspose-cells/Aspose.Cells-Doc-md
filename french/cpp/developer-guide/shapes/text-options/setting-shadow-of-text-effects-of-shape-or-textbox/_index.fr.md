---
title: Définir l ombre des effets de texte de la forme ou de la zone de texte avec C++
linktitle: Définir l ombre des effets de texte
type: docs
weight: 250
url: /fr/cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: Apprenez comment définir l ombre des effets de texte pour les formes ou les zones de texte en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Vous pouvez définir la **Ombre** des **Effets de texte** de n'importe quelle forme ou zone de texte. Veuillez utiliser la propriété [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/). Elle présente le réglage du texte de la forme et retourne des objets [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/). Après y avoir accédé, veuillez définir la **Ombre** via la propriété [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/). Cette propriété est de type [**PresetShadowType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/presetshadowtype/) qui a plusieurs valeurs. Certaines sont :

- DécalageDiagonaleInférieureDroite
- DécalageBas
- DécalageDiagonaleSupérieureDroite
- ÀL'intérieurGauche
- ÀL'IntérieurCentre
- DiagonalePerspectiveSupérieureGauche
- DiagonalePerspectiveInférieureDroite

{{% /alert %}}

Le snippet de code suivant démontre l'utilisation de la propriété [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/) pour définir l'ombre des effets de texte de la forme ou zone de texte.

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
