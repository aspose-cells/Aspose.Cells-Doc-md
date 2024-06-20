---
title: Creación de un gráfico circular con líneas guía
linktitle: Gráfico circular
type: docs
weight: 170
url: /es/java/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

Este artículo explica cómo crear un gráfico de sectores con líneas líderes desde cero utilizando la API Aspose.Cells for Java. En Excel, la opción 'Mostrar líneas líderes' está establecida por defecto, por lo que al crear un gráfico de sectores en Excel las líneas líderes se muestran. Sin embargo, al crear un gráfico similar con las APIs de Aspose.Cells, debes establecer explícitamente la propiedad [**Series.HasLeaderLines**](https://reference.aspose.com/cells/java/com.aspose.cells/series#HasLeaderLines).

{{% /alert %}}

## **Crear gráficos circulares con líneas de líder**

Para demostrar el uso del API Aspose.Cells for Java para crear un gráfico circular con líneas de líder, primero crearemos un nuevo [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) e ingresaremos algunos datos que servirán como origen de datos de la serie. Una vez que los datos estén en su lugar, agregaremos un [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) de tipo [**Pie**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PIE) a la colección de gráficos y configuraremos sus diferentes aspectos para obtener la vista de gráfico deseada.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePieChartWithLeaderLines-CreatePieChartWithLeaderLines.java" >}}

**Gráfico Circular Resultante**

![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)

## Artículos relacionados

- [Creación y personalización de gráficos](/cells/es/java/creating-and-customizing-charts/)
- [Formato de gráficos](/cells/es/java/chart-formatting/)
