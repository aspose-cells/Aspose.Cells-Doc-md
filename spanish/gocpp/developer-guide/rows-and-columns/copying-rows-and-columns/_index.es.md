---
title: Copiando Filas y Columnas
type: docs
weight: 20
url: /es/go-cpp/copying-rows-and-columns/
---

## **Introducción**

A veces es necesario copiar filas y columnas en una hoja de cálculo sin copiar la hoja de cálculo completa. Con Aspose.Cells, es posible copiar filas y columnas dentro o entre libros de trabajo.
Cuando se copia una fila (o columna), los datos contenidos en ella, incluidas las fórmulas, con referencias actualizadas, y valores, comentarios, formato, celdas ocultas, imágenes y otros objetos de dibujo también se copian.

## **Copiando Filas y Columnas con Microsoft Excel**

1. Selecciona la fila o columna que deseas copiar.
1. Para copiar filas o columnas, haz clic en **Copiar** en la barra de herramientas **Estándar**, o presiona **CTRL**+**C**.
1. Selecciona una fila o columna debajo o a la derecha de donde deseas copiar tu selección.
1. Al copiar filas o columnas, haz clic en **Celdas Copiadas** en el menú **Insertar**.

{{% alert color="primary" %}}

Si haces clic en **Pegar** en la barra de herramientas **Estándar** o presionas **CTRL**+**V** en lugar de hacer clic en un comando en el menú **Insertar**, el contenido de las celdas de destino se reemplaza.

{{% /alert %}}

## **Usar Aspose.Cells**

### **Copiando Filas**

Aspose.Cells proporciona el método CopyRow de la clase Aspose::Cells::ICells. Este método copia todo tipo de datos, incluidas fórmulas, valores, comentarios, formatos de celda, celdas ocultas, imágenes y otros objetos de dibujo desde la fila de origen a la fila de destino.

El método CopyRow toma los siguientes parámetros:

- el objeto Cells fuente,
- el índice de fila de origen, y
- el índice de fila de destino.

Utiliza este método para copiar una fila dentro de una hoja, o a otra hoja. El método CopyRow funciona de manera similar a Microsoft Excel. Por lo tanto, por ejemplo, no necesitas establecer la altura de la fila de destino explícitamente, ese valor también se copia.

El siguiente ejemplo muestra cómo copiar una fila en una hoja de cálculo. Utiliza un archivo de plantilla de Microsoft Excel y copia la segunda fila (completa con datos, formato, comentarios, imágenes, etc.) y la pega en la duodécima fila en la misma hoja de cálculo.

Puedes omitir el paso que obtiene la altura de la fila de origen usando el método **GetRowHeigh** y luego establece la altura de la fila de destino usando el método **SetRowHeight** ya que el método **CopyRow** se encarga automáticamente de la altura de la fila.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyingRows.go" >}}

{{% alert color="primary" %}}

Al copiar filas, es importante tener en cuenta las imágenes relacionadas, gráficos u otros objetos de dibujo, ya que es lo mismo que en Microsoft Excel:

1. Si el índice de fila de origen es 5, la imagen, gráfico, etc., se copia si está contenida en las tres filas (el índice de fila de inicio es 4 y el índice de fila final es 6).
1. Las imágenes, gráficos, etc., existentes en la fila de destino no se eliminarán.

{{% /alert %}}

### **Copiar columnas**

Aspose.Cells proporciona el método CopyColumn de la clase ICells, que copia todo tipo de datos, incluyendo fórmulas - con referencias actualizadas - y valores, comentarios, formatos de celda, celdas ocultas, imágenes y otros objetos de dibujo desde la columna de origen a la columna de destino.

El método CopyColumn toma los siguientes parámetros:

- el objeto Cells fuente,
- índice de columna de origen, y
- el índice de columna de destino.

Utilice el método CopyColumn para copiar una columna dentro de una hoja o hacia otra hoja.

Este ejemplo copia una columna de una hoja de cálculo y la pega en una hoja de cálculo en otro libro.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyingColumns.go" >}}
