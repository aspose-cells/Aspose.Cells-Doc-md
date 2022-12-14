---
title: Creación de un gráfico circular con líneas guía
linktitle: Gráfico circular
type: docs
weight: 45
url: /es/net/creating-pie-chart-with-leader-lines/
---
{{% alert color="primary" %}}

 Este artículo explica cómo crear un gráfico circular con líneas guía desde cero usando Aspose.Cells for .NET API. En Excel, la opción 'Mostrar líneas guía' está configurada de manera predeterminada, por lo que cuando crea un gráfico circular en Excel, se muestran las líneas guía. Sin embargo, al crear un gráfico similar con las API Aspose.Cells, debe configurar explícitamente el[**Series.HasLeaderLines**](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/hasleaderlines) propiedad.

{{% /alert %}}

Para demostrar el uso de Aspose.Cells for .NET API para crear un gráfico circular con líneas guía, primero crearemos un nuevo[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) e ingrese algunos datos que servirán como fuente de datos de la serie. Una vez que los datos estén en su lugar, agregaremos un[**Cuadro**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) de tipo[**ChartType.Pie**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)a la colección de gráficos y establezca sus diferentes aspectos para obtener la vista de gráfico deseada.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-CreateWorkbook.cs" >}}

Hasta ahora hemos creado un gráfico circular y establecido sus diferentes aspectos. Ahora vamos a activar las líneas guía del gráfico. Tenga en cuenta que, para mostrar las líneas guía, tenemos que mover un poco las etiquetas de datos.

El siguiente fragmento de código activa las líneas guía, actualiza el gráfico y luego calcula las posiciones de las etiquetas de datos para moverlas en consecuencia.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-TurnOnLeaderLines.cs" >}}

Finalmente, el siguiente código guarda el gráfico en formato de imagen y el libro de trabajo en formato XLSX.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CreatePieChartWithLeaderLines-SaveChartInImageAndWorkbookInXLSX.cs" >}}

|**Gráfico circular resultante**|
|:- |
|![todo:imagen_alternativa_texto](creating-pie-chart-with-leader-lines_1.png)|

## **Temas avanzados**
- [Colores personalizados de sectores o sectores en gráficos circulares](/cells/es/net/custom-slice-or-sector-colors-in-pie-chart/)
- [Averigüe si los puntos de datos están en el segundo pastel o barra en un gráfico circular de pastel o de barra de pastel](/cells/es/net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## Artículos relacionados

- [Creación de gráficos](/cells/es/net/creating-charts/)
- [Gráficos personalizados](/cells/es/net/customizing-charts/)
- [Formato de datos en gráficos](/cells/es/net/data-formatting-in-charts/)
- [Configuración de la apariencia del gráfico](/cells/es/net/setting-chart-appearance/)

