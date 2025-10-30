---
title: Especificar filas máximas de fórmula compartida con C++
linktitle: Especificar el número máximo de filas de la fórmula compartida
type: docs
weight: 40
url: /es/cpp/specify-maximum-rows-of-shared-formula/
description: Aprenda cómo especificar las filas máximas de una fórmula compartida en archivos de Excel usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

El máximo predeterminado de filas de la fórmula compartida es 64. Puede ser cualquier número, por ejemplo, 1000. El rendimiento de la fórmula compartida cambia con un número diferente de filas. Por lo tanto, Aspose.Cells proporciona la propiedad [**GetMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrowsofsharedformula/) que se puede usar para especificar el máximo de filas de la fórmula compartida. La fórmula compartida se dividirá en varias fórmulas compartidas si el total de filas de la fórmula compartida es mayor que ese número, como se muestra en la siguiente captura de pantalla.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Especificar el número máximo de filas de la fórmula compartida**

El siguiente código de ejemplo explica el uso de la propiedad [**GetMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrowsofsharedformula/). Establece el máximo de filas de la fórmula compartida en 5 y añade la fórmula compartida en la celda D1 para 100 filas y guarda en [archivo de Excel de salida](61767856.xlsx). Si extrae el contenido del archivo de Excel de salida y consulta el *sheet1.xml*, verá que la fórmula compartida se divide después de cada 5 filas, como se destaca en la captura de pantalla anterior.

## **Código de muestra**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook wb;

    // Set the max rows of shared formula to 5
    wb.GetSettings().SetMaxRowsOfSharedFormula(5);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell D1
    Cell cell = ws.GetCells().Get(u"D1");

    // Set the shared formula in 100 rows
    cell.SetSharedFormula(u"=Sum(A1:A2)", 100, 1);

    // Save the output Excel file
    wb.Save(u"outputSpecifyMaximumRowsOfSharedFormula.xlsx");

    std::cout << "Shared formula set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
