---
title: Agrupando y Desagrupando Filas y Columnas
type: docs
weight: 40
url: /es/java/grouping-and-ungrouping-rows-and-columns/
---

## **Introducción**
En un archivo de Microsoft Excel, puedes crear un esquema para los datos que te permita mostrar y ocultar niveles de detalle con un solo clic de ratón.

Haz clic en los **Símbolos de Esquema**, 1,2,3, + y - para mostrar rápidamente solo las filas o columnas que proporcionen resúmenes o encabezados para secciones en una hoja de cálculo, o puedes usar los símbolos para ver detalles bajo un resumen o encabezado individual como se muestra a continuación en la figura:

Agrupación de filas y columnas 

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)
## **Gestión de Agrupación de Filas y Columnas**
Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una colección [Worksheets](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) proporciona una colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) que representa todas las celdas en la hoja de cálculo.

La colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) proporciona varios métodos para gestionar filas o columnas en una hoja de cálculo, algunos de los cuales se discuten a continuación con más detalle.
### **Agrupación de Filas y Columnas**
Es posible agrupar filas o columnas llamando a los métodos [groupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupRows\(int,%20int,%20boolean\)) y [groupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupColumns\(int,%20int,%20boolean\)) de la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Ambos métodos toman los siguientes parámetros:

- Índice de la primera fila/columna, la primera fila o columna del grupo.
- Índice de la última fila/columna, la última fila o columna del grupo.
- Está oculto, un parámetro booleano que especifica si ocultar o no filas/columnas después de agrupar.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-GroupingRowsandColumns-1.java" >}}
## **Configuración de Grupo**
Microsoft Excel también permite configurar ajustes de grupo para mostrar:

- Filas resumen debajo del detalle.
- Columnas resumen a la derecha del detalle.

**Ajustes de Grupo** 

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_2.png)

Es posible configurar estos ajustes de grupo usando la propiedad Outline de la clase Worksheet.
### **Filas Resumen Debajo del Detalle**
Los desarrolladores pueden controlar la visualización de las filas resumen debajo del detalle usando el método [SummaryRowBelow](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) de la clase [Outline](https://reference.aspose.com/cells/java/com.aspose.cells/Outline).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowBelow-1.java" >}}
### **Columnas Resumen a la Derecha del Detalle**
Es posible controlar si se muestran las columnas resumen a la derecha de los detalles con el método [SummaryColumnRight](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryColumnRight) de la clase [Outline](https://reference.aspose.com/cells/java/com.aspose.cells/Outline).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowRight-1.java" >}}
### **Desagrupar Filas y Columnas**
Desagrupar filas o columnas agrupadas llamando a los métodos [UngroupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupRows\(int,%20int\)) y [UngroupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupColumns\(int,%20int\)) de la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Ambos métodos toman los mismos parámetros:

- Índice de la primera fila o columna, la primera fila/columna a desagrupar.
- Índice de la última fila o columna, la última fila/columna a desagrupar.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UngroupingRowsandColumns-UngroupingRowsandColumns.java" >}}
