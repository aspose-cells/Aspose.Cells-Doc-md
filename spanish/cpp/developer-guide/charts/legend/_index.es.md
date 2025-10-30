---
title: Gestionar la leyenda de gráficos de Excel con C++
linktitle: Leyenda
description: Aprende cómo utilizar Aspose.Cells for C++ para aprovechar y personalizar eficazmente las leyendas en gráficos de Microsoft Excel. Nuestra guía completa explica la funcionalidad de la leyenda, cómo acceder y modificarla, así como cómo mejorar la visualización y comprensión de datos con las leyendas.
keywords: Aspose.Cells for C++, Leyendas de gráficos, Microsoft Excel, Visualización, Comprensión de datos.
type: docs
weight: 50
url: /es/cpp/chart-legend/
---

## **Opciones de Leyenda**
Aspose.Cells también permite gestionar la leyenda de un gráfico en tiempo de ejecución. Con el objeto [Legend](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legend/), la leyenda puede ser movida, actualizada y formateada.

|![todo:image_alt_text](chart_legend.png)|

## **Establecimiento de la Leyenda del Gráfico**
Es fácil gestionar la leyenda de un gráfico con Aspose.Cells [Legend](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legend/).

El siguiente fragmento de código muestra cómo gestionar la leyenda:

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
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

    // Setting the title of a chart
    chart.GetTitle().SetText(u"Title");

    // Setting the font color of the chart title to blue
    chart.GetTitle().GetFont().SetColor(Color::Blue());

    // Move the legend to left
    chart.GetLegend().SetPosition(LegendPositionType::Left);

    // Set font color of the legend
    chart.GetLegend().GetFont().SetColor(Color::Blue());

    // Save the file
    workbook.Save(u"chart_legend.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Temas avanzados**
- [Establecer el texto de relleno de entrada de leyenda del gráfico a ninguno usando Aspose.Cells](/cells/es/cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)
{{< app/cells/assistant language="cpp" >}}
