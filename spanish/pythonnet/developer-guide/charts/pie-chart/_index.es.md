---
title: Creación de un gráfico circular con líneas guía
description: Aprende cómo usar Aspose.Cells para Python via .NET para crear un gráfico de pastel con líneas guía en Microsoft Excel. Nuestra guía demostrará cómo agregar líneas guía que conectan puntos de datos con la leyenda y mejoran la claridad general de tu gráfico.
keywords: Aspose.Cells para Python via .NET, Gráfico de pastel, Líneas guía, Microsoft Excel, Visualización de datos, Personalización de gráficos.
linktitle: Gráfico circular
type: docs
weight: 45
url: /es/python-net/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

Este artículo explica cómo crear un gráfico de pastel con líneas guía desde cero utilizando la API Aspose.Cells para Python via .NET. En Excel, la opción 'Mostrar líneas guía' está configurada por defecto, así que al crear un gráfico de pastel en Excel las líneas guía se muestran. Sin embargo, al crear un gráfico similar con las API de Aspose.Cells para Python via .NET, debes configurar explícitamente la propiedad [**Series.has_leader_lines**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/has_leader_lines).

{{% /alert %}}

Para demostrar el uso de la API Aspose.Cells para Python via .NET para crear un gráfico de pastel con líneas guía, primero crearemos un [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) nuevo y agregaremos algunos datos que servirán como fuente de datos de la serie. Una vez que los datos están en su lugar, agregaremos un [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) de tipo [**ChartType.PIE**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype/) a la colección de gráficos y configuraremos sus diferentes aspectos para obtener la vista deseada del gráfico.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateWorkbook.py" >}}

Hasta el momento hemos creado un gráfico circular y configurado sus diferentes aspectos. Ahora vamos a activar las líneas guía para el gráfico. Ten en cuenta que para mostrar las líneas guía, debemos mover un poco las etiquetas de datos.

El siguiente fragmento de código activa las líneas guía, actualiza el gráfico y luego calcula las posiciones de las etiquetas de datos para moverlas en consecuencia.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-TurnOnLeaderLines.py" >}}

Finalmente, el siguiente código guarda el gráfico en formato de imagen y el libro de trabajo en formato XLSX.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SaveChartInImageAndWorkbookInXLSX.py" >}}

|**Gráfico de Pastel Resultante**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **Temas avanzados**
- [Personalizar Colores de Sector en Gráfico de Pastel](/cells/es/python-net/custom-slice-or-sector-colors-in-pie-chart/)
- [Encontrar si los Puntos de Datos están en el Segundo Pastel o Barra en un Gráfico de Pastel de Pastel o de Barra de Pastel](/cells/es/python-net/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## Artículos relacionados

- [Creando gráficos](/cells/es/python-net/creating-charts/)
- [Personalizando Gráficos](/cells/es/python-net/customizing-charts/)
- [Formato de Datos en Gráficos](/cells/es/python-net/data-formatting-in-charts/)
- [Configurar la apariencia del gráfico](/cells/es/python-net/setting-chart-appearance/)

