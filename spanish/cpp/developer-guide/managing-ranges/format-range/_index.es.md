---
title: Formatear rangos con C++
linktitle: Formato de rangos
type: docs
weight: 105
url: /es/cpp/how-to-format-a-range/
description: Aprende cómo formatear rangos en Excel usando Aspose.Cells con C++. Aplica estilos, fuentes y colores a rangos de celdas programáticamente.
---

## **Escenarios de uso posibles**
Cuando necesitas aplicar un estilo a un rango, puedes usar el formato de rango.

## **Cómo dar formato a un rango en Excel**

Para dar formato a un rango de celdas en Excel, puedes usar las opciones de formato integradas proporcionadas por Excel. Así es como puedes dar formato a un rango de celdas directamente en Excel:

1. Abre Excel y el libro que contiene el rango que deseas formatear.

2. Selecciona el rango de celdas que deseas formatear. Puedes hacer clic y arrastrar para seleccionar el rango, o puedes usar atajos de teclado como Shift + Flechas para extender la selección.

3. Una vez seleccionado el rango, haz clic derecho en el rango seleccionado y elige "Formato de celdas" en el menú contextual. Alternativamente, ve a la pestaña Inicio en la cinta de Excel, haz clic en el menú desplegable "Formato" en el grupo "Celdas", y selecciona "Formato de celdas".

4. Aparecerá el cuadro de diálogo "Formato de celdas". Aquí, puedes elegir varias opciones de formato para aplicar al rango seleccionado. Por ejemplo, puedes cambiar el estilo de fuente, tamaño de fuente, color de fuente, formato de número, bordes, color de fondo, etc. Explora las distintas pestañas en el cuadro de diálogo para acceder a varias opciones de formato.

5. Después de realizar los cambios de formato deseados, haz clic en el botón "Aceptar" para aplicar el formato al rango seleccionado.

## **Cómo formatear un rango usando C++**

Para formatear un rango usando Aspose.Cells, puedes usar los siguientes métodos:
1. [Range.ApplyStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)
2. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/cpp/aspose.cells/range/setstyle/)

## **Código de muestra**
En este ejemplo, creamos un libro de Excel, agregamos algunos datos de muestra, accedemos a la primera hoja y definimos dos rangos ("A1:C3" y "A4:C5"). Luego, creamos nuevos estilos, configuramos varias opciones de formato (por ejemplo, color de fuente, negrita) y aplicamos el estilo al rango. Finalmente, guardamos el libro en un archivo nuevo.
<br>
![todo:image_alt_text](format-range.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
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

    Range range = worksheet.GetCells().CreateRange(u"A1:C3");
    Style style = workbook.CreateStyle();
    style.GetFont().SetColor(Color::Red());
    style.GetFont().SetIsBold(true);

    StyleFlag flag;
    flag.SetFont(true);
    range.ApplyStyle(style, flag);

    Range range2 = worksheet.GetCells().CreateRange(u"A4:C5");
    Style style2 = workbook.CreateStyle();
    style2.GetFont().SetColor(Color::Blue());
    style2.GetFont().SetIsItalic(true);
    range2.SetStyle(style2);

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
