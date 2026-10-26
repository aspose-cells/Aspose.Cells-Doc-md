---
title: Insertar una tabla dinámica
linktitle: Insertar una tabla dinámica
description: Cree y formatee tablas dinámicas en archivos de hojas de cálculo de Excel.
keywords: Crear tabla dinámica, insertar tabla dinámica, formatear tabla dinámica.
type: docs
weight: 160
url: /es/net/create-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **¿Qué es una tabla dinámica?**
Una tabla dinámica es un informe de resumen interactivo que condensa en una matriz compacta, sin utilizar ninguna fórmula, un bloque grande de datos sin procesar organizados fila por fila. Decida qué columnas se convierten en etiquetas de fila, cuáles en etiquetas de columna y cuáles se agregan como valores; la tabla dinámica se encarga de realizar la agrupación y los cálculos:
- **Resumir** — ventas totales por producto, región o trimestre, en lugar de largas cadenas de fórmulas.
- **Comparar** — las categorías en las filas y los períodos en las columnas convierten una lista plana en un informe de tabulación cruzada en el que las tendencias se aprecian de un vistazo.
- **Desglosar** — haga doble clic en cualquier valor resumido para inspeccionar las filas de origen que lo respaldan.
- **Actualizar** — cuando los datos de origen cambian, una actualización recalcula todo el informe.
Los escenarios típicos son los paneles de ventas, los desgloses de gastos y el análisis de inventario: cualquier pregunta del tipo «¿cómo se desglosan estas cifras por categoría y tiempo?». Aspose.Cells for .NET genera las mismas tablas dinámicas mediante programación, de modo que los libros de trabajo generados por la aplicación puedan incluir informes listos para usar en lugar de únicamente datos sin procesar.

### **Modelo de objetos de la tabla dinámica**
Aspose.Cells ofrece un conjunto especial de clases en el namespace [**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) que permiten crear y controlar tablas dinámicas. Estas clases se utilizan para crear y configurar objetos [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable), que constituyen los componentes básicos de una tabla dinámica. Los objetos son:
- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) representa un campo de una [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) representa una colección de todos los objetos [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) de una [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) representa una tabla dinámica en una hoja de cálculo.
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) representa una colección de todos los objetos [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) de una hoja de cálculo.

### **Creación de una tabla dinámica simple con Aspose.Cells**
La creación de una tabla dinámica consta de tres pasos principales: escribir los datos de origen en las celdas de una hoja de cálculo, agregar la tabla dinámica en una posición de destino y colocar los campos de la tabla dinámica en las áreas de filas, columnas y datos.
1. Agregue datos a una hoja de cálculo mediante el método [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) del objeto [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). Estos datos se usarán como origen de datos de la tabla dinámica.
2. Agregue una tabla dinámica a la hoja de cálculo llamando al método [**Add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) de la colección [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection): `Add(sourceData, row, column)`. `sourceData` es el rango de origen (por ejemplo, "A1:C8"); `row` y `column` son las coordenadas de la celda de destino situada en la esquina superior izquierda de la tabla dinámica (la celda E3 significa fila 2, columna 4). El método devuelve directamente el nuevo objeto [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
3. Coloque los campos de la tabla dinámica con el método `AddFieldToArea` del objeto [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable): asigne un nombre de campo al área de filas (`PivotFieldType.Row`), al área de columnas (`PivotFieldType.Column`) o al área de datos (`PivotFieldType.Data`).
4. Guarde el libro de trabajo; la tabla dinámica se escribe en el archivo guardado.
Tras ejecutar el código de ejemplo, se agrega una tabla dinámica a la hoja de cálculo.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Crear un nuevo libro de trabajo y obtener la primera hoja de cálculo
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// Escribir los datos de origen: ventas por deporte y trimestre
sheet.Cells["A1"].PutValue("Sport");
sheet.Cells["B1"].PutValue("Quarter");
sheet.Cells["C1"].PutValue("Sales");
sheet.Cells["A2"].PutValue("Golf");
sheet.Cells["B2"].PutValue("Qtr3");
sheet.Cells["C2"].PutValue(1500);
sheet.Cells["A3"].PutValue("Golf");
sheet.Cells["B3"].PutValue("Qtr4");
sheet.Cells["C3"].PutValue(2000);
sheet.Cells["A4"].PutValue("Tennis");
sheet.Cells["B4"].PutValue("Qtr3");
sheet.Cells["C4"].PutValue(600);
sheet.Cells["A5"].PutValue("Tennis");
sheet.Cells["B5"].PutValue("Qtr4");
sheet.Cells["C5"].PutValue(1500);
sheet.Cells["A6"].PutValue("Tennis");
sheet.Cells["B6"].PutValue("Qtr3");
sheet.Cells["C6"].PutValue(4070);
sheet.Cells["A7"].PutValue("Tennis");
sheet.Cells["B7"].PutValue("Qtr4");
sheet.Cells["C7"].PutValue(5000);
sheet.Cells["A8"].PutValue("Golf");
sheet.Cells["B8"].PutValue("Qtr3");
sheet.Cells["C8"].PutValue(6430);

// Agregar una tabla dinámica en la celda de destino E3, usando A1:C8 como origen
PivotTable pivotTable = sheet.PivotTables.Add("A1:C8", 2, 4);

// Asignar los campos de la tabla dinámica: Sport a Filas, Quarter a Columnas, Sales a Datos
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Quarter");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");

// Guardar el libro de trabajo
workbook.Save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
Al asignar un rango de celdas como origen de datos, el rango debe extenderse desde la esquina superior izquierda hasta la inferior derecha. Por ejemplo, "A1:C3" es válido, pero "C3:A1" no lo es.
{{% /alert %}}

## Artículos relacionados
- [Agregar campos de filtro a una tabla dinámica en Aspose.Cells for .NET](/cells/es/net/add-page-field-in-pivot-table/)
- [Aplicar estilos a tablas dinámicas en Aspose.Cells for .NET](/cells/es/net/apply-style-to-pivot-table/)
- [Modificar el diseño de los campos de página en una tabla dinámica](/cells/es/net/change-page-field-layout/)
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/net/filter-by-label-or-value-of-pivot-table/)
- [Administrar los campos de valor de tablas dinámicas en Aspose.Cells for .NET](/cells/es/net/manage-value-fields/)

{{< app/cells/assistant language="csharp" >}}