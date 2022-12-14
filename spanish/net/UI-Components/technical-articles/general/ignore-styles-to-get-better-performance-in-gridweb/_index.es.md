---
title: Ignorar estilos para obtener un mejor rendimiento en GridWeb
type: docs
weight: 1060
url: /es/net/aspose-cells-gridweb/ignorestylewithnodata
description: Este artículo describe cómo usar IgnoreStyleWithNoData para obtener un mejor rendimiento para la biblioteca Aspose.Cells.GridWeb.
keywords: performance
---
## **Posibles escenarios de uso**
 Por favor use[GridWeb.IgnoreStyleWithNoData](https://reference.aspose.com/cells/net/aspose.cells.gridweb/mainweb/ignorestylewithnodata)propiedad para cargar menos filas/columnas requeridas del libro de trabajo.
 
## **Obtenga un mejor rendimiento al cargar el libro de trabajo**
 Por favor, checa el[ejemplo de archivo de Excel](largerowswithstyle.xlsx) 

Cuando se establece IgnoreStyleWithNoData = true;

Como puede ver, muestra filas (hasta 15) y columnas (hasta L), no mostrará las últimas filas y columnas continuas sin datos en las celdas. Por lo tanto, el tiempo de carga será menor.

![libro de trabajo con estilo ignorar](ignorestyletrue.png)


Cuando se establece IgnoreStyleWithNoData = falso; (el valor predeterminado es falso)

Como puede ver, muestra muchas más filas (hasta 500) y columnas (hasta CZ)

Desde la fila 16 hasta la fila 500, algunas de las celdas han establecido el estilo de borde, sin embargo, las celdas no contienen datos.

Desde la columna M hasta la columna CZ, algunas de las celdas han establecido el estilo de borde, sin embargo, las celdas no contienen datos.

![libro de trabajo sin ignorar el estilo](ignorestylefalse.png)
 
 
 