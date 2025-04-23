---
title: ActiveX Control mit C++ entfernen
linktitle: AktiveX Steuerung entfernen
type: docs
weight: 1000
url: /de/cpp/remove-activex-control/
description: Lernen Sie, wie Sie ActiveX Control aus Arbeitsmappen mit Aspose.Cells for C++ entfernen.
---

## **AktiveX-Steuerung entfernen**

Aspose.Cells bietet die Möglichkeit, ActiveX-Steuerelemente aus Arbeitsmappen zu entfernen. Für diese Funktion bietet die API die Methode [**Shape.RemoveActiveXControl**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/removeactivexcontrol/). Das folgende Codebeispiel demonstriert die Verwendung der Methode [**Shape.RemoveActiveXControl**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/removeactivexcontrol/), um ein ActiveX-Steuerelement zu entfernen.

## **Beispielcode**

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
