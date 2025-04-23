---
title: Encuentre si los Puntos de Datos están en el Segundo Círculo o Barra en un Gráfico de Círculo de Círculos o Barra de Círculos
description: Aprenda cómo usar Aspose.Cells for .NET para averiguar si los puntos de datos están en el segundo círculo o barra en un gráfico de círculo de círculos o barra de círculos. Nuestra guía demostrará cómo identificar y acceder al segundo círculo o barra en un gráfico compuesto, lo que le permitirá analizar y manipular los datos de manera efectiva.
keywords: Aspose.Cells for .NET, Gráfico de Círculo de Círculos, Gráfico de Barra de Círculos, Círculo Secundario, Barra Secundaria, Análisis de Datos, Manipulación de Datos.
type: docs
weight: 180
url: /es/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Escenarios de uso posibles**
Puede averiguar si los puntos de datos de la serie están en el segundo círculo en el gráfico de Círculo de Círculos o en la barra del gráfico de Barra de Círculos utilizando Aspose.Cells. Utilice la propiedad [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) para determinarlo.

Descargue el [archivo excel de ejemplo](5115193.xlsx) utilizado en el siguiente código de ejemplo y vea su salida en consola. Si abre el [archivo excel de ejemplo](5115193.xlsx), encontrará que todos los puntos de datos que son menores a 10 están dentro de la barra del Gráfico de Barra de Círculos como también se muestra en la salida de consola.
## **Encontrar si los Puntos de Datos están en el Segundo Pastel o Barra en un Gráfico de Pastel de Pastel o de Barra de Pastel**
El siguiente código de ejemplo muestra cómo averiguar si los puntos de datos están en el segundo círculo o barra en un gráfico de Círculo de Círculos o Barra de Círculos.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
## **Salida de la consola**
Consulte la siguiente salida en consola generada después de la ejecución del código de ejemplo anterior con el [archivo excel de ejemplo](5115193.xlsx). Si [IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot) es **false**, el punto de datos está dentro del Círculo o si es **true**, entonces el punto de datos está dentro de la Barra.



{{< highlight java >}}

 Value: 15

IsInSecondaryPlot: False

Value: 9

IsInSecondaryPlot: True

Value: 2

IsInSecondaryPlot: True

Value: 40

IsInSecondaryPlot: False

Value: 5

IsInSecondaryPlot: True

Value: 4

IsInSecondaryPlot: True

Value: 25

IsInSecondaryPlot: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
