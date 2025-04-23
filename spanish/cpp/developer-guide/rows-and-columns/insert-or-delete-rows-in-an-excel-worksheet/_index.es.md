---
title: Insertar o eliminar filas en una hoja de cálculo de Excel con C++
linktitle: Insertar o eliminar filas
type: docs
weight: 20
url: /es/cpp/insert-or-delete-rows-in-an-excel-worksheet/
description: Este artículo proporciona el código en C++ para insertar y eliminar filas en una hoja de cálculo de Excel.
keywords: c++ insertar o eliminar filas en hoja de Excel, c++ insertar o eliminar filas en Excel, c++ insertar filas en Excel, c++ eliminar filas en Excel, insertar o eliminar filas en hoja de cálculo con c++, insertar o eliminar filas en Excel con c++, insertar filas en Excel con c++, eliminar filas en Excel con c++
---

{{% alert color="primary" %}}

Al crear una hoja de cálculo nueva, o trabajar con una hoja de cálculo existente, es posible que necesite agregar filas o columnas adicionales para alojar datos. En otros momentos, es posible que necesite eliminar filas o columnas de posiciones específicas en la hoja de cálculo.

{{% /alert %}}

Aspose.Cells ofrece dos métodos para insertar y eliminar filas: [**Cells.InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) y [**Cells.DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/). Estos métodos están optimizados para el rendimiento y hacen el trabajo muy rápidamente.

Para insertar o eliminar un número de filas, recomendamos que siempre use los métodos [**Cells.InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) y [**Cells.DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) en lugar de usar los métodos [**Cells.InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) o [**DeleteRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterow/) en un bucle.

Aspose.Cells funciona de la misma manera que lo hace Microsoft Excel. Cuando se agregan filas o columnas, el contenido de la hoja de cálculo se desplaza hacia abajo y hacia la derecha. Cuando se eliminan filas o columnas, el contenido de la hoja de cálculo se desplaza hacia arriba o hacia la izquierda. Cualquier referencia en otras hojas de cálculo y celdas se actualiza cuando se agregan o eliminan filas.

```cpp
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out_book1.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the book
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Insert 10 rows at row index 2 (insertion starts at 3rd row)
    sheet.GetCells().InsertRows(2, 10);

    // Delete 5 rows now. (8th row - 12th row)
    sheet.GetCells().DeleteRows(7, 5);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows inserted and deleted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
