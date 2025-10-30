---
title: Diagram till PDF med C++
linktitle: Diagram till PDF
description: Lär dig hur du använder Aspose.Cells for C++ för att konvertera ett diagram till ett PDF dokument. Vår guide visar hur man exporter ett diagram från Microsoft Excel och sparar det som en PDF för vidare distribution och arkivering.
keywords: Aspose.Cells for C++, Diagram till PDF, Microsoft Excel, PDF konvertering, Exportera, Distribution, Arkivering.
type: docs
weight: 47
url: /sv/cpp/chart-to-pdf/
---

## **Rendera diagram till PDF**

För att rendera diagrammet till PDF-format har Aspose.Cells API:er exponerat metoden [**Chart::ToPdf**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/topdf/) med möjlighet att lagra den resulterande PDF-filen på disk eller Stream.

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

## **Skapa diagram-PDF med önskad sidstorlek**
Du kan skapa PDF av diagram med önskad sidstorlek med Aspose.Cells och specificera hur du vill justera diagrammet på sidan, som topp, botten, centrum, vänster, höger etc. Dessutom kan det genererade diagrammet skapas i en ström eller på disk. Se följande exempel som laddar en [provfil i Excel](64716906.xlsx), kommer åt det första diagrammet i arket och konverterar det till [utdata PDF](64716907.pdf) med önskad sidstorlek. Följande skärm visas att sidstorleken i PDF-filen är 7x7 som specificerat i koden, och diagrammet är centrerat både horisontellt och vertikalt.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)

## **Exempelkod**
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
