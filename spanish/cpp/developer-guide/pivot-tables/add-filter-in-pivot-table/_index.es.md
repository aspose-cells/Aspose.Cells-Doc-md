---
title: Filtro de tabla dinámica con C++
linktitle: Filtro dinámico
type: docs
weight: 130
url: /es/cpp/add-or-clear-pivot-filter/
description: Aprende cómo agregar un filtro en tabla dinámica con Aspose.Cells usando C++.
keywords: Agregar un filtro en la tabla dinámica sin office 2013, office 2016, office 2019 y office 365.
---

## **Escenarios de uso posibles**
Cuando creas una tabla dinámica con datos conocidos y deseas filtrarla, necesitas aprender y usar filtro. Puede ayudarte a filtrar los datos que deseas de manera efectiva. Usando la API de Aspose.Cells, puedes agregar y borrar filtros en los valores de los campos en Tablas dinámicas. 

## **Agregar filtro en tabla dinámica en Excel**
Agregar filtro en tabla dinámica en Excel, sigue estos pasos:

1. Selecciona la Tabla Dinámica de la que deseas eliminar el filtro. 
2. Haz clic en la flecha desplegable del filtro que deseas agregar en la tabla dinámica.
3. Selecciona "Los 10 principales" en el menú desplegable.
<br>
<img src="3.png" width=80% />
4. Establece el modo de exhibición y el número de filtros.
<br>
<img src="4.png" width=80% />

## **Agregar filtro en tabla dinámica**
Por favor, consulta el siguiente código de ejemplo. Establece los datos y crea una Tabla Dinámica basada en ellos. Luego añade un filtro en el campo de fila de la tabla dinámica. Finalmente, guarda el libro de trabajo en formato [XLSX de salida](filterout.xlsx). Después de ejecutar el código de ejemplo, se añade una tabla dinámica con filtro top10 a la hoja de cálculo.

### **Código de muestra**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Set values to cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");
    cell = cells.Get(u"A6");
    cell.PutValue(u"Guava");
    cell = cells.Get(u"A7");
    cell.PutValue(u"Carambola");
    cell = cells.Get(u"A8");
    cell.PutValue(u"Banana");
    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);
    cell = cells.Get(u"B6");
    cell.PutValue(5);
    cell = cells.Get(u"B7");
    cell.PutValue(2);
    cell = cells.Get(u"B8");
    cell.PutValue(20);

    // Add a PivotTable to the worksheet
    int32_t i = ws.GetPivotTables().Add(u"=A1:B8", u"D10", u"PivotTable1");

    // Access the instance of the newly added PivotTable
    PivotTable pivotTable = ws.GetPivotTables().Get(i);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);

    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Count");
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    PivotField field = pivotTable.GetRowFields().Get(0);
    field.SetIsAutoSort(true);
    field.SetIsAscendSort(false);
    field.SetAutoSortField(0);

    // Add top10 filter
    PivotField filterField = pivotTable.GetRowFields().Get(0);
    filterField.FilterTop10(0, PivotFilterType::Count, false, 5);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the workbook
    workbook.Save(u"filterout.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Borrar filtro en tabla dinámica en Excel**
Limpiar filtro en Tabla Dinámica en Excel, sigue estos pasos:

1. Selecciona la Tabla Dinámica de la que deseas eliminar el filtro. 
2. Haz clic en la flecha desplegable para el filtro que deseas borrar en la tabla dinámica.
3. Selecciona "Limpiar filtro" en el menú desplegable.
<br>
<img src="1.png" width=80% />
4. Si deseas borrar todos los filtros de la tabla dinámica, también puedes hacer clic en el botón "Limpiar filtros" en la pestaña Analizar tabla dinámica en la cinta de Excel.
<br>
<img src="2.png" width=80% />

## **Borrar filtro en tabla dinámica**
Eliminar filtro en tabla dinámica usando Aspose.Cells. Por favor, consulta el siguiente código de ejemplo. 
1. Establece los datos y crea una tabla dinámica basada en ellos. 
2. Agrega un filtro en el campo de fila de la tabla dinámica. 
3. Guarda el libro en formato XLSX de salida. Después de ejecutar el código de ejemplo, se añade un filtro top10 a la hoja de cálculo. 
4. Elimina el filtro en un campo de la tabla dinámica específico. Después de ejecutar el código para eliminar el filtro, se eliminará el filtro en el campo de la tabla dinámica específico. Por favor, revisa el XLSX de salida.

### **Código de muestra**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Set values to cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");
    cell = cells.Get(u"A6");
    cell.PutValue(u"Guava");
    cell = cells.Get(u"A7");
    cell.PutValue(u"Carambola");
    cell = cells.Get(u"A8");
    cell.PutValue(u"Banana");
    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);
    cell = cells.Get(u"B6");
    cell.PutValue(5);
    cell = cells.Get(u"B7");
    cell.PutValue(2);
    cell = cells.Get(u"B8");
    cell.PutValue(20);

    // Add a PivotTable to the worksheet
    int i = ws.GetPivotTables().Add(u"=A1:B8", u"D10", u"PivotTable1");

    // Access the instance of the newly added PivotTable
    PivotTable pivotTable = ws.GetPivotTables().Get(i);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);

    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Count");
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    PivotField field = pivotTable.GetRowFields().Get(0);
    field.SetIsAutoSort(true);
    field.SetIsAscendSort(false);
    field.SetAutoSortField(0);

    // Add top10 filter
    PivotField filterField = pivotTable.GetRowFields().Get(0);
    filterField.FilterTop10(0, PivotFilterType::Count, false, 5);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"out_add.xlsx");

    // Clear PivotFilter from the specific PivotField
    pivotTable.GetPivotFilters().ClearFilter(field.GetBaseIndex());
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"out_delete.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
