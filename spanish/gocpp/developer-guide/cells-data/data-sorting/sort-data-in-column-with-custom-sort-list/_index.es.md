---
title: Ordenar datos en una columna con lista de ordenación personalizada con Golang a través de C++
linktitle: Ordenar datos en una columna con lista de orden personalizado
type: docs
weight: 290
url: /es/go-cpp/sort-data-in-column-with-custom-sort-list/
description: Aprende cómo ordenar datos en la columna usando una lista personalizada mediante la API Aspose.Cells for C++.
keywords: Ordenar datos en una columna con lista de ordenación personalizada, Ordenar datos por lista personalizada.
---

## **Escenarios de uso posibles**

Puedes ordenar datos en la columna usando una lista personalizada. Esto se puede hacer usando el método [**DataSorter::AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/). Sin embargo, este método solo funciona si los ítems en la lista personalizada no contienen comas. Si contienen comas como "EE.UU.,US", "China,CN" etc., entonces debes usar el método [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/). Aquí, el último parámetro no es una cadena, sino un arreglo de cadenas.

## **Ordenar datos en una columna con lista de orden personalizado**

El siguiente código de ejemplo explica cómo usar el método [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/go-cpp/datasorter/addkey_int_sortorder/) para ordenar datos con una lista de ordenamiento personalizada. Por favor, vea el [archivo de Excel de muestra](50528327.xlsx) utilizado en este código y el [archivo Excel de salida](50528328.xlsx) generado por él. La siguiente captura de pantalla muestra el efecto del código en el archivo de Excel de muestra al ejecutarse.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SortDataInColumnWithCustomSortList.go" >}}
