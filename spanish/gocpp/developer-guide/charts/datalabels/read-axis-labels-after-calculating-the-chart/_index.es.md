---
title: Leer etiquetas del eje después de calcular el gráfico con Golang a través de C++
linktitle: Leer etiquetas del eje después de calcular el gráfico
description: Aprende cómo leer las etiquetas del eje en Aspose.Cells for C++ después de calcular el gráfico. Nuestra guía te mostrará cómo acceder y recuperar las etiquetas del eje, incluyendo su formato y posición.
keywords: Aspose.Cells for C++, gráfico, etiquetas del eje, cálculo, lectura, acceso, recuperación, formato, posición.
type: docs
weight: 90
url: /es/go-cpp/read-axis-labels-after-calculating-the-chart/
---

## **Escenarios de uso posibles**

Puede leer las etiquetas del eje de su gráfico después de calcular sus valores utilizando el método [**Chart.Calculate()**](https://reference.aspose.com/cells/go-cpp/chart/calculate/). Utilice el método [**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/getaxistexts/) para este propósito, que devolverá la lista de etiquetas del eje.

## **Leer etiquetas del eje después de calcular el gráfico**

Consulte el siguiente código de ejemplo que carga el [archivo de Excel de muestra](ReadAxisLabels.xlsx) y lee las etiquetas del eje de categoría del gráfico en la primera hoja de cálculo. Luego imprime los valores de las etiquetas del eje en la consola. Consulte la salida de la consola del código de ejemplo a continuación como referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReadAxisLabelsAfterCalculatingTheChart.go" >}}
## **Salida de la consola**

{{< highlight cpp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
