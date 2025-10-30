---
title: Buscar datos utilizando valores originales
type: docs
weight: 380
url: /es/python-net/search-data-using-original-values/
description: Aprenda a buscar datos usando valores originales a través de la API de Aspose.Cells for Python via .NET.
keywords: Biblioteca de Excel de Python, Buscar datos usando valores originales en Python, Encontrar datos usando valores originales en Python, Buscar datos por valores originales en Python, Encontrar datos por valores originales en Python
---

{{% alert color="primary" %}}

A veces, el valor de los datos está oculto porque está formateado de alguna manera. Por ejemplo, suponga que la celda D4 tiene la fórmula =Suma(A1:A2) y su valor es 20 pero está formateado como ---, entonces el valor 20 está oculto y no se puede encontrar usando las opciones de búsqueda de Microsoft Excel. Sin embargo, puede encontrarlo usando Aspose.Cells para Python via .NET utilizando [**LookInType.ORIGINAL_VALUES**](https://reference.aspose.com/cells/python-net/aspose.cells/lookintype).

{{% /alert %}}

El siguiente código de muestra ilustra el punto anterior. Encuentra la celda D4 que no se puede encontrar utilizando las opciones de búsqueda de Microsoft Excel, pero Aspose.Cells puede encontrarla usando [**LookInType.ORIGINAL_VALUES**](https://reference.aspose.com/cells/python-net/aspose.cells/lookintype). Por favor, lea los comentarios dentro del código para más información.

## Código de Python para buscar datos usando valores originales

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SearchDataUsingOriginalValues.py" >}}

## Salida de consola generada por el código de ejemplo

Aquí está la salida en consola del código de muestra anterior.

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
