---
title: Uso de Sparklines y Configuración de Formato 3D con C++
linktitle: Usando mini gráficos y configuraciones de formato 3D
type: docs
weight: 40
url: /es/cpp/using-sparklines-and-settings-3d-format/
description: Aprenda cómo usar sparklines y aplicar formato 3D en archivos de Excel usando Aspose.Cells con C++.
---

## **Usando Sparklines**
Microsoft Excel 2010 puede analizar la información de más maneras que nunca. Permite a los usuarios realizar un seguimiento y resaltar tendencias importantes de datos con nuevas herramientas de análisis y visualización de datos. Las sparklines son mini gráficos que se pueden colocar dentro de las celdas para que puedas ver los datos y el gráfico en la misma tabla. Cuando se usan sparklines de manera adecuada, el análisis de datos es más rápido y preciso. También proporcionan una vista simple de la información, evitando hojas de cálculo sobrecargadas con una gran cantidad de gráficos ocupados.

Aspose.Cells proporciona una API para manipular sparklines en hojas de cálculo.
### **Sparklines en Microsoft Excel**
Para insertar sparklines en Microsoft Excel 2010:

1. Selecciona las celdas donde quieres que aparezcan las sparklines. Para que sean fáciles de ver, selecciona las celdas al lado de los datos.
1. Haz clic en **Insertar** en la cinta y luego elige **columna** en el grupo de **Sparklines**.
1. Seleccione o ingrese el rango de celdas en la hoja de cálculo que contenga los datos fuente. Los gráficos aparecerán.

Los mini gráficos le ayudan a ver tendencias, por ejemplo, el registro de victorias o derrotas de una liga de softball. Incluso pueden resumir toda la temporada de cada equipo en la liga.
### **Sparklines usando Aspose.Cells**
Los desarrolladores pueden crear, eliminar o leer sparklines (en el archivo de plantilla) usando la API proporcionada por Aspose.Cells. Las clases que gestionan sparklines se encuentran en el espacio de nombres [Aspose.Cells.Charts](https://reference.aspose.com/cells/cpp/aspose.cells.charts/) por lo que debe importar este espacio antes de usar estas funciones.

Al agregar gráficos personalizados para un determinado rango de datos, los desarrolladores tienen la libertad de agregar diferentes tipos de gráficos pequeños a áreas de celdas seleccionadas.

El siguiente ejemplo demuestra la función de Sparklines. El ejemplo muestra cómo:

1. Abrir un archivo de plantilla simple.
1. Leer la información de sparklines para una hoja de cálculo.
1. Agregar nuevas miniaturas para un rango de datos dado a un área de celdas.
1. Guarde el archivo de Excel en disco.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    Workbook book(inputFilePath);
    Worksheet sheet = book.GetWorksheets().Get(0);

    SparklineGroupCollection sparklineGroups = sheet.GetSparklineGroups();
    for (int i = 0; i < sparklineGroups.GetCount(); ++i)
    {
        SparklineGroup g = sparklineGroups.Get(i);
        std::cout << "sparkline group: type:" << static_cast<int>(g.GetType()) << ", sparkline items count:" << g.GetSparklines().GetCount() << std::endl;
        for (int j = 0; j < g.GetSparklines().GetCount(); ++j)
        {
            Sparkline s = g.GetSparklines().Get(j);
            std::cout << "sparkline: row:" << s.GetRow() << ", col:" << s.GetColumn() << ", dataRange:" << s.GetDataRange().ToUtf8() << std::endl;
        }
    }

    CellArea ca;
    ca.StartColumn = 4;
    ca.EndColumn = 4;
    ca.StartRow = 1;
    ca.EndRow = 7;

    int idx = sheet.GetSparklineGroups().Add(SparklineType::Column, u"Sheet1!B2:D8", false, ca);
    SparklineGroup group = sheet.GetSparklineGroups().Get(idx);

    CellsColor clr = book.CreateCellsColor();
    clr.SetColor(Color::Orange());
    group.SetSeriesColor(clr);

    book.Save(outDir + u"Book1.out.xlsx");
    std::cout << "Sparklines added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Configuración de formato 3D**
Es posible que necesite estilos de gráficos 3D para obtener solo los resultados para su escenario. Aspose.Cells proporciona la API relevante para aplicar el formato 3D de Microsoft Excel 2007.

A continuación se muestra un ejemplo completo para demostrar cómo crear un gráfico y aplicar el formato 3D de Microsoft Excel 2007. Después de ejecutar el código de ejemplo, se agregará un gráfico de columnas (con efectos 3D) a la hoja de cálculo.

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

    // Instantiate a new Workbook
    Workbook book;

    // Add a Data Worksheet
    Worksheet dataSheet = book.GetWorksheets().Add(u"DataSheet");

    // Add Chart Worksheet
    Worksheet sheet = book.GetWorksheets().Add(u"MyChart");

    // Put some values into the cells in the data worksheet
    dataSheet.GetCells().Get(u"B1").PutValue(1);
    dataSheet.GetCells().Get(u"B2").PutValue(2);
    dataSheet.GetCells().Get(u"B3").PutValue(3);
    dataSheet.GetCells().Get(u"A1").PutValue(u"A");
    dataSheet.GetCells().Get(u"A2").PutValue(u"B");
    dataSheet.GetCells().Get(u"A3").PutValue(u"C");

    // Define the Chart Collection
    ChartCollection charts = sheet.GetCharts();

    // Add a Column chart to the Chart Worksheet
    int chartSheetIdx = charts.Add(ChartType::Column, 5, 0, 25, 15);

    // Get the newly added Chart
    Chart chart = book.GetWorksheets().Get(2).GetCharts().Get(0);

    // Set the background/foreground color for PlotArea/ChartArea
    chart.GetPlotArea().GetArea().SetBackgroundColor(Color::White());
    chart.GetChartArea().GetArea().SetBackgroundColor(Color::White());
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::White());
    chart.GetChartArea().GetArea().SetForegroundColor(Color::White());

    // Hide the Legend
    chart.SetShowLegend(false);

    // Add Data Series for the Chart
    chart.GetNSeries().Add(u"DataSheet!B1:B3", true);

    // Specify the Category Data
    chart.GetNSeries().SetCategoryData(u"DataSheet!A1:A3");

    // Get the Data Series
    Series ser = chart.GetNSeries().Get(0);

    // Apply the 3-D formatting
    ShapePropertyCollection spPr = ser.GetShapeProperties();
    Format3D fmt3d = spPr.GetFormat3D();

    // Specify Bevel with its height/width
    Bevel bevel = fmt3d.GetTopBevel();
    bevel.SetType(BevelPresetType::Circle);
    bevel.SetHeight(2);
    bevel.SetWidth(5);

    // Specify Surface material type
    fmt3d.SetSurfaceMaterialType(PresetMaterialType::WarmMatte);

    // Specify surface lighting type
    fmt3d.SetSurfaceLightingType(LightRigType::ThreePoint);

    // Specify lighting angle
    fmt3d.SetLightingAngle(20);

    // Specify Series background/foreground and line color
    ser.GetArea().SetBackgroundColor(Color::Maroon());
    ser.GetArea().SetForegroundColor(Color::Maroon());
    ser.GetBorder().SetColor(Color::Maroon());

    // Save the Excel file
    book.Save(outDir + u"3d_format.out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
