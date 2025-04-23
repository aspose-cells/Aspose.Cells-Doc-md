---
title: Especificar advertencia de ordenación al ordenar los datos
type: docs
weight: 100
url: /es/java/specifying-sort-warning-while-sorting-data/
---

## **Escenarios de uso posibles**
Considere los siguientes datos textuales, es decir {11, 111, 22}. Estos datos textuales se ordenan de esta manera porque en términos de texto, 111 viene antes de 22. Pero, si desea ordenar estos datos no como texto, sino como números, entonces se convertirá en {11, 22, 111} porque numéricamente 111 viene después de 22. Aspose.Cells proporciona la propiedad [DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber) para manejar este problema. Configure esta propiedad como **true** y sus datos textuales se ordenarán como datos numéricos. La siguiente captura de pantalla muestra la advertencia de ordenación mostrada por Microsoft Excel cuando se ordenan datos textuales que parecen datos numéricos.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)
## **Código de muestra**
El siguiente código de ejemplo ilustra el uso de la propiedad [DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber) como se explicó anteriormente. Consulte su [archivo de Excel de ejemplo](43352077.xlsx) y [archivo de Excel de salida](43352078.xlsx) para obtener más ayuda.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SpecifyingSortWarningWhileSortingData.java" >}}
{{< app/cells/assistant language="java" >}}
