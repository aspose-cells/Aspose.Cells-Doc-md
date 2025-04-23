---
title: Obtener dirección, conteo de celdas, desplazamiento, columna completa y fila completa del rango con C++
linktitle: Obtener dirección, conteo de celdas, desplazamiento, columna completa y fila completa del rango
type: docs
weight: 330
url: /es/cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
description: Aprende cómo obtener dirección, conteo de celdas, desplazamiento, columna completa y fila completa de un rango usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**
Aspose.Cells proporciona el objeto `Range`, que tiene varios métodos útiles que facilitan trabajar con rangos de Excel. Este artículo ilustra el uso de los siguientes métodos o propiedades del objeto `Range`:

- **Dirección**

  Obtiene la dirección del rango.

- **Recuento de celdas**

  Obtiene el conteo total de celdas en el rango.

- **Desplazamiento**

  Obtiene un rango por desplazamiento.

- **Columna completa**

  Obtiene un objeto `Range` que representa toda la columna (o columnas) que contiene el rango especificado.

- **Fila completa**

  Obtiene un objeto `Range` que representa toda la fila (o filas) que contiene el rango especificado.

## **Obtener dirección, conteo de celdas, desplazamiento, columna completa y fila completa del rango**
El siguiente código de ejemplo explica el uso de los métodos y propiedades discutidos anteriormente. Por favor, vea la salida de consola del código a continuación como referencia.

## **Código de muestra**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Create range A1:B3
    cout << "Creating Range A1:B3" << endl;
    Range rng = ws.GetCells().CreateRange(u"A1:B3");

    // Print range address and cell count
    cout << "Range Address: " << rng.GetAddress().ToUtf8() << endl;
    cout << "Range row Count: " << rng.GetRowCount() << endl;
    cout << "Range column Count: " << rng.GetColumnCount() << endl;

    // Formatting console output
    cout << "----------------------" << endl;
    cout << endl;

    // Create range A1
    cout << "Creating Range A1" << endl;
    rng = ws.GetCells().CreateRange(u"A1");

    // Print range offset, entire column and entire row
    cout << "Offset: " << rng.GetOffset(2, 2).GetAddress().ToUtf8() << endl;
    cout << "Entire Column: " << rng.GetEntireColumn().GetAddress().ToUtf8() << endl;
    cout << "Entire Row: " << rng.GetEntireRow().GetAddress().ToUtf8() << endl;

    // Formatting console output
    cout << "----------------------" << endl;
    cout << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Salida de la consola**
{{< highlight java >}}

Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
