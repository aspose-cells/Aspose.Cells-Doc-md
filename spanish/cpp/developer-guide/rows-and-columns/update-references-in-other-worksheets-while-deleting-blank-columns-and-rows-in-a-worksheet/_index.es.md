---
title: Actualizar referencias en otras hojas de cálculo mientras elimina columnas y filas en blanco en una hoja de cálculo con C++
linktitle: Actualizar referencias en otras hojas de cálculo
type: docs
weight: 5000
url: /es/cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: Aprenda cómo actualizar referencias en otras hojas de cálculo mientras elimina columnas y filas en blanco en una hoja de cálculo usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Cuando elimina columnas y filas en blanco en una hoja de cálculo, sus referencias en otras hojas de cálculo se vuelven inválidas. Si desea evitar este comportamiento y garantizar que las referencias a la hoja de cálculo actual en otras hojas también se actualicen, use la propiedad [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) y configúrela en **true**.

{{% /alert %}}

## **Actualizar referencias en otras hojas de cálculo al eliminar columnas y filas en blanco en una hoja de cálculo**

Consulte el siguiente código de ejemplo y su salida en consola. La celda E3 en la segunda hoja tiene una fórmula `=Sheet1!C3`, que hace referencia a la celda C3 en la primera hoja. Si configura la propiedad [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) en **true**, esta fórmula se actualizará a `=Sheet1!A1` después de eliminar columnas y filas en blanco en la primera hoja. Sin embargo, si configura la propiedad [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) en **false**, la fórmula en la celda E3 de la segunda hoja permanecerá como `=Sheet1!C3` y se volverá inválida.

### **Ejemplo de Programación**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Add second sheet with name Sheet2
    wb.GetWorksheets().Add(u"Sheet2");

    // Access first sheet and add some integer value in cell C1
    // Also add some value in any cell to increase the number of blank rows and columns
    Worksheet sht1 = wb.GetWorksheets().Get(0);
    sht1.GetCells().Get(u"C1").PutValue(4);
    sht1.GetCells().Get(u"K30").PutValue(4);

    // Access second sheet and add formula in cell E3 which refers to cell C1 in first sheet
    Worksheet sht2 = wb.GetWorksheets().Get(1);
    sht2.GetCells().Get(u"E3").SetFormula(u"'Sheet1'!C1");

    // Calculate formulas of workbook
    wb.CalculateFormula();

    // Print the formula and value of cell E3 in second sheet before deleting blank columns and rows in Sheet1.
    std::cout << "Cell E3 before deleting blank columns and rows in Sheet1." << std::endl;
    std::cout << "--------------------------------------------------------" << std::endl;
    std::cout << "Cell Formula: " << sht2.GetCells().Get(u"E3").GetFormula().ToUtf8() << std::endl;
    std::cout << "Cell Value: " << sht2.GetCells().Get(u"E3").GetStringValue().ToUtf8() << std::endl;

    // If you comment DeleteOptions.UpdateReference property below, then the formula in cell E3 in second sheet will not be updated
    DeleteOptions opts;
    opts.SetUpdateReference(true);

    // Delete all blank rows and columns with delete options
    sht1.GetCells().DeleteBlankColumns(opts);
    sht1.GetCells().DeleteBlankRows(opts);

    // Calculate formulas of workbook
    wb.CalculateFormula();

    // Print the formula and value of cell E3 in second sheet after deleting blank columns and rows in Sheet1.
    std::cout << std::endl;
    std::cout << std::endl;
    std::cout << "Cell E3 after deleting blank columns and rows in Sheet1." << std::endl;
    std::cout << "--------------------------------------------------------" << std::endl;
    std::cout << "Cell Formula: " << sht2.GetCells().Get(u"E3").GetFormula().ToUtf8() << std::endl;
    std::cout << "Cell Value: " << sht2.GetCells().Get(u"E3").GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Salida de la consola**

Este es el resultado en consola del código de ejemplo anterior cuando la propiedad [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) se establece en **true**.

{{< highlight java >}}

Cell E3 before deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!C1
Cell Value: 4

Cell E3 after deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!A1
Cell Value: 4

{{< /highlight >}}

Este es el resultado en consola del código de ejemplo anterior cuando la propiedad [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) se establece en **false**. Como puede ver, la fórmula en la celda E3 de la segunda hoja no se actualiza y su valor de celda ahora es 0 en lugar de 4, lo cual es inválido.

{{< highlight java >}}

Cell E3 before deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!C1
Cell Value: 4

Cell E3 after deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!C1
Cell Value: 0

{{< /highlight >}}
