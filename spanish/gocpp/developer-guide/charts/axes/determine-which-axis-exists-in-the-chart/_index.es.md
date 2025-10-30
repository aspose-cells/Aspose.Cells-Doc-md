---
title: Determinar qué eje existe en el gráfico con Golang a través de C++
description: Aprende cómo determinar qué eje existe en un gráfico creado usando Aspose.Cells for C++. Nuestra guía te ayudará a entender cómo identificar y acceder a los diferentes ejes en un gráfico, incluyendo los ejes de categoría, valor y secundario.
keywords: Aspose.Cells for C++, gráfico, eje, existencia, categoría, valor, secundario.
type: docs
weight: 140
url: /es/go-cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

A veces, el usuario necesita saber si un eje particular existe en el gráfico. Por ejemplo, quiere saber si existe un Eje de Valor Secundario dentro del gráfico o no. Algunos gráficos como Pie, PieExploded, PiePie, PieBar, Pie3D, Pie3DExploded, Doughnut, DoughnutExploded, etc. no tienen un eje.

Aspose.Cells proporciona [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/go-cpp/chart/hasaxis/) método para determinar si el gráfico tiene un eje específico o no.

{{% /alert %}}

El siguiente código de ejemplo demuestra el uso de [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/go-cpp/chart/hasaxis/) para determinar si el gráfico de muestra tiene Ejes de Categoría y Valor Principales y Secundarios.

## Código C++ para determinar qué eje existe en el gráfico

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetermineWhichAxisExistsInTheChart.go" >}}
## Salida de consola generada por el código de ejemplo

La salida de consola del código se muestra a continuación, que muestra verdadero para Eje de Categoría y Valor Primario y falso para Eje de Categoría y Valor Secundario.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
