---
title: Colores Personalizados de Segmento o Sector en Gráfico Circular
type: docs
weight: 30
url: /es/java/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

Este artículo explica cómo agregar colores personalizados a las sectores de un gráfico circular. Por defecto, los gráficos circulares utilizan la plantilla predeterminada de Microsoft Excel. Para usar otros colores, es posible redefinir los colores en el gráfico.

{{% /alert %}}

Para establecer el color personalizado para las sectores individuales de un gráfico circular:

1. Acceda al [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) del objeto.
1. Asignar un color de tu elección utilizando el método [**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor).

Este artículo también explica cómo configurar:

- Datos de categoría de un gráfico.
- Un título de gráfico vinculado a una celda.
- Configuraciones de fuente del título del gráfico.
- La posición de la leyenda.

{{% alert color="primary" %}}

El [**ChartPoint.getArea().setForegroundColor()**](https://reference.aspose.com/cells/java/com.aspose.cells/area#ForegroundColor) no es específico para gráficos circulares, pero se puede usar para todo tipo de gráficos.

{{% /alert %}}

**Colores personalizados de las sectores en el gráfico circular**

![todo:image_alt_text](custom-slice-or-sector-colors-in-pie-chart_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSliceOrSectorColorsPieChart-CustomSliceOrSectorColorsPieChart.java" >}}
{{< app/cells/assistant language="java" >}}
