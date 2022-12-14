---
title: Obtener el texto de la ecuación de la línea de tendencia del gráfico
linktitle: línea de tendencia
type: docs
weight: 90
url: /es/java/get-equation-text-of-chart-trendline/
---
{{% alert color="primary" %}}

 Puede recuperar el texto de la ecuación de la línea de tendencia del gráfico usando Aspose.Cells. Aspose.Cells proporciona[**Línea de tendencia.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text) propiedad que devuelve el texto de la ecuación de la línea de tendencia del gráfico. Para hacer uso de esta propiedad, primero tendrá que llamar[**Gráfico.calcular()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#calculate()) método.

{{% /alert %}}

## **Ejemplo**

 La siguiente captura de pantalla muestra el gráfico con una línea de tendencia y su texto de ecuación se muestra en color rojo. Recuperaremos este texto usando el[**Línea de tendencia.getDataLabels().getText()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#Text)propiedad en el siguiente código de ejemplo.

![todo:imagen_alternativa_texto](get-equation-text-of-chart-trendline_1.png)

### Java código para obtener el texto de la ecuación de la línea de tendencia del gráfico

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetEquationText-GetEquationText.java" >}}

### Salida generada por el código de muestra

Esta es la salida de la consola del código de ejemplo anterior.

{{< highlight "java" >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
