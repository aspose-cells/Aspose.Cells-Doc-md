---
title: Especificar advertencia de ordenación al ordenar los datos
type: docs
weight: 140
url: /es/python-net/specifying-sort-warning-while-sorting-data/
description: Aprende cómo especificar una advertencia de ordenación al ordenar datos mediante el uso de la API Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel de Python, Agregar advertencia de ordenación al ordenar datos de Python, Establecer advertencia de ordenación al ordenar datos de Python, Seleccionar advertencia de ordenación al ordenar datos de Python.
---

## **Escenarios de uso posibles**

Por favor, considera estos datos textuales, es decir, {11, 111, 22}. Estos datos textuales están ordenados porque, en términos de texto, 111 viene antes que 22. Pero, si deseas ordenar estos datos no como texto sino como números, entonces se convertirán en {11, 22, 111} porque numéricamente 111 viene después de 22. Aspose.Cells para Python via .NET proporciona la propiedad {0} para abordar este problema. Por favor, establece esta propiedad como **true** y tus datos textuales se ordenarán como datos numéricos. La siguiente captura de pantalla muestra la advertencia de ordenación mostrada por Microsoft Excel cuando se ordenan datos textuales que parecen datos numéricos.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Código de muestra**

El siguiente código de ejemplo ilustra el uso de la propiedad [**DataSorter.sort_as_number**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_as_number/) como se explica anteriormente. Consulte su [archivo de Excel de ejemplo](43352075.xlsx) y [archivo de Excel de salida](43352076.xlsx) para obtener más ayuda.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SpecifyingSortWarningWhileSortingData.py" >}}
