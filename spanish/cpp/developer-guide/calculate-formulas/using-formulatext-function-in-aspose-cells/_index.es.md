---
title: Uso de la función FormulaText en Aspose.Cells con C++
linktitle: Uso de la función FormulaText
description: Este artículo introduce cómo utilizar la función FormulaText en la librería Aspose.Cells para procesar fórmulas en Microsoft Excel. Al cargar un archivo de Excel existente o crear uno nuevo, podemos utilizar el método proporcionado por Aspose.Cells para obtener y establecer el texto de la fórmula de la celda y obtener el resultado. Finalmente, guardamos el archivo de Excel modificado en el disco.
keywords: Aspose.Cells, Excel, funciones FormulaText
type: docs
weight: 60
url: /es/cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText es una función de Excel 2013 y posteriores. No es compatible con versiones anteriores como Excel 2010 o 2007, etc. Como su nombre sugiere, imprime el texto de la fórmula que se encuentra en una celda dada. Este artículo te mostrará cómo hacer uso de esta función con Aspose.Cells.

{{% /alert %}} 

El siguiente código de muestra muestra el uso de FormulaText con Aspose.Cells. El código primero escribe una fórmula en la celda A1 y luego imprime el texto de la fórmula usando FormulaText en la celda A2.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some formula in cell A1
    Cell cellA1 = worksheet.GetCells().Get(u"A1");
    cellA1.SetFormula(u"=Sum(B1:B10)");

    // Get the text of the formula in cell A2 using FORMULATEXT function
    Cell cellA2 = worksheet.GetCells().Get(u"A2");
    cellA2.SetFormula(u"=FormulaText(A1)");

    // Calculate the workbook
    workbook.CalculateFormula();

    // Print the results of A2, It will now print the text of the formula inside cell A1
    std::cout << cellA2.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Salida de la consola**
Aquí está la salida en consola del código de muestra anterior.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
