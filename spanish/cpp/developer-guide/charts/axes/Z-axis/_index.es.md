---
title: Eje Z con C++
linktitle: Eje Z
description: Aprende cómo trabajar con el eje Z en Aspose.Cells for C++. Nuestra guía te ayudará a entender cómo configurar y personalizar el eje Z, incluido su escala y etiquetas, para mejorar tus gráficos.
keywords: Aspose.Cells for C++, eje Z, gráficos, configuración, personalización, escala, etiquetas.
type: docs
weight: 210
url: /es/cpp/z-axis/
---

## **Escenarios de uso posibles**
Para algunos gráficos 3D como columnas 3D, cono 3D o pirámide 3D que tienen un eje de profundidad (serie), también conocido como eje Z, que se puede cambiar. Puede especificar el intervalo entre las marcas de graduación, las etiquetas del eje y otras operaciones.

## **Manejar el eje primario y secundario como en Microsoft Excel**
 Por favor, consulta el siguiente código de ejemplo que crea un nuevo archivo de Excel y coloca los valores del gráfico en la primera hoja. Luego agregamos un gráfico y configuramos el tipo de gráfico a Columna3D, así también podrás ver el eje Z, también llamado eje de profundidad. 

![todo:image_alt_text](excel.png)

## **Código de muestra**
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put values to cells for creating chart
    worksheet.GetCells().Get(u"A1").PutValue(u"A");
    worksheet.GetCells().Get(u"B1").PutValue(u"B");
    worksheet.GetCells().Get(u"C1").PutValue(u"C");
    worksheet.GetCells().Get(u"A2").PutValue(2);
    worksheet.GetCells().Get(u"A3").PutValue(1);
    worksheet.GetCells().Get(u"B2").PutValue(2);
    worksheet.GetCells().Get(u"B3").PutValue(3);
    worksheet.GetCells().Get(u"C2").PutValue(2);
    worksheet.GetCells().Get(u"C3").PutValue(3);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column3D, 9, 6, 25, 16);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Calculate the chart
    chart.Calculate();

    // Add SeriesCollection (chart data source) to the chart ranging from "A2" cell to "C3"
    chart.SetChartDataRange(u"A2:C3", true);

    // Hide the CategoryAxis axis
    chart.GetCategoryAxis().SetIsVisible(false);

    // Hide the ValueAxis axis
    chart.GetValueAxis().SetIsVisible(false);

    // Save the file
    workbook.Save(u"ZAxis.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
