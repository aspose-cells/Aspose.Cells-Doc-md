---
title: Leer etiquetas del eje después de calcular el gráfico
description: Aprenda a leer las etiquetas del eje en Aspose.Cells for .NET después de calcular el gráfico. Nuestra guía le mostrará cómo acceder y recuperar las etiquetas del eje, incluyendo su formato y posicionamiento.
keywords: Aspose.Cells for .NET, gráfico, etiquetas del eje, cálculo, lectura, acceso, recuperación, formato, posicionamiento.
type: docs
weight: 90
url: /es/net/read-axis-labels-after-calculating-the-chart/
---

## **Escenarios de uso posibles**

Puede leer las etiquetas del eje de su gráfico después de calcular sus valores utilizando el método [**Chart.Calculate()**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/calculate/). Utilice el método [**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/net/aspose.cells.charts/axis/getaxistexts/) para este propósito, que devolverá la lista de etiquetas del eje.

## **Leer etiquetas del eje después de calcular el gráfico**

Consulte el siguiente código de ejemplo que carga el [archivo de Excel de muestra](ReadAxisLabels.xlsx) y lee las etiquetas del eje de categoría del gráfico en la primera hoja de cálculo. Luego imprime los valores de las etiquetas del eje en la consola. Consulte la salida de la consola del código de ejemplo a continuación como referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Charts-ReadAxisLabelsAfterCalculatingTheChart.cs" >}}

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
