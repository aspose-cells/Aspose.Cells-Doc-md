---
title: Obtenga todos los índices de filas ocultas después de actualizar el Autofiltro
type: docs
weight: 320
url: /es/net/get-all-hidden-rows-indices-after-refreshing-autofilter/
---
## **Posibles escenarios de uso**

Cuando aplica el filtro automático en las celdas de la hoja de trabajo, algunas de las filas se ocultan automáticamente. Pero podría darse el caso de que el usuario final de Excel ya haya ocultado manualmente algunas de las filas y no estén ocultas por un filtro automático. Por lo tanto, hace difícil saber cuáles de las filas están ocultas por el filtro automático y cuáles están ocultas manualmente por el usuario final de Excel. Aspose.Cells se ocupa de este problema utilizando el int[][**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)método. Este método devuelve los índices de fila de todas las filas que están ocultas por el filtro automático y no manualmente por el usuario final de Excel.

## **Obtenga todos los índices de filas ocultas después de actualizar el Autofiltro**

 Consulte el siguiente código de ejemplo que carga el[ejemplo de archivo de Excel](64716909.xlsx) que contiene algunas de las filas ocultas manualmente por el usuario final de Excel. El código aplica el filtro automático y lo actualiza usando el int[][**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)método que devuelve los índices de fila de todas las filas ocultas por el filtro automático. Luego imprime los índices de las filas ocultas en la consola junto con los nombres y valores de las celdas.

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.cs" >}}

## **Salida de consola**

{{< highlight "java" >}}

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
