---
title: Encontrar el tipo de valores X e Y de los puntos en la serie del gráfico
type: docs
weight: 110
url: /es/java/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Escenarios de uso posibles**

A veces, desea saber el tipo de valores X e Y de los puntos del gráfico en una serie. Aspose.Cells proporciona las propiedades [**ChartPoint.XValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#XValueType) y [**ChartPoint.YValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#YValueType) que se pueden utilizar para este propósito. Tenga en cuenta que deberá llamar al método [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--) antes de poder usar estas propiedades de manera efectiva.

## **Encontrar el tipo de valores X e Y de los puntos en la serie del gráfico**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](64716920.xlsx) y accede al primer gráfico dentro de la primera hoja de cálculo. Luego llama al método [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--) y encuentra el tipo de valores X e Y del primer punto del gráfico, y los imprime en la consola. Consulte la salida de la consola que se muestra a continuación como referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.java" >}}

## **Salida de la consola**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
