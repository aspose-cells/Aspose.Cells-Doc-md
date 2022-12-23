---
title: Copiar filas y columnas
type: docs
weight: 30
url: /es/java/copying-rows-and-columns/
---
## **Introducción**
A veces, necesita copiar filas y columnas en una hoja de trabajo sin copiar toda la hoja de trabajo. Con Aspose.Cells, es posible copiar filas y columnas dentro o entre libros de trabajo.

Cuando se copia una fila (o columna), también se copian los datos contenidos en ella, incluidas las fórmulas (con referencias actualizadas), los valores, los comentarios, el formato, las celdas ocultas, las imágenes y otros objetos de dibujo.
## **Copiar filas y columnas con Microsoft Excel**
1. Seleccione la fila o columna que desea copiar.
1.  Para copiar filas o columnas, haga clic en**Copiar** sobre el**Estándar** barra de herramientas, o presione**CONTROL**+**C**.
1. Seleccione una fila o columna debajo o a la derecha de donde desea copiar su selección.
1.  Cuando esté copiando filas o columnas, haga clic en**Copiado Cells** sobre el**Insertar** menú.

{{% alert color="primary" %}} 

 si haces clic**Pegar** sobre el**Estándar** barra de herramientas o presione**CONTROL**+** V** en lugar de hacer clic en un comando en el**En el menú Insertar**, se reemplaza cualquier contenido de las celdas de destino.

{{% /alert %}} 

## **Copiar una sola fila**

 Aspose.Cells proporciona el[copia fila](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\) ) método de la[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)clase. Este método copia todos los tipos de datos, incluidas fórmulas, valores, comentarios, formatos de celda, celdas ocultas, imágenes y otros objetos de dibujo de la fila de origen a la fila de destino.

 Él[copia fila](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) método toma los siguientes parámetros:

-  la fuente[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)objeto,
- el índice de la fila de origen, y
- el índice de la fila de destino.

 Utilice este método para copiar una fila dentro de una hoja o en otra hoja. Él[copia fila](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)) funciona de manera similar a Microsoft Excel. Entonces, por ejemplo, no necesita establecer la altura de la fila de destino explícitamente, ese valor también se copia.

El siguiente ejemplo muestra cómo copiar una fila en una hoja de cálculo. Utiliza un archivo de Excel de plantilla Microsoft y copia la segunda fila (completa con datos, formato, comentarios, imágenes, etc.) y la pega en la fila 12 en la misma hoja de trabajo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingRows-CopyingRows.java" >}}



El siguiente resultado se genera cuando se ejecuta el siguiente código.

**La fila se copia con el mayor grado de precisión y exactitud.** 

![todo:imagen_alternativa_texto](copying-rows-and-columns_1.png)

{{% alert color="primary" %}} 

Al copiar filas, es importante tener en cuenta las imágenes, gráficos u otros objetos de dibujo relacionados, ya que esto es lo mismo con Microsoft Excel:

1. Si el índice de la fila de origen es 5, la imagen, el gráfico, etc., se copia si está contenido en las tres filas (el índice de la fila inicial es 4 y el índice de la fila final es 6).
1. Las imágenes, gráficos, etc. existentes en la fila de destino no se eliminarán.

{{% /alert %}} 

## **Copiar varias filas**

 También puede copiar varias filas en un nuevo destino mientras usa el[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int)) que toma un parámetro adicional de tipo entero para especificar el número de filas de origen que se van a copiar.

continuación se muestra una instantánea de la hoja de cálculo de entrada que contiene 3 filas de datos, mientras que el fragmento de código proporcionado a continuación copia las 3 filas en una nueva ubicación a partir de la 7.ª fila.

![todo:imagen_alternativa_texto](copy-rows-and-columns_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleRows-CopyingMultipleRows.java" >}}

Aquí está la vista de hoja de cálculo resultante después de ejecutar el fragmento de código anterior.

![todo:imagen_alternativa_texto](copy-rows-and-columns_4.png)

## **Copiar una sola columna**

 Aspose.Cells proporciona el[copiarColumna](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\) ) método de la[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)clase, este método copia todo tipo de datos, incluidas fórmulas, con referencias actualizadas, y valores, comentarios, formatos de celda, celdas ocultas, imágenes y otros objetos de dibujo de la columna de origen a la columna de destino.

 Él[copiarColumna](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) método toma los siguientes parámetros:

-  la fuente[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)objeto,
- índice de la columna fuente, y
- el índice de la columna de destino.

 Utilizar el[copiarColumna](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) método para copiar una columna dentro de una hoja o en otra hoja.

Este ejemplo copia una columna de una hoja de cálculo y la pega en una hoja de cálculo de otro libro.

**Una columna se copia de un libro de trabajo a otro** 

![todo:imagen_alternativa_texto](copying-rows-and-columns_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingColumns-CopyingColumns.java" >}}

## **Copiar varias columnas**

 Similar a[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int) ), las API Aspose.Cells también proporcionan el[**Cells.copyColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns(com.aspose.cells.Cells,%20int,%20int,%20int)) para copiar varias columnas de origen en una nueva ubicación.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleColumns-CopyingMultipleColumns.java" >}}

Así es como se ven las hojas de cálculo de origen y resultantes en Excel.

![todo:imagen_alternativa_texto](copy-rows-and-columns_7.png)

![todo:imagen_alternativa_texto](copy-rows-and-columns_8.png)


## **Pegar filas/columnas con opciones de pegado**
 Aspose.Cells ahora proporciona[PasteOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PasteOptions) durante el uso de funciones[Copiar filas](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRows\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.CopyOptions,%20com.aspose.cells.PasteOptions\) ) y[Copiar columnas](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.PasteOptions\)). Permite configurar opciones de pegado apropiadas similares a Excel.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-PastingDataWithPasteOptions.java" >}}

