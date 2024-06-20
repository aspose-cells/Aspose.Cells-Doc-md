---
title: Determinar qué eje existe en el gráfico
description: Aprenda a determinar qué ejes existen en un gráfico creado usando Aspose.Cells for .NET. Nuestra guía le ayudará a entender cómo identificar y acceder a los diferentes ejes en un gráfico, incluyendo los ejes de categoría, valor y secundarios.
keywords: Aspose.Cells for .NET, gráfico, eje, existencia, categoría, valor, secundario.
type: docs
weight: 140
url: /es/net/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

A veces, el usuario necesita saber si un eje particular existe en el gráfico. Por ejemplo, quiere saber si existe un Eje de Valor Secundario dentro del gráfico o no. Algunos gráficos como Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded, etc. no tienen un eje.

Aspose.Cells proporciona [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) método para determinar si el gráfico tiene un eje específico o no.

{{% /alert %}}

El siguiente código de muestra demuestra el uso de [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/hasaxis) para determinar si el gráfico de muestra tiene Ejes de Categoría y Valor Primarios y Secundarios.

## Código C# para determinar qué ejes existen en el gráfico

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-DetermineAxisInChart-DetermineAxisInChart.cs" >}}

## Salida de consola generada por el código de ejemplo

La salida de consola del código se muestra a continuación, que muestra verdadero para Eje de Categoría y Valor Primario y falso para Eje de Categoría y Valor Secundario.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
