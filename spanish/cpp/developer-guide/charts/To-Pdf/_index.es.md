---
title: Gráfico a PDF con C++
linktitle: Gráfico a PDF
description: Aprenda cómo usar Aspose.Cells for C++ para convertir un gráfico en un documento PDF. Nuestra guía demostrará cómo exportar un gráfico de Microsoft Excel y guardarlo como PDF para su distribución y archivo.
keywords: Aspose.Cells for C++, Gráfico a PDF, Microsoft Excel, Conversión a PDF, Exportar, Distribución, Archivo.
type: docs
weight: 47
url: /es/cpp/chart-to-pdf/
---

## **Renderizando gráfico a PDF**

Para renderizar el gráfico en formato PDF, las API de Aspose.Cells han expuesto el método [**Chart::ToPdf**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/topdf/) con la capacidad de almacenar el PDF resultante en una ruta de disco o en un Stream.

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

    // Obtain the reference of the newly added worksheet by passing its index to WorksheetCollection
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(4);
    worksheet.GetCells().Get(u"B2").PutValue(20);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Convert chart to PDF
    chart.ToPdf(outDir + u"chartPDF_out.pdf");

    std::cout << "Chart converted to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Crear PDF de gráfico con tamaño de página deseado**
Puedes crear un PDF del gráfico con el tamaño de página deseado usando Aspose.Cells y especificar cómo deseas alinear el gráfico dentro de la página, como arriba, abajo, centro, izquierda, derecha, etc. Además, el gráfico de salida puede crearse en un flujo o en disco. Consulta el siguiente ejemplo de código que carga el archivo de Excel de ejemplo ([sample Excel file](64716906.xlsx)), accede al primer gráfico dentro de la hoja de cálculo y lo convierte en [archivo PDF de salida](64716907.pdf) con el tamaño de página deseado. La siguiente captura muestra que el tamaño de página en el PDF de salida es de 7x7 como se especifica en el código, y el gráfico está centrado tanto horizontal como verticalmente.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)

## **Código de muestra**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load sample Excel file containing the chart
    Workbook wb(srcDir + u"sampleCreateChartPDFWithDesiredPageSize.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart ch = ws.GetCharts().Get(0);

    // Create chart pdf with desired page size
    ch.ToPdf(outDir + u"outputCreateChartPDFWithDesiredPageSize.pdf", 7, 7, PageLayoutAlignmentType::Center, PageLayoutAlignmentType::Center);

    std::cout << "Chart PDF created successfully with desired page size!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
