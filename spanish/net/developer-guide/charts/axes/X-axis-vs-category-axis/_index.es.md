---
title: Eje X vs. Eje de categorías
description: Aprenda a diferenciar entre el eje X y el eje de Categoría en Aspose.Cells for .NET. Nuestra guía lo ayudará a comprender las diferencias en su uso y propiedades, y cómo configurarlos según sus necesidades.
keywords: Aspose.Cells for .NET, X axis, Category axis, difference, usage, properties, configuration.
type: docs
weight: 180
url: /es/net/X-axis-vs-category-axis/
---
##  **Posibles escenarios de uso**
Hay diferentes tipos de ejes X. Mientras que el eje Y es un eje de tipo Valor, el eje X puede ser un eje de tipo Categoría o un eje de tipo Valor. Al utilizar un eje de valor, los datos se tratan como datos numéricos que varían continuamente y el marcador se coloca en un punto a lo largo del eje que varía según su valor numérico. Al utilizar un eje de categoría, los datos se tratan como una secuencia de etiquetas de texto no numéricas y el marcador se coloca en un punto a lo largo del eje según su posición en la secuencia. El siguiente ejemplo ilustra la diferencia entre los ejes de valor y categoría.
 Nuestros datos de muestra se muestran en la[archivo de tabla de muestra](sample.png) abajo. La primera columna contiene nuestros datos del eje X, que pueden tratarse como Categorías o Valores. Tenga en cuenta que los números no están espaciados equidistantemente ni siquiera aparecen en orden numérico.

![todo:image_alt_text](sample.png)
##  **Manejar el eje X y Categoría como Microsoft Excel**
Mostraremos estos datos en dos tipos de gráficos: el primer gráfico es el gráfico X XY (dispersión) como eje de valor, el segundo gráfico es el gráfico de líneas X como eje de categoría.

![todo:image_alt_text](compare.png)
##  **Código de muestra**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "X-axis-vs-category-axis.cs" >}}
