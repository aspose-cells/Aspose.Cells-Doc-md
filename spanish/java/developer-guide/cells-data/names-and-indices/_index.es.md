---
title: Conversión entre nombre de celda e índice de fila/columna
linktitle: Cell Conversión de nombre e índice
type: docs
weight: 5
url: /es/java/names-and-indices/
description: Aprenda cómo obtener el resultado de la conversión entre el nombre de la celda y el índice de fila/columna con las API Aspose.Cells for Java.
keywords: Java Convert cell index to name, Convert cell name to row/column index using java apis, How to Get Cell Name from Row and Column Indices with java, Java How to Get Row and Column Indices from Cell Name.
---
##  **Cómo obtener el nombre Cell de los índices de filas y columnas**
Es posible encontrar el nombre de una celda según el índice de fila y columna. Este artículo explica cómo.

 Aspose.Cells proporciona la[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) método que permite a los desarrolladores obtener el nombre de una celda si proporcionan el índice de fila y columna.

{{% alert color="primary" %}} 

A diferencia de Microsoft Excel, donde los índices de filas y columnas comienzan desde 1, Aspose.Cells comienza a contar los índices de filas y columnas desde 0.

{{% /alert %}} 

 El siguiente código de muestra ilustra cómo utilizar[CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) para acceder al nombre de la celda proporcionado en un índice de fila y columna conocido. El código genera el siguiente resultado.



Cell Nombre en [0, 0]: A1

Cell Nombre en [4, 0]: A5

Cell Nombre en [0, 4]: E1

Cell Nombre en [2, 2]: C3

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
##  **Cómo obtener índices de filas y columnas a partir del nombre Cell**
Es posible encontrar un índice de fila y columna de la celda a partir de su nombre. Este artículo explica cómo.

 Aspose.Cells proporciona la[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) método que permite a los desarrolladores obtener un índice de filas y columnas a partir del nombre de la celda.

{{% alert color="primary" %}} 

A diferencia de Microsoft Excel, donde los índices de filas y columnas comienzan desde 1, Aspose.Cells comienza a contar los índices de filas y columnas desde 0.

{{% /alert %}} 

 El siguiente código de muestra ilustra cómo utilizar[CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) para obtener el índice de fila y columna del nombre de la celda. El código genera el siguiente resultado.



Índice de filas de Cell C6: 5

Índice de columnas de Cell C6: 2

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
##  **Cómo crear nombres de hojas seguras**
 A veces es necesario asignar el nombre de la hoja en tiempo de ejecución. En este escenario, puede haber nombres de hojas que pueden contener algunos caracteres adicionales como<>+(?”. Es necesario reemplazar cualquier carácter de este tipo, que no está permitido como nombre de hoja, con algún carácter preestablecido proporcionado por el usuario. De manera similar, la longitud puede aumentar a más de 31 caracteres que deben truncarse. Apache POI proporciona ciertas funciones para crear nombres seguros, por lo que Aspose.Cells proporciona una función similar para manejar todos estos problemas. El siguiente código de ejemplo demuestra esta función:



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**Salida de consola**

este es el nombre que es cre

` `<> + (adj.Privado _ "Privado"
