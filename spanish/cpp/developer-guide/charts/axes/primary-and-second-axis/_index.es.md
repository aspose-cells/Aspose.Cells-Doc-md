---
title: Eje Principal y Secundario con C++
linktitle: Eje Primario y Secundario
description: Aprende cómo entender y trabajar con ejes principales y secundarios en Aspose.Cells for C++. Nuestra guía te ayudará a entender las diferencias entre ejes primarios y secundarios, y cómo configurarlos y usarlos eficazmente en tus gráficos.
keywords: Aspose.Cells for C++, ejes primarios, ejes secundarios, comprensión, diferencias, configuración, uso.
type: docs
weight: 190
url: /es/cpp/primary-and-second-axis/
---

## **Escenarios de uso posibles**
Cuando los números en un gráfico varían ampliamente de serie de datos a serie de datos, o cuando se tienen tipos mixtos de datos (precio y volumen), se traza una o más series de datos en un eje vertical (valor) secundario. La escala del eje vertical secundario muestra los valores de las series de datos asociadas. Un eje secundario funciona bien en un gráfico que muestra una combinación de gráficos de columnas y líneas.

## **Manejar el eje primario y secundario como en Microsoft Excel**
Por favor, vea el siguiente código de ejemplo que crea un nuevo archivo Excel y coloca los valores del gráfico en la primera hoja. 
Luego agregamos un gráfico y mostramos el segundo eje.

![todo:image_alt_text](excel.png)

## **Código de muestra**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put the sample values used in a chart
    worksheet.GetCells().Get(u"A1").PutValue(u"Region");
    worksheet.GetCells().Get(u"A2").PutValue(u"Peking");
    worksheet.GetCells().Get(u"A3").PutValue(u"New York");
    worksheet.GetCells().Get(u"A4").PutValue(u"Paris");
    worksheet.GetCells().Get(u"B1").PutValue(u"Sales Volume");
    worksheet.GetCells().Get(u"C1").PutValue(u"Growth Rate");
    worksheet.GetCells().Get(u"B2").PutValue(100);
    worksheet.GetCells().Get(u"B3").PutValue(80);
    worksheet.GetCells().Get(u"B4").PutValue(140);
    worksheet.GetCells().Get(u"C2").PutValue(0.7);
    worksheet.GetCells().Get(u"C3").PutValue(0.8);
    worksheet.GetCells().Get(u"C4").PutValue(1.0);

    // Create a Scatter chart
    int pieIdx = worksheet.GetCharts().Add(ChartType::Scatter, 6, 6, 15, 11);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Add Series
    chart.GetNSeries().Add(u"B2:C4", true);

    // Set the category data
    chart.GetNSeries().SetCategoryData(u"=Sheet1!$A$2:$A$4");

    // Set the Second-Axis
    chart.GetNSeries().Get(1).SetPlotOnSecondAxis(true);

    // Show the Second-Axis
    chart.GetSecondValueAxis().SetIsVisible(true);

    // Set the second series ChartType to line
    chart.GetNSeries().Get(1).SetType(ChartType::Line);

    // Set the series name
    chart.GetNSeries().Get(0).SetName(u"Sales Volume");
    chart.GetNSeries().Get(1).SetName(u"Growth Rate");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the file
    workbook.Save(u"PrimaryandSecondaryAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
