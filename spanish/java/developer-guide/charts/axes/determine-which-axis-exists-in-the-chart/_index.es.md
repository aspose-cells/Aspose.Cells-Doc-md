---
title: Determinar qué eje existe en el gráfico
type: docs
weight: 130
url: /es/java/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

A veces, el usuario necesita saber si existe un eje en particular en el Gráfico. Por ejemplo, quiere saber si existe un eje de valor secundario dentro del gráfico o no. Algunos gráficos como Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded, etc. no tienen un eje.

 Aspose.Cells proporciona[**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)) para determinar si el gráfico tiene un eje en particular o no.

{{% /alert %}}

## Determinar qué eje existe en el gráfico

La siguiente captura de pantalla muestra un gráfico que solo tiene la categoría principal y el eje de valor. No tiene Categoría Secundaria y Eje de Valor.

![todo:imagen_alternativa_texto](determine-which-axis-exists-in-the-chart_1.png)

 El siguiente código de ejemplo demuestra el uso de[**Chart.hasAxis(int axisType, boolean isPrimary)**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#hasAxis(int,%20boolean)para determinar si el gráfico de muestra tiene categoría primaria y secundaria y eje de valor. La salida de la consola del código se muestra a continuación, que muestra verdadero para la categoría principal y el eje de valor y falso para la categoría secundaria y el eje de valor.

### Java código para determinar qué eje existe en el gráfico

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetermineWhichAxisExistsInChart-DetermineWhichAxisExistsInChart.java" >}}

### Salida de la consola generada por el código de muestra

Aquí está la salida de la consola del código de muestra anterior.

{{< highlight "java" >}}

Has Primary Category Axis: true

Has Secondary Category Axis: false

Has Primary Value Axis: true

Has Secondary Value Axis: false

{{< /highlight >}}
