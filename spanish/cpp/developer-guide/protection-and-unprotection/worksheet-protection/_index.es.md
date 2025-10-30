---
title: Proteger y desbloquear la hoja de cálculo con C++
linktitle: Proteger y Desproteger Hoja de Cálculo
type: docs
weight: 40
url: /es/cpp/protect-and-unprotect-worksheets/
description: Proteger y desbloquear la hoja de cálculo de archivos de Excel con Aspose.Cells for C++.
---

{{% alert color="primary" %}}
Para evitar que otros usuarios cambien, muevan o eliminen datos en una hoja de cálculo de forma accidental o deliberada, puede bloquear las celdas en su hoja de cálculo de Excel y luego proteger la hoja con una contraseña. 
{{% /alert %}}

## **Proteger y desbloquear la hoja en MS Excel**

**![proteger y desproteger Hoja de Cálculo](protect-and-unprotect-worksheet.png)**

1. Haga clic en **Revisar > Proteger Hoja**.
1. Ingrese una contraseña en **el cuadro de Contraseña**.
1. Seleccione las opciones de **permitir**.
1. Seleccione **Aceptar**, vuelva a ingresar la contraseña para confirmarla y luego seleccione **Aceptar** nuevamente.

## **Proteger hoja usando Aspose.Cells for C++**
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

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Protect contents of the worksheet
    sheet.Protect(ProtectionType::Contents);

    // Protect worksheet with password
    sheet.GetProtection().SetPassword(u"test");

    // Save as Excel file
    workbook.Save(u"Book1.xlsx");

    std::cout << "Workbook created and protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Desproteger hoja usando Aspose.Cells for C++**
Desproteger la hoja de cálculo es fácil con la API de Aspose.Cells. Si la hoja de cálculo está protegida con contraseña, se requiere una contraseña correcta.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Unprotect the worksheet with password
    sheet.Unprotect(u"password");

    // Save the workbook
    workbook.Save(u"Book1.xlsx");

    std::cout << "Worksheet unprotected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Temas avanzados**
- [Configuración de Protección Avanzada desde Excel XP](/cells/es/cpp/advanced-protection-settings-since-excel-xp/)
- [Detectar si la hoja de cálculo está protegida con contraseña](/cells/es/cpp/detect-if-worksheet-is-password-protected/)
- [Protección de Hojas de Cálculo](/cells/es/cpp/protecting-worksheets/)
- [Desproteger una Hoja de Cálculo](/cells/es/cpp/unprotect-a-worksheet/)
- [Verificar la Contraseña Utilizada para Proteger la Hoja de Cálculo](/cells/es/cpp/verify-password-used-to-protect-the-worksheet/)
{{< app/cells/assistant language="cpp" >}}
