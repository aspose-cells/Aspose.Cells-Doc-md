---
title: Obtener el rango máximo en una hoja de cálculo
type: docs
weight: 360
url: /es/net/get-max-range-in-a-worksheet/
description: Este artículo describe cómo obtener el rango máximo, el rango de datos máximo, el rango de visualización máxima de archivos de Excel con la biblioteca Aspose.Cells para .Net.
---

{{% alert color="primary" %}} 

Al leer datos de la hoja de cálculo, necesitamos conocer el área máxima.

Al copiar todos los datos de una hoja de cálculo, necesitamos conocer el área máxima.

Al exportar un área especificada a html y pdf, necesitamos conocer el área máxima.

Aspose.Cells para .Net contiene diferentes formas de encontrar el rango máximo en una hoja de cálculo. 


{{% /alert %}} 



## **Obteniendo el rango máximo**
En Aspose.Cells, si los objetos [**row**](https://reference.aspose.com/cells/net/aspose.cells/row) y [**column**](https://reference.aspose.com/cells/net/aspose.cells/column) están inicializados, estas filas y columnas se contarán como el área máxima, incluso si no hay datos en filas o columnas vacías.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Range.cs" >}}

## **Obteniendo el rango máximo de datos**
En la mayoría de los casos, solo necesitamos obtener todos los rangos que contienen todos los datos, incluso si las celdas vacías fuera del rango están formateadas.
Y los ajustes sobre formas, tablas y tablas dinámicas se ignorarán.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Data-Range.cs" >}}

## **Obteniendo el rango máximo de visualización**
Cuando exportamos todos los datos de la hoja de cálculo a HTML, PDF o imágenes, necesitamos obtener un área que contenga todos los objetos visibles, incluidos los datos, estilos, gráficos, tablas y tablas dinámicas.
Los siguientes códigos muestran cómo renderizar el rango de visualización máxima a html:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Get-Max-Display-Range.cs" >}}

Aquí está el [archivo de excel fuente](Book1.xlsx).
