---
title: Ordenar datos en columna con lista de ordenación personalizada
type: docs
weight: 290
url: /es/net/sort-data-in-column-with-custom-sort-list/
---
## **Posibles escenarios de uso**

 Puede ordenar los datos en la columna usando una lista personalizada. Esto se puede hacer usando[**DataSorter.AddKey (clave int, Orden de clasificación, Cadena customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2)método. Sin embargo, este método solo funciona si los elementos de la lista personalizada no tienen comas dentro de ellos. Si tienen comas como "EE. UU., EE. UU.", "China, CN", etc., debe usar [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference. aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3). Aquí, el último parámetro no es String sino una matriz de cadenas.

## **Ordenar datos en columna con lista de ordenación personalizada**

El siguiente código de muestra explica cómo usar [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey /methods/3) método para ordenar datos con una lista de clasificación personalizada. Consulte el [archivo de Excel de muestra] (50528327.xlsx) utilizado en este código y el [archivo de Excel de salida] (50528328.xlsx) generado por él. La siguiente captura de pantalla muestra el efecto del código en el archivo de muestra de Excel durante la ejecución.

![todo:imagen_alternativa_texto](sort-data-in-column-with-custom-sort-list_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
