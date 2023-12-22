---
title: Obtenga el rango máximo en una hoja de trabajo
type: docs
weight: 360
url: /es/net/get-max-range-in-a-worksheet/
description: Este artículo describe cómo obtener el rango máximo, el rango máximo de datos y el rango máximo de visualización de archivos Excel con Aspose.Cells para la biblioteca .Net.
---
{{% alert color="primary" %}} 

Al leer datos de la hoja de trabajo, necesitamos saber el área máxima.

Al copiar todos los datos de una hoja de trabajo, necesitamos saber el área máxima.

Al exportar un área específica a html y pdf, necesitamos saber el área máxima.

 Aspose.Cells para .Net contiene diferentes formas de encontrar el rango máximo en una hoja de trabajo.


{{% /alert %}} 



##  **Obteniendo rango máximo**
 En Aspose.Cells, si el[**fila**](https://reference.aspose.com/cells/net/aspose.cells/row) y[**columna**](https://reference.aspose.com/cells/net/aspose.cells/column) Cuando se inicializan los objetos, estas filas y columnas se contarán hasta el área máxima, incluso si no hay datos en filas o columnas vacías.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Range.cs" >}}

##  **Obteniendo rango máximo de datos**
En la mayoría de los casos, sólo necesitamos obtener todos los rangos que contienen todos los datos, incluso si las celdas vacías fuera del rango están formateadas.
Y se ignorarán las configuraciones sobre formas, tablas y tablas dinámicas.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Data-Range.cs" >}}

##  **Obteniendo el rango máximo de visualización**
Cuando exportamos todos los datos de la hoja de trabajo a HTML, PDF o imágenes, necesitamos obtener un área que contenga todos los objetos visibles, incluidos datos, estilos, gráficos, tablas y tablas dinámicas.
Los siguientes códigos muestran cómo representar el rango máximo de visualización en html:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Display-Range.cs" >}}

 Aquí está[archivo excel fuente](Book1.xlsx).
