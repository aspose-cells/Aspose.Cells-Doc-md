---
title: Cómo establecer el eje de categoría con C++
linktitle: Cómo configurar el eje de categoría
description: Aprende cómo configurar el eje de categoría en Aspose.Cells for C++. Nuestra guía te ayudará a entender cómo definir el rango del eje de categoría, ajustar sus propiedades y formatear sus etiquetas.
keywords: Aspose.Cells for C++, eje de categoría, configuración, rango, propiedades, formateo.
type: docs
weight: 205
url: /es/cpp/how-to-set-category-axis/
---

## **Escenarios de uso posibles**
Después de crear un gráfico en una hoja de cálculo, puedes configurar el eje de categorías para él. En este artículo, te mostraremos cómo configurar el eje de categorías para un gráfico de Excel usando Aspose.Cells con código de ejemplo.

## **Los pasos en el código de muestra**

1. Cree un nuevo libro de trabajo.

2. Cree un nuevo gráfico en la primera hoja de cálculo.

3. Agregue algunos valores a las celdas en la primera hoja de cálculo.

4. Ahora puedes establecer el eje de categoría. Hay dos maneras: usando datos de celdas o usando cadenas directamente, ambas mostradas en el código de ejemplo.

5. Establece el eje de valor, guarda el libro para ver el resultado.

## **Código de muestra**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Your local test path
    U16String path = u"";

    // Create a new workbook
    Workbook workbook;
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);
    worksheet.SetName(u"CHART");

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 8, 0, 20, 10);
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add some values to cells
    worksheet.GetCells().Get(u"A1").PutValue(u"Sales");
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"A4").PutValue(130);
    worksheet.GetCells().Get(u"A5").PutValue(160);
    worksheet.GetCells().Get(u"A6").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(u"Days");
    worksheet.GetCells().Get(u"B2").PutValue(1);
    worksheet.GetCells().Get(u"B3").PutValue(2);
    worksheet.GetCells().Get(u"B4").PutValue(3);
    worksheet.GetCells().Get(u"B5").PutValue(4);
    worksheet.GetCells().Get(u"B6").PutValue(5);

    // Some values in string
    U16String Sales = u"100,150,130,160,150";
    U16String Days = u"1,2,3,4,5";

    // Set Category Axis Data with string
    chart.GetNSeries().SetCategoryData(u"{" + Days + u"}");
    // Or you can set Category Axis Data with data in cells, try it!
    // chart.GetNSeries().SetCategoryData(u"B2:B6");

    // Add Series to the chart
    chart.GetNSeries().Add(u"Demand1", true);
    // Set value axis with string 
    chart.GetNSeries().Get(0).SetValues(u"{" + Sales + u"}");
    chart.GetNSeries().Add(u"Demand2", true);
    // Set value axis with data in cells
    chart.GetNSeries().Get(1).SetValues(u"A2:A6");

    // Set some Category Axis properties
    chart.GetCategoryAxis().GetTickLabels().SetRotationAngle(45);
    chart.GetCategoryAxis().GetTickLabels().GetFont().SetSize(8);
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Save the workbook to view the result file
    workbook.Save(path + u"Output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
