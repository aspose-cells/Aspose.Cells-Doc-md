---
title: Establecer borde de rango con C++
type: docs
weight: 600
url: /es/cpp/set-range-border/
description: Aprende cómo establecer bordes en rangos usando Aspose.Cells con C++.
---

## **Escenarios de uso posibles**
Cuando deseas establecer el borde para un rango, no necesitas configurar cada celda individualmente. Puedes establecer el borde en el rango completo. Aspose.Cells ofrece esta función. Este artículo proporciona un ejemplo de código que usa Aspose.Cells para establecer el borde del rango.

## **Establecer borde de rango en Excel**
Para establecer el borde de un rango en Excel, puedes seguir estos pasos:
1. Selecciona el rango de celdas al que deseas aplicarle el borde.
2. En la pestaña "Inicio" de la cinta, busca el grupo "Fuente".
3. Dentro del grupo "Fuente", haz clic en el botón desplegable "Bordes".
<br>
<img src="border.png" />
4. Elige el tipo de borde que deseas aplicar de las opciones en el menú desplegable. Puedes elegir entre estilos de borde preestablecidos o personalizar tu propio borde.
5. Una vez que hayas seleccionado el estilo de borde deseado, el borde se aplicará al rango seleccionado de celdas.

## **Configurar borde de rango usando Aspose.Cells**
Este ejemplo muestra cómo:

1. Crear un libro de trabajo.
2. Agregar datos a las celdas en la primera hoja de trabajo.
3. Crear un [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range).
4. Establecer el borde interno del rango.
5. Establecer el borde externo del rango.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new Workbook object
    Workbook workbook;

    // Obtain the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get("A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get("B1");
    cell.PutValue(u"Count");
    cell = cells.Get("C1");
    cell.PutValue(u"Price");

    cell = cells.Get("A2");
    cell.PutValue(u"Apple");
    cell = cells.Get("A3");
    cell.PutValue(u"Mango");
    cell = cells.Get("A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get("A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get("B2");
    cell.PutValue(5);
    cell = cells.Get("B3");
    cell.PutValue(3);
    cell = cells.Get("B4");
    cell.PutValue(6);
    cell = cells.Get("B5");
    cell.PutValue(4);

    cell = cells.Get("C2");
    cell.PutValue(5);
    cell = cells.Get("C3");
    cell.PutValue(20);
    cell = cells.Get("C4");
    cell.PutValue(30);
    cell = cells.Get("C5");
    cell.PutValue(60);

    // Create a range (A1:C5)
    Range range = cells.CreateRange(u"A1", u"C5");

    // Set inner border of range
    CellsColor innerColor = workbook.CreateCellsColor();
    innerColor.SetColor(Color::Red());
    range.SetInsideBorders(BorderType::Vertical, CellBorderType::Thin, innerColor);
    innerColor.SetColor(Color::Green());
    range.SetInsideBorders(BorderType::Horizontal, CellBorderType::Thin, innerColor);

    // Set outer border of range
    CellsColor outerColor = workbook.CreateCellsColor();
    outerColor.SetColor(Color::Blue());
    range.SetOutlineBorders(CellBorderType::Thin, outerColor);

    // Save the Workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
