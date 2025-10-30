---
title: Eliminar conexión de pivote con Golang vía C++
linktitle: Eliminar conexión de tabla dinámica
type: docs
weight: 30
url: /es/go-cpp/remove-pivot-connection/
description: Aprenda cómo quitar la conexión de pivote con la biblioteca Aspose.Cells usando C++.
keywords: Eliminar conexión de tabla dinámica sin office 2013, office 2016, office 2019 y office 365.
---

## **Escenarios de uso posibles**

Si desea desvincular un filtro y una tabla dinámica en Excel, debe hacer clic con el botón derecho en el filtro y seleccionar el elemento "Conexiones de informe...". En la lista de opciones, puede operar en la casilla de verificación. Del mismo modo, si desea desvincular un filtro y una tabla dinámica utilizando la API de Aspose.Cells de forma programática, utilice el método [**Slicer.RemovePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/go-cpp/slicer/removepivotconnection/). Desvinculará el filtro y la tabla dinámica.

## **Desasociar filtro y tabla dinámica**

El siguiente código de ejemplo carga el [archivo Excel de muestra](remove-pivot-connection.xlsx) que contiene un filtro existente. Accede a los filtros y luego disocia el filtro y la tabla dinámica. Finalmente, guarda el libro como [archivo Excel de salida](remove-pivot-connection-out.xlsx). 

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovePivotConnection.go" >}}
