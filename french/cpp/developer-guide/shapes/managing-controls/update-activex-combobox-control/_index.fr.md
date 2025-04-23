---
title: Mettre à jour le contrôle ComboBox ActiveX avec C++
linktitle: Mettre à jour le contrôle ComboBox ActiveX
type: docs
weight: 170
url: /fr/cpp/update-activex-combobox-control/
description: Apprenez comment lire ou écrire les valeurs du contrôle ComboBox ActiveX en utilisant Aspose.Cells avec C++.
---

## **Scénarios d'utilisation possibles**
Vous pouvez lire ou écrire les valeurs du contrôle ComboBox ActiveX en utilisant Aspose.Cells. Accédez au contrôle ActiveX via la propriété [Shape.ActiveXControl](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/activexcontrol/) et vérifiez son type via la propriété [ActiveXControl.GetType()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/activexcontrolbase/gettype/). Il doit retourner une valeur [ControlType.ComboBox](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/), puis cast-le en un objet [ComboBoxActiveXControl](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol/) pour lire ou modifier ses diverses propriétés.

Veuillez télécharger le [fichier Excel exemple](5115124.xlsx) utilisé dans le code d'exemple suivant.

## **Mise à jour du contrôle ComboBox ActiveX**
La capture d'écran suivante montre l'effet du code d'exemple sur le [fichier Excel d'exemple](5115124.xlsx). Comme vous pouvez le constater, la valeur de la boîte combinée ActiveX a été mise à jour pour "Il s'agit d'un contrôle de boîte combinée".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |

## **Code d'exemple**
Le code d'exemple suivant met à jour la valeur du contrôle Boîte combi ActiveX présent dans le [fichier Excel d'exemple](5115124.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Drawing::ActiveXControls;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"SourceFile.xlsx");

    Shape shape = wb.GetWorksheets().Get(0).GetShapes().Get(0);

    ActiveXControl c = shape.GetActiveXControl();

    if (c.GetType() == ControlType::ComboBox)
    {
        ComboBoxActiveXControl comboBoxActiveX = static_cast<ComboBoxActiveXControl>(c);
        comboBoxActiveX.SetValue(u"This is combo box control with updated value.");
    }

    wb.Save(outDir + u"OutputFile_out.xlsx");

    std::cout << "Workbook saved successfully with updated ComboBox value!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
