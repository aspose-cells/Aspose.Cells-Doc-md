---
title: Ordenar datos en columna con lista de clasificación personalizada
type: docs
weight: 290
url: /es/net/sort-data-in-column-with-custom-sort-list/
description: Aprenda a ordenar datos en la columna usando una lista personalizada usando Aspose.Cells for .NET API.
keywords: Sort Data in Column with Custom Sort List, Sort data by custom list.
---
##  **Posibles escenarios de uso**

 Puede ordenar los datos de la columna utilizando una lista personalizada. Esto se puede hacer usando[**DataSorter.AddKey (clave int, orden SortOrder, lista personalizada de cadenas)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2)método. Sin embargo, este método sólo funciona si los elementos de la lista personalizada no tienen comas dentro. Si tienen comas como "USA,US", "China,CN", etc., entonces debes usar [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference. aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) método. Aquí, el último parámetro no es una cadena sino una matriz de cadenas.

##  **Ordenar datos en columna con lista de clasificación personalizada**

El siguiente código de muestra explica cómo utilizar [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey /methods/3) método para ordenar datos con una lista de clasificación personalizada. Por favor vea el[archivo de Excel de muestra](50528327.xlsx) utilizado en este código y[archivo de salida de Excel](50528328.xlsx) generado por ello. La siguiente captura de pantalla muestra el efecto del código en el archivo de Excel de muestra durante la ejecución.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

##  **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
