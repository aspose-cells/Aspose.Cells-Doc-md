---
title: Attribuer une macro à un contrôle de formulaire avec C++
linktitle: Attribuer une macro à une commande de formulaire
type: docs
weight: 60
url: /fr/cpp/assign-macro-to-form-control/
description: Apprenez comment attribuer un code macro à un contrôle de formulaire comme un bouton en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells vous permet d'attribuer un code de macro à une Commande de formulaire comme un bouton. Veuillez utiliser la propriété [**Shape.GetMacroName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getmacroname/) pour attribuer un nouveau code de macro à une Commande de formulaire à l'intérieur du classeur.

{{% /alert %}}

Le code d'exemple suivant crée un nouveau classeur, attribue un code macro à un bouton de formulaire, et sauvegarde le résultat au format XLSM. Une fois que vous ouvrez le fichier XLSM dans Microsoft Excel, vous verrez le code macro suivant.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Attribuer une macro à un contrôle de formulaire en C++**

Voici l'exemple de code pour générer le fichier XLSM de sortie avec un code de macro.

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
