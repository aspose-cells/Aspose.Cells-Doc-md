---
title: Copiando Filas y Columnas
type: docs
weight: 40
url: /es/net/copying-rows-and-columns/
description: Este artículo muestra cómo copiar filas y columnas a través de la API Aspose.Cells for .NET.
keywords: C# Cómo Copiar Filas y Columnas, Copiar Filas en C#, Copiar Columnas usando C#, Cómo Pegar Filas y Columnas usando Aspose.Cells for .NET, Pegar múltiples filas y columnas, Cómo copiar y pegar una sola fila o columna.
---

## **Introducción**

A veces, necesitas copiar filas y columnas en una hoja de cálculo sin copiar toda la hoja. Con Aspose.Cells, es posible copiar filas y columnas dentro o entre libros de trabajo.
Cuando se copia una fila (o columna), se copia también los datos contenidos en ella, incluidas fórmulas - con referencias actualizadas - y valores, comentarios, formato de celdas, celdas ocultas, imágenes y otros objetos de dibujo.

## **Cómo copiar filas y columnas con Microsoft Excel**

1. Selecciona la fila o columna que deseas copiar.
1. Para copiar filas o columnas, haz clic en **Copiar** en la barra de herramientas **Estándar**, o presiona **CTRL**+**C**.
1. Selecciona una fila o columna debajo o a la derecha de donde deseas copiar tu selección.
1. Al copiar filas o columnas, haz clic en **Celdas Copiadas** en el menú **Insertar**.

{{% alert color="primary" %}}

Si haces clic en **Pegar** en la barra de herramientas **Estándar** o presionas **CTRL**+**V** en lugar de hacer clic en un comando en el menú **Insertar**, cualquier contenido de las celdas de destino se reemplaza.

{{% /alert %}}

## **Cómo pegar filas y columnas usando opciones de pegado con Microsoft Excel**

1. Selecciona las celdas que contienen los datos u otros atributos que desees copiar.
1. En la pestaña Inicio, haz clic en **Copiar**.
1. Haz clic en la primera celda en el área donde quieras **pegar** lo que copiaste.
1. En la pestaña Inicio, haz clic en la flecha junto a **Pegar**, y luego selecciona **Pegado especial**.
1. Selecciona las **opciones** que desees.

## **Cómo copiar filas y columnas utilizando Aspose.Cells for .NET**

## **Cómo copiar filas individuales**

Aspose.Cells proporciona el método [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) de la clase [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Este método copia todos los tipos de datos, incluidas fórmulas, valores, comentarios, formatos de celda, celdas ocultas, imágenes y otros objetos dibujados, desde la fila de origen a la fila de destino.

El método [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) toma los siguientes parámetros:

- el objeto fuente [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells),
- el índice de fila de origen, y
- el índice de fila de destino.

Utilice este método para copiar una fila dentro de una hoja, o a otra hoja. El método [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) funciona de manera similar a Microsoft Excel. Por ejemplo, no es necesario establecer explícitamente la altura de la fila de destino, ese valor también se copia.

El siguiente ejemplo muestra cómo copiar una fila en una hoja de cálculo. Utiliza un archivo de plantilla de Microsoft Excel y copia la segunda fila (completa con datos, formato, comentarios, imágenes, etc.) y la pega en la 12ª fila en la misma hoja de cálculo.

Puedes omitir el paso que obtiene la altura de la fila fuente usando el método [**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight) y luego establece la altura de la fila de destino usando el método [**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) ya que el método [**CopyRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow) se encarga automáticamente de la altura de la fila.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

Al copiar filas, es importante tener en cuenta las imágenes relacionadas, gráficos u otros objetos de dibujo, ya que es lo mismo que en Microsoft Excel:

1. Si el índice de fila de origen es 5, la imagen, el gráfico, etc., se copian si están contenidos en las tres filas (el índice de fila de inicio es 4 y el índice de fila final es 6).
1. Las imágenes, gráficos, etc. existentes en la fila de destino no se eliminarán.

{{% /alert %}}

## **Cómo Copiar Múltiples Filas**

También puedes copiar múltiples filas en una nueva ubicación mientras usas el método [**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) que toma un parámetro adicional de tipo entero para especificar el número de filas fuente que se copiarán.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


## **Cómo Copiar Columnas**

Aspose.Cells proporciona el método [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) de la clase [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), este método copia todo tipo de datos, incluidas fórmulas, con referencias actualizadas, valores, comentarios, formatos de celdas, celdas ocultas, imágenes y otros objetos dibujados de la columna fuente a la columna de destino.

El método [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) toma los siguientes parámetros:

- el objeto fuente [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells),
- índice de columna de origen, y
- el índice de columna de destino.

Utiliza el método [**CopyColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn) para copiar una columna dentro de una hoja o hacia otra hoja.

Este ejemplo copia una columna de una hoja de cálculo y la pega en una hoja de cálculo en otro libro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

## **Cómo Copiar Múltiples Columnas**

Similar al método [**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index), las APIs de Aspose.Cells también proporcionan el método [**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index) para copiar varias columnas de origen a una nueva ubicación.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


## **Cómo Pegar Filas y Columnas con Opciones de Pegado**

Aspose.Cells ahora proporciona [**PasteOptions**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions) al usar las funciones [**CopyRows**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2) y [**CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1). Permite configurar una opción de pegado adecuada similar a Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
