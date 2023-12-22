---
title: Encuentre si los puntos de datos están en el segundo pastel o barra en un gráfico circular o de barras
description: Aprenda a utilizar Aspose.Cells for .NET para determinar si los puntos de datos están en el segundo pastel o barra de un gráfico circular o de barras. Nuestra guía demostrará cómo identificar y acceder a la barra o pastel secundario en un gráfico compuesto, lo que le permitirá analizar y manipular los datos de manera efectiva.
keywords: Aspose.Cells for .NET, Pie of Pie Chart, Bar of Pie Chart, Secondary Pie, Secondary Bar, Data Analysis, Data Manipulation.
type: docs
weight: 180
url: /es/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---
##  **Posibles escenarios de uso**
 Puede averiguar si los puntos de datos de la serie están en el segundo pastel en*pastel de pastel* gráfico o en la barra de*barra de pastel* gráfico utilizando Aspose.Cells. Utilice el[ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)propiedad para determinarlo.

 Por favor descargue el[archivo de excel de muestra](5115193.xlsx)utilizado en el siguiente código de muestra y vea su salida de consola. Si abres el[archivo de excel de muestra](5115193.xlsx) , encontrará que todos los puntos de datos que son menores de 10 están dentro de la barra de*barra de pastel*gráfico como también se muestra en la salida de la consola.
##  **Encuentre si los puntos de datos están en el segundo pastel o barra en un gráfico circular o de barras**
 El siguiente código de muestra muestra cómo encontrar si los puntos de datos están en el segundo pastel o barra en un*pastel de pastel* o*barra de pastel*cuadro.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindDataPointsInPieBar-FindDataPointsInPieBar.cs" >}}
##  **Salida de consola**
 Consulte el siguiente resultado de consola generado después de la ejecución del código de muestra anterior con el[archivo de excel de muestra](5115193.xlsx) . Si[Está en la parcela secundaria](https://reference.aspose.com/cells/net/aspose.cells.charts/chartpoint/properties/isinsecondaryplot)es *falso**, el punto de datos está dentro del pastel o si es *verdadero**, entonces el punto de datos está dentro de la barra.



{{< highlight "java" >}}

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
