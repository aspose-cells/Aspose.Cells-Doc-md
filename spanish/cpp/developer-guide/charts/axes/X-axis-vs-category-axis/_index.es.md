---
title: Eje X vs. Eje de Categoría con C++
linktitle: Eje X Vs. Eje de Categoría
description: Aprende cómo diferenciar entre el eje X y el eje de categoría en Aspose.Cells for C++. Nuestra guía te ayudará a entender las diferencias en su uso y propiedades, y cómo configurarlos según tus necesidades.
keywords: Aspose.Cells for C++, eje X, eje de categoría, diferencia, uso, propiedades, configuración.
type: docs
weight: 180
url: /es/cpp/X-axis-vs-category-axis/
---

## **Escenarios de uso posibles**
Existen diferentes tipos de ejes X. Mientras que el eje Y es un eje de tipo Valor, el eje X puede ser un eje de tipo Categoría o un eje de tipo Valor. Utilizando un eje de Valor, los datos se tratan como datos numéricos continuamente variables, y el marcador se coloca en un punto a lo largo del eje que varía según su valor numérico. Utilizando un eje de Categoría, los datos se tratan como una secuencia de etiquetas de texto no numéricas, y el marcador se coloca en un punto a lo largo del eje según su posición en la secuencia. El ejemplo a continuación ilustra la diferencia entre los Ejes de Valor y de Categoría.
Nuestros datos de muestra se muestran en el [archivo de tabla de muestra](sample.png) a continuación. La primera columna contiene nuestros datos del eje X, que pueden tratarse como Categorías o como Valores. Tenga en cuenta que los números no están igualmente espaciados, ni tampoco aparecen en orden numérico.

![todo:image_alt_text](sample.png)

## **Maneje el eje X y el eje de categoría como Microsoft Excel**
Mostraremos estos datos en dos tipos de gráficos: el primero es un gráfico XY ( dispersión) con eje de valores en X y el segundo es un gráfico de línea con eje de categorías en X.

![todo:image_alt_text](compare.png)

## **Código de muestra**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put the sample values used in charts
    worksheet.GetCells().Get(u"A2").PutValue(1);
    worksheet.GetCells().Get(u"A3").PutValue(3);
    worksheet.GetCells().Get(u"A4").PutValue(2.5);
    worksheet.GetCells().Get(u"A5").PutValue(3.5);
    worksheet.GetCells().Get(u"B1").PutValue(u"Cats");
    worksheet.GetCells().Get(u"C1").PutValue(u"Dogs");
    worksheet.GetCells().Get(u"D1").PutValue(u"Fishes");
    worksheet.GetCells().Get(u"B2").PutValue(7);
    worksheet.GetCells().Get(u"B3").PutValue(6);
    worksheet.GetCells().Get(u"B4").PutValue(5);
    worksheet.GetCells().Get(u"B5").PutValue(4);
    worksheet.GetCells().Get(u"C2").PutValue(7);
    worksheet.GetCells().Get(u"C3").PutValue(5);
    worksheet.GetCells().Get(u"C4").PutValue(4);
    worksheet.GetCells().Get(u"C5").PutValue(3);
    worksheet.GetCells().Get(u"D2").PutValue(8);
    worksheet.GetCells().Get(u"D3").PutValue(7);
    worksheet.GetCells().Get(u"D4").PutValue(3);
    worksheet.GetCells().Get(u"D5").PutValue(2);

    // Create Line Chart: X as Category Axis
    int pieIdx = worksheet.GetCharts().Add(ChartType::LineWithDataMarkers, 6, 15, 20, 21);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Add Series
    chart.GetNSeries().Add(u"B2:D5", true);

    // Set the category data
    chart.GetNSeries().SetCategoryData(u"=Sheet1!$A$2:$A$5");

    // Set the first series name
    chart.GetNSeries().Get(0).SetName(u"Cats");

    // Set the second series name
    chart.GetNSeries().Get(1).SetName(u"Dogs");

    // Set the third series name
    chart.GetNSeries().Get(2).SetName(u"Fishes");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Create XY (Scatter) Chart: X as Value Axis
    pieIdx = worksheet.GetCharts().Add(ChartType::ScatterConnectedByLinesWithDataMarker, 6, 6, 20, 12);

    // Retrieve the Chart object
    chart = worksheet.GetCharts().Get(pieIdx);

    // Add Series
    chart.GetNSeries().Add(u"B2:D5", true);

    // Set X values for series
    chart.GetNSeries().Get(0).SetXValues(u"{1,3,2.5,3.5}");
    chart.GetNSeries().Get(1).SetXValues(u"{1,3,2.5,3.5}");
    chart.GetNSeries().Get(2).SetXValues(u"{1,3,2.5,3.5}");

    // Set the first series name
    chart.GetNSeries().Get(0).SetName(u"Cats");

    // Set the second series name
    chart.GetNSeries().Get(1).SetName(u"Dogs");

    // Set the third series name
    chart.GetNSeries().Get(2).SetName(u"Fishes");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"XAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
