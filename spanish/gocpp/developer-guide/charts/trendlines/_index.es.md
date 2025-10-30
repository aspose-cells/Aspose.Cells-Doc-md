---
title: Obtener el texto de la ecuación de la línea de tendencia del gráfico con Golang vía C++
linktitle: Líneas de tendencia
description: Aprenda cómo usar Aspose.Cells for C++ para recuperar el texto de la ecuación de una línea de tendencia en un gráfico creado en Microsoft Excel. Nuestra guía demostrará cómo acceder y extraer la ecuación de una línea de tendencia para análisis o visualización posterior.
keywords: Aspose.Cells for C++, Línea de tendencia del gráfico, Texto de ecuación, Microsoft Excel, Análisis de datos, Visualización.
type: docs
weight: 110
url: /es/go-cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Puede recuperar el Texto de la Ecuación de la Línea de Tendencia del Gráfico utilizando Aspose.Cells. Aspose.Cells proporciona la propiedad [**Trendline.GetText()**](https://reference.aspose.com/cells/go-cpp/datalabels/gettext/) que devuelve el Texto de la Ecuación de la línea de tendencia del gráfico. Para hacer uso de esta propiedad, primero deberá llamar al método [**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/).

{{% /alert %}}

La siguiente captura muestra el gráfico con una línea de tendencia y su texto de ecuación en color rojo. Nosotros recuperaremos este texto usando la propiedad [**Trendline.GetText()**](https://reference.aspose.com/cells/go-cpp/datalabels/gettext/) en el siguiente ejemplo de código.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## Código C++ para obtener el texto de la ecuación de la línea de tendencia del gráfico

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Trendlines.go" >}}
Resultado generado por el código de ejemplo

Este es el resultado de consola del código de ejemplo anterior.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
