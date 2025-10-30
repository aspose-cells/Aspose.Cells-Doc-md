---  
title: Descubra si el Proyecto VBA está Protegido con C++  
linktitle: Descubrir si el Proyecto VBA está Protegido  
type: docs  
weight: 20  
url: /es/cpp/find-out-if-vba-project-is-protected/  
description: Verifique si el proyecto VBA de un archivo de Excel está protegido usando Aspose.Cells con C++.  
---  

## **Descubra si el Proyecto VBA está protegido en C++**

Puede verificar si el proyecto VBA (Visual Basic for Applications) de su archivo de Excel está protegido o no usando Aspose.Cells y la propiedad [**VbaProject.IsProtected**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isprotected/).

## **Código de muestra**

El siguiente código de muestra crea un libro de trabajo y luego verifica si su proyecto VBA está protegido o no. Luego protege el proyecto VBA y vuelve a verificar si está protegido o no. Consulte la salida de la consola para referencia. Antes de la protección, [**VbaProject.IsProtected**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isprotected/) devuelve **false** pero después de la protección, devuelve **true**.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a workbook.
    Workbook wb;

    // Access the VBA project of the workbook.
    VbaProject vbaProj = wb.GetVbaProject();

    // Check if VBA Project is Protected using IsProtected method.
    std::wcout << L"IsProtected - Before Protecting VBA Project: " << (vbaProj.IsProtected() ? L"True" : L"False") << std::endl;

    // Protect the VBA project.
    vbaProj.Protect(true, u"11");

    // Check if VBA Project is Protected using IsProtected method.
    std::wcout << L"IsProtected - After Protecting VBA Project: " << (vbaProj.IsProtected() ? L"True" : L"False") << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Salida de la consola**

Esta es la salida en consola del código de muestra anterior como referencia.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}  
{{< app/cells/assistant language="cpp" >}}
