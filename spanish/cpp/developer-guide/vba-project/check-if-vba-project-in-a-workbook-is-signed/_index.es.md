---
title: Verifica si el proyecto VBA en un libro de trabajo está firmado con C++
linktitle: Verifique si el proyecto VBA en un Libro de Trabajo está firmado
type: docs
weight: 70
url: /es/cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Verifica si el proyecto VBA en un libro de trabajo está firmado usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Puedes verificar si tu proyecto VBA está firmado o no usando Microsoft Excel a través del comando del menú **Herramientas > Firmas digitales...**. De manera similar, puedes verificarlo programáticamente usando Aspose.Cells [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned).

{{% /alert %}}

## **Verifica si el proyecto VBA en un libro de trabajo está firmado en C++**

El siguiente código carga el libro de trabajo y verifica si su proyecto VBA está firmado usando la propiedad [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned). La propiedad devolverá **true** si el proyecto está firmado, de lo contrario devolverá **false**.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String sampleFilePath = srcDir + u"Sample1.xlsx";

    // Create workbook
    Workbook workbook(sampleFilePath);

    // Check if the VBA project is signed
    bool isSigned = workbook.GetVbaProject().IsSigned();
    std::wcout << u"VBA Project is Signed: " << (isSigned ? u"true" : u"false") << std::endl;

    Aspose::Cells::Cleanup();
}
```
