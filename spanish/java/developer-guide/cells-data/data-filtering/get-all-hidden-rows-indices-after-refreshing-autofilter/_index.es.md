---
title: Obtener Todos los Índices de Filas Ocultas Después de Actualizar el Autofiltro
type: docs
weight: 240
url: /es/java/get-all-hidden-rows-indices-after-refreshing-autofilter/
---

## **Escenarios de uso posibles**

Cuando aplicas un filtro automático en las celdas de la hoja de cálculo, algunas filas se ocultan automáticamente. Pero podría darse el caso de que algunas de las filas ya estén ocultas manualmente por el usuario final de Excel y no estén ocultas por el filtro automático. Por lo tanto, resulta difícil saber cuáles de las filas están ocultas por el filtro automático y cuáles de ellas están ocultas manualmente por el usuario final de Excel. Aspose.Cells resuelve este problema utilizando el método int[] [**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean)). Este método devuelve los índices de fila de todas las filas que están ocultas por el filtro automático y no manualmente por el usuario final de Excel.

## **Obtener Todos los Índices de Filas Ocultas Después de Actualizar el Autofiltro**

Consulte el siguiente fragmento de código de ejemplo que carga el [archivo de Excel de ejemplo](64716913.xlsx) que contiene algunas filas ocultas manualmente por el usuario final de Excel. El código aplica el filtro automático y lo actualiza utilizando el método int[] [**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean)) que devuelve los índices de las filas ocultas por el filtro automático. Luego imprime los índices de las filas ocultas en la consola junto con los nombres y valores de las celdas.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.java" >}}

## **Salida de la consola**

{{< highlight java >}}

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.

\--------------------------

1       A2      Apple

2       A3      Apple

3       A4      Apple

6       A7      Apple

7       A8      Apple

11      A12     Pear

12      A13     Pear

{{< /highlight >}}
