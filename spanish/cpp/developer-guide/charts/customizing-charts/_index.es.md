---
title: Personalización de gráficos con C++
linktitle: Personalización de gráficos
description: Aprende cómo personalizar gráficos en Aspose.Cells for C++. Nuestra guía te mostrará cómo modificar diseños de gráficos, agregar y dar formato a series de datos, ajustar ejes y aplicar varias opciones de formato para mejorar la apariencia y usabilidad de tus gráficos.
keywords: Aspose.Cells for C++, creación de gráficos, personalización, diseños, series de datos, ejes, formato, apariencia, usabilidad.
type: docs
weight: 40
url: /es/cpp/customizing-charts/
---

{{% alert color="primary" %}}

## **Creación de gráficos personalizados**

Hasta ahora, cuando hemos hablado de gráficos, hemos visto gráficos estándar que tienen su configuración de formato estándar. Solo definimos la fuente de datos, establecemos algunas propiedades y el gráfico se crea con sus configuraciones de formato predeterminadas. Pero las APIs de Aspose.Cells también soportan crear gráficos personalizados que permiten a los desarrolladores crear gráficos con sus propias configuraciones de formato.

Los desarrolladores pueden crear gráficos personalizados en tiempo de ejecución utilizando Aspose.Cells.

Un gráfico está compuesto por una serie de datos. Cada serie de datos en Aspose.Cells está representada por un objeto [**Series**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/), mientras que un objeto [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) sirve como una colección de objetos [**Series**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/). Al crear un gráfico personalizado, los desarrolladores tienen la libertad de usar diferentes tipos de gráficos para diferentes series de datos (recopilados en el objeto [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)).

El código de ejemplo a continuación demuestra cómo crear gráficos personalizados. En este ejemplo, vamos a usar un gráfico de columnas para la primera serie de datos y un gráfico de líneas para la segunda serie. El resultado es que agregamos un gráfico de columnas, combinado con un gráfico de líneas, a la hoja de cálculo.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"A4").PutValue(110);
    worksheet.GetCells().Get(u"B1").PutValue(260);
    worksheet.GetCells().Get(u"B2").PutValue(12);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(100);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Set the chart type of 2nd NSeries to display as line chart
    chart.GetNSeries().Get(1).SetType(ChartType::Line);

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Actualmente, Aspose.Cells solo soporta gráficos personalizados que combinan gráficos de pastel, línea, columna y apilados, pero en futuras versiones se soportarán más gráficos.

{{% /alert %}}
