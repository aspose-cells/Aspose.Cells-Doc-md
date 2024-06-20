---
title: Obtener el texto de ecuación de la tendencia del gráfico
linktitle: Línea de tendencia
type: docs
weight: 90
url: /es/java/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Puede recuperar el Texto de la Ecuación de la Línea de Tendencia del Gráfico utilizando Aspose.Cells. Aspose.Cells proporciona la propiedad [**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text) que devuelve el Texto de la Ecuación de la línea de tendencia del gráfico. Para hacer uso de esta propiedad, primero deberá llamar al método [**Chart.calculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate--).

{{% /alert %}}

## **Ejemplo**

La siguiente captura de pantalla muestra el gráfico con una línea de tendencia y su Texto de la Ecuación se muestra en color rojo. Recuperaremos este texto usando la propiedad [**Trendline.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text) en el siguiente código de ejemplo.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

### Código en Java para obtener el texto de la ecuación de la línea de tendencia del gráfico

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetEquationText-GetEquationText.java" >}}

### Salida generada por el código de ejemplo

Este es el resultado de consola del código de ejemplo anterior.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
