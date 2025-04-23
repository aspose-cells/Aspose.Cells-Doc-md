---
title: Especificar advertencia de ordenación al ordenar los datos
type: docs
weight: 140
url: /es/nodejs-cpp/specifying-sort-warning-while-sorting-data/
description: Aprende cómo especificar advertencias de ordenamiento al ordenar datos usando la API Aspose.Cells for Node.js via C++.
keywords: Agregar advertencia de ordenación al ordenar datos, establecer advertencia de ordenación al ordenar datos, seleccionar advertencia de ordenación al ordenar datos.
---

## **Escenarios de uso posibles**

Por favor, considera estos datos textuales: {11, 111, 22}. Estos datos se ordenan porque, en términos de texto, 111 aparece antes que 22. Pero, si quieres ordenar estos datos no como texto sino como números, serán {11, 22, 111} ya que numéricamente 111 aparece después de 22. La API Aspose.Cells for Node.js via C++ proporciona la propiedad {0} para manejar esta situación. Establece esta propiedad en **true** y tus datos textuales se ordenarán como datos numéricos. La siguiente captura de pantalla muestra la advertencia de ordenamiento que aparece en Microsoft Excel cuando los datos textuales que parecen datos numéricos se ordenan.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Código de muestra**

El siguiente código de ejemplo ilustra el uso de la propiedad [**DataSorter.setSortAsNumber**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#setSortAsNumber-boolean-) como se explica anteriormente. Consulte su [archivo de Excel de ejemplo](43352075.xlsx) y [archivo de Excel de salida](43352076.xlsx) para obtener más ayuda.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SpecifyingSortWarningWhileSortingData.js" >}}

