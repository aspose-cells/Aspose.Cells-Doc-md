---
title: Obtener el texto de ecuación de la tendencia del gráfico
description: Aprenda a utilizar Aspose.Cells for .NET para recuperar el texto de la ecuación de una línea de tendencia en un gráfico creado en Microsoft Excel. Nuestra guía demostrará cómo acceder y extraer la ecuación de una línea de tendencia para un análisis adicional o visualización.
keywords: Aspose.Cells for .NET, Línea de tendencia del gráfico, Texto de la ecuación, Microsoft Excel, Análisis de datos, Visualización.
linktitle: Líneas de tendencia
type: docs
weight: 110
url: /es/net/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Puede recuperar el Texto de la Ecuación de la Línea de Tendencia del Gráfico utilizando Aspose.Cells. Aspose.Cells proporciona la propiedad [**Trendline.DataLabels.Text**](https://reference.aspose.com/cells/net/aspose.cells.charts/datalabels/properties/text) que devuelve el Texto de la Ecuación de la línea de tendencia del gráfico. Para hacer uso de esta propiedad, primero deberá llamar al método [**Chart.Calculate()**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/calculate).

{{% /alert %}}

La siguiente captura de pantalla muestra el gráfico con una línea de tendencia y su Texto de la Ecuación se muestra en color rojo. Recuperaremos este texto usando la propiedad [**Trendline.DataLabels.Text**](https://reference.aspose.com/cells/net/aspose.cells.charts/datalabels/properties/text) en el siguiente código de ejemplo.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

Código de C# para obtener el texto de la ecuación de la línea de tendencia del gráfico

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GetEquationTextOfChartTrendLine-1.cs" >}}

Resultado generado por el código de ejemplo

Este es el resultado de consola del código de ejemplo anterior.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
