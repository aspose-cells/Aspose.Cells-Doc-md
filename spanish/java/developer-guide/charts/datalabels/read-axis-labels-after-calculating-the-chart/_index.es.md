---
title: Leer las etiquetas de los ejes después de calcular el gráfico
description: Aprenda a leer las etiquetas de los ejes en Aspose.Cells for Java después de calcular el gráfico. Nuestra guía le mostrará cómo acceder y recuperar etiquetas de ejes, incluido su formato y posicionamiento.
keywords: Aspose.Cells for Java, chart, axis labels, calculation, reading, accessing, retrieving, formatting, positioning.
type: docs
weight: 90
url: /es/java/read-axis-labels-after-calculating-the-chart/
---
##  **Posibles escenarios de uso**

Puede leer las etiquetas de los ejes de su gráfico después de calcular sus valores utilizando el[**Gráfico.calcular()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart/#calculate--)método. Por favor use el[**Eje.getAxisTexts()**](https://reference.aspose.com/cells/java/com.aspose.cells/axis/#getAxisTexts--)método para este propósito que devolverá la lista de etiquetas de ejes.

##  **Leer las etiquetas de los ejes después de calcular el gráfico**

Consulte el siguiente código de muestra que carga el[archivo de Excel de muestra](64716829.xlsx)y lee las etiquetas del eje de categorías del gráfico en la primera hoja de trabajo. Luego imprime los valores de las etiquetas de los ejes en la consola. Consulte la salida de la consola del código de muestra que se proporciona a continuación como referencia.

##  **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-ReadAxisLabelsAfterCalculatingTheChart.java" >}}

##  **Salida de consola**

{{< highlight "java" >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
