---
title: Deshabilitar ajuste de texto para etiquetas de datos del gráfico
type: docs
weight: 60
url: /es/java/disable-text-wrapping-for-data-labels-of-the-chart/
---
{{% alert color="primary" %}}

Microsoft Excel 2013 permite a los usuarios envolver o desenvolver texto dentro de las etiquetas de datos de un gráfico. De forma predeterminada, el texto de la etiqueta de datos está ajustado.

{{% /alert %}}

Aspose.Cells proporciona el[**Etiquetas de datos.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped) método. Ajustado a**Verdadero** o**Falso** para habilitar o deshabilitar el ajuste de texto en las etiquetas de datos, respectivamente.

 Del mismo modo, utilice el[**Etiquetas de datos.isTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)método para averiguar si una etiqueta de datos ya está envuelta.

Esta captura de pantalla muestra un archivo Excel Microsoft de muestra que contiene un gráfico en el que se envuelve el texto de las etiquetas de datos. Como puede ver, puede marcar o borrar la**Envolver texto en forma** opción en la sección ALINEACIÓN del panel Formatear etiquetas de datos en Microsoft Excel 2013.

**Envolviendo etiquetas de datos**

![todo:imagen_alternativa_texto](disable-text-wrapping-for-data-labels-of-the-chart_1.png)

 El código de muestra que sigue carga el archivo de Excel de muestra Microsoft usando Aspose.Cells y deshabilita el ajuste de texto de la etiqueta de datos usando el[**Etiquetas de datos.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)método. Cuando se ejecuta el código, el gráfico se ve así. El texto previamente envuelto ahora está desenvuelto.

**Mostrar etiquetas de datos en una sola línea**

![todo:imagen_alternativa_texto](disable-text-wrapping-for-data-labels-of-the-chart_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableTextWrapping-DisableTextWrapping.java" >}}
