---
title: Insertar y eliminar filas y columnas
type: docs
weight: 60
url: /es/java/inserting-and-deleting-rows-and-columns/
description: Aprenda a insertar y eliminar filas y columnas a través de las API Aspose.Cells for Java.
keywords: How to Insert and Delete Rows and Columns in Java, Insert Rows and Columns using Java, Java Delete Rows and Columns, Insert Rows or Columns with Java, Delete Rows or Columns via Java.
---
##  **Introducción**
Ya sea que creemos una nueva hoja de trabajo desde cero o trabajemos en una hoja de trabajo existente, es posible que necesitemos agregar filas o columnas adicionales para acomodar más datos. A la inversa, es posible que también necesitemos eliminar filas o columnas de posiciones específicas en la hoja de trabajo.

Para cumplir con estos requisitos, Aspose.Cells proporciona un conjunto de clases y métodos muy simple, que se analiza a continuación.
##  **Cómo administrar filas/columnas**
 Aspose.Cells proporciona un[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) clase que representa un archivo Excel Microsoft. El[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la clase contiene un[Colección de hojas de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) que permite el acceso a cada hoja de cálculo en un archivo Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) clase. El[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) clase proporciona un[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)colección que representa todas las celdas de la hoja de trabajo.

 El[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)La colección proporciona varios métodos para administrar filas y columnas en una hoja de trabajo. Algunos de éstos se discuten a continuación.

{{% alert color="primary" %}} 

Cuando se agregan filas o columnas, el contenido de la hoja de cálculo se desplaza hacia abajo o hacia la derecha, pero si se eliminan filas o columnas, el contenido se desplaza hacia arriba o hacia la izquierda.

{{% /alert %}} 
##  **Cómo insertar una fila**
 Inserte una fila en cualquier ubicación llamando al[insertar filas](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) método de la[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) recopilación. El[insertar filas](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\))El método toma el índice de la fila donde se insertará la nueva fila como primer argumento y el número de filas que se insertarán como segundo argumento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
##  **Cómo insertar varias filas**
 Para insertar varias filas en la hoja de trabajo, llame al[insertar filas](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) método de la[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) recopilación. El[insertar filas](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) El método toma dos parámetros:

- Índice de fila: el índice de la fila desde donde se insertarán las nuevas filas.
- Número de filas: el número total de filas que deben insertarse.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
##  **Cómo insertar una fila con formato**
Para insertar una fila con opciones de formato, utilice el[insertar filas](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int,%20com.aspose.cells.InsertOptions\)sobrecarga que lleva[Insertar opciones](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)como parámetro. Selecciona el[Tipo de formato de copia](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType)propiedad de[Insertar opciones](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)clase con[Tipo de formato de copia](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)Enumeración. El[Tipo de formato de copia](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)La enumeración tiene tres miembros como se enumeran a continuación.

- [SAME_AS_ABOVE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_ABOVE): formatea la fila igual que la fila anterior.
- [SAME_AS_BELOW](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_BELOW): formatea la fila igual que la siguiente.
- [CLEAR](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): borra el formato.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
##  **Cómo eliminar una fila**
 Para eliminar una fila en cualquier ubicación, llame al[eliminar filas](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) método de la[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) recopilación. El[eliminar filas](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) El método toma dos parámetros:

- Índice de fila: el índice de la fila desde donde se eliminarán las filas.
- Número de filas: el número total de filas que deben eliminarse.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
##  **Cómo eliminar varias filas**
 Para eliminar varias filas de una hoja de cálculo, llame al[eliminar filas](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) método de la[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) recopilación. El[eliminar filas](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) El método toma dos parámetros:

- Índice de fila: el índice de la fila desde donde se eliminarán las filas.
- Número de filas: el número total de filas que deben eliminarse.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
##  **Cómo insertar una o varias columnas**
 Los desarrolladores también pueden insertar una columna en la hoja de trabajo en cualquier ubicación llamando al[insertar columnas](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\) ) método de la[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)recopilación. El[insertar columnas](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)) El método toma dos parámetros:

- Índice de columna, el índice de la columna desde donde se insertará la columna
- Número de columnas, el número total de columnas que deben insertarse

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
##  **Cómo eliminar una columna**
 Para eliminar una columna de la hoja de cálculo en cualquier ubicación, llame al[eliminar columnas](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\) ) método de la[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) recopilación. El[eliminar columnas](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\)) El método toma los siguientes parámetros:

- Índice de columna: el índice de la columna desde donde se eliminará la columna.
- Número de columnas: el número total de columnas que deben eliminarse.
- Actualizar referencia: parámetro booleano para indicar si se actualizan referencias en otras hojas de trabajo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

