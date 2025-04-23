---
title: Detectar si una hoja de cálculo está protegida por contraseña con C++
linktitle: Detectar si la hoja de cálculo está protegida con contraseña
type: docs
weight: 360
url: /es/cpp/detect-if-worksheet-is-password-protected/
description: Aprenda cómo detectar si una hoja de cálculo está protegida con contraseña usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Es posible proteger los libros de trabajo y las hojas de cálculo por separado. Por ejemplo, una hoja de cálculo puede contener una o más hojas protegidas por contraseña, sin embargo, el libro de trabajo en sí puede o no estar protegido. Las API de Aspose.Cells proporcionan los medios para detectar si una hoja de cálculo dada está protegida por contraseña o no. Este artículo demuestra el uso de la API Aspose.Cells for C++ para lograrlo.

{{% /alert %}}

Aspose.Cells for C++ ha expuesto la propiedad [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) para detectar si una hoja de cálculo está protegida por contraseña o no. La propiedad Booleana [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) devuelve **true** si [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) está protegida por contraseña y **false** si no.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load a spreadsheet
    Workbook book(srcDir + u"sample.xlsx");

    // Access the protected Worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Check if Worksheet is password protected
    if (sheet.GetProtection().IsProtectedWithPassword())
    {
        std::cout << "Worksheet is password protected" << std::endl;
    }
    else
    {
        std::cout << "Worksheet is not password protected" << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
