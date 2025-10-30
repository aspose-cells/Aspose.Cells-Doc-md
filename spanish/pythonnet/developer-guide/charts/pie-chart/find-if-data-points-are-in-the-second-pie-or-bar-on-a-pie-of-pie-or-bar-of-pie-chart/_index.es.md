---
title: Encuentre si los Puntos de Datos están en el Segundo Círculo o Barra en un Gráfico de Círculo de Círculos o Barra de Círculos
description: Aprende cómo usar Aspose.Cells para Python via .NET para determinar si los puntos de datos están en la segunda tarta o barra en un gráfico de tarta de tartas o barras. Nuestra guía demostrará cómo identificar y acceder a la tarta o barra secundaria en un gráfico compuesto, permitiéndote analizar y manipular los datos eficazmente.
keywords: Aspose.Cells para Python via .NET, Gráfico de Tarta de Pie, Barra de Pie, Tarta Secundaria, Barra Secundaria, Análisis de Datos, Manipulación de Datos.
type: docs
weight: 180
url: /es/python-net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Escenarios de uso posibles**
Puedes encontrar si los puntos de datos de la serie están en la segunda tarta en *Pie of Pie* o en la barra en *Bar of Pie* usando Aspose.Cells para Python via .NET. Por favor, usa la propiedad [ChartPoint.is_in_secondary_plot](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/is_in_secondary_plot) para determinarlo.

Descargue el [archivo excel de ejemplo](5115193.xlsx) utilizado en el siguiente código de ejemplo y vea su salida en consola. Si abre el [archivo excel de ejemplo](5115193.xlsx), encontrará que todos los puntos de datos que son menores a 10 están dentro de la barra del Gráfico de Barra de Círculos como también se muestra en la salida de consola.

## **Encontrar si los Puntos de Datos están en el Segundo Pastel o Barra en un Gráfico de Pastel de Pastel o de Barra de Pastel**
El siguiente código de ejemplo muestra cómo averiguar si los puntos de datos están en el segundo círculo o barra en un gráfico de Círculo de Círculos o Barra de Círculos.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-FindDataPointsInPieBar.py" >}}
## **Salida de la consola**
Por favor, consulta la siguiente salida por consola generada tras la ejecución del código de ejemplo anterior con el [archivo Excel de muestra](5115193.xlsx). Si [is_in_secondary_plot](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/is_in_secondary_plot/) es **falso**, el punto de datos está dentro de la Tarta o si es **verdadero**, entonces el punto de datos está dentro de la Barra.



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
{{< app/cells/assistant language="python-net" >}}
