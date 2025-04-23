---
title: Buscar y Reemplazar Datos en un Rango
type: docs
weight: 60
url: /es/java/search-and-replace-data-in-a-range/
description: Este artículo muestra cómo buscar y reemplazar datos en un rango en Excel usando código Java.
keywords: java buscar y reemplazar datos en excel, java buscar datos en excel, java buscar y reemplazar datos en un rango, java buscar datos en un rango, java búsqueda de datos en un rango, java búsqueda de datos en rango, java búsqueda de datos en excel, java buscar datos en un rango, buscar y reemplazar datos en excel con java, buscar y reemplazar datos en un rango con java, buscar y reemplazar datos en rango con java
---

{{% alert color="primary" %}}

A veces, necesita buscar y reemplazar datos específicos en un rango, ignorando los valores de celda fuera del rango deseado. Aspose.Cells le permite limitar una búsqueda a un rango específico. Este artículo lo explica.

{{% /alert %}}

Aspose.Cells proporciona el método [**FindOptions.setRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#setRange-com.aspose.cells.CellArea-) para especificar un rango al buscar datos.

Supongamos que desea buscar la cadena **"search"** y reemplazarla con **"replace"** en el rango **E3:H6**. En la captura de pantalla a continuación, se puede ver la cadena "search" en varias celdas, pero queremos reemplazarla solo en un rango dado, aquí resaltado en amarillo.

**Archivo de entrada**

![todo:image_alt_text](search-and-replace-data-in-a-range_1.png)

Después de la ejecución del código, el archivo de salida se ve así. Todas las cadenas "search" dentro del rango han sido reemplazadas por "replace".

Archivo de salida

![todo:image_alt_text](search-and-replace-data-in-a-range_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchReplaceDataInRange-SearchReplaceDataInRange.java" >}}

## Artículos relacionados

- [Buscar o buscar datos](/cells/es/java/find-or-search-data/)
{{< app/cells/assistant language="java" >}}
