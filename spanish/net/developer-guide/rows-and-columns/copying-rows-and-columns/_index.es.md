---
title: Copiar filas y columnas
type: docs
weight: 40
url: /es/net/copying-rows-and-columns/
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

## **Pegar filas y columnas usando opciones de pegado con Microsoft Excel**

1. Seleccione las celdas que contienen los datos u otros atributos que desea copiar.
1.  En la pestaña Inicio, haga clic en**Copiar**.
1.  Haga clic en la primera celda en el área donde desea**pegar** lo que copiaste.
1.  En la pestaña Inicio, haga clic en la flecha junto a**Pegar** y luego seleccione**Pegar** Especial.
1.  Selecciona el**opciones** usted quiere.

## **Usando Aspose.Cells**

## **Copiar filas individuales**

 Aspose.Cells proporciona el[**Copiar fila**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) metodo de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)clase. Este método copia todos los tipos de datos, incluidas fórmulas, valores, comentarios, formatos de celda, celdas ocultas, imágenes y otros objetos de dibujo de la fila de origen a la fila de destino.

 los[**Copiar fila**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)método toma los siguientes parámetros:

-  la fuente[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)objeto,
- el índice de la fila de origen, y
- el índice de la fila de destino.

 Utilice este método para copiar una fila dentro de una hoja o en otra hoja. los[**Copiar fila**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)El método funciona de manera similar a Microsoft Excel. Entonces, por ejemplo, no necesita establecer la altura de la fila de destino explícitamente, ese valor también se copia.

El siguiente ejemplo muestra cómo copiar una fila en una hoja de cálculo. Utiliza un archivo de Excel de plantilla Microsoft y copia la segunda fila (completa con datos, formato, comentarios, imágenes, etc.) y la pega en la fila 12 en la misma hoja de trabajo.

 Puede omitir el paso que obtiene la altura de la fila de origen utilizando el[**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight) y luego establece la altura de la fila de destino usando el[**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) método como el[**Copiar fila**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)El método se ocupa automáticamente de la altura de la fila.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

Al copiar filas, es importante tener en cuenta las imágenes, gráficos u otros objetos de dibujo relacionados, ya que esto es lo mismo con Microsoft Excel:

1. Si el índice de la fila de origen es 5, la imagen, el gráfico, etc., se copia si está contenido en las tres filas (el índice de la fila inicial es 4 y el índice de la fila final es 6).
1. Las imágenes, gráficos, etc. existentes en la fila de destino no se eliminarán.

{{% /alert %}}

## **Copiar varias filas**

También puede copiar varias filas en un nuevo destino mientras usa el[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)método que toma un parámetro adicional de tipo entero para especificar el número de filas de origen que se van a copiar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


## **Copiando columnas**

 Aspose.Cells proporciona el[**Copiar columna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) metodo de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)clase, este método copia todo tipo de datos, incluidas fórmulas, con referencias actualizadas, y valores, comentarios, formatos de celda, celdas ocultas, imágenes y otros objetos de dibujo de la columna de origen a la columna de destino.

 los[**Copiar columna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)método toma los siguientes parámetros:

-  la fuente[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)objeto,
- índice de la columna fuente, y
- el índice de la columna de destino.

 Utilizar el[**Copiar columna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)método para copiar una columna dentro de una hoja o en otra hoja.

Este ejemplo copia una columna de una hoja de cálculo y la pega en una hoja de cálculo de otro libro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

## **Copiar varias columnas**

 Similar a[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) método, las API Aspose.Cells también proporcionan el[**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index)método para copiar varias columnas de origen en una nueva ubicación.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


## **Pegar filas/columnas con opciones de pegado**

 Aspose.Cells ahora proporciona[**PasteOptions**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions) durante el uso de funciones[**Copiar filas**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2) y[**Copiar columnas**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1). Permite establecer la opción de pegado apropiada similar a Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

