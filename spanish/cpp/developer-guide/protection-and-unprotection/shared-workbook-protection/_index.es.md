---
title: Protege o desbloquea el libro compartido con C++
linktitle: Proteger o Quitar Protección al Libro de Trabajo Compartido
type: docs
weight: 10
url: /es/cpp/password-protect-or-unprotect-the-shared-workbook/
description: Aprende cómo proteger o desbloquear un libro compartido usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Puedes proteger o quitar la protección al libro de trabajo compartido con Microsoft Excel como se muestra en la siguiente captura de pantalla. Aspose.Cells también ofrece esta función con los métodos [**Workbook::ProtectSharedWorkbook()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/protectsharedworkbook/) y [**Workbook::UnprotectSharedWorkbook()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/unprotectsharedworkbook/).

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **Proteger o Quitar Protección al Libro de Trabajo Compartido**

El siguiente código de ejemplo crea un libro de trabajo y lo protege mientras habilita el uso compartido y lo guarda como [archivo de Excel de salida](55541777.xlsx). La captura de pantalla muestra que cuando intentas quitar la protección, Microsoft Excel te pedirá que ingreses la contraseña para quitarla.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create empty Excel file
    Workbook wb;

    // Protect the Shared Workbook with Password
    wb.ProtectSharedWorkbook(u"1234");

    // Uncomment this line to Unprotect the Shared Workbook
    // wb.UnprotectSharedWorkbook(u"1234");

    // Save the output Excel file
    wb.Save(u"outputProtectSharedWorkbook.xlsx");

    std::cout << "Shared workbook protection applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
