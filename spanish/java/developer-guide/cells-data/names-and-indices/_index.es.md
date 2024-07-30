---
title: Conversión entre el nombre de la celda y el índice de fila/columna
linktitle: Conversión entre Nombre de Celda e Índice
type: docs
weight: 5
url: /es/java/names-and-indices/
description: Aprenda cómo obtener el resultado de conversión entre el nombre de la celda y el índice de fila/columna con Aspose.Cells for Java APIs.
keywords: Convertir índice de celda a nombre, Convertir nombre de celda a índice de fila/columna usando java apis, Cómo obtener el nombre de la celda a partir de los índices de fila y columna en Java, Java Cómo obtener los índices de fila y columna a partir del nombre de la celda.
---

## **Cómo obtener el nombre de la celda a partir de los índices de fila y columna**
Es posible encontrar el nombre de una celda dado el índice de fila y columna. Este artículo explica cómo.

Aspose.Cells proporciona el método [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) que permite a los desarrolladores obtener el nombre de una celda si proporcionan el índice de fila y columna.

{{% alert color="primary" %}} 

Microsoft Excel comienza a contar los índices de filas y columnas desde 1. A diferencia de Microsoft Excel, Aspose.Cells comienza a contar los índices de filas y columnas desde 0.

{{% /alert %}} 

El siguiente código de ejemplo ilustra cómo usar [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName\(int,%20int\)) para acceder al nombre de la celda dada en un índice de fila y columna conocido. El código genera la siguiente salida.

{{< highlight java >}}

Cell Name at [0, 0]: A1

Cell Name at [4, 0]: A5

Cell Name at [0, 4]: E1

Cell Name at [2, 2]: C3

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
## **Cómo obtener los índices de fila y columna a partir del nombre de una celda**
Es posible encontrar un índice de fila y columna de la celda a partir de su nombre. Este artículo explica cómo.

Aspose.Cells proporciona el método [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) que permite a los desarrolladores obtener el índice de fila y columna a partir del nombre de la celda.

{{% alert color="primary" %}} 

Microsoft Excel comienza a contar los índices de filas y columnas desde 1. A diferencia de Microsoft Excel, Aspose.Cells comienza a contar los índices de filas y columnas desde 0.

{{% /alert %}} 

El siguiente código de ejemplo ilustra cómo usar [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex\(java.lang.String\)) para obtener el índice de fila y columna a partir del nombre de la celda. El código genera la siguiente salida.

{{< highlight java >}}

Row Index of Cell C6: 5

Column Index of Cell C6: 2

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
## **Cómo crear nombres seguros para hojas de cálculo**
A veces es necesario asignar el nombre de la hoja en tiempo de ejecución. En este escenario, puede haber nombres de hojas que pueden contener algunos caracteres adicionales como <>+(?”. Hay una necesidad de reemplazar cualquier caracter que no esté permitido como nombre de hoja con algún caracter preestablecido proporcionado por el usuario. Del mismo modo, la longitud puede aumentar a más de 31 caracteres y necesita ser truncada. Apache POI proporciona ciertas características para crear nombres seguros, por lo tanto, Aspose.Cells proporciona una característica similar para manejar todos estos problemas. El siguiente código de ejemplo demuestra esta característica.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

Salida de la consola

este es el primer nombre que se creó

{{< highlight java >}}

` `<> + (adj.Private _ " Private"

{{< /highlight >}}
