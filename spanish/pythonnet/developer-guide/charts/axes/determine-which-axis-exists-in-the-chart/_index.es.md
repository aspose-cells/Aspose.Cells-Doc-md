---
title: Determinar qué eje existe en el gráfico
description: Aprende cómo determinar qué eje existe en un gráfico creado con Aspose.Cells para Python via .NET. Nuestra guía te ayudará a entender cómo identificar y acceder a los diferentes ejes en un gráfico, incluyendo los ejes de categoría, valor y secundarios.
keywords: Aspose.Cells para Python via .NET, gráfico, eje, existencia, categoría, valor, secundario.
type: docs
weight: 140
url: /es/python-net/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

A veces, el usuario necesita saber si un eje particular existe en el gráfico. Por ejemplo, quiere saber si existe un Eje de Valor Secundario dentro del gráfico o no. Algunos gráficos como Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded, etc. no tienen un eje.

Aspose.Cells para Python via .NET proporciona [**Chart.has_axis(AxisType axis_type, bool is_primary)**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/has_axis) método para determinar si el gráfico tiene un eje en particular o no.

{{% /alert %}}

El siguiente código de muestra demuestra el uso de [**Chart.has_axis(AxisType axis_type, bool is_primary)**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/has_axis) para determinar si el gráfico de muestra tiene Ejes de Categoría y Valor Primarios y Secundarios.

## Código C# para determinar qué ejes existen en el gráfico

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-DetermineAxisInChart.py" >}}

## Salida de consola generada por el código de ejemplo

La salida de consola del código se muestra a continuación, que muestra verdadero para Eje de Categoría y Valor Primario y falso para Eje de Categoría y Valor Secundario.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
