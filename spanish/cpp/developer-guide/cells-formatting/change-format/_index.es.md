---
title: Cambiar el formato de una celda con C++
linktitle: Cambiar el formato de una celda
description: Cómo usar la biblioteca Aspose.Cells en C++ para cambiar el formato de las celdas, incluyendo fuente, color, borde, etc. Ajustando estas propiedades, tienes mayor control sobre cómo se ven y aparecen las celdas.
keywords: Aspose.Cells, formateo de celdas, C++, fuente, color, borde
type: docs
weight: 20
url: /es/cpp/how-to-change-format-of-cell/
---

## **Escenarios de uso posibles**
Cuando desee resaltar ciertos datos, puede cambiar el estilo de las celdas.

## **Cómo cambiar el formato de una celda en Excel**

Para cambiar el formato de una sola celda en Excel, siga estos pasos:

1. Abra Excel y abra el libro que contiene la celda que desea formatear.

2. Localice la celda que desea formatear.

3. Haga clic con el botón derecho en la celda y seleccione "Formato de celdas" en el menú contextual. Alternativamente, puede seleccionar la celda, ir a la pestaña Inicio en la cinta de Excel, hacer clic en el menú desplegable "Formato" en el grupo "Celdas" y seleccionar "Formato de celdas".

4. Aparecerá el cuadro de diálogo "Formato de celdas". Aquí, puede elegir varias opciones de formato para aplicar a la celda seleccionada. Por ejemplo, puede cambiar el estilo de fuente, el tamaño de fuente, el color de fuente, el formato de número, los bordes, el color de fondo, etc. Explore las diferentes pestañas en el cuadro de diálogo para acceder a varias opciones de formato.

5. Después de realizar los cambios de formato deseados, haga clic en el botón "Aceptar" para aplicar el formato a la celda seleccionada.

## **Cómo cambiar el formato de una celda usando C++**

Para cambiar el formato de una celda usando Aspose.Cells, puedes usar los siguientes métodos:
1. [Cell.SetStyle(Style style)](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)
2. [Cell.SetStyle(Style style, bool explicitFlag)](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)
3. [Cell.SetStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)

## **Código de muestra**
En este ejemplo, creamos un libro de Excel, agregamos algunos datos de muestra, accedemos a la primera hoja de cálculo y obtenemos dos celdas ("A2" y "B3"). Luego, obtenemos el estilo de la celda, establecemos varias opciones de formato (por ejemplo, color de fuente, negrita) y cambiamos el formato de la celda. Finalmente, guardamos el libro en un nuevo archivo.
![todo:image_alt_text](change-format.png)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

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

    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cell a2 = worksheet.GetCells().Get(u"A2");
    Style style = a2.GetStyle();
    style.GetFont().SetColor(Color::Red());
    style.GetFont().SetIsBold(true);

    StyleFlag flag;
    flag.SetFontColor(true);
    a2.SetStyle(style, flag);

    Cell b3 = worksheet.GetCells().Get(u"B3");
    Style style2 = b3.GetStyle();
    style2.GetFont().SetColor(Color::Blue());
    style2.GetFont().SetIsItalic(true);
    b3.SetStyle(style2);

    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
}
```
