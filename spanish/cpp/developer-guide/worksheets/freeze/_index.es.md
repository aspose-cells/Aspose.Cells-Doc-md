---
title: Congelar paneles de la hoja de Excel con C++
linktitle: Congelar paneles
type: docs
weight: 190
url: /es/cpp/how-to-freeze-panes-of-excel-worksheet
description: En este artículo, aprenderás cómo congelar paneles de hojas de Excel programáticamente usando la biblioteca C++ con la API Aspose.Cells.
keywords: Congelar paneles, congelar ventana.
---

## **Introducción**

En este artículo, aprenderemos Cómo congelar paneles. Cuando tienes una gran cantidad de datos bajo un encabezado común, no puedes ver el encabezado cuando te desplazas hacia abajo en la hoja de cálculo. Y cada registro contiene muchos datos. Puedes congelar paneles para que puedas ver esa parte congelada incluso cuando se desplaza el resto de los datos. Puedes ver fácilmente los encabezados en las filas superiores o en las primeras columnas. Congelar y descongelar paneles solo cambia la vista de los datos sin modificarlos.

## **En Excel**

**![Congelar paneles en Excel](Congelar-paneles.png)**

1. Si deseas congelar paneles, congelar filas y columnas, primero selecciona una celda (como B2).
2. Haz clic en Ver > Congelar paneles.
3. En el menú desplegable, haga clic en Congelar paneles.
4. Si te desplazas hacia abajo o a la derecha, la primera fila y columna permanecen congeladas.

**![Paneles congelados](Frozen-Panes.png)**

Como puedes ver, la primera fila y la columna A están congeladas, la segunda fila es 32, y la segunda columna visible es D.

Los paneles congelados te permiten visualizar tus datos grandes sin mantener el seguimiento de las etiquetas de filas o columnas.

## **Congelar paneles con Aspose.Cells for C++**
Es simple congelar paneles con Aspose.Cells for C++. Por favor, usa el método [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) para congelar paneles en la celda seleccionada.
1. Construye un libro de trabajo para abrir el archivo o crea un archivo vacío.
2. Congelar paneles con el método Worksheet.FreezePanes().
3. Guarda el archivo.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    U16String inputFilePath(u"Freeze.xlsx");
    Workbook workbook(inputFilePath);

    // Freeze panes at the cell B2
    WorksheetCollection sheets = workbook.GetWorksheets();
    sheets.Get(0).FreezePanes(u"B2", 1, 1);

    // Save the file
    U16String outputFilePath(u"frozen.xlsx");
    workbook.Save(outputFilePath);

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Adjunto [archivo de Excel de origen de muestra](Freeze.xlsx).
