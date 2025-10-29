---
title: Удалить элемент ActiveX с помощью C++
linktitle: Удалить элемент управления ActiveX
type: docs
weight: 1000
url: /ru/cpp/remove-activex-control/
description: Узнайте, как удалять элементы ActiveX из рабочих книг с помощью Aspose.Cells for C++.
---

## **Удалить элемент управления ActiveX**

Aspose.Cells предоставляет возможность удалять элементы ActiveX из рабочих книг. Для этого API имеет метод [**Shape.RemoveActiveXControl**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/removeactivexcontrol/). Следующий код демонстрирует использование метода [**Shape.RemoveActiveXControl**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/removeactivexcontrol/) для удаления элемента ActiveX.

## **Образец кода**

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
