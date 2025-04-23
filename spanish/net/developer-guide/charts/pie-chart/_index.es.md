---
title: Creación de un gráfico circular con líneas guía
description: Aprende a usar Aspose.Cells for .NET para crear un gráfico circular con líneas guía en Microsoft Excel. Nuestra guía demostrará cómo agregar líneas guía que conecten los puntos de datos con la leyenda y mejoren la claridad general de tu gráfico.
keywords: Aspose.Cells for .NET, Gráfico circular, Líneas guía, Microsoft Excel, Visualización de datos, Personalización de gráficos.
linktitle: Gráfico circular
type: docs
weight: 45
url: /es/net/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

Este artículo explica cómo crear un gráfico circular con líneas guía desde cero mientras se utiliza la API Aspose.Cells for .NET. En Excel, la opción 'Mostrar líneas guía' se establece de forma predeterminada, por lo que cuando creas un gráfico circular en Excel las líneas guía se muestran. Sin embargo, al crear un gráfico similar con las API de Aspose.Cells, debes establecer explícitamente la propiedad [**Series.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines).

{{% /alert %}}

Para demostrar el uso de la API Aspose.Cells for .NET para crear un gráfico circular con líneas guía, primero crearemos un [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) y agregaremos algunos datos que servirán como origen de datos de la serie. Una vez que los datos estén en su lugar, agregaremos un [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) de tipo [**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) a la colección de gráficos y configuraremos sus diferentes aspectos para obtener la vista de gráfico deseada.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

Hasta el momento hemos creado un gráfico circular y configurado sus diferentes aspectos. Ahora vamos a activar las líneas guía para el gráfico. Ten en cuenta que para mostrar las líneas guía, debemos mover un poco las etiquetas de datos.

El siguiente fragmento de código activa las líneas guía, actualiza el gráfico y luego calcula las posiciones de las etiquetas de datos para moverlas en consecuencia.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

Finalmente, el siguiente código guarda el gráfico en formato de imagen y el libro de trabajo en formato XLSX.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**Gráfico de Pastel Resultante**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **Temas avanzados**
- [Personalizar Colores de Sector en Gráfico de Pastel](/cells/es/net/custom-slice-or-sector-colors-in-pie-chart/)
- [Encontrar si los Puntos de Datos están en el Segundo Pastel o Barra en un Gráfico de Pastel de Pastel o de Barra de Pastel](/cells/es/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## Artículos relacionados

- [Creando gráficos](/cells/es/net/creating-charts/)
- [Personalizando Gráficos](/cells/es/net/customizing-charts/)
- [Formato de Datos en Gráficos](/cells/es/net/data-formatting-in-charts/)
- [Configurar la apariencia del gráfico](/cells/es/net/setting-chart-appearance/)

{{< app/cells/assistant language="csharp" >}}
