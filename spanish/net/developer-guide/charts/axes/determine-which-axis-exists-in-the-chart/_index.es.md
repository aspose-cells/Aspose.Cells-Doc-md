---
title: Determinar qué eje existe en el gráfico
type: docs
weight: 140
url: /es/net/determine-which-axis-exists-in-the-chart/
---
{{% alert color="primary" %}}

A veces, el usuario necesita saber si existe un eje en particular en el gráfico. Por ejemplo, quiere saber si existe un eje de valor secundario dentro del gráfico o no. Algunos gráficos como Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded, etc. no tienen un eje.

 Aspose.Cells proporciona[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) método para determinar si el gráfico tiene un eje en particular o no.

{{% /alert %}}

 El siguiente código de ejemplo demuestra el uso de[**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis)para determinar si el gráfico de muestra tiene categoría primaria y secundaria y eje de valor.

## C# código para determinar qué eje existe en el gráfico

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## Salida de la consola generada por el código de muestra

La salida de la consola del código se muestra a continuación, que muestra verdadero para la categoría principal y el eje de valor y falso para la categoría secundaria y el eje de valor.

{{< highlight "java" >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
