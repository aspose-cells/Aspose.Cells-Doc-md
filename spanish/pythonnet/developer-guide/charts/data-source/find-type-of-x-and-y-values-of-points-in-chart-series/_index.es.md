---
title: Encontrar el tipo de valores X e Y de los puntos en la serie del gráfico
description: Aprenda cómo determinar el tipo de valores de X e Y en los puntos de serie de gráficos usando Aspose.Cells para Python via .NET. Nuestra guía explicará los diferentes tipos de valores de datos y le mostrará cómo acceder y trabajar con ellos en sus gráficos.
keywords: Aspose.Cells para Python via .NET, graficación, valores de X, valores de Y, tipos de datos, acceso, trabajar con, serie de gráficos.
type: docs
weight: 150
url: /es/python-net/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Escenarios de uso posibles**
A veces, deseas conocer el tipo de valores de X e Y de los puntos del gráfico en una serie. Aspose.Cells para Python via .NET proporciona las propiedades [**ChartPoint.x_value_type**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/x_value_type/) y [**ChartPoint.y_value_type**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/y_value_type/) que se pueden usar para este propósito. Ten en cuenta que tendrás que llamar al método [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/#) antes de poder usar estas propiedades de manera efectiva.

## **Encontrar el tipo de valores X e Y de los puntos en la serie del gráfico**
El siguiente código de ejemplo carga el [archivo de ejemplo de Excel](64716905.xlsx) y accede al primer gráfico dentro de la primera hoja. Luego llama al método [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/#) y encuentra el tipo de valores de X e Y del primer punto del gráfico y los imprime en la consola. Por favor, consulta la salida de la consola a continuación para referencia.

## **Código de muestra**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.py" >}}

## **Salida de la consola**

{{< highlight java >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
