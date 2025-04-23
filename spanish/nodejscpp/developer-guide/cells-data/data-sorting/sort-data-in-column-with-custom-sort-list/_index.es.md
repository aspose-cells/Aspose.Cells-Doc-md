---
title: Ordenar datos en una columna con lista de orden personalizado
type: docs
weight: 290
url: /es/nodejs-cpp/sort-data-in-column-with-custom-sort-list/
description: Aprende cómo ordenar datos en la columna usando una lista personalizada con la API Aspose.Cells for Node.js via C++.
keywords: Ordenar datos en una columna con lista de ordenación personalizada, Ordenar datos por lista personalizada.
---

## **Escenarios de uso posibles**

Puedes ordenar datos en la columna usando una lista personalizada. Esto se puede hacer usando el método [**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-string-). Sin embargo, este método solo funciona si los elementos en la lista personalizada no contienen comas. Si contienen comas como "USA,US", "China,CN", entonces debes usar el método [**DataSorter.addKey(number, SortOrder, string[])**)](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-stringarray-). Aquí, el último parámetro no es String sino un Array de Strings.

## **Ordenar datos en una columna con lista de orden personalizado**

El siguiente código de ejemplo explica cómo usar el método [**DataSorter.addKey(number, SortOrder, string[])**)](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addKey-number-sortorder-stringarray-) para ordenar datos con una lista de ordenamiento personalizada. Por favor, vea el [archivo de Excel de ejemplo](50528327.xlsx) utilizado en este código y el [archivo de Excel de salida](50528328.xlsx) generado por él. La siguiente captura de pantalla muestra el efecto del código en el archivo de Excel de muestra al ejecutarlo.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SortDataInColumnWithCustomSortList.js" >}}

