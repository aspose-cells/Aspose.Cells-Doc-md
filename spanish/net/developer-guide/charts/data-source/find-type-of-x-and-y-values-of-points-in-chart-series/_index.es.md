---
title: Encuentre el tipo de valores X e Y de puntos en series de gráficos
description: Aprenda a determinar el tipo de valores X e Y en puntos de series de gráficos usando Aspose.Cells for .NET. Nuestra guía explicará los diferentes tipos de valores de datos y le mostrará cómo acceder a ellos y trabajar con ellos en sus gráficos.
keywords: Aspose.Cells for .NET, charting, X values, Y values, data types, access, work with, chart series.
type: docs
weight: 150
url: /es/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---
##  **Posibles escenarios de uso**
En algún momento, querrás saber el tipo de valores X e Y de los puntos del gráfico en una serie. Aspose.Cells proporciona las propiedades ChartPoint.XValueType y ChartPoint.YValueType que se pueden utilizar para este propósito. Tenga en cuenta que deberá llamar al método Chart.Calculate() antes de poder utilizar estas propiedades de forma eficaz.
##  **Encuentre el tipo de valores X e Y de puntos en series de gráficos**
 El siguiente código de muestra carga el[archivo de Excel de muestra](64716905.xlsx) y accede al primer gráfico dentro de la primera hoja de trabajo. Luego llama al método Chart.Calculate() y encuentra el tipo de valores X e Y del primer punto del gráfico y los imprime en la consola. Consulte la salida de la consola que se muestra a continuación como referencia.
##  **Código de muestra**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}
##  **Salida de consola**
{{< highlight "java" >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
