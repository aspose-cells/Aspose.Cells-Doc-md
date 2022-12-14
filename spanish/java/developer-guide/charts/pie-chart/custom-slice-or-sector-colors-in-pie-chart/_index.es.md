---
title: Colores personalizados de sectores o sectores en gráficos circulares
type: docs
weight: 30
url: /es/java/custom-slice-or-sector-colors-in-pie-chart/
---
{{% alert color="primary" %}}

Este artículo explica cómo agregar colores personalizados a las porciones/sectores de gráficos circulares. De forma predeterminada, los gráficos circulares utilizan la plantilla predeterminada de Excel Microsoft. Para utilizar otros colores, es posible redefinir los colores en el gráfico.

{{% /alert %}}

Para establecer el color personalizado para las porciones o sectores individuales de un gráfico circular:

1.  Acceder al[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) objetos[**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint).
1.  Asigne un color de su elección usando el[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor)método.

Este artículo también explica cómo configurar:

- Los datos de categoría de un gráfico.
- Un título de gráfico vinculado a una celda.
- La configuración de la fuente del título del gráfico.
- La posición de la leyenda.

{{% alert color="primary" %}}

[**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor) no es específico de los gráficos circulares, pero se puede utilizar para todos los tipos de gráficos.

{{% /alert %}}

**Colores de sector personalizados en el gráfico circular**

![todo:imagen_alternativa_texto](custom-slice-or-sector-colors-in-pie-chart_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSliceOrSectorColorsPieChart-CustomSliceOrSectorColorsPieChart.java" >}}
