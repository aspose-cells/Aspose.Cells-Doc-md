---
title: Obtener el rango máximo en una hoja de cálculo
type: docs
weight: 360
url: /es/python-net/get-max-range-in-a-worksheet/
description: Este artículo describe cómo obtener el rango máximo, el rango máximo de datos, el rango máximo de visualización de archivos de Excel con la biblioteca Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel de Python, obtener el rango máximo en Python, obtener el rango máximo de datos en Python, obtener el rango máximo de visualización en Python.
---

{{% alert color="primary" %}} 

Al leer datos de la hoja de cálculo, necesitamos conocer el área máxima.

Al copiar todos los datos de una hoja de cálculo, necesitamos conocer el área máxima.

Al exportar un área especificada a html y pdf, necesitamos conocer el área máxima.

Aspose.Cells para Python via .NET contiene diferentes maneras de encontrar el rango máximo en una hoja de cálculo. 


{{% /alert %}} 



## **Cómo obtener el rango máximo**
En Aspose.Cells para Python via .NET, si los objetos [**row**](https://reference.aspose.com/cells/python-net/aspose.cells/row) y [**column**](https://reference.aspose.com/cells/python-net/aspose.cells/column) están inicializados, se contarán las filas y columnas para formar la área máxima, incluso si no hay datos en las filas o columnas vacías.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Range.py" >}}

## **Cómo obtener el rango máximo de datos**
En la mayoría de los casos, solo necesitamos obtener todos los rangos que contienen todos los datos, incluso si las celdas vacías fuera del rango están formateadas.
Y los ajustes sobre formas, tablas y tablas dinámicas se ignorarán.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Data-Range.py" >}}

## **Cómo obtener el rango máximo de visualización**
Cuando exportamos todos los datos de la hoja de cálculo a HTML, PDF o imágenes, necesitamos obtener un área que contenga todos los objetos visibles, incluidos los datos, estilos, gráficos, tablas y tablas dinámicas.
Los siguientes códigos muestran cómo renderizar el rango de visualización máxima a html:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Get-Max-Display-Range.py" >}}

Aquí está el [archivo de excel fuente](Book1.xlsx).
{{< app/cells/assistant language="python-net" >}}
