---
title: Dividir pantalla de hoja de cálculo de Excel con C++
linktitle: Pantalla dividida
type: docs
weight: 190
url: /es/cpp/how-to-split-screen-of-excel-worksheet
description: En este artículo, aprenderá cómo mostrar en paneles separados ciertas filas y/o columnas dividiendo la hoja de cálculo en dos o cuatro partes programáticamente usando C++.
keywords: Congelar filas superiores, Congelar fila superior.
---

## **Introducción**

En este artículo, aprenderemos cómo mostrar en paneles separados ciertas filas y/o columnas dividiendo la hoja de cálculo en dos o cuatro partes. Cuando se trabaja con conjuntos de datos grandes, necesitamos ver algunas áreas de la misma hoja de cálculo a la vez para comparar diferentes subconjuntos de datos. La función de pantalla dividida puede satisfacer sus necesidades.

## **Cómo dividir la pantalla en Excel**
Para dividir una hoja de cálculo en dos o cuatro partes, haz lo siguiente:

1. Selecciona la fila/columna/celda antes de la cual deseas colocar la división.
2. En la pestaña de Vista, en el grupo de Ventanas, haz clic en el botón Dividir.

**![Pantalla dividida](Split-Screen.png)**

## **Dividir la hoja de cálculo verticalmente en columnas**

Para separar dos áreas de la hoja de cálculo verticalmente, selecciona la columna a la derecha de la columna donde deseas que aparezca la división y haz clic en el botón Dividir en Excel.

Es fácil dividir la hoja de cálculo verticalmente en columnas programáticamente con Aspose.Cells for C++, solo necesita seleccionar una celda en la fila superior como celda activa, luego
dividir con el método [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet in the workbook.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Sets C1 cell in the top row as the active cell.
    sheet.SetActiveCell(u"C1");

    // Split worksheet vertically on columns.
    sheet.Split();

    std::cout << "Worksheet processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Dividir la hoja de cálculo horizontalmente en filas**
Para separar tu ventana de Excel horizontalmente, selecciona la fila debajo de la fila donde deseas que ocurra la división en Excel.

Es fácil dividir la hoja de cálculo horizontalmente en filas programáticamente con Aspose.Cells for C++, solo necesita seleccionar una celda en la columna izquierda como celda activa, luego
dividir con el método [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook and load an existing Excel file.
    Workbook workbook(u"Book1.xlsx");

    // Access the first worksheet in the workbook.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Set the A6 cell in the left column as the active cell.
    sheet.SetActiveCell(u"A6");

    // Split the worksheet horizontally on rows.
    sheet.Split();

    // Save the modified workbook to a new file.
    workbook.Save(u"dest.xlsx");

    std::cout << "Workbook processed and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Dividir la hoja de cálculo en cuatro partes**
Para ver cuatro secciones diferentes de la misma hoja de cálculo simultáneamente, divide tu pantalla tanto vertical como horizontalmente en Excel.

Es fácil dividir la hoja de cálculo verticalmente en columnas programáticamente con Aspose.Cells for C++, solo necesita seleccionar una celda que no esté en la primera fila y columna como celda activa, luego
dividir con el método [**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Set E6 cell as the active cell.
    sheet.SetActiveCell(u"E6");

    // Split worksheet into four parts.
    sheet.Split();

    Aspose::Cells::Cleanup();
}
```

## **Cómo quitar la división**
Para eliminar la división de la hoja de cálculo, simplemente haz clic en el botón Dividir nuevamente.

Aspose.Cells for C++ proporciona un método [**Worksheet.RemoveSplit**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/) para eliminar la configuración de división.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Remove split
    sheet.RemoveSplit();

    // Split worksheet into four parts
    sheet.Split();

    std::cout << "Worksheet split successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
