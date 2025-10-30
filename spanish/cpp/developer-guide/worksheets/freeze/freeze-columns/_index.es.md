---
title: Congelar la(s) primera(s) columna(s) de la hoja de Excel con C++
linktitle: Congelar Columnas
type: docs
weight: 190
url: /es/cpp/how-to-freeze-columns-of-excel-worksheet
description: En este artículo, aprenderás cómo congelar las columnas de la izquierda de las hojas de Excel programáticamente usando la biblioteca C++ con API Aspose.Cells.
keywords: Congelar columnas de la izquierda, Congelar primeras columnas, Bloquear la(s) columna(s)
---

## **Introducción**

En este artículo, aprenderemos cómo congelar la(s) columna(s) izquierda(s). Cuando tienes una gran cantidad de datos en una fila, no puedes ver las columnas de la izquierda al desplazarte horizontalmente por la hoja. Puedes congelar y bloquear la(s) primera(s) columna(s) para que puedas ver esa parte congelada incluso cuando se desplaza el resto de los datos. Puedes ver fácilmente los encabezados en las columnas de la izquierda.

## **Congelar Columnas en Excel**

**![Congelar columnas izquierdas en Excel](freeze-columns.png)**

1. Si deseas congelar la(s) columna(s) izquierda(s), primero selecciona la columna debajo de la columna que debe congelarse.
2. Haz clic en Ver > Congelar paneles.
3. En el menú desplegable, haz clic en Congelar la primera columna.
4. Si te desplazas hacia abajo, la primera columna estará siempre en la vista izquierda.

**![Columna congelada](frozen-columns.png)**

Como puedes ver, la primera columna está congelada, la primera columna siempre se bloquea en la parte superior de la vista cuando te desplazas horizontalmente.

Congelar columnas te permite ver tus datos largos sin seguir la pista de la primera columna.

## **Congelar columnas con Aspose.Cells for C++**
Es simple congelar la(s) primera(s) columna(s) con Aspose.Cells for C++. 
Utiliza el método [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) para congelar columna(s) en la columna seleccionada.
1. Construir un libro de trabajo para abrir el archivo o crear un archivo vacío.
2. Congelar la primera columna con el método Worksheet.FreezePanes()
3. Guarda el archivo.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Freeze.xlsx");

    // Freezing panes at the second column
    workbook.GetWorksheets().Get(0).FreezePanes(u"B1", 0, 1);

    // Saving the file
    workbook.Save(u"frozen.xlsx");

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Adjunto [archivo de Excel de origen de muestra](Freeze.xlsx).
{{< app/cells/assistant language="cpp" >}}
