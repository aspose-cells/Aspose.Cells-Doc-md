---
title: Gestionar títulos de gráficos de Excel con C++
linktitle: Títulos
description: Aprenda a usar Aspose.Cells for C++ para agregar y dar formato a los títulos de gráficos y ejes en Microsoft Excel. Nuestra guía demostrará cómo configurar diferentes tipos de títulos, ajustar su apariencia y modificar los títulos de los ejes para una mejor representación y claridad de los datos.
keywords: Aspose.Cells for C++, Títulos de gráficos, Títulos de ejes, Microsoft Excel, Representación de datos, Apariencia.
type: docs
weight: 50
url: /es/cpp/chart-and-axis-titles/
---

{{% alert color="primary" %}}

En los gráficos de Excel, hay 2 tipos de títulos:
1. Título del Gráfico 
1. Títulos de Ejes

{{% /alert %}}

## **Opciones de Títulos**
Aspose.Cells también permite gestionar los títulos de los gráficos en tiempo de ejecución. Con el objeto [Title](https://reference.aspose.com/cells/cpp/aspose.cells.charts/title/), puede cambiar el texto, la fuente y el formato de relleno de los títulos.

|![todo:image_alt_text](chart_title.png)|

## **Configuración de los Títulos de Gráficos o Ejes**
Puede usar Microsoft Excel para establecer los títulos de un gráfico y sus ejes en un entorno WYSIWYG. Aspose.Cells también permite a los desarrolladores establecer los títulos de un gráfico y sus ejes en tiempo de ejecución. Todos los gráficos y sus ejes contienen una propiedad [Title](https://reference.aspose.com/cells/cpp/aspose.cells.charts/title/) que puede usarse para establecer sus títulos, como se muestra en el ejemplo a continuación.

El siguiente fragmento de código demuestra cómo establecer títulos para gráficos y ejes.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(60);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Setting the foreground color of the plot area
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::Blue());

    // Setting the foreground color of the chart area
    chart.GetChartArea().GetArea().SetForegroundColor(Color::Yellow());

    // Setting the foreground color of the 1st SeriesCollection area
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color::Red());

    // Setting the foreground color of the area of the 1st SeriesCollection point
    chart.GetNSeries().Get(0).GetPoints().Get(0).GetArea().SetForegroundColor(Color::Cyan());

    // Filling the area of the 2nd SeriesCollection with a gradient
    chart.GetNSeries().Get(1).GetArea().GetFillFormat().SetOneColorGradient(Color::Lime(), 1, GradientStyleType::Horizontal, 1);

    // Setting the title of a chart
    chart.GetTitle().SetText(u"Title");

    // Setting the font color of the chart title to blue
    chart.GetTitle().GetFont().SetColor(Color::Blue());

    // Setting the title of category axis of the chart
    chart.GetCategoryAxis().GetTitle().SetText(u"Category");

    // Setting the title of value axis of the chart
    chart.GetValueAxis().GetTitle().SetText(u"Value");

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Temas avanzados**
- [Leer subtítulo del gráfico desde un archivo ODS](/cells/es/cpp/read-chart-subtitle-from-ods-file/)
