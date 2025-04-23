---
title: Obtener el texto de ecuación de la tendencia del gráfico
description: Aprende cómo usar Aspose.Cells para Python via .NET para recuperar el texto de la ecuación de una línea de tendencia en un gráfico creado en Microsoft Excel. Nuestra guía demostrará cómo acceder y extraer la ecuación de una línea de tendencia para análisis o exhibición posterior.
keywords: Aspose.Cells para Python via .NET, línea de tendencia del gráfico, texto de la ecuación, Microsoft Excel, análisis de datos, exhibición.
linktitle: Líneas de tendencia
type: docs
weight: 110
url: /es/python-net/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Puedes recuperar el texto de la ecuación de la línea de tendencia del gráfico usando Aspose.Cells para Python via .NET. Aspose.Cells para Python via .NET proporciona una propiedad que devuelve el texto de la ecuación de la línea de tendencia del gráfico. Para usar esta propiedad, primero debes llamar al método [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate).

{{% /alert %}}

La siguiente captura de pantalla muestra el gráfico con una línea de tendencia y su Texto de la Ecuación se muestra en color rojo. Recuperaremos este texto usando la propiedad [**Trendline.data_labels.text**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/datalabels/text) en el siguiente código de ejemplo.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

Código de C# para obtener el texto de la ecuación de la línea de tendencia del gráfico

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-GetEquationTextOfChartTrendLine-1.py" >}}

Resultado generado por el código de ejemplo

Este es el resultado de consola del código de ejemplo anterior.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
