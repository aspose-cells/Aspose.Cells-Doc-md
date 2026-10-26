---
title: Crear una tabla dinámica
linktitle: Crear una tabla dinámica
description: Cree y formatee tablas dinámicas con Aspose.Cells for C++.
keywords: Crear tabla dinámica, Insertar tabla dinámica, Formatear tabla dinámica.
type: docs
weight: 160
url: /es/cpp/create-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **¿Qué es una tabla dinámica?**
Una tabla dinámica es un informe de resumen interactivo: condensa un gran bloque de datos sin procesar, organizados fila por fila, en una matriz compacta sin necesidad de utilizar una sola fórmula. Decida qué columnas se convierten en etiquetas de fila, cuáles en etiquetas de columna y cuáles se agregan como valores; la tabla dinámica se encarga de la agrupación y los cálculos:
- **Resumir** — las ventas totales por producto, región o trimestre, en lugar de cadenas largas de fórmulas.
- **Comparar** — colocar las categorías en las filas y los períodos en las columnas convierte una lista plana en un informe cruzado en el que las tendencias se aprecian de un vistazo.
- **Profundizar** — haga doble clic en cualquier valor de resumen para inspeccionar las filas de origen que lo respaldan.
- **Actualizar** — cuando los datos de origen cambian, una actualización recalcula todo el informe.
Los escenarios habituales son los paneles de ventas, los desgloses de gastos y el análisis de inventario: cualquier pregunta del tipo «¿cómo se desglosan estas cifras por categoría y período?». En Aspose.Cells for C++, una tabla dinámica se crea con el método [PivotTableCollection.Add()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/add/) de una hoja de cálculo. Una vez creada la tabla dinámica, puede trabajar con ella mediante la clase [PivotTable](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/).

## **Crear una tabla dinámica**
El siguiente código de ejemplo muestra cómo crear una tabla dinámica y trabajar con ella. Consulte el [archivo de Excel generado](23167010.xlsx) con este código y la siguiente captura de pantalla, que muestra el archivo generado en Microsoft Excel.
![todo:image_alt_text](create-pivot-table_1.png)

## **Código de ejemplo**

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Crear un nuevo libro de trabajo y obtener la primera hoja de cálculo
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Escribir los datos de origen: ventas por deporte y trimestre
    cells.Get(u"A1").PutValue(u"Sport");
    cells.Get(u"B1").PutValue(u"Quarter");
    cells.Get(u"C1").PutValue(u"Sales");
    cells.Get(u"A2").PutValue(u"Golf");
    cells.Get(u"B2").PutValue(u"Qtr3");
    cells.Get(u"C2").PutValue(1500);
    cells.Get(u"A3").PutValue(u"Golf");
    cells.Get(u"B3").PutValue(u"Qtr4");
    cells.Get(u"C3").PutValue(2000);
    cells.Get(u"A4").PutValue(u"Tennis");
    cells.Get(u"B4").PutValue(u"Qtr3");
    cells.Get(u"C4").PutValue(600);
    cells.Get(u"A5").PutValue(u"Tennis");
    cells.Get(u"B5").PutValue(u"Qtr4");
    cells.Get(u"C5").PutValue(1500);
    cells.Get(u"A6").PutValue(u"Tennis");
    cells.Get(u"B6").PutValue(u"Qtr3");
    cells.Get(u"C6").PutValue(4070);
    cells.Get(u"A7").PutValue(u"Tennis");
    cells.Get(u"B7").PutValue(u"Qtr4");
    cells.Get(u"C7").PutValue(5000);
    cells.Get(u"A8").PutValue(u"Golf");
    cells.Get(u"B8").PutValue(u"Qtr3");
    cells.Get(u"C8").PutValue(6430);

    // Agregar una tabla dinámica en la celda de destino E3, usando A1:C8 como origen
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"A1:C8", 2, 4);

    // Asignar campos de la tabla dinámica: Sport a Filas, Quarter a Columnas y Sales a Datos
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Quarter");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");

    // Guardar el libro de trabajo
    workbook.Save(u"pivotTable_test_out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{< app/cells/assistant language="cpp" >}}