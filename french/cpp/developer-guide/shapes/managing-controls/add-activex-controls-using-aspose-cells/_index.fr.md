---
title: Ajouter des contrôles ActiveX en utilisant Aspose.Cells avec C++
linktitle: Ajouter des contrôles ActiveX
type: docs
weight: 260
url: /fr/cpp/add-activex-controls-using-aspose-cells/
description: Apprenez comment ajouter des contrôles ActiveX aux feuilles de calcul Excel de manière programmatique en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Vous pouvez ajouter des contrôles ActiveX avec Aspose.Cells en utilisant la méthode [**ShapeCollection::AddActiveXControl()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addactivexcontrol/). Cette méthode prend un paramètre [**ControlType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/) qui spécifie le type de contrôle ActiveX à ajouter dans une feuille de calcul. Les valeurs suivantes sont disponibles :

- ControlType::CheckBox
- ControlType::ComboBox
- ControlType::CommandButton
- ControlType::Image
- ControlType::Label
- ControlType::ListBox
- ControlType::RadioButton
- ControlType::ScrollBar
- ControlType::SpinButton
- ControlType::TextBox
- ControlType::ToggleButton
- ControlType::Inconnu

Une fois que vous avez ajouté le contrôle ActiveX dans la collection de formes, vous pouvez accéder à l'objet contrôle ActiveX via la méthode [**Shape::get_ActiveXControl()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getactivexcontrol/) et définir ses diverses propriétés.

{{% /alert %}}

Le code d'exemple suivant ajoute un contrôle ActiveX de bouton bascule en utilisant Aspose.Cells for C++.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Drawing::ActiveXControls;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Add Toggle Button ActiveX Control inside the Shape Collection
    Shape s = sheet.GetShapes().AddActiveXControl(ControlType::ToggleButton, 4, 0, 4, 0, 100, 30);

    // Access the ActiveX control object and set its linked cell property
    ActiveXControl c = s.GetActiveXControl();
    c.SetLinkedCell(u"A1");

    // Save the workbook in xlsx format
    wb.Save(outDir + u"AddActiveXControls_out.xlsx", SaveFormat::Xlsx);

    std::cout << "ActiveX control added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
