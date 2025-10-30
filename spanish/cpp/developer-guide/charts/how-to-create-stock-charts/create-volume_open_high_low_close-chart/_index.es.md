---
title: Crear Gráfico de Acciones Volume Open High Low Close (VOHLC) con C++
description: Aprenda a crear un gráfico de acciones volume open high low close usando Aspose.Cells for C++. Nuestra guía demostrará cómo trazar datos del mercado de valores, incluyendo volumen, apertura, altos, bajos y precios de cierre, en un gráfico para un mejor análisis y visualización.
keywords: Aspose.Cells for C++, Gráfico de Acciones Volume Open High Low Close, Datos del Mercado de Valores, Análisis, Visualización.
type: docs
weight: 184
url: /es/cpp/create-volume-open-high-low-close-stock-chart/
---

## **Escenarios de uso posibles**
El cuarto gráfico de acciones que veremos es el gráfico de volumen apertura-alto-bajo-cierre. Es importante repetir que los datos deben estar en el orden correcto. Si necesita reorganizar su tabla de datos, háganlo antes de configurar su gráfico. Este gráfico incluye una columna para volumen justo después de la primera columna (categoría), y los gráficos incluyen un gráfico de columnas en el eje primario que muestra este volumen, mientras que los precios se mueven al eje secundario.

![todo:image_alt_text](data.png)

## **Gráfico de valores-apertura-altos-bajos-cierre (VOHLC) de acciones**

![todo:image_alt_text](sample.png)

## **Código de muestra**
El siguiente código de muestra carga el [archivo de Excel de muestra](Volume-Open-High-Low-Close.xlsx) y genera el [archivo de Excel de salida](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Volume-Open-High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close-Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockVolumeOpenHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend to be shown
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Volume-Open-High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:F9", true);

    // Set category data 
    chart.GetNSeries().GetCategoryData() = u"A2:A9";

    // Set Color for the first series (Volume) data 
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color{0xff, 79, 129, 189});

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
