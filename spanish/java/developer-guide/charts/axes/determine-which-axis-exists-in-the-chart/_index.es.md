---
title: Determinar qué eje existe en el gráfico
type: docs
weight: 130
url: /es/java/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

A veces, el usuario necesita saber si un eje particular existe en el gráfico. Por ejemplo, quiere saber si existe un eje de valor secundario dentro del gráfico o no. Algunos gráficos como Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded, etc. no tienen un eje.

Aspose.Cells proporciona [**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis-int-boolean-) método para determinar si el gráfico tiene un eje específico o no.

{{% /alert %}}

## Determinar qué eje existe en el gráfico

La siguiente captura de pantalla muestra un gráfico que solo tiene el eje de categoría y valor primario. No tiene ningún eje de categoría y valor secundario.

![todo:image_alt_text](determine-which-axis-exists-in-the-chart_1.png)

El siguiente código de ejemplo demuestra el uso de [**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis-int-boolean-) para determinar si el gráfico de ejemplo tiene ejes de categoría y valor primarios y secundarios. La salida de la consola del código se muestra a continuación, que muestra verdadero para el eje de categoría y valor primario y falso para el eje de categoría y valor secundario.

### Código Java para determinar qué ejes existen en el gráfico

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetermineWhichAxisExistsInChart-DetermineWhichAxisExistsInChart.java" >}}

### Salida de consola generada por el código de ejemplo

Aquí está la salida de consola del código de ejemplo anterior.

{{< highlight java >}}

Has Primary Category Axis: true

Has Secondary Category Axis: false

Has Primary Value Axis: true

Has Secondary Value Axis: false

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
