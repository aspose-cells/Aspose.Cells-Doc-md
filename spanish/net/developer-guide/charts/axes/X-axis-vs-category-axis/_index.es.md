---
title: Eje X Vs. Eje de Categoría
description: Aprenda a diferenciar entre el eje X y el eje de categoría en Aspose.Cells for .NET. Nuestra guía le ayudará a entender las diferencias en su uso y propiedades, y cómo configurarlos según sus necesidades.
keywords: Aspose.Cells for .NET, eje X, eje de categoría, diferencia, uso, propiedades, configuración.
type: docs
weight: 180
url: /es/net/X-axis-vs-category-axis/
---

## **Escenarios de uso posibles**
Existen diferentes tipos de ejes X. Mientras que el eje Y es un eje de tipo Valor, el eje X puede ser un eje de tipo Categoría o un eje de tipo Valor. Utilizando un eje de Valor, los datos se tratan como datos numéricos continuamente variables, y el marcador se coloca en un punto a lo largo del eje que varía según su valor numérico. Utilizando un eje de Categoría, los datos se tratan como una secuencia de etiquetas de texto no numéricas, y el marcador se coloca en un punto a lo largo del eje según su posición en la secuencia. El ejemplo a continuación ilustra la diferencia entre los Ejes de Valor y de Categoría.
Nuestros datos de muestra se muestran en el [archivo de tabla de muestra](sample.png) a continuación. La primera columna contiene nuestros datos del eje X, que pueden tratarse como Categorías o como Valores. Tenga en cuenta que los números no están igualmente espaciados, ni tampoco aparecen en orden numérico.

![todo:image_alt_text](sample.png)
## **Maneje el eje X y el eje de categoría como Microsoft Excel**
Mostraremos estos datos en dos tipos de gráficos, el primer gráfico es un gráfico XY (dispersión) con el eje X como eje de Valor, y el segundo gráfico es un gráfico de líneas con el eje X como eje de Categoría.

![todo:image_alt_text](compare.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "X-axis-vs-category-axis.cs" >}}
{{< app/cells/assistant language="csharp" >}}
