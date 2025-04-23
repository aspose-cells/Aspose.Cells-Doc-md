---
title: Establecer fuente de datos para el gráfico con C++
linktitle: Origen de datos
type: docs
weight: 10
url: /es/cpp/data-formatting-in-charts/
description: Conoce las diversas fuentes de datos soportadas por Aspose.Cells for C++. Nuestra guía te enseñará los diferentes tipos de fuentes de datos disponibles y cómo conectarte y recuperar datos de ellas para llenar tus hojas de cálculo.
keywords: Aspose.Cells for C++, creación de gráficos, formato de datos, etiquetas, colores, fuentes, apariencia, usabilidad.
---

En nuestros temas anteriores, ya hemos proporcionado muchos ejemplos para demostrar cómo puedes establecer una fuente de datos para tu gráfico. En este tema, proporcionaremos más detalles sobre los tipos de datos que se pueden establecer para un gráfico.

## **Establecer Datos del Gráfico**

Hay dos tipos de datos con los que trabajar al utilizar gráficos con Aspose.Cells como se muestra a continuación:

- Datos del gráfico.
- Datos de categoría.

### **Datos del Gráfico**

Los datos del gráfico son los datos que usamos como fuente de datos para construir nuestros gráficos. Podemos agregar un rango de celdas (que contienen datos del gráfico) llamando al método [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/add/) del objeto [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/).

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Excel object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(170);
    worksheet.GetCells().Get(u"A4").PutValue(300);
    worksheet.GetCells().Get(u"B1").PutValue(160);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(40);

    // Adding sample values to cells as category data
    worksheet.GetCells().Get(u"C1").PutValue(u"Q1");
    worksheet.GetCells().Get(u"C2").PutValue(u"Q2");
    worksheet.GetCells().Get(u"C3").PutValue(u"Y1");
    worksheet.GetCells().Get(u"C4").PutValue(u"Y2");

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Saving the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Datos de Categoría**

Los datos de categoría se utilizan para la etiquetación de los datos del gráfico y se pueden agregar a [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) mediante su propiedad [**GetCategoryData()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/getcategorydata/). A continuación se muestra un ejemplo completo para demostrar el uso de datos del gráfico y de categoría. Después de ejecutar el código de ejemplo anterior, se añadirá un gráfico de columnas a la hoja de cálculo como se muestra a continuación.

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

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(10);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(170);
    worksheet.GetCells().Get(u"A4").PutValue(200);
    worksheet.GetCells().Get(u"B1").PutValue(120);
    worksheet.GetCells().Get(u"B2").PutValue(320);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(40);

    // Add sample values to cells as category data
    worksheet.GetCells().Get(u"C1").PutValue(u"Q1");
    worksheet.GetCells().Get(u"C2").PutValue(u"Q2");
    worksheet.GetCells().Get(u"C3").PutValue(u"Y1");
    worksheet.GetCells().Get(u"C4").PutValue(u"Y2");

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Set the data source for the category data of SeriesCollection
    chart.GetNSeries().SetCategoryData(u"C1:C4");

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Temas Avanzados**
- [Cambiar la fuente de datos del gráfico a la hoja de trabajo de destino al copiar filas o rango](/cells/es/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Crear Gráficos Dinámicos](/cells/es/cpp/create-dynamic-charts/)
- [Forma fácil para la configuración de gráficos utilizando el método Chart.SetChartDataRange](/cells/es/cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Encontrar el tipo de valores X e Y de los puntos en la serie del gráfico](/cells/es/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)
