---
title: Eliminar filas duplicadas en una hoja de cálculo con C++
linktitle: Eliminar filas duplicadas en una hoja de cálculo
type: docs
weight: 370
url: /es/cpp/remove-duplicate-rows-in-a-worksheet/
description: Aprenda cómo eliminar filas duplicadas en una hoja de cálculo usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Eliminar filas duplicadas es una de las muchas funciones útiles de Microsoft Excel. Permite a los usuarios eliminar filas duplicadas en una hoja de cálculo, y puede seleccionar qué columnas deben verificarse para información duplicada.

Aspose.Cells proporciona el método `Cells::RemoveDuplicates()` para este propósito. También puede configurar `startRow`, `startColumn`, `endRow` y `endColumn` para seleccionar columnas.

A continuación se muestran los archivos de muestra que se pueden descargar para probar esta característica:

[removeduplicates.xlsx](removeduplicates.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook book(u"removeduplicates.xlsx");

    // Remove duplicates from the first worksheet
    book.GetWorksheets().Get(0).GetCells().RemoveDuplicates(0, 0, 5, 3);

    // Save the result
    book.Save(u"removeduplicates-result.xlsx");

    std::cout << "Duplicates removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% /alert %}}
