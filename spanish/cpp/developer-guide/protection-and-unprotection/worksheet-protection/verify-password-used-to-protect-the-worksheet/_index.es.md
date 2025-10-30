---
title: Verificar la contraseña utilizada para proteger la hoja con C++
linktitle: Verificar la contraseña utilizada para proteger la hoja de cálculo
type: docs
weight: 370
url: /es/cpp/verify-password-used-to-protect-the-worksheet/
description: Aprenda cómo verificar la contraseña utilizada para proteger una hoja de cálculo usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Las API de Aspose.Cells han mejorado la clase [**Protection**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/) al introducir algunas propiedades y métodos útiles. Uno de estos métodos es [**VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/), que permite especificar una contraseña como una instancia de *string* y verificar si la misma contraseña se ha utilizado para proteger la [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

{{% /alert %}}

El método [**Protection.VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) devuelve **true** si la contraseña especificada coincide con la contraseña utilizada para proteger la hoja dada y **false** si no coincide. El siguiente fragmento de código usa el método [**Protection.VerifyPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/verifypassword/) junto con la propiedad [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) para detectar la protección con contraseña y verificar la contraseña.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load a spreadsheet
    Workbook book(srcDir + u"Sample.xlsx");

    // Access the protected Worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Check if Worksheet is password protected
    if (sheet.GetProtection().IsProtectedWithPassword())
    {
        // Verify the password used to protect the Worksheet
        if (sheet.GetProtection().VerifyPassword(u"1234"))
        {
            std::cout << "Specified password has matched" << std::endl;
        }
        else
        {
            std::cout << "Specified password has not matched" << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
