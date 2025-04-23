---
title: Encuentra la posición absoluta de una forma dentro de la hoja de cálculo con C++
linktitle: Encontrar la posición absoluta de la forma dentro de la hoja de cálculo
type: docs
weight: 8000
url: /es/cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Determina la posición absoluta de una forma en una hoja de cálculo usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A veces, es necesario conocer la posición absoluta de una forma en una hoja de cálculo. Aspose.Cells proporciona las propiedades [**Shape.GetLeftToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlefttocorner/) y [**Shape.GetTopToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettoptocorner/) con este fin. Estas propiedades devuelven la posición absoluta de la forma dentro de la hoja de cálculo en píxeles.

{{% /alert %}}

El siguiente código de ejemplo muestra la posición absoluta de la primera forma en la hoja de cálculo en píxeles. El código de ejemplo muestra la siguiente salida en la consola:

{{< highlight java >}}

Absolute Position of this Shape is (320 , 183)

{{< /highlight >}}

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

    // Load the sample Excel file inside the workbook object
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first shape inside the worksheet
    Shape shape = worksheet.GetShapes().Get(0);

    // Displays the absolute position of the shape
    std::wcout << L"Absolute Position of this Shape is (" << shape.GetLeftToCorner() << L" , " << shape.GetTopToCorner() << L")" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
