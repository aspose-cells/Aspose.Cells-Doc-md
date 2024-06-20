---
title: Encuentre si los Puntos de Datos están en el Segundo Círculo o Barra en un Gráfico de Círculo de Círculos o Barra de Círculos
type: docs
weight: 910
url: /es/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Escenarios de uso posibles**
Puedes encontrar si los puntos de datos de la serie están en el segundo gráfico circular en el gráfico *Tarta de tarta* o en la barra del gráfico *Barra de tarta* utilizando Aspose.Cells. Utiliza la propiedad [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot) para determinarlo.

Descarga el [archivo de Excel de muestra](5473373.xlsx) utilizado en el siguiente código de muestra y observa su salida en la consola. Si abres el [archivo de Excel de muestra](5473373.xlsx), verás que todos los puntos de datos que son menores que 10 están dentro de la barra del gráfico *Barra de tarta*, como también se muestra en la salida de la consola.
## **Encontrar si los Puntos de Datos están en el Segundo Pastel o Barra en un Gráfico de Pastel de Pastel o de Barra de Pastel**
El siguiente código de ejemplo muestra cómo averiguar si los puntos de datos están en el segundo círculo o barra en un gráfico de Círculo de Círculos o Barra de Círculos.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindDataPoints-FindDataPoints.java" >}}
## **Salida de la consola**
Observa la siguiente salida de consola generada después de la ejecución del código de muestra anterior con el [archivo de Excel de muestra](5473373.xlsx). Si [IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot) es **falso**, el punto de datos está dentro de la tarta, y si es **verdadero**, entonces el punto de datos está dentro de la barra.

{{< highlight java >}}

 Value: 15

IsInSecondaryPlot: false

Value: 9

IsInSecondaryPlot: true

Value: 2

IsInSecondaryPlot: true

Value: 40

IsInSecondaryPlot: false

Value: 5

IsInSecondaryPlot: true

Value: 4

IsInSecondaryPlot: true

Value: 25

IsInSecondaryPlot: false

{{< /highlight >}}
