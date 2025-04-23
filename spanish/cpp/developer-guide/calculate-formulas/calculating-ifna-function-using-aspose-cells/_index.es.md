---
title: Calcular la función IFNA usando Aspose.Cells con C++
linktitle: Calcular la función IFNA
description: Cómo calcular funciones IFNA usando la biblioteca Aspose.Cells con C++. Al cargar un archivo de Excel existente o crear uno nuevo, podemos usar los métodos proporcionados por Aspose.Cells para calcular la función IFNA y obtener el resultado. Finalmente, guardamos el archivo de Excel modificado en disco.
keywords: Aspose.Cells, Excel, funciones IFNA, cálculos, C++
type: docs
weight: 40
url: /es/cpp/calculating-ifna-function-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells soporta el cálculo de la función Excel IFNA. La función IFNA devuelve el valor que especifica si la fórmula devuelve el valor de error #N/A; de lo contrario, devuelve el resultado de la fórmula.

{{% /alert %}} 

## **Cálculo de la función IFNA utilizando Aspose.Cells**
El siguiente código de ejemplo ilustra el cálculo de la función IFNA por Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create new workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add data for VLOOKUP
    worksheet.GetCells().Get(u"A1").PutValue(u"Apple");
    worksheet.GetCells().Get(u"A2").PutValue(u"Orange");
    worksheet.GetCells().Get(u"A3").PutValue(u"Banana");

    // Access cell A5 and A6
    Cell cellA5 = worksheet.GetCells().Get(u"A5");
    Cell cellA6 = worksheet.GetCells().Get(u"A6");

    // Assign IFNA formula to A5 and A6
    cellA5.SetFormula(u"=IFNA(VLOOKUP(\"Pear\",$A$1:$A$3,1,0),\"Not found\")");
    cellA6.SetFormula(u"=IFNA(VLOOKUP(\"Orange\",$A$1:$A$3,1,0),\"Not found\")");

    // Calculate the formula of workbook
    workbook.CalculateFormula();

    // Print the values of A5 and A6
    std::cout << cellA5.GetStringValue().ToUtf8() << std::endl;
    std::cout << cellA6.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Salida de la consola**
Aquí está la salida en consola del código de muestra anterior.

{{< highlight java >}}

Not found

Orange

{{< /highlight >}}
