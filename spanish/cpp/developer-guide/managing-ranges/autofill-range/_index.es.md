---
title: AutoRellenar rango de archivos de Excel con C++
linktitle: AutoRellenar Rango
type: docs
weight: 105
url: /es/cpp/autofill-ranges/
description: Aprenda cómo realizar una operación de autorrelleno en un rango especificado de un archivo de Excel usando Aspose.Cells con C++.
---

## **Realizar un AutoLlenado en el rango especificado en Excel**

En Excel, selecciona un rango, mueve el ratón a la esquina inferior derecha y arrastra el "+" para autocompletar los datos.

## **Rellenar Rangos con Aspose.Cells**

El siguiente ejemplo muestra cómo realizar una operación de AutoLlenado en un rango. Aquí está el archivo de muestra que se puede descargar para probar esta función:

[range_autofill.xlsx](range_autofill.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook(u"range_autofill.xlsx");

    // Get Cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Create Range
    Range src = cells.CreateRange(u"C3:C4");
    Range dest = cells.CreateRange(u"C5:C10");

    // AutoFill
    src.AutoFill(dest, AutoFillType::Series);

    // Save the Workbook
    workbook.Save(u"range_autofill_result.xlsx");

    std::cout << "Range auto-filled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
