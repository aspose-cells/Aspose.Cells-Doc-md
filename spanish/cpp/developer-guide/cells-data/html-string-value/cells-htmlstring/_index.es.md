---
title: Gestionar Cadena HTML de Celdas con C++
linktitle: Gestionar Celdas con Cadena Html
type: docs
weight: 600
url: /es/cpp/manage-cells-html-string/
description: Aprende cómo Gestionar Cadena HTML de Celdas mediante la API Aspose.Cells for C++.
keywords: Agregar Cadena HTML dentro de la Celda, Establecer Cadena HTML dentro de la Celda, Agregar Cadena HTML, Obtener Cadena HTML de la Celda, Gestionar Celdas con Cadena Html
---

## **Escenarios de uso posibles**
Cuando necesites establecer datos con estilo en una Celda específica, puedes asignar una cadena HTML a la Celda. Por supuesto, también puedes obtener la cadena HTML de la celda. Aspose.Cells ofrece esta función. Aspose.Cells proporciona las siguientes propiedades y métodos para ayudarte a alcanzar tus metas.
- [**Cell::GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/)
- [**Cell::SetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/sethtmlstring/)

## **Obtener y establecer cadena HTML usando Aspose.Cells**
Este ejemplo muestra cómo:

1. Crear un libro de trabajo y agregar algunos datos.
1. Obtener la celda específica en la primera hoja de cálculo.
1. Establecer cadena HTML en la celda.
1. Obtener cadena HTML de la celda.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object
    Workbook workbook;

    // Obtain the reference of the newly added worksheet
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

    Cell c3 = cells.Get(u"C3");
    // Set HTML string for C3 cell
    c3.SetHtmlString(u"<b>test bold</b>");

    Cell c4 = cells.Get(u"C4");
    // Set HTML string for C4 cell
    c4.SetHtmlString(u"<i>test italic</i>");

    // Get the HTML string of specific cell
    std::cout << c3.GetHtmlString().ToUtf8() << std::endl;
    std::cout << c4.GetHtmlString().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

Resultado generado por el código de ejemplo

La siguiente captura de pantalla muestra la salida del código de muestra anterior.

![todo:image_alt_text](htmlstring.png)
{{< app/cells/assistant language="cpp" >}}
