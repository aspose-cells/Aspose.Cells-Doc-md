---
title: Cómo establecer la propiedad AutoRecover del Libro de trabajo con C++
linktitle: Cómo establecer la propiedad AutoRecover del Libro de trabajo
type: docs
weight: 220
url: /es/cpp/how-to-set-autorecover-property-of-workbook/
description: Aprende cómo habilitar o deshabilitar la propiedad AutoRecover de un libro de trabajo usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Puedes usar Aspose.Cells para establecer la propiedad AutoRecover de un libro de trabajo. El valor predeterminado de esta propiedad es **true**. Cuando lo configuras a **false** en un libro de trabajo, Microsoft Excel deshabilita AutoRecover (Autosave) en ese archivo de Excel.

Aspose.Cells proporciona la propiedad [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getautorecover/) para habilitar o deshabilitar esta opción.

{{% /alert %}}

El siguiente código explica cómo usar la propiedad [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getautorecover/) del libro de trabajo. El código primero lee el valor predeterminado de esta propiedad, que es **true**, luego lo establece en **false** y guarda el libro de trabajo. Luego lee el libro de trabajo nuevamente y obtiene el valor de esta propiedad, que en ese momento es **false**.

## Código C++ para establecer la propiedad AutoRecover del Libro de trabajo

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

    // Create workbook object
    Workbook workbook;

    // Read AutoRecover property
    std::cout << "AutoRecover: " << workbook.GetSettings().GetAutoRecover() << std::endl;

    // Set AutoRecover property to false
    workbook.GetSettings().SetAutoRecover(false);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    // Read the saved workbook again
    Workbook workbook2(outDir + u"output_out.xlsx");

    // Read AutoRecover property
    std::cout << "AutoRecover: " << workbook2.GetSettings().GetAutoRecover() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Salida**

Aquí está la salida en consola del código de muestra anterior.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
