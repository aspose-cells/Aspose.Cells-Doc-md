---
title: Agregar campo calculado en tabla dinámica con C++
linktitle: Agregar campo calculado en tabla dinámica
type: docs
weight: 130
url: /es/cpp/add-calculated-field-in-pivot-table/
description: Cómo agregar un campo calculado en tabla dinámica con Aspose.Cells for C++.
keywords: Agregar un campo calculado en una tabla dinámica.
---

## **Escenarios de uso posibles**
Cuando crea una tabla dinámica basada en datos conocidos, se encuentra con que los datos no son los que desea. Los datos que desea es la combinación de estos datos originales. Por ejemplo, necesita sumar, restar, multiplicar y dividir los datos originales antes de querer los datos. En ese momento, necesita crear un campo calculado y establecer la fórmula correspondiente para el cálculo. Luego realizar algunas estadísticas y otras operaciones en el campo calculado. 

## **Añadir campo calculado en tabla dinámica en Excel**
Para insertar un campo calculado en una tabla dinámica en Excel, siga estos pasos:

1. Seleccione la tabla dinámica a la que desea agregar un campo calculado. 
2. Vaya a la pestaña Analizar tabla dinámica en la cinta.
3. Haga clic en "Campos, elementos y conjuntos" y luego seleccione "Campo calculado" en el menú desplegable.
4. En el campo "Nombre", ingrese un nombre para el campo calculado.
5. En el campo "Fórmula", ingresa la fórmula para el cálculo que deseas realizar utilizando los nombres adecuados de los campos de la tabla dinámica y los operadores matemáticos correspondientes. 
<br>
<img src="1.png" width=80% />
6. Haga clic en "ok" para crear el campo calculado.
7. El nuevo campo calculado aparecerá en la Lista de campos de la Tabla Dinámica bajo la sección de Valores.
8. Arrastre el campo calculado a la sección de Valores de la Tabla Dinámica para mostrar los valores calculados.
<br>
<img src="2.png" width=80% />

## **Agregar campo calculado en tabla dinámica usando C++**
Agrega un campo calculado al archivo de Excel usando Aspose.Cells. Por favor, consulta el siguiente código de muestra. Después de ejecutar el código de ejemplo, se agregará una tabla dinámica con campo calculado a la hoja de cálculo.
1. Establece los datos originales y crea una tabla dinámica. 
2. Crea el campo calculado de acuerdo con el CampoPivote existente en la tabla dinámica.
3. Agrega el campo calculado al área de datos. 
4. Finalmente, guarda el libro en formato [XLSX de salida](out.xlsx). 

## **Código de muestra**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Creating a Workbook object
    Workbook workbook;

    // Obtaining the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the values to the cells
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

    // Adding a PivotTable to the worksheet
    int32_t i = ws.GetPivotTables().Add(u"=A1:C5", u"D10", u"PivotTable1");

    // Accessing the instance of the newly added PivotTable
    PivotTable pivotTable = ws.GetPivotTables().Get(i);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);

    // Adding a calculated field to PivotTable and dragging it to data area
    pivotTable.AddCalculatedField(u"total", u"=Count*Price", true);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
