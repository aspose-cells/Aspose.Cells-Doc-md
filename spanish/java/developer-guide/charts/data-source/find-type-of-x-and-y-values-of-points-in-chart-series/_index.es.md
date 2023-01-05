---
title: Buscar tipo de valores X e Y de puntos en series de gráficos
type: docs
weight: 110
url: /es/java/find-type-of-x-and-y-values-of-points-in-chart-series/
---
## **Posibles escenarios de uso**

A veces, desea saber el tipo de valores X e Y de los puntos del gráfico en una serie. Aspose.Cells proporciona[**ChartPoint.XValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#XValueType)y[**ChartPoint.YValueType**](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#YValueType)propiedades que se pueden utilizar para este fin. Tenga en cuenta que tendrá que llamar[**Gráfico.calcular()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()) antes de poder usar estas propiedades de manera efectiva.

## **Buscar tipo de valores X e Y de puntos en series de gráficos**

El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](64716920.xlsx)y accede al primer gráfico dentro de la primera hoja de cálculo. Luego llama al[**Gráfico.calcular()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()y encuentra el tipo de valores X e Y del primer punto del gráfico y los imprime en la consola. Consulte la salida de la consola que se muestra a continuación para obtener una referencia.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.java" >}}

## **Salida de consola**

{{< highlight "java" >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
