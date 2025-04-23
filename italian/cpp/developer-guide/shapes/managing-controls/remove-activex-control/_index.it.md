---
title: Rimuovi il controllo ActiveX con C++
linktitle: Rimuovi controllo ActiveX
type: docs
weight: 1000
url: /it/cpp/remove-activex-control/
description: Impara come rimuovere il controllo ActiveX dai fogli di lavoro usando Aspose.Cells for C++.
---

## **Rimuovi controllo ActiveX**

Aspose.Cells fornisce la possibilità di rimuovere il controllo ActiveX dai workbook. Per farlo, l'API offre il metodo [**Shape.RemoveActiveXControl**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/removeactivexcontrol/). Il seguente esempio di codice dimostra l'uso del metodo [**Shape.RemoveActiveXControl**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/removeactivexcontrol/) per rimuovere il controllo ActiveX.

## **Codice di Esempio**

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
