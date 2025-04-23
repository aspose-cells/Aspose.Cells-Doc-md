---
title: Implementación de Rangos no secuenciales con C++
linktitle: Implementando rangos no secuenciales
type: docs
weight: 700
url: /es/cpp/implementing-non-sequential-ranges/
description: Aprenda cómo crear rangos con nombre con celdas no adyacentes usando Aspose.Cells con C++.
---

{{% alert color="primary" %}} 

Normalmente, los rangos con nombre son rectangulares con celdas continuas y adyacentes entre sí. Pero a veces, es posible que necesite usar un rango de celdas no secuencial en el que las celdas no sean adyacentes. Aspose.Cells admite la creación de un rango con nombre con celdas no adyacentes.

{{% /alert %}} 

El ejemplo de código a continuación muestra cómo crear un rango no secuencial con Aspose.Cells for C++.

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

    // Create a new workbook
    Workbook workbook;

    // Adding a Name for non sequenced range
    int index = workbook.GetWorksheets().GetNames().Add(u"NonSequencedRange");

    // Get the added name
    Name name = workbook.GetWorksheets().GetNames().Get(index);

    // Creating a non sequence range of cells
    name.SetRefersTo(u"=Sheet1!$A$1:$B$3,Sheet1!$D$5:$E$6");

    // Save the workbook
    workbook.Save(outDir + u"Output.out.xlsx");

    std::cout << "Workbook saved successfully with non-sequenced range!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
