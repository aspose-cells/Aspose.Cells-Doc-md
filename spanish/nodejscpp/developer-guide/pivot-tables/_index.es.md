---
title: Insertar tabla dinámica
linktitle: Insertar tabla dinámica
description: Crear y formatear tablas dinámicas con Aspose.Cells for Node.js mediante C++.
keywords: Crear tabla dinámica, Insertar tabla dinámica, Formatear tabla dinámica.
type: docs
weight: 160
url: /es/nodejs-cpp/create-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **¿Qué es una tabla dinámica?**
Una tabla dinámica es un informe de resumen interactivo: condensa un bloque grande de datos sin procesar, organizados fila por fila, en una matriz compacta sin una sola fórmula. Decide qué columnas se convierten en etiquetas de fila, cuáles en etiquetas de columna y cuáles se agregan como valores; la tabla dinámica se encarga de la agrupación y de los cálculos:
- **Resumir**: ventas totales por producto, por región o por trimestre, en lugar de largas cadenas de fórmulas.
- **Comparar**: las categorías en las filas y los períodos en las columnas convierten una lista plana en un informe de tabulación cruzada, donde las tendencias se aprecian de un vistazo.
- **Desglosar**: haga doble clic en cualquier valor de resumen para inspeccionar las filas de origen asociadas.
- **Actualizar**: cuando cambian los datos de origen, una actualización recalcula todo el informe.
Los escenarios habituales son los paneles de ventas, los desgloses de gastos y el análisis de inventario: cualquier pregunta del tipo «¿cómo se desglosan estas cifras por categoría y tiempo?». Aspose.Cells for Node.js mediante C++ genera las mismas tablas dinámicas de forma programática, por lo que los libros de trabajo que genera su aplicación pueden contener informes listos para usar en lugar de únicamente datos sin procesar.

### **Modelo de objetos de la tabla dinámica**
Aspose.Cells for Node.js mediante C++ proporciona un conjunto especial de clases que se utilizan para crear y controlar tablas dinámicas. Estas clases se utilizan para crear y configurar objetos [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable), los componentes fundamentales de una tabla dinámica. Los objetos son:
- [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) representa un campo en una [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection) representa una colección de todos los objetos [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) de una [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) representa una tabla dinámica en una hoja de cálculo.
- [**PivotTableCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) representa una colección de todos los objetos [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) de una hoja de cálculo.

### **Crear una tabla dinámica simple con Aspose.Cells**
La creación de una tabla dinámica consta de tres pasos principales: escribir los datos de origen en celdas de la hoja de cálculo, agregar la tabla dinámica en una posición de destino y colocar los campos de la tabla dinámica en las áreas de filas, columnas y datos.
1. Agregue datos a una hoja de cálculo mediante el método [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) del objeto [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). Estos datos se utilizarán como origen de datos de la tabla dinámica.
2. Agregue una tabla dinámica a la hoja de cálculo llamando al método [**add**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#add-string-string-string-) de la colección [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection): `add(sourceData, row, column)`. `sourceData` es el rango de origen (por ejemplo, "A1:C8"); `row` y `column` son las coordenadas de la celda de destino en la esquina superior izquierda de la tabla dinámica, indexadas desde cero (la celda E3 significa fila 2, columna 4). El método devuelve directamente el nuevo objeto [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
3. Coloque los campos de la tabla dinámica con el método `addFieldToArea` del objeto [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable): el nombre de un campo se asigna al área de filas (`PivotFieldType.Row`), al área de columnas (`PivotFieldType.Column`) o al área de datos (`PivotFieldType.Data`).
4. Guarde el libro de trabajo; la tabla dinámica se escribe en el archivo guardado.
Después de ejecutar el código de ejemplo, se agrega una tabla dinámica a la hoja de cálculo.

```javascript
const AsposeCells = require("aspose.cells.node");

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

// Agregar una tabla dinámica en la celda de destino E3, usando A1:C8 como origen
let pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// Asignar campos de tabla dinámica: Sport a Filas, Quarter a Columnas, Sales a Datos
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Quarter");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");

// Guardar el libro de trabajo
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
Al asignar un rango de celdas como origen de datos, este debe extenderse desde la esquina superior izquierda hasta la esquina inferior derecha. Por ejemplo, "A1:C3" es válido, pero "C3:A1" no lo es.
{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}