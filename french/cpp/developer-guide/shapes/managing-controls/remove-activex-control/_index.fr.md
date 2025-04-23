---
title: Supprimer le contrôle ActiveX avec C++
linktitle: Supprimer le contrôle ActiveX
type: docs
weight: 1000
url: /fr/cpp/remove-activex-control/
description: Apprenez comment supprimer un contrôle ActiveX des classeurs en utilisant Aspose.Cells for C++.
---

## **Supprimer le contrôle ActiveX**

Aspose.Cells offre la possibilité de supprimer un contrôle ActiveX des classeurs. Pour cela, l'API fournit la méthode [**Shape.RemoveActiveXControl**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/removeactivexcontrol/). L'extrait de code suivant démontre l'utilisation de la méthode [**Shape.RemoveActiveXControl**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/removeactivexcontrol/) pour supprimer un contrôle ActiveX.

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook
    Workbook wb(srcDir + u"sampleUpdateActiveXComboBoxControl.xlsx");

    // Access first shape from first worksheet
    Shape shape = wb.GetWorksheets().Get(0).GetShapes().Get(0);

    // Remove Shape ActiveX Control
    shape.RemoveActiveXControl();

    // Save the workbook
    wb.Save(outDir + u"RemoveActiveXControl_out.xlsx");

    std::cout << "ActiveX Control removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
