--- 
title: Crear Gráfico de Acciones High Low Close (HLC) con C++ 
linktitle: Crear Gráfico de Cotizaciones Altas Bajas Cierre (HLC) 
description: Aprenda a crear un gráfico de acciones high low close usando Aspose.Cells for C++. Nuestra guía paso a paso demostrará cómo trazar datos del mercado de valores, incluyendo los precios altos, bajos y de cierre, en un gráfico para un mejor análisis y visualización. 
keywords: Aspose.Cells for C++, Gráfico de Acciones High Low Close, Datos del Mercado de Valores, Análisis, Visualización. 
type: docs 
weight: 181 
url: /es/cpp/create-high-low-close-stock-chart/ 
--- 

## **Escenarios de uso posibles** 
El gráfico de cotizaciones altas-bajas-cierre (HLC) utiliza cuatro columnas de datos. La primera columna es una categoría, usualmente una fecha pero también se pueden usar nombres de acciones. Las siguientes tres columnas en orden son para los precios altos, bajos y de cierre. El rango de precio para cada categoría se indica mediante una línea vertical de bajo a alto, y el precio de cierre se muestra usando una marca extendiéndose hacia la derecha de esta línea. 

![todo:image_alt_text](sample.png) 
## **Mejoras de visibilidad en el gráfico** 
A veces, para que el gráfico luzca más intuitivo, podemos modificar la apariencia del marcador (cierre), o hacer que se muestre en el eje secundario. 

![todo:image_alt_text](sample2.png) 
## **Código de muestra** 
El siguiente código de ejemplo carga el [archivo de Excel de muestra](High-Low-Close.xlsx) y genera el [archivo de Excel de salida](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close-Stock Chart
    int pieIdx = worksheet.GetCharts().Add(ChartType::StockHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:D9", true);

    // Set category data 
    chart.GetNSeries().GetCategoryData() = u"A2:A9";

    // Set the marker with the built-in data 
    chart.GetNSeries().Get(2).GetMarker().SetMarkerStyle(ChartMarkerType::Dash);
    chart.GetNSeries().Get(2).GetMarker().SetMarkerSize(20);
    chart.GetNSeries().Get(2).GetMarker().GetArea().SetFormatting(FormattingType::Custom);
    chart.GetNSeries().Get(2).GetMarker().GetArea().SetForegroundColor(Color::Maroon());

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
``` 
{{< app/cells/assistant language="cpp" >}}
