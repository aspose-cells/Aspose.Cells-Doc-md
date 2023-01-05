---
title: Buscar y reemplazar datos en un rango
type: docs
weight: 60
url: /es/java/search-and-replace-data-in-a-range/
description: Este artículo muestra cómo buscar y reemplazar datos en un rango en Excel usando el código Java.
keywords: java search and replace data in excel, java search data in excel, java search and replace data in a range, java search data in a range, java searching data in a range, java searching data in range, java searching data in excel, java search data in range, search and replace data in excel with java, search and replace data in a range with java, search and replace data in range with java
---
{{% alert color="primary" %}}

A veces, necesita buscar y reemplazar datos específicos en un rango, ignorando cualquier valor de celda fuera del rango deseado. Aspose.Cells le permite limitar una búsqueda a un rango específico. Este artículo explica cómo.

{{% /alert %}}

Aspose.Cells proporciona el[**BuscarOpciones.setRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#setRange(com.aspose.cells.CellArea)) método para especificar un rango al buscar datos.

 Supongamos que desea buscar la cadena**"búsqueda"** y reemplazarlo con**"reemplazar"** en el rango**E3: H6**. En la captura de pantalla a continuación, la cadena "buscar" se puede ver en varias celdas, pero queremos reemplazarla solo en un rango determinado, aquí resaltado en amarillo.

**Fichero de entrada**

![todo:imagen_alternativa_texto](search-and-replace-data-in-a-range_1.png)

Después de la ejecución del código, el archivo de salida se ve como el siguiente. Todas las cadenas de "búsqueda" dentro del rango han sido reemplazadas por "reemplazar".

**Archivo de salida**

![todo:imagen_alternativa_texto](search-and-replace-data-in-a-range_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchReplaceDataInRange-SearchReplaceDataInRange.java" >}}

## Artículos relacionados

- [Buscar o buscar datos](/cells/es/java/find-or-search-data/)
