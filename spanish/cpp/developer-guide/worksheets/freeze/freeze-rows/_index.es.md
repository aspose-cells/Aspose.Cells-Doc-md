---
title: Congelar fila(s) superior(es) del archivo Excel con C++
linktitle: Congelar Filas
type: docs
weight: 190
url: /es/cpp/how-to-freeze-rows-of-excel-worksheet
description: En este artículo, aprenderás cómo congelar las filas superiores de las hojas de Excel programáticamente usando la biblioteca C++ con API Aspose.Cells.
keywords: Congelar filas superiores, Congelar fila superior.
---

## **Introducción**

En este artículo, aprenderemos cómo congelar fila(s) superior(es). Cuando tienes una gran cantidad de datos bajo un encabezado común, no puedes ver el encabezado al desplazarte hacia abajo en la hoja. Puedes congelar fila(s) superior(es) para que puedas ver esa parte congelada incluso cuando se desplaza el resto de los datos. Puedes ver fácilmente los encabezados en las filas superiores.

## **Congelar Filas en Excel**

**![Congelar fila(s) superior(es) en Excel](Freeze-Rows.png)**

1. Si deseas congelar la(s) fila(s) superior(es), primero selecciona la fila debajo de la fila que debe congelarse.
2. Haz clic en Ver > Congelar paneles.
3. En el menú desplegable, haz clic en Congelar fila superior.
4. Si te desplazas hacia abajo, la primera fila siempre estará en la vista superior.

**![Fila congelada](Frozen-Row.png)**

Como puedes ver, la primera fila está congelada y siempre permanece en la parte superior de la vista cuando te desplazas hacia abajo.

Congelar filas te permite ver tus datos grandes sin perder el rastro de la etiqueta de la fila.

## **Congelar filas con Aspose.Cells for C++**
Es simple congelar fila(s) con Aspose.Cells for C++. 
Utiliza el método [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) para congelar fila(s) en la fila seleccionada.
1. Construye un libro de trabajo para abrir el archivo o crea un archivo vacío.
2. Congelar la primera fila con el método Worksheet.FreezePanes()
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

    // Freezing panes at the cell B2
    workbook.GetWorksheets().Get(0).FreezePanes(u"A2", 1, 0);

    // Saving the file
    workbook.Save(u"frozen.xlsx");

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Adjunto [archivo de Excel de muestra](../Freeze.xlsx).
{{< app/cells/assistant language="cpp" >}}
