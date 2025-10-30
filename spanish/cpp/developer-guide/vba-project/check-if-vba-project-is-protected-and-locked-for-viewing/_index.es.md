---
title: Verifica si el proyecto VBA está protegido y bloqueado para vista con C++
linktitle: Verifique si el Proyecto VBA está Protegido y Bloqueado para Visualización
type: docs
weight: 30
url: /es/cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Aprende cómo verificar si el Proyecto VBA está protegido y bloqueado para vista en archivos Excel usando Aspose.Cells for C++.
---

## Verifica si el Proyecto VBA está protegido y bloqueado para vista en C++

Aspose.Cells permite verificar si el proyecto VBA (Visual Basic for Applications) de un archivo de Excel está protegido y bloqueado para visualización. Para ello, la API proporciona la propiedad [**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/). Si está bloqueado para visualización, entonces la propiedad [**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/) devuelve **true**.

## **Código de muestra**

El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](43352065.xlsm) y verifica si el Proyecto VBA (Visual Basic para Aplicaciones) del archivo está protegido y bloqueado para vista. También consulta su Salida en Consola como referencia.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Vba;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleCheckifVBAProjectisProtected.xlsm";

    // Load your source Excel file
    Workbook wb(inputFilePath);

    // Access the VBA project of the workbook
    VbaProject vbaProject = wb.GetVbaProject();

    // Check if "Lock project for viewing" is true or not
    std::cout << "Is VBA Project Locked for Viewing: " << vbaProject.GetIslockedForViewing() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Salida de la consola**

Esta es la salida de consola del código de muestra anterior cuando se ejecuta con el [archivo de Excel de muestra](43352065.xlsm) proporcionado.

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
