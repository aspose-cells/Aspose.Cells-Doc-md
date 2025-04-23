---
title: Gestionar los ejes de gráficos de Excel con C++
description: Aprenda cómo configurar los ejes del gráfico en Aspose.Cells for C++. Nuestra guía le mostrará cómo ajustar los ejes primarios y secundarios, establecer sus rangos y modificar sus propiedades para mejorar sus gráficos.
keywords: Aspose.Cells for C++, ejes del gráfico, configuración, ejes primarios, ejes secundarios, rango, propiedades.
linktitle: Ejes
type: docs
weight: 50
url: /es/cpp/chart-axes/
---

{{% alert color="primary" %}}

En los gráficos de Excel, hay 3 tipos de ejes:
1. Eje Horizontal (Categoría): Eje X
1. Eje Vertical (Valor): Eje Y
1. Eje de Profundidad (Serie): Eje Z

{{% /alert %}}

## **Opciones del Eje**
Aspose.Cells también permite gestionar los ejes del gráfico en tiempo de ejecución. Con el objeto [Axis](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/) puedes cambiar todas las opciones del eje, como en Excel.

|![todo:image_alt_text](chart_axes.png)|

## **Administrar Ejes X e Y**

En los gráficos de Excel, los ejes horizontal y vertical son los dos ejes más populares para usar.

El siguiente fragmento de código demuestra cómo establecer las opciones de los ejes X e Y.

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
    worksheet.GetCells().Get(u"A1").PutValue(u"Series1");
    worksheet.GetCells().Get(u"A2").PutValue(50);
    worksheet.GetCells().Get(u"A3").PutValue(100);
    worksheet.GetCells().Get(u"A4").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(u"Series2");
    worksheet.GetCells().Get(u"B2").PutValue(60);
    worksheet.GetCells().Get(u"B3").PutValue(32);
    worksheet.GetCells().Get(u"B4").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.SetChartDataRange(u"A1:B4", true);

    // Hiding X axis
    chart.GetCategoryAxis().SetIsVisible(false);

    // Setting max value of Y axis
    chart.GetValueAxis().SetMaxValue(200);

    // Setting major unit
    chart.GetValueAxis().SetMajorUnit(50);

    // Save the file
    workbook.Save(u"chart_axes.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Temas Avanzados**
- [Cambiar la dirección de la etiqueta del eje](/cells/es/cpp/change-tick-label-direction/)
- [Determinar qué Eje existe en el Gráfico](/cells/es/cpp/determine-which-axis-exists-in-the-chart/)
- [Manejar Unidades Automáticas del Eje del Gráfico como Microsoft Excel](/cells/es/cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)
- [Leer etiquetas del eje después de calcular el gráfico](/cells/es/cpp/read-axis-labels-after-calculating-the-chart/)
- [Cómo establecer el Eje de Categoría en el Gráfico de Excel](/cells/es/cpp/how-to-set-category-axis/)
