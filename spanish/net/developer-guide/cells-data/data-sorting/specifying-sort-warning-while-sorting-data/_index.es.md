---
title: Especificación de advertencia de ordenación al ordenar datos
type: docs
weight: 140
url: /es/net/specifying-sort-warning-while-sorting-data/
---
## **Posibles escenarios de uso**

Tenga en cuenta estos datos textuales, es decir, {11, 111, 22}. Estos datos textuales están ordenados porque, en términos de texto, 111 viene antes de 22. Pero, si desea ordenar estos datos no como texto sino como números, entonces se convertirá en {11, 22, 111} porque numéricamente 111 viene después de 22 Aspose.Cells proporciona[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)propiedad para hacer frente a este problema. Establezca esta propiedad**verdadero**y sus datos textuales se clasificarán como datos numéricos. La siguiente captura de pantalla muestra la advertencia de clasificación mostrada por Microsoft Excel cuando se clasifican datos textuales que parecen datos numéricos.

![todo:imagen_alternativa_texto](specifying-sort-warning-while-sorting-data_1.png)

## **Código de muestra**

 El siguiente código de ejemplo ilustra el uso de[**DataSorter.SortAsNumber**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)propiedad como se explicó anteriormente. Por favor revise su[ejemplo de archivo de Excel](43352075.xlsx) y[archivo de salida de Excel](43352076.xlsx) para obtener más ayuda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SpecifyingSortWarningWhileSortingData.cs" >}}
