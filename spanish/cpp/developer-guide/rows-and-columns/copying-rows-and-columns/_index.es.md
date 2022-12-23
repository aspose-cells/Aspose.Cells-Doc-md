---
title: Copiar filas y columnas
type: docs
weight: 20
url: /es/cpp/copying-rows-and-columns/
---
## **Introducción**
A veces necesita copiar filas y columnas en una hoja de trabajo sin copiar toda la hoja de trabajo. Con Aspose.Cells, es posible copiar filas y columnas dentro o entre libros de trabajo.
Cuando se copia una fila (o columna), también se copian los datos contenidos en ella, incluidas las fórmulas (con referencias actualizadas), los valores, los comentarios, el formato, las celdas ocultas, las imágenes y otros objetos de dibujo.
## **Copiar filas y columnas con Microsoft Excel**
1. Seleccione la fila o columna que desea copiar.
1.  Para copiar filas o columnas, haga clic en**Copiar** sobre el**Estándar** barra de herramientas, o presione**CONTROL**+**C**.
1. Seleccione una fila o columna debajo o a la derecha de donde desea copiar su selección.
1.  Cuando esté copiando filas o columnas, haga clic en**Copiado Cells** sobre el**Insertar** menú.

{{% alert color="primary" %}} 

 si haces clic**Pegar** sobre el**Estándar** barra de herramientas o presione**CONTROL**+** V** en lugar de hacer clic en un comando en el**menú Insertar**, se reemplaza cualquier contenido de las celdas de destino.

{{% /alert %}} 
## **Usando Aspose.Cells**
### **Copiar filas**
Aspose.Cells proporciona el método CopyRow de la clase Aspose::Cells::ICells. Este método copia todos los tipos de datos, incluidas fórmulas, valores, comentarios, formatos de celda, celdas ocultas, imágenes y otros objetos de dibujo de la fila de origen a la fila de destino.

El método CopyRow toma los siguientes parámetros:

- el objeto fuente Cells,
- el índice de la fila de origen, y
- el índice de la fila de destino.

Utilice este método para copiar una fila dentro de una hoja o en otra hoja. El método CopyRow funciona de manera similar a Microsoft Excel. Entonces, por ejemplo, no necesita establecer la altura de la fila de destino explícitamente, ese valor también se copia.

El siguiente ejemplo muestra cómo copiar una fila en una hoja de cálculo. Utiliza un archivo de Excel de plantilla Microsoft y copia la segunda fila (completa con datos, formato, comentarios, imágenes, etc.) y la pega en la fila 12 en la misma hoja de trabajo.

 Puede omitir el paso que obtiene la altura de la fila de origen utilizando el**ObtenerAlturaDeFila** y luego establece la altura de la fila de destino usando el**EstablecerRowHeight** método como el**Copiar fila** El método se ocupa automáticamente de la altura de la fila.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingRows.cpp" >}}

{{% alert color="primary" %}} 

Al copiar filas, es importante tener en cuenta las imágenes, gráficos u otros objetos de dibujo relacionados, ya que esto es lo mismo con Microsoft Excel:

1. Si el índice de la fila de origen es 5, la imagen, el gráfico, etc., se copia si está contenido en las tres filas (el índice de la fila inicial es 4 y el índice de la fila final es 6).
1. Las imágenes, gráficos, etc. existentes en la fila de destino no se eliminarán.

{{% /alert %}} 
### **Copiando columnas**
Aspose.Cells proporciona el método CopyColumn de la clase Aspose::Cells::ICells, este método copia todo tipo de datos, incluidas fórmulas, con referencias actualizadas, y valores, comentarios, formatos de celda, celdas ocultas, imágenes y otros objetos de dibujo de la fuente. columna a la columna de destino.

El método CopyColumn toma los siguientes parámetros:

- el objeto fuente Cells,
- índice de la columna fuente, y
- el índice de la columna de destino.

Utilice el método CopyColumn para copiar una columna dentro de una hoja o en otra hoja.

Este ejemplo copia una columna de una hoja de cálculo y la pega en una hoja de cálculo de otro libro.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-CopyingRowsAndColumns-CopyingColumns.cpp" >}}
