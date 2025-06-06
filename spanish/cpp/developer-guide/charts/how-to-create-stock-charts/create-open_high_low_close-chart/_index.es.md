---
title: Crear Gráfico de Acciones Open High Low Close (OHLC) con C++
description: Aprenda a crear un gráfico de acciones open high low close usando Aspose.Cells for C++. Nuestra guía demostrará cómo trazar datos del mercado de valores, incluyendo los precios de apertura, altos, bajos y de cierre, en un gráfico para un mejor análisis y visualización.
keywords: Aspose.Cells for C++, Gráfico de Acciones Open High Low Close, Datos del Mercado de Valores, Análisis, Visualización.
type: docs
weight: 182
url: /es/cpp/create-open-high-low-close-stock-chart/
---

## **Escenarios de uso posibles**
El gráfico de cotizaciones apertura-alta-baja-cierre (OHLC) utiliza cinco columnas de datos, en orden: categoría, apertura, alta, baja y cierre. El rango de precios en cada categoría nuevamente se indica con una línea vertical, mientras que el rango entre la apertura y el cierre se muestra con una barra flotante más ancha; si el precio aumenta en la categoría (el cierre es mayor que la apertura), la barra se llena de un color, mientras que si el precio disminuye, la barra se llena de otro. Este tipo de gráfico a menudo se llama gráfico de velas.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)

## **Mejoras de visibilidad en el gráfico**
A menudo usamos colores en lugar de blanco y negro para indicar precios en aumento y en disminución. En el primer conjunto de velas abajo, el rojo muestra precios en aumento y el verde en disminución.

![todo:image_alt_text](sample2.png)

## **Código de muestra**
El siguiente código de muestra carga el [archivo de Excel de ejemplo](Open-High-Low-Close.xlsx) y genera el [archivo de Excel de salida](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Open-High-Low-Close.xlsx");
    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Create High-Low-Close-Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockOpenHighLowClose, 5, 6, 20, 12);
    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);
    // Set the legend can be showed
    chart.SetShowLegend(true);
    // Set the chart title name
    chart.GetTitle().SetText(u"Open-High-Low-Close Stock");
    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);
    // Set data range
    chart.SetChartDataRange(u"A1:E9", true);
    // Set category data
    chart.GetNSeries().GetCategoryData() = u"A2:A9";
    // Set the DownBars and UpBars with different color
    chart.GetNSeries().Get(0).GetDownBars().GetArea().SetForegroundColor(Color::Green());
    chart.GetNSeries().Get(0).GetUpBars().GetArea().SetForegroundColor(Color::Red());
    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);
    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
