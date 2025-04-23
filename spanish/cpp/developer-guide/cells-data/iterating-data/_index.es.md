---
title: Cómo y Dónde Usar Enumeradores con C++
linktitle: Iterar datos
type: docs
weight: 55
url: /es/cpp/how-and-where-to-use-enumerators/
description: Aprende cómo Cómo y Dónde Usar Enumeradores mediante la API Aspose.Cells for C++.
keywords: Cómo usar Enumeradores, Enumerador de celdas, Enumerador de filas, Enumerador de columnas
---

{{% alert color="primary" %}}

Un enumerador es un objeto que proporciona la capacidad de recorrer un contenedor o colección. Los enumeradores se pueden usar para leer los datos de la colección, pero no pueden usarse para modificar la colección subyacente, mientras que IEnumerable es una interfaz que define un método GetEnumerator que devuelve una interfaz IEnumerator, lo cual permite acceso solo de lectura a una colección.

Las API de Aspose.Cells proporcionan una serie de enumeradores, sin embargo, este artículo discute principalmente los tres tipos que se enumeran a continuación.

1. Enumerador de celdas
1. Enumerador de filas
1. Enumerador de columnas

{{% /alert %}}

## **Cómo usar Enumeradores**

### **Enumerador de celdas**

Hay diversas formas de acceder al enumerador de celdas, y se puede utilizar cualquiera de estos métodos según los requisitos de la aplicación. Aquí están los métodos que devuelven el enumerador de celdas.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getenumerator/)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getenumerator/)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/range/getenumerator/)

Todos los métodos mencionados anteriormente devuelven el enumerador que permite recorrer la colección de celdas que han sido inicializadas.

{{% alert color="primary" %}}

Mientras se recorren las celdas, la colección no debe modificarse (operaciones que causarán una nueva celda que se instancie o celda existente que se elimine). De lo contrario, es posible que el enumerador no pueda recorrer todas las celdas correctamente (algunos elementos pueden ser recorridos repetidamente o ignorados).

{{% /alert %}}

El siguiente ejemplo de código demuestra la implementación de la interfaz IEnumerator para una colección de celdas.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load a file in an instance of Workbook
    Workbook book(srcDir + u"sample.xlsx");

    // Get the enumerator from Cells collection
    auto cellEnumerator = book.GetWorksheets().Get(0).GetCells().GetEnumerator();
    // Traverse cells in the collection
    while (cellEnumerator.MoveNext())
    {
        auto cell = cellEnumerator.GetCurrent();
        std::cout << cell.GetName().ToUtf8() << " " << cell.GetValue().ToString().ToUtf8() << std::endl;
    }

    // Get enumerator from an object of Row
    auto rowEnumerator = book.GetWorksheets().Get(0).GetCells().GetRows().Get(0).GetEnumerator();
    // Traverse cells in the given row
    while (rowEnumerator.MoveNext())
    {
        auto cell = rowEnumerator.GetCurrent();
        std::cout << cell.GetName().ToUtf8() << " " << cell.GetValue().ToString().ToUtf8() << std::endl;
    }

    // Get enumerator from an object of Range
    auto rangeEnumerator = book.GetWorksheets().Get(0).GetCells().CreateRange(u"A1:B10").GetEnumerator();
    // Traverse cells in the range
    while (rangeEnumerator.MoveNext())
    {
        auto cell = rangeEnumerator.GetCurrent();
        std::cout << cell.GetName().ToUtf8() << " " << cell.GetValue().ToString().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **Enumerador de filas**

El enumerador de filas se puede acceder al usar el método [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/getenumerator/). El siguiente ejemplo de código demuestra la implementación de la interfaz IEnumerator para [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/).

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load a file in an instance of Workbook
    Workbook book(srcDir + u"sample.xlsx");

    // Get the enumerator for RowCollection
    auto rowsEnumerator = book.GetWorksheets().Get(0).GetCells().GetRows().GetEnumerator();

    // Traverse rows in the collection
    while (rowsEnumerator.MoveNext())
    {
        auto row = rowsEnumerator.GetCurrent();
        std::cout << row.GetIndex() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **Obtener Columnas**

Las Columnas se pueden acceder al usar el método [**ColumnCollection.Get**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/get/). El siguiente ejemplo de código demuestra la implementación del método Get para [**ColumnCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/).

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook book(srcDir + u"sample.xlsx");

    auto cells = book.GetWorksheets().Get(0).GetCells();
    auto columns = cells.GetColumns();

    for (int i = 0; i < columns.GetCount(); ++i)
    {
        auto col = columns.Get(i);
        std::cout << col.GetIndex() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Dónde usar Enumeradores**

Para discutir las ventajas de usar enumeradores, tomemos un ejemplo en tiempo real.

Escenario

Un requisito de la aplicación es recorrer todas las celdas en un [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) dado para leer sus valores. Podrían implementarse varias formas de lograr esto. Se muestran algunas a continuación.

### **Usando Rango de Visualización**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Load a file in an instance of Workbook
    Workbook book(inputFilePath);

    // Get Cells collection of first worksheet
    Cells cells = book.GetWorksheets().Get(0).GetCells();

    // Get the MaxDisplayRange
    Range displayRange = cells.GetMaxDisplayRange();

    // Loop over all cells in the MaxDisplayRange
    for (int row = displayRange.GetFirstRow(); row < displayRange.GetRowCount(); row++)
    {
        for (int col = displayRange.GetFirstColumn(); col < displayRange.GetColumnCount(); col++)
        {
            // Read the Cell value
            std::cout << displayRange.Get(row, col).GetStringValue().ToUtf8() << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
}
```

### **Usando MaxDataRow y MaxDataColumn**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load a file in an instance of Workbook
    Workbook book(srcDir + u"sample.xlsx");

    // Get Cells collection of first worksheet
    auto cells2 = book.GetWorksheets().Get(0).GetCells();

    // Get maximum data row and column
    int maxDataRow = cells2.GetMaxDataRow();
    int maxDataColumn = cells2.GetMaxDataColumn();

    // Loop over all cells
    for (int row = 0; row <= maxDataRow; row++)
    {
        for (int col = 0; col <= maxDataColumn; col++)
        {
            // Read the Cell value
            auto currentCell = cells2.GetCell(row, col);
            if (!currentCell.IsNull())
            {
                cout << currentCell.GetStringValue().ToUtf8() << endl;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

Como puedes observar, ambos enfoques mencionados anteriormente utilizan más o menos una lógica similar; es decir, recorrer todas las celdas en la colección para leer los valores de las celdas. Esto podría ser problemático por varias razones, como se discute a continuación.

1. Las APIs como [**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxrow/), [**GetMaxDataRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/), [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxcolumn/), [**GetMaxDataColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) y [**GetMaxDisplayRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) requieren tiempo adicional para recopilar las estadísticas correspondientes. En caso de que la matriz de datos (filas x columnas) sea grande, usar estas APIs podría afectar el rendimiento.
1. En la mayoría de los casos, no todas las celdas en un rango dado están instanciadas. En tales situaciones, verificar cada celda en la matriz no es tan eficiente en comparación con verificar solo las celdas inicializadas.
1. Acceder a una celda en un bucle como Cells fila, columna hará que se instancien todos los objetos de celda en un rango, lo que eventualmente podría causar OutOfMemoryException.

## **Conclusión**

Con base en los hechos mencionados anteriormente, los siguientes son los posibles escenarios en los que se deben usar los enumeradores.

1. Se requiere acceso de solo lectura a la colección de celdas, es decir; el requisito es solo inspeccionar las celdas.
1. Se deben recorrer un gran número de celdas.
1. Solo se deben recorrer celdas/filas/columnas inicializadas.
