---
title: Cómo obtener la posición del objeto en un gráfico
description: Aprenda cómo obtener las posiciones de los objetos en un gráfico de Excel usando Aspose.Cells for .NET. 
keywords: Aspose.Cells for .NET, Gráfico de Excel, Obtener posiciones de objetos.
type: docs
weight: 74
url: /es/net/how-to-get-object-position-in-chart/
---

## Posibles Escenarios de Uso
En algunos escenarios, al usar un gráfico de Excel, puede necesitar obtener la posición de los objetos en el gráfico. Puede lograr fácilmente este requisito con Aspose.Cells.

## Ejemplo: Obtener la posición de un objeto en un gráfico

El siguiente código de muestra carga el [archivo Excel de muestra](TestFile.xlsx) y genera el [archivo Excel de salida](Output.xlsx).
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "get-object-position-in-chart.cs" >}}

Con el código anterior, puede obtener la posición del título del gráfico y del área de grafo del gráfico. 
Con la información de posición, las formas pueden colocarse en la posición correspondiente en el gráfico. 
La salida se muestra en la siguiente imagen, donde una forma está colocada en la esquina superior izquierda del área de grafo y otra forma está colocada debajo del título del gráfico.
![todo:image_alt_text](OutputResult.png)

## Explicación de unidades y conversión

Existen tres unidades para la posición del objeto en el gráfico:

1. Unidades de proporción del área del gráfico.

2. Unidades de 1/4000 del área del gráfico. Esta es una unidad utilizada en versiones antiguas de archivos de Excel, y no se recomienda.

3. Unidades de píxel.

El código de conversión del mismo se muestra en el siguiente código: 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "object-position-unit-in-chart.cs" >}}

{{< app/cells/assistant language="csharp" >}}
