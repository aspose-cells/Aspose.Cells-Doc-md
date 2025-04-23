---
title: Eliminar control ActiveX con C++
linktitle: Eliminar Control ActiveX
type: docs
weight: 1000
url: /es/cpp/remove-activex-control/
description: Aprenda cómo eliminar controles ActiveX de libros de trabajo usando Aspose.Cells for C++.
---

## **Eliminar control ActiveX**

Aspose.Cells proporciona la capacidad de eliminar controles ActiveX de libros de trabajo. Para ello, la API ofrece el método [**Shape.RemoveActiveXControl**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/removeactivexcontrol/). El siguiente fragmento de código demuestra el uso del método [**Shape.RemoveActiveXControl**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/removeactivexcontrol/) para eliminar un control ActiveX.

## **Código de muestra**

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
