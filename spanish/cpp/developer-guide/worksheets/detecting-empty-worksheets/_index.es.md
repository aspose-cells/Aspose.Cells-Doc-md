---
title: Detección de hojas de trabajo vacías con C++
linktitle: Detectar hojas de cálculo vacías
type: docs
weight: 410
url: /es/cpp/detecting-empty-worksheets/
description: Este artículo muestra código que explica cómo detectar automáticamente hojas de trabajo vacías en libros de Excel usando la API de C++ con la biblioteca Aspose.Cells.
keywords: detectar hoja de cálculo vacía c++, encontrar hoja de cálculo vacía en Excel c++
---

## **Buscar celdas pobladas**

Las hojas de cálculo pueden tener una o más celdas pobladas con valores, donde los valores pueden ser simples (texto, numérico, fecha/hora) o una fórmula o un valor basado en una fórmula. En tal caso, es fácil detectar si una hoja de cálculo dada está vacía o no. Todo lo que hay que verificar son las propiedades [**Cells.MaxDataRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/) o [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/). Si las propiedades mencionadas devuelven valores cero o positivos, eso significa que una o más celdas han sido pobladas. Sin embargo, si alguna de estas propiedades devuelve -1, eso indica que ninguna de las celdas ha sido poblada en la hoja de cálculo dada.

{{% alert color="primary" %}}

Las colecciones de filas y columnas tienen índice base cero, por lo tanto, una celda en la fila 0 y columna 0 significa la primera celda de la hoja de cálculo, que es A1.

{{% /alert %}}

## **Comprobar celdas inicializadas vacías**

Todas las celdas que tienen valores se inicializan automáticamente. Sin embargo, existe la posibilidad de que una hoja de cálculo tenga celdas solo con formato aplicado. En tal escenario, las propiedades [**Cells.MaxDataRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/) o [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) devolverán -1, indicando la ausencia de valores poblados. Pero las celdas inicializadas debido al formateo no pueden detectarse usando este método. Para verificar si una hoja de cálculo tiene celdas inicializadas vacías, se recomienda usar el método `MoveNext` en el enumerador obtenido de la colección [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Si el método `MoveNext` devuelve **true**, eso significa que hay una o más celdas inicializadas en la hoja dada.

## **Comprobar formas**

Es posible que una hoja dada no tenga celdas pobladas, pero puede contener formas y objetos como controles, gráficos, imágenes, y más. Si necesitamos verificar si una hoja contiene alguna forma, podemos hacerlo inspeccionando la propiedad [**ShapeCollection.Count**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/getcount/). Cualquier valor positivo indica la presencia de formas en la hoja.

## **Ejemplo de Programación**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load an existing spreadsheet
    Workbook book(srcDir + u"sample.xlsx");

    // Loop over all worksheets in the workbook
    WorksheetCollection sheets = book.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        Worksheet sheet = sheets.Get(i);

        // Check if worksheet has populated cells
        if (sheet.GetCells().GetMaxDataRow() != -1)
        {
            cout << sheet.GetName().ToUtf8() << " is not empty because one or more cells are populated" << endl;
        }
        // Check if worksheet has shapes
        else if (sheet.GetShapes().GetCount() > 0)
        {
            cout << sheet.GetName().ToUtf8() << " is not empty because there are one or more shapes" << endl;
        }
        // Check if worksheet has empty initialized cells
        else
        {
            Range range = sheet.GetCells().GetMaxDisplayRange();
            auto rangeIterator = range.GetEnumerator();
            if (rangeIterator.MoveNext())
            {
                cout << sheet.GetName().ToUtf8() << " is not empty because one or more cells are initialized" << endl;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
