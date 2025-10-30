---
title: Obtener índice de celdas con C++
linktitle: Obtener el índice de celdas
type: docs
weight: 600
url: /es/cpp/get-cells-index/
description: Aprende cómo obtener el índice de fila o columna por el nombre de fila, columna o celdas. Convierte el nombre de la celda en índice de fila y columna comenzando desde cero usando Aspose.Cells con C++.
keywords: Obtener el índice de fila y columna por el nombre de la celda, Obtener el índice de columna por el nombre de la columna, Obtener el índice de fila por el nombre de la fila, Obtener el índice por el nombre de la celda.
---

{{% alert color="primary" %}}
 La vista predeterminada de Excel es referencia estilo A1, donde cada columna se define como A, B, C.... y las celdas se nombran como A1, B2, C3... y así sucesivamente.
Es posible que quieras saber en qué fila y columna se encuentra esta celda.

{{% /alert %}}

## **Escenarios de uso posibles**
Cuando solo necesitas manipular datos específicos en la hoja de cálculo por índice de fila y columna, necesitas conocer los índices de fila y columna de esa celda específica. 
 Aspose.Cells ofrece esta función para obtener el índice de fila y columna por el nombre de la fila, columna y celda. 
 Aspose.Cells proporciona las siguientes propiedades y métodos para ayudarte a lograr tus objetivos:
- [**CellsHelper::CellNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/)
- [**CellsHelper::ColumnIndexToName**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/columnindextoname/)
- [**CellsHelper::ColumnNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/columnnametoindex/)
- [**CellsHelper::RowIndexToName**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/rowindextoname/)
- [**CellsHelper::RowNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/rownametoindex/)

 Nota: La indexación comienza en cero en Aspose.Cells for C++, pero el ID de la fila es uno en MS Excel.

## **Obtener Índices de Celdas usando Aspose.Cells**
Este ejemplo muestra cómo:

1. Crear un libro de trabajo y agregar algunos datos.
1. Encontrar la celda específica en la primera hoja de trabajo.
1. Obtener el índice de fila e índice de columna por el nombre de la celda.
1. Obtener el índice de columna por el nombre de la columna.
1. Obtener el índice de fila por el nombre de la fila.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook;

    // Obtaining the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);

    cell = cells.Get(u"C2");
    cell.PutValue(5);
    cell = cells.Get(u"C3");
    cell.PutValue(20);
    cell = cells.Get(u"C4");
    cell.PutValue(30);
    cell = cells.Get(u"C5");
    cell.PutValue(60);

    Cell curr = cells.Find(u"Blackberry", nullptr);
    int currRow, currCol;

    // Get row and column index of current cell
    CellsHelper::CellNameToIndex(curr.GetName(), currRow, currCol);
    std::cout << "Row Index: " << currRow << "  Column Index: " << currCol << std::endl;

    // Get column name by column index
    U16String columnName = CellsHelper::ColumnIndexToName(currCol);

    // Get row name by row index
    U16String rowName = CellsHelper::RowIndexToName(currRow);

    std::cout << "Column Name: " << columnName.ToUtf8() << " Row Name: " << rowName.ToUtf8() << std::endl;

    // Get column index by column name
    int columnIndex = CellsHelper::ColumnNameToIndex(columnName);

    // Get row index by row name
    int rowIndex = CellsHelper::RowNameToIndex(rowName);

    std::cout << "Column Index: " << columnIndex << " Row Index: " << rowIndex << std::endl;

    // Assertions
    if (columnIndex != currCol || rowIndex != currRow) {
        std::cerr << "Assertion failed!" << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
