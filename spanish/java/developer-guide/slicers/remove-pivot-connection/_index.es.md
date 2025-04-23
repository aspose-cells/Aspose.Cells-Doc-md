---
title: Eliminar conexión de tabla dinámica
type: docs
weight: 30
url: /es/java/remove-pivot-connection/
description: Aprenda cómo eliminar la conexión de tabla dinámica con la biblioteca Aspose.Cells Java.
keywords: Eliminar conexión de tabla dinámica sin office 2013, office 2016, office 2019 y office 365.
---

## **Escenarios de uso posibles**

Si desea desvincular un filtro y una tabla dinámica en Excel, debe hacer clic con el botón derecho en el filtro y seleccionar el elemento "Conexiones de informe...". En la lista de opciones, puede operar en la casilla de verificación. Del mismo modo, si desea desvincular un filtro y una tabla dinámica utilizando la API de Aspose.Cells de forma programática, utilice el método [**Slicer.removePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#removePivotConnection-com.aspose.cells.PivotTable-). Desvinculará el filtro y la tabla dinámica.

## **Eliminar rebanador**

El siguiente código de ejemplo carga el [archivo Excel de muestra](remove-pivot-connection.xlsx) que contiene un filtro existente. Accede a los filtros y luego disocia el filtro y la tabla dinámica. Finalmente, guarda el libro como [archivo Excel de salida](remove-pivot-connection-out.xlsx). 


## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Removing-Pivot-Connection.java" >}}
{{< app/cells/assistant language="java" >}}
