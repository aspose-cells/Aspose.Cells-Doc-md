---
title: Obtener Todos los Índices de Filas Ocultas Después de Actualizar el Autofiltro
type: docs
weight: 320
url: /es/net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Aprenda cómo obtener todos los índices de filas ocultas después de actualizar el filtro automático usando la API Aspose.Cells for .NET.
keywords: Obtener todos los índices de filas ocultas después de actualizar el filtro automático, obtener todos los índices de filas ocultas después de actualizar el filtro automático, recuperar todos los índices de filas ocultas después de actualizar el filtro automático
---

## **Escenarios de uso posibles**

Cuando aplica el filtro automático en las celdas de la hoja de cálculo, algunas de las filas se ocultan automáticamente. Pero podría ser el caso de que algunas de las filas ya estén ocultas manualmente por el usuario final de Excel y no estén ocultas por un filtro automático. Por lo tanto, es difícil saber cuáles de las filas están ocultas por el filtro automático y cuáles de ellas están ocultas manualmente por el usuario final de Excel. Aspose.Cells resuelve este problema utilizando el método int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1). Este método devuelve los índices de las filas que están ocultas por el filtro automático y no manualmente por el usuario final de Excel.

## **Obtener Todos los Índices de Filas Ocultas Después de Actualizar el Autofiltro**

Consulte el siguiente código de muestra que carga el [archivo de Excel de ejemplo](64716909.xlsx) que contiene algunas de las filas ocultas manualmente por el usuario final de Excel. El código aplica el filtro automático y lo actualiza utilizando el método int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1) que devuelve los índices de todas las filas ocultas por el filtro automático. Luego imprime los índices de las filas ocultas en la consola junto con los nombres y valores de las celdas.

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.cs" >}}

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
{{< app/cells/assistant language="csharp" >}}
