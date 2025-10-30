---
title: Obtener el rango máximo en una hoja de cálculo con Golang vía C++
linktitle: Obtener el rango máximo en una hoja de cálculo
type: docs
weight: 360
url: /es/go-cpp/get-max-range-in-a-worksheet/
description: Este artículo describe cómo obtener el rango máximo, rango de datos máximo y rango de visualización máximo de archivos de Excel con la biblioteca Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Al leer datos de la hoja de cálculo, necesitamos conocer el área máxima.

Al copiar todos los datos de una hoja de cálculo, necesitamos conocer el área máxima.

Al exportar un área específica a HTML y PDF, debemos conocer el área máxima.

Aspose.Cells for C++ contiene diferentes formas de encontrar el rango máximo en una hoja de cálculo. 

{{% /alert %}} 

## **Obteniendo el rango máximo**
En Aspose.Cells, si los objetos [**Row**](https://reference.aspose.com/cells/go-cpp/row/) y [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/) están inicializados, estas filas y columnas se contarán hasta el área máxima, incluso si no hay datos en filas o columnas vacías.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange.go" >}}
## **Obteniendo el rango máximo de datos**
En la mayoría de los casos, solo necesitamos obtener todos los rangos que contienen todos los datos, incluso si las celdas vacías fuera del rango están formateadas.
Y la configuración sobre formas, tablas y tablas dinámicas se ignorará.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange-1.go" >}}
## **Obteniendo el rango máximo de visualización**
Cuando exportamos todos los datos de la hoja de cálculo a HTML, PDF o imágenes, necesitamos obtener un área que contenga todos los objetos visibles, incluidos los datos, estilos, gráficos, tablas y tablas dinámicas.
Los siguientes códigos muestran cómo renderizar el rango de visualización máxima a HTML:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange-2.go" >}}
Aquí está el [archivo de excel fuente](Book1.xlsx).
