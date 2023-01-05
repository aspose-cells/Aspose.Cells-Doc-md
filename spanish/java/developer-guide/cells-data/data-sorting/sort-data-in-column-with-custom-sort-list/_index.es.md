---
title: Ordenar datos en columna con lista de ordenación personalizada
type: docs
weight: 210
url: /es/java/sort-data-in-column-with-custom-sort-list/
---
## **Posibles escenarios de uso**

Puede ordenar los datos en la columna usando una lista personalizada. Esto se puede hacer usando[DataSorter.AddKey (clave int, Orden de clasificación, Cadena customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)) método. Sin embargo, este método solo funciona si los elementos de la lista personalizada no tienen comas dentro de ellos. Si tienen comas como "EE. UU., EE. UU.", "China, CN", etc., debe usar[DataSorter.AddKey (clave int, Orden de clasificación, Cadena customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey(int,%20int,%20java.lang.String)) método. Aquí, el último parámetro no es String sino una matriz de cadenas.

## **Ordenar datos en columna con lista de ordenación personalizada**

El siguiente código de ejemplo explica cómo usar el método DataSorter.AddKey(int key, SortOrder order, String[]customList) para ordenar datos con una lista de ordenación personalizada. Por favor vea el[ejemplo de archivo de Excel](50528359.xlsx)utilizado en este código y[archivo de salida de Excel](50528358.xlsx)generada por ella. La siguiente captura de pantalla muestra el efecto del código en el archivo de muestra de Excel durante la ejecución.

![todo:imagen_alternativa_texto](sort-data-in-column-with-custom-sort-list_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}
