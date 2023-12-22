---
title: Determinar qué eje existe en el gráfico.
description: Aprenda a determinar qué eje existe en un gráfico creado con Aspose.Cells for .NET. Nuestra guía le ayudará a comprender cómo identificar y acceder a los diferentes ejes de un gráfico, incluidos los ejes de categoría, valor y secundarios.
keywords: Aspose.Cells for .NET, chart, axis, existence, category, value, secondary.
type: docs
weight: 140
url: /es/net/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

A veces, el usuario necesita saber si existe un eje particular en el gráfico. Por ejemplo, quiere saber si existe un eje de valor secundario dentro del gráfico o no. Algunos gráficos como Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Donut, DoughnutExploded, etc. no tienen eje.

 Aspose.Cells proporciona[**Chart.HasAxis (AxisType axisType, bool es Primario)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) Método para determinar si el gráfico tiene un eje particular o no.

{{% /alert %}}

 El siguiente código de muestra demuestra el uso de[**Chart.HasAxis (AxisType axisType, bool es Primario)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)para determinar si el gráfico de muestra tiene categoría primaria y secundaria y eje de valor.

##  Código C# para determinar qué eje existe en el gráfico.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## Salida de consola generada por el código de muestra

La salida de la consola del código se muestra a continuación, que muestra verdadero para la categoría principal y el eje de valor y falso para la categoría secundaria y el eje de valor.

{{< highlight "java" >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
