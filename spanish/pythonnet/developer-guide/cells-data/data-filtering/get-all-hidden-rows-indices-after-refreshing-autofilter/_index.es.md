---
title: Obtener Todos los Índices de Filas Ocultas Después de Actualizar el Autofiltro
type: docs
weight: 320
url: /es/python-net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Aprende cómo obtener todos los índices de filas ocultas después de actualizar el autodetector de filtros utilizando la API Aspose.Cells para Python via .NET.
keywords: Biblioteca de Python Excel, Obtener Todos los Índices de Filas Ocultas después de Actualizar el Autofiltro con Python, Obtener Todos los Índices de Filas Ocultas después de Actualizar el Autofiltro con Python, Recuperar Todos los Índices de Filas Ocultas después de Actualizar el Autofiltro con Python
---

## **Escenarios de uso posibles**

Cuando aplicas el filtro automático en las celdas de la hoja de cálculo, algunas de las filas se ocultan automáticamente. Pero podría ser el caso que algunas de las filas ya estén ocultas manualmente por el usuario final de Excel y no estén ocultas por un filtro automático. Por lo tanto, puede ser difícil saber cuáles de las filas están ocultas por el filtro automático y cuáles de ellas están ocultas manualmente por el usuario final de Excel. Aspose.Cells para Python via .NET aborda este problema utilizando el método [**AutoFilter.refresh(hide_rows)**](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/refresh/#bool). Este método devuelve los índices de fila de todas las filas que están ocultas por el filtro automático y no manualmente por el usuario final de Excel.

## **Obtener Todos los Índices de Filas Ocultas Después de Actualizar el Autofiltro**

Por favor, consulta el siguiente código de ejemplo que carga el [archivo de Excel de muestra](64716909.xlsx) que contiene algunas filas ocultas manualmente por el usuario final de Excel. El código aplica el filtro automático y lo actualiza utilizando el método [**AutoFilter.refresh(hide_rows)**](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/refresh/#bool) que devuelve los índices de todas las filas ocultas por el filtro automático. Luego imprime los índices de las filas ocultas en la consola junto con los nombres y valores de las celdas.

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.py" >}}

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
