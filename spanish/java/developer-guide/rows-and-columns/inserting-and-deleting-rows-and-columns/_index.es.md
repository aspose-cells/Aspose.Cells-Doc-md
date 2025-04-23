---
title: Inserción y Eliminación de Filas y Columnas
type: docs
weight: 60
url: /es/java/inserting-and-deleting-rows-and-columns/
description: Aprenda cómo Insertar y Eliminar Filas y Columnas a través de las APIs Aspose.Cells for Java.
keywords: Cómo Insertar y Eliminar Filas y Columnas en Java, Insertar Filas y Columnas Usando Java, Eliminar Filas y Columnas en Java, Insertar Filas o Columnas con Java, Eliminar Filas o Columnas via Java.
---

## **Introducción**
Ya sea creando una nueva hoja de cálculo desde cero o trabajando en una hoja de cálculo existente, puede ser necesario agregar filas o columnas adicionales para acomodar más datos. Inversamente, también puede ser necesario eliminar filas o columnas de posiciones específicas en la hoja de cálculo.

Para cumplir con estos requisitos, Aspose.Cells proporciona un conjunto muy simple de clases y métodos, discutidos a continuación.
## **Cómo Gestionar Filas/Columnas**
Aspose.Cells proporciona una clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) que permite acceder a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) proporciona una colección de [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) que representa todas las celdas en la hoja de cálculo.

La colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) ofrece varios métodos para gestionar filas y columnas en una hoja de cálculo. Algunos de estos se discuten a continuación.

{{% alert color="primary" %}} 

Cuando se agregan filas o columnas, el contenido de la hoja de cálculo se desplaza hacia abajo o hacia la derecha, pero si se eliminan filas o columnas, el contenido se desplaza hacia arriba o hacia la izquierda.

{{% /alert %}} 
## **Cómo insertar una fila**
Insertar una fila en cualquier lugar llamando al método [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) de la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). El método [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) acepta como primer argumento el índice de la fila donde se insertará la nueva fila y como segundo argumento la cantidad de filas a insertar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
## **Cómo insertar múltiples filas**
Para insertar varias filas en la hoja de cálculo, llame al método [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) de la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). El método [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) acepta dos parámetros:

- Índice de fila: el índice de la fila desde donde se insertarán las nuevas filas.
- Número de filas: el número total de filas que se deben insertar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
## **Cómo insertar una fila con formato**
Para insertar una fila con opciones de formato, use la sobrecarga [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-com.aspose.cells.InsertOptions-) que toma [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) como parámetro. Establezca la propiedad [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType) de la clase [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) con la Enumeración [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType). La Enumeración [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType) tiene tres miembros como se lista a continuación.

- [SAME_AS_ABOVE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME-AS-ABOVE): Formatea la fila igual que la fila de arriba.
- [SAME_AS_BELOW](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME-AS-BELOW): Formatea la fila igual que la fila de abajo.
- [CLEAR](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): Borra el formato.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
## **Cómo borrar una fila**
Para eliminar una fila en cualquier ubicación, llame al método [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) de la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). El método [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) toma dos parámetros:

- Índice de fila: el índice de la fila desde donde se borrarán las filas.
- Número de filas: el número total de filas que deben eliminarse.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
## **Cómo borrar múltiples filas**
Para eliminar varias filas de una hoja de cálculo, llame al método [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) de la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). El método [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) toma dos parámetros:

- Índice de fila: el índice de la fila desde donde se borrarán las filas.
- Número de filas: el número total de filas que deben eliminarse.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
## **Cómo insertar una o varias columnas**
Los desarrolladores también pueden insertar una columna en la hoja de cálculo en cualquier ubicación llamando al método [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns-int-int-) de la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). El método [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns-int-int-) toma dos parámetros:

- Índice de la columna, el índice de la columna desde donde se insertará la columna
- Número de columnas, el número total de columnas que deben ser insertadas

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
## **Cómo eliminar una columna**
Para eliminar una columna de la hoja de cálculo en cualquier ubicación, llame al método [deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns-int-int-boolean-) de la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). El método [deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns-int-int-boolean-) toma los siguientes parámetros:

- Índice de la columna: el índice de la columna desde donde se eliminará la columna.
- Número de columnas: el número total de columnas que deben ser eliminadas.
- Actualizar referencia: parámetro booleano para indicar si se deben actualizar las referencias en otras hojas de cálculo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

{{< app/cells/assistant language="java" >}}
