---
title: Obtener el índice máximo de columna en una fila y el índice máximo de fila en una columna con C++
linktitle: Obtener el índice de columna máximo en fila y el índice de fila máximo en columna
type: docs
weight: 600
url: /es/cpp/get-max-index-in-row-and-column/
description: Aprende cómo obtener el índice máximo de columna en una fila y el índice máximo de fila en una columna mediante la API Aspose.Cells for C++.
keywords: Obtener el índice de columna máximo en fila, obtener el índice de fila máximo en columna, obtener el índice de columna de datos máximo en fila, obtener el índice de fila de datos máximo en columna.
---

## **Escenarios de uso posibles**
Cuando solo necesitas manipular algunos datos en filas o columnas, necesitas conocer el rango de datos de filas y columnas. Aspose.Cells ofrece esta función. Para obtener el índice máximo de columna en una fila, puedes obtener las propiedades [Row.GetLastCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/) y [Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/), y luego usar la propiedad [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) para obtener el índice máximo de columna y el índice de columna de datos máximo. Pero para obtener el índice máximo de fila y el índice de datos de fila en una columna, necesitas crear un rango en la columna, luego recorrer el rango para encontrar la última celda, y finalmente obtener el atributo [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) del celda.

Aspose.Cells proporciona las siguientes propiedades y métodos para ayudarlo a alcanzar sus metas.
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/)

## **Obtener el índice de columna máximo en fila y el índice de fila máximo en columna usando Aspose.Cells**
Este ejemplo muestra cómo:

1. Cargar el [archivo de muestra](sample.xlsx).
1. Obtener la fila que necesita obtener el índice de columna máximo e índice de columna de datos máximo.
1. Obtener el atributo [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) en la celda.
1. Crear un rango basado en la columna.
1. Obtener el iterador y recorrer el rango.
1. Obtener el atributo [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) en la celda.

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String filePath = srcDir + u"sample.xlsx";

    Workbook workbook(filePath);
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    Row row = cells.CheckRow(1);
    if (row)
    {
        std::cout << "Max column index in row: " << row.GetLastCell().GetColumn() << std::endl;
        std::cout << "Max data column index in row: " << row.GetLastDataCell().GetColumn() << std::endl;
    }

    Range columnRange = cells.CreateRange(1, 1, true);
    auto colIter = columnRange.GetEnumerator();

    int maxRow = 0;
    int maxDataRow = 0;

    while (colIter.MoveNext())
    {
        Cell currCell = colIter.GetCurrent();
        if (!currCell.GetStringValue().IsEmpty())
        {
            maxDataRow = currCell.GetRow();
        }
        if (!currCell.GetStringValue().IsEmpty() || currCell.GetHasCustomStyle())
        {
            maxRow = currCell.GetRow();
        }
    }

    std::cout << "Max row index in Column: " << maxRow << std::endl;
    std::cout << "Max data row index in Column: " << maxDataRow << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
