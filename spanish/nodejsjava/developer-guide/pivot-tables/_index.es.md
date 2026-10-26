---
title: Insertar tabla dinámica
linktitle: Insertar tabla dinámica
description: Cree y formatee tablas dinámicas en archivos de hoja de cálculo de Excel mediante Aspose.Cells for Node.js via Java.
keywords: Crear tabla dinámica, Insertar tabla dinámica, Formatear tabla dinámica, Aspose.Cells for Node.js via Java.
type: docs
weight: 160
url: /es/nodejs-java/create-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **¿Qué es una tabla dinámica?**
Una tabla dinámica es un informe de resumen interactivo: condensa un gran bloque de datos sin procesar, organizados fila por fila, en una matriz compacta sin utilizar una sola fórmula. Usted decide qué columnas se convierten en etiquetas de fila, cuáles en etiquetas de columna y cuáles se agregan como valores; la tabla dinámica se encarga de la agrupación y de los cálculos:
- **Resumir** — las ventas totales por producto, por región o por trimestre, en lugar de largas cadenas de fórmulas.
- **Comparar** — las categorías en las filas y los períodos en las columnas convierten una lista plana en un informe cruzado en el que las tendencias se aprecian de un vistazo.
- **Desglosar** — haga doble clic en cualquier valor de resumen para ver las filas de origen que lo componen.
- **Actualizar** — cuando los datos de origen cambian, una actualización recalcula todo el informe.
Los escenarios habituales son los paneles de ventas, los desgloses de gastos y el análisis de inventario: cualquier pregunta como «¿Cómo se desglosan estas cifras por categoría y tiempo?». Aspose.Cells for Node.js via Java crea las mismas tablas dinámicas de forma programática, de modo que los libros de trabajo que genera la aplicación puedan incluir informes listos para usar en lugar de solo datos sin procesar.

### **Modelo de objetos de la tabla dinámica**
Aspose.Cells proporciona un conjunto de clases que se utilizan para crear y controlar tablas dinámicas. Los componentes básicos son:
- `PivotField` representa un campo en una `PivotTable`.
- `PivotFieldCollection` representa una colección de todos los objetos `PivotField` de la `PivotTable`.
- `PivotTable` representa una tabla dinámica en una hoja de cálculo.
- `PivotTableCollection` representa una colección de todos los objetos `PivotTable` de una hoja de cálculo.

### **Creación de una tabla dinámica simple mediante Aspose.Cells**
La creación de una tabla dinámica consta de los siguientes pasos: escribir los datos de origen en las celdas de la hoja de cálculo, agregar la tabla dinámica en la ubicación de destino y colocar los campos de la tabla dinámica en las áreas de filas, columnas y datos.
1. Agregue datos a una hoja de cálculo mediante el método `putValue` de la celda. Estos datos se utilizarán como origen de datos de la tabla dinámica.
2. Agregue una tabla dinámica a la hoja de cálculo llamando al método `add` de la colección `PivotTables`: `add(sourceData, row, column)`. `sourceData` es el rango de origen (por ejemplo, "A1:C8"); `row` y `column` son las coordenadas indexadas desde cero de la celda de destino, situada en la esquina superior izquierda de la tabla dinámica (la celda E3 corresponde a la fila 2 y la columna 4). El método devuelve directamente el nuevo objeto `PivotTable`.
3. Coloque los campos de la tabla dinámica mediante el método `addFieldToArea` del objeto `PivotTable`: asigne el nombre de un campo al área de filas (`PivotFieldType.ROW`), al área de columnas (`PivotFieldType.COLUMN`) o al área de datos (`PivotFieldType.DATA`).
4. Guarde el libro de trabajo: la tabla dinámica se escribe en el archivo guardado.
Después de ejecutar el código de ejemplo, se agrega una tabla dinámica a la hoja de cálculo.

```javascript
const AsposeCells = require("aspose.cells");

// Crear un nuevo libro de trabajo y obtener la primera hoja de cálculo
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Escribir los datos de origen: ventas por deporte y trimestre
sheet.getCells().get("A1").putValue("Sport");
sheet.getCells().get("B1").putValue("Quarter");
sheet.getCells().get("C1").putValue("Sales");
sheet.getCells().get("A2").putValue("Golf");
sheet.getCells().get("B2").putValue("Qtr3");
sheet.getCells().get("C2").putValue(1500);
sheet.getCells().get("A3").putValue("Golf");
sheet.getCells().get("B3").putValue("Qtr4");
sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Tennis");
sheet.getCells().get("B4").putValue("Qtr3");
sheet.getCells().get("C4").putValue(600);
sheet.getCells().get("A5").putValue("Tennis");
sheet.getCells().get("B5").putValue("Qtr4");
sheet.getCells().get("C5").putValue(1500);
sheet.getCells().get("A6").putValue("Tennis");
sheet.getCells().get("B6").putValue("Qtr3");
sheet.getCells().get("C6").putValue(4070);
sheet.getCells().get("A7").putValue("Tennis");
sheet.getCells().get("B7").putValue("Qtr4");
sheet.getCells().get("C7").putValue(5000);
sheet.getCells().get("A8").putValue("Golf");
sheet.getCells().get("B8").putValue("Qtr3");
sheet.getCells().get("C8").putValue(6430);

// Agregar una tabla dinámica en la celda de destino E3, tomando los datos de A1:C8
let pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// Asignar campos de la tabla dinámica: Sport a Filas, Quarter a Columnas, Sales a Datos
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Quarter");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");

// Guardar el libro de trabajo
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
Cuando se asigna un rango de celdas como origen de datos, el rango debe ir de la esquina superior izquierda a la inferior derecha. Por ejemplo, "A1:C3" es válido, pero "C3:A1" no lo es.
{{% /alert %}}

## Artículos relacionados
- [Agregar campos de filtro a una tabla dinámica en Aspose.Cells for Node.js via Java](/cells/es/nodejs-java/add-page-field-in-pivot-table/)
- [Aplicar estilos a tablas dinámicas en Aspose.Cells for Node.js via Java](/cells/es/nodejs-java/apply-style-to-pivot-table/)
- [Modificar la disposición de los campos de página en una tabla dinámica](/cells/es/nodejs-java/change-page-field-layout/)
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Administrar campos de valores de tablas dinámicas en Aspose.Cells for Node.js via Java](/cells/es/nodejs-java/manage-value-fields/)

{{< app/cells/assistant language="nodejs-java" >}}