---
title: Gestionar DataLabels de gráficos de Excel con C++
linktitle: Etiquetas de datos
type: docs
weight: 50
url: /es/cpp/insert-datalabels-to-chart/
description: Aprende a gestionar eficazmente las etiquetas de datos en gráficos de Excel usando Aspose.Cells for C++. Nuestra guía completa cubre varias tareas de gestión, incluyendo agregar, eliminar y modificar etiquetas para mejorar la legibilidad y usabilidad del gráfico.
keywords: Aspose.Cells for C++, gráficos de Excel, etiquetas de datos, gestión, legibilidad, usabilidad, agregar, eliminar, modificar.
---

{{% alert color="primary" %}}

Las etiquetas de datos son una parte importante de un gráfico. Podemos saber fácilmente el valor, porcentaje, etc., de cada serie.

{{% /alert %}}

## **Opciones de etiquetas de datos**
Aspose.Cells también permite gestionar las etiquetas de datos del gráfico en tiempo de ejecución con el objeto [DataLabels](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/). Es sencillo mover, actualizar y formatear las etiquetas de datos del gráfico.

|![todo:image_alt_text](chart_datalabels.png)|

## **Administrar las etiquetas de datos del gráfico**
Es sencillo gestionar las etiquetas de datos del gráfico con Aspose.Cells [DataLabels](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/).

El siguiente fragmento de código demuestra cómo gestionar DataLabels.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(60);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Show value labels
    chart.GetNSeries().Get(0).GetDataLabels().SetShowValue(true);

    // Show series name labels
    chart.GetNSeries().Get(1).GetDataLabels().SetShowSeriesName(true);

    // Move labels to center
    chart.GetNSeries().Get(1).GetDataLabels().SetPosition(LabelPositionType::Center);

    // Save the file
    workbook.Save(u"chart_datalabels.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Temas Avanzados**
- [Agregar etiquetas personalizadas a los puntos de datos en la serie del gráfico](/cells/es/cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)
- [Deshabilitar el ajuste de texto para las etiquetas de datos del gráfico](/cells/es/cpp/disable-text-wrapping-for-data-labels-of-the-chart/)
- [Redimensionar la forma de la etiqueta de datos del gráfico para que se ajuste al texto](/cells/es/cpp/resize-chart-s-data-label-shape-to-fit-text/)
- [Etiqueta de datos personalizada de texto enriquecido del punto del gráfico](/cells/es/cpp/rich-text-custom-data-label-of-chart-point/)
- [Establecer el tipo de forma de las etiquetas de datos del gráfico](/cells/es/cpp/set-the-shape-type-of-data-labels-of-chart/)
- [Mostrar el rango de celdas como las etiquetas de datos](/cells/es/cpp/showing-cell-range-as-the-data-labels/)
{{< app/cells/assistant language="cpp" >}}
