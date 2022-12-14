---
title: Averigüe si los puntos de datos están en el segundo pastel o barra en un gráfico circular de pastel o de barra de pastel
type: docs
weight: 910
url: /es/java/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---
## **Posibles escenarios de uso**
 Puede encontrar si los puntos de datos de la serie están en el segundo pastel en*pastel de pastel* gráfico o en la barra de*barra de pastel* gráfico usando Aspose.Cells. Utilice el[ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot)propiedad para determinarlo.

 Por favor descarga el[ejemplo de archivo de Excel](5473373.xlsx) utilizado en el siguiente código de muestra y vea su salida de consola. Si abres el[ejemplo de archivo de Excel](5473373.xlsx), encontrará, todos los puntos de datos que son menos de 10 están dentro de la barra de*barra de pastel*gráfico como también se muestra en la salida de la consola.
## **Averigüe si los puntos de datos están en el segundo pastel o barra en un gráfico circular de pastel o de barra de pastel**
 El siguiente código de ejemplo muestra cómo encontrar si los puntos de datos están en el segundo gráfico circular o en la barra de un*pastel de pastel* o*barra de pastel*cuadro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindDataPoints-FindDataPoints.java" >}}
## **Salida de consola**
 Consulte la siguiente salida de la consola generada después de la ejecución del código de ejemplo anterior con el[ejemplo de archivo de Excel](5473373.xlsx) . Si[IsInSecondaryPlot](https://reference.aspose.com/cells/java/com.aspose.cells/chartpoint#IsInSecondaryPlot) es**falso** , el punto de datos está dentro de la tarta o si está**verdadero**, entonces el punto de datos está dentro de la barra.

{{< highlight "java" >}}

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
