---
title: Eje de fechas con C++
linktitle: Eje de fecha
description: Aprende cómo gestionar el eje de fechas en Aspose.Cells for C++. Nuestra guía te ayudará a entender cómo trabajar con varios formatos de fecha, escalas de tiempo y frecuencias de etiquetas de marcas de tic.
keywords: Aspose.Cells for C++, eje de fecha, gestionar, formatos de fecha, escalas de tiempo, frecuencias de etiquetas de marcas de tic.
type: docs
weight: 200
url: /es/cpp/date-axis/
---

## **Escenarios de uso posibles**
Cuando creas un gráfico a partir de datos en la hoja que usan fechas, y las fechas se representan en el eje horizontal (categoría) del gráfico, Aspose.Cells automáticamente cambia el eje de categoría a un eje de fecha (escala de tiempo).
Un eje de fecha muestra fechas en orden cronológico a intervalos específicos o unidades base, como el número de días, meses o años, incluso si las fechas en la hoja de cálculo no están en orden secuencial o en las mismas unidades base.
Por defecto, Aspose.Cells determina las unidades base para el eje de fecha según la menor diferencia entre dos fechas en los datos de la hoja de cálculo. Por ejemplo, si tienes datos de precios de acciones donde la menor diferencia entre fechas es de siete días, Aspose.Cells configura la unidad base en días, pero puedes cambiar la unidad base a meses o años si deseas ver el rendimiento de la acción en un período más largo.

## **Manejar el eje de fechas como en Microsoft Excel**
Por favor, vea el siguiente código de ejemplo que crea un nuevo archivo Excel y coloca los valores del gráfico en la primera hoja. 
Luego agregamos un gráfico y establecemos el tipo de [**Axis**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/) 
a [**TimeScale**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/categorytype/) y luego establecemos las unidades base en Días.

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

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add the sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(u"Date");

    // 14 means datetime format
    Style style = worksheet.GetCells().GetStyle();
    style.SetNumber(14);

    // Put values to cells for creating chart
    worksheet.GetCells().Get(u"A2").SetStyle(style);
    worksheet.GetCells().Get(u"A2").PutValue(Date{2022, 6, 26, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"A3").SetStyle(style);
    worksheet.GetCells().Get(u"A3").PutValue(Date{2022, 5, 22, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"A4").SetStyle(style);
    worksheet.GetCells().Get(u"A4").PutValue(Date{2022, 8, 3, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"B1").PutValue(u"Price");
    worksheet.GetCells().Get(u"B2").PutValue(40);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(60);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 9, 6, 21, 13);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.SetChartDataRange(u"A1:B4", true);

    // Set the Axis type to Date time
    chart.GetCategoryAxis().SetCategoryType(CategoryType::TimeScale);

    // Set the base unit for CategoryAxis to days
    chart.GetCategoryAxis().SetBaseUnitScale(TimeUnit::Days);

    // Set the direction for the axis text to be vertical
    chart.GetCategoryAxis().GetTickLabels().SetDirectionType(ChartTextDirectionType::Vertical);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Set max value of Y axis
    chart.GetValueAxis().SetMaxValue(70);

    // Set major unit
    chart.GetValueAxis().SetMajorUnit(10);

    // Save the file
    workbook.Save(u"DateAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
