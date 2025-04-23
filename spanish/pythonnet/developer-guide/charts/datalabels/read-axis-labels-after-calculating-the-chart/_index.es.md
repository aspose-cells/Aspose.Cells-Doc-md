---
title: Leer etiquetas del eje después de calcular el gráfico
description: Aprenda cómo leer las etiquetas de los ejes en Aspose.Cells para Python via .NET después de calcular el gráfico. Nuestra guía le mostrará cómo acceder y recuperar las etiquetas de los ejes, incluyendo su formato y posición.
keywords: Aspose.Cells para Python via .NET, gráfico, etiquetas de eje, cálculo, lectura, acceso, recuperación, formato, posición.
type: docs
weight: 90
url: /es/python-net/read-axis-labels-after-calculating-the-chart/
---

## **Escenarios de uso posibles**

Puede leer las etiquetas del eje de su gráfico después de calcular sus valores utilizando el método [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/). Utilice el método [**Axis.get_axis_texts()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/axis/get_axis_texts) para este propósito, que devolverá la lista de etiquetas del eje.

## **Leer etiquetas del eje después de calcular el gráfico**

Consulte el siguiente código de ejemplo que carga el [archivo de Excel de muestra](ReadAxisLabels.xlsx) y lee las etiquetas del eje de categoría del gráfico en la primera hoja de cálculo. Luego imprime los valores de las etiquetas del eje en la consola. Consulte la salida de la consola del código de ejemplo a continuación como referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ReadAxisLabelsAfterCalculatingTheChart.py" >}}

## **Salida de la consola**

{{< highlight csharp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
