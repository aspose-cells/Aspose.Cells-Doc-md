---
title: Ordenar datos en una columna con lista de orden personalizado
type: docs
weight: 290
url: /es/python-net/sort-data-in-column-with-custom-sort-list/
description: Aprende cómo ordenar datos en la columna utilizando una lista personalizada mediante el uso de la API Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel de Python, Ordenar datos en columna con lista de ordenación personalizada de Python, Ordenar datos de Python por lista personalizada.
---

## **Escenarios de uso posibles**

Puedes ordenar datos en la columna usando una lista personalizada. Esto se puede hacer utilizando el método [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list). Sin embargo, este método solo funciona si los elementos en la lista personalizada no tienen comas en su interior. Si tienen comas como "USA,US", "China,CN" etc., entonces debes usar el método [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list). Aquí, el último parámetro no es un String sino un Array de Strings.

## **Ordenar datos en una columna con lista de orden personalizado**

El siguiente código de ejemplo explica cómo usar el método [**DataSorter.add_key(key, order, custom_list)**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOrder-list) para ordenar datos con lista de ordenación personalizada. Consulta el [archivo de Excel de muestra](50528327.xlsx) utilizado en este código y el [archivo de Excel de salida](50528328.xlsx) generado por él. La siguiente captura de pantalla muestra el efecto del código en el archivo de Excel de muestra al ejecutarse.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithCustomSortList.py" >}}
{{< app/cells/assistant language="python-net" >}}
