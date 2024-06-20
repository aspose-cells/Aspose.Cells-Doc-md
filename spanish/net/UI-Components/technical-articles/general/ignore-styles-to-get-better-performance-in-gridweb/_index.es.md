---
title: Ignorar estilos para obtener un mejor rendimiento en GridWeb
type: docs
weight: 1060
url: /es/net/aspose-cells-gridweb/ignorestylewithnodata
description: Este artículo describe cómo usar IgnoreStyleWithNoData para obtener un mejor rendimiento en GridWeb.
keywords: GridWeb,performance
---

## **Escenarios de uso posibles**
Por favor use la propiedad [GridWeb.IgnoreStyleWithNoData](https://reference.aspose.com/cells/net/aspose.cells.gridweb/mainweb/ignorestylewithnodata) para cargar menos filas/columnas requeridas del libro de trabajo.

## **Obtener un mejor rendimiento al cargar el libro de trabajo**
Por favor revise el [archivo de excel de ejemplo](largerowswithstyle.xlsx) 

Cuando se establece IgnoreStyleWithNoData = true;

Como puedes ver, muestra las filas (hasta 15) y columnas (hasta L), no mostrará las últimas filas y columnas continuas sin datos en las celdas. Por lo tanto, el tiempo de carga será menor.

![libro de trabajo con estilo ignorado](ignorestyletrue.png)


Cuando se establece IgnoreStyleWithNoData = false; (el valor predeterminado es false)

Como puedes ver, muestra muchas más filas (hasta 500) y columnas (hasta CZ)

De la fila 16 a la fila 500, algunas celdas tienen estilo de borde, sin embargo, las celdas no contienen datos.

De la columna M a la columna CZ, algunas celdas tienen estilo de borde, sin embargo, las celdas no contienen datos.

![libro de trabajo sin estilo ignorado](ignorestylefalse.png)



