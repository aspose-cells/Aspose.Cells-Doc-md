---
title: Ta bort ActiveX kontroll med C++
linktitle: Ta bort ActiveX kontroll
type: docs
weight: 1000
url: /sv/cpp/remove-activex-control/
description: Läs hur du tar bort ActiveX kontroll från arbetsböcker med Aspose.Cells for C++.
---

## **Ta bort ActiveX-kontroll**

Aspose.Cells ger möjlighet att ta bort ActiveX-kontroll från arbetsböcker. För detta tillhandahåller API:n [**Shape.RemoveActiveXControl**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/removeactivexcontrol/)-metoden. Följande kodsnutt demonstrerar användningen av [**Shape.RemoveActiveXControl**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/removeactivexcontrol/)-metoden för att ta bort ActiveX-kontroll.

## **Exempelkod**

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
{{< app/cells/assistant language="cpp" >}}
