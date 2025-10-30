---
title: Agregar conexión de pivote con Golang vía C++
linktitle: Agregar conexión de tabla dinámica
type: docs
weight: 30
url: /es/go-cpp/add-pivot-connection/
description: Aprende cómo agregar una conexión de pivote con la biblioteca Aspose.Cells usando C++.
keywords: Agregar conexión de tabla dinámica sin office 2013, office 2016, office 2019 y office 365.
---

## **Escenarios de uso posibles**

Si desea asociar filtro y tabla dinámica en Excel, debe hacer clic con el botón derecho en el filtro y seleccionar el elemento "Conexiones de informe...". En la lista de opciones, puede operar en la casilla de verificación. Del mismo modo, si desea asociar filtro y tabla dinámica usando la API de Aspose.Cells programáticamente, utilice el método [**Slicer.AddPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/go-cpp/slicer/addpivotconnection/). Asociará el filtro y la tabla dinámica.

## **Asociar filtro y tabla dinámica**

El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](add-pivot-connection.xlsx) que contiene un rebanador existente. Accede al Rebanador y luego asocia el Rebanador y la Tabla dinámica. Finalmente, guarda el libro de trabajo como [archivo de Excel de salida](add-pivot-connection-out.xlsx). 

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddPivotConnection.go" >}}
