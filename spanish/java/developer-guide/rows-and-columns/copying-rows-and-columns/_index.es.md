---
title: Copiando Filas y Columnas
type: docs
weight: 30
url: /es/java/copying-rows-and-columns/
---

## **Introducción**
A veces, necesitas copiar filas y columnas en una hoja de cálculo sin copiar toda la hoja. Con Aspose.Cells, es posible copiar filas y columnas dentro o entre libros de trabajo.

Cuando se copia una fila (o columna), se copia también los datos contenidos en ella, incluidas fórmulas - con referencias actualizadas - y valores, comentarios, formato de celdas, celdas ocultas, imágenes y otros objetos de dibujo.
## **Copiando Filas y Columnas con Microsoft Excel**
1. Selecciona la fila o columna que deseas copiar.
1. Para copiar filas o columnas, haz clic en **Copiar** en la barra de herramientas **Estándar**, o presiona **CTRL**+**C**.
1. Selecciona una fila o columna debajo o a la derecha de donde deseas copiar tu selección.
1. Al copiar filas o columnas, haz clic en **Celdas Copiadas** en el menú **Insertar**.

{{% alert color="primary" %}} 

Si haces clic en **Pegar** en la barra de herramientas **Estándar** o presionas **CTRL**+**V** en lugar de hacer clic en un comando en el menú **Insertar**, cualquier contenido de las celdas de destino se reemplaza.

{{% /alert %}} 

## **Copiando una Sola Fila**

Aspose.Cells proporciona el método [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow-com.aspose.cells.Cells-int-int-) de la clase [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Este método copia todo tipo de datos, incluyendo fórmulas, valores, comentarios, formatos de celda, celdas ocultas, imágenes y otros objetos de dibujo desde la fila de origen a la fila de destino.

El método [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow-com.aspose.cells.Cells-int-int-) acepta los siguientes parámetros:

- el objeto de [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) de origen,
- el índice de fila de origen, y
- el índice de fila de destino.

Utiliza este método para copiar una fila dentro de una hoja o a otra hoja. El método [copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow-com.aspose.cells.Cells-int-int-) funciona de manera similar a Microsoft Excel. Por ejemplo, no necesitas establecer explícitamente la altura de la fila de destino, ese valor también se copia.

El siguiente ejemplo muestra cómo copiar una fila en una hoja de cálculo. Utiliza un archivo de plantilla de Microsoft Excel y copia la segunda fila (completa con datos, formato, comentarios, imágenes, etc.) y la pega en la 12ª fila en la misma hoja de cálculo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingRows-CopyingRows.java" >}}



El siguiente resultado se genera cuando se ejecuta el siguiente código.

**La fila se copia con el más alto grado de precisión y exactitud** 

![todo:image_alt_text](copying-rows-and-columns_1.png)

{{% alert color="primary" %}} 

Al copiar filas, es importante tener en cuenta las imágenes relacionadas, gráficos u otros objetos de dibujo, ya que es lo mismo que en Microsoft Excel:

1. Si el índice de fila de origen es 5, la imagen, el gráfico, etc., se copian si están contenidos en las tres filas (el índice de fila de inicio es 4 y el índice de fila final es 6).
1. Las imágenes, gráficos, etc. existentes en la fila de destino no se eliminarán.

{{% /alert %}} 

## **Copia de varias filas**

También puedes copiar varias filas en un nuevo destino mientras usas el método [**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow-com.aspose.cells.Cells-int-int-) que toma un parámetro adicional de tipo entero para especificar la cantidad de filas de origen que se copiarán.

A continuación se muestra una captura de pantalla de la hoja de cálculo de entrada que contiene 3 filas de datos, mientras que el fragmento de código proporcionado a continuación copia las 3 filas a una nueva ubicación a partir de la 7ª fila.

![todo:image_alt_text](copy-rows-and-columns_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleRows-CopyingMultipleRows.java" >}}

Aquí está la vista resultante de la hoja de cálculo después de ejecutar el fragmento de código anterior.

![todo:image_alt_text](copy-rows-and-columns_4.png)

## **Copia de una sola columna**

Aspose.Cells proporciona el método [copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn-com.aspose.cells.Cells-int-int-) de la clase [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), este método copia todo tipo de datos, incluyendo fórmulas (con referencias actualizadas), valores, comentarios, formatos de celda, celdas ocultas, imágenes y otros objetos de dibujo desde la columna fuente a la columna de destino.

El método [copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn-com.aspose.cells.Cells-int-int-) acepta los siguientes parámetros:

- el objeto de [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) de origen,
- índice de columna de origen, y
- el índice de columna de destino.

Utilice el método [copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn-com.aspose.cells.Cells-int-int-) para copiar una columna dentro de una hoja o a otra hoja.

Este ejemplo copia una columna de una hoja de cálculo y la pega en una hoja de cálculo en otro libro.

**Se copia una columna de un libro a otro** 

![todo:image_alt_text](copying-rows-and-columns_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingColumns-CopyingColumns.java" >}}

## **Copiar Múltiples Columnas**

Similar al método [**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow-com.aspose.cells.Cells-int-int-), las APIs de Aspose.Cells también proporcionan el método [**Cells.copyColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns-com.aspose.cells.Cells-int-int-int-) para copiar varias columnas de origen a una nueva ubicación.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleColumns-CopyingMultipleColumns.java" >}}

Así es como se ven las hojas de cálculo de origen y resultado en Excel.

![todo:image_alt_text](copy-rows-and-columns_7.png)

![todo:image_alt_text](copy-rows-and-columns_8.png)


## **Pegar Filas/Columnas con Opciones de Pegado**
Aspose.Cells ahora ofrece [PasteOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PasteOptions) al usar las funciones [CopyRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRows-com.aspose.cells.Cells-int-int-int-com.aspose.cells.CopyOptions-com.aspose.cells.PasteOptions-) y [CopyColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns-com.aspose.cells.Cells-int-int-int-com.aspose.cells.PasteOptions-). Permite configurar las opciones de pegar apropiadas similares a Excel.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-PastingDataWithPasteOptions.java" >}}

{{< app/cells/assistant language="java" >}}
