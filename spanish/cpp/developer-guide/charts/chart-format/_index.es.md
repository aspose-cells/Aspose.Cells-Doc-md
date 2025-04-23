---
title: Configuración de la apariencia del gráfico con C++
linktitle: Formato del Gráfico
description: Aprenda cómo configurar la apariencia de los gráficos en Aspose.Cells for C++. Nuestra guía mostrará cómo modificar el diseño, colores, fuentes y efectos del gráfico para lograr el estilo visual deseado y mejorar sus hojas de cálculo.
keywords: Aspose.Cells for C++, gráficos, apariencia del gráfico, diseños, colores, fuentes, efectos, hojas de cálculo.
type: docs
weight: 20
url: /es/cpp/setting-chart-appearance/
---

## **Configurar la apariencia del gráfico**
En Cómo crear un gráfico dimos una breve introducción a los tipos de gráficos y objetos de gráficos ofrecidos por Aspose.Cells, y describimos cómo crear uno. Este artículo discute cómo personalizar la apariencia de los gráficos configurando sus propiedades:

- Configurando el área del gráfico.
- Configurando las líneas del gráfico.
- Aplicando temas.
- Configurando títulos para gráficos y ejes.
- Trabajando con líneas de cuadrícula.

### **Configurando el área del gráfico**
Hay diferentes tipos de áreas en un gráfico y Aspose.Cells proporciona la flexibilidad para modificar la apariencia de cada área. Los desarrolladores pueden aplicar diferentes configuraciones de formato en un área cambiando su color de primer plano, color de fondo y formato de relleno, etc.

En el ejemplo dado a continuación, hemos aplicado diferentes configuraciones de formato en diferentes tipos de áreas de un gráfico. Estas áreas incluyen:

- Área de trazado
- Área del gráfico
- Área de la colección de series
- Área de un solo punto en una colección de series

El siguiente fragmento de código demuestra cómo configurar el área del gráfico.

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

    // Create workbook
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

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

### **Configurando las líneas del gráfico**
Los desarrolladores también pueden aplicar diferentes estilos en las líneas o marcadores de datos de la [SeriesCollection](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/). El siguiente fragmento de código demuestra cómo establecer líneas del gráfico usando la API de Aspose.Cells.

```c++
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

    // Create workbook
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

    // Applying a dotted line style on the lines of a SeriesCollection
    chart.GetNSeries().Get(0).GetBorder().SetStyle(LineType::Dot);

    // Applying a triangular marker style on the data markers of a SeriesCollection
    chart.GetNSeries().Get(0).GetMarker().SetMarkerStyle(ChartMarkerType::Triangle);

    // Setting the weight of all lines in a SeriesCollection to medium
    chart.GetNSeries().Get(1).GetBorder().SetWeight(WeightType::MediumLine);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Aplicando temas de Microsoft Excel 2007/2010 a gráficos**
Los desarrolladores pueden aplicar diferentes temas/colores de Microsoft Excel a [SeriesCollection](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) u otros objetos del gráfico, como se muestra en el ejemplo.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xlsx";

    // Instantiate the workbook to open the file that contains a chart
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(1);

    // Get the first chart in the sheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Specify the FillFormat's type to Solid Fill of the first series
    chart.GetNSeries().Get(0).GetArea().GetFillFormat().SetFillType(FillType::Solid);

    // Get the CellsColor of SolidFill
    CellsColor cc = chart.GetNSeries().Get(0).GetArea().GetFillFormat().GetSolidFill().GetCellsColor();

    // Create a theme in Accent style
    cc.SetThemeColor(ThemeColor(ThemeColorType::Accent6, 0.6));

    // Apply the theme to the series
    chart.GetNSeries().Get(0).GetArea().GetFillFormat().GetSolidFill().SetCellsColor(cc);

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Chart theme applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Configuración de los Títulos de Gráficos o Ejes**
Puedes usar Microsoft Excel para establecer los títulos de un gráfico y sus ejes en un entorno WYSIWYG. Aspose.Cells también permite a los desarrolladores establecer los títulos de un gráfico y sus ejes en tiempo de ejecución. Todos los gráficos y sus ejes contienen una propiedad [Title](https://reference.aspose.com/cells/cpp/aspose.cells.charts/title/) que puede usarse para establecer sus títulos, como se muestra en el ejemplo.

El siguiente fragmento de código demuestra cómo establecer títulos en gráficos y ejes.

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

    // Create workbook
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

### **Trabajar con líneas de cuadrícula principales**
Es posible personalizar el aspecto de las líneas de cuadrícula principales. Ocultar o mostrar las líneas de cuadrícula, o definir su color y otras configuraciones. A continuación, mostramos cómo ocultar las líneas de cuadrícula y cómo cambiar su color.

#### **Ocultar líneas de cuadrícula principales**
Los desarrolladores pueden controlar la visibilidad de las líneas principales de la cuadrícula estableciendo la propiedad [IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/line/isvisible/) del objeto [Line](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/line/) a **true** o **false**.

El siguiente fragmento de código demuestra cómo ocultar las líneas de cuadrícula principales. Después de ocultar las líneas de cuadrícula principales, se agregará un gráfico de columnas a la hoja de cálculo sin líneas de cuadrícula.

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

    // Create a workbook object
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

    // Hiding the major gridlines of Category Axis
    chart.GetCategoryAxis().GetMajorGridLines().SetIsVisible(false);

    // Hiding the major gridlines of Value Axis
    chart.GetValueAxis().GetMajorGridLines().SetIsVisible(false);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Cambiando la configuración de las líneas de cuadrícula principales**
Los desarrolladores no solo pueden controlar la visibilidad de las líneas de cuadrícula principales, sino también otras propiedades, incluido su color, etc.

El siguiente fragmento de código demuestra cómo cambiar el color de las líneas de cuadrícula principales. Después de establecer el color de las líneas de cuadrícula principales, se agregará un gráfico de columnas a la hoja de cálculo con líneas de cuadrícula modificadas.

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

    // Create a workbook object
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

    // Setting the color of Category Axis' major gridlines to silver
    chart.GetCategoryAxis().GetMajorGridLines().SetColor(Color::Silver());

    // Setting the color of Value Axis' major gridlines to red
    chart.GetValueAxis().GetMajorGridLines().SetColor(Color::Red());

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Chart created and formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Temas avanzados**
- [Establecer el código de formato de valores de la serie del gráfico](/cells/es/cpp/set-the-values-format-code-of-chart-series/)
- [Establecer una imagen como relleno de fondo en el gráfico](/cells/es/cpp/set-picture-as-background-fill-in-the-chart/)
