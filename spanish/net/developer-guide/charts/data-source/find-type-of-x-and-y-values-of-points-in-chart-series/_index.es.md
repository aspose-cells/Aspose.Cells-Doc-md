---
title: Buscar tipo de valores X e Y de puntos en series de gráficos
type: docs
weight: 150
url: /es/net/find-type-of-x-and-y-values-of-points-in-chart-series/
---
## **Posibles escenarios de uso**
En algún momento, querrá saber el tipo de valores X e Y de los puntos del gráfico en una serie. Aspose.Cells proporciona las propiedades ChartPoint.XValueType y ChartPoint.YValueType que se pueden usar para este fin. Tenga en cuenta que deberá llamar al método Chart.Calculate() antes de poder usar estas propiedades de manera efectiva.
## **Buscar tipo de valores X e Y de puntos en series de gráficos**
 El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](64716905.xlsx) y accede al primer gráfico dentro de la primera hoja de cálculo. Luego llama al método Chart.Calculate() y encuentra el tipo de valores X e Y del primer punto del gráfico y los imprime en la consola. Consulte la salida de la consola que se muestra a continuación para obtener una referencia.
## **Código de muestra**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-FindTypeOfXandYValuesOfPointsInChartSeries.cs" >}}
## **Salida de consola**
{{< highlight "java" >}}

 X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
