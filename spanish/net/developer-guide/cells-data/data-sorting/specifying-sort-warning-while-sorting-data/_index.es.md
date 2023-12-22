---
title: Especificación de advertencia de clasificación al ordenar datos
type: docs
weight: 140
url: /es/net/specifying-sort-warning-while-sorting-data/
description: Aprenda a especificar una advertencia de clasificación al ordenar datos utilizando Aspose.Cells for .NET API.
keywords: Add sort warning when sorting data, set sort warning while sorting data, select sort warning when sorting data.
---
##  **Posibles escenarios de uso**

Considere estos datos textuales, es decir, {11, 111, 22}. Estos datos textuales están ordenados porque, en términos de texto, 111 viene antes de 22. Pero, si desea ordenar estos datos no como texto sino como números, entonces se convertirá en {11, 22, 111} porque numéricamente 111 viene después de 22. Aspose.Cells proporciona[**Clasificador de datos.Ordenar como número**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber)propiedad para abordar este problema. Por favor establezca esta propiedad**verdadero**sus datos textuales se ordenarán como datos numéricos. La siguiente captura de pantalla muestra la advertencia de clasificación que muestra Microsoft Excel cuando se ordenan datos textuales que parecen datos numéricos.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

##  **Código de muestra**

 El siguiente código de muestra ilustra el uso de[**Clasificador de datos.Ordenar como número**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortasnumber) propiedad como se explicó anteriormente. Por favor revisa su[archivo de Excel de muestra](43352075.xlsx) y[archivo de salida de Excel](43352076.xlsx) para más ayuda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SpecifyingSortWarningWhileSortingData.cs" >}}
