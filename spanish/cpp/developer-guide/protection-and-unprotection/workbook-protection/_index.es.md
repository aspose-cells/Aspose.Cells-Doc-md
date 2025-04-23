---
title: Protege y desbloquea la estructura del libro con C++
linktitle: Proteger y desproteger la estructura del libro
type: docs
weight: 40
url: /es/cpp/protect-and-unprotect-workbook-structure/
description: Protege y desbloquea la estructura del libro en archivos de Excel usando C++ con Aspose.Cells.
---

{{% alert color="primary" %}}
Para evitar que otros usuarios vean hojas de cálculo ocultas, agreguen, muevan, eliminen u oculten hojas de cálculo, y cambien el nombre de las hojas de cálculo, puede proteger la estructura de su libro de Excel con una contraseña.
{{% /alert %}}

## **Proteger y desbloquear la estructura del libro en MS Excel**

**![proteger y desproteger la estructura del libro](proteger-y-desproteger-la-estructura-del-libro.png)**

1. Haga clic en **Revisar > Proteger libro**.
1. Ingrese una contraseña en **el cuadro de Contraseña**.
1. Seleccione **Aceptar**, vuelva a ingresar la contraseña para confirmarla y luego seleccione **Aceptar** nuevamente.

## **Proteger estructura del libro usando Aspose.Cells for C++**
Solo necesitas las siguientes líneas de código simples para implementar la protección de la estructura del libro de trabajo de archivos de Excel.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Protect workbook structure with a password
    workbook.Protect(ProtectionType::Structure, u"password");

    // Save the workbook to a file
    workbook.Save(u"Book1.xlsx");

    std::cout << "Workbook created and protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Desproteger estructura del libro usando Aspose.Cells for C++**
Desproteger la estructura del libro es fácil con la API de Aspose.Cells.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Open an Excel file which workbook structure is protected.
    U16String inputFilePath = u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Unprotect workbook structure.
    workbook.Unprotect(u"password");

    // Save Excel file.
    workbook.Save(inputFilePath);

    std::cout << "Workbook structure unprotected and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}
Nota: se requiere una contraseña correcta.
{{% /alert %}}
