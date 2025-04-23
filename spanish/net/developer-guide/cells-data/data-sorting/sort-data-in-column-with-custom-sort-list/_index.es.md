---
title: Ordenar datos en una columna con lista de orden personalizado
type: docs
weight: 290
url: /es/net/sort-data-in-column-with-custom-sort-list/
description: Aprenda a ordenar datos en la columna usando una lista de ordenación personalizada mediante la API Aspose.Cells for .NET.
keywords: Ordenar datos en una columna con lista de ordenación personalizada, Ordenar datos por lista personalizada.
---

## **Escenarios de uso posibles**

Puede ordenar datos en la columna usando una lista personalizada. Esto se puede hacer utilizando el método [**DataSorter.AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/2). Sin embargo, este método funciona solo si los elementos en la lista personalizada no tienen comas en su interior. Si tienen comas como "EEUU,US", "China,CN", etc., entonces debe utilizar el método [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3). Aquí, el último parámetro no es String sino un Array de Strings.

## **Ordenar datos en una columna con lista de orden personalizado**

El siguiente código de muestra explica cómo utilizar el método [**DataSorter.AddKey Method (Int32, SortOrder,String[])**)](https://reference.aspose.com/cells/net/aspose.cells.datasorter/addkey/methods/3) para ordenar datos con lista de ordenación personalizada. Consulte el [archivo de Excel de ejemplo](50528327.xlsx) utilizado en este código y el [archivo de Excel generado](50528328.xlsx) por él. La siguiente captura de pantalla muestra el efecto del código en el archivo de Excel de ejemplo al ejecutarlo.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithCustomSortList.cs" >}}
{{< app/cells/assistant language="csharp" >}}
