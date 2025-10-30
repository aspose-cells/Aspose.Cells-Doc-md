---
title: Eliminar conexión de tabla dinámica
type: docs
weight: 30
url: /es/python-net/remove-pivot-connection/
description: Aprenda cómo eliminar la conexión de tabla dinámica con la biblioteca Aspose.Cells para Python via .NET.
keywords: Aspose.Cells for Python Excel, biblioteca Excel Python, eliminar conexión de tabla dinámica sin Excel, eliminar conexión de tabla dinámica mediante Aspose.Cells para Python.
---

## **Escenarios de uso posibles**

Si desea disociar el filtro y la tabla dinámica en Excel, debe hacer clic derecho en el filtro y seleccionar el elemento "Conexiones de informe...". En la lista de opciones, puede operar en la casilla de verificación. De manera similar, si desea disociar el filtro y la tabla dinámica utilizando el API de Aspose.Cells para Python via .NET programáticamente, use el método [**Slicer.remove_pivot_connection(pivot)**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/remove_pivot_connection/#aspose.cells.pivot.PivotTable). Esto disociará el filtro y la tabla dinámica.

## **Cómo disociar filtro y tabla dinámica usando la biblioteca de Excel de Aspose.Cells para Python**

El siguiente código de ejemplo carga el [archivo Excel de muestra](remove-pivot-connection.xlsx) que contiene un filtro existente. Accede a los filtros y luego disocia el filtro y la tabla dinámica. Finalmente, guarda el libro como [archivo Excel de salida](remove-pivot-connection-out.xlsx). 


## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-Removing-Pivot-Connection.py" >}}
{{< app/cells/assistant language="python-net" >}}
