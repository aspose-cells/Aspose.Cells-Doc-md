---
title: Agrupación y desagrupación de filas y columnas
type: docs
weight: 40
url: /es/java/grouping-and-ungrouping-rows-and-columns/
---
## **Introducción**
En un archivo de Excel Microsoft, puede crear un esquema para los datos que le permita mostrar y ocultar niveles de detalle con un solo clic del mouse.

 Haga clic en el**Símbolos de contorno**, 1, 2, 3, + y - para mostrar rápidamente solo las filas o columnas que proporcionan resúmenes o encabezados para las secciones de una hoja de trabajo, o puede usar los símbolos para ver los detalles bajo un resumen o encabezado individual como se muestra a continuación en la figura :

 Agrupación de filas y columnas

![todo:imagen_alternativa_texto](grouping-and-ungrouping-rows-and-columns_1.png)
## **Gestión de grupos de filas y columnas**
 Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) que representa un archivo de Excel Microsoft. los[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la clase contiene un[Hojas de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) colección que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) clase. los[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la clase proporciona un[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)colección que representa todas las celdas de la hoja de trabajo.

 los[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection proporciona varios métodos para administrar filas o columnas en una hoja de trabajo, algunos de estos se analizan a continuación con más detalle.
### **Agrupación de filas y columnas**
 Es posible agrupar filas o columnas llamando al[filas de grupos](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupRows\(int,%20int,%20boolean\) ) y[grupoColumnas](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupColumns\(int,%20int,%20boolean\) ) métodos de[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)recopilación. Ambos métodos toman los siguientes parámetros:

- Índice de la primera fila/columna, la primera fila o columna del grupo.
- Índice de última fila/columna, la última fila o columna del grupo.
- Está oculto, un parámetro booleano que especifica si ocultar filas/columnas después de la agrupación o no.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-GroupingRowsandColumns-1.java" >}}
## **Configuración de grupo**
Microsoft Excel también permite configurar ajustes de grupo para mostrar:

- Filas de resumen debajo del detalle.
- Columnas de resumen a la derecha del detalle.

**Configuraciones de grupo** 

![todo:imagen_alternativa_texto](grouping-and-ungrouping-rows-and-columns_2.png)

Es posible configurar estos ajustes de grupo utilizando la propiedad Esquema de la clase Hoja de trabajo.
### **Filas de resumen debajo del detalle**
 Los desarrolladores pueden controlar la visualización de filas de resumen debajo del detalle mediante el uso de[Esquema](https://reference.aspose.com/cells/java/com.aspose.cells/Outline) clase'[ResumenFilaDebajo](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) método.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowBelow-1.java" >}}
### **Columnas de resumen a la derecha del detalle**
Es posible controlar si las columnas de resumen se muestran a la derecha de los detalles con el[Esquema](https://reference.aspose.com/cells/java/com.aspose.cells/Outline) clase'[ResumenColumnaDerecha](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryColumnRight)método.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowRight-1.java" >}}
### **Desagrupar filas y columnas**
 Desagrupa filas o columnas agrupadas llamando al[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) colección[Desagrupar filas](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupRows\(int,%20int\) ) y[DesagruparColumnas](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupColumns\(int,%20int\)) métodos. Ambos métodos toman los mismos parámetros:

- Índice de la primera fila o columna, la primera fila/columna a desagrupar.
- Índice de la última fila o columna, la última fila/columna a desagrupar.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UngroupingRowsandColumns-UngroupingRowsandColumns.java" >}}
