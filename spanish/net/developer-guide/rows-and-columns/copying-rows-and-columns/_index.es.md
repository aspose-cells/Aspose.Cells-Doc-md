---
title: Copiar filas y columnas
type: docs
weight: 40
url: /es/net/copying-rows-and-columns/
description: Este artículo muestra cómo copiar filas y columnas a través de Aspose.Cells for .NET API.
keywords: C# How to Copy Rows and Columns, Copy Rows in C#, Copy Columns using C#, How to Paste Rows and Columns using Aspose.Cells for .NET, Paste multiple rows and columns, How to Copy and paste Single Row or Column.
---
##  **Introducción**

A veces, es necesario copiar filas y columnas de una hoja de cálculo sin copiar toda la hoja de cálculo. Con Aspose.Cells, es posible copiar filas y columnas dentro o entre libros.
Cuando se copia una fila (o columna), también se copian los datos contenidos en ella, incluidas fórmulas (con referencias actualizadas) y valores, comentarios, formato, celdas ocultas, imágenes y otros objetos de dibujo.

##  **Cómo copiar filas y columnas con Microsoft Excel**

1. Seleccione la fila o columna que desea copiar.
1.  Para copiar filas o columnas, haga clic en**Copiar** sobre el**Estándar** barra de herramientas o presione**CTRL**+*C**.
1. Seleccione una fila o columna debajo o a la derecha de donde desea copiar su selección.
1.  Cuando esté copiando filas o columnas, haga clic en**Copiado Cells** sobre el**Insertar** menú.

{{% alert color="primary" %}}

 Si haces clic**Pegar** sobre el**Estándar** barra de herramientas o presione**CTRL**+**V** en lugar de hacer clic en un comando en **Insertar**menú, se reemplaza cualquier contenido de las celdas de destino.

{{% /alert %}}

##  **Cómo pegar filas y columnas usando las opciones de pegado con Microsoft Excel**

1. Seleccione las celdas que contienen los datos u otros atributos que desea copiar.
1. En la pestaña Inicio, haga clic en *Copiar**.
1.  Haga clic en la primera celda en el área donde desea**pegar** lo que copiaste.
1.  En la pestaña Inicio, haga clic en la flecha junto a**Pegar** y luego seleccione **Pegar** Especial.
1.  Selecciona el**opciones** quieres.

##  **Cómo copiar filas y columnas usando Aspose.Cells for .NET**

##  **Cómo copiar filas individuales**

 Aspose.Cells proporciona la[**Copiar fila**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) método de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)clase. Este método copia todo tipo de datos, incluidas fórmulas, valores, comentarios, formatos de celda, celdas ocultas, imágenes y otros objetos de dibujo desde la fila de origen a la fila de destino.

 El[**Copiar fila**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)El método toma los siguientes parámetros:

-  la fuente[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)objeto,
- el índice de la fila de origen, y
- el índice de la fila de destino.

 Utilice este método para copiar una fila dentro de una hoja o en otra hoja. El[**Copiar fila**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)El método funciona de manera similar a Microsoft Excel. Entonces, por ejemplo, no es necesario establecer explícitamente la altura de la fila de destino, ese valor también se copia.

El siguiente ejemplo muestra cómo copiar una fila en una hoja de trabajo. Utiliza un archivo de Excel de plantilla Microsoft y copia la segunda fila (completa con datos, formato, comentarios, imágenes, etc.) y la pega en la fila 12 de la misma hoja de trabajo.

 Puede omitir el paso que obtiene la altura de la fila de origen usando el[**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight) método y luego establece la altura de la fila de destino usando el[**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) método como el[**Copiar fila**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)El método se encarga automáticamente de la altura de la fila.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

Al copiar filas, es importante tener en cuenta las imágenes, gráficos u otros objetos de dibujo relacionados, ya que ocurre lo mismo con Microsoft Excel:

1. Si el índice de la fila de origen es 5, la imagen, el gráfico, etc., se copia si está contenido en las tres filas (el índice de la fila inicial es 4 y el índice de la fila final es 6).
1. Las imágenes, gráficos, etc. existentes en la fila de destino no se eliminarán.

{{% /alert %}}

##  **Cómo copiar varias filas**

También puede copiar varias filas en un nuevo destino mientras usa el[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)método que toma un parámetro adicional de tipo entero para especificar el número de filas de origen que se copiarán.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


##  **Cómo copiar columnas**

 Aspose.Cells proporciona la[**Copiar columna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) método de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)clase, este método copia todo tipo de datos, incluidas fórmulas (con referencias actualizadas) y valores, comentarios, formatos de celda, celdas ocultas, imágenes y otros objetos de dibujo desde la columna de origen a la columna de destino.

 El[**Copiar columna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)El método toma los siguientes parámetros:

-  la fuente[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)objeto,
- índice de la columna de origen, y
- el índice de la columna de destino.

 Utilizar el[**Copiar columna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)Método para copiar una columna dentro de una hoja o en otra hoja.

Este ejemplo copia una columna de una hoja de trabajo y la pega en una hoja de trabajo de otro libro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

##  **Cómo copiar varias columnas**

 Similar a[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) método, las API Aspose.Cells también proporcionan la[**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index)método para copiar varias columnas de origen a una nueva ubicación.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


##  **Cómo pegar filas y columnas con opciones de pegado**

 Aspose.Cells ahora proporciona[**Opciones de pegado**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions) mientras usa funciones[**Copiar filas**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2) y[**Copiar columnas**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1). Permite configurar la opción de pegado adecuada similar a Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

