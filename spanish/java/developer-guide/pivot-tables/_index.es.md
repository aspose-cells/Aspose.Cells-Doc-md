---
title: Crear una tabla dinámica
linktitle: Crear una tabla dinámica
description: Cree y formatee tablas dinámicas con Aspose.Cells for Java.
keywords: Crear tabla dinámica, Insertar tabla dinámica, Formatear tabla dinámica.
type: docs
weight: 160
url: /es/java/create-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **¿Qué es una tabla dinámica?**
Una tabla dinámica es un informe de resumen interactivo: condensa un gran bloque de datos sin procesar, organizados fila por fila, en una matriz compacta sin usar ni una sola fórmula. El usuario decide qué columnas se convierten en etiquetas de fila, cuáles en etiquetas de columna y cuáles se agregan como valores; la tabla dinámica se encarga de la agrupación y los cálculos:
- **Resumir** — las ventas totales por producto, región o trimestre, en lugar de largas cadenas de fórmulas.
- **Comparar** — organizar las categorías en las filas y los periodos en las columnas convierte una lista plana en un informe cruzado donde las tendencias se aprecian de un vistazo.
- **Desglosar** — haga doble clic en cualquier valor de resumen para inspeccionar las filas de origen que lo componen.
- **Actualizar** — cuando cambian los datos de origen, una actualización recalcula todo el informe.
Los escenarios habituales son los paneles de control de ventas, los desgloses de gastos y el análisis de inventario; es decir, cualquier pregunta del tipo "¿cómo se desglosan estas cifras por categoría y tiempo?". Aspose.Cells for Java crea las mismas tablas dinámicas de forma programática, de modo que los libros de trabajo que genera su aplicación pueden contener informes listos para usar en lugar de únicamente datos sin procesar.

### **Crear una tabla dinámica con Aspose.Cells**

{{% alert color="primary" %}}
Con Aspose.Cells, es posible agregar tablas dinámicas a las hojas de cálculo. Aspose.Cells cuenta con varias clases especiales diseñadas específicamente para crear y controlar tablas dinámicas. Estas clases permiten crear un objeto [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) y establecer sus propiedades; este objeto constituye la base para crear tablas dinámicas.
Los objetos disponibles para trabajar con tablas dinámicas son:
- [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): representa un campo de una tabla dinámica.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection): representa una colección de todos los objetos [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField) de la tabla dinámica.
- [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): representa una tabla dinámica.
- [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): representa la colección de todos los objetos de tabla dinámica de la hoja de cálculo.
{{% /alert %}}

### **Crear una tabla dinámica sencilla**
La creación de una tabla dinámica es un proceso de tres pasos: escribir los datos de origen en las celdas de la hoja de cálculo, agregar la tabla dinámica en una posición de destino y colocar los campos de la tabla dinámica en las áreas de filas, columnas y datos.
1. Agregue datos a las celdas de la hoja de cálculo mediante el método [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setValue-java.lang.Object-) del objeto [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) (`putValue` en la mayoría de los ejemplos). Estos datos se utilizarán como origen de datos de la tabla dinámica.
2. Agregue una tabla dinámica a la hoja de cálculo llamando al método [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add-com.aspose.cells.PivotTable-int-int-) de la clase [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): `add(sourceData, row, column)`. `sourceData` es el rango de origen (por ejemplo, "A1:C8"); `row` y `column` son las coordenadas basadas en cero de la celda de destino situada en la esquina superior izquierda de la tabla dinámica (la celda E3 corresponde a la fila 2 y la columna 4). El método devuelve directamente el nuevo objeto [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable).
3. Coloque los campos de la tabla dinámica con el método `addFieldToArea` del objeto [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): un nombre de campo se asigna al área de filas (`PivotFieldType.ROW`), al área de columnas (`PivotFieldType.COLUMN`) o al área de datos (`PivotFieldType.DATA`).
4. Guarde el libro de trabajo; la tabla dinámica se incorpora al archivo guardado.
El siguiente ejemplo de código crea una tabla dinámica sencilla siguiendo estos pasos. Al ejecutarse, se agrega a la hoja de cálculo una tabla dinámica basada en los datos de origen:
![todo:image_alt_text](create-pivot-table_1.png)

```java
import com.aspose.cells.*;

// Crear un nuevo libro de trabajo y obtener la primera hoja de cálculo
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();

// Escribir los datos de origen: ventas por deporte y trimestre
cells.get("A1").putValue("Sport");
cells.get("B1").putValue("Quarter");
cells.get("C1").putValue("Sales");
cells.get("A2").putValue("Golf");
cells.get("B2").putValue("Qtr3");
cells.get("C2").putValue(1500);
cells.get("A3").putValue("Golf");
cells.get("B3").putValue("Qtr4");
cells.get("C3").putValue(2000);
cells.get("A4").putValue("Tennis");
cells.get("B4").putValue("Qtr3");
cells.get("C4").putValue(600);
cells.get("A5").putValue("Tennis");
cells.get("B5").putValue("Qtr4");
cells.get("C5").putValue(1500);
cells.get("A6").putValue("Tennis");
cells.get("B6").putValue("Qtr3");
cells.get("C6").putValue(4070);
cells.get("A7").putValue("Tennis");
cells.get("B7").putValue("Qtr4");
cells.get("C7").putValue(5000);
cells.get("A8").putValue("Golf");
cells.get("B8").putValue("Qtr3");
cells.get("C8").putValue(6430);

// Agregar una tabla dinámica en la celda de destino E3, usando A1:C8 como origen
PivotTable pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// Asignar campos de la tabla dinámica: Sport a Filas, Quarter a Columnas, Sales a Datos
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Quarter");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");

// Guardar el libro de trabajo
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
Al asignar un rango de celdas como origen de datos, el rango debe establecerse desde la esquina superior izquierda hasta la esquina inferior derecha. Por ejemplo, "A1:C3" es válido; "C3:A1" no lo es.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}