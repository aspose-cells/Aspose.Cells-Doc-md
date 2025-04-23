---
title: Encontrar el tipo de valores X e Y de los puntos en la serie del gráfico
description: Aprenda cómo determinar el tipo de valores de X e Y en los puntos de la serie del gráfico usando Aspose.Cells for .NET. Nuestra guía explicará los diferentes tipos de valores de datos y le mostrará cómo acceder y trabajar con ellos en sus gráficos.
keywords: Aspose.Cells for .NET, creación de gráficos, valores X, valores Y, tipos de datos, acceso, trabajar con, series de gráficos.
type: docs
weight: 150
url: /es/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Escenarios de uso posibles**
A veces, desea conocer el tipo de valores de X e Y de los puntos del gráfico en una serie. Aspose.Cells proporciona las propiedades ChartPoint.XValueType y ChartPoint.YValueType que se pueden usar para este propósito. Tenga en cuenta que deberá llamar al método Chart.Calculate() antes de poder usar estas propiedades de manera efectiva.
## **Encontrar el tipo de valores X e Y de los puntos en la serie del gráfico**
El siguiente código de muestra carga el [archivo Excel de muestra](64716905.xlsx) y accede al primer gráfico dentro de la primera hoja de cálculo. Luego llama al método Chart.Calculate() y encuentra el tipo de valores de X e Y del primer punto del gráfico e imprime en la consola. Consulte la salida en la consola que se muestra a continuación como referencia.

## **Código de muestra**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}

## **Salida de la consola**

{{< highlight java >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
