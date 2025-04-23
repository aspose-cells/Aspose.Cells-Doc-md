---
title: Cómo crear un gráfico TreeMap con C++
description: Aprenda cómo crear un gráfico de mapa de árbol en Aspose.Cells for C++. Nuestra guía le ayudará a entender las diversas propiedades y opciones de formato disponibles para los gráficos de mapa de árbol, incluyendo colores, etiquetas y representación de datos.
keywords: Aspose.Cells for C++, gráfico de mapa de árbol, crear, propiedades, formato, colores, etiquetas, representación de datos, gráfico circular, gráficos jerárquicos.
type: docs
weight: 161
url: /es/cpp/creating-treemap-chart/
---

## **Escenarios de uso posibles**
Un gráfico Treemap proporciona una vista jerárquica de sus datos y facilita detectar patrones, como cuáles son los artículos más vendidos de una tienda. Las ramas del árbol están representadas por rectángulos y cada subrama se muestra como un rectángulo más pequeño. El gráfico Treemap muestra categorías por color y proximidad y puede mostrar fácilmente muchos datos que serían difíciles con otros tipos de gráficos.

![todo:image_alt_text](sample.png)
## **Gráfico TreeMap**
Después de ejecutar el código a continuación, verá el gráfico TreeMap como se muestra a continuación.

![todo:image_alt_text](result.png)
## **Código de muestra**
El siguiente código de muestra carga el [archivo de Excel de muestra](treemap.xlsx) y genera el [archivo de Excel de salida](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"treemap.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a Treemap chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::Treemap, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"TreeMap Chart");

    // Add series data range (D2:F13, actually)
    chart.GetNSeries().Add(u"D2:F13", true);

    // Set category data (A2:C13 is incorrect)
    chart.GetNSeries().SetCategoryData(u"A2:C13");

    // Show the DataLabels with category names
    chart.GetNSeries().Get(0).GetDataLabels().SetShowCategoryName(true);

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
