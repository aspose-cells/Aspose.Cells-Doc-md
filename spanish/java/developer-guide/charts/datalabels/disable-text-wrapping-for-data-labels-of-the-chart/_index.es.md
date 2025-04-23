---
title: Desactivar el ajuste de texto para las etiquetas de datos del gráfico
type: docs
weight: 60
url: /es/java/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013 permite a los usuarios ajustar o desajustar el texto dentro de las etiquetas de datos de un gráfico. De forma predeterminada, el texto de la etiqueta de datos está ajustado.

{{% /alert %}}

Aspose.Cells proporciona el método [**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped). Establezca a **True** o **False** para habilitar o deshabilitar el ajuste de texto en las etiquetas de datos respectivamente.

Del mismo modo, utilice el método [**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped) para averiguar si una etiqueta de datos ya está ajustada.

Esta captura de pantalla muestra un archivo de muestra de Microsoft Excel que contiene un gráfico en el que el texto de las etiquetas de datos está ajustado. Como se puede ver, puede marcar o desmarcar la opción **Ajustar texto dentro de la forma** en la sección de ALINEACIÓN del panel Formato de etiquetas de datos en Microsoft Excel 2013.

**Ajuste de etiquetas de datos**

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_1.png)

El código de ejemplo que sigue carga el archivo de muestra de Microsoft Excel utilizando Aspose.Cells y desactiva el ajuste de texto de las etiquetas de datos utilizando el método [**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped). Cuando el código se ejecuta, el aspecto del gráfico es el siguiente. El texto previamente ajustado ahora está desajustado.

**Mostrar etiquetas de datos en una sola línea solamente**

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableTextWrapping-DisableTextWrapping.java" >}}
{{< app/cells/assistant language="java" >}}
