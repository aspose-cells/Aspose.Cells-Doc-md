---
title: Especificación de advertencia de ordenación al ordenar datos
type: docs
weight: 100
url: /es/java/specifying-sort-warning-while-sorting-data/
---
## **Posibles escenarios de uso**
 Tenga en cuenta estos datos textuales, es decir, {11, 111, 22}. Estos datos textuales se ordenan así porque en términos de texto, 111 viene antes que 22. Pero, si desea ordenar estos datos no como texto sino como números, entonces se convertirá en {11, 22, 111} porque numéricamente 111 viene después 22. Aspose.Cells ofrece[DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber) propiedad para hacer frente a este problema. Establezca esta propiedad**verdadero**y sus datos textuales se clasificarán como datos numéricos. La siguiente captura de pantalla muestra la advertencia de clasificación mostrada por Microsoft Excel cuando se clasifican datos textuales que parecen datos numéricos.

![todo:imagen_alternativa_texto](specifying-sort-warning-while-sorting-data_1.png)
## **Código de muestra**
 El siguiente código de ejemplo ilustra el uso de[DataSorter.SortAsNumber](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#SortAsNumber)propiedad como se explicó anteriormente. Por favor revise su[ejemplo de archivo de Excel](43352077.xlsx) y[archivo de salida de Excel](43352078.xlsx) para obtener más ayuda.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SpecifyingSortWarningWhileSortingData.java" >}}
