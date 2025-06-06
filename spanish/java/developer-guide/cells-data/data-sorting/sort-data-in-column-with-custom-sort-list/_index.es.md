---
title: Ordenar datos en una columna con lista de orden personalizado
type: docs
weight: 210
url: /es/java/sort-data-in-column-with-custom-sort-list/
---

## **Escenarios de uso posibles**

Puedes ordenar datos en la columna usando una lista personalizada. Esto se puede hacer usando el método [DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey-int-int-java.lang.String-). Sin embargo, este método solo funciona si los elementos en la lista personalizada no contienen comas dentro de ellos. Si contienen comas como "USA, US", "China, CN", etc., entonces debes usar el método [DataSorter.AddKey(int key, SortOrder order, String customList)](https://reference.aspose.com/cells/java/com.aspose.cells/datasorter#addKey-int-int-java.lang.String-). Aquí, el último parámetro no es String sino un Arreglo de Strings.

## **Ordenar datos en una columna con lista de orden personalizado**

El siguiente código de ejemplo explica cómo utilizar el método DataSorter.AddKey(int key, SortOrder order, String[] customList) para ordenar datos con una lista de orden personalizado. Consulte el [archivo de Excel de ejemplo](50528359.xlsx) utilizado en este código y el [archivo de Excel de salida](50528358.xlsx) generado por él. La siguiente captura de pantalla muestra el efecto del código en el archivo de Excel de ejemplo al ejecutarlo.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SortDataInColumnWithCustomSortList.java" >}}
{{< app/cells/assistant language="java" >}}
