---
title: Manipulera position, storlek och designers diagram med C++
linktitle: Hantera position, storlek och formgivning av diagram
description: Lär dig hur du använder Aspose.Cells for C++ för att effektivt manipulera position, storlek och designers diagram i Microsoft Excel. Vår guide visar hur du justerar dessa egenskaper för förbättrad layout och visualisering.
keywords: Aspose.Cells for C++, Position, Storlek, Designer Diagram, Microsoft Excel, Layout, Visualisering.
type: docs
weight: 45
url: /sv/cpp/manipulate-position-size-and-designer-chart/
---

## **Diagramposition och storlek**
Ibland vill du ändra positionen eller storleken på det nya eller befintliga diagrammet i arbetsbladet. Aspose.Cells tillhandahåller egenskapen [Chart.GetChartObject()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getchartobject/) för att uppnå detta. Du kan använda dess del-egenskaper för att ändra storlek på diagrammet med nya **höjd** och **bredd** eller flytta det med nya **X** och **Y** koordinater.

### **Kontrollera diagrammets position och storlek**
För att ändra diagrammets position (X, Y-koordinater) eller storlek (höjd, bredd), använd dessa egenskaper:

1. [Chart.GetX()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getx/)
1. [Chart.GetY()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gety/)
1. [Chart.GetHeight()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getheight/)
1. [Chart.GetWidth()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getwidth/)

Följande exempel förklarar användningen av ovanstående API:er, den laddar den befintliga arbetsboken som innehåller ett diagram i dess första kalkylblad. Sedan ändrar det storlek och position för diagrammet med Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"chart.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"chart.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(1);

    // Load the chart from the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Resize the chart
    chart.GetChartObject().SetWidth(400);
    chart.GetChartObject().SetHeight(300);

    // Reposition the chart
    chart.GetChartObject().SetX(250);
    chart.GetChartObject().SetY(150);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Chart resized and repositioned successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Manipulering av Designerdiagram**
Det finns tillfällen då du behöver manipulera eller modifiera diagram i designmallfiler. Aspose.Cells stöder fullständigt manipulation av designmallinnehåll och element. Data, diagraminnehåll, bakgrundsbild och formatering kan bevaras med noggrannhet.

### **Manipulera designmallar i mallfiler för diagram**
För att manipulera designmallar i mallfiler, använd de diagramrelaterade API:erna. Till exempel kan du använda Worksheet.Charts egenskapen för att hämta de befintliga diagrammen i mallfilen.

#### **Skapa ett diagram**
Följande exempel visar hur man skapar ett pyramiddiagram. Senare kommer vi att manipulera detta diagram.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(4);
    worksheet.GetCells().Get(u"B2").PutValue(20);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    int chartIndex = worksheet.GetCharts().Add(ChartType::Pyramid, 5, 0, 15, 5);
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    chart.GetNSeries().Add(u"A1:B3", true);

    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Manipulera diagrammet**
Följande exempel visar hur man manipulerar det befintliga diagrammet. I det här exemplet ändrar vi det skapade diagrammet ovan. I den genererade utmatningen, notera att datumetiketten för en datapunkt har ställts in till 'Storbritannien, 30K'.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"piechart.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Open the existing file
    Workbook workbook(inputFilePath);

    // Get the designer chart in the second sheet
    Worksheet sheet = workbook.GetWorksheets().Get(1);
    Chart chart = sheet.GetCharts().Get(0);

    // Get the data labels in the data series of the third data point
    DataLabels datalabels = chart.GetNSeries().Get(0).GetPoints().Get(2).GetDataLabels();

    // Change the text of the label
    datalabels.SetText(u"Unided Kingdom, 400K ");

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Data label text updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Manipulera ett linjediagram i designmallen**
I det här exemplet kommer vi att manipulera ett linjediagram. Vi kommer att lägga till några data-serier i det befintliga diagrammet och ändra deras linjefärger.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the designer chart in the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Chart chart = worksheet.GetCharts().Get(0);

    // Add the third data series to it
    chart.GetNSeries().Add(U16String(u"{60, 80, 10}"), true);

    // Add another data series (fourth) to it
    chart.GetNSeries().Add(U16String(u"{0.3, 0.7, 1.2}"), true);

    // Plot the fourth data series on the second axis
    chart.GetNSeries().Get(3).SetPlotOnSecondAxis(true);

    // Change the Border color of the second data series
    chart.GetNSeries().Get(1).GetBorder().SetColor(Color::Green());

    // Change the Border color of the third data series
    chart.GetNSeries().Get(2).GetBorder().SetColor(Color::Red());

    // Make the second value axis visible
    chart.GetSecondValueAxis().SetIsVisible(true);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Chart modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
